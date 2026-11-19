* add tstack to `.claude-plugin/marketplace.json` with `"source": "./tstack"`: docs say `/plugin install tstack@tialo`, which does not resolve yet
* no CI runs `python3 scripts/check-tstack.py` or `claude plugin validate --strict ./tstack`
* the author intro at the top of `tstack/README.md` still names poteto.
* maybe add grill-me skill
* maybe add improve-codebase-architecture skill
* reflect should not edit local skills, but remote skills in Tialo/skills (or local, it should be configured by setup-tstack)
* check that Cursor accepts `model: inherit` in `tialo-agent` and runs `tialo-agent` without a `model` parameter on the parent model
* `tstack/plugin.json` uses the agent-plugins schema. It was the generator's input, and nothing builds from it now. Keep or delete it. The version lives in three manifests.
* check the `agent_type` value Claude Code puts in hook input for the plugin agent `tstack:reader`; the read-only guard matches `tstack:reader` and `reader`
* root `README.md`, `.claude-plugin/plugin.json` and the `tialo-skills` entry in `.claude-plugin/marketplace.json` still point at `skills/report-upstream-issues`, which moved to `tstack/skills/`. Its installs (Claude Code, Codex, `npx skills add`) are broken until they move to tstack.
