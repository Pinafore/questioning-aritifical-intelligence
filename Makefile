
.DEFAULT_GOAL := main.pdf
.PHONY: clean publish parts diff diff-sources diff-pdf diff-input-check
.DELETE_ON_ERROR:

PYTHON ?= python3
DIFF_BASE ?= HEAD

# Track current source files, including additions and deletions, and the resolved
# baseline commit. The inexpensive manifest check does not change its timestamp
# unless the file list or baseline changes.
DIFF_INPUTS = $(sort $(wildcard $(shell git ls-files --cached --others --exclude-standard -- main.tex chapter_blurbs.json chapters style bib figures scripts/build_diff.py scripts/split_blurbs.py Makefile) $(shell git ls-files --others --ignored --exclude-standard -- figures style bib)))
DIFF_MANIFEST = build/latexdiff-inputs.txt

$(DIFF_MANIFEST): diff-input-check
	@mkdir -p build
	@git rev-parse --verify "$(DIFF_BASE)^{commit}" > $@.tmp
	@printf '%s\n' $(DIFF_INPUTS) >> $@.tmp
	@cmp -s $@.tmp $@ || mv $@.tmp $@
	@rm -f $@.tmp

diff diff-pdf: build/latexdiff/main-diff.pdf

diff-sources: build/latexdiff/main-diff.tex

build/latexdiff/main-diff.tex: $(DIFF_MANIFEST) $(DIFF_INPUTS)
	$(PYTHON) scripts/build_diff.py --base "$(DIFF_BASE)"
	touch $@

# LaTeX rewrites .aux/.idx on every pass, so use a successful first-pass stamp
# as the dependency for BibTeX and MakeIndex rather than creating a timestamp loop.
build/latexdiff/first-pass.stamp: build/latexdiff/main-diff.tex
	cd build/latexdiff && pdflatex -interaction=nonstopmode -halt-on-error main-diff.tex
	touch $@

build/latexdiff/main-diff.bbl: build/latexdiff/first-pass.stamp
	cd build/latexdiff && bibtex main-diff

build/latexdiff/main-diff.ind: build/latexdiff/first-pass.stamp
	cd build/latexdiff && makeindex main-diff

build/latexdiff/main-diff.pdf: build/latexdiff/first-pass.stamp build/latexdiff/main-diff.bbl build/latexdiff/main-diff.ind
	cd build/latexdiff && pdflatex -interaction=nonstopmode -halt-on-error main-diff.tex
	cd build/latexdiff && pdflatex -interaction=nonstopmode -halt-on-error main-diff.tex

TEX = $(wildcard chapters/*.tex *.tex */*.tex)
GFX = $(wildcard figures/*.*)
BIB = $(wildcard bib/*.bib)

clean:
	rm *.aux *.pdf *.bbl *.idx main.blg *.out *.log *.lot *.toc chapters/blurbs/*

chapters/blurbs/watson.tex: chapter_blurbs.json scripts/split_blurbs.py
	mkdir -p chapters/blurbs
	python3 scripts/split_blurbs.py --draft_sections --proposal_sections

main.aux: $(BIB) main.tex chapters/blurbs/watson.tex
	pdflatex main
	bibtex main
	pdflatex main

main.pdf: $(TEX) $(GFX) main.aux chapter_blurbs.json scripts/split_blurbs.py
	pdflatex main
	makeindex main
	pdflatex main

publish: main.pdf
	cp main.pdf ../jbg-web/teaching/CMSC_848/textbook.pdf

parts: main.pdf
	pdfseparate main.pdf 
