---
name: figure-quality-control
description: Audits and improves scientific figures for readability, provenance, correctness, and manuscript alignment. Use for plots, captions, labels, uncertainty bands, visual comparison, and figure reproducibility.
---

# Figure Quality Control

## Purpose

Ensure figures are correct, readable, and traceable.

## Required inputs

- figure file;
- figure source code;
- data file;
- run log;
- manuscript claim using the figure.

## Checklist

1. Does the figure support the manuscript claim?
2. Are axes labelled with units?
3. Are fonts readable at publication size?
4. Are legends unambiguous?
5. Is uncertainty shown honestly?
6. Is smoothing/binning documented?
7. Can the figure be regenerated from code/data?
8. Does caption say what is plotted, not just repeat the title?

## Output

Create `qc.md` near the figure or an iteration report containing:

- figure provenance;
- visual issues;
- scientific issues;
- changes made;
- checks passed/failed;
- rerun command.
