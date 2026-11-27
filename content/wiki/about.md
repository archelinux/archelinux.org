# About archelinux

archelinux is a rolling-release Arch-based workstation with a lightweight tiling desktop. Boot the USB, choose your tools, and log in to a SwayFX desktop with Zsh, tmux and Neovim. You can edit the configuration files in your home directory.

[Download 2.0.0](../download/index.html) · [Install guide](installation.html) · [Build it yourself](system.html)

![The idle desktop with Waybar and the Twin Blades wallpaper](../assets/archelinux-desktop.jpg)

The installer starts with XFS, optional LUKS encryption, and the Zen and LTS kernels. Keep the recommended workspace or clear the tool selection for a console install. The USB boots LTS and includes networking firmware. The installer downloads archelinux packages from signed stable and Arch packages from Arch mirrors.

## At the keyboard

- **Super+Enter** opens Foot. **Super+D** opens Fuzzel. Move between tiles with **Super+H/J/K/L**.
- Zsh starts with the Oh My Zsh `bureau` prompt. Use **Right** to accept a suggestion and **Esc Esc** to add `sudo`.
- Neovim runs LazyVim with `archevim`, a dark colorscheme with a black file tree. **Ctrl+H/J/K/L** moves between editor splits and tmux panes.
- Choose `gh`, GitHub notifications for Waybar, language servers, developer runtimes, or the NVIDIA CUDA bundle in the installer. You can also add a bundle later with pacman.

![Neovim with its file tree open beside Git history and Alacritty](../assets/archelinux-development.jpg)

![Four SwayFX tiles showing Neovim, btop, Git history and Zsh](../assets/archelinux-tiling.jpg)

Twin Blades wallpaper from [dharmx/walls](https://github.com/dharmx/walls/blob/e8d8a42e4fbecb2cf9619995edbc7ce19610bbd8/anime/aeb9uhrbr41a1.webp). The Waybar theme draws on [okubax/dotfiles](https://github.com/okubax/dotfiles).

## Hardware reports

Tell us which GPU, kernel and display setup you used, especially for NVIDIA, multi-monitor setups or suspend. [Submit a hardware report](../issues/index.html).

archelinux is [GPL-3.0](../LICENSE). Bundled software retains its upstream licenses.
