"""Render the complete static site from the release snapshot in content/."""
import json
import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt

from release_metadata import installation_files, stable_iso, verification_files

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                  autoescape=select_autoescape(["html"]))
md = MarkdownIt("commonmark", {"html": False}).enable("table")
catalog = json.loads((CONTENT / "packages.json").read_text())
packages = catalog["packages"]
releases = json.loads((CONTENT / "releases.json").read_text())
latest = stable_iso(releases)
groups = {
    "Getting started": ["about", "verify", "installation", "shortcuts", "hardware"],
    "Your workspace": ["desktop", "shell", "configuration", "recovery", "maintenance"],
    "Building archelinux": ["system", "installer-internals", "build", "publication", "acceptance", "qemu"],
}
articles = {}
for path in sorted((CONTENT / "wiki").glob("*.md")):
    title, body = path.read_text().split("\n", 1)
    articles[path.stem] = {"title": title.removeprefix("# "), "body": md.render(body)}

def render(path, template, title, section, **context):
    page = ROOT / path
    page.parent.mkdir(exist_ok=True)
    prefix = os.path.relpath(ROOT, page.parent) + "/"
    html = env.get_template(template + ".html").render(
        root=prefix, path=path, section=section, title=title, groups=groups,
        articles=articles, packages=packages, package_source=catalog["source"],
        releases=releases, latest=latest, **context)
    page.write_text(html + "\n")

render("index.html", "home", "Home", "Home")
render("wiki/index.html", "wiki", "Documentation", "Wiki")
for slug, article in articles.items():
    render(f"wiki/{slug}.html", "article", article["title"], "Wiki", body=article["body"])
render("packages/index.html", "packages", "Package directory", "Packages")
for package in packages:
    render(f'packages/{package["name"]}.html', "package", package["name"], "Packages",
           package=package, package_names={p["name"] for p in packages})
render("news/index.html", "news", "Release archive", "News")
for release in releases:
    tag = release["tag"]
    editorial = CONTENT / "news" / (tag + ".md")
    body = editorial.read_text() if editorial.exists() else release["notes"]
    render(f"news/{tag}.html", "release", release["title"], "News", release=release,
           body=md.render(body))
media = installation_files(latest["assets"])
render("download/index.html", "download", "Download archelinux", "Download", media=media,
       media_size=sum(a["size"] for a in media), verification=verification_files(latest["assets"], media))

# Both directories consist entirely of generated catalog pages.
for directory, slugs in (("packages", [p["name"] for p in packages]),
                         ("news", [r["tag"] for r in releases])):
    expected = {"index", *slugs}
    for old_page in (ROOT / directory).glob("*.html"):
        if old_page.stem not in expected:
            old_page.unlink()
