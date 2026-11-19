OpenAI Codex was used to save Matt's supplied text unchanged and add separately labeled verification notes. The analysis and decision are Matt's.

Educational purposes only. Not financial or investment advice.

# Highest-risk claim and possible failures

Received November 19, 2026, after the 15 bp result was reported. This reflection does not replace the previously committed prediction.

## Matt's text — unchanged

My Highest-Risk Claim

Raising the switching cost to 15 bp won’t break the portfolio. My claim is the app can still find a mix that passes and volatility will only go up a little bit to about 7.6%.\
 This could mislead the committee because it can make the actual pilot seem safer than it really is.

Evidence is a higher cost can lower net return, therefore the app has fewer passing mixes to actually choose from. The supposed safest one will be the same or riskier, never actually safer.\
 Second is moving 5% from BIL into stocks can actually add about .5 points of return, which is more than the 0.02-0.05 points the extra costs take away. On top of that there is still room under the 10% volatility to hold some stocks.

3 Ways It Could Fail

1. The app counts switching costs differently than I think it’s supposed to count them. If it charges way more than I assume, the return drop is way higher and the app needs more stocks to pass. I’d check to see how the app calculates switching costs and test it.
2. Stocks may not actually add that much return. The 59 months of data include 2022 when stocks did horribly, so the gap may be smaller. I’d actually compare each of the funds’ estimated return and look at the bp result.
3. The current pass may actually just be a sign of luck rather than actually being correct. I’d check this by rerunning the base case with a shorter window or even a longer window and see if it still passes that same thing.

Conclusion

I would definitely still recommend the pilot but a more careful one because the one I have right now I am not 100% comfortable with. I would change my decision if no mix passes at 15 bp, the volatility goes above 9%, BIL drops below 55, and the base case fails when I change the data window.

## Verification notes — added by Codex

These notes are separate from Matt's words.

- Actual 15 bp results: estimated annual volatility **7.244616%**, first-year net return **7.503349%**, mandate **PASS**. The reflection's **7.6%** is not the executed result. The original locked forecast was **7.7%** and remains unchanged.
- Feasible mixes fell from **655 to 636**. Holding all other inputs fixed, higher nonnegative switching costs cannot expand the feasible set, so minimum feasible volatility cannot fall. Its observed rise was just **0.004063 percentage points**.
- The selected mix kept **65% BIL** and moved **five percentage points from VUG to ONEQ**. Turnover stayed **48.333333%**. Cost at 15 bp is **0.0725% of portfolio value**, or **USD 72.50** on USD 100,000. The hypothetical BIL-to-equity move did not occur.
- This reflection states a **55% BIL** threshold, versus **50%** in the locked prediction, and adds a window-failure condition. These are subsequent stated conditions; they do not change the historical test or model inputs. Whether any single listed condition is sufficient should be made explicit before operational use; the original wording "and" is preserved.
- The current data provides at most **59 monthly returns**. A longer window requires additional sourced history. Existing shorter-window runs can be reviewed.
- The 15 bp result is already observed. Future pilot reliability still requires forward evidence; this check does not establish realized safety.

[Original prediction](prediction-15bp-before-run.md) · [Executed comparison](cost15-prediction-comparison.md) · [Run data](../outputs/cost15-run-record.json)
