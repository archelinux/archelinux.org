# System architecture

archelinux builds on Arch user space and packages its installer, shell and workspace defaults separately. For the current [guided installer internals](installer-internals.html), see how the live image assembles the target. For user-facing settings, see [Configuration files](configuration.html).

## Kernel and userspace choices

- The default installation includes Arch's Zen and LTS kernels. The live USB runs LTS. If a machine fails on the usual kernel, select another installed kernel using the [recovery guide](recovery.html).
- The optional base bundle configures zstd ZRAM at priority 100. Its `arche-maintenance` dependency provides cache retention and the rollback helper.
- A local normal-user login on TTY1 can start a Sway session when the workspace and hooks are installed. Other consoles are available for text login. The launcher distinguishes SSH, root and local sessions.

## Historical unattended storage

The earlier fixed-layout installer selected XFS with reflink and CRC enabled, 512-byte inodes and 16 allocation groups. Its root mount options included `rw,noatime,nodiratime,logbufs=8,logbsize=256k,allocsize=64M` and fstab dump/fsck fields `0 0`. Those settings describe the historical layout. Inspect the current system with `findmnt -no FSTYPE,OPTIONS /`.
