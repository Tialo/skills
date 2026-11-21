# Models in Cursor

- Detect: the slugs you can pass to `Task` in this session. If Cursor also exposes a models API or CLI that lists the user's models, prefer it for completeness. If you cannot detect any, ask the user to paste their slugs.
- Role value: a slug, such as `claude-opus-5-5-xhigh-fast`. The effort is the last token, or the one before a trailing `fast`. A Gemini entry stays at `high` when its role's target is `xhigh`.
- Harness options. Ask both once, and on a re-run show the current value.
  - `fast`: `on` uses the `-fast` slug of every model that has one. Fable and Gemini have none.
  - `cloud`: `on` runs swarm workers as cloud agents.
- Rule file: `.cursor/rules/tstack.mdc` in the project.

Shape, with the default roles, `fast: on`, and `cloud: on`. With `fast: off`, drop each `-fast`.

```
---
description: tstack configuration (roles, models, harness options)
alwaysApply: true
---
# tstack configuration, written by setup-tstack. Rerun it to change. A role with no line runs on the parent model.
harness: cursor
budget: large (xhigh)
fast: on
cloud: on
feature, refactoring: claude-opus-5-5-xhigh-fast
bug-fix: claude-opus-5-5-xhigh-fast
perf-issue: claude-opus-5-5-xhigh-fast
hillclimb: claude-opus-5-5-xhigh-fast
judgment and prose: claude-opus-5-5-xhigh-fast
arena runners: claude-fable-5-2-high, claude-opus-5-5-high-fast, gemini-4-neon-high
arena cross-judge pool: claude-opus-5-5-high-fast, gemini-4-neon-high
swarm workers: claude-opus-5-5-high-fast
interrogate reviewers: claude-fable-5-2-high, claude-opus-5-5-high-fast, gemini-4-neon-high
escalation: claude-fable-5-2-high
```
