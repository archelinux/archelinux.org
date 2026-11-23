# SwayFX and Litho Dark

![SwayFX desktop with Waybar and Twin Blades wallpaper](../assets/archelinux-desktop.jpg)

The selected desktop adapts [okubax/dotfiles](https://github.com/okubax/dotfiles)'s
Litho Dark palette and inset Waybar panel with a centered clock. Provenance and the upstream
license are installed in `/usr/share/doc/arche-tui-stack/`. Tiled and floating windows have a one-pixel outline. The recommended SwayFX compositor adds backdrop blur and gives Waybar and windows a nine-pixel corner radius. The workspace highlight sits eight pixels inside the panel and has a three-pixel radius. Applications that draw their own
internal chrome remain responsible for that chrome.

Super+Return opens Foot; Super+d opens Fuzzel; Super+Shift+q closes a window;
Super+h/j/k/l moves focus; Super+r enters resize mode; Super+Shift+c reloads
configuration; Super+Shift+e exits Sway. No upstream dotfile installer or personal
cloud/service configuration is run. Media keys use WirePlumber and playerctl.

Login hooks exist for Zsh, Bash and Fish. They require a local non-root TTY1
session, no existing display, and no SSH connection. NVIDIA/nouveau detection
sets `WLR_NO_HARDWARE_CURSORS=1` and passes `--unsupported-gpu`; this is a fallback,
not a guarantee for every driver. No hook is added to the live root installer.
`useradd -m -U -k /usr/share/arche/skel` copies all templates directly into the
new user's home and assigns their ownership. Package templates never claim
Bash-owned `/etc/skel` files.

Sway fills the output with Twin Blades from `/usr/share/arche/twin-blades.jpg`. The artwork comes from the [dharmx/walls collection](https://github.com/dharmx/walls/blob/e8d8a42e4fbecb2cf9619995edbc7ce19610bbd8/anime/aeb9uhrbr41a1.webp). The [collection’s credits](https://github.com/dharmx/walls/blob/e8d8a42e4fbecb2cf9619995edbc7ce19610bbd8/.github/README.md#sources) attribute the images to their respective artists. We could not verify an artist credit or a redistribution license for this image.

For automated UEFI installation acceptance on a disposable qcow2 disk, see
[QEMU installation tests](qemu.html).
