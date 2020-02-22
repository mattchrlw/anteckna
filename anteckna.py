#!/usr/bin/env python

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
    # Skip the first line
    toc = f"# Table of Contents\n\n{md_toc.build_toc(filename, skip_lines=1)}\n"
    # Add a date, too.
    date = f"_Last updated {datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%B %d, %Y at %H:%M')}._\n"

    # Write new .md to destination file.
    dest.writelines(title)
    dest.writelines("\n\n")
    dest.writelines(date)
    dest.writelines("\n")
    dest.writelines(toc)
    dest.writelines(doc)

    dest.close()
    source.close()

    # Create pdf file
    sub.call(["pandoc", filename, "--toc", "-o", filename.replace("src/", "pdf/").replace(".md", ".pdf"), \
                                "-V", "geometry:margin=2cm", \
                                "-V", "fontsize=12pt", \
                                "--shift-heading-level-by=-1", \
                                "--metadata", f"date={date.replace('_', '')}"])
    # Create html file
    sub.call(["pandoc", filename.replace("src/", "dest/"),
                                "--quiet", \
                                "-s", \
                                "-H", "css/github-markdown-css.txt", \
                                "--mathjax", \
                                "-T", title, \
                                "-o", filename.replace("src/", "web/").replace(".md", ".html")])
    print("Processing of", os.path.join(root, file), "completed.")

"""
Iterate through all files in the src folder and create clean versions.
"""
def process():
    for root, _, files in os.walk('src'):
        for file in files:
            if os.path.splitext(file)[1] == ".md":
                cleanup(root, file)

if __name__ == "__main__":
    process()