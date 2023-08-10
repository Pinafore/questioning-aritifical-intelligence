
import json


if __name__ == "__main__":
    with open("chapter_blurbs.json", 'r') as infile:
        raw = infile.read()
        blurbs = json.loads(raw)

    for ii in blurbs:
        with open("chapters/blurbs/%s.tex" % ii, 'w') as outfile:
            outfile.write(blurbs[ii])
