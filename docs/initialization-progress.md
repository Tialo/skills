# tstack initialization progress

Track each skill as a whole, including its supporting files. Read [decisions](initialization-decisions.md) and inspect existing edits before resuming. Procedure: [initialization](initialization.md).

- **Source:** [`upstream.sha`](../upstream.sha); unchanged copies in `pstack/` and `pstack-upstream/`. The latter mirrors upstream paths for external support sources. The original checkout is `/private/tmp/tstack-upstream-20261116`; recreate it at the pinned SHA if needed.
- **Current skill:** `pstack/skills/principle-laziness-protocol/`.
- **Open decision:** adapt its two rules as proposed below, keep the original wording, or choose another treatment. The user's bookkeeping changes do not approve the proposed skill adaptation.
- **Next action:** resolve that decision, implement and check the agreed treatment, then continue to the next skill. No tstack skills are implemented yet.
- **Checks:** the 560-file pstack copy was verified against the pinned checkout, including permission bits. The 12 external source files were copied unchanged. Upstream generator `--check` passed in the external checkout. Claude Code and Cursor workflow checks have not run.
- **Coverage:** 58 plugin skills, three Benny automation skills, three external dependency skills, and the shared components below. Each skill row includes its entire directory. Generated upstream output is inspected through the generator when needed, without separate progress entries.

## Current proposal: Laziness Protocol

Proposed verdict: `adapt`. Destination: `tstack/skills/principle-laziness-protocol/SKILL.md`. Not yet agreed.

The source says to consolidate repeated decisions and pass their result as a simple flag, then minimize the diff. Proposed wording:

```markdown
# Laziness Protocol

- **Consolidate decisions.** Make each shared decision in one place and reuse the result. Choose the representation that fits the domain.
- **Minimize the diff.** Make the smallest change that fully solves the problem. Prefer straightforward code to boilerplate and unnecessary abstractions.
```

This keeps the principles without requiring a Boolean flag for every decision or making line count the only criterion. The skill has no supporting files or external dependencies. Its invocation metadata still needs host verification when adapting it. `poteto-mode` calls it for refactoring, diff sizing, and abstraction decisions.

## Plugin skills

Verdicts: `pending`, `keep`, `adapt`, `combine`, `replace`, `exclude`. Statuses: `pending`, `discussing`, `in-progress`, `blocked`, `done`. A row becomes `done` only after the agreed treatment of the whole skill or component is checked. Proposals remain `pending` verdicts.

| Upstream skill scope | Verdict | Destination | Changes and dependencies | Status |
| --- | --- | --- | --- | --- |
| `pstack/skills/principle-laziness-protocol/` | pending | Proposed: `tstack/skills/principle-laziness-protocol/` | Awaiting the proposal above; no target written | discussing |
| `pstack/skills/principle-attack-the-premise/` | pending | — | — | pending |
| `pstack/skills/principle-boundary-discipline/` | pending | — | — | pending |
| `pstack/skills/principle-build-the-lever/` | pending | — | — | pending |
| `pstack/skills/principle-encode-lessons-in-structure/` | pending | — | — | pending |
| `pstack/skills/principle-exhaust-the-design-space/` | pending | — | — | pending |
| `pstack/skills/principle-experience-first/` | pending | — | — | pending |
| `pstack/skills/principle-explain-the-number/` | pending | — | — | pending |
| `pstack/skills/principle-fix-root-causes/` | pending | — | — | pending |
| `pstack/skills/principle-foundational-thinking/` | pending | — | — | pending |
| `pstack/skills/principle-guard-the-context-window/` | pending | — | — | pending |
| `pstack/skills/principle-make-operations-idempotent/` | pending | — | — | pending |
| `pstack/skills/principle-migrate-callers-then-delete-legacy-apis/` | pending | — | — | pending |
| `pstack/skills/principle-minimize-reader-load/` | pending | — | — | pending |
| `pstack/skills/principle-model-the-domain/` | pending | — | — | pending |
| `pstack/skills/principle-never-block-on-the-human/` | pending | — | — | pending |
| `pstack/skills/principle-outcome-oriented-execution/` | pending | — | — | pending |
| `pstack/skills/principle-prove-it-works/` | pending | — | — | pending |
| `pstack/skills/principle-redesign-from-first-principles/` | pending | — | — | pending |
| `pstack/skills/principle-separate-before-serializing-shared-state/` | pending | — | — | pending |
| `pstack/skills/principle-sequence-verifiable-units/` | pending | — | — | pending |
| `pstack/skills/principle-subtract-before-you-add/` | pending | — | — | pending |
| `pstack/skills/principle-test-behavior-not-implementation/` | pending | — | — | pending |
| `pstack/skills/principle-type-system-discipline/` | pending | — | — | pending |
| `pstack/skills/architect/` | pending | — | — | pending |
| `pstack/skills/arena/` | pending | — | — | pending |
| `pstack/skills/automate-me/` | pending | — | — | pending |
| `pstack/skills/benchmark-checklist/` | pending | — | — | pending |
| `pstack/skills/blast-radius/` | pending | — | — | pending |
| `pstack/skills/bro/` | pending | — | — | pending |
| `pstack/skills/correct/` | pending | — | — | pending |
| `pstack/skills/create-formal-verification-skill/` | pending | — | — | pending |
| `pstack/skills/create-verification-skill/` | pending | — | — | pending |
| `pstack/skills/figure-it-out/` | pending | — | — | pending |
| `pstack/skills/how/` | pending | — | — | pending |
| `pstack/skills/in-your-own-words/` | pending | — | — | pending |
| `pstack/skills/interrogate/` | pending | — | — | pending |
| `pstack/skills/ketchup/` | pending | — | — | pending |
| `pstack/skills/ketchup-video/` | pending | — | — | pending |
| `pstack/skills/maintain-formal-verification-skill/` | pending | — | — | pending |
| `pstack/skills/maintain-verification-skill/` | pending | — | — | pending |
| `pstack/skills/make-bot-ui/` | pending | — | — | pending |
| `pstack/skills/no-comments/` | pending | — | — | pending |
| `pstack/skills/poteto-help/` | pending | — | — | pending |
| `pstack/skills/poteto-mode/` | pending | Intended entry point: `tstack/skills/tstack-mode/` | Review playbooks, references, Bun helpers, and tests together; resolve `deslop`, `control-cli`, `control-ui`, built-in `create-skill`, host tools, and model choices | pending |
| `pstack/skills/recall/` | pending | — | — | pending |
| `pstack/skills/reflect/` | pending | — | — | pending |
| `pstack/skills/setup-pstack/` | pending | — | — | pending |
| `pstack/skills/sharpen/` | pending | — | — | pending |
| `pstack/skills/show-me-your-work/` | pending | — | — | pending |
| `pstack/skills/statechart/` | pending | — | Include Node helpers, Java/TLC integration, tests, fixtures, and `fast-check` dependency | pending |
| `pstack/skills/swarm/` | pending | — | — | pending |
| `pstack/skills/tdd/` | pending | — | — | pending |
| `pstack/skills/teach/` | pending | — | — | pending |
| `pstack/skills/technical-writing/` | pending | — | — | pending |
| `pstack/skills/typescript-best-practices/` | pending | — | — | pending |
| `pstack/skills/unslop/` | pending | — | — | pending |
| `pstack/skills/why/` | pending | — | — | pending |

