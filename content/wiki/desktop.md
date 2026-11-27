# Use and customize the Sway desktop

![SwayFX desktop with Waybar and Twin Blades wallpaper](../assets/archelinux-desktop.jpg)

Sway manages windows. Foot is the terminal, Fuzzel launches apps, and Waybar shows workspace and system status. Learn the defaults in [Keyboard shortcuts](shortcuts.html) or practice them in [Your first session](first-session.html).

## Inspect monitors and adjust scale

Run `swaymsg -t get_outputs` inside the desktop to see output names, positions and modes. To try a different scale, use the output name shown on your machine. This example uses an internal panel called `eDP-1`.

```sh
swaymsg output eDP-1 scale 1.25
```

If it looks right, put `output eDP-1 scale 1.25` in your user Sway configuration. Use the [configuration guide](configuration.html) to validate and reload the change. Consult `man 5 sway-output` for placement, rotation and resolution. The [hardware matrix](hardware.html) records physical display tests.

## Add a second keyboard layout

Create or edit `~/.config/sway/keyboard.conf`, which the shipped Sway config includes. This example keeps US English first and adds German. Substitute the second XKB layout code you want.

```text
input type:keyboard xkb_layout us,de
```

Reload Sway, then use the layout shortcut in the [keyboard reference](shortcuts.html) or click the layout indicator in Waybar. Run `swaymsg -t get_inputs` to inspect the active layout.

## Copy a selected region to the clipboard

Run the capture command in a terminal.

```sh
grim -g "$(slurp)" - | wl-copy --type image/png
```

Drag over the region you want, release, then paste into an app that accepts clipboard images. Use Escape to cancel the selection. Screen sharing is a separate feature handled by the Wayland portal. Open a browser or meeting app that supports it and select the output in its sharing prompt.

## Lock, idle and suspend

For a manual lock, use the [lock shortcut](shortcuts.html). The shipped session locks after 15 minutes of inactivity, then powers off the outputs five seconds later. Wake the display with input. Before sleep, the session runs the lock command.

On supported hardware you can suspend from the terminal with `systemctl suspend`. Save your work first. On resume, check that the lock is active and that networking, audio and brightness still work. See the [hardware matrix](hardware.html) for what has been exercised on physical machines.

## Theme and wallpaper

SwayFX uses the Litho Dark palette and adds blur and rounded corners. It draws on [okubax/dotfiles](https://github.com/okubax/dotfiles). The package includes provenance and licensing under `/usr/share/doc/arche-tui-stack/`. The Twin Blades wallpaper comes from the [dharmx/walls collection](https://github.com/dharmx/walls/blob/e8d8a42e4fbecb2cf9619995edbc7ce19610bbd8/anime/aeb9uhrbr41a1.webp). To personalize it, update the background path in your user configuration.
