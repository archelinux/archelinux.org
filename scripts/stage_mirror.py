"""Stage a verified package mirror at the exact commit used for the website catalog."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from sync_metadata import CONTENT, ROOT, parse_database

REPOSITORY = "https://github.com/archelinux/archelinux.git"


def stage(source, dest, revision, keyring):
    sha = subprocess.check_output(["git", "-C", source, "rev-parse", "HEAD"], text=True).strip()
    if sha != revision:
        raise ValueError("Mirror and catalog revisions differ")
    stable = source / "stable"
    allowed = {"arche.db", "arche.files", "arche-enable-rolling"}
    public = {}
    for path in stable.iterdir():
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Unexpected mirror entry: {path.name}")
        if path.name.endswith(".sig") or path.name == "archelinux-release.asc":
            continue
        if path.name not in allowed and not re.fullmatch(r"[a-zA-Z0-9@.+_:-]+(?:-[a-zA-Z0-9@.+_:-]+)+\.pkg\.tar\.zst", path.name):
            raise ValueError(f"Unexpected mirror payload: {path.name}")
        subprocess.run(["gpgv", "--homedir", keyring.parent, "--keyring", keyring, str(path) + ".sig", path], check=True)
        public[path.name] = path
    if not allowed <= public.keys():
        raise ValueError("Incomplete repository metadata")
    for entry in parse_database(public["arche.db"].read_bytes()):
        path = public[entry["filename"]]
        with path.open("rb") as stream:
            if hashlib.file_digest(stream, "sha256").hexdigest() != entry["sha256"]:
                raise ValueError(f"Package does not match signed index: {path.name}")
    dest.mkdir(parents=True)
    for path in public.values():
        shutil.copyfile(path, dest / path.name)
        shutil.copyfile(str(path) + ".sig", dest / (path.name + ".sig"))
    shutil.copyfile(ROOT / "assets/archelinux-release-public.asc", dest / "archelinux-release.asc")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dest", type=Path)
    args = parser.parse_args()
    source = json.loads((CONTENT / "packages.json").read_text())["source"]
    if source["kind"] != "rolling" or not re.fullmatch(r"[0-9a-f]{40}", source["revision"]):
        raise ValueError("A verified rolling catalog is required")
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        repo = tmp / "channel"
        subprocess.run(["git", "init", "-q", repo], check=True)
        subprocess.run(["git", "-C", repo, "fetch", "--depth=1", REPOSITORY, source["revision"]], check=True)
        subprocess.run(["git", "-C", repo, "checkout", "-q", "--detach", "FETCH_HEAD"], check=True)
        keyring = tmp / "release.gpg"
        subprocess.run(["gpg", "--homedir", tmp, "--batch", "--dearmor", "-o", keyring,
                        ROOT / "assets/archelinux-release-public.asc"], check=True)
        stage(repo, args.dest, source["revision"], keyring)
