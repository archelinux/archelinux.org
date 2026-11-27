# Work with coding agents

Filter **Arche software** for **agent workflows**. At a terminal, install the same tools using the [pacman workflow](rolling-updates.html). Use your coding agent's own sign-in and model setup. Selecting a workflow tool installs the tool itself.

| Tool | Where it fits |
| --- | --- |
| Worktrunk (`wt`) | Give each task a separate Git checkout. |
| Herdr | Manage multiple agent terminals and see which ones need input. |
| lazyagents | Browse and resume sessions or manage skills across agents. |
| Difftastic (`difft`) | Review syntax-aware diffs. |
| Playwright | Run browser tests. Set up browsers in the project when needed. |
| OpenSpec | Keep acceptance criteria and planned changes with the code. |
| Beads (`bd`) | Track work and dependencies in the project. |
| ccusage | Read local usage logs to estimate the cost of a run. |

## Take one task from plan to review

1. Start in a Git repository. Use `wt switch --create fix-navbar` to open a separate checkout for the task. This gives the task its own files and Git branch. Filesystem permissions are controlled by your agent's sandbox.
2. Start your agent in that directory. Use Herdr or tmux if you want to leave the session open while working elsewhere.
3. Give the agent the acceptance criteria and the project's test command. For longer changes, initialize OpenSpec or Beads when the project has chosen to use it.
4. Review the changes yourself. For unstaged edits, use `GIT_EXTERNAL_DIFF=difft git diff`. Run the project's tests and keep the result with the review.
5. Use lazyagents to find a previous session. Run `ccusage daily` to see usage recorded in local logs.

For a project that declares Playwright, run the project's pinned `npx playwright test` and follow its browser setup. For running local models, see [Local inference](maintenance.html).
