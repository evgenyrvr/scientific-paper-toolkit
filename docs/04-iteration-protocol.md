# Iteration Protocol

## Goal

Every iteration must be reproducible. One week later you must be able to understand what was done, why, where the model was uncertain, and how to repeat the request.

## File naming format

```text
iterations/YYYYMMDD_NNN_short-title.md
```

Example:

```text
iterations/20260614_017_check_energy_conservation.md
```

## Required sections of every iteration

1. `Metadata` — date, model, skill, task id.
2. `Goal` — one small goal.
3. `Input files read` — what the model read.
4. `Output files changed` — what the model changed.
5. `Public reasoning summary` — brief verifiable reasoning without private chain-of-thought.
6. `Detailed work log` — actions, calculations, formulas, commands.
7. `Assumptions used` — assumptions with IDs.
8. `Claims affected` — claims with IDs.
9. `Verification performed` — list of checks.
10. `Post-flight verification` — per-claim PASS/FAIL/UNVERIFIED table (see `.claude/rules/post-flight-verification.md`).
11. `Failed checks / uncertainties` — what did not pass.
12. `Reviewer prompt` — prompt for independent review by any model in a fresh context.
13. `Rerun prompt` — prompt for repeating the iteration.
14. `Next action` — next minimal step.

## Definition of Done

An iteration is considered complete only if:

- a `.md` report is created;
- all required sections are filled;
- which files were changed is stated;
- the status dashboard is updated;
- all new claims are added to the claims register;
- all new assumptions are added to the assumptions file;
- unverified items have `BLOCKED` or `TODO` entries.

## What to do on model failure

If the model has lost context, use `templates/prompt_handoff_template.md`. Do not ask it to continue "from where it left off." Give it a specific set of files to read and a task id.

## Stall rule

If the model attempts the same step more than twice without progress, it must stop and write `STALL DETECTED` in the report. See `.claude/rules/stall-prevention.md`.
