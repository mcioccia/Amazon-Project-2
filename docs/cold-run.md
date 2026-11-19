I used OpenAI Codex to document the reproduction evidence and improve the startup instructions. The analysis and decision are mine.

This is an educational course project. It is not financial or investment advice.

# Reproduction record

## Partner report — November 19, 2026

Matt supplied the following report attributed to **Aj Chapman**. This is partner-reported evidence, with Codex's comparison labeled separately.

| Field | Reported detail |
|---|---|
| Reviewer | Aj Chapman |
| Start | November 19, 2026, 9:00 AM; time zone not specified |
| Repository supplied | https://github.com/mcioccia/Amazon-Project-2 |
| Exact version / commit | Not supplied; the repository URL does not identify the tested commit |
| Fresh copy used | **Yes — fresh download**, confirmed by Matt in a follow-up clarification |
| First problem | **"No problems"**; Matt confirmed that the fresh download worked |
| Elapsed time | **15 minutes** |
| App tab or result location | Not specified |
| Selected fund weights | Not supplied |
| Control changed, old/new values and resulting verdict | Not supplied |
| Whether only the README was used, without coaching | Not supplied |
| Additional feedback | Not supplied |

Commands supplied for this report:

~~~powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
~~~

The app-launch command was not included in this report. An earlier report supplied a launch command; it has not been attributed to this attempt.

### Results supplied

| Portfolio | Net estimate | Annual volatility | Verdict |
|---|---|---|---|
| Equal weight | 7.494% | 12.138% | Fail — exceeds 10% risk limit |
| Inverse volatility | 3.775% | 1.999% | Fail — below return target |
| Constrained | 7.498% | 7.241% | Pass |

**Codex comparison:** all six displayed numerical values and the three verdicts match the saved base output at the reported precision. The report does not establish the exact software version used.

**Status:** successful fresh-download partner run recorded: Aj Chapman, November 19, 9:00 AM, 15 minutes, no problems. **No fix was needed for this reported run.** Matt clarified: "It was a fresh download and it worked with no problems." This supersedes the earlier "No" recorded for the fresh-copy field. The exact tested commit, app-launch command, result location, README-only confirmation and changed-control observation remain unspecified; the clarification does not fill those details.

## Earlier partner report — November 18, 2026

On November 18, 2026, Matt reported that his partner had tested Project 2 and asked how the calculations were computed. Matt supplied these commands:

~~~powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
~~~

| Field | Status |
|---|---|
| Partner identity and original run date | Not supplied |
| Version / commit tested | Not supplied; review preceded the November 18 rebuild |
| First failure or confirmation of a clean run | Not supplied |
| Elapsed time | Not supplied |
| Result location | Streamlit app, as reported by Matt |
| Partner question | How were the calculations computed? |
| Response implemented | Calculations tab traces historical estimates, covariance, the switching-cost bridge and the selection rule. |
| Partner rerun of revised version | Pending |

The fields in this earlier report describe what was known on November 18. The November 19 report above supplies additional timing and observed-result evidence; it does not establish the identity or exact version of the earlier attempt.

## Automated reproduction

The automated check uses a clean temporary copy and a fresh Python environment with only requirements.txt installed. The installation and verification passed. The executed result and elapsed time are recorded in [outputs/cold-run.txt](../outputs/cold-run.txt). The later theme configuration changes presentation only. It validates software setup and calculation reproducibility. The partner’s observations above retain their own status.
