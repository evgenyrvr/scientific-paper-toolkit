---
name: manuscript-builder
description: Assembles scientific paper sections from verified project artifacts into LaTeX or Markdown manuscript text. Use for drafting introduction, theory, results, discussion, abstract, conclusion, and integrating claims with citations.
---

# Manuscript Builder

## Purpose

Synthesize verified artifacts into paper prose without losing traceability.

## Required inputs

- `project/03_claims_register.md`
- relevant derivation reports;
- literature evidence cards;
- figure QC files;
- `paper/references/reference_audit.md`

## Procedure

1. Identify target manuscript section.
2. List claims allowed in that section.
3. Use only claims with adequate evidence or mark as TODO.
4. Insert citations only from audited references.
5. Avoid overclaiming.
6. After drafting, create a traceability table:
   - paragraph;
   - claim ID;
   - evidence file;
   - citation key.
7. Create iteration report.

## Forbidden

- Do not invent citations.
- Do not add results not in claims register.
- Do not hide uncertainty.
- Do not write a polished final abstract before the results are verified.

## Output contract

- updated section file;
- traceability table;
- TODO list;
- reviewer prompt for section review.
