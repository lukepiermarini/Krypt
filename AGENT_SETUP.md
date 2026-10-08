# Strategy #1 setup: Weather NO-maker

This file replaces the earlier "Weather Favorites agent" plan. A backtest on 10,380 real settled Kalshi
markets showed that version loses money. Details are below.

## What the data says (backtest, 2026-10-08)

Source: `tools/weather_favorites_backtest.py`, run against 27 US city series (20 daily highs and 7 daily
lows): 10,380 settled markets and 1,730 city-days. New York and Chicago go back to May 2026. The other
cities cover Aug–Oct 2026. Full tables are in `results/weather_favorites_backtest.md` and
`results/robustness.md`.

| Version | Result | Verdict |
|---|---|---|
| Buy favorites (72–92¢) **at the ask** (taker) | −0.9% to −5.2% per $ at every entry time | ❌ Fees and spread eat the edge. This is all an agent can paper-trade in Krypt. |
| Same, as a **resting limit order** (maker, no fee), 24h before close | **+2.5% per $, t = 2.8** (2,119 fills) | ✅ The only cell that holds |
| …daily **highs** only | **+3.6% per $, t = 3.7** (1,706 fills) | ✅ |
| …daily **lows** only | −2.0% per $ | ❌ Skip lows |
| …with **strict fills** (a trade must print *through* your price) | +2.6% (24h), +2.2% (21h); about 0% at 30h and 18h | ✅ Narrow but real: about 20–24h before close |
| Longshots under 10¢ | −75% to −100% | ❌ Never buy |

In practice, about 98% of these fills are **NO** orders on the second- or third-most-likely bracket,
the near-miss brackets priced 8–28¢ YES. The edge is that those brackets are overpriced. Selling them
patiently, with a resting order rather than at the market, pays about **2¢ per contract**.

**Caveats:**
- About 2.5 months of data for most cities.
- Six entry times were tried and the best is reported, so some of this is luck.
- The fill model only uses hourly candle highs and lows.
- Expect the real edge to be smaller than the backtest, perhaps +1–2% per $.

That's why the next step is a forward test on days the backtest never saw.

## Step 1: forward paper test (running now, needs nothing from you)

`tools/weather_maker_forward.py` records, each night, the NO limit orders the strategy would post:

- 20 US daily-high cities.
- 20–25h before close.
- NO priced 72–92¢.
- Spread no wider than 15¢.
- Up to 3 brackets per city-day.
- 10 contracts each.

It then checks Kalshi's public trade tape to see whether each order would have filled, using the strict
rule, and books the P&L at settlement. It needs no key and no money.

```bash
python3 tools/weather_maker_forward.py          # run hourly, or at least ~00:00–04:00 ET
python3 tools/weather_maker_forward.py report   # see results
```

Expect about 20–40 fills a day. Judge it after about 4–6 weeks (roughly 1,000 settled fills):

- Return above +1% per $ with t ≥ 2: go to Step 2.
- Return between 0 and +1%: keep running.
- Negative: stop. The backtest was noise.

## Step 2: tiny live test (only after Step 1 passes)

Krypt's agent paper mode can't rest orders, so the live version has two options:

- **Krypt's Terminal ticket.** Place the NO limit orders by hand each night. It's slow, but every
  Krypt safety rail applies.
- **A small live executor.** Add `--live` to the forward script, using your Kalshi API key and the
  same parameters. I'd write it once Step 1 passes.

Live rules:
- Start at **10 contracts per order**.
- Cap total open cost at about $150.
- Stop if down $50.

Compare the live fill rate and P&L against the forward test every week.

## The Krypt agent (optional, for the AI scoreboard only)

The AI agent is still worth running in **paper**, for the forecasting scoreboard rather than for
profit. Its trades are taker trades, which the backtest says lose. Set its **Min edge to 5¢** so it
trades only where it has a real forecast reason, and treat its P&L as a measure of how good the AI's
forecasts are.

| Field | Value |
|---|---|
| Name | `Weather Forecaster` |
| Mode | Paper |
| Categories | Climate |
| Price | 72–92¢ |
| Hours to close | 18–30 |
| Min edge | 5¢ |
| Max contracts per market | 10 |
| Daily spend | $100 |

Guide text (paste into the agent's Guide box):

```
You forecast Kalshi daily HIGH temperature markets for US cities (skip lows,
rain, global series). For each city-day closing in 18-30 hours: read the
market rules (station + settlement source), get the latest NWS/NBM forecast
for that station, and estimate each bracket's probability from forecast high
and a typical 2-3F error. record_forecast for the leading bracket and the
next two. Only trade NO on a near-miss bracket priced 72-92c when your
probability beats the price by the minimum edge after fees. 10 contracts,
hold to settlement. Never buy anything under 20c.
```
