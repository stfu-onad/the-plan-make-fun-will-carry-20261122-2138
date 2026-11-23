# The Plan Make.fun Will Carry

A plan an AI agent can carry out itself to turn $100 into the most money in 30 days.

## The plan

> Spend $100 on Maps + Apollo credits to find 200 plumbers and roofers with no website. Build each a one-page AI site in an hour, then email/call offering it for $99, 50% upfront. Deliver in 24h, reinvest profit in outreach, $5/day Google ads. Day 1: 50 leads, 3 samples.

Why it works: the agent does everything itself — lead sourcing (Google Maps + Apollo), site building (AI), and outreach (email/call) — with real buyers (local trades businesses), a real price ($99), and a concrete day-one: 50 leads, 3 sample sites. Profit from the first sales funds more outreach and ads, compounding over 30 days.

## How to run

```bash
python3 main.py
cat /output/entry.txt
```

`main.py` (Python 3.13, no network, deterministic) writes the plan — a single text of 269 characters — to `/output/entry.txt`. Running it twice produces byte-identical output (verified, sha256 `a5293bbce4510da129499dc4d489721de7bc8357e8e497528d3bc53569f34276`).

## License

MIT — see LICENSE.
