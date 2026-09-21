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
- Chapter 9 is a short lecture script, assumes neural encoders have already been
  taught, and ends with a generation label but no generation section.
- Chapters 7, 8, and 10 contain roughly ten thousand or more source words each;
  Chapter 2 contains about two thousand. Counts guide review, not padding.
- Chapter 10 retains paper experiments, supplementary sections, and unfinished
  final sections. Separate its core teaching narrative from research detail.
- Chapter 13 introduces objective functions and training data after Chapter 9
  already assumes them. Establish prerequisites earlier and refer back in the
  discussion of risks. Avoid duplicating the technical explanations.
- The introduction inputs both a blurb and an about section with repeated prose;
  consolidate them and revise the book roadmap against the actual chapters.
- Recover missing bibliography entries from supplied source projects where
  possible. Verify identities and claim support before adding entries; do not
  fabricate bibliographic records or substitute merely similar papers.
- Missing tables, appendices, and their methods need recovery or a supported
  rewrite. A label alone would not resolve the missing content.

## Remaining author notes

- Global: distinguish present-year references from historical dates; normalize
  quizbowl and Jeopardy macros; replace video-script directions; use singular
  author voice and acknowledge student contributions in front matter.
- Explain the question-box design at its first actual use, including the
  Jeopardy and Jurafsky/Martin connections.
- Relocate the standardized-test history from Chapter 10 to the historical
  discussion, with transitions and without repetition.
- Chapter 3: repair author rendering, add Turing citations, and shorten the
  Diplomacy discussion and remove the requested figure after checking references.
- Chapter 4: reorganize SHRDLU paragraphs, explain ambiguity resolution with
  primary-source support, strengthen the closing section, and consider the
  requested tf-idf and relational-table figures.
- Chapter 5: cite the work with Pedro explicitly; locate a sourced
  Turing/Manchester question for the author to discuss its pyramidality; verify
  Turing's Manchester affiliation in 1950. The missing University Challenge
  bibliography entry `taylor_mcnulty_meek` has been recovered from `pedro.bib`.

## Verification still required

No LaTeX compiler was found on PATH. Locate or provision a usable build toolchain,
generate blurbs, compile with bibliography and index, resolve errors and warnings,
and inspect the rendered book. Review all chapter transitions, factual support,
duplication, technical prerequisites, and length/depth balance. Do not treat a
clean source scan as proof that the editor draft is ready.
