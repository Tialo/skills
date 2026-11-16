# Syncing tstack with pstack

Use this procedure to update an initialized tstack from `cursor/plugins`. For the first import, follow [Initializing tstack](initialization.md). This document defines the workflow; it does not record a completed import or sync.

tstack keeps its own editable instructions. An agent reads upstream changes, adapts them to tstack, checks the result, and completes ordinary updates locally. New skills and unresolved preference changes need the user's decision. Publishing, pushing, and merging branches require a separate instruction.

## State and source

The repository keeps two records:

- `upstream.sha` at the repository root contains the full `cursor/plugins` commit SHA from the last completed initialization or sync, followed by a newline. During first initialization it instead pins the selected source revision; an `Initialization in progress` CHANGELOG entry identifies that state.
- `CHANGELOG.md` at the repository root records meaningful local changes, upstream syncs, and the reasons for intentional differences.

After initialization there is no vendored pstack tree, submodule, patch queue, or separate mapping registry. Read upstream through GitHub or a temporary checkout outside this project. Do not fetch upstream history into this project's Git database. Temporary source material is not part of the deliverable.

After initialization, the SHA is a review boundary: every relevant change up to that point has been considered. It does not mean every upstream feature was adopted. The latest completed sync or initialization entry in CHANGELOG must agree with `upstream.sha`.

Track these upstream paths:

```text
pstack/**
scripts/generate-pstack-harness-trees.mjs
scripts/check-pstack-docs.mjs
scripts/validate-plugins.mjs
schemas/**
.github/workflows/validate-plugins.yml
.claude-plugin/marketplace.json
.cursor-plugin/marketplace.json
cursor-team-kit/skills/deslop/**
cursor-team-kit/skills/control-cli/**
cursor-team-kit/skills/control-ui/**
cursor-team-kit/LICENSE
harness/pstack/**
```

Shared marketplace, schema, validation, and CI files also serve other upstream plugins. Review their changes for their effect on tstack's sources, packaging, and dependencies. Generated harness output remains evidence of source or generator behavior, not a separate initialization progress item.

Inspect other upstream files when a tracked change depends on them. If upstream moves a tracked component or adds a required build dependency elsewhere, update the tracking scope and explain the change in CHANGELOG. Refresh the candidate list for the selected range before finalization so newly relevant commits are accounted for. A relocation must not make future updates disappear from the search.

## 1. Establish the baseline

Read `upstream.sha`, inspect the local working tree, and read relevant CHANGELOG entries before editing. Preserve unrelated local changes; isolate the sync if its edits would overlap with ongoing work.

Use CHANGELOG to reconstruct current intent:

- Find the initialization decisions and subsequent decisions about affected skills, workflows, and platform support.
- Follow recorded renames, replacements, splits, and combinations to their current files. Use local Git history when needed.
- A later explicit reversal supersedes an earlier decision. An unrelated later edit does not.
- A missing file alone does not establish that its removal was intentional. Investigate before skipping its upstream changes.
- Carry forward explicitly deferred work. It remains outstanding even after the review boundary advances.

If the SHA is absent or CHANGELOG still marks initialization in progress, initialization has not established a completed baseline. Resume [initialization](initialization.md) and its working records instead of starting a sync. If the SHA and CHANGELOG disagree, reconcile the interrupted or inconsistent state before starting another range. Do not invent a baseline from a version number or replace it with the latest upstream commit.

## 2. Select one bounded range

Resolve upstream `main` to a full SHA once at the start. Call the recorded baseline `BASE` and this fixed head `HEAD`. Keep `HEAD` fixed throughout the run, even if upstream advances.

Verify that `BASE` is available and lies on the first-parent history leading to `HEAD`. A missing commit or rewritten history requires an explicit recovery decision; leave the baseline unchanged while resolving it.

Enumerate first-parent commits in `BASE..HEAD`, oldest first. Compare each commit with its first parent and retain it if that diff touches any tracked path. Include additions, deletions, and both sides of renames. This counts changes as they entered `main`, without processing both a merge commit and the commits it brought in.

Use a complete, paginated history and complete diffs. If an API response omits or truncates a patch, obtain the full patch or file versions before making a decision. A temporary Git checkout is an alternative when API results are insufficient.

| Relevant commits | Action |
| --- | --- |
| None | Report that there is nothing new to sync. Leave SHA and CHANGELOG unchanged. Report any previously deferred work separately. |
| One through ten | Process the range through the fixed `HEAD`. No batch-size confirmation is needed. |
| More than ten | Show the count and propose the oldest ten relevant commits as the first batch. Obtain the user's choice before editing; they may choose a different range. |

An explicit target or batch size in the user's request takes precedence over these defaults. Resolve a requested target to a full SHA and apply the same ancestry and completeness checks. Do not ask again for an already specified range.

For a ten-commit batch, its target is the SHA of the tenth relevant first-parent commit. All relevant changes between `BASE` and that target belong to the batch, including changes to intentionally excluded skills. Do not filter those out before counting.

After completing an agreed partial batch, stop and report how many relevant commits remain relative to the captured `HEAD`. The user invokes sync again for the next batch. Do not silently continue into a second batch.

## 3. Adapt each commit

Read each selected commit's full tracked diff and enough surrounding source to understand the intended behavior. Inspect other files or the associated discussion if the diff leaves a dependency or rationale unclear. Compare the previous upstream version, the new version, and tstack's current implementation as needed.

