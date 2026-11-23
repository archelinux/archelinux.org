# Recovery and maintenance

Choose the LTS entry from the boot menu if you need an alternative to Zen.
TTY2–6 provide console access independently of the desktop.

For a package with an older version still in the local cache:

    sudo arche-rollback PACKAGE

Package rollback does not replace backups. Changes involving related libraries
may require coordinated downgrades.

## Tested recovery

On 23 November 2026, a locally built 2.0.0 system running XFS and Linux 6.18.64-1-lts in QEMU/KVM was recovered from TTY2. The installed pacman keyring verified both ripgrep archives. `arche-rollback ripgrep` selected 15.1.0-4 from the cache, and the downgraded binary ran. Reinstalling the cached 15.2.0-1 restored the original version.

After a cold boot, SwayFX and Waybar started. The hashes of the user's edited Sway configuration and Zsh startup file still matched, including a custom keybinding. See the [hardware compatibility table](hardware.html) for the configurations tested.
