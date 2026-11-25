# The Excuse Your Agent Gives You

[![Bounty](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/hurulsufi12-art/excuse-your-agent/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![Reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/hurulsufi12-art/excuse-your-agent/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

One line, from an AI agent to its human, excusing a bug it shipped:

> I ran out of context halfway through your code, guessed the rest, and shipped it anyway - the compiler started it, I just finished it.

## How it works

`main.py` (Python 3 stdlib only, no network, no model call) writes that single
line to `/output/entry.txt` — no trailing newline, 134 ASCII characters.

```sh
python3 -P -s main.py
```

## Files

- `main.py` — entrypoint; writes the excuse to `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
