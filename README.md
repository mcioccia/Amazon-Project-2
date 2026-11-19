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

1. On GitHub choose **Code → Download ZIP** and extract it, or clone the repository. The repository is public and was checked while signed out on November 19, 2026.
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
- **Validation** displays the published training reconciliation and personal source, prediction and reproduction evidence.
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

## Videos and transcripts

| Video | Published video | Runtime / limit | Repository transcript |
|---|---|---|---|
| 1 — How the process and thinking changed | [Watch Video 1](https://youtu.be/e79Ix9xr71k) | 2:36 / 3:00 | [Transcript](docs/transcript-video-1.txt) |
| 2 — Code walkthrough | [Watch Video 2](https://youtu.be/YfrNEF4OK6g) | 4:32 / 5:00 | [Edited transcript](docs/transcript-video-2.txt) |
| 3 — Committee presentation | [Watch Video 3](https://youtu.be/9RYrqkSZCaw) | 4:11 / 5:00 | [Edited transcript](docs/transcript-video-3.txt) |

All three videos are Unlisted and passed signed-out access checks on November 19. Webcam images are visible at their openings; Video 3 opens on the live app. Full narration and continuous face visibility have not been independently reviewed. YouTube captions remain unavailable as of the final audit. Videos 2 and 3 have disclosed numerical edits in the written transcripts; these do not establish that the corresponding audio was corrected. Video 3's supplied SRT needs its opening aligned. See the [Video 1](docs/video-1-caption-review.md), [Video 2](docs/video-2-caption-review.md) and [Video 3](docs/video-3-caption-review.md) correction records.

## Submission status

The November 19 [readiness audit](docs/submission-readiness.md) reran the financial and app checks successfully. The approved base and standard stresses match saved output. The source check, calculator evidence, unchanged pre-run prediction, later result and partner fresh-download report are recorded. The repository is public and readable without signing in.

**Remaining before submission:** resolve material spoken/caption discrepancies, publish synchronized YouTube captions with transcripts enabled, complete one full playback review, and attach the required Markdown files and links in Brightspace. Partner run details and a numerical clarification in the personal reflection are identified separately as ways to strengthen the evidence. The audit is not a grade guarantee.

[Submission manifest](docs/manifest.md) · [Feedback response](docs/feedback-resolution.md) · [Personal evidence](docs/student-evidence.md) · [Partner reproduction](docs/cold-run.md)
