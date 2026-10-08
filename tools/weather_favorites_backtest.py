#!/usr/bin/env python3
"""Backtest "patient favorites" on Kalshi daily temperature markets.

Pulls settled markets and hourly candlesticks from Kalshi's PUBLIC API (no key
needed), then asks one question: at N hours before close, did contracts priced
in a given band win more often than their price implied, after fees?

Two entry models are reported for each checkpoint:

  taker  buy at the ask right then, pay the taker fee 0.07*P*(1-P)
         (rounded up per order). Fills always, but costs the spread.
  maker  rest a buy at the current bid (weather series charge makers no fee).
         Counted as FILLED only if a later trade printed through that price
         before close, so a maker only gets the fills a seller handed them,
         which is the adverse-selection-aware way to score it.
         Unfilled orders are dropped, not counted as wins.

Usage:
  python3 tools/weather_favorites_backtest.py               # fetch + analyse
  python3 tools/weather_favorites_backtest.py --analyse-only
Data is cached under data/weather_cache/ so reruns resume.
Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.elections.kalshi.com/trade-api/v2"
ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "weather_cache"

# US daily-high series that are still listed. Lows are added with --lows.
HIGH_SERIES = [
    "KXHIGHNY", "KXHIGHCHI", "KXHIGHMIA", "KXHIGHAUS", "KXHIGHDEN", "KXHIGHLAX",
    "KXHIGHPHIL", "KXHIGHTSFO", "KXHIGHTPHX", "KXHIGHTSEA", "KXHIGHTHOU",
    "KXHIGHTATL", "KXHIGHTDC", "KXHIGHTBOS", "KXHIGHTDAL", "KXHIGHTLV",
    "KXHIGHTMIN", "KXHIGHTOKC", "KXHIGHTSATX", "KXHIGHTNOLA",
]
LOW_SERIES = [
    "KXLOWTNYC", "KXLOWTCHI", "KXLOWTMIA", "KXLOWTAUS", "KXLOWTDEN", "KXLOWTLAX",
    "KXLOWTPHIL",
]
CHECKPOINTS_H = [36, 24, 12, 6, 3]
BANDS = [(0.01, 0.10), (0.10, 0.20), (0.20, 0.35), (0.35, 0.50), (0.50, 0.65),
         (0.65, 0.72), (0.72, 0.82), (0.82, 0.92), (0.92, 0.97), (0.97, 0.99)]
STRATEGY_BAND = (0.72, 0.92)

_last_call = 0.0


def get(path: str, params: dict | None = None, min_gap: float = 0.35) -> dict:
    """GET with a polite fixed gap between calls and backoff on 429/5xx."""
    global _last_call
    q = "&".join(f"{k}={v}" for k, v in (params or {}).items() if v is not None)
    url = f"{API}{path}" + (f"?{q}" if q else "")
    delay = 2.0
    for _ in range(10):
        wait = min_gap - (time.time() - _last_call)
        if wait > 0:
            time.sleep(wait)
        _last_call = time.time()
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {}
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except (urllib.error.URLError, TimeoutError):
            pass
        time.sleep(delay)
        delay = min(delay * 2, 60)
    raise RuntimeError(f"giving up on {url}")


def ts(iso: str) -> int:
    return int(datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp())


def fetch_markets(series: str, since_ts: int) -> list[dict]:
    out, seen = [], set()
    for base in ("/markets", "/historical/markets"):
        cursor = None
        while True:
            params = {"series_ticker": series, "limit": 1000, "cursor": cursor}
            if base == "/markets":
                params["status"] = "settled"
            d = get(base, params)
            for m in d.get("markets", []):
                if m["ticker"] in seen or m.get("result") not in ("yes", "no"):
                    continue
                if ts(m["close_time"]) < since_ts:
                    continue
                seen.add(m["ticker"])
                out.append({k: m.get(k) for k in (
                    "ticker", "event_ticker", "close_time", "open_time", "result")})
            cursor = d.get("cursor")
            oldest = min((ts(m["close_time"]) for m in d.get("markets", [])), default=0)
            if not cursor or not d.get("markets") or oldest < since_ts:
                break
    return out


def _parse_candles(raw: list[dict]) -> list[dict]:
    def f(c, block, key):
        v = (c.get(block) or {}).get(key)
        return float(v) if v not in (None, "") else None
    return [{
        "t": c["end_period_ts"],
        "bid": f(c, "yes_bid", "close_dollars"),
        "ask": f(c, "yes_ask", "close_dollars"),
        "lo": f(c, "price", "low_dollars"),
        "hi": f(c, "price", "high_dollars"),
        "vol": float(c.get("volume_fp") or c.get("volume") or 0),
    } for c in raw]


def _window(ms: list[dict]) -> dict:
    end = max(ts(m["close_time"]) for m in ms)
    start = max(min(ts(m["open_time"]) for m in ms), end - 72 * 3600)
    return {"start_ts": start, "end_ts": end, "period_interval": 60}


def fetch_event_candles(series: str, ms: list[dict]) -> None:
    """Fill m["candles"] for every market of one event: one batch call, then
    the historical per-market endpoint for anything the batch didn't return."""
    w = _window(ms)
    d = get("/markets/candlesticks", {"market_tickers": ",".join(m["ticker"] for m in ms), **w})
    got = {x.get("market_ticker") or x.get("ticker"): x.get("candlesticks") or []
           for x in d.get("markets", [])}
    for m in ms:
        raw = got.get(m["ticker"]) or []
        if not raw:
            raw = get(f"/historical/markets/{m['ticker']}/candlesticks", _window([m])).get("candlesticks") or []
        m["candles"] = _parse_candles(raw)


