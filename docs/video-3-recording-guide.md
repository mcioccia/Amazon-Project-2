I used OpenAI Codex to prepare this live-app presentation and verify the click route against the running app. The analysis and decision are mine.

This is an educational project, not financial or investment advice.

# Video 3 — Live committee presentation

Updated November 19, 2026. **Draft narration, not a transcript of a recorded video.** 475 spoken words. Aim for **4:35–4:50 including clicks**, with a hard maximum of **5:00**. The live app must be visible from the first frame; keep your face visible throughout.

[Read every word of the spoken script](video-3-word-for-word-script.md). This guide contains the separate click instructions and the same spoken paragraphs. The numbers in the narration are spelled out to help you read them accurately.

## Before recording

1. Open the running [live app](http://127.0.0.1:8506/) in your normal browser and maximize the window. Use a wide desktop window; expand the browser if the in-app preview is narrow. Record **app.py's Streamlit app**, not either saved Video 1 or Video 2 HTML dashboard.
2. Click **Reset to approved base**, then **Decision**. Put your pointer over the main content and scroll to the very top so the title, disclosures and opening metrics are visible. Main-content scrolling and sidebar scrolling are separate.
3. Check all seven sidebar values: target **7.49**, risk ceiling **10**, minimum BIL **3**, returns window **59**, cost **10**, QQQ shift **0**, signal delay **0**. The effective BIL floor is **10%** because of CPI even though the sidebar's normal minimum is **3%**.
4. Confirm the opening metrics: **7.498% net, 7.241% volatility, +0.80 bp cushion, 65% BIL**. If they differ, do not read the expected results over a different screen; reset and investigate.
5. In OBS, use Window Capture for this browser and add your microphone and actual webcam. Put the webcam in unused space near the upper right, above the dark decision banner, and check that it does not cover the sidebar, metric cards, table or tabs. Move it only if needed for visibility. Keep your face visible for the entire video.
6. Keep the spoken script and this click guide on paper or a second screen. Record a short sample to check readable numbers, sound and face visibility. Turn off notifications.
7. Start OBS recording **with the live app already visible**, then read the two opening disclosures. There is no slide timer or Next button in this live app. Use OBS's elapsed recording time and the tab/sidebar route below.

The app is currently running at the link above. If it has stopped, this is the verified local environment on Matt's laptop; keep the terminal open:

~~~powershell
cd "C:\Users\mac10\finance-ai-work\Project 2"
..\Lab_14\.venv\Scripts\python.exe -m streamlit run app.py --server.port 8506 --server.address 127.0.0.1 --server.headless true
~~~

A stranger uses the environment/startup command in the README.

## Exact live click route

Change only the named input. For a number field, click its value, press **Ctrl+A**, type the new value, then **Enter**. Wait for the result before reading the result sentence. For the window control, select **36** from the drop-down.

| Time target | Action | Result to verify |
|---|---|---|
| 0:00–0:40 | Start on **Decision** at the approved base. | 7.498% / 7.241% / +0.80 bp / 65% BIL |
| 0:40–1:15 | Scroll to **Mandate verdicts**, then **Allocation by fund**. | Equal weight FAIL; inverse volatility FAIL; constrained PASS. Base BIL 65%, QQQ 15%, ONEQ 5%, VUG 15%. |
| 1:15–1:45 | Scroll up to the tabs → **Sources & timing**. | Measured September 2026; archived vintage October 28; cutoff October 30; CPI 3.717%; effective BIL minimum 10%. |
| 1:45–2:30 | **Decision** → **Cost per dollar switched (bp): 10 → 15**, Enter. | 7.503% / 7.245% / +1.33 bp / 65% BIL. ONEQ and VUG now 10% each. |
| 2:30–3:15 | **Reset to approved base → Decision** → **Monthly returns in estimate: 59 → 36**. Then **Stress results**, scroll to window bars. | Cost back to 10; 7.528% / 2.576% / +3.85 bp / 85% BIL. Saved 48-month and 36-month bars both show 85% BIL. |
| 3:15–3:40 | **Reset to approved base → Decision** → **Minimum BIL (%): 3 → 90**, Enter. | Window back to 59, cost 10. **No eligible allocation. Pause allocation.** |
| 3:40–4:35 | **Reset to approved base** → **Mandate**, scroll to **Pilot reconsideration triggers — clarified November 19**. Finish by returning to **Decision**. | Current triggers: ANY ONE of no mix at 15 bp, risk above 9%, BIL below 55%, or window-change failure. End with original base metrics. |

**Reset matters:** without it, the window test would also carry the higher cost, and the stop case would also carry the shorter window. Do not change the target or risk ceiling to force a pass. The 15 bp result is a live repeat of a test already recorded in the repository; it is not a new pre-run prediction.

## Word-for-word passages with click cues

### 0:00–0:40 · Open on the live decision

**Click / point:** Before recording: click Reset to approved base, then Decision. Keep the live app visible from the first frame. Start OBS and read both disclosures. Point to Pilot on paper and the four metrics.

**Expected screen:** 7.498% net · 7.241% volatility · +0.80 bp cushion · 65% BIL.

**Say exactly:**

I used OpenAI Codex to build, test, and help explain this app. The analysis and decision are mine.

This is an educational project, not financial or investment advice.

I'm asking the committee to authorize a one-year paper pilot, with annual rebalancing and monthly reviews. This live app uses an October thirtieth historical snapshot under the mandate approved later. The base passes, but its expected return cushion is less than one basis point.

### 0:40–1:15 · Compare the baselines and allocation

**Click / point:** Stay on Decision. Scroll the main page to Mandate verdicts; point to both FAIL rows and the Constrained PASS. Scroll slightly farther to Allocation by fund and its Constrained bar. Keep the sidebar untouched.

**Expected screen:** Equal weight: 7.494% net, 12.138% volatility, FAIL. Inverse volatility: 3.775% net, 1.999% volatility, FAIL. Base weights: QQQ 15%, ONEQ 5%, VUG 15%, BIL 65%, IEF 0%, LQD 0%.

**Say exactly:**

Equal weight is my benchmark and starting account. It fails the ten percent volatility ceiling. Inverse volatility lowers risk but misses the return target. The constrained portfolio passes.

My proposed starting allocation is sixty-five percent BIL, fifteen percent QQQ, five percent ONEQ, and fifteen percent VUG. IEF and LQD receive zero. The equity funds overlap, so the fund count overstates diversification.

### 1:15–1:45 · Show the information boundary

**Click / point:** Scroll back up to the tab row and click Sources & timing. Point to the measured month, selected archived vintage, cutoff and CPI formula. Do not change the sidebar.

**Expected screen:** Measured 2026-09; returned vintage 2026-10-28; cutoff 2026-10-30; CPI 3.717% on screen (3.72% rounded); effective BIL minimum 10.0%.

**Say exactly:**

The signal uses September inflation from an archived vintage available by the cutoff. Inflation of about three point seven two percent raises the BIL minimum from three to ten percent. The model already holds sixty-five percent, so this run does not demonstrate a CPI timing advantage. I also checked two QQQ prices against Yahoo and verified the monthly return myself.

### 1:45–2:30 · Rerun the locked cost test live

**Click / point:** Click Decision. In the sidebar, click the numeric value under Cost per dollar switched (bp), press Ctrl+A, type 15, and press Enter. Wait for 7.503% before speaking about the result. Point to risk and BIL; scroll to Allocation by fund if needed to show ONEQ and VUG at 10% each.

**Expected screen:** Only cost changes: 10 → 15 bp. 7.503% net · 7.245% volatility · +1.33 bp cushion · 65% BIL. QQQ 15%, ONEQ 10%, VUG 10%, BIL 65%.

**Say exactly:**

Now I'm increasing switching cost from ten to fifteen basis points, leaving every other input fixed. This repeats my saved test; the prediction was committed before the original run.

The mix still passes. Volatility is seven point two four five percent, below my predicted range. Five percentage points move from VUG to ONEQ, while BIL stays at sixty-five percent. Reoptimization raises gross expected return enough to offset the extra cost. That supports a cautious pilot; future performance remains uncertain.

### 2:30–3:15 · Test a shorter estimation window

**Click / point:** Click Reset to approved base, then Decision. Confirm cost is back to 10. Open Monthly returns in estimate and choose 36. Wait for 7.528%, then point to 85% BIL. Click Stress results and scroll to the 59-, 48- and 36-month allocation bars.

**Expected screen:** Only window changes: 59 → 36 returns. 7.528% net · 2.576% volatility · +3.85 bp cushion · 85% BIL. Stress results always compares each saved scenario with the approved base.

**Say exactly:**

I've reset the base, including costs. Now I use thirty-six monthly returns. BIL rises to eighty-five percent. The forty-eight-month result also holds eighty-five percent.

Across these complete mixes, the range is sixty-five to eighty-five percent BIL, paired with thirty-five to fifteen percent equities. That twenty-point move triggers committee review. A different window changes all estimated means and covariance. The target also came from this historical sample, so I want it confirmed independently.

### 3:15–3:40 · Demonstrate a real stop

**Click / point:** Click Reset to approved base, then Decision. Confirm window 59 and cost 10. In Minimum BIL (%), select the numeric value, press Ctrl+A, type 90, and press Enter. Wait for the warning and Pause allocation heading.

**Expected screen:** No eligible allocation. Pause allocation. The current proposal has no constrained weights or performance metrics; do not read the earlier numbers as the stopped scenario.

**Say exactly:**

I've restored the base again. Now I require ninety percent BIL. No mix meets all the rules, so allocation pauses. I would bring the conflicting requirements back to the committee instead of lowering the target just to force an answer.

### 3:40–4:35 · Close on your conditions

**Click / point:** Click Reset to approved base. Confirm the base metrics return. Click Mandate, then scroll to Pilot reconsideration triggers — clarified November 19 while reading the four conditions. Scroll back to the tabs and click Decision for the final sentence.

**Expected screen:** Current review triggers use OR: no mix at 15 bp; selected volatility above 9%; BIL below 55%; base fails a window change. These are review thresholds, not replacements for the 10% hard risk ceiling. Finish on base Decision.

**Say exactly:**

My decision remains a paper pilot. Any one of these makes me reconsider: no mix passes at fifteen basis points, estimated volatility exceeds nine percent, BIL falls below fifty-five percent, or the base fails after a window change.

I'll monitor source availability, costs, the return cushion, and fund overlap monthly. Missing evidence or an infeasible mandate stops the process. Estimated volatility does not cap actual losses. Before funding, I want confirmed client loss tolerance and forward results after costs. My committee request is approval to track the base allocation on paper.

## Important distinctions for this recording

- The 9% volatility and 55% BIL levels are your **review triggers**, not new hard constraints. Keep the model's 10% volatility ceiling and 3% normal BIL minimum unchanged.
- The range 65–85% BIL is paired with 35–15% aggregate equity across specific complete mixes; do not treat the two ranges as independently selectable allocations.
- The **Stress results** tab shows standard one-input changes from the approved base, even while current sidebar settings differ. The **Decision** tab shows the currently selected controls.
- CPI 3.717% on screen rounds to 3.72% in the script. A data vintage does not establish an intraday publication time.
- A missing/infeasible result is a real stop. The 90% BIL case has no proposed constrained allocation to describe.

## After recording

Stop OBS within 5:00. Review the actual recording for visible face, readable controls/numbers, audio, and restored base at the end. Upload to YouTube as Unlisted, publish captions that match the recording, and check the link while signed out. Send the actual link and SRT for review. Save the completed transcript as docs/transcript-video-3.txt and update the manifest with actual duration and timestamps. This rehearsal script must not be presented as an already-recorded transcript.

[Decision memo](decision-memo.md) · [Mandate](mandate.md) · [Saved base/stresses](../outputs/committee-run.json) · [Original cost prediction and comparison](cost15-prediction-comparison.md) · [Live-route verification](../outputs/video3-review.txt) · [Manifest](manifest.md)

[Project 2 directions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md) · [Course video checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md)
