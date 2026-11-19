I used OpenAI Codex to build, test, and help explain this app. The analysis and decision are mine.

This is an educational project, not financial or investment advice.

I'll trace the actual code from prices to the portfolio verdict. These six funds are the universe. The base sets a 7.49 percent net return target and a ten percent volatility ceiling. The information cutoff is October thirtieth; the mandate approval came later. This is a retrospective paper exercise. The fingerprint check refuses an undocumented change to the saved data.

Here, current price divided by prior price, minus one, gives a monthly return. My checked QQQ example goes from 716.01 to 739.77, about 3.32 percent. Sixty prices give 59 returns. The code annualizes the average by multiplying by twelve, and sample standard deviation by the square root of twelve. It estimates correlations over the same months. These are historical estimates, not promised returns.

Correlation times both volatilities gives covariance. The next block multiplies every covariance by both portfolio weights and adds all the pairs, including each fund with itself. The square root gives portfolio volatility. Funds that move together can add similar risk, even with different tickers. The base is 7.241 percent. The ten percent ceiling limits this estimate; it does not guarantee a maximum loss.

The CPI function first removes archived vintages after the cutoff, then selects the latest eligible one. Both index levels come from that same vintage. September inflation is 3.72 percent. That activates the ten percent BIL floor instead of the normal three percent minimum. Missing eligible evidence pauses the search. The date is the archived vintage, not a claim about the first release time. At base, 65 percent BIL already exceeds this floor.

Starting holdings are equal weight. One-way turnover is half the sum of absolute weight changes, so the buy and sell sides are not counted twice. The base switches 48.333 percent. Ten basis points becomes 0.001. Multiply turnover by that rate and a hundred-thousand-dollar account: 48 dollars and 33 cents. Subtract the cost from gross expected return. This is the initial switch; it does not cover every future expense.

The loop distributes twenty units across six funds. Each unit is five percentage points, so weights add to one hundred percent without shorting. For each candidate, it calculates return, reserve, costs, and risk. Continue skips a failing mix. The best variable changes only when an eligible mix has lower volatility. Of 53,130 candidates, 655 pass at base. This is the best mix on the grid, not every possible allocation. My fifteen-basis-point test reran this whole search. It moved five points from VUG to ONEQ and produced 7.245 percent volatility.

The app displays the engine's results and exports the actual settings with the output. Equal weight fails the risk ceiling; inverse volatility misses the return target. The constrained mix passes, but its return cushion is thin. Requiring ninety percent BIL leaves no eligible mix, so the app says pause. Invalid input evidence also stops the app. Forty-three published training checks passed, and the cost test was independently recalculated. I still recommend a paper pilot, with forward results and the stated review triggers before funding.