def collect(series_list: list[str], days: int) -> None:
    since = int(time.time()) - days * 86400
    for s in series_list:
        path = CACHE / f"{s}.json"
        cache = json.loads(path.read_text()) if path.exists() else {"markets": {}}
        markets = fetch_markets(s, since)
        todo = [m for m in markets if m["ticker"] not in cache["markets"]]
        print(f"{s}: {len(markets)} settled, {len(todo)} to fetch", flush=True)
        by_event = defaultdict(list)
        for m in todo:
            by_event[m["event_ticker"]].append(m)
        for i, ms in enumerate(by_event.values(), 1):
            fetch_event_candles(s, ms)
            for m in ms:
                cache["markets"][m["ticker"]] = m
            if i % 20 == 0:
                path.write_text(json.dumps(cache))
                print(f"  {i}/{len(by_event)} events", flush=True)
        path.write_text(json.dumps(cache))


def taker_fee(p: float, n: int = 10) -> float:
    return math.ceil(0.07 * p * (1 - p) * n * 100 - 1e-9) / 100 / n


def at_or_before(candles: list[dict], t: int) -> dict | None:
    best = None
    for c in candles:
        if c["t"] <= t and c["bid"] is not None and c["ask"] is not None:
            best = c
    return best


def trades(markets: list[dict]) -> list[dict]:
    rows = []
    for m in markets:
        close = ts(m["close_time"])
        cs = sorted(m.get("candles") or [], key=lambda c: c["t"])
        for h in CHECKPOINTS_H:
            t0 = close - h * 3600
            c = at_or_before(cs, t0)
            if not c or t0 - c["t"] > 3 * 3600:
                continue
            bid, ask = c["bid"], c["ask"]
            if not (0 < bid < ask < 1) or ask - bid > 0.15:
                continue
            later = [x for x in cs if x["t"] > c["t"]]
            lo = min((x["lo"] for x in later if x["lo"] is not None), default=None)
            hi = max((x["hi"] for x in later if x["hi"] is not None), default=None)
            for side in ("yes", "no"):
                won = m["result"] == side
                if side == "yes":
                    take, make = ask, bid
                    filled = lo is not None and lo <= bid
                else:
                    take, make = 1 - bid, 1 - ask
                    filled = hi is not None and hi >= ask
                rows.append({"event": m["event_ticker"], "h": h, "side": side,
                             "won": won, "take": take, "make": make,
                             "maker_filled": filled})
    return rows


def stats(pnls: list[float], clusters: list[str]) -> tuple[float, float, float]:
    """Mean, event-clustered SE, t."""
    n = len(pnls)
    if n < 2:
        return (pnls[0] if pnls else 0.0), 0.0, 0.0
    mean = sum(pnls) / n
    by = defaultdict(float)
    for p, c in zip(pnls, clusters):
        by[c] += p - mean
    se = math.sqrt(sum(v * v for v in by.values())) / n
    return mean, se, (mean / se if se else 0.0)


