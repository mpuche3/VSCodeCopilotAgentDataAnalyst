# Copilot Data Analyst Agent Repo (Self-Learning)

This repository is a **turn‑key workspace** for using **GitHub Copilot – Agent Mode** as a *data analyst* in **VS Code** with **Python + Jupyter**.

It adds a simple but powerful *persistent memory* pattern so the agent can **learn from every task** and **reuse that knowledge** next time:
- A project‑level instruction file for the agent (`.github/copilot-instructions.md`).
- A growing knowledge base: **`lessons_learned.md`** (glossary, systems, playbooks, pitfalls).
- A lightweight reflection workflow and utilities in `scripts/agent_hooks/` to **append lessons** automatically or via prompts.
- Notebook templates and examples for EDA, cleaning, and reporting.

> Works even if Agent Mode doesn't auto-detect instruction files: the instructions include a *Startup Ritual* telling the agent to read `lessons_learned.md` and `docs/*` first.

## Quickstart

1. **Open in VS Code** (with Python, Jupyter, and GitHub Copilot Chat extensions).
2. Open **Copilot Chat**, select **Agent Mode** (if available).
3. Run the startup message (paste or click the repo task card):  
   **“Load project context and be my Data Analyst. Read `.github/copilot-instructions.md`, `lessons_learned.md`, and `docs/` before doing anything.”**
4. Start with the example: open `notebooks/examples/01_eda_on_sample.ipynb` and ask:  
   **“Perform a quick EDA using our conventions. Then reflect and update `lessons_learned.md`.”**

## Reflection & Memory

- After any task, the agent writes a **Reflection Entry** into `lessons_learned.md` using the template in that file (with YAML header).
- If needed, run:  
  ```bash
  python scripts/agent_hooks/append_lesson.py --task "Quick EDA on sample data" --summary "…" --pitfalls "…" --improvements "…" --glossary "QTD: quarter to date; SKU: stock keeping unit"
  ```
- Prefer the agent to **edit the file directly** (per instructions), but the script helps standardize entries.

## Repo Layout

```
.
├─ .github/
│  └─ copilot-instructions.md      # Agent mission, rituals, rules, reflection protocol
├─ .vscode/
│  ├─ extensions.json              # Recommended extensions
│  └─ settings.json                # Sensible defaults for notebooks & linting
├─ docs/
│  ├─ data_context.md              # Where to document datasets, DBs, systems
│  ├─ glossary.yml                 # YAML glossary; agent keeps in sync with lessons
│  └─ prompts/
│     ├─ system.md                 # System prompt (redundant with .github file)
│     ├─ reflection.md             # Reflection prompt
│     └─ knowledge_update.md       # How to capture new org/domain knowledge
├─ scripts/
│  └─ agent_hooks/
│     ├─ append_lesson.py          # CLI to append structured lesson entries
│     └─ reflect_and_update.py     # Guide agent to parse artifacts & update lessons
├─ notebooks/
│  ├─ templates/
│  │  ├─ EDA_template.ipynb
│  │  ├─ cleaning_template.ipynb
│  │  └─ dashboard_template.ipynb
│  └─ examples/
│     └─ 01_eda_on_sample.ipynb
├─ data/
│  └─ sample/
│     └─ sales.csv
├─ reports/.gitkeep
├─ lessons_learned.md              # Persistent memory
└─ README.md
```

## Notes

- If Agent Mode settings change, this repo still works: the **instructions prompt** and **startup ritual** make the agent load context explicitly.
- Keep `lessons_learned.md` tidy. When it grows large, ask the agent to **summarize/archive** older entries.
- Extend with company specifics: add DB connection how‑tos and link your internal data dictionary to `docs/`.
