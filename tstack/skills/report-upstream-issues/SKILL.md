---
name: report-upstream-issues
description: "Use when you are about to work around a third-party dependency (library, CLI, runtime, base image, CI action, SaaS API or SDK) that misbehaves, contradicts its docs, or lacks something: patching, pinning or downgrading, casting or suppressing type/lint errors, adding retries or sleeps, monkeypatching, or rewriting code to avoid an API. Checks whether upstream already knows or fixed it, marks the workaround with a removal TODO, and reports to the user. Also use when the user asks to draft an upstream issue or continue investigating a dependency bug."
disable-model-invocation: true
---

# Report Upstream Issues

A silent workaround fixes a dependency problem for one project and hides it from everyone else who hits it. This skill keeps your fix local but makes the knowledge travel: find out what upstream already knows, label the workaround so someone can remove it later, and tell the user what you found so they can report it.

The user's task still comes first. This skill adds a short detour when you hit the problem and a report when the task is done.

## Where are you?

| Moment | Go to |
|---|---|
| You just hit a dependency problem mid-task | [At discovery](#at-discovery) |
| The task is done and you worked around at least one dependency problem | [At the end](#at-the-end) |
| The user approved the opt-in check you offered at the end | [Opt-in check](references/reproduce.md#opt-in-check) |
| The user said yes to drafting issues or comments | Read `references/draft-issue.md` |
| In a later session, the user asks you to look into an existing `TODO(upstream)` | Start from step 3 of [At discovery](#at-discovery), using the marker; then [At the end](#at-the-end) |

Reference paths are relative to this file's directory.

A subagent runs only [At discovery](#at-discovery). It returns each record, its `FINDINGS` and the marker's `path:line` in its report. The agent that answers the user runs [At the end](#at-the-end) over every report it received.

## At discovery

Toward dependencies, mid-task work is **read-only**: no installs, builds or version changes. The cheap check on latest waits for the end of the task. Anything beyond it waits for the user's approval.

1. **Attribute.** Trace the symptom to the first wrong decision (the [**fix-root-causes**](../principle-fix-root-causes/SKILL.md) principle skill) and confirm it is the dependency's: its docs or source for the installed version contradict what it does, the docs are wrong or silent, or it lacks something reasonable. If the project is misusing a correct API, fix the project's code and leave this skill.
   Report problems that made you change code or approach (a workaround, pin, cast, suppression, avoided API, or code you wrote because the docs misled you). Lesser oddities get one footnote line at the end.
2. **Security test.** Could this let someone cross a trust boundary: read or change data they shouldn't, run code, bypass auth, leak secrets, or crash the service with untrusted input? If plausibly yes, read `references/security.md` now. Its wording rules cover every comment, commit message and file you write from here on.
3. **Record** the problem as a todolist item. The record must be enough for a fresh agent to start from:
   - the dependency, its ecosystem and installed version, and the API involved;
   - a one-line symptom and the exact error text;
   - the call that triggers it, with its inputs;
   - the project root, and how to run code in the project's environment (e.g. `.venv/bin/python`, `npm exec`).
4. **Search upstream.** Spawn a fresh read-only subagent (harness: subagents), not a fork of this conversation, so the pages it reads stay out of your context (the [**guard-the-context-window**](../principle-guard-the-context-window/SKILL.md) principle skill). Give it the absolute path of `references/investigate.md`, the record, and the security flag from step 2. It returns a `FINDINGS` block. Use one subagent per problem; several can run in parallel. Pick each subagent's reasoning level for the job, per the Subagents section of the [**tialo-mode**](../tialo-mode/SKILL.md) skill. If you can't spawn subagents, read `investigate.md` and do the search yourself.
   Skip the search for a private dependency with no public source or tracker (an internal company package, say). Searching would leak internal names to public search engines. Mark it and report it as "internal, not searched".
5. **Work around it.** When nothing short of upgrading a dependency fixes it, write the workaround without asking. Keep it small and in one place, at the boundary where the project calls the dependency (the [**boundary-discipline**](../principle-boundary-discipline/SKILL.md) principle skill). An available upgrade gets proposed at the end; you leave versions as they are.
6. **Mark it** at the workaround, picking the first form that fits the findings:

   ```text
   TODO(upstream): remove when <dep> >= <version>. <why, one line>
   TODO(upstream): remove when <PR URL> is merged and released. <why>
   TODO(upstream): remove when <issue URL> is fixed. <why>
   TODO(upstream): remove when upstream fixes <brief description>. <why>
   TODO(upstream): suspected <dep>@<installed> bug, not verified on latest: <brief description>. Investigate further; remove when fixed upstream.
   ```

   Use the "upstream fixes" form only when the installed version is the latest release (so the bug is observed on latest). Otherwise an unknown problem gets the "suspected" form until it is checked on latest. The TODO names only upstream things: versions, URLs, descriptions. Draft files are untracked, so it never points to them. When the file can't hold comments (JSON manifests, lockfiles), put the TODO in the nearest code that relies on the change and name the file it concerns.

Then return to the user's task.

## At the end

Before your final message:

1. **Collect** the problems from this task: your records, plus any `TODO(upstream)` markers you added during this task. Markers left by earlier sessions are not new findings. Report each problem once. A problem found later, for example while continuing an investigation, goes through steps 1 to 4 of discovery and gets its own `FINDINGS` before you report it, since a search for a different problem doesn't count.
2. **Check on latest.** For each problem, spawn a fresh general worker (harness: subagents) with the absolute path of `references/reproduce.md`, the record and the `FINDINGS`. It applies its own cost gates and returns a `REPRO` block. Without subagents, follow `reproduce.md` yourself. If the result changes what is known, rewrite the TODO in the matching form.
3. **Disclose**, after your normal summary of the task, one block per problem:

   ```markdown
   ### <dep>@<installed>: <one-line symptom>
   - **Problem:** <observed vs expected>
   - **Upstream:** <fixed in vX | fix pending in PR <url> | known: <issue url> | no record found> (searched: <from FINDINGS>)
   - **Reproduction:** observed on <installed>; <latest>: reproduced | not reproduced | not run (<reason>)
   - **What I did:** <workaround> at `path:line`
   - **Upgrade:** <dep> <vX> includes the fix; upgrading should let you remove the workaround  ← only when a fix is released
   - **⚠️ Security:** <warning and disclosure procedure, from security.md>  ← only when flagged
   ```

   Below the blocks, add one line for any lesser oddities from step 1 of discovery: `Also noticed: <dep>: <one line>; ...`

4. **Offer** the next step, one line per problem:
   - Unknown upstream and not likely fixed: offer an issue draft.
   - Known issue, and you have new evidence (another affected version, a minimal repro, root cause, a workaround): offer a comment draft. Without new evidence, link the issue and suggest a 👍 reaction, since "+1" comments only add noise for maintainers.
   - `REPRO` has a version `not run (<reason>)`, or `FINDINGS` says the upstream code in that area changed so it may already be fixed: offer the **opt-in check**.
   - Security: a private report draft only.

   Drafts are prepared for the user, who decides whether and when to post them. Posting, commenting and reacting upstream stay with the user.

## Pressure to stay silent

| Thought | Reality |
|---|---|
| "It's a tiny workaround, not worth a mention." | Tiny workarounds are the ones nobody finds again. A TODO and one block cost little. |
| "The user didn't ask about dependencies." | They asked for working code. Its new workaround is part of what they're getting, so tell them. |
| "Someone has surely reported this already." | Then the search finds it quickly and the TODO gets its link. "Surely" is not a status. |
| "I'll just bump or pin the version." | A version change is the user's call, and a pin is a workaround too: mark it and report it. |
| "Searching will derail the task." | The search runs in a subagent, and anything that runs code waits for the end. |
