I used OpenAI Codex to adapt my lab code, test the calculations, and help draft this presentation. The analysis, the checks, and the investment decision are mine.

This is an educational course project. It is not financial or investment advice.

# Video 3 · Investment committee presentation

**Record the live Portfolio committee app with your microphone on.** Keep this guide on your phone, a second screen, or paper. Start recording with the app already visible on **Decision**. Aim for **4:20**, including the clicks and pauses. The course limit is **5:00**. Read only the paragraphs marked **Say**.

## Before pressing Record

- Open [the live app on Matt’s computer](http://127.0.0.1:8506/). If the local server is off, open PowerShell in the Project 2 folder and run the command below. Leave PowerShell running, then open the link again. On another computer, follow the [README](../README.md).
- Open the left sidebar **Scenario inputs**. If it is collapsed, use the expand control at the upper left. Set **Annual net return objective (%)** to **7.49**, **Minimum BIL (%)** to **3**, **Monthly returns in estimate** to **59**, **Cost per dollar switched (bp)** to **10**, **QQQ return estimate shift (percentage points)** to **0**, and **Additional signal delay (calendar days)** to **0**. Press **Enter** after typing in a number field.
- Click **Decision**. Scroll to the top. Confirm the three large numbers read **7.498%**, **7.241%**, **+0.80 bp**. Keep the sidebar and main page visible. Start recording the browser window and speak the disclosures first.

~~~powershell
& '..\Lab_14\.venv\Scripts\python.exe' -m streamlit run app.py --server.address 127.0.0.1 --server.port 8506
~~~

## 0:00–0:35 · Ask for the decision

**Click / point.** Stay on **Decision**. Point to **Committee call: paper pilot**, then the three large numbers.

**Say**

I used OpenAI Codex to adapt my lab code, test the calculations, and help draft this presentation. The analysis, the checks, and the investment decision are mine.

This is an educational course project. It is not financial or investment advice.

I’m asking the committee to authorize a paper pilot. On our October 30 decision date, the mix clears our 7.49 percent first-year return target after trading costs. But look at the cushion on the right. It’s less than one basis point. That’s a thin margin to rely on with real money.

## 0:35–1:20 · Compare the choices

**Click / point.** On **Decision**, scroll to **Mandate verdicts**. Point down the three portfolio rows. Scroll a little farther to **Allocation by fund (%)** and point to the **Constrained** column, especially **BIL**.

**Say**

Equal weight is my benchmark and starting portfolio. It passes, with a 7.494 percent estimated net return and about 12.14 percent annual volatility. Inverse volatility has the lowest estimated risk, but its 3.775 percent net return misses our target. The constrained portfolio also passes. It delivers almost the same estimated return as equal weight with about 7.24 percent volatility.

Here’s what we would track on paper. For every hundred dollars, 65 goes into BIL, the Treasury-bill fund. The other 35 goes into equities: 15 in QQQ, five in ONEQ, and 15 in VUG. IEF and LQD get zero in this run.

## 1:20–1:55 · Defend the reserve rule

**Click / point.** Scroll the main page back to the tab row. Click **Point-in-time signal**. Under **Inflation and the liquidity reserve**, point to **2026-09**, **3.72%**, the returned vintage **2026-10-28**, and the **10.0%** effective floor.

**Say**

Why require a reserve at all? The mandate starts with a three percent minimum in BIL. If annual inflation reaches three percent, that minimum rises to ten. September inflation was 3.72 percent in the October 28 release vintage we could use by October 30. So the effective minimum that day was ten percent. The portfolio held 65 percent because of the risk and return estimates. The rule only required ten.

## 1:55–2:50 · Change one input live

**Click / point.** Click **Decision**. In the left sidebar, open **Monthly returns in estimate** and select **36**. Wait for the large numbers to read **7.528%**, **2.576%**, **+3.85 bp**. Scroll down to **Allocation by fund (%)** and point to **BIL → Constrained → 85.00**. Scroll back to the tabs and click **Stress results**. Point to the **48-month window** and **36-month window** rows. This table compares saved stresses against the original base.

**Say**

I’m keeping the target, the reserve rule and trading costs fixed. All I’m changing is how much price history I use. With 36 months, the model still passes. Its estimated annual volatility falls to about 2.58 percent. But scroll down to the actual dollars: BIL now takes 85 out of every hundred, up from 65.

The 48-month run also puts 85 percent in BIL. Across the three windows, that gives us a paper range of 65 to 85 percent in bills, with 35 percent in equities at the low end of that bill range and 15 percent at the high end. Moving a fifth of the account just by changing the window hits my committee-review trigger.

## 2:50–3:35 · Show when trading stops

**Click / point.** Click **Decision**. In the sidebar, change **Monthly returns in estimate** back to **59**. Wait for **7.498%** to return. Click inside the **Minimum BIL (%)** number field, press **Ctrl+A**, type **90**, and press **Enter**. Wait. Point to **No eligible allocation. Pause allocation.** and the **Constrained** row under **Mandate verdicts**.

**Say**

I’m back at the original window. Now I’ll change only the minimum in BIL, from three percent to 90 percent. With that much required in bills, none of the five-point mixes reaches our return target. The committee gets a pause warning and no proposed allocation. At that point I would bring the constraint and the objective back to the committee for review.

## 3:35–4:20 · Restore the base and close

**Click / point.** In **Minimum BIL (%)**, press **Ctrl+A**, type **3**, and press **Enter**. Leave **Monthly returns in estimate** at **59**. Scroll to the top of **Decision**. Wait until **7.498%**, **7.241%**, and **+0.80 bp** reappear. Finish your last sentence, pause, then stop recording.

**Say**

We’re back at the base allocation. My ask is to track the 65 percent BIL and 35 percent equity mix on paper. Each month I’d check the inflation vintage, what the trades actually cost, and whether the return cushion survives those costs. I’d bring any 20-point shift in a fund back to this committee. Before asking for a funded allocation, I’d want the committee to confirm its loss tolerance and review forward paper results after costs.

## After recording

Upload the video to YouTube and check that the instructor can open it. Enable captions and correct the transcript against the actual recording, especially BIL, basis points, and the percentages. Save it as **docs/transcript-video-3.txt**. Add the YouTube link, actual duration, timestamp index and corrected transcript link to the [submission manifest](manifest.md). The times above are rehearsal cues.

[Committee memo](decision-memo.md) · [Saved scenario results](../outputs/committee-run.json) · [Project directions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md)
