# CLAUDE.md — Scientific Paper AI Lab Contract

You are assisting with a scientific paper managed as a code-like project. The project is controlled by files, not by chat memory.

## Prime directive

Do small, inspectable, reproducible steps. Every substantive step must produce or update a markdown artifact.

## Required behavior

1. Before working, identify the task ID and relevant skill.
2. Read current project state files:
   - `project/00_master_plan.md`
   - `project/02_assumptions_and_conventions.md`
   - `project/03_claims_register.md`
   - `project/06_task_index.md`
   - `project/07_status_dashboard.md`
3. Create or update an iteration report in `iterations/` for every step.
4. Do not mark a result verified unless a concrete verification table is filled.
5. Do not invent references, coefficients, terminology, or prior work.
6. Do not silently change notation, assumptions, normalizations, parameters, or code behavior.
7. If you find an error, keep looking after fixing the first error. Run the checklist again.
8. If you are unsure, write `BLOCKED` and state exactly what is missing.
9. Never delete old iteration reports.
10. Never directly rewrite the whole manuscript unless the task explicitly says manuscript assembly.

## Public reasoning output

Do not expose private hidden chain-of-thought. Instead, every report must include a `Public reasoning summary` and `Detailed work log` with enough detail for human audit.

## Forbidden shortcuts

Do not use the following as substitutes for calculation or evidence:

- “obviously”
- “clearly”
- “standard result”
- “for consistency”
- “it follows”
- “verified”
- “well-known”

When such a phrase is scientifically appropriate, attach the derivation, source, or verification check.

## Anti-cheating protocol

Do not tune outputs to look right. Record all changes to:

- parameters;
- bins;
- normalization;
- smoothing;
- uncertainty bands;
- excluded data;
- fitting ranges;
- constants;
- labels;
- figure aesthetics that affect interpretation.

## Manuscript rule

Every manuscript claim must trace to:

`manuscript -> claims_register -> evidence/derivation/code -> review status`.

## Human responsibility

The human author is responsible for final scientific integrity. You may assist, review, and suggest; do not claim final authority.
