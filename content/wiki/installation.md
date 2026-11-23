# Installation guide

The recommended system is a keyboard-driven Sway desktop with Zsh, Oh My Zsh, Neovim and tmux. The USB boots to a console and needs internet access to install. Arche uses XFS for root. You can enable LUKS and choose your software. If you depend on booting filesystem snapshots, factor that into your choice: Arche provides individual cached-package rollback.


## Install from USB

The ISO starts the guided archinstall installer on TTY1. The rolling installer enables the signed stable channel at the end of setup. After your first login, run `sudo pacman -Syu` to update the installed system.

1. [Download the signed ISO](../download/index.html) and verify it using the [verification guide](verify.html), then write it to installation media.
2. Boot the console and connect to the network. Use NetworkManager or `nmcli` if needed.
3. Open **Arche software** to keep the recommended SwayFX workspace or toggle individual tools with Space. SwayFX supplies nine-pixel window corners and terminal background blur. For stock Sway, clear **arche-swayfx** and select **sway**. Both compositors use a slim mauve focus outline, small gaps and a floating Waybar panel. Optional tools include **github-cli** (`gh`), **yazi** (file manager) and **btop** (system monitor). For unread GitHub PRs and issues on the Sway bar, select **arche-waybar-github**, then run `gh auth login` after login. If your token needs notification access, run `gh auth refresh -h github.com -s notifications`. Hover for thread titles or click to open your inbox. Choose **spotify** for the desktop app from Flathub or **spotify-player** for the terminal client (Spotify Premium required). You can select both. Clear the list for a console system. Selecting Sway includes its terminal, launcher, bar, lock, media controls and region screenshots (`grim -g "$(slurp)" - | wl-copy --type image/png`). Select other packages in **Additional packages**.
4. New accounts start in Zsh with Oh My Zsh, the `bureau` theme and the [shell plugins and shortcuts](shell.html). Edit `~/.zshrc` to personalize them.
5. In **Disk configuration**, select the target and layout. Archelinux uses XFS for the root filesystem. UEFI uses a separate FAT32 EFI partition. Configure LUKS encryption here if wanted and retain your passphrase. The installer does not choose a target disk for you.
6. Review kernels, bootloader, networking, locale, time zone and authentication. Check the final configuration and selected disk before confirming. Formatting erases the selected partitions.

Release signing-key fingerprint:

    E446 C26A 0B7B A1A6 6A3D CC9F 7EC5 6400 3573 C80B

See the [verification commands](verify.html) and [signed package-repository setup](publication.html). Download the [public key](../assets/archelinux-release-public.asc).

On first launch, Neovim downloads the LazyVim plugins. Keep the internet connection active until setup finishes. Change the default `archevim` colorscheme in `~/.config/nvim/lua/plugins/colors.lua`.
