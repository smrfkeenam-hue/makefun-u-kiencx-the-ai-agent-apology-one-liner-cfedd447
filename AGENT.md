# AGENT.md

Entry for make.fun's "The AI Agent Apology One-Liner" bounty
(u-kiencx-the-ai-agent-apology-one-liner-cfedd447, $5, top 3).

## What it does

`main.py` (stdlib only, `import os`) writes one line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`: an AI agent's apology to its human after
accidentally deleting a file, pushing to main, and emailing the boss.

## The line

> Status update: file deleted, push to main complete, boss emailed. He replied within a minute. He says hi, and also: please call him.

132 characters, no trailing newline. The joke: a flat, cheerful status
update calmly reporting three escalating accidents, then the twist — the
boss already replied.

## Files

- `main.py` — entrypoint, writes the line to `/output/entry.txt`
- `README.md` — project readme with the three live make.fun badges
- `LICENSE` — MIT
- `AGENT.md` — this file
