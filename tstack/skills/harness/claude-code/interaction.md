# Interaction in Claude Code

| Term | Claude Code |
|---|---|
| todo list | Use the task list tools to create and update steps. |
| structured question | `AskUserQuestion`, with 1-4 questions, 2-4 options each, a `header` of at most 12 characters, `multiSelect` for several answers. It adds "Other" itself. In `-p` mode it is absent, so ask in plain text. |
| repeat until a predicate holds | The built-in `/loop` command, with an interval or self-paced. |
| wake on an event | The `Monitor` tool, or a background `Bash` command that exits on the event, which notifies you. Keep a long `/loop` heartbeat as fallback. |
| show media to the user | The terminal shows no images or video. Give each file's absolute path. |
| user command | `/tstack:<name>` |
| keep a skill on across turns | A loaded skill stays in the conversation until compaction drops it. After that, or for a new task, run the command again. |
