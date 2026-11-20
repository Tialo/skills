# Interaction in Codex

| Term | Codex |
|---|---|
| todo list | `update_plan` when the session has it. Otherwise keep the steps and their status in your replies. |
| structured question | `request_user_input_async`. Each question has a `title` and optional `options`, and takes one answer. It adds free text itself. |
| repeat until a predicate holds | `create_goal` with the check in its `objective`. Codex keeps working on the goal until `update_goal` sets it `complete`. The user can start one with `/goal <objective>`. |
| wake on an event | `exec_command` with a command that exits on the event, polled with `write_stdin` while the turn runs. |
| show media to the user | In the app, embed images and link videos by absolute path. In the terminal, give each file's absolute path. |
| user command | `$tstack:<name>` |
| keep a skill on across turns | A selected skill stays in the thread until compaction drops it. After that, or for a new task, run the command again. |
