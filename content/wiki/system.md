# System architecture

An Arch-based system for Neovim, tmux, and local agent workflows. TTY1 starts Sway on normal user login, with a titlebar-free Litho Dark desktop with a one-pixel focus outline and a subtle Arche logo over dark violet gradients. TTY2–6 remain console recovery sessions. The new installer provisions Zsh with Oh My Zsh. Local model services are opt-in.


The following layout and mount settings describe the earlier unattended installer. See [guided installer internals](installer-internals.html) for the current USB installer.

- **Storage:** XFS with reflink and CRC enabled, 512-byte inodes, 16 allocation groups. Root mounts with `rw,noatime,nodiratime,logbufs=8,logbsize=256k,allocsize=64M` and fstab dump/fsck fields `0 0`.
- **Kernels:** Arch's `linux-zen` and matching headers, plus `linux-lts` and headers. Zen is the permitted performance-kernel fallback; no CachyOS repository is required. LTS provides a recovery boot choice, not a security-hardening guarantee.
- **Boot:** systemd-boot on UEFI (provided by `systemd`), GRUB on BIOS; Zen default, explicit LTS entry, two-second timeout. Both kernels also boot the live image.
- **Memory:** RAM-sized zstd ZRAM at priority 100; the requested VM, dirty-page and inotify tuning lives in `airootfs/etc/sysctl.d/99-arche-perf.conf`.
- **Recovery:** weekly `paccache.timer` and a transaction hook retain three cached versions. `arche-rollback PACKAGE` selects the newest cached version older than the installed version using pacman's metadata and version ordering. It rejects prefix matches and missing history. This is package recovery, not a filesystem backup; related libraries may need coordinated downgrades. Only versions actually downloaded remain available.
