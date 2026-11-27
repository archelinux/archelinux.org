# Hardware compatibility

These results apply to the named release and configuration. VM checks cover virtual devices. The physical checks below identify exactly what was exercised.

| Release and test date | System | Kernel and graphics | Observed result |
| --- | --- | --- | --- |
| 2.0.0 release candidate build promoted to stable, 23 Nov 2026 | QEMU/KVM x86_64, OVMF UEFI, virtio disk and virtual graphics | linux-lts, SwayFX, one virtual output | Passed guided XFS installation, installed-system boot, Sway IPC and Waybar startup. [Build and boot record](https://github.com/archelinux/archelinux/actions/runs/45154069630) |
| Local build from 2.0.0 release source, 23 Nov 2026 | QEMU/KVM x86_64, XFS | Linux 6.18.64-1-lts, SwayFX | Passed [TTY2 cached package recovery](recovery.html): downgrade, restore, cold boot and preservation of edited Sway and Zsh files. |
| 2026.11.26 installer | QEMU/KVM x86_64, OVMF UEFI, virtio disk and virtual graphics | Linux LTS and Zen installed, SwayFX | The published ISO passed guided XFS installation and an installed desktop boot in CI. [Build and boot record](https://github.com/archelinux/archelinux/actions/runs/45910062233) |
| 2026.11.26 installer, 27 Nov 2026 | QEMU/KVM x86_64, OVMF UEFI, virtio disk and virtual graphics | Linux 6.18.65-1-lts and 7.3.6.zen1-1 installed, SwayFX 0.6.1-3 | Passed a fresh XFS install and desktop boot. The installer enabled iwd, systemd-networkd, systemd-resolved and BlueZ. Both the LTS console and virtual USB [recovery drills](recovery.html) passed. See the [desktop performance baseline](benchmarks.html) for startup and idle measurements. |

## Physical checks

Physical desktop and USB checks ran on 27 November 2026. The Android result comes from the November 2026 file-transfer rehearsal.

| Feature | Hardware and environment | Observed result |
| --- | --- | --- |
| Graphics and external display | Intel Core i3-9100, NVIDIA GeForce GTX 1650, proprietary NVIDIA driver, archelinux with Linux 6.18.65-1-lts and `arche-tui-stack` 2.0.0-42 | SwayFX was running with one active 1920×1080 HDMI output. Hot-plug, docks, and multiple monitors still need testing. |
| Wired networking | Intel I219-V, same installed desktop | Reconnected remotely over the existing network. systemd-networkd and systemd-resolved were active. |
| Audio | Same installed desktop, PipeWire and WirePlumber | WirePlumber reported a default output and its current volume. Playback and Bluetooth audio still need a listening test. |
| Wi-Fi and Bluetooth controllers | Intel AX210, Ubuntu lab host | PCI Wi-Fi and USB Bluetooth controllers were detected. The archelinux desktop exposed no Bluetooth controller. Wi-Fi association and reconnect, Bluetooth pairing, and headset playback on archelinux still need testing. |
| Android USB file transfer | Redmi Note 13 Pro, File Transfer mode, `arche-mtp` on the Linux lab host | Listed files, uploaded a test file, downloaded it with byte-for-byte verification, and removed the test file. |
| Removable USB storage | SanDisk 3.2Gen1, 28.7 GiB, same installed desktop as the GTX 1650 check | Mounted NTFS and FAT read-only from a shell and read both directory listings. Unmounted both partitions and verified a successful SCSI eject. |
| Laptop suspend, brightness and hybrid graphics | Physical laptops and AMD graphics | Awaiting model-specific tests for suspend/resume, backlight control, dock/display reconnect and hybrid graphics. |

## Test a physical machine

- On a laptop, suspend and resume once. Check that the lock screen appears and that Wi-Fi, audio and brightness controls still work after unlocking.
- If you use a dock, plug it in, unplug it and reconnect it. Run `swaymsg -t get_outputs` to see which displays Sway detects, then move a window between them and check the scale.
- Start a screen share in the browser or meeting app you actually use. Choose an output and confirm a second participant can see it.
- On a hybrid-GPU laptop, repeat the display and screen-sharing checks with the external monitor attached. If Sway fails to start, switch to TTY2 with Ctrl+Alt+F2 and log in to inspect the journal with `journalctl -b`.

## Share the result

[Submit a hardware report](../issues/index.html) with your model, GPU, kernel, release and date. Mark each feature working, limited, failed, or untested. Include a workaround when available. Reproduced results can then be linked here with their issue number.
