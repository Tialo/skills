# Interaction in Cursor

| Term | Cursor |
|---|---|
| todo list | Use the agent's to-do list to track each step. |
| structured question | `AskQuestion`, with `allow_multiple: true` for several answers. |
| repeat until a predicate holds | Cursor's `/loop` command. |
| wake on an event | A watcher subagent that wakes you on the event, with a long time-based heartbeat as fallback. |
| show media to the user | Embed screenshots and videos inline in the reply. |
| user command | `/<name>` |
| keep a skill on across turns | Pick the skill from the `/` menu with Option+Enter (Mac) or Alt+Enter (Windows), or Use as Mode from its entry. That makes it a Custom Mode, which stays in context every turn until the user exits it. Enter attaches it to one message only. Cursor's docs at https://cursor.com/docs/skills list Custom Modes in the Agents Window and the CLI. |
