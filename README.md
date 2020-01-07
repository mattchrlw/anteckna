# Anteckna

## Description

> _att anteckna_: to note. (Swedish)

GitHub repos are a nice enough place to dump `.md` notes, but they really don't showcase them that well. (Plus, they're missing a bunch of features, like _actual math support_). The aim of this project is to create a system that allows one to write a bunch of Markdown-format notes and get them in a form of a **repository of notes** (with customisable CSS and all!)

This project aims to be a middleground between full-strength LaTeX (which has its uses) and Markdown (which while incredibly simple, lacks flexibility for certain use-cases).

The aim is to make this system as simple as possible; the process consists o
1. Cleaning up Markdown and adding table of contents, dates and other useful info that would make the Markdown resemble a standard webpage;
2. Passing the Markdown through `pandoc` to obtain PDF outputs of TeX files (for printing, assignments etc);
3. Passing the cleaned up Markdown through `pandoc` to obtain a HTML webpage, with KaTeX support;
4. Constructing a webpage using some frameworks (???);
5. Profit(-ing)!

Currently, the project is up to *step 3* (but very barely there).

## Prerequisites

- Python 3 (of some sort)
- `pip install md-toc` for generating table of contents

## Usage

(Only tested on Unix systems, sorry Windows users)

1. Clone the repo to your computer using `git clone https://github.com/mattchrlw/anteckna`.
2. `cd` to the repo and drop Markdown files in the `src` folder, ensuring they only have *one h1 heading* (might still work with more than one, but results may vary).
3. Run `python anteckna.py`. This should create PDF outputs in the `pdf` folder, webpages in the `web` folder and `.md` files with TOCs and dates in the `dest` folder.
4. Up to you! Incorporate this script into your Markdown workflow or whatever.

## Notes

- You may notice that in the `css` folder, the CSS files are in `.txt` format and have `<style>` HTML tags wrapped around them. Why? For true portability when generating webpages; see [this fantastic blogpost](https://devilgate.org/blog/2012/07/02/tip-using-pandoc-to-create-truly-standalone-html-files/) for more information.

## Things to fix/clean up

LaTeX output is a bit weird (h1 should be title, not a `\section`).