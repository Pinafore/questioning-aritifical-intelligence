
import json


if __name__ == "__main__":
    with open("chapter_blurbs.json", 'r') as infile:
        raw = infile.read()
        blurbs = json.loads(raw)

    for blurb in blurbs:
        short = blurb["short"]
        with open("chapters/blurbs/%s.tex" % short, 'w') as outfile:
            text = blurb["summary"]
            sections = blurb.get("sections", [])

            outfile.write("%s\n\n" % text)

            has_summary = False
            if any("summary" in x for x in sections):
                has_summary = True
                outfile.write("\\ifproposal \n \\noindent Topics in chapter:\n\\begin{enumerate*}")                

            for section in sections:
                section_name = section["label"]
                title = section.get("title", "MISSING TITLE")
                outfile.write("\n\\invisiblesection{sec:%s:%s}{%s}\n\n" % (short, section_name, title))

                if "summary" in section:
                    outfile.write("\\item \\textbf{%s:} %s {\\tiny %s:%s} \n" % (title, section["summary"], short, section_name))

            if has_summary:
                outfile.write("\n\\end{enumerate*}\n\\fi")



