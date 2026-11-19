* no CI runs `python3 scripts/check-tstack.py` or `claude plugin validate --strict ./tstack`
* the author intro at the top of `tstack/README.md` still names poteto.
* reflect should not edit local skills, but remote skills in Tialo/skills (or local, it should be configured by setup-tstack)
* check that Cursor accepts `model: inherit` in `tialo-agent` and runs `tialo-agent` without a `model` parameter on the parent model
* `tstack/plugin.json` uses the agent-plugins schema. It was the generator's input, and nothing builds from it now. Keep or delete it. The version lives in three manifests.
* check the `agent_type` value Claude Code puts in hook input for the plugin agent `tstack:reader`; the read-only guard matches `tstack:reader` and `reader`
* Cursor install of tstack is untested: neither the team marketplace import of `.cursor-plugin/marketplace.json` nor the local `~/.cursor/plugins/local/tstack` copy. `/add-plugin tstack` needs a Cursor Marketplace listing
