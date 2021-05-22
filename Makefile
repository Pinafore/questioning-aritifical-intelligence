
TEX = $(wildcard chapters/*.tex *.tex */*.tex)
GFX = $(wildcard figures/*.*)
BIB = $(wildcard bib/*.bib)

clean:
	rm *.aux *.pdf *.bbl *.idx main.blg *.out *.log *.lot *.toc

main.aux: $(BIB) main.tex
	pdflatex main
	bibtex main
	pdflatex main

main.pdf: $(TEX) $(GFX) main.aux
	pdflatex main
