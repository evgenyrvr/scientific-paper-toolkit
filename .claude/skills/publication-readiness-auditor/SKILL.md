---
name: publication-readiness-auditor
description: Performs final pre-submission audit for a scientific paper, including claims, references, derivations, figures, reproducibility, AI-use disclosure, journal/preprint server requirements, and unresolved risks.
---

# Publication Readiness Auditor

## Purpose

Prevent premature submission.

## Required files

- manuscript;
- claims register;
- reference audit;
- risk register;
- decision log;
- reviews/rebuttal matrix;
- figure QC files;
- run logs.

## Checklist

1. Every manuscript claim maps to a verified claim ID.
2. Every citation is audited.
3. Every formula is derived or sourced.
4. Every figure has provenance and QC.
5. Every numerical result has reproducible code/run log.
6. All major reviewer issues are closed or explicitly rejected with reasons.
7. AI tool use is disclosed according to target venue expectations.
8. AI systems are not listed as authors unless the target venue explicitly permits it.
9. No AI meta-comments remain.
10. Human author has performed final read-through.

## Output

Create `reviews/publication_readiness_audit_YYYYMMDD.md` with:

- pass/fail table;
- blocking issues;
- non-blocking issues;
- submission readiness judgment;
- required human actions.

## Judgment labels

- `not-ready`
- `ready-after-minor-fixes`
- `ready-for-human-final-audit`
- `ready-to-submit`
