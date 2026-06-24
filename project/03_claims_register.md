# Claims Register

Every claim that may appear in the paper must be registered here before being written into the manuscript.

## Rules

- Each claim must have a unique ID (CL-NNN).
- Status is tracked in two columns: `verification status` and `passport status`.
- No claim may be added to the manuscript with `passport status: FAIL` or `STALE`.
- `EXPLAINED` means a known discrepancy is documented — it can proceed if the explanation is recorded.

## Status definitions

**Verification status** (process tracking):
- `draft` — written but not yet checked
- `needs-verification` — identified as needing a check, assigned to a task
- `verified-by-model` — model checked it; human confirmation pending
- `verified` — human-confirmed with evidence recorded
- `retracted` — found to be incorrect

**Passport status** (claim health, updated by post-flight checks):
- `PASS` — independently confirmed
- `FAIL` — found error or contradiction; iteration must be BLOCKED
- `EXPLAINED` — numeric mismatch within tolerance; reason documented
- `STALE` — was PASS, but a dependency changed; must re-verify
- `UNVERIFIED` — source not accessible; flagged for human check

## Claims

| Claim ID | Claim | Type | Evidence file | Verification status | Passport status | Manuscript location |
|----------|-------|------|---------------|---------------------|-----------------|---------------------|
| CL-001 | [First claim] | theory / result / literature / conceptual | iterations/YYYYMMDD_NNN_first_derivation.md | draft | UNVERIFIED | Section 2 |

## Claim types

- `theory`: a derived mathematical result
- `result`: output of a computation or numerical experiment
- `literature`: a claim imported from a cited source
- `conceptual`: a framing or novelty claim
