# The Zsh workspace

| What you want to do | How to use it |
| --- | --- |
| Accept a suggestion from command history | Press Right at the end of the command. Syntax highlighting colors the command as you type. |
| Find an earlier command | Type a fragment and press Up or Down. With fzf installed, Ctrl+R opens fuzzy history search. |
| Complete a package, path or Git branch | Press Tab. With fzf installed, fzf-tab lets you filter the matches. Arch’s zsh-completions package supplies additional completions. |
| Work with Git or pacman | `gst` shows Git status. Run `alias pacin` to see the pacman install shortcut before using it. |
| Edit a command to run with sudo | Press Esc twice. At an empty prompt this recalls the previous command and adds `sudo`. Review it before pressing Enter. |
| Unpack an archive or read a manual | Use `extract FILE`, or `man COMMAND` for a colored manual page in a supported pager. |

For paired brackets and quotes, add `autopair` to `plugins=(...)` in `~/.zshrc`. Add `you-should-use` for reminders about existing aliases. Oh My Zsh also ships integrations such as `docker`, `kubectl` and `vi-mode`. Run `omz plugin list` for the installed catalog. The installed zoxide and direnv integrations also load automatically when you select those tools. Open a new terminal after editing your plugin list.
