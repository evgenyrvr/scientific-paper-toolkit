# Project Architecture

## Folder tree

```text
physics-paper-ai-lab/
├── README.md
├── MEMORY.md
├── docs/
│   ├── 00-vibe-physics-method.md
│   ├── 01-project-architecture.md
│   ├── 02-tools-and-setup.md
│   ├── 03-model-roles.md
│   ├── 04-iteration-protocol.md
│   └── 05-review-and-publication.md
├── .claude/
│   ├── CLAUDE.md
│   ├── rules/
│   │   ├── post-flight-verification.md
│   │   ├── session-logging.md
│   │   └── stall-prevention.md
│   └── skills/
│       ├── scientific-project-orchestrator/
│       │   └── SKILL.md
│       ├── research-question-scope/
│       │   └── SKILL.md
│       ├── literature-review-ledger/
│       │   └── SKILL.md
│       ├── physics-derivation-auditor/
│       │   └── SKILL.md
│       ├── mathematical-consistency-checker/
│       │   └── SKILL.md
│       ├── numerical-experiment-runner/
│       │   └── SKILL.md
│       ├── figure-quality-control/
│       │   └── SKILL.md
│       ├── manuscript-builder/
│       │   └── SKILL.md
│       ├── reviewer-panel/
│       │   └── SKILL.md
│       ├── publication-readiness-auditor/
│       │   └── SKILL.md
│       ├── compress-session/
│       │   └── SKILL.md
│       └── seven-pass-review/
│           └── SKILL.md
├── project/
│   ├── 00_master_plan.md
│   ├── 01_research_question.md
│   ├── 02_assumptions_and_conventions.md
│   ├── 03_claims_register.md
│   ├── 04_risk_register.md
│   ├── 05_decision_log.md
│   ├── 06_task_index.md
│   └── 07_status_dashboard.md
├── iterations/
│   ├── README.md
│   ├── TEMPLATE_iteration_report.md
│   ├── 0001_problem_scoping.md
│   ├── 0002_literature_map.md
│   ├── 0003_core_assumptions.md
│   ├── 0004_derivation_first_pass.md
│   └── 0005_model_review_first_pass.md
├── quality_reports/
│   ├── session_logs/
│   ├── audits/
│   ├── decisions/
│   └── plans/
├── paper/
│   ├── manuscript/
│   │   ├── main.tex
│   │   └── sections/
│   │       ├── 01_introduction.tex
│   │       ├── 02_background.tex
│   │       ├── 03_theory.tex
│   │       ├── 04_results.tex
│   │       ├── 05_discussion.tex
│   │       └── 06_conclusion.tex
│   ├── figures/
│   │   └── README.md
│   └── references/
│       ├── references.bib
│       └── reference_audit.md
├── notes/
│   └── obsidian/
│       ├── Home.md
│       └── MOC_Physics_Article.md
├── reviews/
│   ├── TEMPLATE_review.md
│   ├── reviewer_prompt.md
│   ├── reviewer_prompt_claude.md
│   ├── reviewer_prompt_chatgpt.md
│   ├── reviewer_prompt_deepseek.md
│   └── rebuttal_matrix.md
├── templates/
│   ├── task_report_template.md
│   ├── derivation_report_template.md
│   ├── evidence_card_template.md
│   ├── prompt_handoff_template.md
│   ├── session-log.md
│   └── decision-record.md
└── scripts/
    ├── new_iteration.py
    └── check_project_contract.py
```

## Purpose of key folders

### `.claude/`

Contract and skills for Claude Code (or any AI agent that reads SKILL.md files). This is the operational layer of the project. Here the model learns how to behave, which files it must create, and how to verify results.

The `rules/` subfolder contains persistent behavioral rules that apply to every session:
- `post-flight-verification.md` — anti-hallucination protocol for new formulas, numbers, and citations
- `session-logging.md` — when and how to write session logs
- `stall-prevention.md` — how to recognize and exit cognitive spin

### `project/`

Project state. These files are the analog of `README`, `ROADMAP`, `CHANGELOG`, `ISSUES`, `DECISIONS` in a software project.

### `iterations/`

Work journal. Each iteration creates a new `.md` file. Old iterations are never overwritten, except to correct obvious typos with a changelog entry.

### `quality_reports/`

Audit artifacts separated from the work journal. Contains:
- `session_logs/` — session snapshots for context recovery
- `audits/` — seven-pass reviews and other audit outputs
- `decisions/` — structured decision records (see `templates/decision-record.md`)
- `plans/` — session plans written at post-plan logging time

### `paper/`

The final paper and everything that will appear in the publication. The manuscript may not be changed directly without a reference to the task/iteration from which the result was taken.

### `reviews/`

Independent checks. Model reviews are stored separately from the author's work to avoid mixing generation and audit. Use `reviews/reviewer_prompt.md` with any AI model — the model-specific files are kept for reference only.

### `templates/`

Templates that models must use. If a model does not use the template, the iteration is considered incomplete.

## Traceability principle

Every claim in the paper must have a path:

```text
manuscript claim
  -> claims_register row
  -> derivation/evidence file
  -> source/code/data/log
  -> review/audit status
```

Without this path, a claim is considered unprepared for publication.
