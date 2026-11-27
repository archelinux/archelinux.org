# Your first ten minutes in archelinux

This walkthrough uses the recommended SwayFX, Foot, tmux and Neovim workspace.
See the [keyboard reference](shortcuts.html) for the current modifier keys.
You can read the guide and use the terminal offline. The first normal Neovim
launch needs internet access to install LazyVim and its plugins.

## Open the guide and a terminal

With arche-workspace-defaults 2.0.0-41 or newer, press **Alt+D**, type
**First Session**, and press **Return**. Fuzzel opens this guide in Foot.
Use **Space** to page down, **b** to go back, **/** to search, and **q** to
close the guide. From a shell or a recovery console, open the same file with:

    less /usr/share/doc/arche-workspace-defaults/first-session.md

Press **Alt+Return** to open a second terminal. Use **Alt+H** and
**Alt+L** to move between tiles to the left and right. The thin highlight
marks the focused window. Keep the guide open in one tile while you work in
the other.

## Build a two-pane work session

In the new terminal, run:

    tmux new-session -s practice

Press **Ctrl+B**, release both keys, then press **%**. The new pane opens on
the right. Press **Ctrl+H** to focus the left pane. On the first connected
launch, allow Neovim to finish downloading its plugins. Start an empty editor:

    nvim

Press **i**, type a short line, then press **Esc**. Type **:vsplit** and press
**Return**. You now have two views of the same buffer. In normal mode,
**Ctrl+L** moves right through the editor, then into the shell pane at the
outer edge. **Ctrl+H** takes you back. For a vertical stack the corresponding
keys are **Ctrl+J** (down) and **Ctrl+K** (up).

If the plugins have never been downloaded and you are offline, start
**nvim --clean** instead. You can practice typing and **:vsplit** immediately.
Use **Ctrl+W** followed by **h** or **l** between editor splits and **Ctrl+B**
followed by an arrow key between tmux panes in this mode.

To leave the unsaved practice buffer, press **Esc**, type **:qa!** and press
**Return**. To keep the tmux session in the background, press **Ctrl+B**, then
**d**. Return to it later with **tmux attach -t practice**. If a session named
practice already exists, attach to it instead of starting another.

## Give yourself a shortcut

Your copy of the Sway configuration lives at **~/.config/sway/config**.
Choose an unused chord. For example, the shipped configuration leaves
**Alt+F10** free. Add this binding to open Foot with it.

    bindsym $mod+F10 exec foot

Save the file, press **Alt+Shift+C** to reload Sway, then press
**Alt+F10** to try it. To undo the change, remove that line and reload.
For the file locations and validation command, see [Configuration files](configuration.html).

If you get stuck, open [Troubleshoot by symptom](troubleshooting.html). To learn more about the editor or file manager, see [Neovim, tmux and Yazi](editor-workspace.html).
