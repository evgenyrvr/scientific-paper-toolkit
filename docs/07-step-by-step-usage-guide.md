# Step-by-step guide: how to use the project structure

This file describes a practical workflow for Visual Studio Code, Obsidian, and one or more AI models. It works on **Linux**, **macOS**, and **Windows 11** (native or WSL 2) — there are no platform restrictions. The goal is to write a scientific paper not as one long document, but as a managed research repository: with tasks, versions, reviews, verifications, and reproducible artifacts.

---

## 0. The core idea of the workflow

You do not ask the model: "write the paper."

You ask the model to execute a small task inside the project, create a verifiable markdown report, update the project registers, and stop.

One cycle looks like this:

```text
Task -> model reads needed files -> small result -> iteration report -> review -> fix -> git commit
```

The minimum unit of work is not a paper chapter, but an iteration in the `iterations/` folder.

Every iteration must leave a trail:

- what the model read;
- what it changed;
- which assumptions it used;
- which claims it touched;
- which checks it performed;
- which uncertainties remain;
- which prompt can reproduce the work.

---

## 1. Recommended tools

### Required

1. **Linux, macOS, or Windows 11 + WSL 2** — all platforms are supported equally.
2. **Visual Studio Code** — main working tool for the project.
3. **Obsidian** — navigation, concept map, reading, manual notes.
4. **Git** — version control for every step.
5. **Python 3.11+** — scripts, calculations, checks.
6. **TeX Live** (Linux/macOS/WSL) or **MiKTeX** (Windows native) — LaTeX manuscript build.
7. **Zotero or JabRef** — bibliography and BibTeX.

### AI models and agents

Any AI model with file access can act as the executor agent. For review tasks, any model in a fresh context works. There is no required mapping of models to roles.

1. **Claude Code in VS Code** — best option for working with `.claude/skills/` and project files directly.
2. **Any other AI model** (ChatGPT, DeepSeek, Gemini, etc.) — can execute any role; paste files into context manually.
3. **GitHub Copilot / Continue / Cline** — additional options for connecting models to VS Code.

---

## 2. Initial setup

See `docs/02-tools-and-setup.md` for platform-specific installation instructions (Linux, macOS, Windows + WSL, Windows native).

### Step 2.1. Create a working folder

**Linux / macOS / WSL:**
```bash
mkdir ~/Research
cd ~/Research
```

**Windows native:**
```powershell
mkdir C:\Research
cd C:\Research
```

Extract or clone the toolkit into a permanent folder. Avoid `Downloads`.

### Step 2.2. Install base programs

- Visual Studio Code
- Git
- Python 3.11+
- Obsidian
- TeX Live (Linux/macOS/WSL) or MiKTeX (Windows)
- Zotero or JabRef

After installation, verify:

```bash
git --version
python3 --version   # or: python --version on Windows
code --version
```

### Step 2.3. Open the project in VS Code

```bash
cd ~/Research/physics-paper-ai-lab   # Linux/macOS/WSL
code .
```

### Step 2.4. Initialize Git

```bash
git init
git add .
git commit -m "init physics paper AI lab scaffold"
```

Now any model step can be rolled back.

---

## 3. Working in Visual Studio Code

VS Code is the primary environment for active work: editing files, running scripts, Git, LaTeX, Python, agents, reviewing changes.

### Step 3.1. Install VS Code extensions

Recommended extensions:

- Markdown All in One;
- Markdown Preview Enhanced or the standard Markdown Preview;
- LaTeX Workshop;
- Python;
- GitLens;
- Todo Tree;
- YAML;
- Claude Code (if using Claude);
- Continue or Cline (for multi-provider setups).

### Step 3.2. Check the project structure

In the VS Code terminal:

```powershell
python scripts/check_project_contract.py
```

Expected result:

```text
Project contract check passed.
```

If the script shows missing files, restore the project structure before continuing to write the paper.

### Step 3.3. Open key files

Open and read in this order:

