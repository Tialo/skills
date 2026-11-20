# Skills in Codex

| Term | Codex |
|---|---|
| explicit-only invocation | Set `policy.allow_implicit_invocation: false` in the skill's `agents/openai.yaml`. |
| project skills folder | `.agents/skills/<name>/SKILL.md` |
| personal skills folder | `~/.agents/skills/<name>/SKILL.md` |
| installed plugin copy | `~/.codex/plugins/cache/`. Never edit it. |
| external skill (`deslop`, `control-cli`, `control-ui`) | `<name>/SKILL.md` in the project skills folder, which `setup-tstack` installs. Until it does, read `../claude-code/vendor/<name>.md` next to this file. |
| install external skills | For each of `deslop`, `control-cli`, and `control-ui`, copy `../claude-code/vendor/<name>.md` next to this file to `.agents/skills/<name>/SKILL.md` with an explicit-only `agents/openai.yaml` beside it, overwriting earlier copies. Copy [`agents/tstack-reader.toml`](agents/tstack-reader.toml) to `.codex/agents/tstack-reader.toml` in the project, keeping an existing one. Codex loads it only in a trusted project. Tell the user to trust tstack's hook in `/hooks` and start a new session. |
| skill-authoring tool | The built-in `$skill-creator`. |
