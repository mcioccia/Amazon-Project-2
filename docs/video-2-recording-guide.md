I used OpenAI Codex to adapt my lab code, test the calculations, and draft this walkthrough. The analysis, the checks, and the decision are mine.

This is an educational course project. It is not financial or investment advice.

# Video 2 · Code walkthrough

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

Each unit is five percent of the portfolio. The search distributes twenty units across six funds, so the weights add up to one hundred percent. For each mix it calculates gross return and the BIL weight. Then it deducts ten basis points on the dollars switched from equal weight. A mix that misses either the net return target or the reserve minimum hits continue and drops out. Of 53,130 possible mixes, 15,294 survive. Among those, the code keeps the mix with the lowest estimated volatility.

## 3:36–4:25 · Verdict

**Show** [app.py](../app.py). Point to the net metric and comparison table call. Finish on the warning branch and your decision.

**Say**

The app takes the constrained result from the engine. It shows 7.498 percent estimated net return, 7.241 percent annual volatility, and 65 percent in BIL. It also shows the comparison table so the committee can see which baselines passed. Our mix clears the return target by just 0.80 basis points. Raise the BIL minimum to 90 percent and no mix qualifies. That warning tells me to pause. With such a small cushion and weights that move when I change the estimation window, I’d keep this as a paper pilot.

## After recording

Upload to YouTube with an instructor-accessible link. Enable captions and correct the transcript against what you actually said. Check BIL, QQQ, covariance, basis points, and numerical values. Save the corrected transcript as **docs/transcript-video-2.txt**. Enter the YouTube URL, actual runtime, actual chapter timestamps and transcript link in the [submission manifest](manifest.md). Check access before submission.

[Saved committee run](../outputs/committee-run.json) · [Calculation checks](../outputs/verification.txt) · [Course video checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md)
