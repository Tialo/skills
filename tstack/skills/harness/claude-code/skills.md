# Skills in Claude Code

| Term | Claude Code |
|---|---|
| project skills folder | `.claude/skills/<name>/SKILL.md` |
| personal skills folder | `~/.claude/skills/<name>/SKILL.md` |
| installed plugin copy | `~/.claude/plugins/cache/`. Never edit it. |
| external skill (`deslop`, `control-cli`, `control-ui`) | `<name>/SKILL.md` in the project skills folder, which `setup-tstack` installs. Until it does, read `vendor/<name>.md` next to this file. |
| install external skills | For each of `deslop`, `control-cli`, and `control-ui`, copy `vendor/<name>.md` next to this file to `.claude/skills/<name>/SKILL.md`, overwriting earlier copies. |
| skill-authoring tool | Claude Code has no built-in one. Use a `skill-creator` skill when the session lists one. Check a skill with `claude plugin validate <skill folder>`. |
