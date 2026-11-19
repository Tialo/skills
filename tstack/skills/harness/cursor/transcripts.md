# Transcripts in Cursor

- This workspace's transcripts: `~/.cursor/projects/<slug>/agent-transcripts/<uuid>/<uuid>.jsonl`. `<slug>` is the workspace path with the leading `/` dropped and each `/` changed to `-`, so `/Users/you/proj` is `Users-you-proj`. The system prompt names the folder. Do not glob across `~/.cursor/projects/*/`, which reads unrelated private chats.
- Current session: the newest transcript by modification time.
- Format: each line is one chat message. The uuid is the chat id.
