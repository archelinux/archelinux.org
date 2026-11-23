"""Render the complete static site from the release snapshot in content/."""
import json
import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
env = Environment(loader=FileSystemLoader(ROOT / "templates"),
                  autoescape=select_autoescape(["html"]))
env.tests["match_iso"] = lambda name: name.endswith(".iso")
md = MarkdownIt("commonmark", {"html": False}).enable("table")
packages = json.loads((CONTENT / "packages.json").read_text())
releases = json.loads((CONTENT / "releases.json").read_text())
latest = releases[0]
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
        articles=articles, packages=packages, releases=releases, latest=latest, **context)
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
    body = (CONTENT / "news" / (tag + ".md")).read_text()
    render(f"news/{tag}.html", "release", release["title"], "News", release=release,
           body=md.render(body))
render("download/index.html", "download", "Download archelinux", "Download")
render("community/index.html", "community", "Community forum", "Forum")
render("issues/index.html", "issues", "Report an issue", "Support")
render("docs/index.html", "docs", "Documentation", "Wiki")
