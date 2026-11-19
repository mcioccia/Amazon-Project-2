# CPI data card

The signal is year-over-year U.S. all-items CPI inflation from **CPIAUCSL**, a monthly seasonally adjusted index (1982–84 = 100). Both levels in each calculation come from the same archived ALFRED vintage. Inflation is 100 × (latest index / same month a year earlier − 1). [Series description](https://fred.stlouisfed.org/series/CPIAUCSL)

| Requested archive | Returned vintage | Use |
|---|---|---|
| 2026-09-30 | 2026-09-30 | Earlier information set for the lag stress. [ALFRED data](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=CPIAUCSL&vintage_date=2026-09-30) |
| 2026-10-29 | 2026-10-28 | Latest evidence available in this project. [ALFRED data](https://alfred.stlouisfed.org/graph/alfredgraph.csv?id=CPIAUCSL&vintage_date=2026-10-29) |

Lab 17 downloaded both archives October 29, 2026. The bundled file retains the last 15 published observations per vintage, actual label, source URL and retrieval timestamp. For the October 30 decision, select the newest **returned** vintage dated on or before the decision date minus the optional delay. September CPI appears in the October vintage and was unavailable in the September vintage. Date labels denote observation months. Seasonally adjusted history may be revised. An archive establishes day-level availability and cannot support an intraday release-time claim.

**Approved paper-pilot rule.** When annual inflation is at least 3%, require at least 10% BIL to preserve liquidity for review of real spending needs. Otherwise apply the mandate floor alone. This is a committee design choice, with no established forecasting performance. At baseline the 10% floor activates, but the optimizer already selects 65% BIL. An unavailable vintage stops the process. The lag slider tests an older information set, not a download made on the earlier date.

**Fund prices.** Identical copy of the six-column Lab 15 Yahoo adjusted-close file, downloaded October 22, 2026. Daily adjusted closes were reduced to the last trading observation in each complete month. Monthly observations from October 29, 2021 through September 30, 2026 produce 59 simple returns. The shorter windows use 36 or 48 returns. Annual arithmetic mean = monthly mean × 12. Annual sample covariance = monthly covariance × 12. Prices are a fixed adjusted-history download available before this decision. They do not reconstruct what a data vendor would have shown on each earlier date. No missing values are filled. [QQQ](https://finance.yahoo.com/quote/QQQ/history/) · [ONEQ](https://finance.yahoo.com/quote/ONEQ/history/) · [VUG](https://finance.yahoo.com/quote/VUG/history/) · [BIL](https://finance.yahoo.com/quote/BIL/history/) · [IEF](https://finance.yahoo.com/quote/IEF/history/) · [LQD](https://finance.yahoo.com/quote/LQD/history/)

AI-use disclosure: OpenAI Codex assisted with software, analysis and writing. Educational purposes only. Not financial or investment advice.
## Source audit on November 18, 2026

The source ledger records each fund’s original download timestamp, exact chart endpoint, field, scale, transformation and input-file SHA-256. The app compares input fingerprints before calculating. A fingerprint proves which file was used; the source comparison supplies separate evidence about the observations.

Fresh downloads of both requested ALFRED vintages match every nonmissing CPI observation retained in the input archive. The refreshed October response labels its column CPIAUCSL_20261029; the original Lab 17 record labeled the effective vintage 2026-10-28. The input retains that original metadata. Both dates precede the October 30 decision, and compared values agree. The November 18 retrieval does not re-establish the original response header or an intraday release time.

Prices are retained from the October 22 download. Live adjusted-close history can change after later distributions or corrections. The hash comparison and existing Lab 15 verification preserve the fixed input panel. Matt supplied QQQ source screenshots on November 18: August 31 Adj Close 716.01 and September 30 Adj Close 739.77 USD per share. Codex's comparison matches the archive at displayed cent precision. The [images, comparison and Matt's calculator evidence](student-evidence.md#source-check) are retained. His result is +3.31838940797% for September, or +3.32%; Codex verified the arithmetic. The archived full-precision prices also give +3.32% when rounded. Matt's response recorded November 18 says he checked Yahoo that day, found the numbers aligned and still wants to pilot. His exact wording is retained in the personal source check; screenshot capture time is not independently established.

[Source ledger](../data/source-ledger.json) · [Automated comparison](../outputs/source-check.json) · [Personal source check](student-evidence.md)
