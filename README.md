# Tialo's skills

Agent skills for Claude Code, Codex and other coding agents.

## Skills

### [`report-upstream-issues`](skills/report-upstream-issues/SKILL.md)

When an agent hits a bug, a docs mismatch or a missing feature in a dependency, it usually works around it silently. Your code gets a little uglier, and the maintainers and everyone else who hits the same problem learn nothing. With this skill the agent still writes the workaround, but it also:

1. **Checks upstream.** It looks through the changelog, the code, open and closed issues, and open and merged PRs to find out whether the authors already know about the problem or have fixed it. The search runs in a fresh-context subagent, so your task's context stays clean.
2. **Marks the workaround** with a removal condition you can `grep` for, e.g. `TODO(upstream): remove when foo >= 2.3. <why>`.
3. **Checks on the latest release, cheaply.** It only does this when the latest release can be tried with no build from source, no install scripts, a small download and an isolated temp directory. Anything beyond that waits for your approval.
4. **Tells you, when the task is done.** For each problem: what it is, whether the authors know, what was done in your code, and whether an upgrade would remove the workaround.
5. **Offers issue drafts** (or comment drafts with new evidence). The drafts follow the project's contributing guide, disclose that an AI agent wrote them, and are never posted for you. Possible security issues get a warning and a summary of the project's private disclosure procedure instead.

## Install

Pick one install method per agent.

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add Tialo/skills
claude plugin install tialo-skills@tialo
```

Update with `claude plugin marketplace update tialo`, then `claude plugin update tialo-skills@tialo`.

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add Tialo/skills
codex plugin add tialo-skills@tialo
```

Update with `codex plugin marketplace upgrade tialo`.

</details>

<details>
<summary><strong>Other agents</strong> (Cursor, Copilot, Gemini CLI, OpenCode, ...)</summary>

Use [Vercel's `skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add Tialo/skills --skill report-upstream-issues
```

</details>

### Optional: make it fire more reliably

The skill triggers from its description. To make it harder to skip, add this line to your `AGENTS.md` or `CLAUDE.md`:

```markdown
When a third-party dependency misbehaves and you are about to work around it, use the report-upstream-issues skill first.
```
