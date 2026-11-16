# Initializing tstack

Use this guide for the first adaptation of pstack into this repository. Subsequent updates follow [Syncing tstack with pstack](upstream-sync.md). These are instructions for future initialization, not a claim that the import or platform support is already complete.

tstack is a personal, Claude-first plugin with one main entry point, `tstack-mode`. Its skills can be rewritten, renamed, combined, replaced, or removed. During initialization, keep a temporary pstack source copy in this project and gradually populate tstack with files processed with the user. After initialization, maintain the upstream relationship through a commit SHA and meaningful CHANGELOG entries.

## Source and generated packages

Use this layout when implementing the initialization:

```text
tstack/                              Editable Claude Code plugin
  .claude-plugin/plugin.json
  skills/
    tstack-mode/SKILL.md
  agents/                            Retained and adapted agent definitions
  docs/harness/cursor.md              Claude-to-Cursor adapter
  licenses/pstack-MIT.txt             Upstream license notice
harness/tstack/cursor/                Generated Cursor plugin
scripts/generate_cursor_plugin.py    Python generator
upstream.sha                         Last completed upstream baseline
CHANGELOG.md                         Significant changes and decisions
docs/                                Repository maintenance guides
pstack/                              Temporary, unchanged upstream source
docs/initialization-decisions.md     Temporary adaptation decisions and lessons
docs/initialization-progress.md      Temporary per-file inventory and progress
```

Create other supporting directories only when retained components need them. Keep the generated package outside `tstack/`, so installing the primary plugin does not also install its generated counterpart.

Update the marketplace configuration to point Claude Code at `tstack/` and Cursor at `harness/tstack/cursor/`. Use `tstack` as the plugin identity and preserve the existing repository and marketplace identities unless the user asks to change them. Keep root maintenance documents separate from documentation that must ship with the plugin.

The existing `skills/report-upstream-issues/` skill stays in its current location unchanged during initialization. Its adaptation and integration into tstack are separate, later work and are not an initialization acceptance criterion.

## 1. Clone pstack and create the working records

Clone `cursor/plugins` into a temporary checkout outside this project, resolve `main` to a full SHA, and check out that revision. Copy the complete `pstack/` directory, including hidden files, into this project's root as `pstack/`. Keep that copy unchanged as the source for the whole initialization; put adapted files into `tstack/` only after the review below. Keep the upstream Git database outside this project.

Then create exactly two temporary Markdown working records in this project:

- `docs/initialization-decisions.md`: record agreed adaptation rules, user preferences, reasons for decisions, corrections, and lessons that later sessions must retain to avoid repeating mistakes. Reference affected upstream and local paths. When a decision changes, identify which earlier decision it supersedes.
- `docs/initialization-progress.md`: record the full selected upstream SHA and one row for every file in the copied `pstack/` tree, including hidden files. Each row contains the upstream path, verdict (`pending`, `keep`, `adapt`, `combine`, `replace`, or `exclude`), destination path or paths where applicable, agreed and actual changes, and processing status (`pending`, `discussing`, `in-progress`, `blocked`, or `done`). Link to the decision record when a rationale needs more detail. Above the table, identify the current file or agreed group, any unanswered question or blocker, and the next action.

Inventory skills, playbooks, principles, agents, references, executable helpers, assets, documentation, and automations at file level. Include binary and other non-Markdown files; looking at `SKILL.md` alone is insufficient. Inspect the upstream harness generator and its output, plus external dependencies needed by retained workflows, in the external checkout. Add relevant files outside `pstack/` to the same progress record using their upstream paths.

The source copy and these two records are working material, outside both installable packages. Keep them available across sessions until initialization is complete. At the start of every resumed session, read both records and inspect existing edits, then continue the current file or group. Reuse the recorded SHA and source copy. Write the completed baseline to `upstream.sha` only after the initialization checks pass.

