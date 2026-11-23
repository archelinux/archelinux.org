# Package repository mirrors

The signed stable repository contains the archelinux packages used for rolling updates. Arch dependencies come from your Arch mirror list. Both archelinux endpoints below use GitHub infrastructure.

| Package endpoint | What it serves |
| --- | --- |
| `https://raw.githubusercontent.com/archelinux/archelinux/rolling-channel/stable` | Primary. Updated when a tested package snapshot is promoted. |
| `https://archelinux.github.io/archelinux.org/mirror/stable` | Secondary. The website verifies the signed database, file index, helper and package signatures before deploying the snapshot. Refreshes every six hours and on website deployment. The mirror can lag the primary between refreshes. |

On an existing archelinux installation, follow [Rolling updates](rolling-updates.html) to trust the release key and configure the signed repository. To use the secondary endpoint as a fallback, append the following line under the existing `Server` in the **same** `[arche]` section of `/etc/pacman.conf`. Preserve the section’s signature requirements.

    Server = https://archelinux.github.io/archelinux.org/mirror/stable

Run `pacman-conf --repo arche Server` to inspect the configured order. See the [latest website builds](https://github.com/archelinux/archelinux.org/actions/workflows/pages.yml) for mirror verification and publication results.
