# Standalone tools on Arch Linux

These utilities and the archevim colorscheme can be installed on a plain Arch Linux system. Their recipes build from a versioned source file and list dependencies available in Arch’s official repositories. [Source and packaging recipes](https://github.com/archelinux/arch-tools).

| Package | What it does |
| --- | --- |
| `arche-waybar-github` | Counts unread pull requests and issues. Hover to see repository names and titles. |
| `arche-waybar-status` | Produces Waybar JSON for low disk space, active VPNs or GPU readings. |
| `arche-rollback` | Reinstalls the newest older version of a package available in your configured pacman cache. |
| `neovim-archevim` | The distro’s Neovim colorscheme and matching lualine theme. Enable it with `:colorscheme archevim`. |

## Install a package on plain Arch

Install the build tools, clone the packaging repository and review the recipe you want. Build as your regular user. For example:

    sudo pacman -S --needed base-devel git
    git clone https://github.com/archelinux/arch-tools.git
    cd arch-tools/aur/arche-waybar-github
    less PKGBUILD
    makepkg -si

On archelinux, the signed repository supplies `arche-waybar-github`. Its workspace package includes the status indicators, and `arche-maintenance` provides the rollback command.

## Set up the GitHub indicator

Sign in with `gh auth login --hostname github.com`. Your account needs access to read its notifications. Add `custom/github` to a Waybar module list, add this object to your Waybar configuration and restart Waybar:

```json
"custom/github": {
  "exec": "arche-waybar-github",
  "return-type": "json",
  "interval": 120,
  "hide-empty-text": true,
  "on-click": "xdg-open https://github.com/notifications"
}
```

In standalone version 2.0.1, an empty inbox hides the module. `GH login` asks you to sign in. `GH ?` means the notification check failed. The optional click action uses xdg-utils.

For other indicators, use `arche-waybar-status disk`, `arche-waybar-status vpn` or `arche-waybar-status gpu` as the module command. For a known package regression, `sudo arche-rollback PACKAGE` applies the cached downgrade immediately. Check [recovery and maintenance](recovery.html) before downgrading related libraries.
