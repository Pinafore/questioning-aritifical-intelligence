# Original notes: status after the methods-script pass

Checked against the original pasted notes and current source on 2026-09-21.
“Done” here means edited in source, not verified in a compiled PDF.

## Still open

- Global consistency: finish the book-wide pass for authorial “I”, video directions,
  present-year wording, and quizbowl macros. Preserve historical dates and
  pedagogical “we” where it means author and reader together.
- Move the standardized-test history out of `240-leaderboards.tex` into the
  historical discussion. Keep the psychometric methods with leaderboards.
- Chapter 3: add the Turing-machine reference; shorten Joy's Diplomacy
  discussion and remove the requested figure.
- Chapter 4: explain SHRDLU's ambiguity resolution and limitations with references
  to specific Winograd chapters. The author supplies this new explanation and
  the expanded closing section.
- Chapter 5: explicitly cite the paper with Pedro; select a sourced
  Turing/Manchester quizbowl question; the author writes the pyramidality walkthrough.
- Optional figures: the tf-idf example and SELECT/WHERE on small tables.
- Review the earlier added passages listed in `author-review.md`, particularly
  the assistant-written “That history matters” transition.

## Done in source

- Introduction: NTU/Maryland history and the book's lecture/course origins.
- Student-contribution acknowledgment in front matter.
- Current-year macro introduced and used for identified present-year statements.
- Question-box explanation at its first use in the tf-idf section.
- Chapter 2: Oedipus as a Greek story; model-training connection; clarification
  of Odin's role and the reference to Turing. Earlier prose remains reviewable.
- Chapter 3: Wilcox author metadata; “effectively read all of the Internet”;
  citations to Hodges's *Alan Turing: The Enigma* (1983) and Tyldum's
  *The Imitation Game* (2014).
- Chapter 4: recursion alignment, Maryland wording, F1 equation, Siraj punctuation,
  e-reader footnote, Linotype recap, SHRDLU paragraph organization and figure credit,
  and the “small and brittle” wording. The new technical explanation is still open.
- Chapter 5: College Bowl history adapted from the supplied `20-task.tex`, and a
  primary institutional citation for Turing being at Manchester in 1950.
- Leaderboards already has its own chapter (`240-leaderboards.tex`), and Chapter 5
  points to it. Whether to merge them remains an authorial structural choice.
- Jeopardy macros checked for their distinct sentence-ending form; no extra
  sentence punctuation was found in that earlier pass. Repeat during final proofing.

## Added note: ROUGE duplication

- Done in source: detailed BLEU/ROUGE explanation and critique now reside in
  `230-methods.tex`, under `sec:methods:long-answers`.
- `210-formats.tex` retains the dataset discussion and points forward to that
  section and `sec:methods:preferences`.
- Corrected the Conan example to three matching bigrams out of twenty (0.15).
  Its seven-token longest common subsequence, precision 7/17, and recall 7/21
  were checked against the actual example strings.

## New script follow-up

See `methods-review.md` for missing source material and uncertain citations.
The separate full-book draft plan includes additional gaps beyond these original notes.
