I used OpenAI Codex to adapt my lab code, check calculations and draft the documentation. I am responsible for the analysis, the checks and the investment decision.

This is an educational course project. It is not financial or investment advice.

# Committee decision

**Authorize a paper pilot.** Begin with 15% QQQ, 5% ONEQ, 15% VUG and 65% BIL. IEF and LQD receive zero. Require committee review before committing real money, after confirming loss tolerance and reviewing forward paper results after costs.

Decision information snapshot October 30, 2026. Mandate updated November 18, 2026 when Matt approved a 10% annual volatility ceiling. The model uses USD adjusted fund prices through September 30, 2026. Returns and risk are annual estimates.

| Portfolio | Gross estimate | First-year net | Annual volatility | BIL | Verdict |
|---|---:|---:|---:|---:|---|
| Equal weight | 7.494% | 7.494% | 12.138% | 16.67% | Fail — volatility exceeds 10% |
| Inverse volatility | 3.843% | 3.775% | 1.999% | 84.37% | Fail — net return below 7.49% |
| Constrained | 7.546% | 7.498% | 7.241% | 65.00% | Pass |

## Why pilot

The selected mix passes the return, risk and reserve rules, with estimated volatility below equal weight. However, its net return clears the target by only **0.80 basis points**. Moving 48.33% of the account at the assumed 10 bp switching cost deducts 4.83 bp from portfolio value. A $100,000 account would incur approximately $48.33.

The target originated in the same price history used to estimate returns. The equity funds are highly correlated. The CPI signal raises the required reserve to 10%, while the model independently chooses 65% BIL. This run supplies no evidence of a CPI timing advantage. These limitations support a paper trial.

## Locked cost test — November 19

The prediction was committed before changing switching cost from 10 to 15 bp. The selected portfolio passes with 15% QQQ, 10% ONEQ, 10% VUG and 65% BIL, net estimate 7.503% and annual volatility 7.245%. Risk rises only 0.004063 percentage points, below the predicted range. No pre-run reconsideration trigger fires, supporting continued pilot under Matt's stated rule. The approved base remains 10 bp and was restored. [Prediction, results and diagnosis](cost15-prediction-comparison.md).

## Range, monitoring and reversal

Across the 59-, 48- and 36-month estimation windows, the feasible mixes hold **65–85% BIL**, paired with **35–15% aggregate equities**. Each complete mix totals 100%. A 20-point move in BIL meets the committee-review trigger. The 90% minimum BIL stress produces no eligible portfolio.

**Reconsideration triggers clarified November 19:** reconsider the pilot if **any one** occurs: no mix passes at 15 bp switching cost; selected estimated annual volatility exceeds **9%**; BIL falls below **55%**; or the base case fails when the estimation window changes. These are review triggers and do not alter the model's hard constraints or the original locked prediction.

At each monthly review, check vintage availability, reserve, net return cushion, actual trading costs and fund overlap. Pause on missing or invalid source evidence or an infeasible mandate. Escalate a fund move of at least 20 points across windows. Continue on paper until the committee confirms suitability and reviews independently observed forward results after costs.

Estimated annual volatility is a statistical risk measure. The exercise has no realized forward record, maximum-loss guarantee, tax model or full market-impact model. Later rebalances must use actual holdings and measured costs.

[Computed base and stresses](../outputs/committee-run.json) · [Mandate](mandate.md) · [Source evidence](data-card.md) · [Validation](validation-and-ai-use.md)
