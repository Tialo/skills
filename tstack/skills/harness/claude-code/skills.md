# Skills in Claude Code

| Term | Claude Code |
|---|---|
| explicit-only invocation | Set `disable-model-invocation: true` in the skill frontmatter. |
| project skills folder | `.claude/skills/<name>/SKILL.md` |
| shared project skills folder | `.agents/skills/<name>/SKILL.md`. Claude Code does not load that folder, so also symlink `.claude/skills/<name>` to `../../.agents/skills/<name>`. |
| personal skills folder | `~/.claude/skills/<name>/SKILL.md` |
| installed plugin copy | `~/.claude/plugins/cache/`. Never edit it. |
| external skill (`deslop`, `control-cli`, `control-ui`) | The `cursor-vendored:<name>` skill. tstack declares the `cursor-vendored` plugin as a dependency, so it installs with tstack. |
| install external skills | Install nothing. |
| skill-authoring tool | Claude Code has no built-in one. Use a `skill-creator` skill when the session lists one. Check a skill with `claude plugin validate <skill folder>`. |
