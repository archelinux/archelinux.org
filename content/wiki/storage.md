# Removable drives and Android phones

USB drives and phone file transfer use different tools. A phone in File Transfer mode can exchange files without exposing its storage as a disk.

## Mount and eject a USB drive

With Yazi installed and its shipped keymap in place, open `yazi` and press **Shift+M**. Select the removable device in the mount menu. From a desktop shell, you can also inspect the device and use UDisks directly. Substitute the partition name from `lsblk`.

```sh
lsblk -o NAME,TRAN,RM,SIZE,FSTYPE,MOUNTPOINTS
udisksctl mount -b /dev/USB_PARTITION
```

UDisks prints the mount path. Close files on the drive and exit any shell whose working directory is on it, then unmount it in Yazi or with:

```sh
udisksctl unmount -b /dev/USB_PARTITION
```

Wait for unmount to succeed before removing the drive. If it is busy, check which application is using it and close the file there. Install `udisks2` separately if you use a custom profile and `udisksctl` is missing.

## Copy files from an Android phone

Unlock the phone, connect a data-capable USB cable, then select **File Transfer** in Android's USB settings. The default installation includes the Android USB tools and MTP helpers. Use the interactive shell or list the phone to find a file ID:

```sh
arche-mtp shell
arche-mtp ls
```

In the shell, enter `help` to see the available commands and `exit` to return to your terminal. From the terminal, substitute the IDs in the following examples. Omit `FOLDER_ID` to upload to the root of the phone storage.

```sh
arche-mtp ls FOLDER_ID
arche-mtp get FILE_ID ./photo-from-phone.jpg
arche-mtp put ./example.txt FOLDER_ID
```

Keep the phone unlocked until the transfer finishes. If it switches to charging or the device disappears, reconnect, reselect File Transfer, and try a cable or port known to carry data. USB debugging is a separate Android feature and ordinary file transfer uses MTP.
