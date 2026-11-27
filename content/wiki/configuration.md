# Configuration files

Edit the files in your home directory to personalize your session. Package updates can replace the templates in `/usr/share/arche/skel`. Use those templates as a reference when comparing your settings with a newer release.

| Component | User configuration |
| --- | --- |
| Sway and SwayFX | `~/.config/sway/config` |
| Extra keyboard layouts | `~/.config/sway/keyboard.conf` with the shipped Sway include |
| Waybar | `~/.config/waybar/config.jsonc` and `style.css` in the same directory |
| Foot | `~/.config/foot/foot.ini` |
| Zsh and Oh My Zsh | `~/.zshrc` |
| Neovim and LazyVim | `~/.config/nvim/` |
| tmux | `~/.tmux.conf`; distro defaults are in `/etc/tmux.conf` |
| Yazi | `~/.config/yazi/` |

## Edit and check Sway

Save a working copy before editing:

```sh
cp -a ~/.config/sway/config ~/.config/sway/config.before-edit
```

Edit the configuration file, then run:

```sh
sway --validate --config ~/.config/sway/config
```

If validation succeeds, run `swaymsg reload` inside your desktop or use the [reload shortcut](shortcuts.html). If validation fails, follow the reported line and check the files your config includes. If the desktop is unusable, use [Troubleshoot by symptom](troubleshooting.html) to reach a text console.

## Compare your settings with the package template

Use a diff before copying any update into your home directory. For example:

```sh
diff -u ~/.config/sway/config /usr/share/arche/skel/.config/sway/config
```

Move just the changes you want into your current file. For the installer's software choices and official repositories, see [Choose software](software.html).
