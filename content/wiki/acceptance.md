# Release acceptance checks

`tests/check.sh` checks shell syntax, source checksums, rollback edge cases, and formats a disposable sparse file to inspect XFS geometry. `arche-smoke-test` checks image binaries, LSP registration and parser loading and measures warm interactive shell startup over 20 samples. The median budget is 15 ms for Bash and 100 ms for Zsh with Oh My Zsh, its theme and the default plugins.

Run these checks in a disposable installed guest.

```sh
findmnt -no FSTYPE,OPTIONS /
xfs_info /
cat /etc/fstab
printf 'reflink test\n' > ~/clone-source
cp --reflink=always ~/clone-source ~/clone-copy
zramctl
systemctl is-enabled paccache.timer iwd systemd-networkd systemd-resolved
systemctl --user is-enabled ollama llama-server  # disabled
nvim example.lua                   # :checkhealth vim.lsp, :InspectTree
```

The release job boots the sealed ISO under UEFI, installs to a fresh XFS disk,
removes the ISO, and boots the installed system. The guest checks the hostname,
the user’s Zsh configuration, the running SwayFX compositor and Waybar. Build
logs, the installer screenshot and the installed desktop screenshot are available
in the GitHub Actions run. For the older dual-kernel acceptance run, see
the [QEMU acceptance record](qemu.html).