Useful inspected starting references are the [upstream generator](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/scripts/generate-pstack-harness-trees.mjs), [Claude Code adapter](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/pstack/docs/harness/claude-code.md), and [harness description](https://github.com/cursor/plugins/blob/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7/harness/pstack/README.md). They document the version examined during planning. Inspect the chosen initialization revision again instead of assuming those files or host APIs are unchanged.

## 2. Discuss and process one file at a time

Work through the progress inventory sequentially. For each file:

1. Read it and enough surrounding context to explain what it does, its notable behavior and assumptions, dependencies, and host-specific details. Explain these to the user, including consequences of retaining or excluding it.
2. Discuss whether it belongs in tstack and what should change. Propose a verdict and destination, and wait for the user's decision before adapting or excluding it. If the decision is already explicit in the conversation or working records, apply it without asking again.
3. Record the decision and its rationale in the working records. Apply the agreed changes to the destination in `tstack/`, or record the agreed exclusion. Leave the source copy intact. Handle routine implementation details within the agreed scope; return to the user if a new choice is needed.
4. Check the result and update the progress row with the actual changes and status. Mark a retained file `done` only when its agreed adaptation is implemented and checked; mark an excluded file `done` when its exclusion and rationale are recorded. Track unresolved dependencies as blockers rather than claiming the file is ready.

Keep one file active until its decision and processing are complete. While waiting for an answer, stay on that file; do not begin discussing or adapting the next one. Closely coupled files may be handled together when a coherent decision requires it: explain the connection, agree the group with the user, and keep a separate inventory row for every file. Finish that group before moving on. If a dependency prevents completion, discuss expanding the current group with the user.

Update both records as decisions are made and work progresses, so another session can resume without repeating settled questions or mistakes. The implementation requirements in sections 3–5 apply to the files retained through this review; they do not authorize a bulk import ahead of the user's decisions. tstack grows as files are processed.

The lasting record is the resulting plugin plus a concise initialization CHANGELOG entry. At finalization, transfer enduring decisions from the temporary records into that entry and the relevant maintained instructions.

Keep enough provenance in that entry to reconstruct intentional differences:

- Name upstream and local components for renames, combinations, splits, and replacements.
- Name deliberately excluded skills or groups and explain the reason.
- Explain meaningful workflow changes, especially autonomy, delegation, verification, and model-selection choices.
- Identify external capabilities that are retained, replaced, or unavailable in the initial target hosts.

Preserve necessary resources and dependency code when retaining a skill. If a workflow depends on a skill from another plugin or a host-specific service, choose an available dependency, a local replacement, or an explicit exclusion. Do not leave a mandatory step pointing at a missing capability.

Retain upstream attribution and license notices with adapted material, and include those notices in the generated package. Preserve the licensing and attribution of existing local material as well.

## 3. Make Claude Code the primary implementation

Author the editable skills, agent definitions, playbooks, and supporting instructions in Claude Code terminology. Adapt tool calls, agent options, namespaced skill calls, model roles, configuration locations, and transcript paths. Check the actual host interfaces rather than treating a historical tool name or model identifier as permanent.

Use upstream's Claude adapter as evidence about intent, then write native Claude instructions. Resolve duplicated or contradictory instructions during the conversion instead of making Claude users mentally apply an inverse adapter to every skill.

Separate genuine configuration, such as chosen models for roles, from workflow prose where it improves maintainability. Keep the configuration small. Arbitrary behavioral customization belongs in the editable skills rather than in a general-purpose Markdown transformation language.

Build `tstack-mode` from the selected workflows and the user's decisions. It should provide the main route into the plugin and load detailed instructions when relevant. Update all callers when a skill is renamed, combined, or removed. Confirm that the entry point can reach every intended workflow without referring to the old plugin namespace.

Document how the user invokes the entry point in each host. Choose and verify invocation metadata for the actual hosts during initialization; copying a field from one host does not prove the other host honors it.

## 4. Document the Claude-to-Cursor adapter

Create `tstack/docs/harness/cursor.md` as shipped runtime guidance for Cursor. Cover only distinctions that affect execution:

- Tool names and calls, such as agent spawning and user questions.
- Agent types, supported parameters, execution context, and background behavior.
- Model and reasoning choices, including inheritance where supported.
- Skill routing, command namespaces, and local resource lookup.
- Configuration, plugin, workspace, and transcript paths.
- Capabilities without an equivalent and the explicitly chosen alternative or limitation.

Design the mapping by behavior. An upstream translation from a Cursor cloud agent into a Claude worktree does not imply that every Claude worktree should become a Cursor cloud agent. Several source operations may map to one target operation, and the reverse may need a different decision.

Give Cursor a clear pointer to this adapter before following affected skills. Make it reachable through direct leaf-skill invocation as well as through `tstack-mode`. Keep required instructions and resources local to the installed package.

## 5. Generate the Cursor package with Python

Implement `scripts/generate_cursor_plugin.py` as a deterministic packaging script. The upstream generator's useful pattern is copying the required tree and adding adapter pointers, rather than rewriting every sentence. Follow that pattern with Claude source and Cursor output.

The generator should:

- Read only canonical tstack inputs and generate the Cursor plugin metadata and required package contents.
- Add the adapter pointer to affected skill entry points without accumulating duplicate wrappers on repeated runs.
- Preserve required references, scripts, assets, license notices, and executable permissions.
- Keep links valid inside the installed package. A required runtime instruction cannot be replaced by a link to unpinned upstream `main`.
- Detect missing resources, invalid skill metadata, unresolved packaged references, and known platform terms lacking an adapter mapping.
- Produce stable output for identical inputs and remove stale generated files only inside its owned output directory.
- Support `--check`, which compares expected contents and executable flags with the committed output, reports drift, returns failure on a mismatch, and writes nothing.

Generate from canonical inputs every time. Do not take the previous generated package as the source or accept hand edits in it. Keep the generated Cursor tree in Git so it can be installed directly and reviewed alongside its source changes.

Document the normal build and check commands:

```bash
python3 scripts/generate_cursor_plugin.py
python3 scripts/generate_cursor_plugin.py --check
```

The Python requirement applies to this generator. Retained upstream utilities may continue to use their existing runtimes where appropriate; assess their dependencies during the component audit.

## 6. Validate and establish the first baseline

Before marking initialization complete:

1. Reconcile the progress inventory with the pinned source: every upstream file has an agreed verdict and a completed processing status, with exclusions and behavioral choices explained. Confirm that `skills/report-upstream-issues/` remains unchanged and its later adaptation is recorded as deferred work.
2. Validate skill metadata, the entry point's routes, supporting references, dependency closure, and each package's manifest and install location.
3. Run appropriate checks for retained or modified scripts, including the generator's repeatability, stale-file cleanup, resource preservation, and non-mutating `--check` behavior.
4. Install and exercise representative workflows in Claude Code and Cursor. Include the main entry point, direct invocation of a platform-sensitive leaf skill, a changed behavioral decision, and any retained workflow that delegates to an agent. Verify actual tool usage and results, not just generated text.
5. Confirm that neither installed package contains a duplicate alternate package or unadapted upstream skill tree. Record any incomplete host checks as limitations rather than claiming compatibility from static checks alone.
6. Once required checks pass, write `upstream.sha` and the initialization CHANGELOG entry together. Preserve enduring decisions, corrections, and lessons from the working records in CHANGELOG or the relevant maintained instructions. Then remove the temporary `pstack/` copy and the two temporary Markdown records. The completed project retains no original pstack tree or permanent mapping registry. Do not mark a partially audited import complete.

The initialization entry records the date and full upstream SHA, Claude-first source architecture, Python-based Cursor generation, the principal changes to skill membership and behavior, and reasons for those differences. Include provenance for renamed or replaced components and any deliberately deferred work. A long list of unchanged copied files is unnecessary.

Update installation and development instructions to match the resulting packages. After initialization, use the [sync procedure](upstream-sync.md) for upstream updates and the same CHANGELOG for meaningful local evolution.

## Later: adapt the existing local skill

Adapt and integrate `skills/report-upstream-issues/` in a separate task after initialization. Review its behavior and the desired integration with the user then, preserving its local intent rather than replacing it with an upstream alternative. Record the resulting changes in CHANGELOG.

## Later: a Codex package

Plan a separate Python generator for a Codex package derived from the same canonical Claude plugin, with its own host adapter and compatibility checks. Do not derive Codex from the generated Cursor tree or maintain a second hand-edited set of skill bodies.

Codex packaging is a future addition, not an acceptance criterion for the initial Claude and Cursor implementation. Its generator, output location, metadata, and host mappings should be implemented against the Codex interfaces available at that time and recorded as a separate CHANGELOG decision.
