# Tools and Setup

## Supported platforms

This toolkit works on:

- **Linux** (Ubuntu, Debian, Arch, etc.) — native, no extra steps.
- **macOS** — native, no extra steps.
- **Windows 11 + WSL 2** — recommended for Windows users; run all terminal commands inside WSL.
- **Windows 11 native** — works, but LaTeX and Python commands may differ slightly.

There are no platform restrictions. The project is entirely file-based (Markdown, Python, LaTeX, Git) and runs identically on all platforms.

---

## Recommended toolset

| Tool | Purpose | Notes |
|------|---------|-------|
| **Visual Studio Code** | Primary project editor | Works on all platforms |
| **Git** | Version control | `git` (Linux/macOS/WSL) or Git for Windows |
| **Python 3.11+** | Scripts, calculations, checks | Pre-installed on most Linux distros |
| **TeX Live** (Linux/macOS/WSL) or **MiKTeX** (Windows) | LaTeX manuscript build | TeX Live recommended for non-Windows |
| **Obsidian** | Navigation, concept map, reading | Optional but useful |
| **Zotero or JabRef** | Bibliography and BibTeX management | Optional |
| **Claude Code** or any AI agent with file access | AI executor role | Claude Code CLI works on Linux, macOS, Windows |

---

## Installation (Linux / macOS / WSL)

```bash
# Git
sudo apt install git          # Debian/Ubuntu
brew install git              # macOS

# Python
sudo apt install python3 python3-pip

# TeX Live (minimal, add packages as needed)
sudo apt install texlive-full  # or texlive texlive-latex-extra

# Claude Code CLI
npm install -g @anthropic-ai/claude-code
# or: curl -fsSL https://claude.ai/install.sh | sh
```

Verify:

```bash
git --version
python3 --version
pdflatex --version
```

---

## Installation (Windows 11 native)

Install:

- [Git for Windows](https://git-scm.com/)
- [Python 3.11+](https://python.org)
- [MiKTeX](https://miktex.org/) or [TeX Live](https://tug.org/texlive/)
- [Visual Studio Code](https://code.visualstudio.com/)

Verify in PowerShell:

```powershell
git --version
python --version
pdflatex --version
```

---

## Project folder

**Linux / macOS / WSL:**
```bash
mkdir ~/Research
cd ~/Research
# unzip or clone the toolkit here
```

**Windows native:**
```powershell
mkdir C:\Research
cd C:\Research
```

---

## VS Code recommended extensions

- Markdown All in One
- LaTeX Workshop
- Python
- GitLens
- Todo Tree
- YAML
- Claude Code (if using Claude)

---

## Obsidian setup

Open the project root folder as a vault. Suggested start pages:

- `notes/obsidian/Home.md`
- `project/07_status_dashboard.md`

---

## Synchronization rule

Do not keep the only copy of important work in a chat window. After every model response, transfer the result to a `.md` file — or require the model to write the file directly via Claude Code or another file-capable agent.
