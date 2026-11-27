# archelinux.org

The [archelinux website](https://archelinux.github.io/archelinux.org/) is hosted on GitHub Pages. The static portal is inspired by [archlinux.org](https://archlinux.org/). Serve the repository root for local development. All navigation uses relative links and works from a subdirectory.

## Editing the site

Edit the hand-written wiki in `content/wiki/` and release notes in `content/news/`. To change an existing editorial title or summary, edit the corresponding entry in `content/releases.json`. New ISO release pages use the published release body unless a local Markdown article overrides it.

Install Python 3, GnuPG and the dependencies in `requirements.txt`. For a release refresh, run:

    python3 scripts/sync_metadata.py
    python3 scripts/build.py
    python3 scripts/check_site.py

The refresh reads the distro's published releases and preserves editorial titles and summaries. The Download page follows the newest stable ISO, including split images. Prereleases and package-only publications do not replace it. Set `GH_TOKEN` to a read-only GitHub token in CI for a higher API rate limit.

Package versions, dependencies and licenses come from the promoted pacman database on the distro's `rolling-channel` branch. The synchronizer fetches the database and its signature at the same commit, then verifies them using the release key shipped in `assets/`. Until the channel is first published, the existing 2.0.0 catalog is labeled as an ISO snapshot. Missing or invalid signed data on an established channel fails the refresh.

For local development, skip the refresh to rebuild from the checked-in snapshot. Run `python3 -m unittest discover -s tests` to check release selection and package metadata parsing. Commit rendered HTML with edits to its sources.

The symbol and screenshots come from [archelinux](https://github.com/archelinux/archelinux). The desktop features the [Twin Blades wallpaper](https://github.com/dharmx/walls/blob/e8d8a42e4fbecb2cf9619995edbc7ce19610bbd8/anime/aeb9uhrbr41a1.webp).

The release archive publishes Atom at `news/feed.xml`. During the Pages deployment, `scripts/stage_mirror.py public/mirror/stable` fetches the exact rolling commit recorded in the verified package catalog. It verifies detached signatures and archive hashes before copying packages into the Pages artifact. Primary and secondary endpoints are documented in `wiki/mirrors.html`. The repository contains the generator and rendered pages. The mirror files are deployed as build artifacts.