```text
README.md
docs/00-vibe-physics-method.md
docs/01-project-architecture.md
docs/04-iteration-protocol.md
.claude/CLAUDE.md
project/00_master_plan.md
project/06_task_index.md
project/07_status_dashboard.md
```

### Step 3.4. Create a new iteration manually

Copy the template:

```text
iterations/TEMPLATE_iteration_report.md
```

and rename it, for example:

```text
iterations/20260614_001_define_problem_statement.md
```

### Step 3.5. Create a new iteration with the script

In the terminal:

```powershell
python scripts/new_iteration.py
```

The script asks for a short name:

```text
Short title: define problem statement
```

It creates a file like:

```text
iterations/YYYYMMDD_NNN_define-problem-statement.md
```

### Step 3.6. Give the model the first task

Use a short but precise prompt:

```text
You are working inside this scientific paper repository.

First read:
- .claude/CLAUDE.md
- docs/04-iteration-protocol.md
- project/00_master_plan.md
- project/01_research_question.md
- project/06_task_index.md
- iterations/TEMPLATE_iteration_report.md

Use skill scientific-project-orchestrator.

Task: execute only task T001 — clarify the physical problem statement.

Requirements:
1. Do not write the whole paper.
2. Do not change assumptions without a record in project/05_decision_log.md.
3. Create a new file iterations/YYYYMMDD_001_problem_scoping.md.
4. Update project/01_research_question.md.
5. If claims appear, add them to project/03_claims_register.md.
6. At the end, show the list of changed files and open questions.
```

### Step 3.7. After the model responds, check the diff

In VS Code open Source Control.

Check:

- which files were changed;
- no accidental deletions;
- the model did not rewrite too much;
- it created an iteration report;
- it updated claims/assumptions/decision log.

Commands:

```powershell
git status
git diff
```

If the result is bad:

```powershell
git restore .
```

If the result is good:

```powershell
git add .
git commit -m "T001 problem scoping iteration"
```

---

## 4. How to connect a model directly in VS Code

A model can be connected directly through VS Code. For this project structure this is more convenient than copying text into a browser, because the agent can see files, create `.md` reports, edit LaTeX, run Python, and show diffs.

### Option A — Claude Code in VS Code (recommended)

This is the best option for this project because the structure already contains:

```text
.claude/CLAUDE.md
.claude/skills/*/SKILL.md
```

How to connect:

1. Open VS Code.
2. Press `Ctrl+Shift+X`.
3. Find the **Claude Code** extension.
4. Install it.
5. Restart VS Code.
6. Open the project folder:

```powershell
cd C:\Research\physics-paper-ai-lab
code .
```

7. Open any file, for example `README.md`.
8. Click the Claude Code icon in the VS Code interface.
9. Sign in to your Claude account.
10. Start with the prompt from section 3.6.

You can also install Claude Code CLI:

```powershell
irm https://claude.ai/install.ps1 | iex
```

or via WinGet:

```powershell
winget install Anthropic.ClaudeCode
```

After that you can launch Claude directly in the project terminal:

```powershell
cd C:\Research\physics-paper-ai-lab
claude
```

### Option B — Any model via Continue

Continue is convenient for connecting different providers: Anthropic, OpenAI, DeepSeek, local models via Ollama, and others.

Useful for:

- quick chat/edit in VS Code;
- working with multiple models;
- local models.

Since Continue does not automatically understand Claude `SKILL.md` files the way Claude Code does, explicitly tell it in the prompt:

```text
Read .claude/CLAUDE.md and the relevant .claude/skills/.../SKILL.md as your working instructions.
```

### Option C — Cline

Cline is useful as an agent that can read files, change them, run commands, and show diffs. It supports many API providers and OpenAI-compatible endpoints.

Useful for:

- DeepSeek via OpenAI-compatible API;
- Anthropic;
- OpenAI;
- OpenRouter;
- local models.

Safety rule: do not enable full-auto mode for a scientific project. Every change must go through a diff review.

