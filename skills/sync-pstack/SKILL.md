---
name: sync-pstack
description: Use when syncing tstack with upstream pstack in Tialo/skills.
---

# Sync pstack

Follow upstream by default. Keep the smallest diff that preserves a deliberate tstack decision.

## Scope the sync

Create a sync branch from the current HEAD and record the starting commit. In `cursor/plugins`, review the commits and net diff from `upstream.sha` to the target (fetched `main` for latest). Scope both to `pstack/` and `scripts/generate-pstack-harness-trees.mjs`.

Follow renames. Skip locally removed components once history confirms the removal was deliberate. Survey the full range before asking. Keep revisions, paths and open questions in a note outside the repo so the sync can resume on the same branch.

## Resolve differences

Compare pinned pstack with pre-sync tstack. Check later revisions, reverts and related rules for the local intent. Take upstream verbatim when it already satisfies that intent.

Discuss skill additions, removals of retained skills and conflicts with local decisions before applying them. Ask one question at a time, starting with choices that affect later ones.

1. Explain the prior local change and its purpose. Cite the commit or changelog entry. Say when the passage matched upstream or the reason is unknown.
2. Show two diffs of the same passage. Label them **Upstream** (pin to target) and **Proposed tstack** (current to proposed).
3. Recommend one outcome and explain its effect. Apply the answer to that decision and revise the remaining questions.

## Apply and verify

Update callers, playbooks and guides in the same step. Leave harness generation out of the diff. Check verbatim imports byte for byte and compare adaptations with the target. The user reviews and commits each step unless they delegate commits.

In `CHANGELOG.md`, add one short bullet per local decision first introduced in this sync. Carrying an existing decision into a new passage needs no entry. Cite the implementing commit in chat, or show the pending diff before commit.

For a sync to latest, fetch `main` again and review any extra range. Account for every affected path, check references and run `git diff --check` against the starting commit. Write the full reviewed SHA to `upstream.sha` last.
