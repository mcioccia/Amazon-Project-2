I used OpenAI Codex to adapt and test the software, document sources and draft this record. I am responsible for the analysis, the personal checks and the investment decision.

This is an educational course project. It is not financial or investment advice.

# Validation and AI use

Updated November 18, 2026. This exercise uses an October 30 historical information snapshot under a mandate approved later. The 10% annual volatility ceiling was approved November 18.

## Executed checks

Run python verify.py after installing requirements.txt. Independent arithmetic estimates sample covariance from monthly returns and enumerates 53,130 portfolios with a separate stars-and-bars construction. It compares the winning weights, volatility and 655 eligible mixes with the production search. Both baseline verdicts are checked, including equal weight’s failure of the new risk ceiling.

The published reconciliation uses the actual portfolio engine for Labs 14 and 15 and independently computes the Week 2 financial mini-case. All 43 comparisons pass at the stated published precision. Invalid correlation matrices, missing months anywhere in the panel, invalid weights, invalid risk limits and duplicate CPI dates are refused. Missing trailing CPI observations are handled explicitly. A 90% BIL floor pauses allocation. A missing eligible vintage pauses the search. The app tests cover changed controls and restoring the full base.

The scenario download captures its actual settings and result. Source fingerprints identify the input bytes used. Base and standard-stress results are reproduced and retained.

[Verification](../outputs/verification.txt) · [Training reconciliation](training-reconciliation.md) · [Automated source comparison](../outputs/source-check.json) · [Reproduction record](cold-run.md)

## Cost and economic limits

First-year net estimate equals gross estimate minus switching-cost rate times one-way turnover. Turnover is half the absolute weight changes from equal weight. The assumed 10 bp applies to each dollar switched and covers both trading legs together. It is deducted once. Later rebalances need actual holdings and measured execution costs. Taxes, ongoing advisory fees and market impact are outside this calculation.

Historical means are estimates. The target was selected from the original equal-weight historical average, creating a mechanical near-match. QQQ, ONEQ and VUG overlap substantially. The CPI floor is slack at base, providing no demonstrated timing advantage. A statistical volatility ceiling cannot promise a maximum loss. A forward paper record begins after the process is frozen.

## Material AI use

OpenAI Codex assisted with Lab 15 code reuse, the committee terms initially proposed and approved by Matt, documentation, validation, source retrieval, interface design and recording guides. The November 18 revision was prompted by Project 1 feedback. Matt supplied the 10% risk ceiling and reported his partner’s calculation question and startup commands. Product identification is OpenAI Codex; an exact underlying model build was not exposed in the saved project evidence.

The 25 bp practice prediction below was authored with AI. Matt's own highest-risk claim, three possible failures and fresh AI-off prediction remain pending. For the load-bearing source check, Matt supplied two QQQ Yahoo screenshots on November 18. Codex transcribed August 31 Adj Close of 716.01 and September 30 Adj Close of 739.77 (USD per share), which match the archived inputs to the displayed cent precision. Original images and fingerprints are retained in [Personal evidence](student-evidence.md#source-check). Matt then supplied calculator-input and result screenshots: (739.77 / 716.01 - 1) x 100 = 3.31838940797%, or +3.32%. Codex verified this arithmetic; the full-precision archive gives 3.31782706792%, also +3.32% when rounded. The small difference follows from rounding the price inputs. The formula was supplied by Codex and executed by Matt; this is separate from the AI-off prediction. Access-date confirmation and Matt's interpretation remain pending.

[Personal evidence](student-evidence.md)

**Matt's independent calculation check (November 16, 2026).** I got $48.33 for the base trading cost on a $100,000 portfolio. At 48.33% one-way turnover, I would switch $48,330. At 10 basis points (0.10%) per dollar switched, the cost is $48,330 × 0.001 = **$48.33**. The model uses unrounded turnover and also gives $48.33 to the nearest cent. [Base run, constrained portfolio](../outputs/committee-run.json)

## Locked Changed-Input Record

Complete the before-run fields yourself with AI closed. Choose one new input change whose output you have not seen. Commit and push this record before running that exact scenario. Keep other inputs at the stated base. Retain the before and after output and commit the outcome separately.

The current base is target 7.49% net, volatility ceiling 10%, BIL minimum 3% before the CPI rule, 59 monthly returns, switching cost 10 bp per dollar switched, QQQ shift 0 percentage points and signal delay 0 days.

| Before run | Matt’s entry |
|---|---|
| One input, old and new values, units | Pending |
| All held-fixed inputs | Pending |
| Expected direction for a named numerical output | Pending |
| Expected committee-decision effect | Pending |
| My economic reasoning | Pending |
| Pre-run commit URL and timestamp | Pending |

| After run | Matt’s entry |
|---|---|
| Run time and exact command or app settings | Pending |
| Base and changed output links | Pending |
| Actual output and signed change, with units | Pending |
| Did my decision change? | Pending |
| Why the result matched or differed, or stayed unchanged | Pending |
| Separate post-run commit URL | Pending |

The saved standard stresses and the completed 25 bp practice scenario have already been observed. They do not supply a fresh blind prediction.

## Historical 25 bp AI-assisted practice

This practice occurred November 16 under the earlier mandate with no numerical volatility ceiling. Its original output is retained for attribution.


GitHub contained the [pre-run prediction](https://github.com/mcioccia/Amazon-Project-2/commit/337b7ff05b30530c148bfa30aba5245db50669b2) before execution. The commit timestamp was 2026-11-16T20:23:31Z. The practice run began at 2026-11-16T20:28:51.569937+00:00. Only switching cost changed, from 10 to 25 basis points per dollar switched. [Saved output](../outputs/switching-cost-25bp-practice.json).

The lowest-risk feasible portfolio moved from a first-year net estimate of 7.498034% to 7.505646% (+0.761 bp). The actual result differed from the predicted decline. Gross return changed from 7.54637% to 7.63481%, while modeled trading cost changed from 0.04833% to 0.12917%. The difference between those changes explains the observed net direction after reoptimization.

New weights: QQQ 15%, ONEQ 20%, VUG 0%, BIL 65%, IEF 0%, LQD 0%. The portfolio verdict is **PASS**. The practice result supports keeping the existing paper-pilot decision. This scenario is AI-assisted. The separate AI-off record remains pending.
