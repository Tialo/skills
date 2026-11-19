# Transcripts in Claude Code

- This workspace's transcripts: `~/.claude/projects/<slug>/*.jsonl`, one file per session, named by session id. `<slug>` is the workspace path with each `/` and `.` changed to `-`, so `/Users/you/proj` is `-Users-you-proj`. Read no other project's folder.
- Current session: the newest `.jsonl` in that folder.
- Subagent transcripts: `<slug>/<session id>/subagents/`.
- Format: each line is one JSON event. Lines with `type` `user` or `assistant` hold the chat in `message.content`, as text, `tool_use`, and `tool_result` blocks. Other types are metadata. The session id in the file name is the chat UUID.
