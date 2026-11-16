#!/usr/bin/env python3

import json
import os
import posixpath
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSTACK = ROOT / "tstack"
SKILLS = TSTACK / "skills"
# Outside tstack/ so Cursor, which copies the whole plugin folder, does not install this tree too.
OUT = ROOT / "harness"
TREE = "claude-code"
ADAPTER = "docs/harness/claude-code.md"
GUIDE = "docs/guide"
MANIFESTS = ["plugin.json", ".claude-plugin/plugin.json"]
COMMAND = "python3 scripts/generate-tstack-harness.py"
GITHUB = "https://github.com/Tialo/skills"
LINK = re.compile(r"\]\(([^)\s]+)\)")
README = f"""# tstack harness tree

This folder is generated from `tstack/skills`, `tstack/agents`, `tstack/{GUIDE}`, `tstack/{ADAPTER}`, `tstack/README.md`, `tstack/LICENSE`, and `tstack/plugin.json`. Do not edit it by hand.

Cursor uses `tstack/` directly, and Claude Code installs `{TREE}/`. The tree leaves out the rest of `tstack/`, such as `tstack/automations` and `tstack/assets`. A relative link to a tstack file that the tree leaves out points at that file on GitHub `main` instead.

After editing those sources, run `{COMMAND}` from the repository root and commit the result.
"""

TERMS = [
    ("`Task`", re.compile(r"`Task`|\bTask (tool|subagent|call)")),
    ("`AskQuestion`", re.compile(r"AskQuestion")),
    ("todolist", re.compile(r"\btodo ?list\b", re.I)),
    ("generalPurpose", re.compile(r"generalPurpose")),
    ("poteto-agent", re.compile(r"poteto-agent")),
    ("`readonly: true`", re.compile(r"readonly: (true|false)|readonly/Ask")),
    ('`environment: "cloud"`', re.compile(r'environment: "(cloud|local)"')),
    ("cloud_base_branch", re.compile(r"cloud_base_branch")),
    ("`run_in_background: true`", re.compile(r"run_in_background")),
    ("`resume`", re.compile(r"`resume`")),
    ("`file_attachments`", re.compile(r"file_attachments")),
    ("claude-", re.compile(r"\bclaude-[a-z]+-\d")),
    ("grok-", re.compile(r"\bgrok-\d")),
    ("gpt-", re.compile(r"\bgpt-\d")),
    ("inherit-parent", re.compile(r"inherit-parent")),
    ("tstack-models.mdc", re.compile(r"tstack-models\.mdc")),
    (".cursor/skills/", re.compile(r"\.cursor/skills")),
    ("~/.cursor/plugins/", re.compile(r"\.cursor/plugins|\.cursor-plugin")),
    (".cursor/rules/", re.compile(r"\.cursor/rules|always-applied rule")),
    ("agent-transcripts", re.compile(r"agent-transcripts|\.cursor/projects")),
    (
        "Cursor-only features",
        re.compile(r"Bugbot|Cursor [Aa]utomation|cursor\.(sh|com)/automations|[Cc]loud [Aa]gent|built-in PR tool"),
    ),
]
ROUTE_KEY = "Run another tstack skill"
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def walk(directory):
    paths = []
    for name in sorted(os.listdir(directory)):
        if name in (".DS_Store", "node_modules"):
            continue
        path = Path(directory) / name
        paths.extend(walk(path) if path.is_dir() else [path])
    return paths


def file(path):
    return {"bytes": Path(path).read_bytes(), "executable": (os.stat(path).st_mode & 0o111) != 0}


def text_of(data):
    return data.decode("utf-8", errors="replace")


def rel(path, base):
    return Path(path).relative_to(base).as_posix()


skills = [name for name in sorted(os.listdir(SKILLS)) if (SKILLS / name / "SKILL.md").exists()]


def classify(skill):
    directory = SKILLS / skill
    others = "|".join(re.escape(name) for name in skills if name != skill)
    route = re.compile(rf"the \*\*(?P<bold>{others})\*\* skill|`/(?P<command>{others})`")

    def links_to_skill(line, name):
        return f"(../{name}/" in line

    def names_bare_skill(line):
        return any(
            not links_to_skill(line, m.group("bold") or m.group("command")) for m in route.finditer(line)
        )

    uses_cursor_names = []
    for path in walk(directory):
        if not path.name.endswith(".md"):
            continue
        text = text_of(path.read_bytes())
        for key, pattern in TERMS:
            if pattern.search(text) and key not in uses_cursor_names:
                uses_cursor_names.append(key)
        if any(names_bare_skill(line) for line in text.split("\n")) and ROUTE_KEY not in uses_cursor_names:
            uses_cursor_names.append(ROUTE_KEY)
    text = text_of((directory / "SKILL.md").read_bytes())
    wrap = len(uses_cursor_names) > 0 and re.search(r"^# ", text, re.M) is not None
    return {"uses_cursor_names": uses_cursor_names, "wrap": wrap}


