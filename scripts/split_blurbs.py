
import json


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--draft_sections", action="store_true")
    parser.add_argument("--proposal_sections", action="store_true")

    flags = parser.parse_args()

    print("Draft sections:", flags.draft_sections)
    print("Proposal sections:", flags.proposal_sections)

    with open("chapter_blurbs.json", 'r') as infile:
        raw = infile.read()
        blurbs = json.loads(raw)

    for blurb in blurbs:
        short = blurb["label"]
        with open("chapters/blurbs/%s.tex" % short, 'w') as outfile:
            text = blurb["summary"]
            sections = blurb.get("sections", [])

            outfile.write("%s \\\\ \n\n" % text)

            titles = ["\t\\item \\textbf{%s.} %s" % (x["title"], x.get("summary", "")) for x in sections if "title" in x]
            labels = ["\t\\invisiblesection{%s}{sec:%s:%s}" % (x.get("title", ""), short, x["label"]) for x in sections]

            outfile.write("\\ifproposal \n")
            # Always write the labels
            outfile.write("\n".join(labels))
            outfile.write("\n\\fi")


            if (flags.proposal_sections or flags.draft_sections) and any("summary" in x for x in sections):
                if not flags.draft_sections:
                    outfile.write("\\ifproposal \n")
                
                outfile.write("\\noindent Topics in chapter:\n\\begin{enumerate*}\n\t")
                outfile.write("\n".join(titles))                
                
                outfile.write("\n\\end{enumerate*}")
                if not flags.draft_sections:
                    outfile.write("\n\\fi")

            # Create stubs for the section if it is the proposal
            # outfile.write("\\ifproposal \n")
            # for section in sections:
            #    section_name = section["label"]
            #    title = section.get("title", "MISSING TITLE")
            #    outfile.write("\n\\invisiblesection{%s:%s}{%s}\n\n" % (short, section_name, title))
            #outfile.write("\\fi")
            