### Option D — GitHub Copilot

GitHub Copilot is well integrated into VS Code and useful for:

- inline suggestions;
- code explanation;
- quick edits;
- agent mode;
- project search.

For this project it is less precise as a SKILL.md executor if project instructions are not configured. Use it as a supplementary assistant, not as the sole orchestrator.

---

## 5. Working in Obsidian

Obsidian is not a replacement for VS Code. It is a tool for thinking, navigation, and checking connections between ideas.

### Step 5.1. Open the project as a vault

In Obsidian:

```text
Open folder as vault -> C:\Research\physics-paper-ai-lab
```

Important: open the project root, not `notes/obsidian` separately. Then Obsidian will see:

```text
project/
iterations/
docs/
reviews/
paper/
quality_reports/
```

### Step 5.2. Start from Home

Open:

```text
notes/obsidian/Home.md
notes/obsidian/MOC_Physics_Article.md
project/07_status_dashboard.md
```

Pin these files in Obsidian.

### Step 5.3. Use Obsidian for conceptual links

Add links between files:

```markdown
Related to [[project/03_claims_register]]
Checked in [[iterations/20260614_001_problem_scoping]]
Based on [[project/02_assumptions_and_conventions]]
```

Use tags:

```markdown
#claim
#risk
#todo
#verified
#blocked
#needs-review
#dimension-check
#literature
#derivation
```

### Step 5.4. Maintain the dashboard

Main status file:

```text
project/07_status_dashboard.md
```

It must contain:

- current task;
- last successful iteration;
- blocked items;
- unverified claims;
- list of next steps.

### Step 5.5. Use Obsidian for review, not for auto-generating the entire project

Obsidian is convenient for:

- reading all iteration reports;
- seeing backlinks;
- finding unclosed `TODO` items;
- building a claims map;
- writing manual scientific notes;
- preparing questions for models.

Obsidian is less convenient for:

- running Python;
- building LaTeX;
- viewing Git diffs;
- controlling agent edits;
- making bulk changes.

The rule is:

```text
VS Code = production and change control.
Obsidian = thinking, map, reading, review.
```

---

## 6. Is there a difference between VS Code and Obsidian?

Yes, a significant one.

| Question | VS Code | Obsidian |
|---|---|---|
| Primary role | IDE / project control | Knowledge base / thinking system |
| Best use | Edit files, run code, Git, LaTeX, agent edits | Read, link ideas, see the project map |
| Git diff | Excellent | Limited, through plugins |
| Python/LaTeX | Excellent | Not the primary use case |
| AI agent with file access | Yes, convenient | Possible through plugins, less controlled |
| Work with `.claude/skills` | Best through Claude Code | Can read as ordinary `.md` files |
| Risk of accidental bulk edits | Controlled through diff | Higher if plugins are used without control |

Practical conclusion:

- write and run the project in VS Code;
- read and think about the project in Obsidian;
- keep the same folder open in both tools;
- do not edit the same file simultaneously in both applications;
- after major changes, make a `git commit`.

---

## 7. Recommended daily work cycle

### Step 7.0. Context recovery at the start of a session

Before starting each session, the model must be given the current project state again.
The model does not remember previous conversations. This is especially important when working on long projects
where context is compacted or lost.

Template prompt for starting a session:

```text
You are working in the physics-paper-ai-lab repository.

First read these files:
1. .claude/CLAUDE.md
2. project/07_status_dashboard.md
3. project/06_task_index.md
4. [the last file in iterations/]

Choose one unfinished task from the task index.
Tell me: which task you chose, which files you still need to read, whether there are blocking issues.
Do not start executing the task until I confirm.
```

If the session context was compacted (old messages replaced by a summary), add to the prompt:

```text
The previous session context was automatically compressed. All necessary project state
is in the files. Do not make assumptions about what was in the previous messages —
read only the files.
```

Context recovery takes one model response. After that you can give the next task.

### Step 7.1. Open the project

