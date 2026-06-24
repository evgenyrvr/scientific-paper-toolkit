# Vibe Research Method — Adapted for a Scientific Paper Project

## What is taken from the approach

In the experiment described by Anthropic/Schwartz, what proved decisive was not that the model received one large prompt, but that the work was broken down into a tree of tasks and files. The model maintained separate markdown files for tasks and summary files for stages, read previous summaries before each new task, and the plan was edited as the project progressed. This transforms research from an endless chat into a file system with memory.

## Core principles

### 1. Research work as a repository

Every significant object must be a file:

- problem statement;
- list of notation;
- assumptions;
- task report;
- derivation report;
- verification report;
- review report;
- manuscript section;
- figure provenance;
- code/run log.

If something cannot be found in a file, it is considered unrecorded.

### 2. Small tasks instead of one large request

Bad prompt:

> Write the final paper on my physical theory.

Good prompt:

> Execute task `T2.3`: verify the derivation of formula X from assumptions A1–A4. Create `iterations/20260614_023_derivation_x.md`. Do not change the manuscript. If a step is not proven, write `BLOCKED` and list the missing preconditions.

### 3. Markdown files as inspectable memory

The model must leave a trail showing:

- what it read;
- what it changed;
- what it derived;
- what it verified;
- what remains unverified;
- which prompt to use to repeat the iteration;
- which hypotheses/claims have now changed.

### 4. Cross-model review

Models are interchangeable for all roles. Any AI model can act as executor, reviewer, or technical auditor. What matters is the role (executor vs. reviewer), not which specific model fills it.

The key rule: use a **fresh context** for review. A reviewer model should not see the conversation history of the model that produced the artifact — this prevents self-confirmation bias.

Agreement among models is a signal for the human, not a proof. Disagreement among models is a reason to open a separate verification task.

### 5. Explicit honesty requirements

Forbidden phrases without a calculation:

- "obviously";
- "clearly";
- "it follows";
- "for consistency";
- "standard result";
- "verified".

If a standard result is used, a source or file where it is proven/accepted must be cited.

### 6. Anti-cheating protocol

The model must not:

- tune parameters to make a plot look better;
- smooth a curve without recording the method;
- change normalization without recording the reason;
- remove inconvenient uncertainty variations;
- declare a check complete without a concrete checklist;
- invent references, coefficients, or terms.

Any change to a formula, code, figure, constant, normalization, or text must be recorded in the corresponding report.

## How a stage cycle looks

1. `Stage 0 — Project Setup`: structure, rules, themes, tools.
2. `Stage 1 — Problem Scoping`: physical problem statement, novelty, boundaries.
3. `Stage 2 — Literature Map`: literature map, sources, BibTeX.
4. `Stage 3 — Theory Core`: definitions, assumptions, derivations.
5. `Stage 4 — Verification`: dimensions, limits, special cases, independent derivations.
6. `Stage 5 — Numerics/Experiments`: code, parameters, reproducibility.
7. `Stage 6 — Figures and Tables`: plots, captions, provenance.
8. `Stage 7 — Manuscript Assembly`: draft, sections, references.
9. `Stage 8 — Review Panel`: independent review by a model (or multiple models) in fresh context.
10. `Stage 9 — Human Audit and Submission`: final responsibility of the author.
