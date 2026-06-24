---
name: physics-derivation-auditor
description: Produces and audits detailed physics derivations from explicit assumptions. Use for deriving equations, factorization formulas, conservation laws, approximations, perturbative expansions, or theoretical results that must be shown step by step.
---

# Physics Derivation Auditor

## Purpose

Create derivations that can be checked line by line.

## Required inputs

- `project/02_assumptions_and_conventions.md`
- `project/03_claims_register.md`
- relevant prior iteration reports
- `templates/derivation_report_template.md`

## Procedure

1. State the target result exactly.
2. List all assumptions and notation IDs used.
3. Derive from first principles or explicitly cited prior results.
4. Write every algebraic step needed for audit.
5. Mark any skipped or uncertain step as `BLOCKED`.
6. Run basic checks:
   - dimensions;
   - signs/factors;
   - limiting cases;
   - symmetries;
   - consistency with definitions.
7. Add or update claims in `project/03_claims_register.md`.
8. Create a new iteration report.

## Required language discipline

Do not write “clearly”, “obviously”, “standard”, “for consistency”, or “verified” without a concrete supporting line.

## Output contract

- derivation report;
- assumptions table;
- check table;
- affected claims;
- reviewer prompt for independent audit;
- rerun prompt.

## Failure mode

If the derivation depends on an unproven lemma, create a new task for that lemma rather than hiding it.
