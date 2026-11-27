# Connect to the network

archelinux uses iwd for Wi-Fi association, systemd-networkd for IP configuration, and systemd-resolved for DNS. The live installer and the default installed system support Ethernet with DHCP. Plug in the cable and check the link if the connection does not come up.

## Join a Wi-Fi network

Run `iwctl` and enter these commands at its prompt. Replace `wlan0` with the device name from `device list` and use your network's name.

```text
device list
station wlan0 scan
station wlan0 get-networks
station wlan0 connect "Your SSID"
station wlan0 show
exit
```

Enter the passphrase when prompted. The station should show a connected state. Verify the network from the shell:

```sh
ip -br address
getent hosts archlinux.org
```

Look for an address on the connected interface and an address returned by the hostname lookup. If the live Wi-Fi profile should carry over, keep the installer's default network mode. Choose fresh iwd setup when you want to reconnect after installation, or manual mode when the network requires explicit settings.

## Find where the connection fails

| What you see | What to check |
| --- | --- |
| No wireless device in iwd | Check `rfkill list`. A soft block can be cleared with `sudo rfkill unblock wifi`. A hardware block requires the switch or firmware setting. |
| The station connects, but has no address | Check `networkctl status wlan0` for link and DHCP state. Substitute the actual interface. |
| There is an address, but names fail to resolve | Check `resolvectl status` and the resolved service. |
| The issue appears only after leaving the USB | Confirm the correct install network mode and inspect the installed boot's service logs. |

```sh
systemctl status iwd systemd-networkd systemd-resolved
journalctl -b -u iwd -u systemd-networkd -u systemd-resolved
```

See [report a problem](troubleshooting.html) for what to include when asking for help. Avoid sharing Wi-Fi passwords or files from `/var/lib/iwd`.
