# Kalshi Short-Duration Crypto Markets & LLM Forecasting vs Prediction Markets (research as of 2026-10-08)

## A1. How Kalshi 15-min/hourly crypto markets work, settle, fees, liquidity

### Takeaway
KXBTC15M opens a new up/down contract every 15 minutes, 24/7. It settles on a 60-second average of the CF Benchmarks Real-Time Index (BRTI), taken once per second in the minute before close, compared against a reference value at the open. Taker fees follow Kalshi's standard 0.07·P·(1−P) formula, which is about 1.75¢ per contract at 50¢. I found no public liquidity or spread numbers.

### Cited Findings
- KXBTC15M: a new up/down pair at :00/:15/:30/:45, 24/7, paying $1 or $0. Settles on the CF Benchmarks Bitcoin Real-Time Index, sampled once per second over the final minute (a 60-sec average). The strike/reference "locks at the open". Every Kalshi BTC frequency (15-min, hourly, daily…) uses the same index; there is no separate 15-min index. Page updated 2026-09-25. — [PredictionMarketsPicks](https://predictionmarketspicks.com/articles/kalshi-bitcoin-15-minute-markets)
- The 15-min contract compares the final-minute BRTI average with the same average taken at the window's open. Crypto settles on CF Benchmarks RTIs; commodities use Pyth 1-minute candles. — [PredictionMarketsPicks: How Kalshi settles Bitcoin](https://predictionmarketspicks.com/articles/how-kalshi-settles-bitcoin); [How Kalshi 15-minute markets settle](https://predictionmarketspicks.com/articles/how-kalshi-15-minute-markets-settle)
- **Conflict:** an older guide (about March 2026) says 15-min markets use Kalshi-captured reference prices and hourly markets use BRRNY. Newer sources call BRRNY a once-daily fixing that is not used for intraday contracts. — [KalshiBacktest](https://kalshibacktest.com/resources/kalshi-settlement-mechanics); [KalshiBacktest settlement source](https://kalshibacktest.com/resources/what-is-kalshi-settlement-source). Treat the newer BRTI-average description as current, but check the contract's rulebook on kalshi.com.
- Independent check of settlement integrity: across 2,238 settles (Sep 9–27, 2026), a self-captured BRTI 60-sec average matched Kalshi's published settle to a median of $0.13. 98% were within $1 and only 1 of 2,238 disagreed. Of 3,320 15-min windows (Aug 24–Sep 27, 2026), 50.0% settled up. — [PredictionMarketsPicks: Is Kalshi Bitcoin rigged?](https://predictionmarketspicks.com/articles/is-kalshi-bitcoin-rigged)
- Closeness of finishes: 0.7% of 15-min windows were decided by under $1, 4.3% by under $5, 23% by under $25 and 41.4% by under $50. — [same](https://predictionmarketspicks.com/articles/is-kalshi-bitcoin-rigged)
- Standard Kalshi taker fee is 0.07 × contracts × P × (1−P), rounded up. That is 1.75¢ per contract at 50¢ (3.5% of cost) and 0.63¢ at 90¢. S&P/Nasdaq markets use a 0.035 multiplier. Maker fees are reported as 25% of taker in some markets and zero in others (conflicting). — [DeFi Rate fees](https://defirate.com/prediction-markets/fees/); [Whirligig Bear: Maker/Taker math on Kalshi](https://whirligigbear.substack.com/p/makertaker-math-on-kalshi)
- I found no source confirming whether the 15-min crypto series uses the 0.07 coefficient or a special schedule. One guide only says the same "quadratic fee" applies. — [PredictionMarketsPicks](https://predictionmarketspicks.com/articles/kalshi-bitcoin-15-minute-markets)
- Liquidity "thins overnight and on weekends". No volume or spread figures were published. — [PredictionMarketsPicks](https://predictionmarketspicks.com/articles/kalshi-bitcoin-15-minute-markets). A vendor blog calls hourly BTC/crypto contracts "the most active, fastest-cycling markets on the platform" (vendor claim). — [BotForKalshi](https://www.botforkalshi.com/blog/kalshi-trading-bots-complete-guide)

### Inferences
- Settlement is the average of the last 60 seconds, so the outcome is partly locked in during the final minute. A bot that tracks the running BRTI average (built from the constituent exchanges: Coinbase, Kraken, Bitstamp and others) can estimate the settle more precisely than the last spot tick. Fast participants already reprice quickly near close (see A2).
- Peak fee at 50¢ is about 3.5% of notional for takers. A taker needs an edge of more than about 2–4¢ on near-even contracts just to break even after fees and the spread.

### Gaps
- Official Kalshi contract terms and the fee schedule for KXBTC15M, KXETH15M and KXSOL15M were not fetched directly. I found no reliable numbers on order-book depth, spreads or daily volume.
- I did not confirm whether ETH/SOL 15-min and hourly range markets settle the same way (they likely use the CF ETH and SOL RTIs, but this is unverified).

## A2. Known edges (latency arb, fair-value mispricing, last-minute sweeps, momentum) and evidence on bots

### Takeaway
On Polymarket, fee-free 15-min crypto markets were heavily farmed by latency-arbitrage bots in late 2025. In early 2026 Polymarket added dynamic taker fees that peak near 50¢, and a reported 500ms delay was removed. Practitioners report that pure taker latency arb died and the edge moved to market-making. On Kalshi, a one-month calibration study of 15-min BTC found prices well calibrated in every band, including the last 3 minutes, with no exploitable edge.

### Cited Findings
- Polymarket introduced dynamic taker fees on short-term crypto markets specifically to curb latency arbitrage. Fees peak near 50% odds, where arb was concentrated, and fund daily maker rebates. — [Finance Magnates](https://www.financemagnates.com/cryptocurrency/polymarket-introduces-dynamic-fees-to-curb-latency-arbitrage-in-short-term-crypto-markets/); [Unchained](https://unchainedcrypto.com/polymarket-introduces-taker-fees-in-15-minute-markets/); [DeFi Rate](https://defirate.com/news/polymarket-users-approve-new-crypto-market-fees/)
- Polymarket's current docs give the formula fee = C × feeRate × p(1−p). For Crypto the taker feeRate is 0.07, the maker fee is 0 and the maker rebate is 20%. That works out to $1.75 per 100 shares at 50¢ (about 3.5% of notional). — [Polymarket docs](https://docs.polymarket.com/trading/fees). Earlier reported peak rates **conflict**: ~1.56% ([BlockBeats](https://m.theblockbeats.info/en/news/61326)), ~1.80% ([KuCoin](https://www.kucoin.com/blog/polymarket-fees-trading-guide-2026)), ~3.15% ([Finance Magnates](https://www.financemagnates.com/cryptocurrency/polymarket-introduces-dynamic-fees-to-curb-latency-arbitrage-in-short-term-crypto-markets/)). Fees likely changed over time and are stated on different bases.
- Polymarket reportedly removed a 500ms taker delay without notice (Feb 2026), which broke many bots. One developer says latency-arb strategies "stopped working the same day" (single-source accounts). — [BlockBeats](https://m.theblockbeats.info/en/news/61326); [DEV: February 2026 changed Polymarket](https://dev.to/lkto1m/february-2026-changed-polymarket-forever-heres-what-happened-to-my-bots-numbers-2fi5)
- Pre-fee claims: a bot builder said Polymarket 5-min BTC markets lagged Binance by 30–90 seconds (69.6% win rate on only 23 trades). — [chudi.dev](https://chudi.dev/blog/how-i-built-polymarket-trading-bot). There are unverified anecdotes of bots earning "$5–10k daily" and one turning "$313 into $414k in a month". — [KuCoin news](https://www.kucoin.com/news/insight/BTC/695f8764e781bf0007e01c10)
- Counter-anecdote: one retail bot made about $2 net after 176 trades over 8 days. Partial fills cost $41.50 in 15 minutes. — [DEV Community](https://dev.to/manja316/176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think-3iib)
- A secondary source cites IMDEA Networks research (86M trades): the median arb window shrank from 12.3s (early 2024) to ~2.7s (2026), and 73% of arb profits go to sub-100ms bots. It also cites an arXiv estimate of ~$40M in Polymarket arb profits from Apr 2024 to Apr 2025. I did not verify either primary source. — [Turbinefi](https://www.turbinefi.com/blog/prediction-market-arbitrage-latency-speed-2026); [Polymarket strategies guide](https://www.datawallet.com/crypto/top-polymarket-trading-strategies)
- Kalshi KXBTC15M calibration (2,764 windows, Aug 29–Sep 27, 2026, midpoints with the final minute excluded): every 10¢ band was within about 1 point of its price. Examples: 8.1¢ priced → 8.6% won; 46.2¢ → 45.8%; 91.9¢ → 91.4%. — [PredictionMarketsPicks](https://predictionmarketspicks.com/articles/is-kalshi-bitcoin-rigged)
- Late favorites (95–99¢): at ~3 min left, avg price 97.6¢ and 98.2% won; at ~90s, 97.8¢ and 97.8%; at ~45s, 97.7¢ and 98.9%. The authors conclude that favorites return about their price minus fees, that there is no edge, and that "automated traders reprice quickly near the close". — [same](https://predictionmarketspicks.com/articles/is-kalshi-bitcoin-rigged)
- Fair-value angle: no listed option expires in 15 minutes, so options-implied vol is unavailable. Candidate edges are short-window realized vol, order-flow imbalance and the "spread-plus-fee cost wall", which the author calls the main obstacle ("right on direction and still lose money"). The publisher's own live 15-min model "has not beaten the market's Brier score in any minute-remaining bucket". — [PredictionMarketsPicks](https://predictionmarketspicks.com/articles/kalshi-bitcoin-15-minute-markets)
- Kalshi-wide structural evidence: across 300k+ contracts there is a favorite-longshot bias. Contracts under 10¢ lose heavily, and expensive contracts sometimes earn small profits. Pre-fee, takers lose about 32% on average and makers about 10%. There is some evidence the bias is shrinking over time. — [Bürgi, Deng & Whelan, "Makers and Takers" (CESifo 2026)](https://www.ifo.de/en/cesifo/publications/2026/working-paper/makers-and-takers-economics-kalshi-prediction-market); [VoxEU summary](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market)

### Inferences
- Pure latency arb (taking stale quotes after a spot move) is the edge most clearly competed away. Polymarket designed its fee curve to kill it. On Kalshi, the September 2026 calibration data shows no residual mispricing at the 10¢-band level, even in the last minutes.
- What remains is mostly maker-side: quoting both sides around a BRTI/realized-vol fair value, collecting spread and rebates, and managing adverse selection. The favorite-longshot bias suggests systematically not buying cheap longshots, or selling them as a maker, is a small structural tilt. It is not a large edge after fees.

### Gaps
- I found no rigorous, primary study of Kalshi-specific crypto bot P&L. The ETH/SOL and price-range (bracket) markets were not studied. The calibration study used midpoints, not executable prices, and covers about one month.
- The IMDEA and arXiv arbitrage figures are unverified secondhand.

## A3. Competition level; can a home-internet retail bot compete?

### Takeaway
Short-duration crypto on Kalshi and Polymarket is a bot-dominated arena with institutional makers (Susquehanna is Kalshi's flagship MM) and co-located VPS operators. A home-internet taker bot cannot win latency races. Its only plausible niche is slower, model-driven maker quoting, which retail usually underperforms at.

### Cited Findings
- Susquehanna has been Kalshi's first market-maker partner since April 2024 and is believed to be the largest. A class action alleges its infrastructure gives "a systematic advantage over retail". Kalshi says institutional MMs are "not a large percent of volume" on most liquid markets and that ~95% of bid matches come from 2,000+ smaller makers. — [Finance Magnates](https://www.financemagnates.com/fintech/kalshi-says-its-edge-comes-from-retail-traders-but-the-picture-is-more-complex/); [American Prospect, 2026-08-26](https://prospect.org/2026/08/26/house-always-wins-kalshi-prediction-markets/)
- VPS vendors advertise ~1ms to Kalshi API from NY4. A competitor says the public endpoints sit behind CloudFront and reports ~10ms round trip from Chicago to the FIX engine (both are vendor claims). — [NYC Servers](https://newyorkcityservers.com/kalshi-vps); [TradoxVPS](https://tradoxvps.com/best-vps-for-kalshi-trading-bots/)
- Press: prediction markets are "turning into a bot playground", with bots exploiting latency and arb faster than humans can react. — [Finance Magnates via TradingView](https://www.tradingview.com/news/financemagnates:7f126ddf1094b:0-prediction-markets-are-turning-into-a-bot-playground/)
- Retail market-making underperforms mainly because of an "inability to refresh a defensible probability estimate at the speed the book requires". — [Turbinefi MM guide](https://www.turbinefi.com/blog/how-to-market-make-prediction-markets-2026)
- An open-source Kalshi BTC bot notes that Kalshi MMs lack spot-exchange-grade low-latency infrastructure, which suggests some lag versus spot exists (an unquantified claim). — [GitHub brandononchain/kalshibot](https://github.com/brandononchain/kalshibot)
- Polymarket concentration: 3.5% of wallets did 88% of volume in 2026 (aggregator). — [pm.wiki](https://pm.wiki/news/wire/agg_d954bfef76f68f9c)

### Inferences
- Home broadband adds roughly 20–100ms of jitter on top of an exchange that already has sub-10ms competitors. The fee curve also penalizes takers most at 50¢. Retail is therefore structurally the slow taker, the adversely selected flow that makers profit from.
- A realistic retail approach would be a modest, small-size maker or fair-value strategy on less-watched series (ETH/SOL, bracket strikes, off-hours), where competition may be thinner. This is untested and has no evidence of profitability.

### Gaps
- I found no hard data on the number of active bots, the market share of MMs in crypto series specifically, or measured quote-update latency on Kalshi crypto books.

## B1. LLM forecasting benchmarks vs markets and superforecasters (Brier scores)

### Takeaway
By mid-2026, frontier LLM systems have roughly caught up with superforecasters on ForecastBench. The FRI said on 2026-07-16 that they have "likely reached parity", and one system beat the superforecaster median on market questions. Against live Kalshi prices, raw frontier models are about equal on Brier (Prophet Arena: GPT-5 0.184 vs market 0.187, within confidence intervals) and better calibrated, but they do not beat the market on returns.

### Cited Findings
- ForecastBench (FRI), 2026-07-16: "Several models are statistically indistinguishable from superforecaster-level accuracy." The top tournament entry is Cassi AI (p=0.41 vs supers), followed by xAI entries (p=0.16, 0.15) and a Google DeepMind entry (p=0.14). On *market* questions, Cassi is the first model to rank above the superforecaster median. On dataset questions, 17 submissions rank above supers (Torchcast holds the top 3). Caveat: superforecasters were last surveyed in 2024, and tournament entries may use tools, fine-tuning or ensembles. — [FRI Substack](https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity); [ForecastBench leaderboards](https://www.forecastbench.org/leaderboards/)
- Earlier ForecastBench gap: superforecasters 0.081 vs GPT-4.5 0.101 Brier (Oct 2025). In January 2026 supers still led the best LLM by 0.017. FRI had extrapolated parity around late 2026 (CI Dec 2025–Jan 2028). — [FRI: LLMs closing the gap](https://forecastingresearch.substack.com/p/llms-are-closing-the-gap-on-human); [EA Forum summary](https://forum.effectivealtruism.org/posts/Spyz3wESZu2eeqhDj/ai-forecasting-in-2026-what-11-analyses-say)
- ForecastBench paper (v5, Feb 2025): on market questions, the best LLM scores (e.g. GPT-4o 0.069) came with the crowd/market forecast given as input. Without it, Claude-3.5-Sonnet's market Brier rose to 0.133. Much of the LLM "market" accuracy is therefore borrowed from the market itself. — [arXiv 2409.19839v5](https://arxiv.org/html/2409.19839v5)
- Prophet Arena (ICLR 2026; 1,367 Kalshi events resolved before Oct 11 2025, 76% sports). Brier: GPT-5 (reasoning) 0.184, Grok-4 0.189, Claude Sonnet 4 0.194, Gemini 2.5 Flash 0.197, Llama-4-Scout 0.219, **Kalshi market 0.187** (CI ±0.006). All top LLMs are better calibrated (ECE ~0.04 vs market 0.069). — [arXiv 2510.17638](https://arxiv.org/html/2510.17638v1)
- KalshiBench (Dec 2025, 300 Kalshi questions resolving after Oct 1 2025): all models were overconfident. Claude Opus 4.5 had the best ECE (0.120, 69.3% accuracy); others ranged 0.28–0.40. GPT-5.2-XHigh had ECE 0.395, so more reasoning did not improve calibration. Models were wrong 27% of the time when they claimed over 90% confidence. — [arXiv 2512.16030](https://arxiv.org/html/2512.16030v1)
- The live Prophet Arena leaderboard shows a "Kalshi Markets" baseline row (1−Brier ≈ 0.946) and model return columns. The search snippet listed Claude Opus 5.5 with a 120.89% return, but I could not verify the filter or window. — [Prophet Arena leaderboard](https://www.prophetarena.co/leaderboard/forecast)

### Inferences
- "Parity with superforecasters" is not the same as "beats the market". On the market-referenced subsets, LLMs are at best roughly tied with prices. Beating the market requires beating a price that already aggregates information and other bots, possibly including other LLMs.
- LLM overconfidence at extremes (KalshiBench) is dangerous for a bot that sizes bets on model confidence.

### Gaps
- The live ForecastBench and Prophet Arena tables are rendered as images or dynamically, so I could not extract current numeric Brier scores. No direct Metaculus AI Benchmark (Q2/Q3 2026) results were retrieved.

## B2. Evidence of LLM agents trading profitably on Kalshi/Polymarket

### Takeaway
Most rigorous evidence shows LLM agents losing money. Prophet Arena returns are below break-even, and in Prediction Arena six frontier models lost 16–31% on Kalshi with real capital over 57 days. Positive results come from one small live run ($200 → $361, a Gemini 3 agent with a proper-scoring-rule bet-sizing strategy, co-authored by Kalshi Research) and short paper-trading windows.

### Cited Findings
- Prophet Arena: under a risk-neutral strategy, average return per unit budget is GPT-5 0.943, Claude Sonnet 4 0.909, Gemini 2.5 Flash 0.883, Grok-4 0.864, market baseline 0.899. No model reaches break-even (1.0), and variance is high. — [arXiv 2510.17638](https://arxiv.org/html/2510.17638v1)
- Prediction Arena (arXiv 2604.07355, Cohort 1 live with $10k each on Kalshi, Jan 12–Mar 9 2026). Kalshi returns: glm-4.7 −16.0%, grok-4-20 −20.0%, gpt-5.2 −20.5%, claude-opus-4-5 −25.9%, gemini-3-pro −30.5%, grok-4-1-fast −30.8%; average −22.6%. On Polymarket (Feb 9–Mar 9) the average was −1.1%. Kalshi positions were 71–97% weather markets. Initial prediction accuracy was the best predictor of P&L, and research volume did not correlate with performance. Cohort 2 (3-day paper trading): gpt-5.4 +1.22% Kalshi; gemini-3.1-pro +6.02% Polymarket; claude-opus-4-6 −10.06% Polymarket. The authors call this too short to infer anything. — [arXiv 2604.07355](https://arxiv.org/html/2604.07355v1)
- "When do prophets profit in prediction markets?" (arXiv 2607.06166, Jul 2026). Expected profit = score gap + Bregman divergence − liquidity loss. Proper-scoring-rule ("Brier-weighted") bet sizing was the only strategy with reliably positive ROI for strong models. Claude Opus 4.6 made +22.1% on a 200-event Kalshi subset, while Kelly sizing lost 99.9% (backtest assumes zero price impact). Live: Gemini 3 agent, 26 trading days in Apr/May 2026 on a 2-hour cadence, $200 → $360.67 (+80.33%). It made 1,605 forecasts and 236 fills across 129 markets, paid $26.31 in fees, had a 50.9% win rate and a Sharpe of 3.35. One author is affiliated with Kalshi Research. — [arXiv 2607.06166](https://arxiv.org/html/2607.06166v1)
- Alpha Arena (Nof1) traded crypto perps and stocks, not prediction markets. Season 1 (Oct–Nov 2025, $10k each on Hyperliquid): Qwen3-Max +22%, DeepSeek +5%. Claude Sonnet 4.5, Gemini 2.5 Pro, Grok and GPT-5 lost 42–59%. Season 1.5 (stocks): Grok 4.20 was the only profitable model. — [ForkLog](https://forklog.com/en/four-out-of-six-ai-models-suffer-losses-in-trading-tournament/); [ForkLog S1.5](https://forklog.com/en/ai-model-grok-4-2-triumphs-in-trading-tournament/)

### Inferences
- The bet-sizing method matters as much as forecast accuracy. Naive Kelly on overconfident LLM probabilities blows up. Proper-scoring-rule sizing turned a modest accuracy edge into profit in the one live study.
- The evidence for a durable LLM trading edge is thin: one $200 live run over one month, plus backtests without market impact.

### Gaps
- I found no audited long-horizon (6+ months) live LLM-agent P&L on Kalshi or Polymarket. I found no 2026 Alpha Arena prediction-market season.

## B3. Where LLMs do relatively better vs worse

### Takeaway
LLMs do relatively better at long lead times, on calibration, and possibly on less-watched markets. Markets win near resolution and on breaking news. For short-horizon crypto price markets, LLMs offer essentially no advantage, because the problem is pure price dynamics and latency.

### Cited Findings
- Some LLMs beat the market baseline when forecasting far in advance. The market is stronger near resolution because it absorbs breaking news faster. Prophet Arena excludes forecasts within 3 hours of close because "retrieval, not reasoning" dominates there. LLMs are more hesitant than markets at extreme probabilities. — [arXiv 2510.17638](https://arxiv.org/html/2510.17638v1)
- Source and news context helps more in politics than in entertainment or sports. Recall is weakest for weather and politics. — [arXiv 2510.17638](https://arxiv.org/html/2510.17638v1)
- Weather-heavy Kalshi trading produced large LLM losses (Prediction Arena). Polymarket's open-ended market discovery gave much smaller losses. — [arXiv 2604.07355](https://arxiv.org/html/2604.07355v1)
- LLMs are overconfident above 90% confidence, wrong 27% of the time. — [arXiv 2512.16030](https://arxiv.org/html/2512.16030v1)
- Profit requires enough liquidity that slippage stays small, and can arise from divergence from the market even without an accuracy edge. — [arXiv 2607.06166](https://arxiv.org/html/2607.06166v1)
- Kalshi prices become more accurate closer to close, and the favorite-longshot bias (overpriced cheap contracts) persists but is shrinking. — [Bürgi/Deng/Whelan](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market)

### Inferences
- The most plausible LLM niche is long-dated, low-attention, text-heavy markets: rules and resolution-criteria nuance, niche politics and economics, long-tail events. Prices there are stale or longshot-biased and fast quant competition is thin. Liquidity limits position size, though. These are inferences; I found no source that directly measured an LLM edge on "rules-reading" markets.
- Combining the two topics, an LLM is the wrong tool for 15-min crypto. That is a quantitative microstructure problem (BRTI averaging, realized vol, order flow, latency), where LLM inference latency of seconds is disqualifying.

### Gaps
- I found no study isolating LLM performance by market liquidity or by resolution-rule complexity, and no data on LLMs in Kalshi's long-tail or mention markets.
