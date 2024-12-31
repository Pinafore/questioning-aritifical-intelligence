
import json


if __name__ == "__main__":
    with open("chapter_blurbs.json", 'r') as infile:
        raw = infile.read()
        blurbs = json.loads(raw)

    for ii in blurbs:
        with open("chapters/blurbs/%s.tex" % ii, 'w') as outfile:
            if isinstance(blurbs[ii], list):
                text, subsections = blurbs[ii]
            else:
                text = blurbs[ii]
                subsections = []
                
            outfile.write(text)

            sections = []
            for ii in subsections:
                if len(ii) > 2:
                    label, section_name, description = ii
                    sections.append((section_name, description))
                else:
                    label, section_name = ii
                outfile.write("\n\\invisiblesection{%s}{%s}\n\n" % (section_name, label))

            if len(sections) > 1:
                outfile.write("Topics in chapter:\\n\\begin{enumerate*}")
                outfile.write("\n\t".join("\\item \\textbf{%s:} %s" % (x, y) for x, y in sections))
                outfile.write("\n\\end{enumerate*}")
