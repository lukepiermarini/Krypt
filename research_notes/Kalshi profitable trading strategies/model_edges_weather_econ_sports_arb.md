# Model- and Information-Driven Edges on Kalshi: Weather, Economic Data, Sports, Cross-Venue Arbitrage (as of Oct 2026)

Research note scope: whether an automated US retail trader using public forecasts or data can find positive expected value after fees in four Kalshi categories. Researched 2026-10-08. Several sources are vendors selling tools. They are flagged as such and are not treated as independent evidence.

Cross-cutting fact base (applies to all categories):
- Kalshi taker fee = roundup(0.07 x C x P x (1-P)). The maker formula uses 0.0175. That is about 1.75c per contract taker and about 0.44c maker at a 50c price, and fees are symmetric around 50c. Which series carry maker fees varies, and kalshi.com/fee-schedule is the authority. Secondary sources disagree on whether makers pay by default. S&P/Nasdaq markets reportedly use a 0.035 multiplier. — [Kalshi fee schedule PDF](https://kalshi.com/docs/kalshi-fee-schedule.pdf); [Kalshi help: fees](https://help.kalshi.com/en/articles/13823805-fees); [Whirligig Bear: Maker/Taker Math on Kalshi](https://whirligigbear.substack.com/p/makertaker-math-on-kalshi); [Oddpool fee explainer](https://www.oddpool.com/research/prediction-market-fees-explained)
- **The key academic baseline is Bürgi, Deng and Whelan, "Makers and Takers: The Economics of the Kalshi Prediction Market"** (UCD; CEPR DP20631 / CESifo WP 12122; Jan 2026 version). It uses transaction-level data on 313,972 Yes/No contracts (46,282 contracts with at least $1k volume) from 2021 to April 2025.
  - Prices are informative and become more accurate toward close, but there is a clear favorite–longshot bias. Contracts under 10c lose over 60% of money. Contracts above 50c earn small, statistically significant positive returns.
  - The average pre-fee return is about -20%. Takers lose about 32% on average and makers about 10%.
  - The bias is rejected as unbiased in every category: Financials, Climate & Weather, Crypto, Politics, Entertainment, Economics, Other. It is weakening in 2025 data. — [Whelan paper PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf); [CESifo listing](https://www.ifo.de/en/cesifo/publications/2025/working-paper/makers-and-takers-economics-kalshi-prediction-market); [CEPR DP20631](https://cepr.org/publications/dp20631)
- In the Whelan category regressions (Table 8, dependent variable pre-fee profit on price), the "Climate & Weather" price slope is the largest of all categories. It is 0.058 (n=8,150 taker contracts), against 0.034 overall, 0.034 Economics, and about 0.02 Politics/Entertainment. The favorite-longshot mispricing therefore looks strongest in weather. — [Whelan paper PDF, Table 8](https://www.karlwhelan.com/Papers/Kalshi.pdf)

## Weather markets (daily high/low temp per city, rain, etc.)

### Takeaway
Weather is the most plausible category for a small automated retail trader. Settlement is mechanical and public (the NWS Daily Climate Report for a named station). The relevant data (NBM/GFS/ECMWF ensembles, METAR/ASOS obs) is free. The best academic data show the strongest favorite–longshot bias in Climate & Weather. But every profit claim found is vendor or self-reported. Markets are thin, and the edge is mostly in getting settlement mechanics right (station, LST/DST window, rounding) and in maker-side or late-day observation trades, not in beating NWP models directionally.

### Cited Findings
- **Settlement:** Daily high/low markets settle on the *final* NWS Daily Climate Report (CLI) for the station listed in each market's rules, typically released the next morning. Consumer apps such as AccuWeather, iOS and Google do not count. — [Kalshi Help: Weather Markets](https://help.kalshi.com/en/articles/13823837-weather-markets)
- **DST trap:** NWS climate reports use local *standard* time. During DST the "day" runs 1:00 AM to 12:59 AM the next day, not midnight to midnight. — [Kalshi Help: Weather Markets](https://help.kalshi.com/en/articles/13823837-weather-markets)
- **Settlement delays:** Settlement can be delayed if the CLI high doesn't match the METAR 6-hr/24-hr max, or if the final CLI high is lower than the preliminary report. — [Kalshi Help: Weather Markets](https://help.kalshi.com/en/articles/13823837-weather-markets)
- **Hourly markets:** Hourly temperature markets (e.g. "Chicago temperature at 5 PM") settle on The Weather Company data at named station coordinates (e.g. KORD), about 25–35 minutes after close. Market structure for daily markets is ranges plus "or above/or below" tails. — [Kalshi Help: Weather Markets](https://help.kalshi.com/en/articles/13823837-weather-markets)
- **Station bias (vendor claim):** Forecasts for a city center can sit about 1°F off the settlement station, and integer-degree brackets make that decisive. One vendor claims the Miami NWS gridpoint runs about 3°F warm versus the airport station. These are unverified. — [Bot for Kalshi strategy guide](https://www.botforkalshi.com/blog/kalshi-weather-trading-strategy); [Bot for Kalshi weather edge tool](https://www.botforkalshi.com/tools/kalshi-weather-edge)
- **Naive model gaps are often illusory:** The same guide gives an NYC ">84°F" case where the model said ~98% and the market ~81%, and attributes it mostly to station/model issues. It advises requiring multi-model agreement and edge > fee + slippage + buffer ("a 3¢ apparent edge can disappear after fee and slippage"). — [Bot for Kalshi strategy guide](https://www.botforkalshi.com/blog/kalshi-weather-trading-strategy)
- **Forecast skill alone is not EV:** A practitioner skill guide warns that a model beating climatology by 0.05 Brier does not guarantee +EV at market prices because the market already incorporates NWP. It suggests the practical edge is maker-side fading of overpriced longshot brackets. — [claude-trading-skills: kalshi-weather-markets](https://claudeskills.info/ja/skills/agiprolabs/claude-trading-skills/kalshi-weather-markets/)
- **Late-day METAR "lock" (vendor claim):** After about 2 PM local, an airport METAR showing a reading already above a threshold (example: 82°F at 2:47 PM vs a ">80°F" contract at $0.72) lets you buy near-certain contracts before repricing. The vendor claims an ~88% win rate, unaudited. — [Kalshi Weather Edge](https://www.kalshiweatheredge.com/)
- **Data tooling:** Data tools expose settlement-station METAR/ASOS temperature, 3-hour trend, and distance-to-strike, plus settled-bracket history for backtesting. — [Apify Kalshi weather scraper](https://apify.com/lergassy/kalshi-weather-scraper); [Apify station nowcast](https://apify.com/nanare-sudo/kalshi-weather-markets); [minutetemp.com](https://minutetemp.com/)
- **Open-source bot:** suislanchez/polymarket-kalshi-weather-bot trades KXHIGH using a 31-member GFS ensemble from Open-Meteo, with Kelly sizing and calibration. Its README advertises "Highest profits $1.8k" (self-reported). — [GitHub](https://github.com/suislanchez/polymarket-kalshi-weather-bot)
- **Paid signals:** A paid daily weather-pick service claims a "67% verified" win rate at $25/month. This is marketing, and a win rate means little without prices. — [weatheredge.it.com](https://weatheredge.it.com/)
- **Polymarket profit claim (unverified):** A Polymarket trader "Hans323" reportedly made about $1.1M on London temperature contracts, attributed to speed in folding model updates into trades. Single promotional secondary source, not verified. — [PredictMarketCap: Weather Betting Boom](https://predictmarketcap.com/analysis/weather-betting-boom)
- **Manipulation allegation:** There is an allegation that a trader tampered with a Paris weather station (April 2026) and netted about $21k on Polymarket. It is unconfirmed, but it shows single-station settlement risk. — [PredictMarketCap](https://predictmarketcap.com/analysis/weather-betting-boom)
- **Volume:** Weather markets are clearing over $2M per day on Polymarket alone (secondary). Interactive Brokers' chairman said temperature contracts are its most frequently traded ForecastEx contracts. — [PredictMarketCap](https://predictmarketcap.com/analysis/weather-betting-boom); [Prediction News](https://predictionnews.com/story/kalshi-and-polymarket-weigh-climate-markets-as-next-growth-area)
- **Liquidity:** Weather markets are thinner than Kalshi's sports and crypto markets, so size is limited. — [Bot for Kalshi: can you bet on the weather](https://www.botforkalshi.com/blog/can-you-bet-on-the-weather)

### Inferences
- The realistic edges, in rough order of robustness:
  1. Settlement-mechanics correctness: the exact station, the LST window during DST, the CLI vs METAR rounding (METAR °C to °F conversion can differ from CLI), and avoiding settlement-delay edge cases.
  2. Late-day observation trades once the daily max is effectively locked (but the fee at high prices is small and competition from bots is high, so expect thin margins).
  3. Resting maker orders that sell overpriced longshot tail brackets, consistent with Whelan's finding that weather has the strongest longshot bias.
  4. Calibrated ensemble (NBM/GFS/ECMWF) bracket probabilities with station bias correction.
- Directional "my model vs market" trading at the open is the most crowded and least proven.
- Integer brackets plus 1–2°F station bias mean a beginner's naive app-based forecast is probably *negative* EV.

### Gaps
- No independent, audited P&L for any Kalshi weather bot was found. All profit and win-rate figures are vendor or self-reported.
- No Reddit r/Kalshi threads were surfaced by search. Practitioner community evidence is missing.
- No source gives concrete order-book depth or typical max fill size per city bracket.
- Rain/snow market settlement specifics were not checked.
- It was not verified whether weather series currently carry maker fees.

## Economic data markets (CPI, jobs, Fed decision, GDP)

### Takeaway
Kalshi econ markets are at least as accurate as, and for headline CPI significantly more accurate than, consensus. The best evidence is an independent Fed/NBER paper, so "trade the Cleveland Fed nowcast or consensus against Kalshi" is unlikely to be a systematic retail edge. The market already beats those inputs. The Fed decision market is especially efficient near meetings. Any remaining edge is likely the generic longshot bias and fast reaction to releases, which favors well-capitalized speed traders, not retail.

### Cited Findings
- **Fed/NBER paper:** Diercks, Katz and Wright, "Kalshi and the Rise of Macro Markets" (NBER WP 34702; Fed FEDS paper, Feb 2026) compare Kalshi-implied distributions against Bloomberg consensus, fed funds futures, SOFR options and the NY Fed Survey of Market Expectations. — [NBER w34702](https://www.nber.org/papers/w34702); [Federal Reserve FEDS page](https://federalreserve.gov/econres/feds/kalshi-and-the-rise-of-macro-markets.htm)
  - For headline CPI, Kalshi's median and mode give a statistically significant improvement over Bloomberg consensus. Core CPI and unemployment forecasts are statistically similar to the alternatives. — [Gambling Insider summary](https://www.gamblinginsider.com/news/113897/fed-study-kalshi-economic-forecasting); [Motley Fool](https://fool.com/investing/2026/03/16/federal-reserve-research-kalshi-prediction-markets)
  - Kalshi's modal forecast reportedly matched the fed funds outcome the day before every FOMC meeting since 2022, which futures and survey did not. This comes from a secondary summary and should be verified in the paper. At 150 days ahead, Kalshi MAE is very similar to professional forecasters. — [Slashdot](https://tech.slashdot.org/story/26/02/09/1957211/); [Yogonet](https://www.yogonet.com/international/news/2026/03/20/118189-federal-reserve-study-highlights-kalshi-as-emerging-tool-for-macroeconomic-forecasting)
  - Kalshi provides the only market-based distributions for GDP, core inflation, unemployment and payrolls. — [iGaming Business](https://igamingbusiness.com/finance/federal-reserve-prediction-markets-paper-warsh/)
- **Kalshi's own "Crisis Alpha" research (self-interested source):** For Feb 2023 to mid-2025, Kalshi CPI forecasts had 40.1% lower MAE than consensus, about 50% lower in shocks greater than 0.2pp at week-ahead, and markets were right in 75% of disagreements with consensus. Deviations of more than 0.1pp from consensus came with an ~81% shock rate (~82% a day before). The authors acknowledge a modest sample of large shocks. — [Kalshi Research: Crisis Alpha](https://kalshi.com/research/publications/crisis-alpha); [Casino.org](https://www.casino.org/news/want-an-accurate-inflation-forecast-kalshi-says-it-beats-wall-street/)
- **Economics category in Whelan:** Economics shows the longshot-bias slope (0.034) but an insignificant constant, n=24,405 taker contracts. — [Whelan paper PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)

### Inferences
- Because Kalshi beats consensus on headline CPI, a bot that buys whatever consensus or the Cleveland Fed nowcast implies would systematically trade *against* better-informed prices. The Kalshi-consensus gap is itself a signal about consensus error, not about Kalshi error.
- The FedWatch-vs-Kalshi Fed decision gap near meetings is likely near zero after fees. Any persistent difference is probably contract-definition or fee related, not mispricing.
- The plausible retail angle is limited to:
  1. Selling overpriced tail brackets (longshot bias).
  2. Monitoring multi-bracket sums for internal inconsistency.
- Neither of these is "information-driven."

### Gaps
- I did not access the NBER full text, so exact MAE numbers and the FOMC "every meeting" claim are from secondary summaries.
- No direct study of Kalshi vs Cleveland Fed nowcast, or Kalshi vs CME FedWatch trading P&L, was found.
- No data on jobs/GDP market depth or typical spreads.

## Sports (Kalshi vs sharp books, e.g. de-vigged Pinnacle)

### Takeaway
Sports is Kalshi's biggest category by far (about $144B in March 2026 volume per Blockworks/PANews), and its single-game prices are competitive with or tighter than US retail books. That means Kalshi is being priced off sharp lines by professional market makers. "Copy the de-vigged Pinnacle line" is the standard approach and is heavily competed. Small gaps rarely clear Kalshi's taker fee (up to 1.75c at 50c). No independent study shows systematic retail +EV.

### Cited Findings
- **Volume:** Kalshi sports volume reached about $144B in March 2026, up 80x from early 2025, and is about 68% of Kalshi volume. Kalshi holds about 70% of prediction-market sports volume. Basketball is 44%, football 28% and tennis 10% of sports volume. High fees and thin in-game liquidity are challenges for large traders. — [KuCoin/PANews summary of Blockworks](https://www.kucoin.com/news/flash/kalshi-s-sports-prediction-market-volume-surges-80x-in-one-year); [Blockworks Research](https://app.blockworksresearch.com/research/from-betting-to-trading-how-kalshi-is-reshaping-sports-markets)
- **NFL Week 1 2026 (Citizens JMP, 28 data points):** Kalshi blended implied vig was 4.32%, vs FanDuel 4.44% and DraftKings 4.51%. FanDuel was better on sampled moneylines, Kalshi better on totals, and the books were better on parlays. The sample is small. — [Prediction News](https://predictionnews.com/story/kalshi-vs-the-sportsbooks-nfl-game-prices-week-by-week); [1x2bettingpro](https://1x2bettingpro.com/index.php/2026/09/17/kalshi-fanduel-draftkings-nfl-week-1-pricing/)
- **Other vig comparisons (not rigorous):** One site sampled NBA playoffs and found Kalshi vig averaging 0.85% vs 4.62% at sportsbooks (methodology unclear, conflicts with Citizens). SmartStake reports Kalshi had the sharpest MLB player-prop prices, ahead of Pinnacle (vendor). — [SmartStake](https://www.smartstake.app/learn/kalshi-vs-sportsbook); [Dimers](https://www.dimers.com/industry/news/kalshi-record-nfl-week-1-2026)
- **200-game tracker (not peer reviewed):** A self-published comparison (NFL 70, NBA 80, MLB 50) of Kalshi vs consensus Vegas close in the same 15-minute window claims Kalshi moved faster and more precisely. — [PillarLab](https://pillarlabai.com/blog/kalshi-vs-vegas-odds-accuracy-200-games/)
- **Pinnacle as benchmark:** Pinnacle is the standard sharp benchmark for closing-line value. Vendors (SharpAPI etc.) sell Kalshi-vs-Pinnacle +EV feeds, which is evidence the strategy is commoditized. — [SharpAPI Kalshi odds API](https://sharpapi.io/sportsbooks/kalshi-odds-api); [TheStatsAPI Pinnacle](https://thestatsapi.com/odds-api/pinnacle)
- **Late-game longshot bias:** The Whelan literature review notes prior work finding that prices on trailing teams in the final 15 minutes of sports events were too high relative to win rates. — [Whelan paper PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- **Polymarket Arbitrage in NBA markets (Polymarket only, 75M+ LOB snapshots, 173 games):** finds "profound microstructural efficiency", i.e. arbs are rare or short-lived. — [arXiv 2605.00864](https://arxiv.org/html/2605.00864v1)

### Inferences
- Kalshi sports prices appear to be anchored to sharp books by professional market makers. A retail bot copying de-vigged Pinnacle will mostly find gaps of about 1–2c, which taker fees erase. It would also compete on latency with firms that have better feeds.
- Possible residual edges:
  1. Stale Kalshi quotes right after sharp-book line moves (latency game).
  2. Resting maker orders at fair value minus a margin (lower fee, earns the spread).
  3. Niche or low-liquidity props and less-covered sports where Kalshi market makers are thin.
- In-game live trading has thin liquidity, and the information lag vs TV/data feeds is a risk to the retail side.

### Gaps
- No rigorous, season-long study of Kalshi vs de-vigged Pinnacle closing lines (CLV) was found.
- The full Blockworks pricing-accuracy figure (0.54% average difference) could not be read in context; the page returned 404.
- No data on Kalshi sports position limits or typical fill sizes for retail.

## Cross-venue arbitrage (Kalshi vs Polymarket, PredictIt, sportsbooks)

### Takeaway
Academic evidence shows that cross-platform price gaps are real and persistent: 2–4% execution-aware on average, and only about 6% of events are cross-listed (Gebele & Matthes 2026). But they persist *because* they are hard to arbitrage. Resolution-rule mismatches turn arbs into directional pair trades. Capital stays locked until resolution on two separately funded venues. Fees eat 1–3c gaps. For a small-bankroll beginner, true risk-free arbs are rare. The reported high APYs come mostly from short time-to-resolution, not big mispricings.

### Cited Findings
- **Gebele & Matthes (TUM), "Semantic Non-Fungibility and Violations of the Law of One Price in Prediction Markets"** (arXiv 2601.01706). — [arXiv 2601.01706](https://arxiv.org/pdf/2601.01706)
  - The dataset is human-validated and covers over 100,000 events across 10 venues, 2018–2025.
  - About 6% of events are concurrently listed across platforms, representing about 10% of event-days.
  - Semantically equivalent markets show persistent execution-aware deviations of 2–4% on average, driven by structural frictions, not information.
  - Many pairs have a risk-free, execution-aware arb nearly the whole overlap period. Others are near zero because fees absorb the gaps.
  - High APYs are driven mainly by short horizons to resolution rather than substantial mispricing.
  - A naive mechanical strategy (always hold the single highest-yield arb to resolution) returned 1,218.66% over 800 days, but across only 15 completed trades. This is a backtest, not live, and it implies low capacity and frequency.
  - 2024 US election case: execution-adjusted spreads averaged about $0.03, up to $0.07, before the election-night call.
  - The authors conclude that divergence reflects constrained arbitrage capacity: offsetting positions held until resolution are capital-intensive.
- **Gebele, Mutzel & Matthes, "Executable Arbitrage and Market Efficiency in Prediction Markets"** (arXiv 2608.00666, Aug 2026). This is Polymarket only, not cross-venue. — [arXiv 2608.00666](https://arxiv.org/html/2608.00666v1)
  - About 1.12M USDC of realized intra-Polymarket arb profit after taker fees, mostly via the NegRisk converter.
  - The median exact-duration CLOB violation lasts about 16 seconds, meaning bots dominate.
  - The paper notes Kalshi's collateral-return mechanism reduces capital lockup for eligible portfolios.
- **Resolution mismatch examples:** A Kalshi Fed-cut contract requires a cut of 25bp or more at a scheduled meeting, while a Polymarket version resolved on any cut. A 12.5bp emergency cut would win one leg and lose the other. Crypto example: Polymarket settling on CoinGecko at 23:59 UTC vs Kalshi on CME/CF reference prices. — [pm.wiki: arbitrage after fees](https://pm.wiki/es/learn/prediction-market-arbitrage-after-fees); [NexusFi](https://nexusfi.com/a/prediction-markets/arbitrage-prediction-markets); [newyorkcityservers guide](https://newyorkcityservers.com/blog/prediction-market-arbitrage-guide)
- **Fees vs screenshot arbs:** Practitioner guides say 1–2c "screenshot" arbs at mid prices are reliably eaten by Kalshi's fee plus Polymarket category fees, and one example has a 3c gap consumed by about 2.2c of fees. These are secondary and unverified against official schedules. — [pm.wiki](https://pm.wiki/es/learn/prediction-market-arbitrage-after-fees); [newyorkcityservers guide](https://newyorkcityservers.com/blog/prediction-market-arbitrage-guide)
- **US access to Polymarket:** Polymarket re-entered the US via its QCX acquisition (CFTC amended order, Nov 25, 2025). The US app rolled out from December 2025, starting with sports, through FCMs. As of April 2026 the main global platform was still not open to US users, and the US app has thinner market selection than Kalshi. — [The Block](https://www.theblock.co/amp/post/381253/polymarket-begins-opening-us-app-to-users-on-waitlist); [Cointelegraph](https://cointelegraph.com/news/polymarket-cftc-approval-main-platform-us-report); [InGame review](https://www.ingame.com/polymarket-review/)
- **Polymarket US fees:** Polymarket US launched with 10bp taker and zero maker fees. A later review says that from April 3, 2026 it moved to a parabolic fee with a 5% coefficient and maker rebates (unconfirmed against the official page). — [Bitcoin Magazine](https://bitcoinmagazine.com/markets/polymarket-rolls-out-us-app); [InGame review](https://www.ingame.com/polymarket-review/)
- **Price discovery (secondhand, unverified):** Price discovery reportedly led on Polymarket during 2024, with Kalshi lagging by minutes. This is attributed to an SSRN paper. — [newyorkcityservers guide](https://newyorkcityservers.com/blog/prediction-market-arbitrage-guide)
- **Tooling exists:** Open-source and commercial arb scanners exist, e.g. lslb05/prediction-markets-arb with semantic matching and spread logging, and an Apify Polymarket+Kalshi arb finder. This indicates competition. — [GitHub lslb05](https://github.com/lslb05/prediction-markets-arb); [Apify arb finder](https://apify.com/congism/polymarket-kalshi-arb-finder?fpr=p2hrc6)

### Inferences
- Cross-venue arbs that survive fees exist mostly in long-dated or structurally segmented markets. There, return per year is low unless resolution is near, and capital is split and locked across two venues.
- For a small bankroll, the absolute dollar profit is small and rule-mismatch tail risk dominates. Each pair must be read rule by rule: source, timing, edge cases, cancellation/void rules.
- Kalshi vs sportsbook "arbs" add sportsbook limiting and account-restriction risk. Sportsbooks limit winning bettors, while Kalshi as an exchange does not. Gaps are mostly 1–3c.
- PredictIt was not researched in detail here. Its fees (historically 10% of profits plus 5% withdrawal) would make most arbs uneconomic.

### Gaps
- No 2025–2026 dataset was found that gives the frequency and size of Kalshi–Polymarket US arbs specifically after both venues' current fees.
- The Clinton & Huang (2025) and SSRN "Price Discovery and Trading in Prediction Markets" claims are secondhand and unverified.
- PredictIt's current status and fees were not checked.
- No primary-source practitioner P&L reports were found; no r/Kalshi threads surfaced.

## Which is most practical for a beginner with a small bankroll?

### Takeaway
Weather is the most practical starting point. Its settlement is transparent, data is free and well-documented, the markets are less dominated by institutional market makers than sports, and academic data show the strongest exploitable longshot bias there. Small size is fine given thin books. Econ markets are already more accurate than consensus. Sports is efficiently priced and fee-heavy relative to typical gaps. Cross-venue arb is capital-intensive with rule-mismatch risk. The universal structural edges are to post maker (limit) orders rather than take, and to avoid buying cheap longshots.

### Cited Findings
- Takers average about -32% and makers about -10%. Contracts under 10c lose over 60%, and contracts over 50c earn small positive returns. — [Whelan paper PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Climate & Weather has the steepest favorite–longshot slope among categories. — [Whelan paper PDF, Table 8](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Maker fee is about 1/4 of the taker fee (0.0175 vs 0.07 coefficient) where it applies. — [Kalshi fee schedule PDF](https://kalshi.com/docs/kalshi-fee-schedule.pdf)
- Econ markets beat consensus on headline CPI. — [NBER w34702](https://www.nber.org/papers/w34702)
- Cross-venue gaps of 2–4% persist due to capital and enforceability constraints. — [arXiv 2601.01706](https://arxiv.org/pdf/2601.01706)

### Inferences
- A suggested beginner path:
  1. Paper-trade or backtest weather brackets using settled-market data and the exact CLI station.
  2. Build station-bias-corrected ensemble probabilities (NBM/GFS/ECMWF via Open-Meteo or NOAA).
  3. Trade only as a maker, and mostly on the "sell overpriced tails / buy underpriced favorites" side.
  4. Add a late-day METAR monitor.
  5. Size small, using fractional Kelly.
- Even then, the expected edge is a few cents per contract on small volume. Expect modest dollar returns and meaningful variance, and evaluate against the -20% average baseline that most participants realize.
- The longshot bias is weakening (smaller 2025 coefficient), so edges likely shrink as bots proliferate.

### Gaps
- No independent evidence quantifies realized retail bot returns in any category.
- Recommendations above are inferences from structural evidence, not demonstrated P&L.
