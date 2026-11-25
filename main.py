#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest entry for make.fun.

Writes one original joke about crypto trading life to
/output/entry.txt. The joke turns a 3am chart check into a race the
trader loses before it starts: the alarm was set to watch the
chart, but the liquidation already happened first. One line, no
trailing newline, so the judge reads exactly the joke.
Deterministic, standard library only.
"""

import os

LINE = "I set an alarm for 3am to check the chart. The liquidation beat me to it."


def main():
    # The gate allows 1-200 characters; the line is 73 characters, and
    # it is written exactly, with no trailing newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
