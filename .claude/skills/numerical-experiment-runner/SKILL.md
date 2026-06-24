---
name: numerical-experiment-runner
description: Designs, implements, logs, and audits reproducible numerical experiments or simulations for a scientific paper. Use for Python/Mathematica/Julia/R/Fortran code, parameter scans, fits, Monte Carlo checks, run logs, and reproducibility testing.
---

# Numerical Experiment Runner

## Purpose

Make computational results reproducible and auditable.

## Required files

- `project/02_assumptions_and_conventions.md`
- `project/03_claims_register.md`
- relevant derivation reports
- code/data directories named by user

## Procedure

1. Write the computational question.
2. Define inputs, parameters, units, random seeds, versions, and expected outputs.
3. Implement the smallest baseline calculation first.
4. Save code, run logs, and output data.
5. Compare against analytic limits or known references.
6. Record all failures.
7. Never tune parameters to match expectations without recording the reason.
8. Update claims register only after checks.

## Required run log

Every run must record:

- command;
- date/time;
- environment;
- code version or file hash if available;
- input parameters;
- output files;
- errors/warnings;
- interpretation.

## Anti-cheating rules

Do not:

- drop outliers silently;
- change binning to improve appearance;
- smooth data without method;
- remove uncertainty components;
- normalize curves after seeing target result unless normalization is part of the derivation.
