# Review and Preparation for Publication

## AI as reviewers, not responsible authors

AI models can be used as reviewers, editors, verification generators, and reproducibility assistants. But responsibility for the scientific content, references, conclusions, and publication remains with the human author.

## Minimum set of checks before submission

- All references exist and match the claims they support.
- All BibTeX entries have been verified manually.
- All formulas have a derivation report or a source.
- All figures have provenance.
- All calculations are reproducible from a clean state.
- All claims in `project/03_claims_register.md` have passport status `PASS` or `EXPLAINED`, or are explicitly excluded from the manuscript.
- All AI contributions are described in acknowledgements/methods in accordance with the rules of the venue/journal.
- No "zombie sections": old repeated fragments that contradict the current version.
- No "AI meta-comments": phrases such as "as an AI language model", "insert citation here", "needs verification".

## Reviewer roles

### Friendly reviewer

Tries to understand the idea, improves the presentation, looks for weaknesses gently.

### Hostile reviewer

Looks for reasons to reject the paper: unverified novelty, weak references, formula errors, non-reproducibility.

### Technical auditor

Checks only derivations, code, units, limits, equations, figures.

### Editor

Checks whether there is a story, why it matters, who the paper is addressed to, and whether the journal level is appropriate.

## How to run a review

Use `reviews/reviewer_prompt.md` with any AI model in a **fresh context**. Paste the artifact (manuscript section, iteration report, derivation) and the appropriate prompt. Do not carry conversation history into the review session.

For a comprehensive pre-submission review, use the seven-pass review skill: `.claude/skills/seven-pass-review/SKILL.md`.

## Rebuttal matrix

Every comment goes into `reviews/rebuttal_matrix.md`:

```text
review_id -> issue -> severity -> affected files -> response -> status
```

A comment cannot be closed with the word "fixed." You must specify a commit/iteration/file/line or explain why the comment is rejected.
