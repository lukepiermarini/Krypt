import sys, json
sys.path.insert(0, "/home/user/Krypt/tools")
import weather_favorites_backtest as w
markets=[]
for p in w.CACHE.glob("KXHIGH*.json"):
    markets += list(json.loads(p.read_text())["markets"].values())
# strict fill: a trade must print STRICTLY through our price (queue at our level assumed ahead of us)
def trades_strict(markets, h):
    out=[]
    for m in markets:
        close=w.ts(m["close_time"]); cs=sorted(m.get("candles") or [], key=lambda c:c["t"])
        c=w.at_or_before(cs, close-h*3600)
        if not c or close-h*3600-c["t"]>3*3600: continue
        bid,ask=c["bid"],c["ask"]
        if not (0<bid<ask<1) or ask-bid>0.15: continue
        later=[x for x in cs if x["t"]>c["t"]]
        hi=max((x["hi"] for x in later if x["hi"] is not None), default=None)
        lo=min((x["lo"] for x in later if x["lo"] is not None), default=None)
        for side in ("yes","no"):
            cost = bid if side=="yes" else 1-ask
            filled = (lo is not None and lo < bid - 1e-9) if side=="yes" else (hi is not None and hi > ask + 1e-9)
            if 0.72<=cost<0.92 and filled:
                out.append((m["event_ticker"], cost, m["result"]==side, m["close_time"][:7]))
    return out
for h in (30,24,21,18):
    rs=trades_strict(markets,h)
    ret=[((1-c) if wn else -c)/c for _,c,wn,_ in rs]
    mean,se,t=w.stats(ret,[e for e,*_ in rs])
    print(f"h={h} strict-fill highs: n={len(rs)} ret={mean*100:+.2f}% t={t:+.1f}")
