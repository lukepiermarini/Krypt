# Market Making, Liquidity Provision and Incentive Programs on Kalshi (small retail bot operator, as of Oct 2026)

Research date: 2026-10-08. Kalshi has changed fees and incentive terms many times in 2025-2026. Every number below should be checked against the live market page, the fee schedule and kalshi.com/regulatory/notices before money is risked. Undated or stale items are flagged.

## 1. Incentive programs as of 2026 (LIP, volume incentives, MM program, interest)

### Takeaway
The **Liquidity Incentive Program (LIP)** is the program a small resting-order bot can actually use. It pays daily per-market pools of **$1 to $1,000**, scored on once-per-second random snapshots of resting two-sided depth near the touch, with a **$1 minimum payout**. A July 30, 2026 amendment extended it to **Jan 1, 2027** and appears to have removed the exclusion of Kalshi affiliates and contracted market makers, so retail now competes for the same pools as the professionals. The **Volume Incentive Program** is being terminated no earlier than **Oct 13, 2026**, amid wash-trading allegations about perps volume. Interest of about **3.25% APY** on cash plus open positions (balances of $250 or more) is a small extra yield on capital tied up in quotes.

### Cited Findings
**Liquidity Incentive Program: mechanics (primary sources)**
- The program applies to all Kalshi markets. Market pages say whether a market is eligible and show a "Liquidity Incentive Schedule" of Time Periods, each with a Target Size, a Discount Factor and a Time Period Reward — [CFTC filing, July 15, 2026 amendment](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf)
- Parameter bounds: a Time Period is at most 31 days and may overlap others. Target Size is more than 100 and less than 20,000 contracts. Discount Factor is at most 1.00. Reward is **at least $1 and at most $1,000 per calendar day** (the minimum was $10 before the July 2026 amendment) — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf)
- Snapshots are taken once per second at a uniformly random time. A snapshot is excluded if the market is closed or if resting orders do not reach the Target Size on **both** the yes and no sides — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf); [Kalshi Help Center – LIP](https://help.kalshi.com/en/articles/13823851-liquidity-incentive-program)
- How the qualifying set is built: a yes ask counts as a no bid. Start at the best yes bid and walk down, adding size. The **Reference Price** is the first level where cumulative size reaches 1/5 of the Target Size. Stop once cumulative size reaches the Target Size. Bids beyond the Target Size are not counted, and if total depth never reaches the Target Size the side has no qualifying bids — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf)
- Score per bid = DiscountFactor^max(RefPrice − bidPrice in ticks, 0) × size, normalized by the sum over all qualifying bids on that side. A user's snapshot score is the sum of their yes and no normalized shares, so the maximum is 2.0. The Time Period score is the user's summed snapshot scores divided by everyone's. Payout = TP score × TP Reward × (non-excluded snapshots / total snapshots), paid only if it is $1.00 or more and rounded down to the cent — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf)
- Kalshi's CRO can revoke a participant's status if participation is "abusive or in any way inconsistent with the purpose of the Program". Kalshi may end the program at any time — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf)