Apply changes in integration order. Map behavior into tstack's current files rather than cherry-picking the monorepo commit wholesale. For each meaningful change, establish one outcome: adopted, adapted, rejected with a reason, or explicitly deferred by the user. A commit can contain several outcomes.

| Change | Agent action |
| --- | --- |
| Small, compatible correction | Apply it, verify it, and include it in the final summary at an appropriate level of detail. |
| New upstream skill | Explain its purpose and dependencies and ask whether the user wants it. Group related choices where practical. |
| Update to an explicitly removed or rejected skill | Skip that component according to CHANGELOG. Continue processing other changes in the same commit. |
| Rename or relocation | Trace the component to its current tstack counterpart; do not mistake a move for an unrelated new skill. |
| Removal of a retained upstream component | Check the reason, replacement, and local callers before adapting or proposing its removal in tstack. |
| Change conflicting with a recorded preference | Preserve the decision and adapt or reject the upstream change. Ask if a genuinely new tradeoff cannot be settled from the record. |
| Change to a shared dependency | Check affected callers, including workflows whose own files did not change. |

Do not repeatedly ask about a skill already explicitly excluded. Reconsider it when the user requests that, or when a new dependency or changed premise creates a material decision. Explain that dependency rather than silently restoring the skill.

A text merge is only a candidate. Read the resulting workflow for contradictions between the entry point, playbooks, leaf skills, and supporting instructions. For example, an upstream playbook can introduce a mandatory review that conflicts with a locally chosen review policy even when the changed lines do not overlap.

While waiting for a required decision, continue independent work in the selected batch. Do not finalize the batch with an unanswered decision. If the user chooses to defer the change, record its source commit, affected component, reason, and what would allow it to be revisited.

## 4. Preserve the Claude-first architecture

tstack's editable source uses Claude Code terminology. Upstream's Cursor-first structure is a source of improvements, not the target layout.

- Translate upstream tool names, agent parameters, model settings, paths, and skill calls into the corresponding Claude behavior.
- Adapt generator improvements from JavaScript into tstack's Python generator where relevant. A generator fix may concern packaging or validation rather than instruction wording.
- Keep the Claude-to-Cursor adapter consistent with changed source instructions.
- Inspect `harness/pstack/**` changes to understand their effect on the upstream Claude package. When they are generated consequences of a source or generator change, account for them once rather than applying the same change twice.
- Investigate changes made only to upstream generated files. If the behavior belongs in tstack, implement it in tstack's source, adapter, or generator and regenerate the Cursor package.

Edit generated tstack files only by running the generator. Regeneration must preserve tstack's selected skill set and intentional differences.

## 5. Verify and finalize

Before advancing the baseline:

1. Account for every relevant commit in the selected range. Rejected changes have reasons, and any deferred work has an explicit user decision and source reference.
2. Check affected skill metadata, routes, local references, supporting resources, and callers. Excluded skills must not leave unresolved dependencies.
3. Run appropriate checks for modified executable code. For changed skill behavior, use realistic task scenarios that exercise the changed decision or workflow; matching headings or wording is not behavioral validation.
4. Run the Python generator, then its `--check` mode. Inspect both the canonical Claude package and the generated Cursor package. When routing, tools, or packaging change, exercise the affected behavior in both hosts. Report a host check that could not be run as unverified; if it is needed to establish the changed behavior, leave the sync incomplete until it is run or the user accepts that limitation.
5. Review the final diff against the recorded preferences and the selected range. Update CHANGELOG and `upstream.sha` together in the same set of local changes, with the selected target as the new SHA.

Ordinary, fully checked updates need no additional final approval. Completion means the local files, generated output, SHA, and CHANGELOG agree. It does not implicitly authorize a commit, push, release, or branch merge.

If work is interrupted before finalization, keep the old SHA and identify the unfinished range. On resumption, inspect existing edits and any partial finalization before reapplying changes. Do not reset user work or claim the range is complete because some files were updated.

The final report names the processed range, meaningful changes, exclusions or deferrals, checks performed, and any remaining batch. State limitations alongside the affected result.

## Writing CHANGELOG entries

Keep dated entries newest first. Use full SHA links in completed initialization and sync entries. Group related edits by their effect rather than reproducing every commit message or file change.

For a sync, record:

- **Upstream range:** previous full SHA to the completed target, with commit or comparison links.
- **Changed:** useful behavior adopted or adapted, including renamed components where relevant.
- **Not adopted:** rejected additions or changes, with the reason or a reference to the still-applicable earlier decision.
- **Deferred:** only explicitly agreed unfinished work, with its source and revisit condition.

Omit empty sections. Group repeated changes to an excluded component; do not write a separate paragraph for every generated duplicate. A previously deferred item that is resolved should reference its original entry. When abandoning it, record the rejection reason.

Local, non-sync entries describe meaningful changes to behavior, skill membership, interfaces, architecture, or preferences. Record upstream and local component names when a rename, replacement, split, or combination would otherwise make future mapping unclear. Explain why an intentional difference exists and whether a new decision supersedes an earlier one. Pure formatting, typo fixes, and routine internal cleanup do not need individual entries unless they change meaning relevant to future syncs.

The initialization entry establishes the first baseline and explains the foundational differences described in [Initializing tstack](initialization.md). CHANGELOG is the decision record; the working skills and code remain the authoritative implementation.
