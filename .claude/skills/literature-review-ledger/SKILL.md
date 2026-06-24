---
name: literature-review-ledger
description: Builds a verified literature map, evidence cards, BibTeX entries, and claim-source ledger for any scientific paper. Use for literature review, citation checks, novelty audit, and preventing hallucinated references.
---

# Literature Review Ledger

## Purpose

Create a literature review that is traceable, not hallucinated.

## Required files

- `paper/references/references.bib`
- `paper/references/reference_audit.md`
- `project/03_claims_register.md`
- `templates/evidence_card_template.md`

## Workflow

1. Define search terms and inclusion/exclusion criteria.
2. For each source, create or update an evidence card.
3. Check bibliographic data before writing BibTeX.
4. Map each cited source to specific claims.
5. Identify conflicts, gaps, and limitations.
6. Update `reference_audit.md`.
7. Add unresolved source issues to `risk_register.md`.

## Evidence rules

A paper can support only claims actually present in that paper. Do not infer stronger support than the source gives.

## Bibliography rules

Never invent:

- title;
- author order;
- journal;
- DOI;
- arXiv ID;
- year;
- equation number.

If metadata is uncertain, write `needs-manual-check`.

## Output contract

Every run must output:

- literature search strategy;
- list of sources considered;
- included/excluded table;
- updated reference audit;
- claim-source mapping;
- iteration report.
