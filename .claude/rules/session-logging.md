# Session Logging Rule

Session logs prevent knowledge loss when context compacts or a new session starts cold.

## Three triggers

**1. Post-plan logging** — immediately after agreeing on what to do this session:
- Goal of the session
- Strategy and approach
- Files to read/change
- Definition of done

**2. Incremental logging** — add a 1-2 line entry whenever:
- A design decision is made
- A calculation produces an unexpected result
- A claim status changes
- An error is found and fixed
- The approach changes

**3. End-of-session logging** — before closing:
- Summary of what was accomplished
- Open questions and BLOCKED items
- Next recommended task
- Any MEMORY.md entries that should be added

## Storage

Session logs go in `quality_reports/session_logs/YYYYMMDD_NNN_short-title.md` using `templates/session-log.md`.

## Rule

Update `project/07_status_dashboard.md` at end-of-session. The dashboard is the recovery point for the next session.
