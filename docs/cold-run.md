I used OpenAI Codex to document the reproduction evidence and improve the startup instructions. The analysis and decision are mine.

This is an educational course project. It is not financial or investment advice.

# Reproduction record

## Partner’s run

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

Ask the partner to confirm the timing, first-error outcome and result independently. Preserve their words.

## Automated reproduction

The automated check uses a clean temporary copy and a fresh Python environment with only requirements.txt installed. The installation and verification passed. The executed result and elapsed time are recorded in [outputs/cold-run.txt](../outputs/cold-run.txt). The later theme configuration changes presentation only. It validates software setup and calculation reproducibility. The partner’s observations above retain their own status.
