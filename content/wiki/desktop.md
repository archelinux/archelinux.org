# SwayFX and Litho Dark

![SwayFX desktop with Waybar and Graphite wallpaper](../assets/archelinux-desktop.jpg)

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

The screenshot previews Graphite, the archelinux project’s original wallpaper for `arche-workspace-defaults` 2.0.0-42. It installs at `/usr/share/arche/graphite.jpg`. An existing Sway configuration pointing to `/usr/share/arche/twin-blades.jpg` will pick up Graphite through a compatibility symlink. [Download Graphite](../assets/graphite.svg) and read its [0BSD license](../assets/LICENSE.graphite).

For automated UEFI installation acceptance on a disposable qcow2 disk, see
[QEMU installation tests](qemu.html).
