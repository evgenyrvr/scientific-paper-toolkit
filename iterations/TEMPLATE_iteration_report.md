# Iteration Report: <short title>

## Metadata

| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| Iteration ID | YYYYMMDD_NNN |
| Task ID | T?.? |
| Model | [model name and version] |
| Skill used | skill-name |
| Operator | [Author] / model |
| Status | draft / complete / blocked / rejected |

## Goal

One small goal for this iteration.

## Input files read

- `path/to/file.md` — why it was read.

## Output files changed

- `path/to/file.md` — what changed.

## Public reasoning summary

Brief verifiable explanation of the logic — enough for a human to understand why the next step was taken, without private chain-of-thought. If a formula was derived, state the key steps. If a decision was made, state the reason.

## Detailed work log

1. Step.
2. Step.
3. Step.

## Calculations / derivations / code actions

Use equations, code snippets, commands, or tables as needed.

## Assumptions used

| Assumption ID | Used how | Concern |
|---|---|---|
| A-??? | TODO | TODO |

## Claims affected

| Claim ID | Change | New status |
|---|---|---|
| CL-??? | TODO | PASS / FAIL / EXPLAINED / STALE / UNVERIFIED |

## Verification performed

| Check | Result | Evidence |
|---|---|---|
| Dimensional analysis | pass / fail / not-run | TODO |
| Limit check | pass / fail / not-run | TODO |
| Source check | pass / fail / not-run | TODO |
| Alternative derivation | pass / fail / not-run | TODO |

## Post-flight verification

Run after producing any new formula, number, or citation (see `.claude/rules/post-flight-verification.md`).

| Claim | Verification question | Outcome | Note |
|-------|----------------------|---------|------|
| [claim text] | [specific question] | PASS / FAIL / UNVERIFIED | [note] |

## Failed checks / uncertainties

- TODO.

## Reviewer prompt

Use this in a fresh context with any AI model:

```text
You are an independent technical reviewer. Review the following iteration report for:
1. Hidden or unstated assumptions
2. Algebraic errors, sign errors, missing factors
3. Dimensional inconsistencies
4. Missing limiting case checks
5. Statements declared "verified" without a concrete check
6. Citations attributed incorrectly

Return: severity-tagged issue list (CRITICAL / MAJOR / MINOR). Do not rewrite. Do not accept "standard result" without source.

[paste iteration report here]
```

## Rerun prompt

```text
Re-run iteration YYYYMMDD_NNN from scratch. Read the same input files listed above. Do not use the previous result except as a comparison. Produce a new report and list differences.
```

## Next action

- TODO.
