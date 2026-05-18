---
name: academic-review-workflow
description: Create and execute structured academic review-paper projects from a reusable folder template. Use when Codex needs to scaffold a literature-review/report workspace, turn README requirements into an ordered writing plan, coordinate academic-paper-strategist and academic-paper-composer, enforce downloaded-paper-only citations, or run final checks for citation frequency, figure references, topic fit, abstract fidelity, and reviewer-style quality control.
---

# Academic Review Workflow

Use this skill as the orchestration layer around an academic review project.

## Core workflow

1. Create the project folder.
   - Choose the template before writing:
     - `assets/project-template` for CJME / Chinese-journal style papers.
     - `assets/project-template-ieee` for IEEE-like single-column course reports; keep every top-level section on a fresh page in this template.
   - Use `examples/` only as finished reference projects, not as clean starters.
   - Keep the same layout: `docs/`, `docs/sections/`, `refs/papers/`, `refs/notes/`, `refs/bib/`, `assets/`.

2. Read and update `README.md` before writing.
   - Treat it as the source of truth for page count, word count, topic, citation rules, image rules, formatting rules, and submission constraints.
   - Replace every placeholder before substantive drafting.

3. Plan before drafting.
   - Use `academic-paper-strategist` first for topic confirmation, search strategy, gap analysis, source selection, and outline design.
   - Do not draft the paper until the topic, outline, and evidence base are coherent.

4. Build the evidence base before drafting.
   - Download the required real papers into `refs/papers/` first.
   - Maintain `refs/notes/paper_index.md` as the allowed-citation ledger. Prefer recording a local PDF link for each key; the checker accepts a key-only row but cannot verify a file path from it.
   - Add only real sources to `refs/bib/references.bib`.
   - Do not cite undownloaded papers.

5. Draft in order.
   - Then use `academic-paper-composer` to write from the approved outline.
   - Use numbered headings in the required style: `1.` / `1.1` / `1.1.1`.
   - For IEEE-style course reports, preserve the template rule that every top-level `\section` begins on a new page.
   - Write the “总结与展望” or “结论” section in a total-part-total structure. The middle summary points must be formatted as `（1）` / `（2）` / `（3）`, and each point must be its own standalone paragraph rather than compressed into one block.
   - Keep the prose under each heading substantive: avoid thin one- or two-sentence sections; ensure each section develops a clear claim, supporting explanation, and coherent transition so the paper remains content-rich, logically clear, and well layered.
   - During the first drafting pass, add about 3-5 mathematical formulas when the topic reasonably supports them. Every formula must come from a textbook or paper and retain a clear citation to its source; do not invent decorative formulas merely to satisfy a quota.
   - Leave figure placeholders first; tell the author to capture reference-paper figures into `assets/` later.

6. Revise as a reviewer, not as a copyeditor.
   - Remove course-like phrasing such as “从课程内容看”“课程要求表明”.
   - Check topic alignment, argument continuity, section balance, paragraph sufficiency, prose clarity, abstract-body consistency, and useless material.
   - When Chinese prose polish matters, use `humanizer-zh` after the substantive revision pass to polish expression while preserving content density, logical clarity, and hierarchical structure.
   - When the paper is technical/CS-oriented, also use `academic-research-writing`.

7. Run deterministic checks before declaring completion.
   - Use `scripts/check_review_project.py <project_root>`.
   - This script only performs mechanical checks; fix any violations it reports, then rerun until clean.

## Required final checks

- Every cited paper appears in `refs/notes/paper_index.md`; use local PDF links there when you want the checker to verify file existence.
- Every reference stays within the citation-frequency rule in `README.md`.
- The paper reaches the README minimum reference count when that count is numeric.
- Every figure label is referenced exactly once, and every figure reference resolves to an actual figure label.
- When the topic supports formulas, the first full draft includes about 3-5 source-backed mathematical formulas, each traceable to a textbook or paper rather than invented ad hoc. Check this manually.
- In IEEE-style course reports, every top-level section begins on a fresh page. Check this manually after compilation.
- The conclusion section uses a total-part-total structure, and numbered summary points `（1）` / `（2）` / `（3）` appear as separate standalone paragraphs. Check this manually.
- Paragraphs under each heading are sufficiently developed rather than perfunctory, with clear logic, adequate content, and distinct levels of argument. Check this manually.
- Abstract, title, keywords, and body all match the same topic. Check this manually.
- No personal information remains in reusable templates.

## Validation

- Run `scripts/check_review_project.py <project_root>` before delivery.
- It checks citation frequency, bibliography entries, paper-index coverage, optional local PDF links, minimum citation count, and figure-reference mechanics.
