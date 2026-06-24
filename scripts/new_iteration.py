from pathlib import Path
from datetime import datetime
import re

ROOT = Path(__file__).resolve().parents[1]
ITER = ROOT / "iterations"
TEMPLATE = ITER / "TEMPLATE_iteration_report.md"

slug = input("Short title: ").strip().lower()
slug = re.sub(r"[^a-z0-9а-яё]+", "-", slug).strip("-") or "untitled"
existing = sorted(ITER.glob(f"{datetime.now():%Y%m%d}_*.md"))
number = len(existing) + 1
path = ITER / f"{datetime.now():%Y%m%d}_{number:03d}_{slug}.md"
content = TEMPLATE.read_text(encoding="utf-8")
content = content.replace("<short title>", slug.replace("-", " "))
content = content.replace("YYYY-MM-DD", f"{datetime.now():%Y-%m-%d}")
content = content.replace("YYYYMMDD_NNN", f"{datetime.now():%Y%m%d}_{number:03d}")
path.write_text(content, encoding="utf-8")
print(path)