```powershell
cd C:\Research\physics-paper-ai-lab
code .
```

Open the Obsidian vault in parallel:

```text
C:\Research\physics-paper-ai-lab
```

### Step 7.2. Check status

Open:

```text
project/07_status_dashboard.md
project/06_task_index.md
```

Choose one small task.

### Step 7.3. Create an iteration report

```powershell
python scripts/new_iteration.py
```

Short name:

```text
check dimensional consistency
```

### Step 7.4. Run the executor model

The prompt depends on the current project stage. Use the appropriate template below.

**Stage 1–2 (problem statement, literature):**

```text
Read .claude/CLAUDE.md, skill research-question-scope, project/01_research_question.md and project/02_assumptions_and_conventions.md.
Execute task [T_ID]: [task name].
Create a new iteration report in iterations/.
Do not change the manuscript and do not make claims that are not verified.
```

**Stage 2–3 (deriving formulas, checks):**

```text
Read .claude/CLAUDE.md, skill physics-derivation-auditor, project/02_assumptions_and_conventions.md and project/03_claims_register.md.
Execute task [T_ID]: [task name].
Create a new iteration report. Fill in all Verification sections.
If a step is not proven, write BLOCKED.
```

**Stage 3–4 (numerical calculations, figures):**

```text
Read .claude/CLAUDE.md, skill numerical-experiment-runner, project/03_claims_register.md.
Execute task [T_ID]: [task name].
Save code, run logs, parameters. Do not tune parameters without recording the change.
Create an iteration report with a run log.
```

**Stage 5 (manuscript):**

```text
Read .claude/CLAUDE.md, skill manuscript-builder, project/03_claims_register.md, paper/references/reference_audit.md.
Write only section [X]. Use only claims with passport status PASS or EXPLAINED.
Do not add citations without checking in reference_audit.md.
Create an iteration report with a traceability table.
```

**Stage 6 (review):**

```text
Read .claude/CLAUDE.md, skill reviewer-panel and reviews/TEMPLATE_review.md.
Conduct a [friendly/hostile/technical] review of [artifact].
Fill in reviews/TEMPLATE_review.md. Add blocking issues to reviews/rebuttal_matrix.md.
Do not fix the manuscript in the same iteration.
```

General rule: one prompt — one small task. Do not give multiple tasks at once.

### Step 7.5. Check the result

Check:

```powershell
git diff
python scripts/check_project_contract.py
```

If calculations appeared, run the corresponding Python scripts or notebooks.

### Step 7.6. Send to a reviewer model

Copy the iteration report and use the prompt from `reviews/reviewer_prompt.md` in a fresh context with any AI model.

The standard review prompt from that file works with any model. The key requirement is fresh context — do not carry conversation history into the review.

### Step 7.7. Record the human decision

Update:

```text
project/05_decision_log.md
project/07_status_dashboard.md
reviews/rebuttal_matrix.md
```

### Step 7.8. Compress the session (before closing)

If the session was productive, run the compress-session skill before closing:

```text
Use skill compress-session. Write the session log and update the status dashboard.
```

This creates a recovery point for the next session.

### Step 7.9. Make a commit

```powershell
git add .
git commit -m "T0XX verify dimensional consistency"
```

---

## 8. Model roles

See `docs/03-model-roles.md` for the full description. Summary:

Any AI model can execute any role. The roles are:

1. **Executor**: reads and writes project files, creates iteration reports, builds LaTeX.
2. **Reviewer**: examines an artifact in a fresh context for errors and gaps.
3. **Human Author**: the only non-interchangeable role — takes scientific responsibility.

Do not assign a specific model to a specific role permanently. Use whichever model is available.

---

## 9. Minimum set of files the model must read before each task

For any task:

```text
.claude/CLAUDE.md
project/07_status_dashboard.md
project/06_task_index.md
iterations/TEMPLATE_iteration_report.md
```

For problem scoping:

```text
.claude/skills/research-question-scope/SKILL.md
project/01_research_question.md
project/02_assumptions_and_conventions.md
```

