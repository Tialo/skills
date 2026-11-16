# tstack initialization decisions

Important agreed decisions only. Current proposals, findings, checks, and status belong in [progress](initialization-progress.md). The process is defined in [initialization](initialization.md).

## Architecture and scope

- Author the personal plugin for Claude Code in `tstack/`, with `tstack-mode` as its main entry point. Generate the Cursor package in `harness/tstack/cursor/` with Python and a local host adapter.
- Use plugin identity `tstack`; preserve repository `Tialo/skills`, marketplace `tialo`, and applicable upstream and local attribution and licenses.
- Adapt `skills/report-upstream-issues/` and add Codex packaging in later, separate tasks.

## 2026-11-16 — Review and source tracking

- Review and track whole skills, including playbooks, references, helpers, tests, fixtures, and assets. Track shared infrastructure as coherent components. This replaces the initial per-file inventory and review granularity.
- Exclude automatically generated upstream harness output from progress. Review its canonical sources and generator instead.
- Keep only important accepted decisions here. Put proposals and operational details in progress; they are not accepted decisions.
- Keep unchanged `pstack/` and relevant external sources in root `pstack-upstream/` throughout initialization. The latter preserves upstream paths without overwriting the local marketplace or activating upstream CI.
- Create `upstream.sha` and root `CHANGELOG.md` at the start. The SHA pins the selected source; an explicit `Initialization in progress` entry distinguishes it from a completed baseline. This supersedes the earlier requirement to create both files only at finalization.
