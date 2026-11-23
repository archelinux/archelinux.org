"""Validate relative page, asset, anchor and form links in the deployment tree."""
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids = set()
        self.refs = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        fields = dict(attrs)
        if fields.get("id"):
            self.ids.add(fields["id"])
        for key in ("href", "src", "action"):
            if fields.get(key):
                self.refs.append(fields[key])


def check(root):
    pages = {p: Page(p) for p in root.rglob("*.html")
             if p.relative_to(root).parts[0] not in {"templates", ".git"}
             and not any(part.startswith(".") for part in p.relative_to(root).parts)}
    errors = []
    for path, page in pages.items():
        for value in page.refs:
            uri = urlsplit(value)
            if uri.netloc or uri.scheme:
                continue
            target = path if not uri.path else (path.parent / unquote(uri.path)).resolve()
            if target.is_dir():
                target /= "index.html"
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f"{path.relative_to(root)}: missing local target {value}")
            elif uri.fragment and target in pages and unquote(uri.fragment) not in pages[target].ids:
                errors.append(f"{path.relative_to(root)}: missing anchor {value}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated local links in {len(pages)} pages")


if __name__ == "__main__":
    check(Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else ROOT)
