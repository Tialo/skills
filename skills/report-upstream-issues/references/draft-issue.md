# Drafting upstream issues and comments

Read this when the user agrees to drafts. Write one draft per problem. Each draft is prepared for the user, who reviews it and posts it if they choose.

Each draft needs a `FINDINGS` block from an upstream search for that exact problem. If it has none, run the search first (see `investigate.md`). If the search turns up an existing issue, the draft becomes a comment, or nothing at all.

## 1. Read the receiving project's rules

Before writing a word, find and read:

- the contributing guide (`CONTRIBUTING*` at the root, in `.github/` or in `docs/`, or the org-level `.github` repository);
- the issue templates and forms in `.github/ISSUE_TEMPLATE/`, plus `config.yml` there, which may route bugs, questions or features elsewhere;
- any AI or LLM policy, in the contributing guide, `AI_POLICY*`, `AGENTS.md`, the README or the org `.github` repository.

Note the required template and fields, title conventions, where each kind of report goes, and whether AI-generated content is banned, restricted, or must be disclosed in specific wording. The project's rules beat this file's defaults.

## 2. Choose the kind

- **New issue**: nothing upstream covers it yet.
- **Comment on an existing issue**: only with new evidence. Lead with what's new: another affected version, a minimal repro, the root cause, or a workaround.
- **Discussion or forum post**: when the project routes questions or feature requests there.

## 3. Write the file

Write `.upstream-drafts/<dep>-<short-slug>.md` at the project root. If `.upstream-drafts/` doesn't exist, create it along with `.upstream-drafts/.gitignore` containing `*`, so the folder ignores itself. Leave the project's own `.gitignore` alone. Security drafts go in `.upstream-drafts/security/` and follow `security.md`.

```markdown
# Draft: <title>
- File at: <new-issue or template URL>
- Template: <name, or none>
- Status: verified on <version> | ⚠️ observed on <installed>; not verified on latest <version> (<reason>)
- Before posting: run the reproduction yourself and fill any <placeholders>.

--- paste below this line ---

> This issue was drafted by an AI coding agent.

<body>
```

If the project prescribes its own disclosure wording, use it instead of the line above. The user may remove the disclosure before posting; that's their call.

**When the project bans or restricts AI-written issues**, still write the draft, but put this above everything else in the file, and repeat it in chat:

```markdown
> ⚠️ **<project> does not accept AI-generated issues** (<policy link>). Posting this as-is will
> probably get the issue closed or you banned from contributing. Rewrite it in your own words, and
> check the issue and the reproduction yourself before posting.
```

## 4. The body

Fill the project's template if it has one. Otherwise, in this order:

- **Title:** the observed symptom, phrased so it stays true if the suspected cause turns out wrong. Follow the project's title conventions.
- **What happens:** the observed behaviour with the exact error output.
- **Expected:** what should happen, with a docs link when the docs say so.
- **Reproduction:** the standalone snippet from `REPRO`, the exact commands, and the versions of the dependency, runtime and OS.
- **Latest:** the result on the latest release, with its version number.
- **Workaround:** a short one, if it helps other users.
- **Notes:** the suspected cause, labelled as inference; and related issues, each with one line on how this differs.

Keep facts and inferences visibly separate. Write for a maintainer with 30 seconds to triage.

**Redact:** include no project code beyond the minimal snippet, and no internal names, paths, hostnames, tokens or data. Swap in generic names.

## 5. Present

List each draft with its path and where to post it, and repeat any AI-ban warning. Nothing has been published. Posting is the user's decision, and so is when.
