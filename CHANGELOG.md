# Changelog

## 2026-11-16 — Initialization in progress

Selected upstream revision: [`bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7`](https://github.com/cursor/plugins/commit/bf0c7cd80abdbf7fe47b634978a7d1b4071f71a7). `upstream.sha` pins this source revision; the adaptation audit and host validation are not complete.

- Prepared unchanged `pstack/` and `pstack-upstream/` source copies for review, including packaging tools, validation sources, marketplace configuration, and the `deslop`, `control-cli`, and `control-ui` dependencies from `cursor-team-kit`.
- Track progress by whole skill, including its supporting files; track shared infrastructure as components. Generated upstream harness output has no separate progress entries. Keep only important agreed decisions in the temporary decision record.
- Target architecture: editable Claude Code plugin in `tstack/`, entered through `tstack-mode`, with a Python-generated Cursor package in `harness/tstack/cursor/`. Preserve repository `Tialo/skills` and marketplace `tialo`.
- Deferred: adaptation of the existing `skills/report-upstream-issues/` skill and Codex packaging.

No tstack skills have been implemented yet. Finalize this entry after the agreed adaptations and required checks pass.
