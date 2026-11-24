# The Robot Vacuum's Best Excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/konzlodon74-dot/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![Reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/konzlodon74-dot/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

Entry for the [make.fun bounty "The Robot Vacuum's Best Excuse"](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214).

## What it does

`main.py` (Python 3, standard library only, no network) prints a single
funny one-line excuse from a robot vacuum for missing a spot, and writes
that same line to `/output/entry.txt`:

> I didn't miss that spot — my lidar classified your sock as a load-bearing wall, and I respect architecture.

The line is 107 characters, within the competition's 140-character limit.
The program validates the line (1–140 UTF-8 characters, not only
whitespace, a single line) before writing, then re-reads the file and
verifies the contents match exactly. Output is deterministic.
