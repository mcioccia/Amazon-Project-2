I used OpenAI Codex to prepare this code walkthrough and verify its displayed source excerpts. The analysis and decision are mine.

This is an educational project, not financial or investment advice.

# Video 2 — Code walkthrough and recording guide

Updated November 19, 2026. **Draft narration, not an actual transcript.** 527 words. Aim for **4:25–4:45** including clicks; hard maximum **5:00**. Rehearse your actual pace before recording.

## Open and prepare

1. Open `Video-2-Dashboard.html` in your Project 2 folder, or [the local preview](http://127.0.0.1:8507/Video-2-Dashboard.html) while the preview server is running. This is a saved code walkthrough; Video 3 is the live app demonstration.
2. Click **Reset** then **Full screen**. Start on **Inputs**. The source excerpts and line numbers come directly from the current Python files; skipped lines are explicitly marked. Click any source line to highlight it while explaining. **Full source** opens the complete file in a dialog for rehearsal; it is not a required timed click.
3. In OBS, capture this browser window, turn on your microphone and webcam, and place the webcam over the reserved box on the right. Keep your face visible for the whole recording. The box itself does not turn on a camera.
4. Open the [word-for-word spoken script](video-2-word-for-word-script.md) on a second screen or print it. Only read the spoken paragraphs; do not read click instructions. Use **Show script** during rehearsal, then hide it for the final take.
5. Record a short audio/face/readability check. Turn off notifications. Start OBS recording, then click **Start rehearsal** and read the first disclosure immediately. The dashboard timer does not record or advance the scenes.

## Exact click route

Click the next named tab after finishing the current passage. Right Arrow and **Next →** follow the same route. The times are rehearsal targets, not measured recording timestamps.

| Target time | Click | Point at |
|---|---|---|
| 0:00–0:40 | **Inputs** | Point to FUNDS, AS_OF and BASE, then the fingerprint check. |
| 0:40–1:15 | **Returns** | Point to current / prior − 1, then mean × 12 and stdev × √12. |
| 1:15–1:45 | **Risk** | Trace correlation × volatility × volatility, both weights, and the square root. |
| 1:45–2:20 | **CPI cutoff** | Point to ≤ cutoff, max eligible vintage, year-over-year change, and max reserve floor. |
| 2:20–2:55 | **Costs** | Point to absolute weight changes ÷ 2, bp ÷ 10,000, cost, then net. |
| 2:55–3:45 | **Search** | Trace weights → net → continue → risk → continue → best. Click a line to highlight it. |
| 3:45–4:25 | **Verdict** | Point to input-error stop, the no-mix warning, displayed results and exported settings. |

## Say exactly

### 0:00–0:40 · Inputs

**Click:** Inputs. **Point:** Point to FUNDS, AS_OF and BASE, then the fingerprint check.

**Say exactly:**

I used OpenAI Codex to build, test, and help explain this app. The analysis and decision are mine.

This is an educational project, not financial or investment advice.

I'll trace the actual code from prices to the portfolio verdict. These six funds are the universe. The base sets a 7.49 percent net return target and a ten percent volatility ceiling. The information cutoff is October thirtieth; the mandate approval came later. This is a retrospective paper exercise. The fingerprint check refuses an undocumented change to the saved data.

### 0:40–1:15 · Returns

**Click:** Returns. **Point:** Point to current / prior − 1, then mean × 12 and stdev × √12.

**Say exactly:**

Here, current price divided by prior price, minus one, gives a monthly return. My checked QQQ example goes from 716.01 to 739.77, about 3.32 percent. Sixty prices give 59 returns. The code annualizes the average by multiplying by twelve, and sample standard deviation by the square root of twelve. It estimates correlations over the same months. These are historical estimates, not promised returns.

### 1:15–1:45 · Risk

**Click:** Risk. **Point:** Trace correlation × volatility × volatility, both weights, and the square root.

**Say exactly:**

Correlation times both volatilities gives covariance. The next block multiplies every covariance by both portfolio weights and adds all the pairs, including each fund with itself. The square root gives portfolio volatility. Funds that move together can add similar risk, even with different tickers. The base is 7.241 percent. The ten percent ceiling limits this estimate; it does not guarantee a maximum loss.

### 1:45–2:20 · CPI cutoff

**Click:** CPI cutoff. **Point:** Point to ≤ cutoff, max eligible vintage, year-over-year change, and max reserve floor.

**Say exactly:**

The CPI function first removes archived vintages after the cutoff, then selects the latest eligible one. Both index levels come from that same vintage. September inflation is 3.72 percent. That activates the ten percent BIL floor instead of the normal three percent minimum. Missing eligible evidence pauses the search. The date is the archived vintage, not a claim about the first release time. At base, 65 percent BIL already exceeds this floor.

### 2:20–2:55 · Costs

**Click:** Costs. **Point:** Point to absolute weight changes ÷ 2, bp ÷ 10,000, cost, then net.

**Say exactly:**

Starting holdings are equal weight. One-way turnover is half the sum of absolute weight changes, so the buy and sell sides are not counted twice. The base switches 48.333 percent. Ten basis points becomes 0.001. Multiply turnover by that rate and a hundred-thousand-dollar account: 48 dollars and 33 cents. Subtract the cost from gross expected return. This is the initial switch; it does not cover every future expense.

### 2:55–3:45 · Search

**Click:** Search. **Point:** Trace weights → net → continue → risk → continue → best. Click a line to highlight it.

**Say exactly:**

The loop distributes twenty units across six funds. Each unit is five percentage points, so weights add to one hundred percent without shorting. For each candidate, it calculates return, reserve, costs, and risk. Continue skips a failing mix. The best variable changes only when an eligible mix has lower volatility. Of 53,130 candidates, 655 pass at base. This is the best mix on the grid, not every possible allocation. My fifteen-basis-point test reran this whole search. It moved five points from VUG to ONEQ and produced 7.245 percent volatility.

### 3:45–4:25 · Verdict

**Click:** Verdict. **Point:** Point to input-error stop, the no-mix warning, displayed results and exported settings.

**Say exactly:**

The app displays the engine's results and exports the actual settings with the output. Equal weight fails the risk ceiling; inverse volatility misses the return target. The constrained mix passes, but its return cushion is thin. Requiring ninety percent BIL leaves no eligible mix, so the app says pause. Invalid input evidence also stops the app. Forty-three published training checks passed, and the cost test was independently recalculated. I still recommend a paper pilot, with forward results and the stated review triggers before funding.

## Finish and submit

After the final sentence, stop OBS before 5:00. Your face must stay visible throughout. Replay the recording to check readable code, audio and actual runtime. Upload it to YouTube as Unlisted, publish corrected captions, and check the link while signed out. Send the actual video link and exported captions for correction; the completed transcript belongs at `docs/transcript-video-2.txt`. Do not rename this rehearsal script as the recorded transcript.

The video should show you explaining how the code works. Each screen includes a financial interpretation, source lines and a calculated result. Do not claim that volatility caps losses, that the grid explores every possible weight, or that the archived vintage is the first release timestamp.

## Evidence and reproducibility

[Base and stresses](../outputs/committee-run.json) · [Locked test result](../outputs/cost15-changed.json) · [Personal source/calculation check](student-evidence.md) · [Training reconciliation](training-reconciliation.md) · [Point-in-time data card](data-card.md) · [Manifest](manifest.md)

`build_video2.py` rebuilds this dashboard, narration and guide from saved results and current source excerpts. It does not change model assumptions, financial source files or the locked prediction. The source fingerprints in `outputs/video2-presentation-sources.json` identify the displayed implementation.

[Project 2 directions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md) · [Length and submission checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md)
