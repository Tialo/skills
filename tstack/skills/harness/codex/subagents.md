# Subagents in Codex

| Term | Codex |
|---|---|
| spawn a subagent | `spawn_agent` with `fork_turns: "none"` and file paths in the brief. It returns at once. Call `wait_agent` when the next step needs the result. |
| general worker | `spawn_agent` with no `agent_type`. |
| `tialo-agent` | A general worker whose kickoff, after the line to read `worker.md`, tells it to read the [tialo-mode skill](../../tialo-mode/SKILL.md) in full by absolute path. |
| read-only subagent | `agent_type: "tstack-reader"`, which `setup-tstack` installs. Its hook allows only read-only shell commands, `view_image`, and web search, so it has no MCP. The hook runs only after the user trusts it in `/hooks`. |
| cloud worker | With a `cloud: <env id>` line in the tstack rule, push the starting branch and run `codex cloud exec --env <env id> --branch <branch> "<brief>"`. Follow the task with `codex cloud status <task id>`, read its result with `codex cloud diff <task id>`, and bring it into the checkout with `codex cloud apply <task id>`. With `cloud: off` or no rule, the worker is local and shares the parent's checkout, so give each parallel writer its own `git worktree` at the named commit and pass its absolute path. |
| a role's model | The value is `<model id> <effort>`, such as `gpt-6.2-sol xhigh`. Pass the id as `model` and the effort as `reasoning_effort`. With no role line, omit both. |
| one level up or down | Move `reasoning_effort` on `low` < `medium` < `high` < `xhigh`. |
| model family | The id's last word, such as `sol` in `gpt-6.2-sol`. |
| resume a subagent | `followup_task` to its id, or `send_message` to steer one still running. |
| stop a subagent | `interrupt_agent`. |
