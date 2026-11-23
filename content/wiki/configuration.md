# Packages and configuration

| Package | Contents |
| --- | --- |
| `arche-base` | Base development tools, both kernels, firmware, XFS, ZRAM, NetworkManager, cache retention and rollback |
| `arche-tui-stack` | Sway, top Waybar, Fuzzel, Mako, fonts/audio controls, tmux, terminals, CLI tools, shells, Neovim and preinstalled language servers |
| `arche-agentic-core` | uv, Bun from Arch extra, cargo-binstall, ast-grep, tree-sitter-cli, disabled inference user units |
| `arche-cuda` | Optional nvidia-open-dkms, nvidia-utils, Arch's `cuda` toolkit and cudnn |

`pkgs/*/PKGBUILD` are the canonical dependency lists. `packages.x86_64` defines the live console image. The ISO carries the optional arche-cuda metapackage in its local repository. The driver, toolkit and cuDNN download from Arch mirrors when selected. `arche-maintenance` provides `paccache-hook` with a locally maintained hook backed by `pacman-contrib`; there is no additional AUR hook dependency.

Live configuration overrides and package-owned files are linked into package sources with SHA-256 checksums. Package-owned `/usr` files live in `pkgs/*/files/`, outside the live overlay, so archiso does not pre-create files that pacman must install. After changing an overlay source, update its PKGBUILD checksum (`updpkgsums` from `pacman-contrib`). Package templates live under `/usr/share/arche/skel` to avoid colliding with Bash-owned skeleton files. The installer copies these into `/etc/skel` before creating the user. Installing metapackages on an existing Arch system does not overwrite user dotfiles; copy the templates explicitly.

The TUI package generates `zoxide init --cmd cd SHELL` and `direnv hook SHELL` once at build time and compiles the Zsh hook loader. Shell startup sources those files, sets `EDITOR=nvim` and `FZF_DEFAULT_COMMAND`, when the relevant tools are installed. The guided install initializes Oh My Zsh before loading these hooks. Rebuild the package when upgrading hook generators to refresh their output. Interactive prompt hooks still perform the intended directory tracking and environment checks.

Neovim starts LazyVim with the dark `archevim` colorscheme. On first launch, lazy.nvim downloads plugins into the user’s data directory. Language servers are selected through the installer and use Neovim’s LSP API. Lua, C, Vim, Vimdoc, query, Python and Rust parsers are installed; Python and Rust have baseline highlight queries. Other filetypes retain standard syntax highlighting; Go has its preinstalled LSP. Inside Wayland, Neovim uses wl-copy/wl-paste for system clipboard synchronization. In console/SSH sessions, OSC 52 copies through supported terminals/tmux and paste uses the local yank register. Ctrl-h/j/k/l navigates Neovim windows and adjacent tmux panes.
