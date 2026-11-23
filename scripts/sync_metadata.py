"""Refresh release assets and the package directory from public, immutable inputs."""
import io
import json
import os
import re
import subprocess
import tarfile
import tempfile
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

from release_metadata import installation_files, stable_iso

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SLUG = "archelinux/archelinux"
API = f"https://api.github.com/repos/{SLUG}"
SAFE_TAG = re.compile(r"[a-zA-Z0-9_-][a-zA-Z0-9._-]*")
PACKAGE_NAME = re.compile(r"[a-z0-9@_+][a-z0-9@._+-]*")


def fetch(url):
    headers = {"User-Agent": "archelinux-website"}
    if url.startswith(API + "/") and os.getenv("GH_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GH_TOKEN"]
    with urlopen(Request(url, headers=headers), timeout=30) as response:
        return response.read()


def published_releases():
    releases = []
    page = 1
    while True:
        batch = json.loads(fetch(f"{API}/releases?per_page=100&page={page}"))
        releases.extend(batch)
        if len(batch) < 100:
            return releases
        page += 1


def release_catalog(published, existing):
    curated = {r["tag"]: r for r in existing}
    releases = []
    for item in published:
        if item["draft"]:
            continue
        tag = item["tag_name"]
        assets = [
            {"name": a["name"], "url": a["browser_download_url"], "size": a["size"]}
            for a in item["assets"] if a["state"] == "uploaded"
        ]
        if not installation_files(assets):
            continue  # The separately promoted package channel has its own catalog.
        if not SAFE_TAG.fullmatch(tag) or tag == "index":
            raise ValueError(f"Unsupported ISO release tag: {tag!r}")
        for asset in assets:
            if urlsplit(asset["url"]).scheme != "https" or asset["size"] <= 0:
                raise ValueError(f"Invalid release asset in {tag}: {asset['name']}")
        old = curated.get(tag, {})
        # One historical RC was published without GitHub's prerelease flag.
        candidate = item["prerelease"] or re.search(r"(?:^|[.-])(?:rc|alpha|beta|pre)\d*(?:$|[.-])", tag, re.I)
        release = {
            "tag": tag, "title": old.get("title") or item["name"] or tag,
            "date": item["published_at"][:10], "published_at": item["published_at"],
            "channel": "preview" if candidate else "stable", "assets": assets,
        }
        if old.get("summary"):
            release["summary"] = old["summary"]
        if not (CONTENT / "news" / f"{tag}.md").exists():
            release["notes"] = item.get("body") or ""
        releases.append(release)
    releases.sort(key=lambda r: (r["published_at"], r["tag"]), reverse=True)
    latest = stable_iso(releases)
    media = installation_files(latest["assets"])
    iso = media[0]["name"].split(".iso", 1)[0] + ".iso"
    names = {a["name"] for a in latest["assets"]}
    checksums = {iso + ".sha256", "SHA256SUMS", "sha256sums.txt"}
    if not any(c in names and c + ".sig" in names for c in checksums):
        raise ValueError(f"Stable ISO {iso} lacks a signed checksum file")
    if not any(name.endswith(".asc") for name in names):
        raise ValueError(f"Stable ISO {iso} lacks its release public key")
    return releases


def parse_database(data):
    packages = {}
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:*") as archive:
        for member in archive:
            if not member.isfile() or not member.name.endswith("/desc"):
                continue
            desc = archive.extractfile(member).read().decode("utf-8").strip()
            fields = {}
            for block in desc.split("\n\n"):
                key, _, value = block.partition("\n")
                fields[key.strip("%")] = value.splitlines()
            name = fields["NAME"][0]
            if not PACKAGE_NAME.fullmatch(name) or name in packages or name == "index":
                raise ValueError(f"Invalid or duplicate package name: {name!r}")
            filename = fields["FILENAME"][0]
            digest = fields["SHA256SUM"][0]
            if not re.fullmatch(r"[a-zA-Z0-9@_+.:-]+\.pkg\.tar\.zst", filename) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise ValueError(f"Invalid archive metadata for {name}")
            packages[name] = {
                "filename": filename, "sha256": digest,
                "name": name, "base": fields.get("BASE", [name])[0],
                "description": fields["DESC"][0], "version": fields["VERSION"][0],
                "arch": fields["ARCH"][0], "license": " / ".join(fields.get("LICENSE", [])),
                "depends": fields.get("DEPENDS", []),
            }
    if not packages:
        raise ValueError("No packages found in promoted database")
    return [packages[name] for name in sorted(packages)]


def verified_database(database, signature):
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        keyring = work / "release.gpg"
        subprocess.run(["gpg", "--homedir", temp, "--batch", "--dearmor", "--output", str(keyring),
                        str(ROOT / "assets/archelinux-release-public.asc")], check=True)
        (work / "arche.db").write_bytes(database)
        (work / "arche.db.sig").write_bytes(signature)
        subprocess.run(["gpgv", "--homedir", temp, "--keyring", str(keyring),
                        "arche.db.sig", "arche.db"], cwd=work, check=True)
    return parse_database(database)


def rolling_catalog(previous):
    try:
        sha = json.loads(fetch(f"{API}/git/ref/heads/rolling-channel"))["object"]["sha"]
    except HTTPError as exc:
        if exc.code == 404 and previous["source"]["kind"] == "iso":
            # The 2.0.0 recipe snapshot remains explicitly labeled during bootstrap.
            return previous
        raise
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise ValueError("Invalid rolling channel commit")
    endpoint = f"https://raw.githubusercontent.com/{SLUG}/{sha}/stable/arche.db"
    packages = verified_database(fetch(endpoint), fetch(endpoint + ".sig"))
    return {"source": {"kind": "rolling", "revision": sha}, "packages": packages}


def save(name, obj):
    path = CONTENT / name
    text = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    if path.read_text() != text:
        with tempfile.NamedTemporaryFile(mode="w", dir=CONTENT, delete=False) as tmp:
            tmp.write(text)
        os.chmod(tmp.name, 0o644)
        os.replace(tmp.name, path)


def main():
    existing = json.loads((CONTENT / "releases.json").read_text())
    releases = release_catalog(published_releases(), existing)
    packages = rolling_catalog(json.loads((CONTENT / "packages.json").read_text()))
    save("releases.json", releases)
    save("packages.json", packages)
    print(f'{len(releases)} ISO releases, latest stable {stable_iso(releases)["tag"]}; '
          f'{len(packages["packages"])} packages from {packages["source"]["revision"]}')


if __name__ == "__main__":
    main()