**LIP: eligibility and dates (conflicting sources)**
- The **redlined** July 2026 filing shows the old exclusions struck: "(i) affiliates of Kalshi; (ii) members who have executed a Market Maker Agreement with Kalshi". The **clean** version excludes only Introducing Brokers, FCMs and their customers. The stated purpose is to make the program "more uniformly available to market participants", and the amendment took effect **July 30, 2026** — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf)
- The Help Center still lists Kalshi affiliates and employees as excluded, along with IBs, FCMs and their customers, and **non-U.S. users**. It also says a **verified SSN** is required to receive reward credits above IRS reporting thresholds, and that referral earnings count toward that threshold. Daily rewards run $1–$1,000 per market. The program end date is Jan 1, 2027 — [Kalshi Help Center – LIP](https://help.kalshi.com/en/articles/13823851-liquidity-incentive-program). This page may lag the filing on the affiliate and MM exclusion, so treat that point as a conflict.
- The previous end date was the earlier of Sept 1, 2026 or Jan 1, 2027. The clean amendment changes it to Jan 1, 2027 — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf). Some search snippets of the help page still show "Sept 15, 2025 – Sept 1, 2026", which is outdated.
- Original launch: the CFTC filing was dated around Aug 2025 with a start "Aug 22 or later". An ex-Kalshi Trading market maker described it as a direct payment for tight quotes, scored as size × discount^distance and averaged over random per-second snapshots — [UFO Holdings Substack (Adhi Rajaprabhakaran), Aug 25, 2025](https://ufoholdings.substack.com/p/kalshis-new-liquidity-incentives)
- A separate **FOOTBALLSTATS Liquidity Incentive Program** starts on or after Aug 25, 2026 and runs until Jan 1, 2027 — per search summary of [CFTC filing 08122616002](https://www.cftc.gov/filings/orgrules/rules08122616002.pdf) (not fetched in full; details unverified).

**Volume Incentive Program (ending)**
- Kalshi filed with the CFTC to end its "Volume Incentive Program" **no earlier than Oct 13, 2026**. The program launched in March 2023 and paid traders from reward pools in proportion to their share of eligible volume, for CLOB trades typically priced $0.03–$0.97. Pool sizes were not disclosed — [The Block, Sept 30, 2026](https://theblock.co/news/business/2026-09-30-kalshi-ends-trader-incentive-program-417247); [Gambling.com](https://www.gambling.com/us/news/kalshi-end-volume-incentive-program-october-13)
- Context: the WSJ reported that the CFTC was examining repeated ~$5,500 ETH-perp trades, said to total more than $5B of volume in a month. Kalshi says it is not under investigation, that wash trading does not occur on its platform, and that the trades came from market makers posting fixed quotes that faster traders hit — [The Block](https://theblock.co/news/business/2026-09-30-kalshi-ends-trader-incentive-program-417247). Note that The Block's headline says "liquidity incentive program" but the body says the *Volume* Incentive Program. The LIP itself does not appear to be terminated.

**Market Maker program (institutional)**
- Susquehanna (SIG) was onboarded in April 2024 as Kalshi's first dedicated institutional market maker — [BusinessWire, Apr 3, 2024](https://www.businesswire.com/news/home/20240403664852/en/Kalshi-Onboards-Its-First-Dedicated-Institutional-Market-Maker)
- Applicants are reportedly evaluated on financial stability, experience and reputation. Benefits reportedly include financial incentives, reduced fees, adjusted position limits and enhanced access. Kalshi's membership terms disclose order protections that can advantage market makers — search summaries citing [Sportico](https://www.sportico.com/business/sports-betting/2025/kalshi-trading-exchange-peer-house-1234870465/) and related sources (secondary; not verified against a Kalshi primary page)
- Kalshi Trading is an in-house affiliate market maker. Kalshi's co-founder said it is "not profitable" — [Yahoo Finance](https://finance.yahoo.com/news/kalshi-co-founder-says-house-174507266.html) (headline and snippet only)

**Interest (APY)**
- Help Center: **3.25%** variable, accrued daily on available cash plus the end-of-day value of open positions at last-traded prices. Paid monthly, usually in the first week, up to 10 business days. U.S. users only, and only on balances of **$250 or more** — [Kalshi Help – APY](https://help.kalshi.com/navigating-the-exchange/your-portfolio/apy-on-kalshi)
- An older FAQ page says 4.05%, available only for Kalshi Klear deposits, and is **outdated** (from an Oct 2024 launch) — [Kalshi FAQ](https://help.kalshi.com/faq/interest-apy-on-kalshi). An affiliate review says 3.50% — [defirate](https://defirate.com/?p=1823) (referral site, lower trust)

### Inferences
- **Small accounts can participate in the LIP**, but the pool is split by share of qualifying depth. Every market's book has to reach the Target Size (at least 100 contracts) on both sides before a snapshot counts, and a small account cannot make that happen alone. The account only earns a share alongside larger quoters.
- Example: a market pays $50/day and a retail bot supplies 5% of time-weighted qualifying depth on both sides. That earns about $2.50/day, before any fill P&L. A few hundred dollars of capital can only post a few hundred contracts near 50¢, or more near the extremes. Reward per dollar of capital is better in low-competition, low-volatility markets.
- Since July 30, 2026, Kalshi's own affiliate and contracted market makers appear to count in the same denominator. This makes high-traffic markets less attractive to retail. The "garage-band market maker" opportunity is most plausible in long-tail markets with a small pool and few quoters.
- APY makes resting capital roughly carry-neutral. 3.25% on $2,000 is about $65/year.

### Gaps
- No public data on the **actual distribution** of LIP payouts (total paid, per-market pool sizes over time, or concentration). I found no API field that exposes the incentive schedule; the 2025 Substack raised this as an open question.
- Whether the Help Center's "affiliates excluded" or the July 2026 filing's clean text (affiliates and MMs eligible) governs in practice.
- Terms of the FOOTBALLSTATS LIP and of the perps referral or incentive programs were not read in full.
- No primary source found for maker "rebates" to retail. The Bitcoin.com article mentions "rebates and liquidity rewards paid to market makers" without detail.

## 2. Maker fees: which markets, how much

### Takeaway
Most Kalshi markets charge **no maker fee**. A specific list of series does, with a rate generally quoted as **1.75% × C × P × (1−P)**, rounded up. That is about a quarter of the taker coefficient (0.07). They include major sports games, some econ series (CPI, Fed) and awards. Since **Aug 20, 2026**, **combo/parlay** series charge makers 50% of the taker fee. Canceling is free.

### Cited Findings
- Maker fees apply only when a resting order is later executed, and canceling a resting order costs nothing. Some markets, often elections, awards and major sports championships, have different fees. The per-market fee is shown via the "i" icon next to "You're buying" — [Kalshi Help – Fees (dated Apr 19, 2026)](https://help.kalshi.com/trading/fees)
- Maker fee formula: round up(0.0175 × C × P × (1−P)). Maker fees are not the default — per search summary of [Kalshi fee schedule PDF](https://kalshi.com/docs/kalshi-fee-schedule.pdf) (direct fetch returned HTTP 429) and [Oddpool](https://www.oddpool.com/research/prediction-market-fees-explained). For comparison, the standard taker coefficient is commonly cited as 0.07. That figure is not re-verified here; see [Whirligig Bear survey](https://whirligigbear.substack.com/p/a-quick-survey-of-prediction-market).
- Markets with maker fees, per 2025 reporting: NFL, NBA and NHL games, golf and tennis majors, and some economy markets — [InGame](https://www.ingame.com/kalshis-change-may-increase-fee-sports-traders/). One third-party site counts about 156 series (e.g. KXMLB, KXNBA, KXNFLGAME, KXCPI, KXFED) — [StartPolymarket](https://startpolymarket.com/reviews/kalshi-review/); another says about 100 series sit outside the no-maker-fee default — [Oddpool](https://www.oddpool.com/research/prediction-market-fees-explained). These counts conflict and come from different dates.
- **Combo/parlay maker fee**: effective Aug 20, 2026 on three combo series, at 50% of the taker fee ("double the standard maker rate" of 1/4 taker). Uncorrelated NFL parlays are exempt. It raised about $26M in its first four weeks, with $1.7M on Sept 12 alone, and parlay maker fees are now the majority of maker-fee revenue. Average total fees were $12.3M/day in the week to Sept 15. The markup on uncorrelated non-NFL combos rose from about 0.55% to about 3.1%. Makers earned $24M profit after fees in the four weeks after the change, lower than any of the prior three four-week periods — [Bitcoin.com News, citing InGame analysis](https://news.bitcoin.com/kalshis-parlay-maker-fee-brought-26-million-four-weeks/)
- Retail cannot offer parlay lines in the app; parlays are filled through RFQ by professional market makers — [Sportico, 2026](https://www.sportico.com/business/sports-betting/2026/kalshi-parlays-retail-bettor-losses-rfq-1234894471/) (via search summary)

### Inferences
- At P = 0.50, the maker fee is 0.0175 × 0.25 ≈ 0.44¢ per contract. Because of round-up per order, small orders pay more per contract (1 contract = 1¢). A small MM should (a) prefer no-maker-fee series, and (b) where maker fees apply, post larger single orders rather than many 1-lot orders.
- A spread of 1–2¢ in fee-bearing sports markets loses roughly 20–45% of the gross spread to maker fees on both legs. The fee-free long tail (weather, many econ and mention markets, niche events) is the natural target for a retail MM.

### Gaps
- Could not download the current fee schedule PDF (HTTP 429), so there is no authoritative current list of maker-fee series. Pull `GET /series` (each has a fee type and multiplier) to build the list programmatically.

## 3. Evidence of retail and small market makers profiting; typical spreads and depth

### Takeaway
There is **no verified public P&L** from a retail Kalshi market-making bot. The GitHub ecosystem is mostly directional or AI-signal bots that disclaim profitability. Academic evidence shows **makers as a class do much better than takers** (about −10% vs about −32% average return in one study), but not that makers are net profitable, and maker vs taker is an order classification, not a user type. Measured spreads in liquid crypto markets are sub-cent with 3,000+ contracts at the touch, which leaves no room for retail there. Category-level spread and depth data for sports, politics or weather is not publicly available.

### Cited Findings
- *Makers and Takers: The Economics of the Kalshi Prediction Market* (Bürgi, Deng, Whelan; 300k+ contracts) finds a favorite-longshot bias. Makers are relatively well-informed but slightly over-optimistic. Per the CEPR/VoxEU summary, takers lose almost 32% on average and makers about 10%, and the bias is much stronger for takers on longshots — [ifo/CESifo working paper 2025](https://www.ifo.de/en/cesifo/publications/2025/working-paper/makers-and-takers-economics-kalshi-prediction-market); [2026 edition](https://www.ifo.de/en/cesifo/publications/2026/working-paper/makers-and-takers-economics-kalshi-prediction-market); [GWU PDF](https://www2.gwu.edu/~forcpgm/2026-001.pdf) (the PDF could not be text-extracted; figures are from the search summary of the VoxEU column, so verify)
- Kalshi disputes using maker/taker as a proxy for professional vs casual traders, after the Roosevelt Institute estimated $583.5M in retail losses from July 2021 to May 2026 — [Casino.org](https://casino.org/news/kalshi-rebuffs-think-tank-claim-regular-traders-lost-584-million-on-platform); [Kalshi blog](https://news.kalshi.com/p/debunking-bloombergs-kalshi-retail-loss-study)
- GitHub: ryanfrigo/kalshi-ai-trading-bot says no strategy is guaranteed and some examples lose money. OctagonAI/kalshi-trading-bot-cli and muxprotocol/kalshi-trading-bot are edge-taking or AI-ensemble bots, not MMs. rodlaf/KalshiMarketMaker (an Avellaneda-Stoikov style MM) is referenced by a Substack — [ryanfrigo repo](https://github.com/ryanfrigo/kalshi-ai-trading-bot); [Encyclopedia Autonomica, Feb 19, 2025](https://jdsemrau.substack.com/p/automated-market-making-on-kalshi) (paywalled; no P&L shown)
- Commercial bot sellers (Medium freelancer posts, "Predict & Profit" at $97+) provide no verified results — [Medium](https://medium.com/@zegham.ali/kalshi-trading-bot-automate-arbitrage-crypto-contracts-ai-market-making-8c23ad62e0ea); [PeerPush](https://peerpush.com/p/predict-and-profit)
- Kalshi BTC 15-min up/down (Aug 21, 2026, L2 replay of 97 windows): median top-of-book spread **0.82¢** (IQR 0.70–0.92¢), with sub-cent price levels quoted at the top. Median size at best bid/ask is **3,244 / 3,400** contracts. The book is two-sided about 94.7% of the time. The day had 2.95M trades, 239M contracts, $125.7M turnover and about 50.5M L2 events — [Cryptostruct](https://cryptostruct.com/guides/kalshi-vs-polymarket-data)
- Category depth claims conflict. Reviews say NFL, NBA and MLB books are tight. A bot guide says individual-game liquidity is thinner than politics or macro. No rigorous cross-category study was found — [Covers](https://www.covers.com/betting/prediction-sites/polymarket-vs-kalshi); [ClawArbs](https://clawarbs.com/blog/kalshi-vs-polymarket-arbitrage/)
- Sports are reportedly about 80% of Kalshi volume. Quant firms (SIG and others) run dedicated prediction-market desks — [Tradermath](https://www.tradermath.org/articles/prediction-markets-trading-at-quant-firms)
- Exchange scale: $52.98B in monthly volume in Sept 2026 (incomplete) vs $38.67B in August — [The Block](https://theblock.co/news/business/2026-09-30-kalshi-ends-trader-incentive-program-417247)
- A former Kalshi Trading MM sees the LIP as enabling "garage-band market makers", and suggests specializing where you have domain knowledge, quoting close with size on both sides and staying consistently present. He says snapshot farming (~0.1s flashes) catches only ~10% of snapshots and draws compliance risk — [UFO Holdings Substack](https://ufoholdings.substack.com/p/kalshis-new-liquidity-incentives)

### Inferences
- High-volume crypto and major-sports books are professionally quoted (sub-cent spreads, thousands of contracts at the touch). Retail would sit deep in the queue and get filled mostly when informed flow arrives. Edge, if any, lies in long-tail markets with wider spreads (several cents), no maker fee and an LIP pool, where large firms find the capacity too small.
- The −10% average maker return covers all makers, including directional limit-order users. It does not show that a disciplined two-sided quoter loses or wins.

### Gaps
- No Reddit, X or Discord first-hand retail MM P&L reports were found in searches (Reddit did not surface).
- No measured spread or depth statistics for weather, politics, econ or individual sports markets. These need to be collected via the API.

## 4. Risks: adverse selection, news jumps, inventory, rate limits, professional competition

### Takeaway
The dominant risk is **adverse selection on discrete jumps**. Binary contracts can gap from 50¢ to 0 or 100¢ on a single data release, score or injury. Quotes left resting through scheduled events are free options for faster traders. Inventory risk is unhedged binary exposure. Rate limits for a Basic account (about 10 writes/sec) are workable for a few markets but not for broad quoting. Professional MMs now share LIP pools and have fee and limit privileges.

### Cited Findings
- Adverse selection: if price-moving news hits and quotes don't move quickly, faster, better-informed traders pick them off. Injury and news risk is especially acute on the No side of player props — [UFO Holdings Substack](https://ufoholdings.substack.com/p/kalshis-new-liquidity-incentives)
- Event markets can be illiquid, spreads can widen, and pricing can move rapidly — [QuickNode builders guide](https://www.quicknode.com/builders-guide/tools/bot-for-kalshi-by-bot-for-kalshi)
- Retail makers face a speed problem: fair values move within minutes of news, and manual recalculation lags — [PillarLab guide](https://pillarlabai.com/blog/market-making-prediction-markets-guide/) (vendor blog, moderate trust)
- Rate limits are token buckets, and most requests cost 10 tokens. **Basic** (on signup) allows 200 read and 100 write tokens/sec, about 20 reads and 10 writes per second. **Advanced** (via the Upgrade Account API Usage Level endpoint) allows 300/300. Expert 600, Premier 1,200, Paragon 2,400, Prime 4,800 and Prestige 12,000/9,600 are earned by 30-day volume share: Expert earn/keep is 0.075%/0.05% of 2× the previous month's exchange volume. Order place, amend and cancel, order groups, RFQ quotes and block-trade accepts all use the write bucket — [Kalshi API docs – Rate limits](https://docs.kalshi.com/getting_started/rate_limits)
- At Sept 2026 volumes (about $53B/month), even Expert would need roughly $80M of 30-day volume (0.075% × 2 × 53B), out of reach for a small account — derived from [rate limits](https://docs.kalshi.com/getting_started/rate_limits) and [The Block](https://theblock.co/news/business/2026-09-30-kalshi-ends-trader-incentive-program-417247)
- A class action alleges Susquehanna is not financially independent of Kalshi (unproven allegation). Kalshi's terms disclose order protections that can advantage MMs — [The American Prospect, Aug 26, 2026](https://prospect.org/2026/08/26/house-always-wins-kalshi-prediction-markets/)
- Since July 30, 2026, the LIP clean terms no longer exclude Kalshi affiliates or members with Market Maker Agreements — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf)
- Compliance risk: the CRO can revoke LIP status for abusive participation. Rapid post and cancel patterns may draw scrutiny, and the current wash-trading controversy raises regulatory attention — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf); [The Block](https://theblock.co/news/business/2026-09-30-kalshi-ends-trader-incentive-program-417247)
- Program risk: Kalshi "may end the Program at any time", and the Volume Incentive Program is being ended on about two weeks' notice — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf); [Gambling.com](https://www.gambling.com/us/news/kalshi-end-volume-incentive-program-october-13)

### Inferences
- Practical mitigations: pull quotes ahead of scheduled releases (CPI, NFP, Fed) and during live games, or avoid live sports entirely. Use `cancel_order_on_pause`. Use order groups or expirations as a dead-man switch. Cap per-market inventory and skew quotes with inventory (Avellaneda-Stoikov). Quote small size near the touch only where a reliable fair-value anchor exists, such as weather models or sportsbook odds.
- At about 10 writes/sec on Basic, re-quoting both sides costs 2+ writes per update. A bot can actively manage perhaps 3–10 markets with sub-second responsiveness, or more if updates are infrequent.

### Gaps
- No quantified data on how much adverse selection retail makers suffer on Kalshi by category.
- The exact MM "order protections" were not read from the primary member agreement.

## 5. Practical API mechanics (order types, post-only, websocket, rate limits)

### Takeaway
Use the **V2 create-order endpoint** (`/portfolio/events/orders`). It takes a single YES-side book (`bid` or `ask`), fixed-point dollar prices with up to 4 decimals and sub-cent levels in some markets, and fractional counts (0.01 minimum). Required fields are `time_in_force` (GTC, IOC or FOK) and `self_trade_prevention_type`. Optional fields are `post_only`, `expiration_time`, `cancel_order_on_pause`, `order_group_id` and `reduce_only` (IOC only). The legacy `/portfolio/orders` endpoint was slated for deprecation no earlier than May 6, 2026.

### Cited Findings
- V2 fields: `ticker`; `side` (`bid` buys YES, `ask` sells YES); `count` (fixed-point string, 0.01 granularity); `price` (fixed-point dollars, 2–4 decimals in, up to 6 out, constrained by the market's price-level structure); `time_in_force` ∈ {fill_or_kill, good_till_canceled, immediate_or_cancel}; `expiration_time` (Unix seconds, used with GTC; "GTT" is not a valid value); `post_only` (boolean, behavior not described in the spec); `self_trade_prevention_type` ∈ {taker_at_cross, maker}; `cancel_order_on_pause`; `reduce_only` (IOC only); `subaccount`; `order_group_id`; `client_order_id`; `exchange_index` — [Kalshi API – Create Order V2](https://docs.kalshi.com/api-reference/orders/create-order-v2.md)
- The legacy endpoint `POST /trade-api/v2/portfolio/orders` (yes_price/no_price, count, post_only, etc.) will be deprecated no earlier than May 6, 2026 — [Kalshi API – Create Order (legacy)](https://docs.kalshi.com/api-reference/portfolio/create-order); [V2 docs](https://docs.kalshi.com/api-reference/orders/create-order-v2.md)
- Third-party guide: the legacy endpoint now expects dollar-string fields (`count_fp`, `yes_price_dollars`), and integer-cent bodies return 400 — [claudeskills.info Kalshi API skill](https://claudeskills.info/skills/agiprolabs/claude-trading-skills/kalshi-api/) (unverified; conflicts with the older official legacy reference)
- Kalshi publishes full-depth orderbooks via snapshot plus deltas, with no separate BBO stream, so the book must be rebuilt locally. Sub-cent top-of-book levels exist in some markets — [Cryptostruct](https://cryptostruct.com/guides/kalshi-vs-polymarket-data)
- Rate-limit tiers: see Section 4 — [Kalshi API docs – Rate limits](https://docs.kalshi.com/getting_started/rate_limits)

### Inferences
- Minimal MM stack: a websocket orderbook-delta and fill feed, plus REST V2 for orders. Use `post_only=true` to guarantee maker status and avoid taker fees. Use `self_trade_prevention_type=maker`. Use `cancel_order_on_pause=true`. Use an order group or short `expiration_time` as a kill-switch. Keep full price precision.
- Upgrade to the Advanced tier immediately; it is a free API call and triples the write budget.

### Gaps
- Official `post_only` semantics (reject vs reprice when crossing) were not found in the spec. Test in the demo environment.
- Websocket channel names and message rates were not fetched here; see docs.kalshi.com websocket section.
- Whether the API exposes LIP schedules per market (it was unanswered in 2025).

## 6. How well would a paper simulation of resting orders approximate real maker fills?

### Takeaway
A "fill when the book crosses my limit" paper simulator will be **systematically optimistic**. It ignores queue position behind thousands of contracts at the touch in liquid markets. It also misses adverse selection: real fills cluster exactly when the price is about to move against you, while "touch" fills in a naive sim are partly the benign ones. It still has value for **LIP reward estimation**, because rewards depend on resting size and position, not fills, and for long-tail markets with thin queues.

### Cited Findings
- Kalshi data is aggregated by price level (L2), so per-order queue position is not observable and must be modeled. With a median of about 3,000+ contracts at the touch in BTC 15-min markets, a new resting order would sit behind substantial size — [Cryptostruct](https://cryptostruct.com/guides/kalshi-vs-polymarket-data) (inference stated by the summarizer, based on the reported depth)
- Sub-cent top-of-book levels exist. A simulator that rounds to cents will misplace the touch — [Cryptostruct](https://cryptostruct.com/guides/kalshi-vs-polymarket-data)
- LIP scoring depends only on resting order size and distance from the Reference Price at random per-second snapshots, gated by both sides reaching the Target Size — [CFTC filing](https://www.cftc.gov/filings/orgrules/rules07152610358.pdf)

### Inferences
- Recommended sim design:
  1. **Queue-aware fills.** On order placement, record the size ahead at that price level. Decrement it only by traded volume at that price; cancellations ahead can be assumed pro-rata. Fill only once the queue ahead is consumed. Treat a price trading *through* the level as a full fill.
  2. **Fill only on trades, not on quote changes.** Use the trade/fill feed, not just book crossings.
  3. **Latency.** Add 100–500 ms for retail cloud latency on both placement and cancel, so that during jumps the sim leaves you resting and filled at stale prices.
  4. **Fees.** Charge per-series maker fees, rounded up per order.
  5. **Mark-out analysis.** Measure P&L of each simulated fill at +1s, +10s, +1min and at settlement to quantify adverse selection.
  6. **LIP accrual.** Recompute each market's Reference Price and qualifying set at random 1/sec snapshots, with your order inserted, and estimate your share of the posted daily reward.
- Validate the sim by running a tiny live bot (1–10 contracts) alongside it for 1–2 weeks, comparing live fill rate and mark-outs to the sim, and calibrating a haircut.
- In thin long-tail markets (few quoters, queue ahead often zero), the naive cross-to-fill sim is closer to reality. The main error there is adverse selection timing, not queue position.

### Gaps
- No published Kalshi-specific study comparing simulated vs realized maker fills. These recommendations are standard market-microstructure practice, not Kalshi-validated results.
