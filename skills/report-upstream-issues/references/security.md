# Security-sensitive problems

Read this as soon as a problem may be a vulnerability. Its job: the maintainers learn about it privately, and nothing public points attackers at it before a fix ships.

"Public" means anything other people can read: issues, PRs, discussions, commit messages, branch names, code comments, CI logs, and any file that may get committed.

## 1. Neutral wording, from now on

Make the TODO, the code comments and the commit messages describe what the workaround *does*, not the weakness it covers:

```text
TODO(upstream): remove when <dep> >= <version>. Validates <input> before passing it to <dep>.
TODO(upstream): remove when upstream fixes <neutral description>. Normalises paths before <dep> sees them.
```

Leave out words like "injection", "bypass", "traversal" or "CVE", and any exploit detail. Once an advisory is published, the TODO may cite it.

Keep the reproduction local. Test nothing against systems the user doesn't own.

## 2. Is it already public?

The upstream search covers published advisories when the caller flags security (see `FINDINGS`). A published advisory makes this a *known vulnerability*. Report it as known, and propose the fixed version as an upgrade.

## 3. Find the disclosure procedure

Look in this order:

1. `SECURITY.md` in the repository root, in `.github/`, or in the org-level `.github` repository.
2. GitHub private vulnerability reporting. `gh api repos/OWNER/REPO/private-vulnerability-reporting` returns `{"enabled": true}` when it's on, and reports then go through the repository's Security tab, "Report a vulnerability".
3. `/.well-known/security.txt` on the project's official domain.
4. A security page in the project's docs.
5. The ecosystem's security team (for example the language foundation or the package registry), when the project names none.

Record the channel, its URL, what it asks reporters to include, and any supported-versions or response-time policy. Never guess an email address.

## 4. Report to the user

In the problem's disclosure block, the **⚠️ Security** line:

- warns that this may be a vulnerability and must not be filed as a public issue;
- summarises the procedure in 2 to 4 lines, with its link.

If no private channel exists, say so plainly and advise against filing publicly. Suggest asking the maintainers for a private contact, without details, or going to the ecosystem's security team.

## 5. Private report draft

Offer only a private report draft, never a public one. When the user agrees, write `.upstream-drafts/security/<dep>-<short-slug>.md`. If `.upstream-drafts/` doesn't exist yet, create it with a `.gitignore` containing `*`.

Follow the channel's requested fields. Otherwise include:

- affected component and versions;
- impact, marked as provisional;
- preconditions;
- the minimal local reproduction;
- a fix idea, if one is obvious.

Put `> This report was drafted by an AI coding agent.` at the top, apply the AI-policy and redaction rules from `draft-issue.md`, and tell the user where to submit it. Submitting stays with the user.
