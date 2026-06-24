# Post-Flight Verification Rule

Every iteration that produces a new formula, numerical result, or citation must run a self-verification pass before marking the iteration complete.

## The protocol

After producing a result:

1. **Extract claims** — list every verifiable assertion: equations, numbers, citations, existence claims.
2. **Generate verification questions** — one specific, source-answerable question per claim.
3. **Verify in isolation** — re-examine each claim independently, without reference to how you derived it. Treat your own prior output as a draft to be challenged.
4. **Report outcome** — structured block with: claim count, PASS/FAIL/UNVERIFIED per claim, any discrepancies.

## Outcome labels

- **PASS** — independently confirmed
- **FAIL** — found error or contradiction
- **EXPLAINED** — numeric mismatch within expected tolerance, reason documented
- **UNVERIFIED** — source not accessible; flagged for human check
- **STALE** — claim was PASS in a prior iteration but a dependency changed

## Fail-closed rule

If any claim is FAIL, the iteration report status must be `blocked` — not `complete`. Fix the FAIL before marking done.

## When to skip

Mechanical steps (copying a file, running a known-good script, formatting) do not require post-flight verification. Skip only when no new claim is produced.
