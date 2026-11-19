---
name: grill-me
description: "Interview the user relentlessly about a plan, decision, or idea until you share one understanding of it, before anyone acts. Use for /grill-me, 'grill me', or 'think this through with me'."
disable-model-invocation: true
---

# Grill me

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Word each question so "yes" accepts your recommended answer.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Sort each open question before it reaches a round:

- A **fact** the environment holds (code, history, tools) is your job. Find it with a read-only subagent (harness: subagents). Never ask the user for anything you could look up.
- A **fork you could settle by running something** (a behavior, a timing, an approach) is also your job. Settle it with a prototype per the [Prototype playbook](../tialo-mode/playbooks/prototype.md), and report what you observed in the next round.
- A **decision** of preference, scope, or priority is the user's. Put it to them and wait.

Don't block on a lookup or a prototype. A running one is an unsettled prerequisite, so only the questions downstream of it wait. Ask the rest of the frontier now.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Close with a restatement per the [**in-your-own-words**](../in-your-own-words/SKILL.md) skill and the list of settled decisions. Do not act on it until the user confirms you have reached a shared understanding.
