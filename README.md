# questioning-aritifical-intelligence
A Book on QA

## Review uncommitted edits

Run `make diff` to compare the current working tree with `HEAD` (the last
commit). The marked-up PDF is `build/latexdiff/main-diff.pdf`. This includes
staged and unstaged edits, plus new, non-ignored chapter files. To compare
against another revision, use `make diff DIFF_BASE=HEAD~1`.

Requires Python 3.9+, Git, and a TeX distribution providing `latexdiff`,
`pdflatex`, `bibtex`, and `makeindex` (latexdiff also needs Perl).
Use `make diff PYTHON=python` if needed.

Python only prepares the sources (`make diff-sources`, or
`python scripts/build_diff.py`). The Makefile runs each `pdflatex`, `bibtex`,
and `makeindex` command directly, stopping at the failing command.
Both `make diff` and `make diff-pdf` reuse up-to-date outputs. Source changes,
added/deleted input files, or a different baseline commit regenerate the sources.
Otherwise, a failed build resumes at the missing or outdated output: a BibTeX
failure does not repeat source generation or the successful first LaTeX pass.
The bibliography, index, and final PDF are separate file targets. A small manifest
check runs each time without changing timestamps when its contents are unchanged.
`build/latexdiff` is this generated directory, not the installed `latexdiff`
executable. For a BibTeX-only retry, run
`cd build/latexdiff && bibtex main-diff`; its log is `main-diff.blg` there.

The build uses separate snapshots and regenerates chapter summaries for each
revision. If an older baseline lacks `scripts/split_blurbs.py`, it uses the current
generator with the baseline's own `chapter_blurbs.json` and prints a notice.
Preparation errors identify the step, snapshot or file, working directory, and
command; the underlying tool's output remains visible.
It marks changes to main.tex and chapter text, including question and
evidence excerpts. Current styles, images, and bibliography files are used;
formatting-only changes, changed image contents, and bibliography-record edits
are not individually highlighted. Entirely removed chapter files are omitted.
Graphics highlighting is disabled to keep diff markers compatible with table
alignment commands such as `\multicolumn`; text highlighting remains enabled.
The sample book index in Chapter 4 appears in its current form without change
highlighting, so latexdiff does not process its table layout.
The normal manuscript and main.pdf are untouched. Source regeneration replaces
the generated `build/latexdiff` directory; compilation retries retain it and its
logs. Running `python scripts/build_diff.py` directly forces source regeneration.
