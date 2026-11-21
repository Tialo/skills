# Skills in Codex

| Term | Codex |
|---|---|
| explicit-only invocation | Set `policy.allow_implicit_invocation: false` in the skill's `agents/openai.yaml`. |
| project skills folder | `.agents/skills/<name>/SKILL.md` |
| shared project skills folder | `.agents/skills/<name>/SKILL.md` |
| personal skills folder | `~/.agents/skills/<name>/SKILL.md` |
| installed plugin copy | `~/.codex/plugins/cache/`. Never edit it. |
| external skill (`deslop`, `control-cli`, `control-ui`) | The skill of that name from the `cursor-vendored` plugin, which `setup-tstack` installs. |
| install external skills | If `codex plugin list` does not show `cursor-vendored@tialo` as installed, run `codex plugin add cursor-vendored@tialo`. If the sandbox blocks it, give the user that command. Copy [`agents/tstack-reader.toml`](agents/tstack-reader.toml) to `.codex/agents/tstack-reader.toml` in the project, keeping an existing one. Codex loads it only in a trusted project. Tell the user to trust tstack's hook in `/hooks` and start a new session. |
| skill-authoring tool | The built-in `$skill-creator`. |
