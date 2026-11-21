# Models in Codex

- Detect: the models are the `model` values in the `spawn_agent` schema, and the efforts are its `reasoning_effort` values. `codex debug models` lists more models than a subagent can run.
- Role value: `<model id> <effort>`, such as `gpt-6.2-sol xhigh`. The effort is the last token.
- Default roles: the newest `sol` model for the code roles, `judgment and prose`, and `swarm workers`. Panels take the newest model of up to three families, `sol` first. The cross-judge pool is the panel's models with `sol` last. `escalation` is the newest `astra` model, which the catalog calls the most capable.
- Harness options. Ask once, and on a re-run show the current value.
  - `cloud`: a Codex Cloud environment id, which `codex cloud` lists, or `off`. An id runs swarm workers as Codex Cloud tasks in that environment.
- Rule file: `.codex/tstack.md` in the project. Codex does not load it into a session, so read it whenever a step needs the tstack rule.

Shape, with the default roles and `cloud: off`:

```
# tstack configuration, written by setup-tstack. Rerun it to change. A role with no line runs on the parent model.
harness: codex
budget: large (xhigh)
cloud: off
feature, refactoring: gpt-6.2-sol xhigh
bug-fix: gpt-6.2-sol xhigh
perf-issue: gpt-6.2-sol xhigh
hillclimb: gpt-6.2-sol xhigh
judgment and prose: gpt-6.2-sol xhigh
arena runners: gpt-6.2-sol high, gpt-6.2-astra high, gpt-6.1-terra high
arena cross-judge pool: gpt-6.2-astra high, gpt-6.1-terra high, gpt-6.2-sol high
swarm workers: gpt-6.2-sol high
interrogate reviewers: gpt-6.2-sol high, gpt-6.2-astra high, gpt-6.1-terra high
escalation: gpt-6.2-astra high
```
