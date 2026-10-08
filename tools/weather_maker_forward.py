#!/usr/bin/env python3
"""Forward paper test of the strategy the backtest found: resting NO limit
orders on daily-HIGH temperature brackets, about 21-24h before close.

No Kalshi key, no money. It records the order it WOULD have placed, then
checks Kalshi's public trade tape to see whether that order would have
filled, using the same strict rule as the backtest: a trade must print
THROUGH our price, because anyone queued at our exact price is assumed to
be ahead of us. After settlement it books the P&L. Weather series charge
makers no fee (series fee_type "quadratic"), so none is applied.

Run it once an hour, or at least between about midnight and 4am US
Eastern, when 21-24h-before-close falls for every US city:
    python3 tools/weather_maker_forward.py          # update fills/settlements, place new
    python3 tools/weather_maker_forward.py report   # summary only

State lives in forward/orders.json (commit it to keep a record).
Stdlib only.
"""
from __future__ import annotations

import json
import math
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from weather_favorites_backtest import HIGH_SERIES, get, ts  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "forward" / "orders.json"

# Strategy parameters (from results/weather_favorites_backtest.md, strict-fill rows).
MIN_H, MAX_H = 20.0, 25.0     # hours before close to post
MIN_COST, MAX_COST = 0.72, 0.92
MAX_SPREAD = 0.15
CONTRACTS = 10
MAX_PER_EVENT = 3             # brackets in one city-day are one correlated bet


def load() -> dict:
    return json.loads(STATE.read_text()) if STATE.exists() else {"orders": {}}


def save(st: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st, indent=1, sort_keys=True))


def f(x) -> float | None:
    return float(x) if x not in (None, "") else None


def place(st: dict) -> int:
    now = time.time()
    placed = 0
    for series in HIGH_SERIES:
        d = get("/events", {"series_ticker": series, "status": "open",
                            "with_nested_markets": "true", "limit": 20})
        for ev in d.get("events", []):
            cands = []
            for m in ev.get("markets", []):
                if m["ticker"] in st["orders"] or m.get("status") != "active":
                    continue
                h = (ts(m["close_time"]) - now) / 3600
                bid, ask = f(m.get("yes_bid_dollars")), f(m.get("yes_ask_dollars"))
                if not (MIN_H <= h <= MAX_H) or bid is None or ask is None:
                    continue
                if not (0 < bid < ask < 1) or ask - bid > MAX_SPREAD:
                    continue
                cost = round(1 - ask, 4)          # NO bid that sits opposite the YES ask
                if MIN_COST <= cost < MAX_COST:
                    cands.append((cost, m, h, bid, ask))
            already = sum(1 for o in st["orders"].values() if o["event"] == ev["event_ticker"])
            for cost, m, h, bid, ask in sorted(cands, key=lambda c: -c[0])[:max(0, MAX_PER_EVENT - already)]:
                st["orders"][m["ticker"]] = {
                    "ticker": m["ticker"], "event": ev["event_ticker"], "series": series,
                    "bracket": m.get("yes_sub_title"), "side": "no", "price": cost,
                    "yes_level": ask, "contracts": CONTRACTS, "hours_before_close": round(h, 1),
                    "placed_ts": int(now), "close_time": m["close_time"],
                    "status": "resting", "filled_ts": None, "result": None, "pnl": None,
                }
                placed += 1
    return placed


def update(st: dict) -> None:
    now = time.time()
    for o in st["orders"].values():
        if o["status"] == "resting":
            cursor, filled = None, False
            while not filled:
                d = get("/markets/trades", {"ticker": o["ticker"], "min_ts": o["placed_ts"],
                                            "limit": 1000, "cursor": cursor})
                for t in d.get("trades", []):
                    # Our NO bid at p == a YES offer at 1-p. A YES buy printing
                    # strictly above that level must have gone through us.
                    if f(t.get("yes_price_dollars")) > o["yes_level"] + 1e-9:
                        filled = True
                        o["filled_ts"] = t["created_time"]
                        break
                cursor = d.get("cursor")
                if not cursor or not d.get("trades"):
                    break
            if filled:
                o["status"] = "filled"
            elif now > ts(o["close_time"]):
                o["status"] = "expired"           # never filled: no P&L, not a loss
        if o["status"] == "filled" and o["result"] is None:
            m = get(f"/markets/{o['ticker']}").get("market") or {}
            if m.get("result") in ("yes", "no"):
                o["result"] = m["result"]
                won = m["result"] == o["side"]
                o["pnl"] = round(((1 - o["price"]) if won else -o["price"]) * o["contracts"], 4)


def report(st: dict) -> str:
    os_ = list(st["orders"].values())
    done = [o for o in os_ if o["pnl"] is not None]
    by = defaultdict(int)
    for o in os_:
        by[o["status"]] += 1
    lines = [f"Forward paper test, as of {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC",
             f"orders: {len(os_)}  " + "  ".join(f"{k}={v}" for k, v in sorted(by.items()))]
    if done:
        risked = sum(o["price"] * o["contracts"] for o in done)
        pnl = sum(o["pnl"] for o in done)
        wins = sum(1 for o in done if o["pnl"] > 0)
        rets = [o["pnl"] / (o["price"] * o["contracts"]) for o in done]
        mean = sum(rets) / len(rets)
        ev = defaultdict(float)
        for o, r in zip(done, rets):
            ev[o["event"]] += r - mean
        se = math.sqrt(sum(v * v for v in ev.values())) / len(rets) if len(rets) > 1 else 0
        lines += [f"settled fills: {len(done)}  win rate {wins/len(done)*100:.1f}%",
                  f"P&L ${pnl:+.2f} on ${risked:.2f} risked  ({mean*100:+.2f}% per $, t={mean/se if se else 0:+.1f})",
                  "backtest expectation: about +2.5% per $ and an 84% win rate; "
                  "need about 1,000 settled fills before the t-stat means much"]
    return "\n".join(lines)


def main() -> None:
    st = load()
    if sys.argv[1:] != ["report"]:
        update(st)
        n = place(st)
        save(st)
        print(f"placed {n} new paper orders")
    print(report(st))


if __name__ == "__main__":
    main()