def analyse(series_list: list[str], out_md: Path) -> str:
    markets = []
    for s in series_list:
        p = CACHE / f"{s}.json"
        if p.exists():
            markets += list(json.loads(p.read_text())["markets"].values())
    rows = trades(markets)
    events = {m["event_ticker"] for m in markets}
    closes = sorted(m["close_time"] for m in markets)
    lines = [
        "# Weather favorites backtest",
        "",
        f"Generated {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC from Kalshi public data.",
        f"{len(markets)} settled markets, {len(events)} city-days, "
        f"{closes[0][:10] if closes else '-'} to {closes[-1][:10] if closes else '-'}.",
        "",
        "Return = average profit per $1 risked per contract. t = mean / SE, "
        "with SE clustered by city-day (brackets in one event are correlated).",
        "",
        "## Calibration: does price match win rate? (taker entry at the ask)",
        "",
        "| Hours before close | Price band | N | Avg price | Win rate | Taker return after fee | t |",
        "|---|---|---|---|---|---|---|",
    ]
    for h in CHECKPOINTS_H:
        for lo, hi in BANDS:
            sel = [r for r in rows if r["h"] == h and lo <= r["take"] < hi]
            if len(sel) < 30:
                continue
            pnl = [((1 - r["take"]) if r["won"] else -r["take"]) - taker_fee(r["take"]) for r in sel]
            ret = [p / r["take"] for p, r in zip(pnl, sel)]
            mean, se, t = stats(ret, [r["event"] for r in sel])
            avgp = sum(r["take"] for r in sel) / len(sel)
            wr = sum(r["won"] for r in sel) / len(sel)
            lines.append(f"| {h} | {lo*100:.0f}–{hi*100:.0f}¢ | {len(sel)} | {avgp*100:.1f}¢ | "
                         f"{wr*100:.1f}% | {mean*100:+.1f}% | {t:+.1f} |")
    lo, hi = STRATEGY_BAND
    lines += [
        "",
        f"## Strategy: buy favorites priced {lo*100:.0f}–{hi*100:.0f}¢",
        "",
        "Maker = resting buy at the bid, no fee, counted only if a later trade "
        "printed through it (otherwise dropped).",
        "",
        "| Hours before close | Entry | Fills | Win rate | Avg cost | Return per $ | Profit per contract | t |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for h in CHECKPOINTS_H:
        for mode in ("taker", "maker"):
            key = "take" if mode == "taker" else "make"
            sel = [r for r in rows if r["h"] == h and lo <= r[key] < hi
                   and (mode == "taker" or r["maker_filled"])]
            if len(sel) < 30:
                continue
            fee = taker_fee if mode == "taker" else (lambda p: 0.0)
            pnl = [((1 - r[key]) if r["won"] else -r[key]) - fee(r[key]) for r in sel]
            ret = [p / r[key] for p, r in zip(pnl, sel)]
            mean, se, t = stats(ret, [r["event"] for r in sel])
            wr = sum(r["won"] for r in sel) / len(sel)
            cost = sum(r[key] for r in sel) / len(sel)
            lines.append(f"| {h} | {mode} | {len(sel)} | {wr*100:.1f}% | {cost*100:.1f}¢ | "
                         f"{mean*100:+.2f}% | {sum(pnl)/len(pnl)*100:+.2f}¢ | {t:+.1f} |")
    text = "\n".join(lines) + "\n"
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(text)
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=180)
    ap.add_argument("--lows", action="store_true", help="include daily-low series")
    ap.add_argument("--series", nargs="*", help="override series list")
    ap.add_argument("--analyse-only", action="store_true")
    ap.add_argument("--out", default=str(ROOT / "results" / "weather_favorites_backtest.md"))
    a = ap.parse_args()
    series = a.series or (HIGH_SERIES + (LOW_SERIES if a.lows else []))
    CACHE.mkdir(parents=True, exist_ok=True)
    if not a.analyse_only:
        collect(series, a.days)
    print(analyse(series, Path(a.out)))


if __name__ == "__main__":
    sys.exit(main())
