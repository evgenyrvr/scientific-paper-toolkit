# Prompt Handoff Template

Use this when switching model, restarting context, or asking another model to verify work.

```text
You are working inside a scientific paper project structured like a software repository.

Read these files first:
1. project/00_master_plan.md
2. project/02_assumptions_and_conventions.md
3. project/03_claims_register.md
4. project/06_task_index.md
5. iterations/<last_iteration>.md
6. <specific file to review>

Task:
<one small task>

Rules:
- Do not rewrite unrelated files.
- Do not invent references.
- Do not mark anything verified without a concrete check.
- Create a new iteration report in iterations/YYYYMMDD_NNN_short-title.md.
- Include a rerun prompt and reviewer prompt.
- If blocked, write BLOCKED and explain exactly what is missing.
```
