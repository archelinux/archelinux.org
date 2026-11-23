"""Publish the release archive as Atom for feed readers."""
from xml.etree import ElementTree as ET

SITE = "https://archelinux.github.io/archelinux.org/"


def write_feed(path, releases):
    feed = ET.Element("feed", xmlns="http://www.w3.org/2005/Atom")
    ET.SubElement(feed, "id").text = SITE + "news/"
    ET.SubElement(feed, "title").text = "archelinux releases"
    ET.SubElement(feed, "updated").text = max(r["published_at"] for r in releases)
    ET.SubElement(ET.SubElement(feed, "author"), "name").text = "archelinux"
    ET.SubElement(feed, "link", rel="self", href=SITE + "news/feed.xml")
    ET.SubElement(feed, "link", href=SITE + "news/")
    for release in releases:
        entry = ET.SubElement(feed, "entry")
        url = SITE + "news/" + release["tag"] + ".html"
        for field, value in (("id", url), ("title", release["title"]), ("updated", release["published_at"]),
                             ("summary", release.get("summary") or release["title"])):
            ET.SubElement(entry, field).text = value
        ET.SubElement(entry, "link", href=url)
    ET.indent(feed)
    ET.ElementTree(feed).write(path, encoding="utf-8", xml_declaration=True)
