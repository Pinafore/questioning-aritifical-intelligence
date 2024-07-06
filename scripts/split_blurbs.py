
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

            for ii in subsections:
                label, section_name = ii
                outfile.write("\\invisiblesection{%s}{%s}\n" % (section_name, label))
