I used OpenAI Codex to audit and revise the app and evidence package. The analysis and investment decision are mine.

This is an educational course project. It is not financial or investment advice.

# Response to Project 1 feedback

Review date November 18, 2026. The supplied instructor feedback is the basis of this record.

| Feedback | Project 2 response | Evidence or remaining work |
|---|---|---|
| Data integrity and traceability | Record per-fund source, download timestamp, units, transformation and file fingerprints. Compare archived CPI observations with fresh ALFRED downloads. | [Source ledger](../data/source-ledger.json), [source comparison](../outputs/source-check.json), [data card](data-card.md). Matt's two QQQ screenshots are retained in [personal evidence](student-evidence.md#source-check) and match archived prices to cents; his calculator screenshots also support +3.32% for September. His response recorded November 18 confirms he checked Yahoo that day and still supports a pilot; his words remain unchanged. |
| Financial soundness | Apply Matt’s 10% annual volatility ceiling to all portfolios. Explain historical means, covariance, cost convention, ETF overlap, target circularity and CPI floor. | [Mandate](mandate.md), app Calculations tab, [memo](decision-memo.md). |
| Published training case | Reconcile Week 2 FCFF and equity bridge and the actual portfolio engine against Labs 14 and 15. | [43 computed checks](training-reconciliation.md). Week 2 is supplementary arithmetic; Labs 14 and 15 validate the app’s engine. |
| Validation and reproducibility | Independently enumerate all 53,130 allocations and test risk, input, vintage, export and reset behavior. | [Verification](../outputs/verification.txt). |
| AI-off highest-risk claim and three failures | Retain Matt's supplied claim, supporting reasoning, three failures and detection methods. | [Unchanged reflection and verification notes](highest-risk-claim.md), received after the 15 bp result; any one condition triggers reconsideration and BIL threshold is confirmed at 55%; numerical-consistency note remains for review. |
| Locked Changed-Input Record | Preserve the old AI-assisted practice outcome as practice. Provide a fresh record with old/new units, immutable pre-run commit, output links, direction and diagnosis. | [Validation](validation-and-ai-use.md) links the November 19 locked prediction and [executed 15 bp comparison](cost15-prediction-comparison.md); original prediction preserved. |
| Cold run / partner reproduction | Retain the earlier calculation question and Aj Chapman's November 19 report: 15 minutes, no problems, matching displayed base results. | [Reproduction record](cold-run.md). Matt clarified that a fresh download worked with no problems; successful partner reproduction recorded and no fix needed. Exact commit and changed-control evidence remain unspecified. |
| Communication and manifest | Use Markdown evidence, permanent repository file links and explicit status. Keep scripts separate from corrected transcripts of actual recordings. | [Manifest](manifest.md). All three video links and transcript files are present; final audio/text accuracy, caption publication and continuous webcam review remain. |
| Webcam and duration | Every recording guide now calls for a visible face throughout. Limits remain 3, 5 and 5 minutes. | Published runtimes are 2:36, 4:32 and 4:11, all within limits. Webcam images are visible at the openings; continuous visibility and full narration still need review. |
| WACC and terminal switch | The analogous portfolio checks trace dated inputs, same-vintage CPI, return estimation and the initial cost deduction. | This portfolio app calculates no corporate WACC or terminal enterprise value. |
| Original Amazon Edition A and attribution | Apply the supplied Project 2-specific checklist, which says to skip the Before AI and research-evolution submission items. | Original Amazon deliverables remain part of Project 1 history. |

## Corrections found in the software review

- The old download button returned the saved base file even after inputs changed. It now exports the displayed settings, result and source fingerprints.
- Full price-history validation now precedes window selection, catching an old missing month that a shorter window could hide.
- The engine rejects a symmetric correlation matrix when its joint correlations are mathematically impossible.
- Missing trailing CPI observations are handled explicitly; duplicate observations and invalid levels are refused.
- The 10% risk ceiling applies to the search and both baselines. Equal weight now fails, and 655 grid mixes are eligible at base.
- Reset restores every independent assumption. A current scenario and the saved standard stresses are labeled separately.

These changes resolve concrete software and documentation issues. Personal checks, recordings and the final decision remain student responsibilities.
