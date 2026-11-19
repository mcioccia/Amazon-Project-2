OpenAI Codex executed the requested test, checked the calculations and prepared this comparison. Matt supplied the pre-run prediction and decision conditions; the analysis and decision remain his responsibility.

Educational purposes only. Not financial or investment advice.

# Switching cost: 10 bp to 15 bp — prediction versus result

**The 15 bp allocation passes.** Volatility rises slightly to 7.244616%, below Matt's 7.7% central forecast and his 7.3–8.6% subjective range. The allocation moves five percentage points from VUG to ONEQ and keeps 65% BIL. None of Matt's stated reconsideration conditions fires, so his pre-run decision rule continues to support a paper pilot. This is the application of his recorded rule, not a new personal post-run statement from him.

## Sequence and unchanged inputs

- [Original prediction commit](https://github.com/mcioccia/Amazon-Project-2/commit/ed8b8f9829c95249d369d99120ef4b40b47f86b4): 2026-11-19T00:41:21-05:00.
- Original [prediction text](https://github.com/mcioccia/Amazon-Project-2/blob/ed8b8f9829c95249d369d99120ef4b40b47f86b4/docs/prediction-15bp-before-run.md) is preserved unchanged.
- Changed run began 2026-11-19T00:43:53.395026-05:00 and finished 2026-11-19T00:43:53.903116-05:00, America/New_York.
- GitHub's remote was checked before execution; the prediction commit was an ancestor of execution revision 6ffd81ad19068e14a797ddd455dc8a0595b85d09.
- Only cost per dollar switched changed: 10 bp (0.10%) to 15 bp (0.15%). Fixed: 7.49% net target, 10% volatility ceiling, 3% BIL control, existing CPI rule (effective floor 10%), 59 returns, zero QQQ shift, zero additional lag, six funds, equal-weight starting holdings, five-point allocation grid and the same source files.
- This is a November 19 test of the October 30 information snapshot under the mandate updated November 18. It uses no new market data.

Actual changed-run command from the Project 2 folder:

~~~powershell
..\Lab_14\.venv\Scripts\python.exe -B analysis.py --target 7.49 --reserve 3 --window 59 --cost-bp 15 --qqq-shift 0 --lag 0 --vol-limit 10
~~~

Use the Python environment created by the README on another computer; the full executed command and interpreter path are retained in the run record.

## Before and after

Changes below are **percentage points**, except the explicitly labeled basis-point and dollar rows.

| Measure | Base: 10 bp | Changed: 15 bp | Signed change |
|---|---:|---:|---:|
| Gross annual return estimate | 7.546368% | 7.575849% | +0.029482 pp |
| First-year net return estimate | 7.498034% | 7.503349% | +0.005315 pp |
| Estimated annual volatility | 7.240553% | 7.244616% | +0.004063 pp |
| BIL weight | 65.000000% | 65.000000% | +0.000000 pp |
| One-way turnover | 48.333333% | 48.333333% | +0.000000 pp |
| Switching cost / portfolio value | 0.048333% | 0.072500% | +0.024167 pp |
| Net return cushion above 7.49% | 0.803417 bp | 1.334928 bp | +0.531511 bp |
| Cost on a USD 100,000 illustration | USD 48.33 | USD 72.50 | USD +24.17 |
| Feasible allocations | 655 | 636 | -19 allocations |
| Mandate verdict | PASS | PASS | Both pass |

| Fund | Base weight | Changed weight | Signed change |
|---|---:|---:|---:|
| QQQ | 15% | 15% | +0 pp |
| ONEQ | 5% | 10% | +5 pp |
| VUG | 15% | 10% | -5 pp |
| BIL | 65% | 65% | +0 pp |
| IEF | 0% | 0% | +0 pp |
| LQD | 0% | 0% | +0 pp |

## Prediction compared with the result

| Matt's locked prediction | Result | Assessment |
|---|---|---|
| Volatility rises from about 7.241% | 7.240553% to 7.244616% | Direction correct; increase only 0.004063 pp |
| Central volatility forecast 7.7% | 7.244616% | Actual minus prediction: -0.455384 pp; rise was overestimated |
| Subjective 80%-likely range: 7.3–8.6% | Actual below 7.3% | Outside the stated range |
| A feasible mix remains | 636 mixes qualify | A feasible mix was found |
| BIL falls below 65% or equities are rearranged | BIL stays 65%; ONEQ rises 5 pp and VUG falls 5 pp | Equity-rearrangement branch occurred |
| Pilot continues if valid, subject to his triggers | Pass; no trigger fires | Consistent with the pre-run pilot decision |

One outcome cannot validate or calibrate the stated 80% probability or the below-10% probability of infeasibility. These remain personal pre-run judgments.

## Why the result differed in magnitude

1. **The old mix does fail at the higher cost.** Holding its weights fixed, turnover stays 48.333333%. The extra five basis points per dollar switched cost 0.024167 percentage points of portfolio value, taking its net estimate to 7.473868%, below 7.49%. This supports the prediction that the old return cushion was insufficient.

2. **The replacement changes the equity composition, not the BIL allocation.** ONEQ's annual mean estimate in the fixed sample is 14.257756% versus VUG's 13.668121%. Moving five points from VUG to ONEQ adds 2.948178 bp to gross portfolio return. Extra cost is 2.416667 bp, leaving a net increase of 0.531511 bp after reoptimization. Higher transaction cost lowers return for a fixed trading mix; it need not lower the return of the newly selected mix.

3. **Turnover does not fall.** It stays 48.333333%. The improvement comes from a higher gross return estimate with nearly unchanged covariance-based risk, not from reducing the dollars switched. The base and changed mixes both leave BIL above its initial equal weight and every other fund below its initial equal weight, so one-way turnover remains the same.

4. **The predicted large risk increase was unnecessary.** The total equity share stays 35%, and the five-point substitution changes annualized estimated volatility by only 0.004063 pp. A small input change and a five-point grid do not require a large risk jump.

5. **Pure equity is not a feasible fallback under this mandate.** The effective BIL floor is 10%, so an all-equity mix fails the reserve rule regardless of return or volatility. The actual 65%-BIL allocation establishes feasibility. This corrects that part of the reasoning in the after-run diagnosis; the original prediction remains untouched.

## Decision triggers

| Pre-run reconsideration condition | Observed result | Triggered? |
|---|---|---|
| No mix at 15 bp | 636 eligible mixes | No |
| Selected volatility above 9% | 7.244616% | No |
| BIL below 50% | 65% | No |

The result supports continuing the **paper pilot** under Matt's stated conditions. The net cushion is still only 1.33 bp, and this test does not resolve estimation uncertainty or establish forward performance. It does not change the approved 10 bp base assumption or authorize a live trade.

## Retained output and checks

- [10 bp before](../outputs/cost15-base-before.json)
- [15 bp after](../outputs/cost15-changed.json)
- [Restored 10 bp base](../outputs/cost15-base-restored.json)
- [Run times, commands, input hashes, signed changes and independent check](../outputs/cost15-run-record.json)

All three commands exited successfully. The original saved base was reproduced, only cost changed, source hashes matched, and the final base rerun matched the initial base exactly. An independent calculation from the prices and a separate enumeration of all 53,130 mixes reproduced the 655 base and 636 changed eligible counts, both winning allocations and their financial metrics.

The model, data, original prediction and saved committee base were not changed.
