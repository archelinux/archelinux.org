"""Select installation media independently of package-channel promotions."""
import re

PART = re.compile(r"(.+\.iso)\.part(\d{2})$")


def installation_files(assets):
    complete = [a for a in assets if a["name"].endswith(".iso")]
    parts = sorted((a for a in assets if PART.fullmatch(a["name"])), key=lambda a: a["name"])
    if complete:
        if len(complete) != 1 or parts:
            raise ValueError("Expected a single ISO or a single series of ISO parts")
        return complete
    if parts:
        matches = [PART.fullmatch(a["name"]) for a in parts]
        numbers = [int(m[2]) for m in matches]
        if (len(parts) < 2 or len({m[1] for m in matches}) != 1 or numbers[0] not in (0, 1)
                or numbers != list(range(numbers[0], numbers[0] + len(parts)))):
            raise ValueError("Incomplete or mixed ISO part series")
    return parts


def verification_files(assets, media):
    iso_name = media[0]["name"].split(".iso", 1)[0] + ".iso"
    checks = {iso_name + extension for extension in (".sha256", ".sha256.sig", ".sig")}
    legacy = {"sha256sums", "sha256sums.sig", "sha256sums.txt", "sha256sums.txt.sig"}
    return [a for a in assets if a["name"] in checks or a["name"].lower() in legacy
            or a["name"].endswith(".asc")]


def stable_iso(releases):
    candidates = (r for r in releases if r["channel"] == "stable" and installation_files(r["assets"]))
    chosen = max(candidates, key=lambda r: r["published_at"], default=None)
    if chosen is None:
        raise ValueError("No stable ISO release to publish")
    return chosen
