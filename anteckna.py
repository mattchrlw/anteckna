import md_toc
import subprocess as sub
import os
from datetime import datetime

"""
"Cleanup" an individual file, adding a table of contents and date.
"""
def cleanup(root, file):
    # Reads first line as header, then inserts table of contents, then writes the rest.
    filename = os.path.join(root, file)
    source = open(filename, "r")
    dest = open(filename.replace("src/", "dest/"), "w")

    title = source.readline()
    doc = source.readlines()
    toc = f"# Table of Contents\n\n{md_toc.build_toc(filename)}\n"
    # Add a date, too.
    date = f"_Last updated {datetime.today().strftime('%d %B, %Y')}._\n"

    dest.writelines(title)
    dest.writelines("\n\n")
    dest.writelines(date)
    dest.writelines("\n")
    dest.writelines(toc)
    dest.writelines(doc)

    dest.close()
    source.close()

    # Create pdf file
    sub.call(["pandoc", filename, "--toc", "-o", filename.replace("src/", "pdf/").replace(".md", ".pdf")])
    # Create html file
    sub.call(["pandoc", filename.replace("src/", "dest/"),
                                  "--quiet", \
                                  "-s", \
                                  "-H", "css/github-pandoc-css.txt", \
                                  "--mathjax", \
                                  "-T", title, \
                                  "-o", filename.replace("src/", "web/").replace(".md", ".html")])

"""
Iterate through all files in the src folder and create clean versions.
"""
def process():
    for root, dirs, files in os.walk('src'):
        for file in files:
            if os.path.splitext(file)[1] == ".md":
                cleanup(root, file)

if __name__ == "__main__":
    process()