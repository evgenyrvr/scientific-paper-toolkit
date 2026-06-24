# Assumptions and Conventions

## Notation

| ID    | Symbol | Meaning | Units | Source/status |
|-------|--------|---------|-------|---------------|
| N-001 | [sym1] | [description] | [unit] | defined here, draft |
| N-002 | [sym2] | [description] | [unit] | defined here, draft |

Add rows as you define notation. Every symbol that appears in a formula must have a row here before it can be used in the manuscript.

## Assumptions

| ID    | Assumption | Type | Status | Evidence/derivation |
|-------|-----------|------|--------|---------------------|
| A-001 | [assumption] | modeling / physical / mathematical / observational | draft | [source, derivation file, or reasoning] |

Types: `modeling` (simplification of reality), `physical` (about the system), `mathematical` (approximation), `observational` (about data).

## Conventions

| ID    | Convention | Status | Notes |
|-------|-----------|--------|-------|
| C-001 | [convention, e.g., a specific profile definition or normalization] | draft | [what this convention implies, what it is NOT] |

## Forbidden implicit defaults

The model must NOT silently substitute:
- [List dangerous default substitutions specific to your problem, e.g., "point-mass limit for b < R"]
- [Another example]

If any such substitution is tempting, record it as a risk in `project/04_risk_register.md`.

## Physical constants

| Constant | Value | Units | Source |
|----------|-------|-------|--------|
| G | 6.674e-11 | m³ kg⁻¹ s⁻² | CODATA |
| [other constants used] | | | |
