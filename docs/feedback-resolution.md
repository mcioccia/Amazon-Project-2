I used OpenAI Codex to audit and revise the app and evidence package. The analysis and investment decision are mine.

This is an educational course project. It is not financial or investment advice.

# Response to Project 1 feedback

Review date November 18, 2026. The supplied instructor feedback is the basis of this record.

| Feedback | Project 2 response | Evidence or remaining work |
|---|---|---|
| Data integrity and traceability | Record per-fund source, download timestamp, units, transformation and file fingerprints. Compare archived CPI observations with fresh ALFRED downloads. | [Source ledger](../data/source-ledger.json), [source comparison](../outputs/source-check.json), [data card](data-card.md). Matt's two QQQ screenshots are retained in [personal evidence](student-evidence.md#source-check) and match archived prices to cents; his calculator screenshots also support +3.32% for September. Access-date confirmation and his interpretation remain pending. |
| Financial soundness | Apply Matt’s 10% annual volatility ceiling to all portfolios. Explain historical means, covariance, cost convention, ETF overlap, target circularity and CPI floor. | [Mandate](mandate.md), app Calculations tab, [memo](decision-memo.md). |
| Published training case | Reconcile Week 2 FCFF and equity bridge and the actual portfolio engine against Labs 14 and 15. | [43 computed checks](training-reconciliation.md). Week 2 is supplementary arithmetic; Labs 14 and 15 validate the app’s engine. |
| Validation and reproducibility | Independently enumerate all 53,130 allocations and test risk, input, vintage, export and reset behavior. | [Verification](../outputs/verification.txt). |
| AI-off highest-risk claim and three failures | Provide a student-owned record with empty fields for the claim and potential failures. | [Personal evidence](student-evidence.md), pending Matt. |
| Locked Changed-Input Record | Preserve the old AI-assisted practice outcome as practice. Provide a fresh record with old/new units, immutable pre-run commit, output links, direction and diagnosis. | [Validation](validation-and-ai-use.md), new personal record pending. |
| Cold run / partner reproduction | Record Matt’s report that the partner tested the app, the three startup commands, and their question about calculations. | [Reproduction record](cold-run.md). Error and timing details unconfirmed; revised-build partner rerun pending. |
| Communication and manifest | Use Markdown evidence, permanent repository file links and explicit status. Keep scripts separate from corrected transcripts of actual recordings. | [Manifest](manifest.md). Final video links and transcripts pending. |
| Webcam and duration | Every recording guide now calls for a visible face throughout. Limits remain 3, 5 and 5 minutes. | Recording guides and dashboards. Actual recordings require verification. |
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
