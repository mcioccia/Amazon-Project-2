OpenAI Codex was used to save and version Matt's supplied prediction without rewriting it. The analysis and decision are Matt's.

Educational purposes only. Not financial or investment advice.

# Switching-cost prediction — before run

Received November 19, 2026. The text below is Matt's supplied prediction, preserved as written. Predictions and probability judgments are not observed results.

## Matt's prediction

1\. Input alteration

I am going to change the switching cost from 10 basis points to 15 basis points (or 0.15%) per dollar.

The reason for this is that I believe there is almost no buffer in the current pass: the projected return is 7.498%, while the target is 7.49% - only a mere 0.008 pp between them. A 5 basis points change is a rather minor, yet realistic stress test of execution costs (spreads and slippage). It is positioned between the base case and the previously run 25 basis points scenario, which helps see if the allocated investment is stable in case of small cost errors.


I haven’t obtained the results of the simulation for the given situation. I am not reusing the scenarios with 25 or 50 basis points.\
\
2\. What is going to stay constant

I would maintain the return objective, volatility limit, BIL configuration, CPI rule, estimation window, QQQ modification, signal delay, initial investments, fund universe and the data source according to the base values described earlier. 

3\. My prediction in numbers

The result I expect to see is: average annual volatility of an allocation chosen by the application.

The present value of the variable in question is: 7.241% per year (annualized expected standard deviation).

I believe that this number will increase, reaching around 7.7%. The range of outcomes that I consider 80% likely goes from 7.3% to 8.6%. I think that there will be a proper combination of the underlying instruments, so the situation "no combinations are possible" is not very probable (< 10%). I expect the allocation chosen to change: BIL will become less than 65% or stocks will be rearranged or both.

4\. My project forecast

I currently suggest that a pilot is the way to proceed.

Following this modification, I anticipate that my final choice will still be Pilot, as long as the newly assigned mix is still valid. It is also relevant to mention that base scenario is very close to the limit regarding returns and this depends on the cost going by.

There are the outcomes that would make me rethink this decision, and they are any of the following:

absence of a mix for 15bp

the volatility chosen is above 9% leaving only less than one point to the limit of 10%

the weight of BIL falls below 50% indicating that id a little adjustment in costs would provide for the huge switch towards the equity market.


5. 


I am at the opinion that, the new updated methods will most likely not tend to lead to the performance of 15 bp. This study means that the performance will most likely chase by 48.4%. As a result, the level of 15 bp switching costs will increase by 5bp and might affect the return by about .02-.05%, depending on how the app deals with the different dollars. Either amount is actually larger than the 0.008- point margin, so 7.5% falls to roughly 7.45% to 7.47%, then below the 7.49%. A high cost can lower net return for every mix that trades. The minimum volatility mix drops out which it then should rise quickly.

Moving into one 5-point step from BIL into equities should actually add about .5 points in gross returns. This is way more than the lost margin. The app can and may find a cheaper fix; reshuffling among QQQ, ONEQ and VUG to cut turnover. Either would raise volatility less. That is why my central estimate is below the full one step estimate.

Some valid mix still exists. Pure equity mixes have a big enough return spread and can remain within 10% volatility limit.

## Execution context retained with this prediction

This context records the existing settings; it is separate from Matt's wording above. No scenario was run while preparing this record.

| Setting | Held fixed / changed |
|---|---|
| Cost per dollar switched | Only change: 10 bp (0.10%) to 15 bp (0.15%) |
| Net return objective | 7.49% |
| Maximum estimated annual volatility | 10% |
| BIL minimum control | 3%; existing CPI rule unchanged (effective floor 10% at base) |
| Monthly-return estimation window | 59 |
| QQQ estimate adjustment | 0 percentage points |
| Additional signal delay | 0 calendar days |
| Starting allocation | Equal weight across QQQ, ONEQ, VUG, BIL, IEF and LQD |
| Search grid | Five-percentage-point steps |
| Decision information snapshot | October 30, 2026; revised mandate approved November 18 |
| Model revision before this record | 7ef6337b9602f1a3836854cf0cc507c335da76f9 |

Input files stay unchanged:

| Input | SHA-256 |
|---|---|
| data/prices.csv | 2c93e65a793d2ecc89f704cff078f0bdf92bf2ec3bcb03e57b0ac57214fdc9c6 |
| data/cpi-vintages.json | 38fdcd3fabeb45924ee0d8dc34ecf331c56bbb185640917ba5eff340e6476c78 |
