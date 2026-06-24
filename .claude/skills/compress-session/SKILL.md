---
name: compress-session
description: Distills the current session into a structured snapshot before context compression occurs. Use proactively when the conversation is long, or reactively after a compaction event. Produces a session log and updates the status dashboard.
---

# Compress Session

## Purpose

Preserve session state so the next session can start with full context from files, not from conversation memory.

## When to use

- Proactively: after 60+ minutes of work, before a long expected gap
- Reactively: at the start of a session when context was compacted
- Always: before ending any productive session

## Procedure

1. Read `project/07_status_dashboard.md` and the last iteration report.
2. Write `quality_reports/session_logs/YYYYMMDD_NNN_session.md` using `templates/session-log.md`.
3. Update `project/07_status_dashboard.md`:
   - Current stage and task
   - Last completed iteration (file path)
   - Any new BLOCKED issues
   - Next recommended action
4. Identify any MEMORY.md entries worth adding. Write them as `[LEARN:category] one sentence.`
5. Report: "Session snapshot complete. Next session should start by reading status_dashboard + [last iteration file]."

## Output contract

- `quality_reports/session_logs/YYYYMMDD_NNN_session.md`
- Updated `project/07_status_dashboard.md`
- Optional MEMORY.md additions
- Recovery prompt for next session
