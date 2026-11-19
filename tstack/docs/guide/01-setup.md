# Set up tstack

In this page you install the plugin, pick which models tstack uses, and run your first task. Setup is one command plus a short conversation.

## Install the plugin

In a Cursor chat, run:

```text
/add-plugin tstack
```

Cursor confirms the plugin is installed.

In Claude Code, run `/plugin marketplace add Tialo/skills`, then `/plugin install tstack@tialo`. Claude Code prefixes plugin commands, so each command in this guide takes a `tstack:` prefix there, such as `/tstack:setup-tstack`.

## Pick your models

Run:

```text
/setup-tstack
```

[`/setup-tstack`](../../skills/setup-tstack/SKILL.md) detects the models you have access to, asks for a reasoning budget, shows you each role (code delegates, judgment, the review panels), and asks what you want. In Cursor it also asks whether to use fast models and cloud agents. Answer the questions. It writes a small rule into your project, in the harness's own rules folder, and every tstack skill reads it.

The defaults are the same as the `large` budget. Code, prose, and judgment run on Opus 5.5 at `xhigh` reasoning, and the review panels and swarm workers run at `high`. No role runs above `xhigh`. Outside a review panel, Fable 5.2 runs only when you name it for a task or after two Opus 5.5 runs of the same brief fail their check. Where the Cursor defaults use Gemini 4 Neon, Claude Code uses Sonnet 5.5. `medium` lowers each role one level and `small` lowers it two, and both spend fewer tokens.

A role with no line in the rule, or a project with no rule, runs on your chat's model. A rerun of `/setup-tstack` keeps your choices and offers newer versions of the models you picked. For a panel role the value is a list, and one subagent runs per entry, so the list length sets the panel size. Setup also configures `swarm workers`, the default model for every `/swarm` worker unless a race names a model for each arm.

## Accept the verification offers, or don't

At the end of setup, `/setup-tstack` looks for a way to prove app behavior in your project, either a `verify-*` skill or an existing harness. If it finds neither, it offers once to generate one with [`/create-verification-skill`](../../skills/create-verification-skill/SKILL.md).

Say yes and it writes a `verify-<app>` skill into your project's skills folder, a project-local skill that teaches agents to drive your app the way a user does. It proves the skill works once before handing it over. Say no and setup moves on. You can run `/create-verification-skill` yourself any time. [Verify and ship](./06-verify-and-ship.md#create-a-project-verification-skill) covers it in depth.

If you're new to tstack, say yes. An agent that can check its own work keeps going until the check passes. An agent that can't hands every result back to you to check by hand. Of everything in this guide, the verification skill pays off the most.

Then setup offers once to generate a formal verification skill with [`/create-formal-verification-skill`](../../skills/create-formal-verification-skill/SKILL.md), unless the project already has one. Tests check the cases someone thought to write. A formal verification skill checks one key property of your code, such as "a job never runs twice at once", in every case within a stated scope. Say yes when your code has concurrency, retries, a state machine, or a parser, where a bug is costly and tests rarely reach the case that breaks. Otherwise say no, and run it later if that changes. [Verify and ship](./06-verify-and-ship.md#prove-a-property-with-a-formal-verification-skill) covers it.

After setup, start a new chat. The rule applies to new sessions in this project.

## Keep the cost in check

tstack spends extra tokens on subagents and review panels. That's the price of the rigor. To spend fewer:

- Rerun `/setup-tstack` and pick a smaller reasoning budget or cheaper models. A strong model in the main chat with cheaper, faster models in the code roles is a good split.
- Delete a role's line so it runs on the chat's own model.
- Shorten a panel list. Each entry runs one subagent.
- Save `/tialo-mode` for work that needs rigor. A small, obvious edit doesn't.

## Run your first task

Pick something real but small, and describe it the way you'd describe it to a colleague:

```text
/tialo-mode add a --json flag to this command. text output stays byte-identical. verify both.
```

Watch the todo list. Its first items are the matched playbook's steps copied in, the Feature playbook for this prompt.

From here you can type normal follow-ups. In Claude Code, the skill stays in the chat until compaction drops it. In Cursor, to keep `/tialo-mode` on for the whole chat, pick it from the `/` menu with Option+Enter (Mac) or Alt+Enter (Windows) instead of Enter. That makes it a [Custom Mode](https://cursor.com/docs/skills#using-a-skill-as-a-custom-mode), which stays in context on every turn until you exit it. Custom Modes are available in the Agents Window and the CLI. Plain Enter attaches the skill to one message, and it fades as the chat moves on.

Next: [Route work through `/tialo-mode`](./02-tialo-mode.md).
