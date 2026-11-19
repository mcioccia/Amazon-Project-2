I used OpenAI Codex to adapt my lab code, check calculations and draft the documentation. I am responsible for the analysis, the checks and the investment decision.

This is an educational course project. It is not financial or investment advice.

# Portfolio committee · Project 2

**Decision requested — authorize a paper pilot.** Track 15% QQQ, 5% ONEQ, 15% VUG and 65% BIL under a 7.49% net return objective, 10% annual volatility ceiling and CPI-dependent reserve floor. Monthly monitoring and forward results after costs are required before considering funding.

| Portfolio | Net estimate | Annual volatility | Verdict |
|---|---:|---:|---|
| Equal weight | 7.494% | 12.138% | Fail — exceeds 10% risk limit |
| Inverse volatility | 3.775% | 1.999% | Fail — below return target |
| Constrained | 7.498% | 7.241% | Pass |

Information snapshot October 30, 2026. Prices end September 30. The mandate was updated November 18 when Matt approved the risk ceiling. These are historical estimates in a retrospective paper exercise.

[Decision memo](docs/decision-memo.md) · [Visible output](outputs/committee-run.json) · [Sources](docs/data-card.md) · [Validation](docs/validation-and-ai-use.md) · [Submission manifest](docs/manifest.md)

## Run the app

Requires Python 3.12. Internet access is needed for the initial package install. All financial input data is included.

1. On GitHub choose **Code → Download ZIP** and extract it, or clone the repository. If the private repository shows a 404, sign in with the account invited by Matt and accept the invitation.
2. Open a terminal in the extracted folder containing **app.py** and **requirements.txt**.
3. On Windows PowerShell, run these commands once to install the environment.

~~~powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
~~~

Start the app with this one command.

~~~powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
~~~

Open the Local URL printed in the terminal on the same computer. Keep the terminal running. If a port is busy, add --server.port 8506. For later sessions, open the same folder and run the app command again.

On macOS or Linux create the environment with python3.12 -m venv .venv, then use .venv/bin/python for installation and launch.

If Python 3.12 is unavailable, install it from [python.org](https://www.python.org/downloads/) and reopen the terminal. If requirements.txt cannot be found, change into the extracted repository folder before running the install command.

## Reach the decision

- **Decision** compares both baselines with the constrained mix, shows every failed rule and charts return against risk.
- **Stress results** holds the original base fixed and changes one assumption per row. Window changes re-estimate all means and covariance.
- **Calculations** traces prices into estimates and explains portfolio volatility, one-way turnover and net return.
- **Sources & timing** shows CPI observation and vintage dates, fund download timestamps and the input fingerprints.
- **Validation** displays the published training reconciliation and evidence still requiring Matt’s personal work.
- **Mandate** states the approved rules and remaining suitability limits.

Changing a sidebar control reruns the current scenario. **Reset to approved base** restores every control. **Download this scenario** exports the current settings and output. The saved standard stresses remain comparisons to the approved base.

At base the metrics are 7.498%, 7.241%, +0.80 bp and 65% BIL. Selecting 36 monthly returns gives 85% BIL. Requiring 90% BIL pauses allocation. Reset afterward.

## Reproduce the evidence

~~~powershell
.\.venv\Scripts\python.exe analysis.py
.\.venv\Scripts\python.exe reconcile.py
.\.venv\Scripts\python.exe verify.py
~~~

analysis.py prints the current base record without writing over saved evidence. Use --help for scenario options. reconcile.py writes the published training results. verify.py independently recomputes the allocation grid and checks failures and app interactions.

The source ledger fingerprints the archived inputs. The app refuses an undocumented file change. Review and document legitimate source revisions before updating their fingerprints.

## Record Video 1

Open **Video-1-Dashboard.html** from your downloaded Project 2 folder. It runs locally without additional dependencies and presents saved results. Read the [324-word, word-for-word spoken script](docs/video-1-word-for-word-script.md). Keep the [separate click guide](docs/video-1-recording-guide.md) beside it: Decision → What changed → My checks → Locked test → Reproduction → Pilot conditions. Use Show script for rehearsal, hide it for recording, and keep your actual webcam visible in the reserved space. Target 2:40–2:50; maximum 3:00. The dashboard timer does not record video. Matt reports Video 1 is recorded. The [corrected transcript](docs/transcript-video-1.txt) and [YouTube caption file](docs/captions-video-1-corrected.srt) are prepared from his supplied SRT; see the [correction review and upload steps](docs/video-1-caption-review.md). The YouTube link, final playback review, actual runtime and access check remain pending.

[Dashboard preview](docs/evidence/video1-dashboard-preview.jpg) · [Presentation checks](outputs/video1-review.txt)

## Submission status

Software and recorded numerical checks are complete for this revision. The [15 bp prediction and result](docs/cost15-prediction-comparison.md) are saved with a pre-run commit and restored baseline. Personal source-verification status, the highest-risk claim and three failures, final video links/transcripts, instructor access and the remaining partner-run metadata and control-change evidence remain tracked in the [manifest](docs/manifest.md). Every video requires a visible webcam image. Video 3 starts with the live app. Record after the mandate and thesis are finalized.

[Feedback resolution](docs/feedback-resolution.md) · [Personal evidence](docs/student-evidence.md) · [Partner reproduction](docs/cold-run.md)
