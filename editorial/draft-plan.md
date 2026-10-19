# Editor draft work plan

Objective: a complete, connected, nonduplicative first-pass book draft, with no
undefined references, reasonably balanced chapter lengths and technical depth,
and a mostly chronological progression of technical prerequisites.

Style authority: https://users.umiacs.umd.edu/~ying/static/style.html
The author's book-specific instruction to use first-person singular takes
precedence over the guide's paper-specific preference for plural authorship.
Preserve quotations; revise surrounding prose for clear topic sentences,
transitions, specific claims, citation context, and consistent LaTeX typography.

## Evidence and immediate priorities

Authorship boundary (author instruction): work in small, interactive batches.
Mechanical fixes, citation/reference repairs, and rewriting existing lecture
scripts are authorized. New prose longer than one sentence must be written by
the author. Do not fill missing chapters, expand arguments, or manufacture
transitions paragraph by paragraph to bypass this limit. Present a focused
writing question when new material is needed. Earlier additions are listed in
`author-review.md`; they remain subject to author review.

- `source-audit.md` is a reproducible source inventory, not a compilation result.
  Run `python scripts/audit_manuscript.py` after reference or structure changes.
- Chapters 11 and 12 lack draft bodies. Identify existing source material for
  author review; ask the author to write missing material. Do not silently drop
  promised chapters.
  Source check: `dynabench.tex` contains the Wallace adversarial-question-writing
  interface and a literary clue example. `game-show.tex` contains an annual
  blind-test proposal already represented in Chapter 5, plus a speech-versus-text
  discussion using a Kilkenny clue. Neither supplies the promised ten-season,
  2035 gameshow narrative in `chapter_blurbs.json`. `modern-qa.tex` only says
  “Write me”. No material moved; ask the author for the gameshow narrative source.
- Chapter 9 now contains the author's expanded methods script, revised on
  2026-09-21. Generation has a real section; missing examples, equations, and
  uncertain citations are tracked in `methods-review.md`.
- Chapters 7, 8, and 10 contain roughly ten thousand or more source words each;
  Chapter 2 contains about two thousand. Counts guide review, not padding.
- Chapter 10 retains paper experiments, supplementary sections, and unfinished
  final sections. Separate its core teaching narrative from research detail.
- Chapter 13 introduces objective functions and training data after Chapter 9
  already assumes them. Establish prerequisites earlier and refer back in the
  discussion of risks. Avoid duplicating the technical explanations.
- The duplicated introductory blurb input has been removed; review the book
  roadmap against the actual chapters.
- Recover missing bibliography entries from supplied source projects where
  possible. Verify identities and claim support before adding entries; do not
  fabricate bibliographic records or substitute merely similar papers.
- Missing tables, appendices, and their methods need recovery or a supported
  rewrite. A label alone would not resolve the missing content.
  The final chapter's `sec:unsup` reference promises a discussion of applications
  and evaluation of unsupervised learning that is not present. Ask the author
  whether this promise belongs in the book before drafting or removing it.

## Remaining author notes

See `original-notes-status.md` for the current item-by-item status of the pasted
notes, including completed changes and the new ROUGE-consolidation item.
See `methods-review.md` for follow-up on the new Chapter 9 script.
The author section also promises named acknowledgments at the end of the book;
the author needs to supply that list or revise the promise.

## Verification still required

No LaTeX compiler was found on PATH or in the standard TeX Live and MiKTeX
installation locations checked on this Windows host. The Makefile now defaults
to building `main.pdf`, runs `makeindex`, and requires an explicit `make publish`
to copy the PDF into the website checkout; these commands have not been run.
Locate or provision a usable build toolchain,
generate blurbs, compile with bibliography and index, resolve errors and warnings,
and inspect the rendered book. Review all chapter transitions, factual support,
duplication, technical prerequisites, and length/depth balance. Do not treat a
clean source scan as proof that the editor draft is ready.


## Diagrams when adapting lecture scripts

Author instruction (2026-10-18): when an explanation adapted from a lecture script needs a diagram, flag it explicitly so the author and editor can recover the figure from the slides. Add a local LaTeX AUTHOR comment stating what the diagram should show and, when known, the source lecture or example. Do not silently replace a necessary visual explanation with prose.

Current candidates from the encoder/decoder adaptation: query–key–value attention and multiple heads in Chapter 7; causal masking versus encoder attention, and encoder–decoder cross-attention in Chapter 9. Review these with the author before retrieving or recreating figures.
