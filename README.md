# archelinux.org

Static distribution portal inspired by [archlinux.org](https://archlinux.org/). Serve the repository root. All navigation uses relative links and works from a subdirectory.

## Editing the site

Edit articles in `content/wiki/`, news in `content/news/`, release assets in `content/releases.json`, and package metadata in `content/packages.json`. The initial snapshot uses archelinux v2.0.0 (a48dc3098), its PKGBUILDs, and the project's six published releases through 23 November 2026. Historical release notes describe their original images.

Shared layouts live in `templates/`. Rebuild with Python 3, Jinja2 and markdown-it-py installed:

    python3 scripts/build.py

Commit the rendered HTML with its sources. No build step or application server is needed on the host. The CNAME declares archelinux.org. DNS and hosting are configured separately.

The symbol and screenshots come from [archelinux](https://github.com/archelinux/archelinux). The desktop features the [Twin Blades wallpaper](https://github.com/dharmx/walls/blob/e8d8a42e4fbecb2cf9619995edbc7ce19610bbd8/anime/aeb9uhrbr41a1.webp).
