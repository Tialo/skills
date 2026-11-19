# Subagents in Cursor

| Term | Cursor |
|---|---|
| spawn a subagent | The `Task` tool with `run_in_background: true`. |
| general worker | `subagent_type: "generalPurpose"` |
| `tialo-agent` | `subagent_type: "tialo-agent"` |
| read-only subagent | `readonly: true`. It strips MCP, so a worker that needs MCP runs in agent mode. |
| cloud worker | With `cloud: on` in the tstack rule, `environment: "cloud"`, plus `cloud_base_branch` for a non-default pushed branch. Use `environment: "local"` when the worker needs something on the user's computer. With `cloud: off` or no rule, `environment: "local"`. |
| a role's model | Pass the role's slug as `model`. With no role line, omit `model`. |
| one level up or down | Move the slug's effort token on `low` < `medium` < `high` < `xhigh`, and keep a trailing `-fast`. Gemini stays at `high` or below. |
| model family | The vendor, which is the slug's text before the first hyphen after dropping a leading `cursor-`. Fable counts as `claude`. |
| resume a subagent | `resume` |
