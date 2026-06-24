from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    "project/00_master_plan.md",
    "project/01_research_question.md",
    "project/02_assumptions_and_conventions.md",
    "project/03_claims_register.md",
    "project/04_risk_register.md",
    "project/05_decision_log.md",
    "project/06_task_index.md",
    "project/07_status_dashboard.md",
    "iterations/TEMPLATE_iteration_report.md",
    ".claude/CLAUDE.md",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("Missing required files:")
    for p in missing:
        print("-", p)
    raise SystemExit(1)
print("Project contract check passed.")
