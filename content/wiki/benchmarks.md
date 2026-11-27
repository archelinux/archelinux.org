# Desktop performance baseline

This page records how the recommended SwayFX desktop starts and idles on a small, reproducible system. See the [hardware compatibility matrix](hardware.html) for physical-device checks.

## Test environment

- [Signed archelinux 2026.11.26 installer](https://github.com/archelinux/archelinux/releases/tag/rolling-20261126), with the recommended SwayFX workspace (`arche-swayfx` 1.0.0-8 and SwayFX 0.6.1-3), XFS root and both default kernels installed.
- QEMU 10.2.1 with KVM on an Intel Core i5-12400F host, with two vCPUs, 4 GiB assigned RAM, a local 24 GiB virtual disk, OVMF UEFI, virtio graphics and networking, and one 1280×800 output at 74.994 Hz.
- After verifying the initial install, the same guest was booted three times for measurement. The VM process exited between trials. The host disk cache was left warm.
- The disposable guest automatically signed in so human input delay would not affect the result. Each trial ended at an idle desktop with the default bar and background.

## Results

Measured on 27 November 2026 with Linux `7.3.6-zen1-1-zen`.

| Boot | Ready from QEMU launch | Guest RAM in use | Idle CPU busy | SwayFX PSS | Waybar PSS |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 17.76 s | 516.4 MiB | 1.37% | 145.7 MiB | 39.6 MiB |
| 2 | 16.95 s | 517.7 MiB | 1.35% | 143.5 MiB | 39.2 MiB |
| 3 | 17.24 s | 516.3 MiB | 1.37% | 137.4 MiB | 39.6 MiB |
| Median | 17.24 s | 516.4 MiB | 1.37% | 143.5 MiB | 39.6 MiB |

## How to reproduce

1. Verify the ISO signature and install the recommended workspace in a fresh guest with the settings above. Use the [guided QEMU test](https://github.com/archelinux/archelinux/blob/2b4318fedaf18abc0bce624df0db2fa03450f7b2/tests/qemu/guided.py) for the desktop readiness probe.
2. Start a wall-clock timer just before launching QEMU. Stop it when the guest reports the desktop ready. The probe checks that the Sway IPC socket and Waybar are running, an output is available, and the configured network services can resolve a hostname. This includes firmware and bootloader time.
3. Leave the desktop untouched for 30 seconds, then sample the aggregate `cpu` line in `/proc/stat` twice, 30 seconds apart. Compute busy time as the difference in total ticks minus the difference in idle and I/O-wait ticks. Divide by the difference in total ticks.
4. At the end of that interval, subtract `MemAvailable` from `MemTotal` in `/proc/meminfo` and divide by 1,024 for MiB. For per-process proportional memory, read `Pss` from each process's `/proc/PID/smaps_rollup`.

The aggregate tick count uses the first eight fields after `cpu`. The guest fields are already included in earlier fields. The CPU percentage is across both vCPUs.

Real machines will differ in boot firmware, graphics drivers and background activity. The virtual graphics setup provides no physical GPU utilization result. A comparison with another distribution should use an installed desktop with the same resources, readiness criteria and sampling interval.
