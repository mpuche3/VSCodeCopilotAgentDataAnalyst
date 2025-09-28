#!/usr/bin/env python3
import argparse, sys, os, datetime, re

LESSONS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "lessons_learned.md")
LESSONS_FILE = os.path.abspath(LESSONS_FILE)

def prepend_text(path, text):
    with open(path, "r", encoding="utf-8") as f:
        existing = f.read()
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n\n" + existing)

def main():
    p = argparse.ArgumentParser(description="Append a structured Reflection Entry to lessons_learned.md (prepends at top).")
    p.add_argument("--task", required=True, help="Short task title")
    p.add_argument("--summary", default="", help="2–5 bullet points summary")
    p.add_argument("--pitfalls", default="", help="Pitfalls & fixes")
    p.add_argument("--improvements", default="", help="Improvements next time")
    p.add_argument("--artifacts", default="", help="Comma-separated paths")
    p.add_argument("--tags", default="analysis,data", help="Comma-separated tags")
    p.add_argument("--glossary", default="", help="Semicolon-separated 'TERM: definition' pairs to also add into docs/glossary.yml")
    args = p.parse_args()

    date = datetime.date.today().isoformat()
    artifacts = [a.strip() for a in args.artifacts.split(",") if a.strip()]
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    def bullets(text):
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        return "\n".join([f"- {l}" for l in lines]) if lines else "- (none)"

    header = f"""---
date: {date}
task: "{args.task}"
artifacts: {artifacts}
tags: {tags}
---"""

    entry = f"""{header}
**Summary:**
{bullets(args.summary)}

**Pitfalls & Fixes:**
{bullets(args.pitfalls)}

**Improvements Next Time:**
{bullets(args.improvements)}

**Glossary Updates:**
{'; '.join([g.strip() for g in args.glossary.split(';') if g.strip()]) or '(none)'}
"""

    # Ensure file exists
    if not os.path.exists(LESSONS_FILE):
        with open(LESSONS_FILE, "w", encoding="utf-8") as f:
            f.write("# Lessons Learned\n\n")

    prepend_text(LESSONS_FILE, entry)

    # Also write to docs/glossary.yml if provided
    if args.glossary.strip():
        gpath = os.path.abspath(os.path.join(os.path.dirname(LESSONS_FILE), "docs", "glossary.yml"))
        os.makedirs(os.path.dirname(gpath), exist_ok=True)
        if not os.path.exists(gpath):
            with open(gpath, "w", encoding="utf-8") as f:
                f.write("# Glossary (YAML)\n\n")
        with open(gpath, "a", encoding="utf-8") as f:
            for pair in args.glossary.split(";"):
                pair = pair.strip()
                if not pair: continue
                if ":" not in pair: continue
                term, definition = pair.split(":", 1)
                f.write(f"{term.strip()}: \"{definition.strip()}\"\n")
    print("Reflection entry added.")

if __name__ == "__main__":
    main()
