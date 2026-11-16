"""Portfolio committee app built from Lab 15. AI-assisted education. Not financial or investment advice."""
import pandas as pd
import streamlit as st
from analysis import AS_OF, BASE, FUNDS, ROOT, calculate, stress_runs

st.set_page_config(page_title="Project 2 | Portfolio committee", layout="wide")
st.title("Portfolio committee")
st.caption("Project 2 · Decision snapshot " + AS_OF + " · OpenAI Codex assisted with development and analysis. Educational purposes only. Not financial or investment advice.")
st.write("**Committee call: paper pilot.** Compare the six-fund allocation with equal weight and inverse volatility. All returns and risks below are estimates.")

@st.cache_data(show_spinner=False)
def scenario(settings):
    return calculate(**settings)

@st.cache_data(show_spinner=False)
def standard_stresses():
    return stress_runs()

def pct(x):
    return f"{x*100:.3f}%"

def comparison(result):
    rows = []
    for name, r in result["results"].items():
        if r is None:
            rows.append({"Portfolio":name, "Verdict":"FAIL", "Rule or reason":result["stop"]})
            continue
        rows.append({"Portfolio":name, "Verdict":r["verdict"], "Rule or reason":"; ".join(r["rules"]) or "All rules pass",
                     "Gross return":pct(r["gross"]), "Net return":pct(r["net"]), "Volatility":pct(r["risk"]),
                     "BIL":pct(r["reserve"]), "Turnover":pct(r["turnover"]), "Trading cost":pct(r["cost"])})
    return pd.DataFrame(rows)

with st.sidebar:
    st.header("Scenario inputs")
    st.caption("Settings apply to all portfolios. Standard stresses use the saved base.")
    target = st.number_input("Annual net return objective (%)", 0.0, 40.0, 7.49, 0.05, format="%.2f")
    reserve = st.number_input("Minimum BIL (%)", 0.0, 100.0, 3.0, 1.0)
    window = st.selectbox("Monthly returns in estimate", [59,48,36,24])
    cost = st.number_input("Cost per dollar switched (bp)", 0.0,200.0,10.0,1.0)
    shift = st.number_input("QQQ return estimate shift (percentage points)",-15.0,15.0,0.0,0.25)
    lag = st.selectbox("Additional signal delay (calendar days)", [0,15,30,60,90])
settings = dict(target=target,reserve=reserve,window=window,cost_bp=cost,qqq_shift=shift,lag=lag)
with st.spinner("Evaluating portfolio weights…"):
    current = scenario(settings)
decision,stress,signal,mandate = st.tabs(["Decision", "Stress results", "Point-in-time signal", "Mandate"])
with decision:
    if current["stop"]:
        st.warning(current["stop"])
    if current["results"]:
        chosen = current["results"]["Constrained"]
        if chosen:
            left,mid,right=st.columns(3)
            left.metric("First-year net estimate",pct(chosen["net"]))
            mid.metric("Annual volatility",pct(chosen["risk"]))
            right.metric("Target cushion",f"{(chosen['net']-target/100)*10000:+.2f} bp")
        st.subheader("Mandate verdicts")
        st.dataframe(comparison(current),hide_index=True,width="stretch")
        weights = pd.DataFrame({name:{f:r["weights"][f]*100 for f in FUNDS}
                                for name,r in current["results"].items() if r is not None})
        st.subheader("Allocation by fund (%)")
        st.dataframe(weights.style.format("{:.2f}"),width="stretch")
        st.bar_chart(weights, stack=False, y_label="Portfolio weight (%)")
        st.caption(f"Price-estimation window {current['estimate_start']} to {current['estimate_end']}. BIL minimum after signal {current['floor']:.1%}.")
    st.download_button("Download saved committee run",(ROOT/"outputs/committee-run.json").read_bytes(),"committee-run.json","application/json")

with stress:
    st.subheader("One input changed from the base")
    ref=scenario(BASE)["results"]["Constrained"]
    rows=[]
    for name,out in standard_stresses().items():
        m=out["results"].get("Constrained")
        rows.append({"Change":name, "Result":m["verdict"] if m else "PAUSE",
                     "Net":pct(m["net"]) if m else "—", "Volatility":pct(m["risk"]) if m else "—",
                     "BIL":pct(m["reserve"]) if m else "—",
                     "Largest weight move (pp)":round(100*max(abs(m["weights"][f]-ref["weights"][f]) for f in FUNDS),2) if m else None,
                     "Reason":out["stop"] or "Feasible"})
    st.dataframe(pd.DataFrame(rows),hide_index=True,width="stretch")
    st.write("**Escalate to committee** when any fund moves by 20 percentage points or more across windows. Pause on missing signal evidence or an infeasible mandate. Paper allocations only until the committee confirms its risk tolerance and observes forward results.")

with signal:
    st.subheader("Inflation and the liquidity reserve")
    sig=current["signal"]
    if sig:
        st.write(f"Measured month **{sig['month'][:7]}**, prior-year index **{sig['prior']}**, latest index **{sig['level']}**. Year-over-year change **{sig['yoy']:.2f}%**.")
        st.write(f"Permitted vintage cutoff **{sig['cutoff']}**. Returned ALFRED vintage **{sig['vintage']}**. Downloaded **{sig['download']}**.")
        st.write(f"Signal calls for a BIL floor of **{sig['floor']:.0f}%**. With the mandate, the effective floor is **{current['floor']:.1%}**.")
    else:
        st.warning("No archived vintage at or before this information cutoff.")
    st.markdown((ROOT/"docs/data-card.md").read_text(encoding="utf-8"))
with mandate:
    st.markdown((ROOT/"docs/mandate.md").read_text(encoding="utf-8"))
