# Install archelinux

Use this walkthrough to go from the boot menu to your first login. You need an x86_64 computer, a [verified installation USB](install-media.html), an internet connection, and a [backup of any files on the target disk](backups.html).

## Boot and get online

1. Open your computer's firmware boot menu and choose the USB. On a UEFI machine, select its UEFI entry. You should see a text console and the archelinux installer.
2. Connect Ethernet or follow [Connect to the network](networking.html) to join Wi-Fi with `iwctl`. Check that a hostname resolves before continuing. The installer verifies the signed stable channel before changing the target disk.
3. Open **Arche software**. Space toggles a selection. Keep the recommended SwayFX workspace for a keyboard-driven desktop, or clear the selections for a console install. Use [Choose software](software.html) to decide what else to select.

## Choose the disk and review

Use **Disk configuration** to select the target. If you have similar drives, switch to a text console and compare their sizes and models with:

```sh
lsblk -d -o NAME,SIZE,MODEL,TRAN
```

A guided layout uses XFS for root. On UEFI the boot files use a separate EFI system partition. Select LUKS in disk configuration if you want encryption, keep the passphrase somewhere safe, and read the final review for the partitions the installer will encrypt.

At the final review, check the target device, each partition's action, user account, bootloader, locale, kernels, software, and networking mode. **Create**, **reformat**, and **delete** can destroy existing data. For a disk shared with another operating system, inspect every action before confirming.

## Boot the installed system

When the installer finishes, reboot and remove the USB. Start from the installed disk and sign in with the account you created. If you selected a Sway desktop, signing in on the local first console launches it. Use the [first session walk-through](first-session.html) to get oriented, then [run the first system update](rolling-updates.html).

If you return to the USB installer, check the firmware boot order. If the installed system boots to a login but the desktop fails, start with [desktop troubleshooting](troubleshooting.html). If it cannot boot, keep the USB for [system recovery](recovery.html).
