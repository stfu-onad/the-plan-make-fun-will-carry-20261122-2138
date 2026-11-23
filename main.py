#!/usr/bin/env python3
"""Write a concrete 30-day plan (<=280 chars) to /output/entry.txt.

Deterministic: same bytes on every run. No network, no randomness.
"""
import os

PLAN = (
    "Spend $100 on Maps + Apollo credits to find 200 plumbers and roofers with "
    "no website. Build each a one-page AI site in an hour, then email/call "
    "offering it for $99, 50% upfront. Deliver in 24h, reinvest profit in "
    "outreach, $5/day Google ads. Day 1: 50 leads, 3 samples."
)

assert 1 <= len(PLAN) <= 280, f"plan length {len(PLAN)} out of range"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)

if __name__ == "__main__":
    main()
