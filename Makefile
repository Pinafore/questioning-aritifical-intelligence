
TEX = $(wildcard chapters/*.tex *.tex */*.tex)
GFX = $(wildcard figures/*.*)
BIB = $(wildcard bib/*.bib)

clean:
	rm *.aux *.pdf *.bbl *.idx main.blg *.out *.log *.lot *.toc

chapters/blurbs/qb.tex: chapter_blurbs.json scripts/split_blurbs.py
	mkdir -p chapters/blurbs
	python3 scripts/split_blurbs.py

main.aux: $(BIB) main.tex chapters/blurbs/qb.tex
	pdflatex main
	bibtex main
	pdflatex main

main.pdf: $(TEX) $(GFX) main.aux
	pdflatex main
	cp main.pdf ../jbg-web/teaching/CMSC_848/textbook.pdf
