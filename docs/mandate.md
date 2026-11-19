I used OpenAI Codex to help implement and document the portfolio rules. I am responsible for the analysis and decision.

This is an educational course project. It is not financial or investment advice.

# Committee mandate

**Paper pilot approved by Matt.** Initial terms were approved November 16, 2026. Matt added a **10% maximum estimated annual volatility** on November 18. The app applies these rules to the October 30, 2026 information snapshot. This is a retrospective exercise under a subsequently approved mandate.

| Item | Rule and rationale |
|---|---|
| User and horizon | Committee considering a one-year ETF paper portfolio, annual scheduled rebalancing and monthly monitoring. |
| Universe | QQQ, ONEQ and VUG provide overlapping Nasdaq/growth equity exposure. BIL provides Treasury bills, IEF Treasury duration and LQD investment-grade credit. |
| Return objective | At least 7.49% estimated first-year return after initial switching costs. Matt selected the rounded original equal-weight historical mean. The target requires client confirmation because it is tied to this sample. |
| Risk limit | At most 10% estimated annual standard deviation, approved by Matt November 18. It measures dispersion and does not promise a maximum calendar-year loss. |
| Investment constraints | Fully invested, long only, no borrowing or derivatives. Each fund may be 0–100%. Five-percentage-point allocation grid. |
| Reserve | Only BIL qualifies. At least 3%, increasing to 10% when same-vintage annual CPI inflation is at least 3%. |
| Benchmark and starting holdings | Equal weight across the six funds. This policy reference can fail the mandate, which the app shows. |
| Second baseline | Inverse volatility, with weights proportional to each fund’s inverse estimated volatility. |
| Cost | 10 bp per dollar switched from equal weight. One-way turnover is half the absolute weight changes. The charge covers the two trading legs together and is deducted once. |
| Decision rule | Among eligible mixes, choose the lowest estimated volatility. Stop if none qualifies. |
| Monitoring | Monthly review of source availability, net cushion, actual costs, overlap and reserve. Refer a move of at least 20 percentage points in any fund across windows to the committee. |
| Funded allocation | Requires confirmed client loss tolerance, review of suitability and observed forward paper results after costs. |

## Pilot reconsideration triggers — clarified November 19

Matt confirmed that **any one** of these conditions triggers reconsideration of the pilot: no mix passes at 15 bp switching cost; selected estimated annual volatility is above **9%**; BIL weight is below **55%**; or the base case fails when the estimation window changes. The conditions are joined by **OR**.

The 9% volatility and 55% BIL levels are review triggers, distinct from the existing 10% volatility hard limit and reserve constraint. They do not change the optimization inputs. The original pre-run record retains its earlier 50% BIL condition.

## Assumption register

| Value | Label | Reason |
|---|---|---|
| 59 monthly returns at base; 48 and 36 in window tests | History | Uses the archived five-year price panel and checks sensitivity to its length. |
| Annual mean = monthly arithmetic mean × 12 | Estimate | Transparent historical estimate. It can be unstable as a forward return input. |
| Annual sample covariance = monthly sample covariance × 12 | Estimate | Uses joint returns from the same complete months. |
| 7.49% target | Student judgment | Matt selected the original six-fund average for the course pilot. Its similarity to equal weight is mechanical. |
| 10% volatility ceiling | Student judgment | Matt’s stated acceptable maximum annual volatility. Client suitability remains to be confirmed before funding. |
| 3% reserve; 10% after the 3% inflation trigger | Student-approved judgment | Preserves liquidity for committee review of real spending needs. No predictive advantage has been demonstrated. |
| 10 bp switching charge | Student-approved judgment | Illustrative cost assumption, stressed separately. Actual execution must be measured. |
| Equal-weight initial holdings | Student-approved judgment | Provides a transparent common starting point for comparing transaction costs. |

The October 30 information date and November mandate approval have different roles. An actual forward record begins only after the committee freezes the process.

[Source data](data-card.md) · [Decision memo](decision-memo.md)
