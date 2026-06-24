---
name: seven-pass-review
description: Performs a comprehensive seven-lens review of a physics manuscript section or full draft. Each lens examines a distinct dimension. Use at submission-ready or major-revision stage. Any AI model can run this.
---

# Seven-Pass Review

## Purpose

Systematic manuscript review that forces examination across seven independent dimensions, preventing the common failure mode of reviewing only what you wrote.

## The seven lenses

| Pass | Lens | What to check |
|------|------|---------------|
| 1 | Abstract audit | Does the abstract state the physical question, method, key numerical result, and one implication? Does it match the paper body? |
| 2 | Introduction structure | Is the gap clearly identified? Is each cited result actually in that paper? Is the contribution precisely stated? |
| 3 | Derivations | Is every formula derived or explicitly sourced? Are all assumptions stated before use? Are dimensions correct? |
| 4 | Results + tables | Are all numbers in tables and text consistent? Are units shown? Are uncertainties stated? Can the tables stand alone? |
| 5 | Limits and robustness | Are limiting cases checked? Does the result behave correctly as parameters go to zero or infinity? Are known special cases recovered? |
| 6 | Prose quality | Are sentences clear without jargon inflation? Is hedging proportional to evidence? Are forbidden phrases used ("obviously", "clearly", "it follows")? |
| 7 | Citation audit | Does each cited paper actually support the specific claim it is cited for? Are DOI/arXiv IDs consistent with title and authors? |

## Workflow

1. Read the manuscript section or full draft.
2. Run passes 1–7 sequentially. For each pass, produce a finding list with severity labels: CRITICAL / MAJOR / MINOR.
3. Synthesize: produce a prioritized revision plan with the top 3–5 blocking issues.
4. Write output to `quality_reports/audits/YYYYMMDD_seven-pass-review.md`.
5. Add CRITICAL and MAJOR findings to `reviews/rebuttal_matrix.md`.

## Severity definitions

- **CRITICAL**: invalidates a key result, must fix before submission
- **MAJOR**: weakens a claim or argument, should fix
- **MINOR**: style, clarity, or completeness issue

## Output contract

- Seven-pass audit file in `quality_reports/audits/`
- Prioritized revision plan
- Updated `reviews/rebuttal_matrix.md`
- Iteration report with post-flight verification status
