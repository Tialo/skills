## Initialization

* Renamed the plugin to tstack.
* Script for harness generation rewritten from node to python.
* Script for harness generation now outputs into harness/*.
* Removed the Comment Sicko agent and the skill that spawned it.
* Renamed poteto to tialo.
* Removed the Cursor-only benny automation pack.
* Removed the illustrations from `docs/guide/images/`.
* Removed the make-bot-ui skill.
* Removed the multi-phase-plan playbook and its `check-plan.mjs` checker from tialo-mode; tialo-help and the design guide now point to Claude Code's plan mode and figure-it-out.
* Removed the autopilot-full, autopilot-stack, and orchestrate playbooks from tialo-mode, with the guide sections about PR queues and Cursor Projects.
* Removed the babysit and shipping playbooks, the Bugbot triage rubric, and the `watch-pr` watcher from tialo-mode.
* Removed the worktree and simulator cleanup playbook and its `worktree-audit.sh` script from tialo-mode.
* Removed the never-block-on-the-human principle. tialo-mode drops the full-autonomy grant, session overrides, and the rule that external actions proceed without asking.
* Removed the "Run work while you sleep" guide page and the prompts about stepping away, overnight runs, and parallel cloud agents.
* Removed the Origin forge and the built-in PR tool from the opening-a-pr playbook; PR commands now use `gh` only.
* Renumbered guide pages 08–10 to 07–09 after removing the overnight page.
* Removed `typescript-best-practices`. Shared skills support external type checkers or manual type analysis when the compiler does not check types.