For literature:

```text
.claude/skills/literature-review-ledger/SKILL.md
paper/references/references.bib
paper/references/reference_audit.md
```

For formulas:

```text
.claude/skills/physics-derivation-auditor/SKILL.md
.claude/skills/mathematical-consistency-checker/SKILL.md
project/02_assumptions_and_conventions.md
project/03_claims_register.md
```

For numerical checks:

```text
.claude/skills/numerical-experiment-runner/SKILL.md
project/04_risk_register.md
```

For the manuscript:

```text
.claude/skills/manuscript-builder/SKILL.md
paper/manuscript/main.tex
paper/manuscript/sections/*.tex
```

For review:

```text
.claude/skills/reviewer-panel/SKILL.md
reviews/TEMPLATE_review.md
reviews/rebuttal_matrix.md
reviews/reviewer_prompt.md
```

---

## 10. Hard safety and quality rules

### Rule 1. No result without a `.md` report

If the model changed something, it must create or update a file in `iterations/`.

### Rule 2. No new claim without the claims register

Every claim in the paper must have an entry in:

```text
project/03_claims_register.md
```

### Rule 3. No new assumption without a decision log

New assumptions are recorded in:

```text
project/02_assumptions_and_conventions.md
project/05_decision_log.md
```

### Rule 4. No figure without provenance

Every figure must have:

- data source;
- generation script;
- parameters;
- date;
- verification that the figure was not manually tuned.

### Rule 5. No final text without hostile review

Every important section passes at minimum:

```text
draft -> review in fresh context (any model) -> human decision
```

### Rule 6. Git commit after each accepted step

Do not accumulate 20 changes without a commit.

---

## 11. Recommended order for writing the paper

Do not start with the Introduction. Start with the verifiable core.

### Phase 1 — problem statement

Files:

```text
project/01_research_question.md
project/02_assumptions_and_conventions.md
project/04_risk_register.md
```

Result:

- clear research question;
- exactly what is claimed;
- what is not claimed;
- limits of applicability.

### Phase 2 — claims register

File:

```text
project/03_claims_register.md
```

Result:

- list of all claims;
- evidence for each;
- verification status;
- links to derivations/experiments.

### Phase 3 — derivations

Files:

```text
templates/derivation_report_template.md
iterations/*derivation*.md
paper/manuscript/sections/03_theory.tex
```

Result:

- formula derivations;
- assumptions;
- dimensional checks;
- limiting cases.

### Phase 4 — numerical checks

Files:

```text
iterations/*numerical*.md
paper/figures/
```

Result:

- reproducible calculations;
- figures;
- logs;
- failure cases.

### Phase 5 — manuscript assembly

Files:

```text
paper/manuscript/main.tex
paper/manuscript/sections/*.tex
paper/references/references.bib
```

Result:

- coherent manuscript;
- citations;
- figures;
- discussion;
- limitations.

### Phase 6 — review panel

Files:

```text
reviews/TEMPLATE_review.md
reviews/rebuttal_matrix.md
reviews/reviewer_prompt.md
```

Result:

- list of blocking issues;
- major/minor comments;
- responses to comments;
- final readiness checklist.

---

## 12. How to formulate good prompts

### Bad prompt

```text
Write me a paper on my theory.
```

Why it is bad:

- task is too large;
- the model will start speculating;
- no report;
- no verification;
- cannot be reproduced.

### Good prompt

```text
You are working in the physics-paper-ai-lab repository.

Read:
- .claude/CLAUDE.md
- .claude/skills/physics-derivation-auditor/SKILL.md
- project/02_assumptions_and_conventions.md
- project/03_claims_register.md
- iterations/20260614_003_core_equation.md

Task: check Claim C-004.

Do only the following:
1. Check the algebraic derivation.
2. Check the dimensions.
3. Check two limiting cases.
4. Do not rewrite the manuscript.
5. Create a new iteration report.
6. Return a list of blocking issues and suggested next tasks.
```

