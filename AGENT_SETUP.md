# Agent setup: Weather Favorites (strategy #1)

This sets up the first strategy from `reports/Kalshi profitable trading strategies.md`: buy the
**favorite** in Kalshi's daily city-temperature markets, never the longshots, in a category where
makers pay no fee.

## How the pieces fit

| Question | Where it gets answered |
|---|---|
| Have weather favorites historically won more often than their price says? | `tools/weather_favorites_backtest.py`, run against Kalshi's real settled markets. Results are in `results/weather_favorites_backtest.md`. |
| Does it still work right now, on live books, after fees? | The **Weather Favorites** agent below, trading on **paper** in Krypt Trader. |
| Does a resting limit order (maker) do better than buying at the ask (taker)? | The backtest's maker rows. Krypt's agent paper orders are *immediate-or-cancel* (see `python/mcp_server.py`, `place_order`), so agents can't paper-test resting orders. Only the backtest can. |

## 1. Create the agent in Krypt Trader

Go to **AI Agents → New agent** and enter these values.

| Field | Value |
|---|---|
| Name | `Weather Favorites` |
| Emoji / colour | 🌡️ / any |
| Mode | **Paper** |
| Categories (allow) | **Climate** only |
| Min price (¢) | `72` |
| Max price (¢) | `92` |
| Min hours to close | `2` |
| Max hours to close | `36` |
| Sides | Both |
| Max contracts per market | `20` |
| Max open positions | `8` |
| Min edge (¢) | `2` |
| Max order ($) | `20` |
| Daily spend ($) | `150` |

Under **Settings → Account**, set the paper bankroll to the amount you'd really use, for example **$500**.
Leave approvals on. Leave the research-data, scripts and strategy-settings switches off. This agent
doesn't need them.

## 2. Paste this into the agent's Guide box

```
You trade ONE strategy: favorites in Kalshi daily city-temperature markets
(high/low temperature brackets for a single city and date). Nothing else.

Each run:
1. discover_markets / search_markets for daily high or low temperature markets
   closing in 2-36 hours. Skip rain, snow, hurricanes, global/monthly series.
2. For each city-day event, get_market on its brackets and READ rules_primary:
   note the exact station and settlement source (most now settle on The
   Weather Company for a named station; a few on the NWS climate report).
3. Form your own probability for the leading bracket (or for NO on a bracket
   that looks unlikely) from the latest forecast for THAT station: NWS point
   forecast / NBM, plus today's observed high so far if it is the same day.
   Think in degrees, not vibes: forecast high, typical error (~2-3F a day
   out, ~1-2F same day), and where the bracket edges sit.
4. Only consider contracts whose ask is 72-92 cents. Never buy anything
   under 20 cents. One position per city per day.
5. record_forecast with your probability and a one-line reason (forecast
   value + station). Be honest: if your number is not at least 2 points
   above the price after fees, record it anyway and do NOT trade.
6. If it clears: preview_order, then place_order for 10-20 contracts at the
   current ask (never chase above 92c). Hold to settlement; don't sell early.
7. Skip a city if the forecast is unstable (models disagree by >4F), a
   front is arriving, or the bracket edge is within 1F of the forecast.

You are not trying to be clever. The edge being tested is that favorites
in these markets win a little more often than their price, and that
longshots lose a lot. Your job is to avoid the favorites the forecast
clearly says are wrong and to keep sizes small and consistent.
```

## 3. Connect Claude Code

**AI Agents → Weather Favorites → Copy config**, then paste it into Claude Code's MCP config. Run the
agent once or twice a day, for example around 10am and 4pm ET, with:

> Use krypt-trader as the Weather Favorites agent. Follow your guide for today's and tomorrow's
> temperature markets.

## 4. What to watch, and when to stop

- **Scoreboard:** the "Does the AI beat the market?" panel for this agent.
- **Weekly:** export the agent's trades, add a row to the Log in `PLAYBOOK.md`, and rerun the backtest
  (`python3 tools/weather_favorites_backtest.py`) to add the newest settled days.
- **Kill it** if after about 150 paper trades the net return per $ is negative and the backtest has
  turned negative too.
- **Go-live gate:** both the backtest and the paper results are positive after fees, the paper run
  has 300+ trades, and nothing in the result depends on a handful of days. Even then, start live at
  10 contracts with approvals on.
