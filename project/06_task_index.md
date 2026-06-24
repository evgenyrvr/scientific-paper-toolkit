# Task Index

## Stage 0 — Setup

| Task ID | Task | Skill | Output | Status |
|---------|------|-------|--------|--------|
| T0.1 | Initialize project | scientific-project-orchestrator | folder tree, dashboard | todo |
| T0.2 | Fill research question | research-question-scope | project/01_research_question.md | todo |
| T0.3 | Define conventions and notation | research-question-scope | project/02_assumptions_and_conventions.md | todo |

## Stage 1 — Literature Review

| Task ID | Task | Skill | Output | Status |
|---------|------|-------|--------|--------|
| T1.1 | Compile key observational constraints table | literature-review-ledger | literature/observations_table.md | todo |
| T1.2 | Compile competing models/candidates table | literature-review-ledger | literature/models_table.md | todo |
| T1.3 | Audit core papers with evidence cards | literature-review-ledger | literature/evidence_cards/ | todo |
| T1.4 | Build BibTeX and reference audit | literature-review-ledger | paper/references/references.bib | todo |

## Stage 2 — Theory Core

| Task ID | Task | Skill | Output | Status |
|---------|------|-------|--------|--------|
| T2.1 | Derive the central formula/result | physics-derivation-auditor | iterations/YYYYMMDD_NNN_derivation.md | todo |
| T2.2 | Derive auxiliary quantities (potentials, profiles, integrals) | physics-derivation-auditor | iterations/YYYYMMDD_NNN_auxiliary.md | todo |
| T2.3 | Check units and dimensional analysis | mathematical-consistency-checker | iterations/YYYYMMDD_NNN_units_check.md | todo |
| T2.4 | Check limiting cases and symmetries | mathematical-consistency-checker | iterations/YYYYMMDD_NNN_limits_check.md | todo |

## Stage 3 — Verification

| Task ID | Task | Skill | Output | Status |
|---------|------|-------|--------|--------|
| T3.1 | Independent verification of main formula | mathematical-consistency-checker | iterations/YYYYMMDD_NNN_verification.md | todo |
| T3.2 | Numerical spot checks against analytic limits | numerical-experiment-runner | code/verify_formula.py + iterations/ | todo |

## Stage 4 — Numerics/Experiments

| Task ID | Task | Skill | Output | Status |
|---------|------|-------|--------|--------|
| T4.1 | Implement main computation | numerical-experiment-runner | code/main_calc.py | todo |
| T4.2 | Parameter scan / constraint grid | numerical-experiment-runner | code/param_scan.py + figures/ | todo |
| T4.3 | Generate paper figures | figure-quality-control | figures/ + figure QC reports | todo |

## Stage 5 — Manuscript Assembly

| Task ID | Task | Skill | Output | Status |
|---------|------|-------|--------|--------|
| T5.1 | Write Introduction | manuscript-builder | paper/manuscript/sections/01_introduction.tex | todo |
| T5.2 | Write Theory section | manuscript-builder | paper/manuscript/sections/03_theory.tex | todo |
| T5.3 | Write Results section | manuscript-builder | paper/manuscript/sections/04_results.tex | todo |
| T5.4 | Write Discussion section | manuscript-builder | paper/manuscript/sections/05_discussion.tex | todo |
| T5.5 | Write Conclusion and Abstract | manuscript-builder | paper/manuscript/sections/06_conclusion.tex + main.tex abstract | todo |
| T5.6 | Cross-reference and consistency review | publication-readiness-auditor | iterations/YYYYMMDD_NNN_consistency_review.md | todo |

## Stage 6 — Model Review Panel

| Task ID | Task | Skill | Output | Status |
|---------|------|-------|--------|--------|
| T6.1 | Claude structural review | reviewer-panel | reviews/review_claude_YYYYMMDD.md | todo |
| T6.2 | ChatGPT methodology review | reviewer-panel | reviews/review_chatgpt_YYYYMMDD.md | todo |
| T6.3 | DeepSeek technical audit | reviewer-panel | reviews/review_deepseek_YYYYMMDD.md | todo |
| T6.4 | Build rebuttal matrix | reviewer-panel | reviews/rebuttal_matrix.md | todo |

## Stage 7 — Human Final Audit

| Task ID | Task | Skill | Output | Status |
|---------|------|-------|--------|--------|
| T7.1 | Publication readiness audit | publication-readiness-auditor | reviews/publication_readiness_audit_YYYYMMDD.md | todo |
| T7.2 | arXiv/journal submission package | publication-readiness-auditor | arxiv_submission/ | todo |