classes = {skill: classify(skill) for skill in skills}
problems = []
users = {}
for skill, info in classes.items():
    if info["uses_cursor_names"] and not info["wrap"]:
        problems.append(f"skills/{skill}/SKILL.md uses Cursor names but has no H1")
    for key in info["uses_cursor_names"]:
        users.setdefault(key, []).append(skill)
    # Cursor runs a skill by its folder name and Claude Code lists it by its frontmatter `name`, so the two must match. The Agent Skills spec limits both to SKILL_NAME.
    frontmatter_match = re.match(r"---\n([\s\S]*?)\n---", text_of((SKILLS / skill / "SKILL.md").read_bytes()))
    frontmatter = frontmatter_match.group(1) if frontmatter_match else ""
    name_match = re.search(r"^name:(.*)$", frontmatter, re.M)
    name = re.sub(r"^([\"'])(.*)\1$", r"\2", name_match.group(1).strip()) if name_match else None
    if name != skill:
        problems.append(
            f"skills/{skill}/SKILL.md has name {json.dumps(name or '', ensure_ascii=False)}, not its folder name {skill}"
        )
    if not SKILL_NAME.match(skill) or len(skill) > 64:
        problems.append(f"skills/{skill} is not lowercase words joined by hyphens, at most 64 characters")
adapter = text_of((TSTACK / ADAPTER).read_bytes())
for key, using in users.items():
    if key not in adapter:
        problems.append(f"Claude Code adapter has no row for {key}, used by {', '.join(using)}")
for problem in problems:
    print(f"FAIL {problem}")
if problems:
    sys.exit(1)


def resolve(source, href):
    """The tstack-relative path that a relative link in `source` points at, if that path exists."""
    target = re.sub(r"[#?].*", "", href)
    if not target or re.match(r"[a-z][a-z0-9+.-]*:", target, re.I):
        return None
    path = re.sub(r"/$", "", posixpath.normpath(f"{posixpath.dirname(source) or '.'}/{target}"))
    return path if (TSTACK / path).exists() else None


def has(files, path):
    return path in files or any(key.startswith(f"{path}/") for key in files)


def render():
    # Skills read the adapter, the guide, and the README at runtime, so Claude Code never fetches them.
    copies = [
        *walk(SKILLS),
        *walk(TSTACK / "agents"),
        *walk(TSTACK / GUIDE),
        TSTACK / ADAPTER,
        TSTACK / "README.md",
    ]
    files = {rel(path, TSTACK): file(path) for path in copies}
    line = (
        f"In Claude Code, read [the Claude Code adapter](../../{ADAPTER}) once per session before you follow this skill. "
        "It maps the Cursor names in tstack skills to Claude Code."
    )
    for skill, info in classes.items():
        path = f"skills/{skill}/SKILL.md"
        text = text_of(files[path]["bytes"])
        if info["wrap"]:
            text = re.sub(r"^(# .*)\n+", lambda m: f"{m.group(1)}\n\n{line}\n\n", text, count=1, flags=re.M)
            files[path]["bytes"] = text.encode("utf-8")
    files["LICENSE"] = file(TSTACK / "LICENSE")
    for manifest in MANIFESTS:
        files[manifest] = file(TSTACK / "plugin.json")
    for path, entry in files.items():
        if not path.endswith(".md"):
            continue

        def relink(m, path=path):
            href = m.group(1)
            target = resolve(path, href)
            if not target or target.split("/")[0] == ".." or has(files, target):
                return m.group(0)
            kind = "tree" if (TSTACK / target).is_dir() else "blob"
            suffix = re.search(r"[#?]", href)
            return f"]({GITHUB}/{kind}/main/tstack/{target}{href[suffix.start():] if suffix else ''})"

        entry["bytes"] = LINK.sub(relink, text_of(entry["bytes"])).encode("utf-8")
    return files


# Claude Code installs only the tree, so a relative link that works from tstack/ has to work inside the tree too.
# Links to tstack files that the tree leaves out already point at GitHub, so a failure here is a link that leaves tstack/.
files = render()
rendered = {"README.md": {"bytes": README.encode("utf-8"), "executable": False}}
dangling = []
for path, entry in files.items():
    rendered[f"{TREE}/{path}"] = entry
    if not path.endswith(".md"):
        continue
    for m in LINK.finditer(text_of(entry["bytes"])):
        href = m.group(1)
        target = resolve(path, href)
        if target and not has(files, target):
            dangling.append(f"harness/{TREE}/{path} links to {href}, which is not in the tree")
for link in dangling:
    print(f"FAIL {link}")
if dangling:
    sys.exit(1)

if "--check" in sys.argv[1:]:
    on_disk = {rel(path, OUT): file(path) for path in walk(OUT)} if OUT.exists() else {}
    drifted = [
        path
        for path in sorted(set(rendered) | set(on_disk))
        if path not in rendered
        or path not in on_disk
        or rendered[path]["bytes"] != on_disk[path]["bytes"]
        or rendered[path]["executable"] != on_disk[path]["executable"]
    ]
    for path in drifted[:20]:
        print(f"harness/{path}")
    if drifted:
        print(f"harness is out of date. Run `{COMMAND}` and commit the result.")
        sys.exit(1)
    print("harness is up to date.")
else:
    shutil.rmtree(OUT, ignore_errors=True)
    for path, entry in rendered.items():
        target = OUT / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(entry["bytes"])
        os.chmod(target, 0o755 if entry["executable"] else 0o644)
    wrapped = sum(1 for info in classes.values() if info["wrap"])
    print(f"{len(skills)} skills, {wrapped} SKILL.md files with the adapter line")
