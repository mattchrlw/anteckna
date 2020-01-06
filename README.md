# Anteckna

> att anteckna: to note. (Swedish)

GitHub repos are a nice enough place to dump `.md` notes, but they really don't showcase them that well. (Plus, they're missing a bunch of features, like _actual math support_). The aim of this project is to create a system that allows one to write a bunch of Markdown-format notes and get them in a form of a **repository of notes** (with customisable CSS and all!)

This project aims to be a middleground between full-strength LaTeX (which has its uses) and Markdown (which while incredibly simple, lacks flexibility for certain use-cases).

The aim is to make this system as simple as possible; the process consists o
1. Cleaning up Markdown and adding table of contents, dates and other useful info that would make the Markdown resemble a standard webpage;
2. Passing the Markdown through `pandoc` to obtain PDF outputs of TeX files (for printing, assignments etc);
3. Passing the cleaned up Markdown through `pandoc` to obtain a HTML webpage, with KaTeX support;
4. Constructing a webpage using some frameworks (???);
5. Profit(-ing)!
