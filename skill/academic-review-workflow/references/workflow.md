# Academic Review Project Checklist

## 1. Start from a copy, never from a blank page

1. Copy `example/科技论文写作` and rename it, or use `assets/project-template`.
2. Edit `README.md` first.
3. Confirm:
   - topic
   - target length/page count
   - minimum number of papers
   - citation-frequency rule
   - figure policy
   - required format
   - forbidden wording

## 2. Work in this order

1. Confirm requirements from `README.md`.
2. Use `academic-paper-strategist`:
   - define topic boundary
   - identify top venues and representative papers
   - test originality/fit
   - produce the outline
3. Download the required real papers into `refs/papers/`.
4. Record the approved paper set in `refs/notes/paper_index.md`.
5. Add matching BibTeX entries to `refs/bib/references.bib`.
6. Use `academic-paper-composer` to draft sections in outline order.
7. Add formulas only from textbooks or papers and cite the source.
8. Reserve figure positions first. Ask the author to screenshot source figures into `assets/`.
9. Revise for:
   - topic fit
   - abstract-body consistency
   - logic and transitions
   - redundant passages
   - professional reviewer standard
10. Run automated checks, repair, rerun.

## 3. Non-negotiable writing rules

- Use `1.` / `1.1` / `1.1.1` heading hierarchy.
- Write “总结与展望” or “结论” in a total-part-total structure, using `（1）` / `（2）` / `（3）` for the middle summary points.
- Do not cite papers that are not downloaded locally.
- Do not let any one reference appear more than twice unless the project rules say otherwise.
- Every figure must be cited exactly once.
- Do not use course-framing language such as:
  - `从课程内容看`
  - `课程中提到`
  - `根据课程要求`
- If the project is a short review, keep all sections serving one central review question.

## 4. Figure handling

- During drafting, leave explicit placeholders.
- Tell the author:
  - screenshot figures from the approved reference papers
  - save them into `assets/`
  - keep filenames stable once cited
- Before final delivery:
  - each figure label must exist once
  - each figure label must be referenced exactly once

## 5. Formula handling

- Prefer canonical formulas already used in the field.
- Every inserted formula should be traceable to a textbook or paper in the allowed source set.
- Do not invent formulas to decorate the paper.

## 6. Final reviewer pass

Read the paper as if deciding whether it meets the assignment brief:

1. Is the paper genuinely about the requested topic?
2. Does the abstract faithfully summarize the paper that was actually written?
3. Is the section order natural?
4. Does each subsection earn its place?
5. Are references sufficient, real, and used with discipline?
6. Are the visuals and formulas functional rather than ornamental?
7. Is the prose clear, fluent, and free of irrelevant course-language?
