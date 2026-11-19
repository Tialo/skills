# Models in Claude Code

- Detect: the families are the `model` values in the `Agent` tool schema, and the efforts are its `effort` values. Take each family's version from the model ids the system prompt lists, such as `claude-opus-5-5`. Ask the user for any id you cannot find there.
- Role value: `<model id> <effort>`, such as `claude-opus-5-5 xhigh`. The effort is the last token.
- Harness options. Ask once, and on a re-run show the current value. Claude Code has no per-subagent fast mode, so never ask about one.
  - `fable`: whether tstack may use Fable models. Tell the user that on the Pro plan Fable runs only on usage credits. `off` replaces each Fable entry with the detected Opus id at the same effort, drops an entry that would repeat a model already in its list, and drops the `escalation` line.
- Rule file: `.claude/rules/tstack.md` in the project, with no frontmatter. Claude Code loads it into each new session in this project.

Shape, with the default roles and `fable: on`:

```
# tstack configuration, written by setup-tstack. Rerun it to change. A role with no line runs on the parent model.
harness: claude-code
budget: large (xhigh)
fable: on
feature, refactoring: claude-opus-5-5 xhigh
bug-fix: claude-opus-5-5 xhigh
perf-issue: claude-opus-5-5 xhigh
hillclimb: claude-opus-5-5 xhigh
judgment and prose: claude-opus-5-5 xhigh
arena runners: claude-fable-5-2 high, claude-opus-5-5 high, claude-sonnet-5-5 high
arena cross-judge pool: claude-opus-5-5 high, claude-sonnet-5-5 high
swarm workers: claude-opus-5-5 high
interrogate reviewers: claude-fable-5-2 high, claude-opus-5-5 high, claude-sonnet-5-5 high
escalation: claude-fable-5-2 high
```
