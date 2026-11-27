# Recovery and maintenance

If the desktop stops starting after an update, use a text console to check the update and restore the affected package. Personal settings in your home directory remain editable from the console.

## Recover from the installed system

1. Switch to **Ctrl+Alt+F2** and sign in. TTY2 through TTY6 work independently of Sway. If the current kernel cannot boot and the LTS entry is installed, select **Archelinux (linux-lts)** from the boot menu and retry.
2. Check the package transaction and the current boot's warnings:

       tail -n 60 /var/log/pacman.log
       journalctl -b -p warning

3. If a compositor update caused the failure and the previous package is cached, run:

       sudo arche-rollback swayfx
       pacman -Q swayfx

   Then reboot and check that SwayFX and Waybar start. For a different failed package, substitute its exact package name.

## Recover from the installer USB

Boot the signed installer USB and use **Ctrl+Alt+F2** to reach a root console. Use `lsblk -f` to identify the installed root filesystem. If it is encrypted, unlock its LUKS partition with `cryptsetup open` and use the resulting mapper device as the root filesystem.

Mount the installed root at `/mnt`, substituting its actual device in the example:

    mount /dev/ROOT_DEVICE /mnt
    arch-chroot -r /mnt pacman -Q swayfx
    arch-chroot -r /mnt arche-rollback swayfx
    umount /mnt

This compositor repair uses the installed system's package cache and keyring. To repair a kernel or boot files, mount the installed boot partition according to the target's `/etc/fstab` before making those changes. Remove the USB and boot the installed system to confirm the repair.

For a package with an older version still in the local cache:

    sudo arche-rollback PACKAGE

Keep a separate backup of personal files. If related libraries changed together, check their version requirements before downgrading any of them.

## Tested recovery

On 27 November 2026, a fresh QEMU/KVM install from the signed 2026.11.26 ISO successfully booted SwayFX and Waybar with XFS and both default kernels installed. On a disposable copy, a local test package replaced SwayFX with a failing executable. The desktop did not start. We selected Linux 6.18.65-1-lts and confirmed that TTY2 worked. `arche-rollback swayfx` restored the signed 0.6.1-3 package from cache and the desktop returned after a cold boot. The edited Sway, Waybar and Zsh files matched their original SHA-256 hashes.

On a second disposable copy with the same fault, the signed installer booted from an emulated USB drive. We mounted the installed XFS root and ran the rollback inside it with `arch-chroot -r`, using the installed package cache and keyring. After removing the installer and cold booting the repaired disk, SwayFX and Waybar started and all three edited files still matched. These drills used an unencrypted XFS root.


On 23 November 2026, a locally built 2.0.0 system running XFS and Linux 6.18.64-1-lts in QEMU/KVM was recovered from TTY2. The installed pacman keyring verified both ripgrep archives. `arche-rollback ripgrep` selected 15.1.0-4 from the cache, and the downgraded binary ran. Reinstalling the cached 15.2.0-1 restored the original version.

After a cold boot, SwayFX and Waybar started. The hashes of the user's edited Sway configuration and Zsh startup file still matched, including a custom keybinding. See the [hardware compatibility table](hardware.html) for the configurations tested.

## Rolling upgrade rehearsal

On 23 November 2026, we installed the signed public 2.0.0 ISO on a fresh UEFI/XFS virtual disk. The guest verified a locally staged, signed archelinux package repository and completed a full system upgrade. From the local package cache it rolled `arche-maintenance` back from 2.0.0-3 to 2.0.0-2, then upgraded to 2.0.0-3 again. SwayFX and Waybar started after a cold boot. The original Twin Blades checksum matched, the edited Sway shortcut survived, and the offline First Session guide was present.

Check the [rolling update guide](rolling-updates.html) for public channel availability.
