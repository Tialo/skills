# Transcripts in Codex

- This workspace's transcripts: `~/.codex/sessions/YYYY/MM/DD/rollout-<time>-<thread id>.jsonl`, one file per thread, with archived threads in `~/.codex/archived_sessions/`. The folders mix projects. The first line is `session_meta`, and its `payload.cwd` is the workspace. Read only files whose `cwd` is this workspace.
- Current session: the rollout whose thread id is `$CODEX_THREAD_ID`.
- Subagent transcripts: rollouts whose `session_meta` `payload.source.subagent.thread_spawn.parent_thread_id` is the parent's thread id.
- Format: each line is one JSON event. Lines with `type` `response_item` hold the chat in `payload`: `message` items carry text by `role`, and `function_call`, `custom_tool_call`, and their `_output` items carry tool calls. The thread id in the file name is the chat UUID.
