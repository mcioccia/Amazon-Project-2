I used OpenAI Codex to adapt my lab code, test the calculations, and draft this walkthrough. The analysis, the checks, and the decision are mine.

This is an educational course project. It is not financial or investment advice.

# Video 2 · Code walkthrough

**Recording requirement.** Keep your face visible in a webcam overlay throughout, with your microphone on. Place it clear of the key numbers. This November 18 draft reflects the approved 10% volatility ceiling. Correct the transcript from your actual final recording.

Record the browser window showing [the code dashboard](../Video-2-Dashboard.html) with your microphone. Open it locally, choose **Full screen**, and start at **Inputs**. Keep this guide on a second screen or on paper. Use → to advance and N to toggle narration during rehearsal. The timing is a rehearsal target of 4:25. The course maximum is 5:00.

## 0:00–0:30 · Inputs

**Show** [analysis.py](../analysis.py). Read both disclosures aloud. Point to the fund list and the decision date.

**Say**

I used OpenAI Codex to adapt my lab code, test the calculations, and draft this walkthrough. The analysis, the checks, and the decision are mine.

This is an educational course project. It is not financial or investment advice.

I’ll trace one decision from the price file to the verdict on screen. The six tickers are the investments the model can choose from. The date matters just as much. It sets the boundary on what the committee could have known.

## 0:30–1:12 · Returns

**Show** [portfolio.py](../portfolio.py). Point to current divided by prior, then to the factors 12 and the square root of 12.

**Say**

Start with QQQ. Its adjusted close moved from about 374.74 to 382.22. The code divides the second price by the first and subtracts one. That gives about a two percent return for that month. Sixty month-end prices give me 59 changes. For each fund I multiply the average monthly return by twelve. For volatility I multiply the sample standard deviation by the square root of twelve. Those are annual estimates based on history.

## 1:12–1:55 · Risk

**Show** [portfolio.py](../portfolio.py). Point to the two volatility factors, then the two portfolio weights in the sum.

**Say**

Owning two funds doesn’t necessarily diversify me very much. If they tend to rise and fall together, they can carry much of the same risk. The first block multiplies their correlation by both volatilities to get covariance. The second weights each pair by how much of each fund I own and adds up those contributions. Taking the square root gives me the volatility of the whole mix. That’s the risk measure the search tries to minimize.

## 1:55–2:38 · CPI cutoff

**Show** [analysis.py](../analysis.py). Point to the cutoff comparison, the latest eligible vintage, and the 3% trigger.

**Say**

September is the month this number measures. October 28 is the vintage that was available by our October 30 decision. I filter out later vintages first. Then I compare September with the same month a year earlier, using both index levels from that vintage. Inflation was 3.72 percent. That crossed my three percent trigger, so the effective minimum in Treasury bills went from three percent to ten. If no eligible vintage exists, the model pauses.

## 2:38–3:36 · Search

**Show** [portfolio.py](../portfolio.py). Follow one candidate from its weights to its net return. Point to continue and the volatility comparison.

**Say**

The search distributes twenty five-percent units across six funds. For each mix it calculates the gross return and BIL weight, then deducts the cost of switching from equal weight. A mix drops out if it misses the net return target, the reserve floor or my ten percent volatility ceiling. Of 53,130 mixes, 655 survive all three limits. The code keeps the eligible mix with the lowest estimated volatility.

## 3:36–4:25 · Verdict

**Show** [app.py](../app.py). Point to the net metric and comparison table call. Finish on the warning branch and your decision.

**Say**

The app shows the engine’s result. Our chosen mix has a 7.498 percent estimated net return, 7.241 percent volatility, and 65 percent in BIL. Equal weight fails the risk limit, and inverse volatility fails the return target. The export now saves these actual controls and results. If I require 90 percent BIL, no mix qualifies. The app displays a pause, which is a decision the committee needs to see.

## After recording

Upload to YouTube with an instructor-accessible link. Enable captions and correct the transcript against what you actually said. Check BIL, QQQ, covariance, basis points, and numerical values. Save the corrected transcript as **docs/transcript-video-2.txt**. Enter the YouTube URL, actual runtime, actual chapter timestamps and transcript link in the [submission manifest](manifest.md). Check access before submission.

[Saved committee run](../outputs/committee-run.json) · [Calculation checks](../outputs/verification.txt) · [Course video checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md)
