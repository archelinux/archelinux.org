# Prepare a bootable USB or VM

The installation ISO boots Linux LTS and downloads packages during installation. You can try the same ISO in a virtual machine before using it on a physical disk.

## Download and verify

Download the installation ISO and verification files from the [download page](../download/index.html). Follow [Verify the ISO](verify.html) before writing the image. If the download comes in parts, reassemble them during verification.

## Write a USB

Writing the image replaces the contents of the selected USB drive. Back it up and disconnect other removable drives if practical.

- **Windows.** In [Rufus](https://rufus.ie/), select the USB device and the verified ISO. When offered a choice of write modes, use DD image mode.
- **Linux.** Use a disk image writer or identify the USB before and after plugging it in with `lsblk -d -o NAME,SIZE,MODEL,TRAN`. Unmount any of its mounted partitions. Substitute the verified image path and the whole USB device in the example below. Confirm the model and size again before pressing Enter.

```sh
sudo dd if=/path/to/archelinux.iso of=/dev/USB_DEVICE bs=4M status=progress conv=fsync
```

For example, the whole device would be `/dev/sdb` if Linux listed the USB as `sdb`. Wait for the write to finish before unplugging it. Follow the [installation walkthrough](installation.html) when you boot it.

## Try it in a VM

Create a new x86_64 guest with UEFI, two vCPUs, 4 GiB RAM, a fresh virtual disk of at least 24 GiB, and a virtual network adapter using NAT. Attach the verified ISO as optical media and boot it. The [installation walkthrough](installation.html) applies to the guest too. After completing it, detach the ISO and boot the guest disk. These settings match the [tested VM baseline](benchmarks.html).
