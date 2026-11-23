# archelinux.org

Static distribution portal inspired by [archlinux.org](https://archlinux.org/). Serve the repository root. All navigation uses relative links and works from a subdirectory.

## Editing the site

Edit the hand-written wiki in `content/wiki/` and release notes in `content/news/`. To change an existing editorial title or summary, edit the corresponding entry in `content/releases.json`. New ISO release pages use the published release body unless a local Markdown article overrides it.

Install Python 3, GnuPG and the dependencies in `requirements.txt`. For a release refresh, run:

    python3 scripts/sync_metadata.py
    python3 scripts/build.py
    python3 scripts/check_site.py

The refresh reads the distro's published releases and preserves editorial titles and summaries. The Download page follows the newest stable ISO, including split images. Prereleases and package-only publications do not replace it. Set `GH_TOKEN` to a read-only GitHub token in CI for a higher API rate limit.

Package versions, dependencies and licenses come from the promoted pacman database on the distro's `rolling-channel` branch. The synchronizer fetches the database and its signature at the same commit, then verifies them using the release key shipped in `assets/`. Until the channel is first published, the existing 2.0.0 catalog is labeled as an ISO snapshot. Missing or invalid signed data on an established channel fails the refresh.

For local development, skip the refresh to rebuild from the checked-in snapshot. Run `python3 -m unittest discover -s tests` to check release selection and package metadata parsing. Commit rendered HTML with edits to its sources. The CNAME declares archelinux.org.

The symbol and SwayFX screenshots come from [archelinux](https://github.com/archelinux/archelinux). The project created the [Graphite wallpaper](assets/graphite.svg) and released it under [0BSD](assets/LICENSE.graphite).
