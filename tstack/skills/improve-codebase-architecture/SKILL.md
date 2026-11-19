---
name: improve-codebase-architecture
description: "Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one the user picks. Use for /improve-codebase-architecture, 'find what to restructure', or a refactor with no named target."
disable-model-invocation: true
---

# Improve Codebase Architecture

Surface architectural friction and propose **deepening opportunities**: refactors that turn shallow modules into deep ones. The aim is testability and AI-navigability.

## Lens

- **Depth** is leverage at the interface: how much behavior a caller or test reaches per unit of interface it must learn. The interface is everything a caller must know to use a module correctly: types, invariants, ordering, error modes, configuration. A module is **deep** when a lot of behavior sits behind a small interface, **shallow** when the interface is nearly as complex as the implementation.
- **Leverage** is what callers get from depth. One implementation pays back across N call sites and M tests.
- **Locality** is what maintainers get from depth. Change, bugs, knowledge, and verification concentrate in one place.

The deletion test and the one-adapter rule come from the [**minimize-reader-load**](../principle-minimize-reader-load/SKILL.md) principle skill. The interface as the test surface comes from the [**test-behavior-not-implementation**](../principle-test-behavior-not-implementation/SKILL.md) principle skill. Read both before you scan.

## Process

### 1. Explore

**Scope before you scan: YAGNI.** Deepening a module pays off by making future changes to it easier, so put extra weight on the parts of the codebase that have recently changed. Decide *where* to look before you look:

- If the user named a direction (a module, a subsystem, a pain point), take it, and skip the inference below.
- Otherwise, walk back a good stretch of the commit history (`git log --oneline`) to find the codebase's hot spots, the files and areas that keep coming up, and let those paths pull your attention first. If the changes are scattered with no clear hot spot, widen the net.

Then spawn a read-only subagent (harness: subagents) to walk the codebase, with the Lens and the two principle paths in its brief. Don't follow rigid heuristics; explore organically and note where you experience friction:

- Where does understanding one concept require bouncing between many small modules?
- Where are modules **shallow**, with an interface nearly as complex as the implementation?
- Where have pure functions been extracted just for testability, but the real bugs hide in how they're called (no **locality**)?
- Where do tightly-coupled modules leak across their boundaries?
- Which parts of the codebase are untested, or hard to test through their current interface?

Apply the deletion test to anything you suspect is shallow: would deleting it concentrate complexity, or just move it? A "yes, concentrates" is the signal you want. Back each candidate with the callers you counted and the commits that touched it.

### 2. Present candidates as an HTML report

Write a self-contained HTML file to the OS temp directory so nothing lands in the repo. Resolve the temp dir from `$TMPDIR`, falling back to `/tmp` (or `%TEMP%` on Windows), and write to `<tmpdir>/architecture-review-<timestamp>.html` so each run gets a fresh file. Open it for the user (`xdg-open <path>` on Linux, `open <path>` on macOS, `start <path>` on Windows) and tell them the absolute path.

The report uses **Tailwind via CDN** for layout and styling, and **Mermaid via CDN** for diagrams where a graph/flow/sequence reliably communicates the structure. Mix Mermaid with hand-crafted CSS/SVG visuals: use Mermaid when relationships are graph-shaped (call graphs, dependencies, sequences), and hand-built divs/SVG when you want something more editorial (mass diagrams, cross-sections, collapse animations). Each candidate gets a **before/after visualisation**. Be visual.

For each candidate, render a card with:

- **Files**: which files/modules are involved
- **Problem**: why the current architecture is causing friction
- **Solution**: plain English description of what would change
- **Benefits**: explained in terms of locality and leverage, and how tests would improve
- **Before / After diagram**: side-by-side, custom-drawn, illustrating the shallowness and the deepening
- **Recommendation strength**: one of `Strong`, `Worth exploring`, `Speculative`, rendered as a badge

End the report with a **Top recommendation** section: which candidate you'd tackle first and why.

See [HTML-REPORT.md](HTML-REPORT.md) for the full HTML scaffold, diagram patterns, and styling guidance.

Do NOT propose interfaces yet. After the file is written, ask the user: "Which of these would you like to explore?"

### 3. Grill the pick

Once the user picks a candidate, run the [**grill-me**](../grill-me/SKILL.md) skill on it: constraints, dependencies, the shape of the deepened module, what sits behind its interface, what tests survive. To explore alternative interfaces for the deepened module, run the [**architect**](../architect/SKILL.md) skill.

### 4. Build it

Once the user confirms, build the candidate per the [Refactoring playbook](../tialo-mode/playbooks/refactoring.md), starting at its step 1. A candidate that changes behavior routes to the [Feature playbook](../tialo-mode/playbooks/feature.md).