---

## 13. How to restart a failed iteration

If the model did poorly:

1. Do not continue the same chat indefinitely.
2. Save the bad report as rejected or remove changes via Git.
3. Create a new iteration report.
4. Use `templates/prompt_handoff_template.md`.
5. Explicitly state that the previous attempt was rejected.

Prompt:

```text
Previous attempt rejected.
Reason: the model changed the manuscript without checking the claims register.

Start over.
Read only these files:
- .claude/CLAUDE.md
- .claude/skills/mathematical-consistency-checker/SKILL.md
- project/03_claims_register.md
- iterations/20260614_004_rejected_attempt.md

Make a new iteration with a smaller goal: only check the dimensions of Claim C-004.
Do not change the manuscript.
```

---

## 14. How to use Obsidian and VS Code together

Open the same folder in both:

```text
C:\Research\physics-paper-ai-lab
```

In VS Code:

- edit;
- run;
- check diff;
- commit.

In Obsidian:

- read;
- link;
- build MOC;
- mark risks;
- write manual notes.

After changing files in VS Code, Obsidian usually updates the vault automatically.

Not recommended:

- editing the same file simultaneously in both applications;
- keeping the project as a nested vault;
- storing important data only in Obsidian Canvas without a markdown copy;
- trusting AI plugins in Obsidian to change the entire repository without Git diff.

---

## 15. Minimal startup scenario for one day

### 1. Open the project

```powershell
cd C:\Research\physics-paper-ai-lab
code .
```

### 2. Check the contract

```powershell
python scripts/check_project_contract.py
```

### 3. Make the first Git commit if not done yet

```powershell
git status
git add .
git commit -m "init project scaffold"
```

### 4. Open the Obsidian vault

```text
C:\Research\physics-paper-ai-lab
```

### 5. Open the dashboard

```text
project/07_status_dashboard.md
```

### 6. Create the first working iteration

```powershell
python scripts/new_iteration.py
```

Short title:

```text
define research question
```

### 7. Launch the model

Prompt:

```text
Read .claude/CLAUDE.md, docs/04-iteration-protocol.md, project/00_master_plan.md, project/01_research_question.md and skill research-question-scope.

Execute only one task: clarify the research question and scope of the paper.

Create/fill the current iteration report.
Update project/01_research_question.md.
If assumptions appeared, add them to project/02_assumptions_and_conventions.md and project/05_decision_log.md.
Do not write the introduction and do not make claims you cannot verify.
```

### 8. Check the diff

```powershell
git diff
```

### 9. Send the result to a reviewer model

Copy the iteration report and use `reviews/reviewer_prompt.md` in a fresh context with any AI model. Ask for a hostile review.

### 10. Accept or reject

If accepted:

```powershell
git add .
git commit -m "T001 define research question"
```

If rejected:

```powershell
git restore .
```

or create a new rejected report and repeat with a smaller task.

---

## 16. Recommended model configurations

### Simplest configuration

```text
VS Code + Claude Code extension + Obsidian + Git
```

This is the best starting point.

### Stronger configuration

```text
VS Code
├── Primary executor model (any model with file access)
├── Secondary model in fresh context: reviewer and structural critic
├── Continue or Cline: connect additional models as needed
└── Git: change control

Obsidian
└── reading, map, dashboard, backlinks
```

### Maximum verification configuration

```text
Any model creates artifact
A different model (or same model in fresh context) checks structure and text
Same or another model checks formulas, code, counterexamples
Human makes the decision
Git records the result
```

The specific model assignment is up to you. There is no required combination.

---

## 17. The main rule of the project

A paper is not considered written until a verifiable chain exists:

```text
research question
-> assumptions
-> claims
-> derivations
-> numerical checks
-> figures
-> manuscript
-> reviews
-> rebuttal matrix
-> publication checklist
```

If any element is missing, the model must not "write something nice" to fill it — it must create a task to verify that element.
