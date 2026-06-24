---
name: scientific-project-orchestrator
description: Orchestrates a scientific paper project managed like a software repository. Use for planning stages, creating task trees, updating dashboards, generating iteration files, maintaining claims/risks/decisions, and coordinating AI models and human review.
---

# Scientific Project Orchestrator

## Purpose

Keep the research project coherent across many small iterations.

## Required inputs

Read before acting:

1. `project/00_master_plan.md`
2. `project/06_task_index.md`
3. `project/07_status_dashboard.md`
4. Latest file in `iterations/`
5. Any task-specific file named by the user

## Workflow

1. Identify current stage and task.
2. Check whether the task is small enough for one iteration.
3. If too large, split into sub-tasks and update `project/06_task_index.md`.
4. Create a new iteration report from `iterations/TEMPLATE_iteration_report.md`.
5. Perform only the requested planning/coordination step.
6. Update:
   - `project/07_status_dashboard.md`
   - `project/05_decision_log.md` if a project decision was made
   - `project/04_risk_register.md` if a new risk appears
7. End with a rerun prompt and next recommended action.

## Output contract

Every run must produce:

- one new iteration `.md` file;
- dashboard update;
- list of files read;
- list of files changed;
- public reasoning summary;
- next task.

## Do not

- Do not solve physics derivations unless the specific derivation skill is invoked.
- Do not edit manuscript text except to insert TODO markers requested by the task.
- Do not close tasks without verification evidence.
