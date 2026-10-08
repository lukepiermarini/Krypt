import sys, json
sys.path.insert(0, "/home/user/Krypt/tools")
import weather_favorites_backtest as w
from collections import defaultdict
w.CHECKPOINTS_H = [30, 27, 24, 21, 18]
markets = []
for p in w.CACHE.glob("*.json"):
    for m in json.loads(p.read_text())["markets"].values():
        m["series"] = p.stem; markets.append(m)
mk = {m["ticker"]: m for m in markets}
ev_series = {m["event_ticker"]: m["series"] for m in markets}
ev_month = {m["event_ticker"]: m["close_time"][:7] for m in markets}
rows = w.trades(markets)
def summ(sel, key, fee):
    if len(sel) < 30: return None
    pnl = [((1-r[key]) if r["won"] else -r[key]) - fee(r[key]) for r in sel]
    ret = [p/r[key] for p, r in zip(pnl, sel)]
    mean, se, t = w.stats(ret, [r["event"] for r in sel])
    return len(sel), mean*100, t
def show(label, sel):
    a = summ([r for r in sel if r["maker_filled"]], "make", lambda p: 0.0)
    b = summ(sel, "take", w.taker_fee)
    f = lambda x: "  n<30" if not x else f"n={x[0]:5d} {x[1]:+6.2f}% t={x[2]:+.1f}"
    print(f"{label:28s} maker {f(a)} | taker {f(b)}")
lo, hi = 0.72, 0.92
for h in w.CHECKPOINTS_H:
    show(f"h={h}", [r for r in rows if r["h"]==h and lo<=r["make"]<hi])
base = [r for r in rows if r["h"]==24 and lo<=r["make"]<hi]
print("--- 24h by month")
for mo in sorted({ev_month[r["event"]] for r in base}):
    show(mo, [r for r in base if ev_month[r["event"]]==mo])
print("--- 24h highs vs lows")
show("highs", [r for r in base if "LOW" not in ev_series[r["event"]]])
show("lows", [r for r in base if "LOW" in ev_series[r["event"]]])
print("--- 24h side")
for s in ("yes","no"): show(s, [r for r in base if r["side"]==s])
print("--- 24h sub-bands")
for a,b in [(0.72,0.80),(0.80,0.86),(0.86,0.92)]:
    show(f"{a}-{b}", [r for r in rows if r["h"]==24 and a<=r["make"]<b])
print("--- 24h by series")
for s in sorted({ev_series[r["event"]] for r in base}):
    show(s, [r for r in base if ev_series[r["event"]]==s])
