---
name: reviewer-panel
description: Coordinates independent model reviews from Claude, ChatGPT, DeepSeek, and human perspectives. Use to create reviewer prompts, compare reviews, build rebuttal matrix, and decide next revisions.
---

# Reviewer Panel

## Purpose

Use models as structured reviewers without treating them as final authorities.

## Review modes

1. Friendly scientist.
2. Hostile technical reviewer.
3. Mathematical auditor.
4. Editor/journal fit reviewer.
5. Reproducibility reviewer.

## Procedure

1. Select artifact to review.
2. Create three separate prompts using `reviews/reviewer_prompt_*.md`.
3. Store each model review as a separate file.
4. Summarize overlaps and disagreements.
5. Add all actionable issues to `reviews/rebuttal_matrix.md`.
6. Create follow-up tasks in `project/06_task_index.md`.
7. Do not apply fixes in the same iteration unless explicitly requested.

## Output contract

- review prompt package;
- comparison table;
- rebuttal matrix update;
- next task list;
- iteration report.

## Rule

A model review cannot close a scientific issue. Only human approval can close it.
