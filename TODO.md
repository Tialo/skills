* `tstack/README.md` says "ci fails while the generated copy is out of date", but this repo has no CI that runs `python3 scripts/generate-tstack-harness.py --check`
* add tstack to `.claude-plugin/marketplace.json` with `"source": "./harness/claude-code"`: docs now say `/plugin install tstack@tialo`, which does not resolve yet
* the author intro at the top of `tstack/README.md` still names poteto.
* remove notes about models speed
* make tstack claude first
* don't do cloud computations
* vendor deslop, control-ui, control-cli
* maybe add grill-me skill
* maybe add improve-codebase-architecture skill
* transcript paths in session-pickup, eval and recall still point to Cursor (`agent-transcripts/`, `~/.cursor/projects/*/`)
* right now this plugin is built around cursor ability to use different model vendors, which is not the case in codex/claude code
* fix recall for claude code architecture
* reflect should not edit local skills, but remote skills in Tialo/skills (or local, it should be configured by setup-tstack)
* make setup-tstack choose models for skills
