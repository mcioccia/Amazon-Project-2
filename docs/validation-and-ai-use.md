# Validation and AI use

AI-use disclosure: OpenAI Codex assisted with software, analysis and writing. Educational purposes only. Not financial or investment advice.

**Evidence date.** Built November 16, 2026 using the October 30 historical decision snapshot. See [data card](data-card.md) for sources, units and both vintage dates. The baseline and stressed numbers are estimates from archived inputs. No live client account, realized performance or genuinely untouched holdout is claimed. A forward paper record must begin after the committee freezes the process.

**Finance checks.** Run `python verify.py`. It estimates an independent sample covariance from monthly returns, enumerates 53,130 portfolios using a separate stars-and-bars algorithm, deducts the same assumed costs, and verifies the winner, risk and feasible count. It verifies equal weight independently, re-creates Lab 15's gross base allocation at zero cost, checks the exact CPI ratio with the same-vintage denominator, rejects a missing price month, and exercises the app under feasible, infeasible and missing-vintage conditions. [Executed verification](../outputs/verification.txt)

**Cost convention.** First-year net estimate = weighted annual gross estimate − switching cost × one-way turnover. One-way turnover = half the absolute weight changes from equal weight. The illustrative 10 bp charge applies once per dollar switched and includes both trading legs together. At subsequent rebalances use actual starting holdings and observed costs before making any funding decision. No tax, ongoing advisory fee or recurring multi-period performance is modeled.

**Standard stresses already run.** [Full inputs and outputs](../outputs/committee-run.json). Each row changes one setting from base. The QQQ shift changes just its annual mean. Window changes re-estimate all means and covariances. The cost shock reprices the transition for every mix before testing feasibility. The reserve shock changes eligibility. The vintage lag selects a prior information set. The target stays fixed. None of these completed runs is eligible for a new blind prediction.

| Stress | Observed consequence |
|---|---|
| QQQ annual mean −1 percentage point | QQQ moves to 25%, ONEQ to 10%, VUG to 0%, BIL stays at 65%. |
| Last 36 returns | 10% QQQ, 5% VUG and 85% BIL. |
| Last 48 returns | 5% QQQ, 10% VUG and 85% BIL. |
| Switching cost 50 bp | 25% QQQ, 5% ONEQ, 5% VUG, 65% BIL. |
| BIL minimum 90% | No feasible allocation. Committee must pause. |
| Vintage delayed 30 calendar days | August replaces September as the latest measured month. Base weights persist. |

**AI use.** OpenAI Codex, November 16, 2026, adapted the Lab 15 estimator/search, proposed the committee benchmark and cost-aware pilot terms, extracted the Lab 17 CPI vintages, built the interface, wrote verification code and drafted the committee documents. Matt previously selected the six ETFs, objective, reserve, and conditional pilot. Lab 19's NVIDIA business screens are supplementary company research. They do not estimate ETF returns or set ETF weights.

**Student check to record personally.** Use the CPI values or the turnover calculation in the memo, recompute it independently and record your calculation, source, finding and date here. Automated independent code verification appears above. Personal check: pending.

## Locked Changed-Input Record — student completes

Close AI, choose **one new input change whose output you have never seen**, and write the first group of fields below. Keep other inputs at base. Commit and push this file to your GitHub repository **before** running the scenario. The pre-run commit must contain your own prediction. The built-in stresses, the 90% and missing-vintage demonstrations, and previously observed lab runs cannot serve as fresh predictions.

| Before run · fill with AI closed | Your entry |
|---|---|
| Base decision and all held-fixed settings | |
| One input, old and new values, units | |
| Predicted direction for a named output and decision effect | |
| Economic reasoning | |

After the pre-run commit is visible on GitHub, add its permanent commit link below. Run exactly that scenario in the app or with `python analysis.py --help` to see the command options. Save the actual result, commit it separately and retain both commits.

| After run | Your entry |
|---|---|
| Pre-run GitHub commit URL and timestamp | |
| Run time, exact settings, and output evidence link | |
| Actual value, units and direction versus base | |
| Did the portfolio verdict or committee decision change? | |
| Why it matched, failed or stayed unchanged | |
| Post-run commit URL | |
