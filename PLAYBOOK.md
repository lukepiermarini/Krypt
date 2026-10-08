# Kalshi Bot Playbook (Krypt Trader v6.4)

Goal: find a Kalshi strategy that makes money after fees. Prove it on paper first, then go live small.

Bot: https://github.com/kryptccgit/KryTrader (v6.4.0, MIT license). It's an Electron desktop app with a
local Python backend, so it runs on **your own computer** and not on a server.

---

## 0. Code check (done 2026-10-08)

Before trusting it with a Kalshi key, I pulled the source and checked it:

- **Outbound hosts:** only Kalshi, the AI provider you choose (Anthropic, OpenAI, Gemini, OpenRouter),
  public price feeds (Coinbase, CoinGecko, CryptoCompare, Hyperliquid, Polymarket public API,
  weather.gov), and Discord/Telegram if you turn on the remote bot. I found nothing that sends keys or
  data to the authors.
- **No obfuscated code:** no `eval`, no base64-encoded payloads, no npm install hooks. The one `b64decode`
  is the Windows DPAPI decryption of your stored key.
- **Tests:** all 1,356 Python backend tests pass on Linux (Python 3.13).
- **Things to watch:**
  - "Build from source" in the README points to `scripflipped/krypt-trader`, a different repo from the
    one in the Discord post. Use the Discord link, or the Releases page of the repo you actually reviewed.
  - The Kalshi signup link in the README is a referral link that pays the authors. That's harmless, just
    so you know.
  - "Trusted mode" scripts run Python on your machine with no sandbox. Never turn it on for a script
    someone else wrote unless you've read it.
  - Installers aren't code-signed. Building from source is the safer option if you're comfortable doing it.

---

## 1. Install and first run (Paper mode, no money)

1. Download the installer for your OS from the repo's **Releases** page, or build it yourself:
   ```bash
   git clone https://github.com/kryptccgit/KryTrader.git && cd KryTrader
   npm install
   npm run dev        # needs Node 18+ and Python 3.11+
   ```
2. The app opens in **Paper** mode: real Kalshi prices and order books, with fake money. You don't need a
   Kalshi key yet.
3. Under **Settings → Account**, set the paper bankroll to the amount you would really trade with, for
   example $500. Testing with a fake $100k gives P&L numbers that won't carry over to real money.

## 2. Turn on data collection (do this on day one)

The backtester only uses history that **your own copy of the app records while it's open**. It has no
bulk history download. So:

- Go to **Backtest → Data collection** and switch it on.
- Leave the app running 24/7 if you can, on an always-on PC or a cheap mini PC, with sleep disabled.
- Every day it isn't recording is a day of data you can't test on later. Aim for **at least 2–4 weeks**
  before you believe any backtest.

## 3. Connect Claude Code as the agent (MCP)

1. In the app, open **AI Agents → Your own MCP client → Claude Code → Copy config**.
2. Paste that config into your Claude Code MCP settings. The token goes to the clipboard and is never
   shown on screen.
3. Create a few **named agents**, each with its own style and rules, so the scoreboard tracks them
   separately:
   - `Value hunter`: any category, needs a high minimum edge.
   - `Favorites`: only buys contracts above 80¢ (see §4).
   - `Closing-soon`: only trades markets that settle within 24 hours.
4. Example prompt: *"Use krypt-trader. Look through markets closing in the next 48h, read the rules,
   record honest forecasts for each, and only trade where your edge clears the minimum after fees."*

## 4. What to test

Starting ideas, ordered by how much evidence supports them:

| # | Hypothesis | Why it might work | How to test in-app |
|---|---|---|---|
| 1 | **Avoid longshots, lean toward favorites** | Academic studies of Kalshi data find that cheap contracts (under ~10–15¢) lose most of their stake on average, while expensive favorites lose much less or come out slightly ahead. This is the favorite-longshot bias. | A named agent capped to buys at ≥80¢. Track net ROI after fees. Note: fees round **up per order**, so 1-lot orders at 95¢ pay about 3× the fee rate. Use sizes of 10+ contracts. |
| 2 | **Post limit orders (maker) instead of crossing the spread (taker)** | The same studies find takers lose on average and makers do better. | Rest limit orders inside the spread. Paper fills resting orders conservatively (only when the real book crosses your price), so paper will understate this strategy. That's acceptable. |
| 3 | **AI forecasts on slow, rules-heavy markets** (weather, economic data, politics) | The model reads the settlement rules carefully, where many traders don't. | Use the **"Does the AI beat the market?"** scoreboard. It needs 30+ settled markets before it gives a verdict. |
| 4 | **15-minute crypto presets** (38 included: VWAP and momentum strategies) | Easy to backtest quickly. | Run them on collected data, then see the warning below. Heavy competition from bots. |

**Warning about running dozens of strategies.** If you backtest 38 presets, a few will look profitable by
pure luck. Any strategy that passes the backtest must **also** pass a fresh paper run on data it wasn't
tuned on before it counts.

## 5. Bar a strategy must clear to go live

Every item must be true:

- [ ] Positive **net** EV after Kalshi fees, using the same order size you'll trade live.
- [ ] **100+ trades** in total, or 30+ settled forecasts for AI agents, with t-stat ≥ 2. The backtester
      shows `t`.
- [ ] It worked in the backtest **and** in at least 2 weeks of later paper trading that wasn't used to
      tune it.
- [ ] Not driven by one or two lucky trades. Remove the top 3 winners and check it's still positive.
- [ ] Fills are realistic: you're not assuming fills at prices with almost no depth in the book.
- [ ] You can explain in one sentence *why* the edge exists.

## 6. Going live safely

1. Open a Kalshi account and fund it with a small amount you could lose completely, such as $100–$300.
2. **API Keys** page: add the key with the wizard. Then **Settings → Account → Go live** and work through
   the checklist.
3. Keep **approvals ON** for the first few weeks. Every order then waits for your OK, in the app or by
   phone (`approve N`).
4. Set tight rails: a small per-order cap, a daily cap, and a **daily loss stop** of about 5% of the
   bankroll.
5. Only one strategy goes live at a time. Keep everything else on paper and compare live results with
   paper results. If live does much worse than paper, stop and find out why.
6. Increase size only after about a month of live results that match paper.

---

## Log

| Date | Strategy / agent | Mode | Trades | Net P&L | t-stat | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |
