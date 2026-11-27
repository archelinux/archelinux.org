# Audio and Bluetooth

The recommended desktop uses PipeWire and WirePlumber. Click the Waybar speaker to open Wiremix, or run `wiremix` from Foot. The mixer lets you check which outputs and streams are active. The volume and mute keys act on the default device.

## Choose a default device

Run `wpctl status`, find the numeric ID under **Sinks** or **Sources**, then use it in place of `TARGET_ID`.

```sh
wpctl set-default TARGET_ID
wpctl get-volume @DEFAULT_AUDIO_SINK@
```

Start new playback and confirm the expected device is active. If an already-running application stays on its previous output, restart the stream and check its routing in Wiremix.

## Connect a Bluetooth headset

BlueZ is selected with the recommended workspace. On another profile you can select it during installation or add `bluez` and `bluez-utils` using the [package guide](software.html). On an installed system, confirm the service is running with `systemctl status bluetooth`.

Put your headset in pairing mode. Click the Bluetooth indicator or run `bluetoothctl`. Replace `DEVICE_ADDRESS` with the address beside your headset in the scan.

```text
power on
scan on
devices
pair DEVICE_ADDRESS
connect DEVICE_ADDRESS
scan off
exit
```

Confirm the device in Wiremix, or choose its sink using the instructions above. If there is no controller, check `rfkill list` and `journalctl -b -u bluetooth`. If the controller is present and pairing works, but the headset never appears as an output, check which desktop audio services are running.

```sh
systemctl --user status pipewire pipewire-pulse wireplumber
wpctl status
```

The [hardware compatibility matrix](hardware.html) records which physical tests have been completed.
