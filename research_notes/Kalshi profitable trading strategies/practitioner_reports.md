# Practitioner Experience Trading Kalshi with Bots/Systematic Strategies + Practical/Legal Notes for a US Beginner (as of Oct 2026)

Research notes compiled 2026-10-08. Note on evidence quality: almost all "strategy P&L" claims online come from self-published blogs, vendor sites (TurbineFi, Bot for Kalshi, KalshiSpy, LaikaLabs), or SEO pages. The only rigorous data comes from academic work on Kalshi trade data (Bürgi, Deng & Whelan, UCD/GWU) and company-provided stats. Two promising first-person Medium posts ("I Spent Six Months Trading on Kalshi", "I Automated 4,000 Trades on Kalshi") returned HTTP 403 and could not be read in full. Reddit threads could not be retrieved directly.

## 1. Which strategies do practitioners report making money with (2024–2026)?

### Takeaway
The best evidence says the edge sits with makers (liquidity providers) and with people who have real informational or modeling edges in narrow niches (weather, data-driven categories like Spotify charts, deep research). Taking liquidity across the spread loses on average. Backtest "winners" in Kalshi's 15-minute BTC markets mostly vanished once fees, liquidity limits, and realistic fills were modeled, or once the test window moved forward a few days. Buying high-probability favorites does better than buying longshots on average, but it carries rule-driven and tail risk.

