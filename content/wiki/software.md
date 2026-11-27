# Choose software

In the installer, **Arche software** is the curated list. Use its search filter and toggle individual entries. **Additional packages** is for other packages from the enabled pacman repositories. Some choices add companions, such as the audio system and status bar that Sway uses.

| What you want | What to select |
| --- | --- |
| Recommended tiling desktop | `arche-swayfx` for blur and rounded corners. Select `sway` for stock Sway. |
| Console workstation | Clear the desktop selection. Keep just the tools you want, such as Git, Neovim and tmux. |
| Browsing | Firefox from Arch, or Google Chrome Stable via its Flathub wrapper. |
| File management | Yazi for a keyboard-driven file manager and removable drive controls. |
| Development | Go and `gopls` when you need them, or `arche-agentic-core` for a larger runtime and code-search bundle. |
| Coding workflows | Filter for **agent workflows**, then pick from the [workflow tools](agent-workflows.html). |
| NVIDIA compute | `arche-cuda` for the optional driver and CUDA bundle. Review [hardware compatibility](hardware.html) and allow for the large download. |

After installation, run `pacman -Ss PATTERN` to search the local repository metadata and `pacman -Si PACKAGE` to inspect a result. Use the [rolling update guide](rolling-updates.html) for installing and upgrading system packages together.

To work with community recipes, install `paru`. Search with `paru -Ss NAME` and inspect the package's AUR page, PKGBUILD and comments before building. AUR packages are maintained by the community. Review what a recipe downloads and runs before accepting the build. Use [Arch's pacman manual](https://man.archlinux.org/man/pacman.8) for command reference.
