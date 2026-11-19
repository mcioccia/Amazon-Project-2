I used OpenAI Codex to adapt and test the software, document sources and draft this record. I am responsible for the analysis, the personal checks and the investment decision.

This is an educational course project. It is not financial or investment advice.

# Validation and AI use

Updated November 19, 2026. This exercise uses an October 30 historical information snapshot under a mandate approved later. The 10% annual volatility ceiling was approved November 18.

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

The 25 bp practice prediction below was authored with AI. Matt supplied his [highest-risk claim, three failures and conclusion](highest-risk-claim.md) on November 19 after receiving the 15 bp result. His wording is retained; separate notes distinguish the 7.6% statement from actual 7.244616% volatility and the revised 55% BIL condition from the earlier 50% trigger. Matt confirmed that any one of his four conditions triggers reconsideration; this later clarification is recorded separately from the locked prediction. On November 19, Matt supplied the [new 15 bp prediction](prediction-15bp-before-run.md), retained without rewriting and committed before execution. The [15 bp comparison](cost15-prediction-comparison.md) records the November 19 result and diagnosis. For the load-bearing source check, Matt supplied two QQQ Yahoo screenshots on November 18. Codex transcribed August 31 Adj Close of 716.01 and September 30 Adj Close of 739.77 (USD per share), which match the archived inputs to the displayed cent precision. Original images and fingerprints are retained in [Personal evidence](student-evidence.md#source-check). Matt then supplied calculator-input and result screenshots: (739.77 / 716.01 - 1) x 100 = 3.31838940797%, or +3.32%. Codex verified this arithmetic; the full-precision archive gives 3.31782706792%, also +3.32% when rounded. The small difference follows from rounding the price inputs. The formula was supplied by Codex and executed by Matt; this is separate from the AI-off prediction. Access-date confirmation and Matt's interpretation remain pending.

[Personal evidence](student-evidence.md)

**Matt's independent calculation check (November 16, 2026).** I got $48.33 for the base trading cost on a $100,000 portfolio. At 48.33% one-way turnover, I would switch $48,330. At 10 basis points (0.10%) per dollar switched, the cost is $48,330 × 0.001 = **$48.33**. The model uses unrounded turnover and also gives $48.33 to the nearest cent. [Base run, constrained portfolio](../outputs/committee-run.json)

## Locked Changed-Input Record

Complete the before-run fields yourself with AI closed. Choose one new input change whose output you have not seen. Commit and push this record before running that exact scenario. Keep other inputs at the stated base. Retain the before and after output and commit the outcome separately.

The current base is target 7.49% net, volatility ceiling 10%, BIL minimum 3% before the CPI rule, 59 monthly returns, switching cost 10 bp per dollar switched, QQQ shift 0 percentage points and signal delay 0 days.

| Before run | Matt’s entry |
|---|---|
| One input, old and new values, units | Switching cost 10 bp to 15 bp per dollar switched; supplied wording in [section 1](prediction-15bp-before-run.md) |
| All held-fixed inputs | [Section 2 and execution context](prediction-15bp-before-run.md); all other base settings and input files unchanged |
| Expected direction for a named numerical output | Matt's exact forecast is retained in [section 3](prediction-15bp-before-run.md) |
| Expected committee-decision effect | Matt's exact decision and reconsideration conditions are retained in [section 4](prediction-15bp-before-run.md) |
| My economic reasoning | [Section 5](prediction-15bp-before-run.md), preserved without correcting the prediction |
| Pre-run commit URL and timestamp | [Locked prediction commit ed8b8f9](https://github.com/mcioccia/Amazon-Project-2/commit/ed8b8f9829c95249d369d99120ef4b40b47f86b4) · 2026-11-19T00:41:21-05:00 (America/New_York); pushed and remote verified before the November 19 15 bp execution. |

| After run | Matt’s entry |
|---|---|
| Run time and exact command or app settings | 15 bp run: 2026-11-19T00:43:53.395026-05:00; exact command and fixed settings in [comparison](cost15-prediction-comparison.md) and [run record](../outputs/cost15-run-record.json) |
| Base and changed output links | [10 bp before](../outputs/cost15-base-before.json), [15 bp after](../outputs/cost15-changed.json), [10 bp restored](../outputs/cost15-base-restored.json) |
| Actual output and signed change, with units | Annual volatility 7.240553% to 7.244616% (+0.004063 pp); net 7.498034% to 7.503349% (+0.005315 pp); BIL 65% unchanged |
| Did my decision change? | Applying Matt's pre-run conditions supports continued pilot: a mix exists, volatility is below 9%, and BIL is above 50%. This is the recorded-rule assessment, not an invented personal post-run statement. |
| Why the result matched or differed, or stayed unchanged | Volatility rose as predicted but below the 7.3–8.6% range. Five points moved from VUG to ONEQ; BIL and turnover stayed fixed. Gross estimate gain exceeded added cost. Full [after-run diagnosis](cost15-prediction-comparison.md) prepared by Codex. |
| Separate post-run commit URL | [Results commit 0e42306](https://github.com/mcioccia/Amazon-Project-2/commit/0e4230638481a93bdcf86394db007ad5f111e922) · 2026-11-19T00:46:51-05:00 (America/New_York), pushed after execution |

The saved standard stresses and the completed 25 bp practice scenario have already been observed. They do not supply a fresh blind prediction.

## Historical 25 bp AI-assisted practice

This practice occurred November 16 under the earlier mandate with no numerical volatility ceiling. Its original output is retained for attribution.


GitHub contained the [pre-run prediction](https://github.com/mcioccia/Amazon-Project-2/commit/337b7ff05b30530c148bfa30aba5245db50669b2) before execution. The commit timestamp was 2026-11-16T20:23:31Z. The practice run began at 2026-11-16T20:28:51.569937+00:00. Only switching cost changed, from 10 to 25 basis points per dollar switched. [Saved output](../outputs/switching-cost-25bp-practice.json).

The lowest-risk feasible portfolio moved from a first-year net estimate of 7.498034% to 7.505646% (+0.761 bp). The actual result differed from the predicted decline. Gross return changed from 7.54637% to 7.63481%, while modeled trading cost changed from 0.04833% to 0.12917%. The difference between those changes explains the observed net direction after reoptimization.

New weights: QQQ 15%, ONEQ 20%, VUG 0%, BIL 65%, IEF 0%, LQD 0%. The portfolio verdict is **PASS**. The practice result supports keeping the existing paper-pilot decision. This scenario is AI-assisted. The separate November 19 prediction and its executed 15 bp result are retained above.


## Video 1 transcript correction — November 19, 2026

OpenAI Codex corrected the SRT supplied by Matt for finance terms, ticker symbols, attribution and recognition errors, retained his **my partner** wording, and checked material numbers against saved output. Matt confirmed the script wording for two unclear passages. The [correction record](video-1-caption-review.md) separates text checking from playback checks not yet performed. [Original captions](evidence/video-1-original.srt), [corrected captions](captions-video-1-corrected.srt) and [transcript](transcript-video-1.txt) are retained. The original prediction, financial model, saved results and rehearsal script were not changed.


On November 19, Codex checked the [published Video 1](https://youtu.be/e79Ix9xr71k) in a signed-out browser. The title was PROJECT 2 VID 1 FINAL, duration 2:36, and visibility Unlisted. Brief playback and opening webcam visibility passed; full-video audio and continuous webcam review were not performed. YouTube reported captions unavailable, so publishing the corrected caption file remains outstanding. See the [access check](video-1-caption-review.md#published-video-access-check--november-19-2026).


## Video 2 preparation — November 19, 2026

OpenAI Codex prepared the [word-for-word draft](video-2-word-for-word-script.md), [click guide](video-2-recording-guide.md) and source-code recording dashboard. The generator reads actual source lines and saved outputs; all displayed excerpts were checked against their files. The approved base rerun matched its archive, and a 90% BIL floor returned no eligible mix. [Presentation review](../outputs/video2-review.txt) records UI checks and limitations; [source fingerprints](../outputs/video2-presentation-sources.json) identify the code displayed. No model inputs, archived results or locked prediction text changed. This draft is not an actual recording transcript; the actual video and corrected transcript remain pending.


## Video 2 caption review — November 19, 2026

Codex compared the supplied SRT with the script and saved results and prepared [review drafts](video-2-caption-review.md). Original cues and timings are retained, and the source SRT is archived unchanged. Three possible spoken-versus-caption errors (decision date, basis-point conversion and passing-mix count) require Matt’s playback confirmation. Drafts use the correct script/model values but are not certified transcripts. No model inputs or archived results were changed.

Matt subsequently confirmed at least one spoken error. A short recording-correction guide is saved; no corrected audio, final transcript or revised caption timing is claimed yet.
