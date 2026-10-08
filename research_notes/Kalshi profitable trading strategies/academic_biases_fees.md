# Kalshi: Academic Evidence on Systematic Return Patterns, and Exact Fee Math (as of Oct 8, 2026)

## Q1. What does Bürgi, Deng & Whelan, "Makers and Takers: The Economics of the Kalshi Prediction Market", find?

### Takeaway
Kalshi shows a strong favorite-longshot bias, for both makers and takers. Contracts priced 10c or less lose more than 60% after fees. Contracts priced above 70c earn small but statistically significant positive post-fee returns. The average taker return is -31.46% and the average maker return is -9.64%. Makers buying at 50c or more earn about +2.6% per contract, with a standard deviation of 33%. The bias holds in every category, volume quintile, trade-size quintile and horizon tested. It is somewhat weaker in 2025 but still present. All data predate maker fees (sample ends April 2025).

### Cited Findings
**Versions and data**
- Versions:
  - CEPR DP20631 and CESifo WP 12122 (2025).
  - A January 2026 revision on the author's site.
  - GWU Forecasting Program WP 2026-001 (titled "Makers or Takers").
  - Sources: [Whelan PDF, Jan 2026](https://www.karlwhelan.com/Papers/Kalshi.pdf); [CEPR DP20631](https://cepr.org/publications/dp20631); [CESifo](https://www.ifo.de/en/cesifo/publications/2025/working-paper/makers-and-takers-economics-kalshi-prediction-market); [GWU](https://www2.gwu.edu/~forcpgm/2026-001.pdf)
- Sample: transaction data pulled from the Kalshi API, covering Kalshi's 2021 launch through April 2025. [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
  - 46,282 Yes contracts across 12,403 events.
  - 156,986 daily Yes prices (the last trade of each day, from closing back to 10 days before). Counting both the Yes and No side gives 313,972 contract prices.
- Filters: final volume of at least $1,000; final bid-ask spread of 20c or less; markets open at least 24 hours. **Hourly crypto and index markets are excluded.** [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Fees modeled: takers paid $0.07·P·(1−P) per contract, rounded up to the cent; makers paid nothing. The authors used a 100-contract lot for rounding, which makes the fee at 50c equal to 1.77% of price instead of 1.75%. They chose the April 2025 cut-off because "Kalshi began to charge fees on Makers after April 2025." [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Price distribution: about two-thirds of observations are priced below 10c or above 90c (106,209 in each tail, or 33.8% each). Only 8,351 observations fall in the 50-59c band. [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Market size and liquidity: [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
  - Median money staked per contract: $8,982.
  - Mean final volume: $61,977; top-decile mean: $526,245.
  - Mean transaction: $100; median transaction: $35.

**Returns by price**
- Contracts at 10c or less: average loss above 60%.
- Losses shrink as price rises, with small positive returns above 50c. Above 70c, post-fee returns are positive and statistically significant but small.
- Worked example: a 5c contract that wins 3% of the time returns −40% before fees. A 95c contract that wins 98% of the time returns +3.1% before fees.
- The equal-weighted average pre-fee return across contracts is −20%.
- Source: [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)

**Makers vs takers**
- Average maker return: −9.64%. Average taker return: −31.46%. The difference is highly significant. [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Makers buying at 50c or more earn +2.6% on average. The standard deviation of those returns is 33%. [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Maker share of purchases by price band: [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)

| Price band | Maker share |
|---|---|
| 1-10c | 43.5% |
| 41-50c | 49.5% |
| 80-89c | 53.3% |
| 90-99c | 56.5% |

  Cheap contracts are bought mainly by takers.
- On the closing day, makers' losses on cheap contracts look similar to takers' losses. The authors read this as a possible "Yogi Berra effect": losing sides stay overpriced late in the market. [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)

**Bias regressions**

The test regresses pre-fee profit (Y − P) on price: (Y−P) = α + ψP. A positive ψ with a negative α means a favorite-longshot pattern. (The coefficients appear to be scaled with price in cents.) All results below are from [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf).

- **Full sample:** ψ = 0.034, α = −1.736. Unbiasedness is rejected with p = 0.000.
- **By contract structure:**

| Contract type | ψ |
|---|---|
| Single-contract markets (largest) | 0.045 |
| Non-exclusive | 0.036 |
| Exclusive numerical | 0.014 |

- **By days to close:** ψ is between 0.017 and 0.041 for every horizon from 0 to 10 days, and every horizon rejects. Day 0: ψ = 0.036 (n = 46,282). Mean absolute error falls steadily as close approaches, with a sharp drop on the last day.
- **By final-volume quintile:** ψ falls from 0.045 (lowest quintile) to 0.032 (highest). Apart from the lowest quintile, there is "no evidence of prices in higher-volume markets being more efficient."
- **By mean trade-size quintile:** the largest-trade quintile has the largest ψ (0.043). Bigger trades do not mean better prices.
- **By category:**

| Category | ψ | Significance |
|---|---|---|
| Crypto | 0.058 | *** |
| Other | 0.053 | *** |
| Financials | 0.032 | *** |
| Climate & Weather | 0.031 | *** |
| Economics | 0.034 | *** |
| Politics | 0.022 | not significant |
| Entertainment | 0.020 | not significant |

- **By year:**

| Year | ψ | Significance | n |
|---|---|---|---|
| 2021 | 0.041 | | |
| 2022 | 0.023 | | |
| 2023 | 0.036 | | |
| 2024 | 0.048 | | |
| 2025 (Jan–Apr) | 0.021 | * (weakest) | 51,321 |

  The authors call this "some evidence that the bias in prices is diminishing over time." Results are robust to dropping sports or ending the sample in December 2024.

**Why the bias is not competed away (Section 6)**

All from [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf):
- Volumes and order-book depth are small. In their example, the April 2025 CPI order book had only $33.60 available at the best ask.
- Risk is high: SD 33% against a mean of +2.6%.
- Lack of awareness. The authors expect the anomaly might decay now that it has been published.

**Model**

Traders hold heterogeneous beliefs and choose to make or take. A behavioral overweighting of small probabilities is necessary to fit the data. In the calibration, a true 20% probability is believed to be about 23%. [CEPR VoxEU summary (via search snippet)](https://cepr.org/voxeu/columns/economics-kalshi-prediction-market)

### Inferences
- The +2.6% maker return on contracts priced 50c and above was earned with **zero maker fees**. A maker fee of 0.0175·P(1−P) at 75c costs about 0.44% of stake, and at 90c about 0.18%. That still leaves a positive margin in pre-fee terms, but it is thinner. It also applies only to the series that now charge maker fees (see Q3).
- The returns are equal-weighted across daily last-trade snapshots, not dollar-weighted P&L from a strategy. Fill uncertainty (adverse selection on resting orders) is not modeled. A maker's realized fills would likely be worse than the average trade price.
- The paper excludes hourly and 15-minute crypto and index markets, which are now a large share of activity. Its results should not be assumed to transfer to those markets.

### Gaps
- The paper's figures, not its text, report exact return values per 10c price band (Figures 5–8). Only the text summaries above could be extracted, so the per-band percentages (for example, 80-89c and 90-99c separately) are not available here.
- No published study yet tests the period after maker fees began (May 2025 onward), or the sports-heavy era from 2025 to 2026, with the same methodology.

---

## Q2. Other studies (2023–2026): favorite-longshot bias and calibration on Kalshi, Polymarket and others; does the bias shrink with volume?

### Takeaway
Independent work on Polymarket also finds overpriced longshots and underpriced favorites. A large two-platform study (353M trades) finds calibration depends on domain: political markets are *underconfident*, with prices compressed toward 50%. Evidence that volume removes the bias is weak. Press-reported studies find the taker-to-maker transfer on Kalshi is about ±1.12% per trade, with takers losing hundreds of millions of dollars in total.

### Cited Findings
- **Le, "Decomposing Crowd Wisdom: Domain-Specific Calibration Dynamics in Prediction Markets"** (arXiv 2602.19520; v1 Feb 23, 2026, v2 Aug 4, 2026): [arXiv](https://arxiv.org/abs/2602.19520)
  - Data: 353M trades across 429k binary contracts on Kalshi and Polymarket.
  - The most robust pattern is persistent **underconfidence in political markets** (prices compressed toward 50%). This replicates on Polymarket.
  - Large political trades on Kalshi come with further compression, with a calibration-slope gap of about 0.5. That result is not robust on Polymarket.
  - A slope decomposition explains 87.3% of variance in-sample and 71.5% out-of-sample. About half of the raw slope variation is estimation noise.
  - Conclusion: "a price's meaning depends on what, when and how much is traded."
- **Princeton senior thesis on Polymarket calibration** (author and date not confirmed): [Princeton (search snippet)](https://theses-dissertations.princeton.edu/entities/publication/d5708372-5ea3-4252-b669-7f9cee07387c)
  - Brier Skill Score 0.398.
  - Logistic recalibration slope 1.112. A slope above 1 means longshots are overpriced and favorites underpriced.
- **Qin & Yang, "Polymarket-v1 Database"** (arXiv 2606.04217, June 2026): [arXiv](https://arxiv.org/abs/2606.04217); [search snippet](https://arxiv.org/pdf/2606.04217)
  - Data: 1.20B trades across 1.30M markets, $61B nominal volume, Nov 2022 to Apr 2026, with aggressor side known from on-chain data.
  - The tick rule and bulk-volume classification identify the aggressor with only 49.83% and 50.51% accuracy. Inferred order-flow metrics are unreliable.
  - Per the search snippet, contracts priced at or below 0.30 show negative mean returns and those at 0.40 or above show positive mean returns. The abstract does not confirm this.
- **Wealth-transfer studies, as reported by the press:** [American Prospect, Aug 26, 2026](https://prospect.org/2026/08/26/house-always-wins-kalshi-prediction-markets/); [Casino.org](https://www.casino.org/news/kalshi-rebuffs-think-tank-claim-regular-traders-lost-584-million-on-platform/)
  - An SSRN study found Kalshi takers lose 1.12% per trade on average and makers gain 1.12%. The pattern was reversed early in Kalshi's life, before institutional liquidity providers arrived.
  - The Roosevelt Institute estimates takers lost $584M from July 2021 to mid-May 2026.
  - Kalshi disputes the Roosevelt framing, saying it conflates "maker" and "taker" with "professional" and "casual."
- Further figures from the Prospect article: [American Prospect](https://prospect.org/2026/08/26/house-always-wins-kalshi-prediction-markets/)
  - Sportico: retail lost $117M to market makers on Kalshi "combos" (parlays) between January and April 2026.
  - Bloomberg: the bottom quartile of new Kalshi users lose 28c per dollar in their first 3 months, against 11c at sportsbooks.
  - Kalshi gives market makers fee discounts, rebates and revenue share.
  - DraftKings estimates 80–90% of its prediction-market volume is professional or institutional.
- A crypto-exchange news piece attributes to "Jonathan Becker" an analysis of 72.1M Kalshi trades ($18.26B volume) with the same ±1.12% taker/maker split. **I could not locate the primary source.** [HTX news (secondary)](https://www.htx.com/news/only-43-return-on-1-why-are-87-of-polymarket-players-losing-VF6N2Lau/)
- Earlier literature as summarized by BDW: [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
  - Iowa Electronic Markets: no favorite-longshot bias (Berg & Rietz 2019).
  - InTrade: favorite-longshot bias only more than 10 days out, explained by discounting (Page & Clemen 2013).
  - InTrade sports: losing teams overpriced in the final 15 minutes, the "Yogi Berra bias" (Page 2012).

### Inferences
- Across platforms, the evidence agrees: **cheap contracts and taker flow lose, and patient liquidity provision on favorites gains a little**. The exception is that political markets may be *underconfident* rather than longshot-biased, so a blanket "buy favorites" rule may be wrong-signed in politics. Both Le 2026 and BDW find politics to be the weakest favorite-longshot category, with insignificant ψ.
- The ±1.12% per-trade figure, if accurate, shows the maker edge is small per trade and is now captured mainly by institutional market makers who receive fee rebates. A retail bot without rebates competes against them.

### Gaps
- The SSRN paper behind the 1.12% figure, the Roosevelt methodology and the Becker analysis could not be retrieved firsthand.
- No replication or formal critique of BDW was found. Its methodological limits (equal-weighting, daily snapshots, no maker fees, hourly markets excluded) are noted in Q1.
- Betfair and PredictIt studies from 2023–2026 were not covered within the tool budget.

---

## Q3. Kalshi's current fee schedule (2026)

### Takeaway
- **Taker fee:** ceil(0.07 × M × C × P × (1−P)).
- **Maker fee (only on series flagged `quadratic_with_maker_fees`):** ceil(0.0175 × M × C × P × (1−P)).
- M is a per-series multiplier: usually 1, 0.5 for MLB since Aug 7, 2026, and 0 for a few fee-free series.
- No settlement, membership or ACH fees. Card deposits cost up to 2%.
- **Change on Jul 3, 2026:** the half-rate (0.035) for S&P 500 and Nasdaq-100 markets was removed. The KXINX and KXNASDAQ100 families now pay the standard 0.07.

### Cited Findings
**Official fee schedule PDF (last updated and effective Feb 5, 2026)**

All from the [Kalshi Fee Schedule PDF (Wayback copy of Jun 12, 2026)](https://web.archive.org/web/20260612075630/https://kalshi.com/docs/kalshi-fee-schedule.pdf):
- Taker fee: "fees = round up(0.07 x C x P x (1-P))", where P is price in dollars, C is contract count, and "round up = rounds to the next cent." The fee applies only to orders that are immediately matched.
- Maker fee: "round up(0.0175 x C x P x (1-P))". It applies only to markets listed on kalshi.com/fee-schedule, is charged only on execution, and cancelling costs nothing. If rounding causes maker-fee overpayment above $10 in a month, it is reimbursed in the first week of the following month.
- General fee table:

| Price | Fee for 1 contract | Fee for 100 contracts |
|---|---|---|
| 1c | $0.01 | $0.07 |
| 5c | $0.01 | $0.34 |
| 10c | $0.01 | $0.63 |
| 20c | $0.02 | $1.12 |
| 25c | $0.02 | $1.32 |
| 30c | $0.02 | $1.47 |
| 40c | $0.02 | $1.68 |
| 50c | $0.02 | $1.75 |
| 85c | $0.01 | $0.90 |
| 90c | $0.01 | $0.63 |
| 95c | $0.01 | $0.34 |
| 99c | $0.01 | $0.07 |

- In the February 2026 PDF, S&P 500 (INX\*) and Nasdaq-100 (NASDAQ100\*) markets use round up(0.035 × C × P × (1−P)). That is $0.88 per 100 contracts at 50c and $0.32 per 100 at 10c or 90c.
- Other fees:
  - Settlement fee: none. Membership fee: none.
  - ACH deposits and withdrawals: free.
  - Kalshi adds no fee on wire deposits. Wire withdrawals are not supported under $500,000.
  - Debit card deposits: up to 2%.
  - Crypto deposits and withdrawals: third-party processor fees may apply.
  - Customers coming through an FCM may face different fees.

**Live API check (Oct 8, 2026)**

Values pulled from `GET /trade-api/v2/series/{ticker}` and `/series/fee_changes?show_historical=true` on [Kalshi API](https://api.elections.kalshi.com/trade-api/v2/series/fee_changes?show_historical=true):
- `fee_type` and `fee_multiplier` by series:

| Fee type and multiplier | Series |
|---|---|
| quadratic, M = 1 (taker only, no maker fee) | KXBTC15M, KXETH15M, KXSOL15M, KXBTCD, KXETHD, KXINX, KXINXU, KXNASDAQ100, KXNASDAQ100U, KXHIGHNY, KXUFCFIGHT, KXTRUFEGGS, KXMVENFLSINGLEGAME |
| quadratic_with_maker_fees, M = 1 | KXNBAGAME, KXNFLGAME, KXNHLGAME, KXNCAAFGAME, KXWNBAGAME, KXEPLGAME, KXATPMATCH, KXFED, KXCPI, KXPAYROLLS, KXGDP, KXINXY |
| quadratic_with_maker_fees, M = 0.5 | KXMLBGAME |

- Number of series by fee type, per category (counts series, not volume):

| Category | Taker only (M = 1) | With maker fees (M = 1) | Half rate (M = 0.5) | Fee-free (M = 0) | Other |
|---|---|---|---|---|---|
| Sports | 3,746 | 106 | 18 taker-only, 1 with maker fees | | |
| Crypto | 272 | 2 | | 2 | |
| Financials | 995 | 13 | | | |
| Economics | 845 | 10 | | 3 | |
| Entertainment | 2,579 | 7 | | | |
| Elections | 2,213 | | | 2 | |
| Climate & Weather | 419 | | | | |
| Companies | 216 | | | | |
| Exotics | 11 | | | | 3 combo-maker |

  The *flagship high-volume* game-winner and macro series are the ones that carry maker fees.
- Fee-change log: 107 entries, from Oct 2025 to Sep 2026.

| Month | Entries |
|---|---|
| Oct 2025 | 9 |
| Nov 2025 | 23 |
| Jan 2026 | 3 |
| Feb 2026 | 4 |
| Mar 2026 | 4 |
| Jun 2026 | 1 |
| Jul 2026 | 10 |
| Aug 2026 | 23 |
| Sep 2026 | 30 |

  Notable entries:
  - **2026-07-03:** KXINX, KXINXU, KXINXPOS, KXINXMINY, KXINXMAXY, KXNASDAQ100 and KXNASDAQ100U set to quadratic with M = 1. **This ended the 0.035 half-rate** shown in the February PDF.
  - **2026-08-07:** about 20 MLB series (game, spread, total, props) cut to M = 0.5. Only KXMLBGAME keeps maker fees.
  - **2026-08-20:** KXMVECROSSCATEGORY and KXMVESPORTSMULTIGAMEEXTENDED moved to `quadratic_with_combo_maker_fees`.
  - **Fee-free (M = 0):** KXBTCY, KXETHY, KXCITRINI, KXLAYOFFSYINFO (Feb 26, 2026); KXGDPYEAR (Jul 28, 2026); several geopolitical series (Iran, Greenland, Trump-out and others; Oct 2025 and Mar 2026).
  - **2026-09-03:** a batch of GPU-price series (KXH100\*, KXA100\*, KXB200\*) given maker fees.
- Combo/RFQ adjustment on KXMVE, effective no earlier than Jul 24, 2026. For trades that do not involve an order resting more than 5 seconds, the trader hitting a quote pays the taker fee and the quoter pays the maker fee. The adjustment is applied within 5 seconds after execution. [CFTC filing, Jul 12, 2026](https://www.cftc.gov/filings/orgrules/rules0712269458.pdf)
- Perpetual futures have a separate tiered bps schedule (filing effective no earlier than Jun 22, 2026). Volume tiers count prediction-contract volume too. [CFTC filing (search summary)](https://www.cftc.gov/filings/orgrules/rules0608265590.pdf)
- Fee rounding mechanics (API docs): [Kalshi docs: fee rounding](https://docs.kalshi.com/getting_started/fee_rounding) (via search summary); [Allium](https://docs.allium.so/historical-data/predictions/kalshi/series-fee-changes)
  - Each fill has a trade fee, which is rounded up to $0.0001, plus a sub-cent "rounding fee" that brings the balance to cent alignment, minus any rebate.
  - A per-order **fee accumulator** issues a 1c rebate whenever accumulated rounding overpayment passes $0.01, so many small fills cost about the same as one fill.
  - Direct members' balances target $0.0001 precision; others target $0.01.
  - Subpenny prices and fractional contracts exist (fixed-point migration doc, March–April 2026).
- The help center (Apr 19, 2026) says some markets carry event-specific fees (elections, awards, championships). The fee for a given order is shown via the "i" icon in the order ticket. [Kalshi Help: Fees](https://help.kalshi.com/trading/fees)
- Market makers can get fee discounts, rebates and revenue share under their agreements. [American Prospect](https://prospect.org/2026/08/26/house-always-wins-kalshi-prediction-markets/)

### Inferences
- A bot should **read `fee_type` and `fee_multiplier` from the series endpoint and poll `/series/fee_changes`** rather than hard-code values. The schedule changed in about 50 series between Jul and Sep 2026 alone.
- Third-party guides still citing a 0.035 rate for S&P/Nasdaq are outdated as of Jul 3, 2026 for the KX-prefixed series.
- Rounding: one contract at 50c pays $0.02, which is 4.0% of stake against 3.5% for a large order. One contract at 95c pays $0.01, which is 1.05% of stake against 0.35% for a large order. Trade in lots large enough for rounding to be negligible, or rely on the accumulator within a single order.

### Gaps
- The live kalshi.com/fee-schedule page sits behind a Vercel bot check and was not readable. A newer PDF than the Feb 5, 2026 version may exist (the Jun 12 Wayback snapshot still showed Feb 5).
- The exact formula for `quadratic_with_combo_maker_fees` was not found.
- Whether 15-minute crypto series had different rates earlier in 2025 is unknown. As of today they are taker-only at M = 1 (no maker fee).
- Volume-tier or market-maker rebate rates for event contracts are not public.

---

## Q4. Implied break-even edge (taker vs maker)

### Takeaway
To break even, a taker needs a true win probability above P by 7·P·(1−P) percentage points: 1.75 pp at 50c, 0.63 pp at 10c or 90c, 0.33 pp at 95c. A maker on a fee-charging series needs a quarter of that (0.44 pp at 50c). A maker on a taker-only series needs only to be right on average, net of adverse selection.

### Cited Findings
- Formulas: taker 0.07·P·(1−P) and maker 0.0175·P·(1−P) per contract, rounded up to the cent. There is no settlement fee. [Kalshi Fee Schedule PDF](https://web.archive.org/web/20260612075630/https://kalshi.com/docs/kalshi-fee-schedule.pdf)
- River Markets case study (Aug 2026): filling 50,000 contracts as a taker cost $598 in venue fees, against $155 for a routed maker execution. [River Markets](https://www.rivermarkets.com/insights/kalshi-fees.html)

### Inferences (computed from the official formula, large lots, M = 1)

| Price P | Taker fee (c/contract) | Taker fee as % of stake | Taker break-even win prob | Maker fee (c) | Maker break-even |
|---|---|---|---|---|---|
| 5c | 0.33 | 6.65% | 5.33% | 0.08 | 5.08% |
| 10c | 0.63 | 6.30% | 10.63% | 0.16 | 10.16% |
| 30c | 1.47 | 4.90% | 31.47% | 0.37 | 30.37% |
| 50c | 1.75 | 3.50% | 51.75% | 0.44 | 50.44% |
| 70c | 1.47 | 2.10% | 71.47% | 0.37 | 70.37% |
| 85c | 0.89 | 1.05% | 85.89% | 0.22 | 85.22% |
| 90c | 0.63 | 0.70% | 90.63% | 0.16 | 90.16% |
| 95c | 0.33 | 0.35% | 95.33% | 0.08 | 95.08% |
| 98c | 0.14 | 0.14% | 98.14% | 0.03 | 98.03% |

- For MLB (M = 0.5), halve every fee figure. Fee-free series (M = 0) have zero fees.
- Fees fall with distance from 50c, so favorites are the cheapest place to trade on fee drag. Above 90c, though, payoff variance per dollar of edge is extreme: losing once at 95c wipes out about 19 wins.
- Exiting before settlement pays the fee a second time (settlement is free). A taker round trip at 50c costs about 3.5c, or 3.5 pp of probability.
- The fee is set by price, not by edge. In relative terms the fee bites hardest on cheap contracts: 6.3% of stake at 10c, which adds to BDW's measured loss of more than 60% on longshots.

### Gaps
- Real break-even must also cover spread crossing (takers), adverse selection (makers) and capital lock-up. No source quantified adverse selection for Kalshi makers.

---

## Q5. Is a simple rule (buy favorites above 85c, sell longshots, always make) profitable after fees? Capacity?

### Takeaway
The evidence favors **selling longshots / buying favorites as a maker**. That is the only bucket with a significantly positive return: about +2.6% per contract for makers at 50c and above, before maker fees, on 2021–Apr 2025 data. The edge is small relative to variance (SD 33%), is limited by thin books, may be decaying (weakest ψ in 2025), and is already the business model of rebated institutional market makers. Buying favorites as a taker is roughly break-even to slightly positive above 70c. Buying longshots loses heavily in every cut.

### Cited Findings
- Post-fee returns above 70c are "statistically significant, though small, positive." Contracts at 10c or less lose more than 60%. Makers at 50c and above earn +2.6% with SD 33%. [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Capacity: top-decile markets average only $526k in final volume; the median contract has $8,982 staked; best-level depth is often tens of dollars. "Someone who wanted to invest substantial capital as a Maker... may have to post prices that are less advantageous." Unfilled orders cut deployed capital further. [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- Higher volume does not remove the bias, apart from the lowest quintile. The 2025 bias coefficient is the smallest of any full year. [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf)
- The maker-side transfer of about +1.12% per trade now accrues to institutional liquidity providers. Those providers get fee discounts and rebates, and DraftKings estimates 80–90% of its prediction-market volume is professional. [American Prospect](https://prospect.org/2026/08/26/house-always-wins-kalshi-prediction-markets/)
- Politics: weakest favorite-longshot ψ (0.022, not significant) per [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf). Politics prices are underconfident (compressed toward 50%) per [Le 2026](https://arxiv.org/abs/2602.19520). Crypto shows the strongest bias (ψ = 0.058) for daily-plus markets per [Whelan PDF](https://www.karlwhelan.com/Papers/Kalshi.pdf).

### Inferences
- "Always be maker" on **taker-only series** (most weather, 15-minute crypto, S&P/Nasdaq daily and hourly, most entertainment) avoids all fees. These are also the categories where BDW find a strong bias (crypto, weather, financials). On flagship sports and macro series, makers now pay 0.0175·P(1−P). That is about 0.16–0.37c per contract in the 70–90c zone, which takes a meaningful bite out of a +2.6% edge.
- A rough check of edge versus fee at 85c:
  - An 85c contract that wins 87% of the time earns 2c/85c ≈ +2.35% pre-fee.
  - The maker fee is 0.22c, about 0.26%. The taker fee is 0.89c, about 1.05%.
  - Both still clear, but a 1 pp miscalibration erases the taker's margin.
- The equal-weighted, daily-snapshot design of BDW overstates what a resting order earns. Resting orders on favorites are filled mostly when news moves against them (adverse selection). Expect realized returns below +2.6%.
- Capacity estimate: tens of thousands of dollars of deployed capital per day across many markets, not millions. Thin depth and competing rebated market makers cap scale.
- Avoid buying longshots under 20c in any role. Makers lost money on 10c-and-under contracts on 5 of 6 horizons tested, and on the closing day losses were similar to takers'. Be most careful in the final hours, when losing sides stay overpriced.

### Gaps
- No out-of-sample test of a "maker buys at 85c or above" strategy after May 2025 with maker fees exists in the literature found.
- No study quantifies fill rates or adverse selection for retail resting orders on Kalshi.
- Returns for 15-minute and hourly markets (now high-volume) have not been studied academically.
