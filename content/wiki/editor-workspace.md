# Neovim, tmux and Yazi

The editor, multiplexer and file manager work independently. Use the [first session walk-through](first-session.html) to practice moving between configured Neovim splits and tmux panes.

## Keep an editing session open

From a project's directory, use `tmux new-session -A -s project` to create or attach to a named session. Open `nvim .` there. Use `tmux ls` to see your sessions from another terminal.

The first normal Neovim launch downloads LazyVim plugins. If you are offline and the plugins have never been installed, run `nvim --clean` to open the upstream editor. After bootstrap, use `:Lazy` to inspect the plugin status and `:checkhealth vim.lsp` to diagnose language-server setup. Open an actual file for the language before checking which servers attached. For Go, look for `gopls` in the installer or the [software guide](software.html).

## Find and move files in Yazi

Run `yazi` in the directory you want to browse. Use the arrow keys or H/J/K/L to move. Press **Space** to toggle selection and **q** to quit. Open the key help with **~** if you're using the default bindings, or consult the [Yazi keybinding reference](https://yazi-rs.github.io/docs/quick-start/). For removable disks, use the [mount and eject guide](storage.html).

## Use the clipboard

Inside the desktop, `printf '%s' 'some text' | wl-copy` copies text and `wl-paste` reads it. Neovim uses the Wayland clipboard integration there. In a console or SSH session, OSC 52 depends on the terminal and tmux settings. Test with a short non-sensitive string first. For screenshots, see [Copy a selected region](desktop.html).
