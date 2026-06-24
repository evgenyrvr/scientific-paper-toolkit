# Risk Register

| Risk ID | Risk | Severity | Trigger | Mitigation | Owner | Status |
|---------|------|----------|---------|-----------|-------|--------|
| R-001 | Model may declare verification complete without real check | high | word "verified" without checklist | require verification table | human | open |
| R-002 | Model may tune plots to look right | high | parameter changes / smoothing without recording | figure provenance + anti-cheating protocol | human | open |
| R-003 | Model may invent a reference | high | bib item without DOI/arXiv/journal confirmation | reference audit for each claim | human | open |
| R-004 | Model may revert to standard notation silently | medium | notation mismatch between iteration reports | assumptions/conventions lock in project/02 | Claude | open |
| R-005 | Impulse or other approximation may fail in a regime not checked | medium | [problem-specific trigger] | check validity condition explicitly | Claude | open |
| R-006 | Point-mass or other limiting formula used accidentally outside its domain | high | any formula applied without checking domain of validity | flag all formulas: if b < R, use extended formula | Claude | open |
| R-007 | [Problem-specific risk] | [severity] | [trigger] | [mitigation] | [owner] | open |
| R-008 | Context compaction mid-session causes model to lose project state | medium | model starts producing inconsistent results mid-session | run compress-session skill; update status_dashboard before closing | Claude | open |
| R-009 | Stall/cognitive-spin: model loops on same step without progress | medium | same calculation attempted 3+ times with no new approach | see stall-prevention rule; mark BLOCKED after 2 failed attempts | Claude | open |

## Risk severity legend

- `high`: could invalidate the main result
- `medium`: could affect a secondary result or introduce a factor
- `low`: affects presentation or precision only
