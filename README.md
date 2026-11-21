This repository ships [tstack](tstack/README.md), a plugin with agent workflows, engineering principles and review skills for Claude Code, Codex, and Cursor.

## Install

<details>
<summary><strong>Claude Code</strong></summary>

```bash
claude plugin marketplace add Tialo/skills
claude plugin install tstack@tialo
```

Update with `claude plugin marketplace update tialo`, then `claude plugin update tstack@tialo`.

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add Tialo/skills
codex plugin add tstack@tialo
```

Open Codex in your project and run `$tstack:setup-tstack`. To enable the read-only reader, review and trust tstack’s hook in `/hooks` and start a new session.

</details>

<details>
<summary><strong>Cursor</strong></summary>

tstack is not in the Cursor Marketplace. On a Teams or Enterprise plan, import `https://github.com/Tialo/skills` as a team marketplace: in the dashboard, open **Plugins & MCPs**, then **Team Marketplaces**, **Add Marketplace**, **Import from Repo**. Otherwise, install it as a local plugin:

```bash
git clone https://github.com/Tialo/skills.git tialo-skills
mkdir -p ~/.cursor/plugins/local
rsync -a --delete tialo-skills/tstack/ ~/.cursor/plugins/local/tstack/
```

Then run **Developer: Reload Window**. To update, run `git -C tialo-skills pull` and the `rsync` line again.

</details>

## Credits

tstack is inspired by [pstack](https://github.com/cursor/plugins/tree/main/pstack) and [mattpocock/skills](https://github.com/mattpocock/skills).
