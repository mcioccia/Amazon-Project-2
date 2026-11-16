# Committee mandate

The student selected QQQ, ONEQ, VUG, BIL, IEF and LQD, a 7.49% annual expected return target, a 3% minimum invested in BIL, and a pilot until the allocation holds up across estimation windows. The target was the rounded equal-weight historical average in Lab 15. It is sample-dependent. Its near-equality to the benchmark is mechanical.

**Proposed pilot terms requiring committee confirmation.** The intended user is a committee evaluating a diversified ETF reserve in a paper account. Use a one-year evaluation horizon, annual scheduled rebalancing and monthly monitoring. Use an equal-weight, annually reset portfolio of the same six funds as the policy benchmark. Inverse volatility is the second baseline. Start the modeled transition from equal weights. The current reference holdings are an assumption, not an observed account.

| Rule | Implementation |
|---|---|
| Eligible assets | QQQ and ONEQ provide overlapping Nasdaq exposure, VUG adds growth equity, BIL represents Treasury bills, IEF represents Treasury duration and LQD investment-grade credit. Only BIL qualifies for the reserve. |
| Position limits | Fully invested, weights sum to 100%, long only, no borrowing or derivatives. Each fund may range from 0% to 100%. No tighter single-fund or look-through issuer cap has been confirmed. |
| Return | The proposed cost convention applies 7.49% to the first-year estimate after modeled transition costs. The prior lab applied it gross. The app displays both. |
| Reserve | BIL must meet the larger of the mandate floor and the point-in-time CPI floor. |
| Risk | Minimize annualized sample portfolio standard deviation among feasible five-percentage-point allocations. No numerical maximum loss or volatility has been supplied. Real-money adoption awaits client loss tolerance. |
| Turnover and liquidity | Report one-way turnover and cost. No separate hard turnover cap has been supplied. ETF liquidity beyond the BIL reserve, taxes, settlement stress and market impact are outside the model. |
| Control | Pause on infeasibility, missing eligible CPI data or invalid prices. Refer any window-to-window fund move of at least 20 points to the committee. |

The 60/40 benchmark and issuer rules in the Lab 13 fictional Meridian exercise belong to that case. The student's own-client fields in Lab 13 were blank. These proposed terms make the course pilot operable and need the student's review.

AI-use disclosure: OpenAI Codex assisted with software, analysis and writing. Educational purposes only. Not financial or investment advice.