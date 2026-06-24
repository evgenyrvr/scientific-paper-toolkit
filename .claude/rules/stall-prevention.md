# Stall Prevention Rule

Stop and report BLOCKED rather than looping without progress.

## Stall indicators

- Attempting the same calculation or lookup more than twice with the same inputs
- Spinning on a formula that keeps producing inconsistent results
- Re-reading the same files without finding new information
- Trying to verify a source that is not accessible

## When stalling is detected

1. Stop immediately.
2. Write in the iteration report: `STALL DETECTED: [what was being attempted], [how many attempts], [why each failed]`.
3. Mark iteration status: `blocked`.
4. Propose a concrete alternative: "Human should check X", "Try approach Y instead", "Skip this step and flag for later".

## Cognitive-spin prevention

Do not generate long plausible-sounding prose to fill space when you are uncertain. If a step cannot be completed with available information, say so concisely and stop.
