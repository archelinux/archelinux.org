import io
import sys
import tarfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError

from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from release_metadata import installation_files, stable_iso, verification_files
from sync_metadata import parse_database, release_catalog, rolling_catalog


def release(tag, names, *, prerelease=False, draft=False, date="2026-12-10"):
    names = [*names, "SHA256SUMS", "SHA256SUMS.sig", "release.asc"]
    return {
        "name": tag, "tag_name": tag, "draft": draft, "prerelease": prerelease,
        "published_at": date + "T00:00:00Z", "body": "Published notes",
        "assets": [{"name": n, "browser_download_url": "https://example.com/" + n,
                    "size": 32, "state": "uploaded"} for n in names],
    }


class ReleaseTests(unittest.TestCase):
    def test_stable_download_skips_package_only_and_prerelease(self):
        rows = [
            release("pkgs-123", ["arche.db"]),
            release("preview", ["test.iso"], prerelease=True),
            release("v2.9-rc1", ["test.iso"]),
            release("draft", ["draft.iso"], draft=True),
            release("rolling-20261201", ["disk.iso"], date="2026-12-01"),
        ]
        catalog = release_catalog(rows, [])
        self.assertEqual(len(catalog), 3)
        self.assertEqual(stable_iso(catalog)["tag"], "rolling-20261201")

    def test_download_template_handles_both_part_numbering_conventions(self):
        env = Environment(loader=FileSystemLoader(ROOT / "templates"))
        for names in (["disk.iso"], ["disk.iso.part01", "disk.iso.part00"],
                      ["disk.iso.part02", "disk.iso.part01"]):
            assets = names + ["disk.iso.sha256", "public.asc", "disk.iso.sig", "irrelevant.txt"]
            selected = stable_iso(release_catalog([release("test-tag", assets)], []))
            parts = installation_files(selected["assets"])
            self.assertEqual([a["name"] for a in parts], sorted(names))
            page = env.get_template("download.html").render(
                section="Download", path="download/index.html", root="../", latest=selected,
                media=parts, media_size=64, groups={}, packages=[], articles={},
                verification=verification_files(selected["assets"], parts))
            for n in assets[:-1]:
                self.assertIn(f'href="https://example.com/{n}"', page)
            self.assertNotIn("irrelevant.txt", page)
            self.assertEqual("Download every part" in page, len(parts) > 1)

    def test_rejects_incomplete_or_mixed_iso(self):
        for names in (["a.iso.part00", "a.iso.part02"], ["a.iso", "a.iso.part00"],
                      ["a.iso", "b.iso"]):
            with self.assertRaises(ValueError):
                release_catalog([release("v3", names)], [])

    def test_incomplete_stable_upload_is_rejected(self):
        item = release("stable", ["disk.iso"])
        item["assets"] = item["assets"][:1]
        with self.assertRaisesRegex(ValueError, "signed checksum"):
            release_catalog([item], [])

    def test_editorial_summary_preserved(self):
        previous = [{"tag": "v3", "title": "A new release", "summary": "Editor's summary"}]
        row, = release_catalog([release("v3", ["disk.iso"])], previous)
        self.assertEqual(row["summary"], "Editor's summary")
        self.assertEqual(row["notes"], "Published notes")

    def test_stable_must_exist(self):
        with self.assertRaisesRegex(ValueError, "No stable ISO"):
            release_catalog([release("pkgs", ["arche.db"])], [])


class DatabaseTests(unittest.TestCase):
    def test_uses_built_desc_and_handles_split_packages(self):
        data = io.BytesIO()
        with tarfile.open(fileobj=data, mode="w:gz") as tar:
            desc = b"%NAME%\narche-example\n\n%BASE%\narche-suite\n\n%VERSION%\n2:1.2-3\n\n%ARCH%\nany\n\n%DESC%\nExample\n\n%LICENSE%\nMIT\n\n%DEPENDS%\nfoo>=2\nbar\n\n"
            info = tarfile.TarInfo("arche-example-1.2-3/desc")
            info.size = len(desc)
            tar.addfile(info, io.BytesIO(desc))
        row, = parse_database(data.getvalue())
        self.assertEqual((row["name"], row["base"], row["version"], row["depends"]),
                         ("arche-example", "arche-suite", "2:1.2-3", ["foo>=2", "bar"]))

    def test_missing_channel_only_allowed_for_bootstrap(self):
        missing = HTTPError("https://example.test", 404, "missing", {}, None)
        with patch("sync_metadata.fetch", side_effect=missing):
            previous = {"source": {"kind": "iso"}}
            self.assertEqual(rolling_catalog(previous), previous)
            with self.assertRaises(HTTPError):
                rolling_catalog({"source": {"kind": "rolling"}})
