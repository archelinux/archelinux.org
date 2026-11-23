# Hardware compatibility

These results apply to the named release and configuration. A VM check verifies the virtual devices the guest saw. Physical systems need separate reports.

| Release and test date | System | Kernel and graphics | Observed result |
| --- | --- | --- | --- |
| 2.0.0 release candidate build promoted to stable, 23 Nov 2026 | QEMU/KVM x86_64, OVMF UEFI, virtio disk and virtual graphics | linux-lts, SwayFX, one virtual output | Passed guided XFS installation, installed-system boot, Sway IPC and Waybar startup. [Build and boot record](https://github.com/archelinux/archelinux/actions/runs/45154069630) |
| Local build from 2.0.0 release source, 23 Nov 2026 | QEMU/KVM x86_64, XFS | Linux 6.18.64-1-lts, SwayFX | Passed [TTY2 cached package recovery](recovery.html): downgrade, restore, cold boot and preservation of edited Sway and Zsh files. |
| 2.0.0 | Physical laptops, desktops and docks | Intel, AMD and NVIDIA | Awaiting model-specific reports for graphics, screen sharing, suspend, Wi-Fi, audio and external monitors. |

## Test a physical machine

- On a laptop, suspend and resume once. Check that the lock screen appears and that Wi-Fi, audio and brightness controls still work after unlocking.
- If you use a dock, plug it in, unplug it and reconnect it. Run `swaymsg -t get_outputs` to see which displays Sway detects, then move a window between them and check the scale.
- Start a screen share in the browser or meeting app you actually use. Choose an output and confirm a second participant can see it.
- On a hybrid-GPU laptop, repeat the display and screen-sharing checks with the external monitor attached. If Sway fails to start, switch to TTY2 with Ctrl+Alt+F2 and log in to inspect the journal with `journalctl -b`.

## Share the result

[Submit a hardware report](../issues/index.html) with your model, GPU, kernel, release and date. Mark each feature working, limited, failed, or untested. Include a workaround when available. Reproduced results can then be linked here with their issue number.
