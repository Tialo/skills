* change links from harness/pstack to harness
* add python script to create claude harness folder like in upstream (upstream `scripts/generate-pstack-harness-trees.mjs` is copied as is; it still reads `pstack/`, writes `harness/pstack/` and links to `github.com/cursor/plugins`)
* regenerate `harness/pstack/` from `tstack/`: it is still the upstream tree as is (pstack names, upstream manifests and links)
* add tstack to `.claude-plugin/marketplace.json`: docs now say `/plugin install tstack@tialo`, which does not resolve yet
