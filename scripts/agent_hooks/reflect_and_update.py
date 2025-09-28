#!/usr/bin/env python3
"""Guide agent or user to synthesize lessons from artifacts.
Currently, this utility just extracts plain-text headings from notebooks or md files and
provides a draft summary to paste into lessons.
"""
import argparse, os, json, re, nbformat

def draft_from_notebook(path):
    nb = nbformat.read(path, as_version=4)
    headings = []
    for cell in nb.cells:
        if cell.cell_type == "markdown":
            for line in cell.source.splitlines():
                if line.strip().startswith("#"):
                    headings.append(line.strip().lstrip("# ").strip())
    bullets = "\n".join(f"- Section: {h}" for h in headings[:8]) or "- (no headings found)"
    return bullets

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("artifact", help="Notebook (.ipynb) or Markdown (.md)")
    args = ap.parse_args()
    path = os.path.abspath(args.artifact)
    if path.endswith(".ipynb"):
        summary = draft_from_notebook(path)
    elif path.endswith(".md"):
        with open(path, "r", encoding="utf-8") as f:
            lines = [l.strip() for l in f if l.strip()]
        summary = "\n".join(f"- {l[:120]}" for l in lines[:8])
    else:
        summary = "- (unsupported file type)"
    print("DRAFT SUMMARY BULLETS:\n" + summary)

if __name__ == "__main__":
    main()
