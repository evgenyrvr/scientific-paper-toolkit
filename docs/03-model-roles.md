# AI Model Roles

## The key principle: models are interchangeable for all tasks

Any AI model — Claude, ChatGPT, DeepSeek, Gemini, Mistral, or others — can perform any role in this project. Do not hard-wire a specific model to a specific task.

The roles below describe **what kind of work is needed**, not which model to use.

---

## Role 1: Executor / File agent

The model that actively reads and writes project files, runs code, creates iteration reports, builds LaTeX drafts.

**Typical tasks:**
- Read project state files and identify the current task
- Create a new iteration report
- Write or edit manuscript sections
- Run Python scripts, interpret output
- Update claims register and dashboard

**Any model** can do this. Claude Code has file-access tools built in; other models need files pasted into context.

---

## Role 2: Reviewer / Auditor

An independent model that reviews an artifact without knowledge of how it was created.

**Critical rule:** Use a **fresh context** for review. Paste the artifact and the reviewer prompt (see `reviews/reviewer_prompt.md`). Do not carry the conversation history into the review.

**Typical tasks:**
- Hostile technical review (algebra, dimensions, limits)
- Structural review (argument, story, literature)
- Post-flight verification (claims, citations)
- Seven-pass review (use `.claude/skills/seven-pass-review/SKILL.md`)

**Any model** can do this. The "fresh context" requirement is more important than which model you use.

---

## Role 3: Human Author (not interchangeable)

Only the human author can:
- Decide what is physically meaningful and novel
- Accept or reject any claim for the manuscript
- Choose the journal and sign the submission
- Take scientific responsibility
- Disclose AI use in acknowledgements

No model should be listed as an author. No model's judgment replaces the author's.

---

## Practical workflow (single-model version)

If you are working with one model only:
1. Give the model the executor role for the current task.
2. After the task, start a fresh context and give it the reviewer role for what was just produced.
3. Act on the review findings as the human author.

## Practical workflow (multi-model version)

If you have access to multiple models:
1. Any model executes the task.
2. A different model reviews it in fresh context.
3. Human decides on findings.

The combination is up to you. There is no "right" model for a given role.

---

## What no model should do without explicit instruction

- Declare the paper ready for submission.
- Send the manuscript anywhere.
- Delete old iterations.
- Tune plots without recording the change.
- Change physical assumptions without a decision log entry.
- Accept "standard result" without a source or derivation.
