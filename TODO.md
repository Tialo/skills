* change links from harness/pstack to harness
* adapt `scripts/generate-pstack-harness-trees.py` to tstack: it is a 1:1 port of the upstream Node script and still reads `pstack/`, writes `harness/pstack/`, links to `github.com/cursor/plugins`, and expects a `Run another pstack skill` adapter row
* regenerate `harness/pstack/` from `tstack/`: it is still the upstream tree as is (pstack names, upstream manifests and links, and its README still says `node scripts/generate-pstack-harness-trees.mjs`)
* `tstack/README.md` says "ci fails while the generated copy is out of date", but this repo has no CI that runs `--check`
* add tstack to `.claude-plugin/marketplace.json`: docs now say `/plugin install tstack@tialo`, which does not resolve yet
