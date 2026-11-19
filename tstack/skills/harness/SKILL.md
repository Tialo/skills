---
name: harness
description: Maps the harness-neutral terms in tstack skills to the current harness. Read a topic when a tstack skill marks a step with (harness: <topic>).
disable-model-invocation: true
---

# Harness

tstack skills use harness-neutral terms. A step marked `(harness: <topic>)` uses a term that needs the current harness's meaning. Read `<harness>/<topic>.md` next to this file once per session, before that step. Read only the topics your steps mark.

## Find the harness

The `harness:` line of the tstack rule in your context names it. With no rule, tell the harness by its subagent tool. `Agent` means `claude-code`, and `Task` means `cursor`. Any other harness has no folder here, so map each term yourself.

## Terms

| Term | Topic |
|---|---|
| spawn a subagent, general worker, `tialo-agent`, read-only subagent, cloud worker, a role's model, one level up or down, model family, resume or stop a subagent | `subagents` |
| structured question, repeat until a predicate holds, wake on an event, show media to the user, user command, keep a skill on across turns | `interaction` |
| this workspace's transcripts, current session, subagent transcripts | `transcripts` |
| project skills folder, personal skills folder, installed plugin copy, skill-authoring tool, external skill, install external skills | `skills` |
| detect models, role value, default roles, rule file, harness options | `models` |

## Roles

The tstack rule maps each role, with the labels tialo-mode uses, to a model in the harness's format. A role with no line, or no rule at all, runs on the parent model.