### Cited Findings
**Academic/trade-data evidence (strongest):**
- Bürgi, Deng & Whelan, "Makers and Takers: The Economics of the Kalshi Prediction Market": over 300,000 contract prices (both sides) from 12,403 events, each open at least 24h. Average return on Kalshi contracts is about −20%. One version says this is before fees. — [UCD WP2025_19](https://www.ucd.ie/economics/t4media/WP2025_19.pdf); [GWU 2026-001](https://www2.gwu.edu/~forcpgm/2026-001.pdf); [karlwhelan.com](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Favorite-longshot bias: buyers of contracts under 10c lose over 60% of their money, while contracts above 50c show a small positive return. — [GWU working paper](https://www2.gwu.edu/~forcpgm/2026-001.pdf); [VoxEU/CEPR summary](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market)
- Takers lose about 32% on average (−31.46%), makers about 10% (−9.64%). Makers buying at 50c+ earned about +2.6%. The sample ends April 2025, when Kalshi began charging maker fees. — [VoxEU](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market); figures as summarized by [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)
- A Stanford Law study (as summarized by a secondary source) reported measurable adverse selection in single-name contracts: informed traders pick off stale quotes before they update. — cited via [TurbineFi "Why you're losing money to bots and insiders"](https://www.turbinefi.com/blog/why-prediction-market-trades-get-picked-off-2026) (secondary; original not reviewed)
- Prophet Arena (1,367 Kalshi events): the best AI model's Brier score (0.184) roughly matched the market's (0.187), and its best average return was 0.943 per $1 against a 1.0 breakeven. So LLM forecasting did not beat the market. — [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)

**Systematic backtests (vendor, hypothetical):**
- TurbineFi, Kalshi 15-min BTC series (KXBTC15M), 30-day windows. Run 1 (Apr 20, 2026; no fees, no liquidity cap, same-candle fills): 695 of 1,000 strategies profitable, median ROI +1.37%. Run 2 (Apr 29, 2026; per-contract fees, order-book liquidity limits, next-candle-open fills): 102 of 4,904 profitable (2.1%), median −14.53%. — [TurbineFi, Sep 21 2026](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)
- Same source: the top archetype from run 1 ("buy YES at 50c, sell at 70c", +56.6%) had 7 of 4,290 variants profitable nine days later, with mean −19.95% and worst −77.73%. This is a textbook case of a regime change or overfit. — [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)
- Same source: "panic-fade" (fading sharp moves) had 93 of 96 variants profitable, best +18.32%. Mean-reversion had 0 of 432 profitable. The 10 worst strategies each made 7,000+ trades with 62–63% win rates yet lost 75–78%. — [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)
- Weather backtest (NYC high temp): 70 of 500 strategies profitable (14%), median −41.61%, best +117.75%. Caveat: it used LaGuardia observations, but the contract settles on Central Park, so it is directional only. — [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)

**Practitioner/anecdotal:**
- A Medium author who automated about 4,000 Kalshi trades reported a single 9,100% winner ("that one was luck") and a bad day caused by a bug. They warned: "don't walk in thinking you'll find easy mispricings everywhere… you're competing with other bots, and the profitable ones are fast." No overall P&L was visible in the snippet. — [oneforest, Medium](https://oneforest.medium.com/i-automated-4-000-trades-on-kalshi-heres-the-results-2f686c214e25) (full text blocked, 403)
- Named profitable traders (self-reported or press): Clay Alter, reported $1.5M+ profit in 8 months as a highly active manual trader (May 2026 podcast). Gaëtan Dugas, self-identified Top-100 trader, finds mispricings in data-driven categories like Spotify charts. — [LaikaLabs top traders roundup](https://laikalabs.ai/prediction-markets/top-kalshi-traders) (commercial aggregator)
- Hunter Foschini (MarketWatch): uses "deep research" plus his own models and algorithmic strategies, says he is profitable overall, figures not disclosed. — [MarketWatch via iTiger](https://www.itiger.com/hant/news/2537923561)
- An X post listing "top Kalshi traders" (e.g., @Domahhhh "$980K profit", @GaetenD "$420K", @Foster "best mentions trader", @theduckguesses "$100 to $145K"). These are unverified self-reported or leaderboard claims. — [X @aulijk](https://x.com/aulijk/status/1977453499131797531)
- Kalshi liquidity incentive programs have been described as enabling small "garage-band" market makers. — [fiftycentdollars Substack](https://fiftycentdollars.substack.com/p/kalshis-new-liquidity-incentives)
- Favorites near expiry: a Medium guide argues buying heavy favorites near resolution "can be a low-drama, consistent-return strategy," paired with selling overpriced longshots. This is opinion, not a verified result. — [Coinmonks Medium](https://medium.com/coinmonks/i-spent-six-months-trading-on-kalshi-heres-what-actually-works-c5fd9b7d6fe2) (as quoted in search results; full page 403)
- Copy trading: Kalshi accounts are private and have no built-in copy feature. Third-party trackers like KalshiSpy rank traders by realized profit, but sourcing is "proprietary and intentionally undisclosed." By the time you see a trade, price has often moved, especially in thin markets. — [KalshiSpy FAQ](https://kalshispy.com/faq); [KalshiSpy](https://kalshispy.com/)
- One GitHub research gist claims 30–50% annual returns from single-whale copy trading, with no source. Treat as unsupported. — [gist 2080ufo](https://gist.github.com/2080ufo/b3ab50a1ad8e465da923a091329242b6)
- Mention markets: niche specialists exist (e.g., "@Foster best mentions trader" above), but I found no systematic P&L data. The main documented lesson is resolution risk (see Section 3).

### Inferences
- Since takers lose about 32% on average and makers about 10% (with makers at 50c+ slightly positive before the April 2025 maker-fee change), a beginner's bot that crosses the spread is structurally disadvantaged. Passive limit-order or market-making approaches, or genuine model edges (weather ensembles, data categories), are the plausible paths.
- "Buy favorites" is supported directionally by the favorite-longshot data (50c+ slightly positive), but the edge is small. One loss at 95c erases about 19 wins, and rules or sourcing quirks add hidden tail risk.
- No source gives long-run, audited P&L for any retail systematic strategy. Edges reported in backtests decayed within days in the one documented test.

### Gaps
- No verified Reddit (r/Kalshi, r/algotrading) threads were retrievable. The two first-person Medium posts were blocked (403), so their overall P&L is unknown.
- No data on closing-time sweeps, news-speed trading, or momentum on Kalshi specifically, beyond the TurbineFi BTC backtests.
- No independent data on how long any reported edge lasted.

## 2. Public analyses of what share of Kalshi traders profit

### Takeaway
Kalshi's own one-month snapshot puts roughly 26–33% of users in profit. Critics argue that single-month figures overstate skill, and informal expert estimates of long-run profitability are 1–10%, mostly 2–5%. Aggregate retail losses are estimated above $500M since launch.

### Cited Findings
- WSJ (May 2026, Kalshi data): 2.9 unprofitable users for every profitable one in the most recent month, which works out to about 26% profitable. — [How Gambling Works Substack, Oct 6 2026](https://howgamblingworks.substack.com/p/are-30-of-kalshi-users-really-profitable)
- Kalshi COO Luana Lopes Lara: about 70% of users lose. CEO Tarek Mansour: "⅔ of people on Kalshi lose money." Kalshi's rebuttal to Roosevelt cites a "one to three ratio" of net profitable users. The author believes all of these come from the same one-month dataset. — [How Gambling Works](https://howgamblingworks.substack.com/p/are-30-of-kalshi-users-really-profitable)
- Critique: a simulated roulette bettor ($100 on red daily for 31 days) has a 44% chance of a profitable month despite negative expected value. Informal poll of more than a dozen traders, employees, and analysts: long-run profitable share of 1–10%, mostly 2–5%, and none above 1% for "regular users." Buying fair 50/50 contracts yields about −3.4% after taker fees, versus −2.7% for single-zero roulette. The author is a professional gambler and a prediction-market critic. — [How Gambling Works](https://howgamblingworks.substack.com/p/are-30-of-kalshi-users-really-profitable)
- Roosevelt Institute: ordinary users lost more than $500M from July 2021 to May 2026, based on public Kalshi data (advocacy group; critic says it excluded fees, which understates losses). — [Roosevelt Institute](https://rooseveltinstitute.org/blog/since-kalshis-launch-ordinary-users-have-lost-half-a-billion-dollars/)
- A claim that "New Yorkers were up $200M" likely includes NY-based market makers, which distorts the retail picture. — [TradeInformer](https://tradeinformer.com/broker-news/3-ways-kalshis-ceo-lied-about-new-yorkers-making-200m)
- Polymarket comparison (CEPR, Akey et al.): 588M trades and $67B in volume, with the top 1% of profitable users capturing 76.5% of profits. — via [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)

### Inferences
- A beginner should assume a base rate of long-run profitability in the low single digits, with profits concentrated among a few market makers and specialists.

### Gaps
- Kalshi has not published multi-month or lifetime cohort profitability. No public Kalshi leaderboard analysis with methodology was found.

## 3. Common failure modes

### Takeaway
Documented failure modes include: fees turning gross edges negative, overfitting and regime decay in backtests, rule and settlement-source quirks causing 90c "locks" to resolve No, outages where retail is locked out while API traders keep trading, and adverse selection against slow quotes.

### Cited Findings
- Fees: the taker fee is 0.07 × P × (1−P) per contract, rounded up to the cent (1.75c at 50c). It was applied to takers in the 2021–Apr 2025 sample, and makers began paying fees in April 2025. — [TurbineFi citing UCD](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)
- Cost modeling moved backtest results from 69.5% to 2.1% of strategies profitable. The author calls the gap an upper bound, because the window and strategy mix also changed. — [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)
- Overfitting: Bailey et al. (2014) show that testing only 10 configurations can yield an in-sample Sharpe of 1.57 when the true Sharpe is 0. — [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)
- Resolution risk example: the Bernie Sanders Greensboro rally mention market (Feb 12, 2026) had "Trump" Yes trading near 90c and more than $3M on the board. Every strike settled No because the event was closed to press, no approved broadcast existed, and attendee phone footage didn't qualify. The full rules required a live broadcast and press access, which the one-line summary omitted. — [OddsShopper](https://www.oddsshopper.com/articles/prediction-markets/kalshi-rules-summary-vs-full-rules)
- Kalshi's rulebook gives Kalshi "sole discretion to interpret a Contract's Terms and Conditions." Under Rule 7.1, an Outcome Review Committee's determinations are final. — [OddsShopper](https://www.oddsshopper.com/articles/prediction-markets/kalshi-rules-summary-vs-full-rules)
- Settlement is normally about 3 hours after the outcome, and can take up to 1–2 days if an official source must be checked. — [tech-insider](https://tech-insider.org/prediction-markets/how-does-kalshi-payout-work/) (secondary)
- Outages: in Oct 2025 (college football), glitches affected "less than half" of users per Kalshi. The API kept working, so API traders filled retail resting orders, and Kalshi later refunded affected users. — [Covers](https://www.covers.com/industry/kalshi-users-face-widespread-glitches-during-college-football-trading-oct-20-2025)
- In Dec 2025 (NFL), users could not access portfolios or close positions, and balances showed $0. — [PiunikaWeb](https://piunikaweb.com/2025/12/29/kalshi-outage-blocks-users-from-closing-positions/)
- At the Super Bowl (Feb 2026), deposits were delayed, described as the third high-volume degradation in about five months. — [DeFiRate](https://defirate.com/?p=5044)
- Kalshi also went down as the Pope was announced (May 2025). — [Closing Line Substack](https://closingline.substack.com/p/the-takeaway-kalshi-goes-down-pope-betting-markets)
- High win rate does not mean profit: strategies winning 62–63% of 7,000+ trades still lost 75–78%. — [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)
- Settlement-source mismatch in modeling (LaGuardia vs Central Park for NYC temperature) is a common bot bug. — [TurbineFi](https://www.turbinefi.com/blog/do-automated-trading-bots-make-money-prediction-markets-2026)
- An LLM-bot author's caveat: "AI ensemble can be 80% confident and still be wrong; no edge on economic releases." — [Bot for Kalshi ecosystem review](https://www.botforkalshi.com/blog/open-source-kalshi-bot-ecosystem)

### Inferences
- A 95c+ "near-certain" strategy is most exposed to exactly the Greensboro-type failure: a technicality in the settlement source, not the real-world outcome. Bots must parse the full contract terms, not the summary.
- Outages appear to cluster at peak-volume events, and API access sometimes survives when the app fails. That is an advantage for bots, but also a risk if a bot assumes stable fills.

### Gaps
- No public, quantified record of how often Kalshi markets resolve against the "obvious" outcome. No documented 2026 API-specific outage postmortems.

## 4. Practical: account, state restrictions, taxes, funding, API/demo

### Takeaway
You must be 18+ with KYC. Sports contracts face a live circuit split heading to the Supreme Court (cert petition No. 26-299 pending, with 39 states plus DC backing review). Kalshi provides 1099s only for certain items (interest, rewards, crypto), so trading P&L generally comes from Kalshi's PnL statement, and tax treatment is unsettled. API keys are RSA key pairs signed with RSA-PSS, and a separate demo environment exists but has thin books.

### Cited Findings
**Account/funding:**
- Minimum age is 18 nationwide under CFTC regulation, with KYC and government ID required. — [next.io](https://next.io/prediction-markets/kalshi/age/)
- Deposits: ACH ($10 min, no fee) and debit card (2% fee, per an affiliate page), plus wire. Withdrawals: free ACH (about 1–3 business days) or a $5 wire, paid only to a verified bank account in your name, and the first withdrawal may trigger a compliance review. Figures come from third parties and may be outdated. — [SailGP deposit page](https://sailgp.com/prediction-markets/kalshi/deposit-bonus); [Bot for Kalshi deposit guide](https://www.botforkalshi.com/blog/kalshi-deposit-withdrawal-guide)

**State/legal status (sports contracts):**
- Third Circuit (KalshiEX v. Flaherty, Apr 2026, 2–1) affirmed a preliminary injunction barring New Jersey from enforcing gambling law against Kalshi, finding CFTC jurisdiction likely exclusive. — [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/04/federal-appeals-court-cftc-jurisdiction-over-sports-event-contracts); [Skadden](https://www.skadden.com/insights/publications/2026/04/third-circuit-affirms-kalshis-preliminary-injunction)
- Sixth Circuit (Ohio/Tennessee, late Sep 2026): held the sports contracts are not swaps and that the CEA does not preempt state gambling law. — [CoinDesk Sep 25 2026](https://www.coindesk.com/policy/2026/09/25/another-appeals-court-rules-against-prediction-market-provider-kalshi-says-sports-contracts-are-subject-to-state-regulations); [CryptoTimes Oct 8 2026](https://www.cryptotimes.io/2026/10/08/39-states-urge-supreme-court-to-review-kalshi-sports-betting-dispute/). CONFLICT: a Prediction News headline reads "Sixth Circuit lets Kalshi keep sports contracts in Ohio and Tennessee" ([Prediction News](https://predictionnews.com/story/kalshi-split-widens-with-6th-circuit-ruling-on-sports-event-contracts); page 403, could not verify). The two fuller sources say the ruling went against Kalshi.
- Ninth Circuit ruled against Kalshi (not swaps, no preemption of Nevada law). The Second, Fourth, Seventh, Eighth, and Tenth Circuits and the Massachusetts SJC were still pending as of Oct 8, 2026. — [CryptoTimes](https://www.cryptotimes.io/2026/10/08/39-states-urge-supreme-court-to-review-kalshi-sports-betting-dispute/). CONFLICT: a CoinDesk summary referenced an Eighth Circuit holding that the contracts are not swaps, but CryptoTimes lists the Eighth as pending.
- Supreme Court: Flaherty v. KalshiEX, No. 26-299. NJ filed Sep 2, docketed Sep 8. Ohio plus 38 states and DC filed an amicus on Oct 7 supporting review. Kalshi's response is due Nov 9, 2026, and cert has not been granted. — [CryptoTimes](https://www.cryptotimes.io/2026/10/08/39-states-urge-supreme-court-to-review-kalshi-sports-betting-dispute/)
- New York sued Kalshi on July 31, 2026, and the CFTC then ordered Kalshi to keep offering markets in NY. — [CoinDesk Aug 11 2026](https://www.coindesk.com/policy/2026/08/11/cftc-orders-kalshi-to-continue-offering-prediction-markets-in-new-york-after-state-lawsuit)
- Massachusetts: in Jan 2026 a Suffolk Superior Court ruled Kalshi's sports contracts subject to state gaming law, and Kalshi moved to dismiss the expanded complaint in late Sep. — [Law360](https://www.law360.com/compliance/articles/2530632)
- Michigan: a court order on June 29, 2026 restricted sports contracts, and Kalshi "unwound the trades." — [SailGP/other guides via search](https://sailgp.com/prediction-markets/kalshi/pennsylvania)
- The CFTC has taken actions against AZ, CT, IL, KY, MN, NM, NY, RI, and WI over jurisdiction. — [CryptoTimes](https://www.cryptotimes.io/2026/10/08/39-states-urge-supreme-court-to-review-kalshi-sports-betting-dispute/)
- Availability counts conflict across affiliate sites: "42 states + DC" (listing NV, AZ, MD, MA, MI, MT, NJ, OH as unavailable, July 2026) vs "47 states" vs "all 50." Check the app. — [SailGP](https://sailgp.com/prediction-markets/kalshi/new-york); [Sportsbettingdime](https://www.sportsbettingdime.com/prediction-markets/kalshi/)
- States' motives: prediction markets compete with taxed state gambling and serve 18+ users while most sportsbooks require 21+. — [CoinDesk](https://www.coindesk.com/policy/2026/09/25/another-appeals-court-rules-against-prediction-market-provider-kalshi-says-sports-contracts-are-subject-to-state-regulations)

**Taxes:**
- Kalshi issues forms only above IRS thresholds: 1099-INT (interest), 1099-MISC (credits/rewards), 1099-B (crypto transfers), and 1099-DA (digital assets via ZeroHash), delivered via Zenwork. The PnL statement (FIFO, including fees and rebates, updated monthly) is the main record of trading gains. Kalshi gives no tax advice. — [Kalshi Help: Tax Info](https://help.kalshi.com/en/articles/13823849-tax-info); [Kalshi Help: Documents & Taxes](https://help.kalshi.com/documents-and-taxes/tax-info)
- Tax treatment is unsettled. Ordinary income is the most conservative approach. Capital gains and Section 1256 (60/40) treatment have been argued, but the IRS hasn't blessed 1256 for event contracts. Contract profits may not appear on any form, so keep your own trade log. — [Keeper Tax](https://www.keepertax.com/posts/how-to-file-taxes-on-kalshi-and-polymarket); [Octagon](https://www.octagonai.co/answers/kalshi-taxes/); [Beancount](https://beancount.io/zh/blog/2026/09/07/prediction-market-winnings-tax-kalshi-polymarket-guide)

**API/demo:**
- Create API keys in Account Settings → API Keys, which produces a Key ID plus an RSA private key shown once (Kalshi doesn't store it). The process is the same in demo and production. — [Kalshi Docs: API keys](https://docs.kalshi.com/getting_started/api_keys)
- Requests need the KALSHI-ACCESS-KEY, KALSHI-ACCESS-TIMESTAMP, and KALSHI-ACCESS-SIGNATURE headers, with an RSA-PSS signature over timestamp + method + path (query params stripped). The official demo example uses https://demo-api.kalshi.co/trade-api/v2. — [Kalshi Docs: quick start authenticated requests](https://docs.kalshi.com/getting_started/quick_start_authenticated_requests)
- Demo requires a separate account and keys, and its order book is reportedly near-empty, so use production for realistic read-only data. One third-party doc lists a different demo host (demo-api.elections.kalshi.com). — [PredictionHunt](https://www.predictionhunt.com/blog/kalshi-api-getting-started-guide); [pmxt SETUP_KALSHI](https://raw.githubusercontent.com/pmxt-dev/pmxt/HEAD/core/docs/SETUP_KALSHI.md)

### Inferences
- For a beginner, non-sports markets (weather, economics, crypto, mentions) carry less legal-status risk than sports, which could be curtailed state by state depending on SCOTUS.
- Because 1099s don't cover trading P&L, a bot should log every fill and fee independently for tax reconciliation.

### Gaps
- No authoritative, current list of states where Kalshi is unavailable. Official Kalshi deposit/withdrawal fee pages were not fetched (third-party figures only). IRS guidance on event-contract tax treatment does not exist yet.

## 5. Open-source Kalshi bots on GitHub and documented results

### Takeaway
There are dozens of open-source Kalshi bots (LLM-driven, weather, market-making, arbitrage, BTC short-term), but essentially none publish verified live results. The only reported figure found is an unverified "$1.8k max profit" for the most-starred weather bot.

### Cited Findings
- A Sep 23, 2026 catalog of 35 repos says none were code-audited or execution-tested, and only one performance figure appears. — [Bot for Kalshi (commercial competitor)](https://www.botforkalshi.com/blog/open-source-kalshi-bot-ecosystem)
- suislanchez/polymarket-kalshi-weather-bot (about 763 stars): KXHIGH markets, 31-member GFS ensemble via Open-Meteo, trades when edge > 8%, 15% fractional Kelly, plus a BTC 5-min strategy. Reported max profit $1.8k, unverified. — [GitHub](https://github.com/suislanchez/polymarket-kalshi-weather-bot); [catalog](https://www.botforkalshi.com/bot-catalog/suislanchez-weather)
- ryanfrigo/kalshi-ai-trading-bot (about 596 stars): Grok-4 multi-agent with 0.25 Kelly. Author caveat: no edge on economic releases. — [Bot for Kalshi](https://www.botforkalshi.com/blog/open-source-kalshi-bot-ecosystem)
- rodlaf/KalshiMarketMaker (about 401 stars): multiple MM strategies including Avellaneda-Stoikov. nikhilnd/kalshi-market-making (about 83 stars): S&P close band MM, a 2023 student project. — [Bot for Kalshi](https://www.botforkalshi.com/blog/open-source-kalshi-bot-ecosystem)
- OctagonAI/kalshi-trading-bot-cli (about 391 stars): AI edge calculation, Kelly sizing, risk gates. — [Bot for Kalshi](https://www.botforkalshi.com/blog/open-source-kalshi-bot-ecosystem)
- Arbitrage bots (Kalshi–Polymarket): ImMike/polymarket-arbitrage (about 283 stars), CarlosIbCu BTC 1-hour arb (about 253), and realfishsam/prediction-market-arbitrage-bot (about 180, blog billed as "risk-free," unverified). — [Bot for Kalshi](https://www.botforkalshi.com/blog/open-source-kalshi-bot-ecosystem)
- fsevkli/ProjectKM (KMBot): HRRR, METAR, and GEFS for same-day temperature, paper mode by default, MIT license. — [gitblind mirror](https://gitblind.noratr.app/fsevkli/ProjectKM)
- EddieTGH/kalshi-weather-predictor reports forecast MAE of 1.0°F (transformer) and 1.55°F (XGBoost). That measures forecast accuracy, not trading P&L. — [Bot for Kalshi](https://www.botforkalshi.com/blog/open-source-kalshi-bot-ecosystem)
- A paid weather bot ("Predict & Profit") reports 8 sales in its first two weeks, which are sales, not performance. — [IndieHackers](https://www.indiehackers.com/product/predict-profit)

### Inferences
- Open-source bots are useful as API/auth/order-management scaffolding (signing, websocket, kill switches), not as proven alpha. Weather and market-making repos match where the academic evidence suggests edges might exist.

### Gaps
- No repo found with audited live P&L over a meaningful sample. Star counts and claims are as reported by a commercial catalog, and eight repos were unverifiable.