## Automation skills

| Upstream skill scope | Verdict | Destination | Changes and dependencies | Status |
| --- | --- | --- | --- | --- |
| `pstack/automations/benny/skills/reproduce-and-fix-issues/` | pending | — | Include references; resolve Cursor Automations capabilities with the shared Benny component | pending |
| `pstack/automations/benny/skills/setup-benny/` | pending | — | Include references; resolve Cursor Automations capabilities with the shared Benny component | pending |
| `pstack/automations/benny/skills/triage-issue-reports/` | pending | — | Include references; resolve Cursor Automations capabilities with the shared Benny component | pending |

## External dependency skills

Sources are copied under `pstack-upstream/<upstream path>`. Copying a dependency for review does not select it for tstack.

| Upstream skill scope | Verdict | Destination | Changes and dependencies | Status |
| --- | --- | --- | --- | --- |
| `cursor-team-kit/skills/deslop/` | pending | — | Referenced by `poteto-mode`; source inspected, retention unresolved | pending |
| `cursor-team-kit/skills/control-cli/` | pending | — | Referenced by `poteto-mode`; source inspected, retention unresolved | pending |
| `cursor-team-kit/skills/control-ui/` | pending | — | Referenced by `poteto-mode`; source inspected, retention unresolved | pending |

## Shared components

Paths here are upstream paths; external files are under `pstack-upstream/`. These rows cover source material outside skill directories.

| Component | Upstream scope | Verdict | Destination | Changes and dependencies | Status |
| --- | --- | --- | --- | --- | --- |
| Agent definitions | `pstack/agents/` | pending | `tstack/agents/` if retained | Review both agents and their callers | pending |
| User documentation | `pstack/README.md`, `pstack/docs/guide/` | pending | — | Include guide images; update for selected skills and hosts | pending |
| Host adapter | `pstack/docs/harness/claude-code.md` | pending | `tstack/docs/harness/cursor.md` | Claude-first direction already agreed; actual host mappings unresolved | pending |
| Plugin packaging | `pstack/plugin.json`, `pstack/.cursor-plugin/plugin.json`, `pstack/assets/`, `pstack/.gitignore` | pending | — | Claude source manifest, generated Cursor metadata, assets and ignore rules | pending |
| Licenses | `pstack/LICENSE`, `cursor-team-kit/LICENSE` | keep | `tstack/licenses/pstack-MIT.txt`; dependency notice if retained | Preserve original notices with retained material and generated output; not implemented yet | pending |
| Benny infrastructure | `pstack/automations/benny/README.md`, `pstack/automations/benny/FOR_AGENTS.md`, `pstack/automations/benny/templates/` | pending | — | Shared setup, automation prompts, and configuration for the three Benny skills | pending |
| Harness generator | `scripts/generate-pstack-harness-trees.mjs` | replace | `scripts/generate_cursor_plugin.py` | Python and reversed host direction agreed; implementation pending; upstream `--check` passed | pending |
| Documentation checks | `scripts/check-pstack-docs.mjs` | pending | — | Align routes, links, skill counts, and model references with retained components | pending |
| Package validation and CI | `scripts/validate-plugins.mjs`, `schemas/`, `.github/workflows/validate-plugins.yml` | pending | — | Shared upstream validator uses `ajv` and `ajv-formats`; CI also runs generation and skill tests; copied as review sources, not active CI | pending |
| Marketplace registration | `.claude-plugin/marketplace.json`, `.cursor-plugin/marketplace.json` | adapt | Same paths in this repository | Retain local marketplace `tialo`; route tstack to its Claude and generated Cursor packages when ready | pending |
