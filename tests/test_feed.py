import sys
from pathlib import Path
import tempfile
import unittest
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from release_feed import write_feed


class ReleaseFeedTest(unittest.TestCase):
    def test_reader_gets_dates_links_and_unescaped_title(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "feed.xml"
            release = {"tag": "v1", "published_at": "2026-11-23T12:00:00Z", "title": "Arch & tools"}
            write_feed(path, [release])
            root = ElementTree.parse(path).getroot()
            self.assertEqual(root.findtext("{*}updated"), release["published_at"])
            entry = root.find("{*}entry")
            self.assertEqual(entry.findtext("{*}title"), release["title"])
            self.assertTrue(entry.find("{*}link").get("href").endswith("/news/v1.html"))
