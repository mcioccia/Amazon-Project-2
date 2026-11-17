I used OpenAI Codex to adapt my lab code, check calculations and draft the documentation. I am responsible for the analysis, the checks and the investment decision.

This is an educational course project. It is not financial or investment advice.

# Project 2 · Investment Management Application

**Committee action requested: authorize a paper pilot.** This local app compares three allocations of six ETFs under a 7.49% annual objective and a BIL reserve rule. The model uses prices through September 30, 2026 and signal information available for an October 30, 2026 committee meeting. Review the [decision memo](docs/decision-memo.md) and [saved output](outputs/committee-run.json).

## Start the app

Open this repository on GitHub. If GitHub shows a 404 page, sign in to the account invited to the private repository and accept the invitation. Select **Code → Download ZIP**, extract the entire archive, and open the extracted folder containing **app.py**, **requirements.txt**, and this README. On Windows, right-click inside that folder and choose **Open in Terminal**.

Use Python 3.12 and the following commands on Windows. If the first command reports that Python 3.12 is missing, install it from [python.org](https://www.python.org/downloads/) and reopen the terminal. No financial-data account, API key or download of financial data is required. Installing packages requires internet access.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

On macOS or Linux use `python3.12 -m venv .venv` and replace the Python executable in the remaining commands with `.venv/bin/python`. Open the local URL printed by Streamlit on the same computer and keep the terminal running. A localhost link points to the computer opening it, so each reviewer starts their own copy of the app. From an environment already containing the dependencies, `python -m streamlit run app.py` is sufficient.

The **Decision** tab displays mandate verdicts, allocations and annual net estimates. Change a sidebar control to run the whole comparison. **Stress results** shows saved-base perturbations. **Point-in-time signal** shows the permitted vintage and reserve effect. **Mandate** distinguishes the student's established rules from the committee terms proposed for this pilot. With base settings, raising the reserve to the documented 90% stress illustrates an infeasible portfolio. Reset to 3% afterward.

The original Lab 15 interface is included as `lab15_app.py` and uses the same engine. For the numbers without a browser, run `python analysis.py`. Run `python verify.py` for the financial checks and Streamlit interaction check.

## Submission

[Manifest and student completion steps](docs/manifest.md) · [Validation and AI use](docs/validation-and-ai-use.md) · [Signal data card](docs/data-card.md). Decision dates, saved evidence and the prediction sequence matter. Use a **new** scenario for the student’s locked record.