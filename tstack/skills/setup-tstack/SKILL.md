---
name: setup-tstack
description: Configure which models tstack uses per role, at what reasoning budget, and with which harness options. Detects your available models and writes a project rule that overrides the skill defaults. Use for /setup-tstack, "configure tstack models", "tstack budget", or changing tstack's model choices.
---

# Setup tstack

Write the project's tstack rule: the harness, the budget, the harness options, and a model per role. Read the `models` topic first (harness: models). It gives the detection method, the role value format, the default roles, the harness options, and the rule file.

Roles, with the labels tialo-mode uses:

- `feature, refactoring`, `bug-fix`, `perf-issue`, `hillclimb`: the code delegates of those playbooks.
- `judgment and prose`: prose and judgment.
- `arena runners`, `interrogate reviewers`: review and design panels, one subagent per entry.
- `arena cross-judge pool`: the arena judge, in order of preference.
- `swarm workers`: swarm workers, verification, and trivial mechanical edits.
- `escalation`: runs outside a panel only when the user names it for the task or two runs of the same brief on the role's own model failed its check.

## Steps

### 1. Detect available models

Detect the models the topic names. Never write a model you have not confirmed is available.

### 2. Load current state

If the project's tstack rule exists, read it and treat its budget, options, and role values as the current choices. Otherwise start from the topic's default roles. Drop a line whose role is not in the list above, and tell the user.

### 3. Budget, options, map, and confirm

**(a) Ask for a budget and the harness options.** Ask in one structured question round (harness: interaction). Offer these three budgets with these exact labels, and name the current budget when the rule records one. With no rule, say that `large` matches the defaults.

- `large — xhigh reasoning`
- `medium — high reasoning`
- `small — medium reasoning`

Add one question per harness option the topic lists.

**(b) Apply them.** Build the working table from the defaults, and on a re-run keep any role the user changed. Each role has a target effort, which is its default's effort moved by the budget. `large` keeps it, `medium` lowers it one step, and `small` lowers it two steps, on the ladder `xhigh` > `high` > `medium` > `low`. No role runs above `xhigh`, and a target at the bottom of the ladder stays there. Set the effort of every model in the role, panel entries included, to the role's target, in the topic's value format. If the result is not detected, use the same model with the highest detected effort at or below the target, else mark the role as needing a choice. Apply the options as the topic says. On a re-run, when a newer version of a role's model is detected, offer to move the role to it.

**(c) Show the roles and confirm.** Show every role with its value, marking any value not detected as needing a choice, and list each line step 2 dropped. Ask whether to accept as-is or change specific roles, in a structured question. Offer the detected models at `xhigh` or below, plus no line, which runs the role on the parent model. `arena runners` and `interrogate reviewers` are lists, so their length sets the count. `arena cross-judge pool` is also a list, but Arena runs one judge, the first entry whose model family differs from the parent's (harness: subagents), so order it by preference. `swarm workers` is the default model for every worker unless a race or comparison assigns another model per arm.

### 4. Validate

Every model written must be detected and at `xhigh` or below. If a chosen model is not available, stop and ask again.

### 5. Write the rule

Write the rule file in the topic's shape: the header comment, the `harness` line, the `budget` line with the chosen label and the effort it names, one line per harness option, and one line per role. Replace the previous tstack rule at the location the topic specifies.

### 6. Install external skills

Install the external skills tstack uses (harness: skills).

### 7. Confirm

Tell the user the rule was written, which external skills were installed, and that both apply to new sessions in this project. Re-running this skill updates it.

### 8. Offer a verification skill (optional)

Check whether the project has a way to drive the real app for proof (a `verify-*` skill, or an existing harness). If not, offer once: "want a project-local verification skill, so agents can drive the app the way a user does and prove changes work? I can generate one with /create-verification-skill." On yes, read [`../create-verification-skill/SKILL.md`](../create-verification-skill/SKILL.md) and follow it. On no, move on without pushing.

### 9. Offer a formal verification skill (optional)

Check whether the project already has a formal verification skill (a project skill that runs a model checker, a proof, or another verifier against the code). If not, offer once: "want a formal verification skill, so agents can prove a key property of your code holds in every case in scope, not only the cases tests reach? I can generate one with /create-formal-verification-skill." On yes, read [`../create-formal-verification-skill/SKILL.md`](../create-formal-verification-skill/SKILL.md) and follow it. On no, move on without pushing.
