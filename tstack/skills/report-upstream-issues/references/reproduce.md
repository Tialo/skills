# Check on latest (and the opt-in check)

You are checking whether a dependency problem still happens on newer released versions, cheaply and without touching the user's project.

## Inputs

From the caller:

- **The problem record:** dependency, ecosystem, installed version, symptom, exact error, the triggering call and its inputs, the project root, and how to run code in the project's environment.
- **Its `FINDINGS`:** the latest stable version, and the fix version if one is named.

Return early when there's nothing to run:

- **Installed version is already the latest:** the project's own failure is the observation on latest. Return `<installed>: reproduced (installed is latest)`.
- **Hosted dependency** (a SaaS API, a CI action run by the platform, anything without a version you can install): return `not applicable (hosted)`.

## 1. Write a standalone snippet

Write the smallest program that shows the problem using only the dependency's public API. It contains no project code, no project data and no secrets. Run it once with the **installed** version in the project's existing environment. That counts as running, not installing, so the project stays untouched.

It must fail there the same way the project did. If it doesn't, adjust it once. If it still doesn't fail, stop and report `installed: snippet does not capture it`, along with what you tried.

## 2. Gates

Check all of these **before** installing anything. Each one is a yes/no fact, not an estimate:

- **Prebuilt only.** A prebuilt artifact exists for this platform, and the install runs neither the dependency's build step nor its install scripts.
- **Size known up front.** The total download (the package plus every new dependency) comes from registry metadata, and it is **at most 50 MB**.
- **Self-contained.** No service, GPU, browser, container, account or credentials are needed. It uses a runtime that's already installed (ideally the project's own interpreter). Downloading an interpreter, SDK or toolchain doesn't count as a cheap check.
- **Isolated.** Everything goes into a fresh temporary directory outside the project. The project's manifests, lockfiles, virtualenvs, `node_modules` and caches it owns are never touched.
- **Bounded.** Every command gets a **120-second timeout** and one attempt. Any setup failure ends as `not run (setup failed: <error>)`, with no retries and no repairing the setup.
- **Limited versions.** Test only the latest stable release, plus the fix version that `FINDINGS` names, if any.
- **No compiling.** If testing a version means compiling the dependency itself (common in Rust, Go and C/C++), the result is `not run (needs compilation)`.

A failed gate is a valid result. Report which gate failed. The user can approve going further through the [opt-in check](#opt-in-check).

### Meeting the gates in any ecosystem

The package manager you are about to use is the authority, so don't trust memory. In its `--help` or official docs, find:

1. the flag that refuses to build from source;
2. the flag that disables install scripts;
3. a dry run that lists what would be downloaded;
4. the registry API that reports file sizes.

Confirm each flag in the installed tool's own `--help` before relying on it. If a guarantee can't be confirmed, the result is `not run (cannot guarantee <which>)`.

### Example: Python

Checked with uv 0.13 and pip 26:

```bash
d=$(mktemp -d)
uv venv "$d/venv" --python <path to the project's interpreter> --no-python-downloads   # fails rather than fetching a Python
uv pip install --python "$d/venv" --no-build --dry-run "<pkg>==<version>"   # lists the resolution; refuses source-only packages
# size: per listed package, take the largest wheel "size" in https://pypi.org/pypi/<name>/<version>/json, then sum
uv pip install --python "$d/venv" --no-build "<pkg>==<version>"
"$d/venv/bin/python" snippet.py
```

With pip, `--only-binary=:all:` refuses source builds, and `--dry-run --report <file>` lists the resolution. Older pips (21 and earlier) lack `--dry-run`, which is why the flag check above comes first. Wheels run no install scripts, so binary-only also covers the scripts gate.

## 3. Run and report

Run the snippet against each allowed version. Count a result as **reproduced** only when you ran it and saw the same failure. If it might be flaky, run it twice. Delete the temporary directory afterwards.

Return exactly:

```text
REPRO <dep>
installed <version>: reproduced | snippet does not capture it
<version>: reproduced | not reproduced | not run (<gate or error>)      (one line per version tried)
snippet:
<the snippet, at most 30 lines>
commands: <exact commands run>
```

## Opt-in check

Read this section only when the user approves the opt-in check offered at the end of their task. It covers everything the gates exclud
ed: source builds, large installs, other versions, bisecting, PR branches and the default branch.

Present **one plan** and wait for approval:

- **Question:** what the plan will answer, e.g. "is it fixed on main?" or "which release fixed it?".
- **Footprint:** what gets downloaded or built, and roughly how large it is.
- **Commands:** the exact commands, and where they run (a temporary directory).
- **Untouched:** the project's dependencies and environment.

After approval, stay inside the plan. If something outside it becomes necessary, stop and present a new plan. Return the same `REPRO` block; the main agent updates the TODO and the report.
