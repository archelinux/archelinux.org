# Troubleshoot by symptom

Start with what you can still see or open. The links take you straight to the relevant procedure.

| Symptom | Start here |
| --- | --- |
| USB never appears in the firmware boot menu | [Prepare the installation media](install-media.html). |
| Installer cannot reach the signed repositories | [Connect to the network](networking.html), then check [mirror and signature failures](rolling-updates.html). |
| No graphical desktop after signing in | Switch to TTY2 using [Keyboard shortcuts](shortcuts.html) and check the logs below. |
| An update stopped Sway from starting, or the installed system will not boot | [Recover from the installed console or USB](recovery.html). |
| Bluetooth pairs but audio plays through laptop speakers | [Choose an audio output](audio.html). |
| Android only charges over USB | [Switch to File Transfer](storage.html). |
| Second monitor is missing | [Inspect Sway outputs](desktop.html). Compare detected hardware with the [compatibility matrix](hardware.html). |
| Pacman reports a lock, signature error, or failed download | [Update troubleshooting](rolling-updates.html). |

## When login works but Sway fails

Log in on the text console and inspect the boot and the login service. Compare the installed kernel with the [hardware matrix](hardware.html).

```sh
uname -r
journalctl -b -u getty@tty1.service --no-pager -n 80
journalctl -b -p warning --no-pager -n 80
```

If you just edited Sway's config, restore the file you saved before editing. The [configuration guide](configuration.html) describes how to validate and reload it.

## Report a problem

Include the ISO date or affected package versions, the kernel from `uname -r`, what you expected, and the steps that reproduce the problem. Share only the relevant log lines or errors. Remove credentials, private paths and logs unrelated to the problem. [Open a support report](../issues/index.html).
