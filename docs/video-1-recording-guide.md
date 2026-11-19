I used OpenAI Codex to build, test, and help explain this app and prepare this recording guide. The analysis and decision are mine.

This is an educational project, not financial or investment advice.

# Video 1 — How my process and thinking changed

Updated November 19, 2026. **Draft script, not a transcript of a recorded video.** 324 spoken words; aim for **2:40–2:50**, with a hard limit of **3:00**. The subject follows the [Project 2 Video 1 directions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md): how the system and thinking changed, and an AI output checked. [Length checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md).

Read every word in the [word-for-word spoken script](video-1-word-for-word-script.md). That file contains only what you say aloud, with no headings or click instructions to read. The same words appear under **Say exactly** below and in the dashboard's **Show script** panel. Use this guide separately for when to click.

## Before recording

1. Open **Video-1-Dashboard.html** from the Project 2 folder in a browser. It runs directly from the extracted folder, with no server or internet needed for the dashboard and local screenshots. GitHub's file page shows its source; download the repository first.
2. Maximize the browser. A local preview is also available at http://127.0.0.1:8507/Video-1-Dashboard.html while the preview server is running. To restart it from Project 2, use the command below. On another computer use the Python environment installed through the README.
3. Click **Reset**, then **Full screen** if available. If absent, use the browser's full-screen control.
4. In your recording software select this browser window or display, turn on your microphone, and enable your actual webcam. Place its overlay inside the reserved **Your webcam here** box on the right. The box is only reserved space, not a camera feed.
5. Keep your face visible throughout. Turn off notifications. Check a short sample recording for clear speech and readable numbers.
6. Rehearse with **Show script** (or N). It follows the selected screen. Before the final take, click **Hide script** and use this guide on a second screen or paper.
7. Start your recorder first. With **Decision** selected, click **Start rehearsal** to start the dashboard timer and begin speaking. The dashboard does not record video or advance automatically.

~~~powershell
..\Lab_14\.venv\Scripts\python.exe -m http.server 8507 --bind 127.0.0.1
~~~

## Exact click route

Click the named tab after finishing its passage. Right Arrow or **Next →** advances the same route. Target times are rehearsal guidance, not the measured video duration.

| Target time | Click | What to point at |
|---|---|---|
| 0:00–0:25 | **Decision** | Point to Paper pilot, then the 65% BIL allocation. |
| 0:25–0:50 | **What changed** | Point to the two failing baselines, then the constrained row. |
| 0:50–1:15 | **My checks** | Point to the two QQQ prices, the calculator result, then the $48.33 check. |
| 1:15–1:55 | **Locked test** | Trace the commit → run → result sequence. Point to 7.7% predicted and 7.245% actual, then the two allocation bars. |
| 1:55–2:15 | **Reproduction** | Point to the 43 checks, then AJ's fresh-download report. |
| 2:15–2:50 | **Pilot conditions** | Point to the 65% → 85% window change, then ANY ONE and the four review triggers. |

On **Pilot conditions**, finish the last sentence and stop your recorder before 3:00. Correct a wrong click by selecting the named tab. Use **Reset** between takes.

**Evidence** and source-image buttons are optional during rehearsal, not required clicks in the timed take. Close images with **Close image** or Escape; close the evidence list with **Close evidence** or Escape.

## Spoken script and screen cues

### 0:00–0:25 · Decision

**Click:** Decision. **Point:** Point to Paper pilot, then the 65% BIL allocation.

**Say exactly:**

I used OpenAI Codex to build, test, and help explain this app. The analysis and decision are mine.

This is an educational project, not financial or investment advice.

I recommend a paper pilot. My process now includes costs, risk limits, source checks, and a prediction recorded before testing.

### 0:25–0:50 · What changed

**Click:** What changed. **Point:** Point to the two failing baselines, then the constrained row.

**Say exactly:**

Lab 15 found a low-risk mix meeting return and reserve targets. I added switching costs, a ten percent volatility limit, and point-in-time CPI.

Equal weight fails the risk limit. Inverse volatility misses the return target. My mix passes, with a very thin return cushion.

### 0:50–1:15 · My checks

**Click:** My checks. **Point:** Point to the two QQQ prices, the calculator result, then the $48.33 check.

**Say exactly:**

I checked the AI-prepared QQQ inputs against Yahoo: 716.01 in August and 739.77 in September. My calculator gave a 3.32 percent monthly return, and both adjusted prices matched to the cent.

My separate trading-cost check also matched: 48 dollars and 33 cents on a hundred-thousand-dollar account. The evidence is saved.

### 1:15–1:55 · Locked test

**Click:** Locked test. **Point:** Trace the commit → run → result sequence. Point to 7.7% predicted and 7.245% actual, then the two allocation bars.

**Say exactly:**

Before the run, I committed my prediction for a cost increase from ten to fifteen basis points. I expected volatility around 7.7 percent.

Actual volatility was 7.245 percent, below my predicted range. The app moved five percentage points from VUG to ONEQ and kept BIL at 65 percent.

The higher gross return offset the extra cost. My direction was right, but I overestimated the risk change. I learned to check the new allocation, not just the higher fee.

### 1:55–2:15 · Reproduction

**Click:** Reproduction. **Point:** Point to the 43 checks, then AJ's fresh-download report.

**Say exactly:**

All forty-three published training checks passed. Independent calculations confirmed the cost test, and the base reset matched.

AJ Chapman reported a fresh download worked in fifteen minutes, with matching results and no problems. His exact commit and changed-control evidence remain unspecified.

### 2:15–2:50 · Pilot conditions

**Click:** Pilot conditions. **Point:** Point to the 65% → 85% window change, then ANY ONE and the four review triggers.

**Say exactly:**

My confidence increased, but I still recommend a paper pilot. Shorter windows move BIL from 65 to 85 percent. The target also comes from the estimation history.

Any one condition makes me reconsider: no mix passes at fifteen basis points, volatility exceeds nine percent, BIL falls below 55 percent, or the base fails after a window change. I want forward evidence before funding.

## Final recording check

- Read both opening disclosures. Keep your face visible throughout.
- Use the **locked prediction 7.7%**, actual test volatility **7.245%**, and current **55% BIL** review trigger. The original 50% pre-run trigger remains historical evidence; 55% was clarified afterward.
- The source check samples observations and arithmetic; it does not verify every price or future performance.
- AJ's fresh-download success is reported. Missing version and changed-control details remain visible.
- The 55% and 9% levels prompt reconsideration. Existing model hard constraints are unchanged.
- This dashboard presents saved results. Video 3 separately opens with the Streamlit app running live.
- After recording, upload to YouTube, correct a transcript from what you actually said, save it as docs/transcript-video-1.txt, and enter the actual URL, runtime, chapters and access status in the manifest. Do not submit this draft as though it were the recorded transcript.

## Evidence

[Base output](../outputs/committee-run.json) · [Source and calculator evidence](student-evidence.md) · [Locked prediction](prediction-15bp-before-run.md) · [Cost comparison](cost15-prediction-comparison.md) · [Training reconciliation](training-reconciliation.md) · [Partner report](cold-run.md) · [Current conditions](highest-risk-claim.md)

The dashboard is generated from saved results by build_video1.py. Rerunning it changes presentation files, not the financial model or original prediction.
