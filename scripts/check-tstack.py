#!/usr/bin/env python3
"""Checks that tstack skills stay harness-neutral and that their links resolve."""

import os
import re
import sys
from pathlib import Path

TSTACK = Path(__file__).resolve().parent.parent / "tstack"
SKILLS = TSTACK / "skills"
HARNESS = SKILLS / "harness"
HARNESSES = ["claude-code", "codex", "cursor"]
MARKER = re.compile(r"\(harness: ([a-z-]+)")
LINK = re.compile(r"\]\(([^)\s]+)\)")
BARE_SKILL = re.compile(r"(?<!\[)\*\*([a-z0-9-]+)\*\*(?!\]\()")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
# Harness-specific names that belong in skills/harness/<harness>/, not in shared skills.
DENY = re.compile(
    r"AskQuestion|AskUserQuestion|generalPurpose|run_in_background|"
    r"readonly: |environment: \"|isolation: |cloud_base_branch|inherit-parent|agent-transcripts|"
    r"\.cursor/|\.claude/|\.codex/|\.agents/skills/|\bspawn_agent\b|\bCodex\b|"
    r"\.mdc\b|\bclaude-[a-z]+-\d|\bgemini-|\bgpt-\d|\bgrok-\d|-fast\b|"
    r"\b(Opus|Sonnet|Fable|Haiku)\b|\bCursor\b|Claude Code"
)


def markdown(directory):
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in ("node_modules", "scripts")]
        for name in files:
            if name.endswith(".md"):
                yield Path(root) / name


skills = {p.name for p in SKILLS.iterdir() if (p / "SKILL.md").exists()}
problems = []

for skill in sorted(skills):
    text = (SKILLS / skill / "SKILL.md").read_text()
    frontmatter = text.split("\n---", 1)[0]
    match = re.search(r"^name:\s*(.*)$", frontmatter, re.M)
    name = match.group(1).strip().strip("\"'") if match else ""
    if name != skill:
        problems.append(f"skills/{skill}/SKILL.md has name {name!r}, not its folder name")
    if not SKILL_NAME.match(skill) or len(skill) > 64:
        problems.append(f"skills/{skill} is not lowercase words joined by hyphens, at most 64 characters")
    explicit_only = "disable-model-invocation: true" in frontmatter.splitlines()
    metadata = SKILLS / skill / "agents/openai.yaml"
    codex_policy = metadata.read_text() if metadata.exists() else ""
    codex_explicit_only = "policy:\n  allow_implicit_invocation: false\n" in codex_policy
    if explicit_only != codex_explicit_only:
        problems.append(f"skills/{skill}: Codex invocation policy differs from the skill frontmatter")

for path in markdown(TSTACK):
    rel = path.relative_to(TSTACK).as_posix()
    text = path.read_text()
    shared = (rel.startswith("skills/") or rel.startswith("agents/")) and not rel.startswith("skills/harness/")
    for n, line in enumerate(text.split("\n"), 1):
        for topic in MARKER.findall(line):
            for harness in HARNESSES:
                if not (HARNESS / harness / f"{topic}.md").exists():
                    problems.append(f"{rel}:{n} marks topic {topic!r}, missing for {harness}")
        if shared:
            for m in DENY.finditer(line):
                problems.append(f"{rel}:{n} names {m.group(0)!r}, which belongs in a harness topic")
            for m in BARE_SKILL.finditer(line):
                if m.group(1) in skills or f"principle-{m.group(1)}" in skills:
                    problems.append(f"{rel}:{n} names skill {m.group(1)!r} without a link to its SKILL.md")
    for href in LINK.findall(text):
        if re.match(r"[a-z][a-z0-9+.-]*:", href) or href.startswith("#"):
            continue
        target = (path.parent / re.sub(r"[#?].*", "", href)).resolve()
        if not target.exists():
            problems.append(f"{rel} links to {href}, which does not exist")

for problem in problems:
    print(f"FAIL {problem}")
if problems:
    sys.exit(1)
print(f"{len(skills)} skills, no problems")
