# Subagents in Claude Code

| Term | Claude Code |
|---|---|
| spawn a subagent | The `Agent` tool. Subagents run in the background and notify you when they finish. |
| general worker | `subagent_type: "general-purpose"` |
| `tialo-agent` | `subagent_type: "tstack:tialo-agent"` |
| read-only subagent | `subagent_type: "tstack:reader"`. It has only read tools, no MCP, and a hook allows only read-only shell commands. |
| cloud worker | Claude Code runs it locally with `isolation: "worktree"`. The worktree starts at HEAD without uncommitted changes, so commit or copy what the worker needs, and name the branch or commit to check out. |
| a role's model | The value is `<model id> <effort>`, such as `claude-opus-5-5 xhigh`. Pass the family word of the id as `model`, such as `opus` for `claude-opus-5-5`, and the effort as `effort`. With no role line, omit both. |
| one level up or down | Move `effort` on `low` < `medium` < `high` < `xhigh`. |
| model family | The family word of the id, which is `opus`, `sonnet`, `haiku`, or `fable`. |
| resume a subagent | `SendMessage` to its id or name. |
| stop a subagent | `TaskStop`. |
