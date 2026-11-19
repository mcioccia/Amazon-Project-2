"""Portfolio committee. AI-assisted coursework. Educational only, not investment advice."""
import json

import altair as alt
import pandas as pd
import streamlit as st

import analysis as engine

st.set_page_config(page_title="Portfolio committee | Matt Cioccia", page_icon="◈", layout="wide")
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Libre+Caslon+Text&display=swap');
.stApp {background:#f5f6f2;color:#183b40;}
.block-container {max-width:1450px;padding-top:2rem;padding-bottom:3rem;}
h1,h2,h3 {color:#173c41;}
h1 {font-family:Georgia,serif!important;font-weight:400!important;letter-spacing:-.035em;}
html,body,[class*="css"],p,li {font-family:"DM Sans","Segoe UI",sans-serif;}
section[data-testid="stSidebar"] {background:#e8eeea;border-right:1px solid #ccd8d0;}
div[data-testid="stMetric"] {background:#fff;border:1px solid #d3ded7;border-radius:9px;padding:14px 18px;}
div[data-testid="stMetricValue"] {color:#155c58;font-family:Georgia,serif;font-size:2rem;}
div[data-testid="stTabs"] {margin-top:12px;}
.committee {background:#153d43;color:#f7faf5;border-radius:10px;padding:20px 25px;margin:15px 0 22px;}
.committee .eyebrow {font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:#afd6c9;}
.committee h2 {color:#fff;font:normal 29px Georgia,serif;margin:4px 0 8px;}
.committee p {color:#e5efea;margin:0;max-width:105ch;}
.smallprint {font-size:13px;color:#526d68;}
</style>
""", unsafe_allow_html=True)

st.title("Portfolio committee")
st.caption("Matt Cioccia · Historical decision snapshot October 30, 2026 · Mandate updated November 18, 2026")
st.caption("Built with OpenAI Codex assistance. Matt owns the analysis and decision. Educational purposes only. Not financial or investment advice.")

def reset_base():
    for name, value in engine.BASE.items():
        st.session_state[name] = value


@st.cache_data(show_spinner=False)
def run_scenario(settings, fingerprint):
    return engine.calculate(**settings)


@st.cache_data(show_spinner=False)
def standard_stresses(fingerprint):
    return engine.stress_runs()


def pct(number):
    return f"{100 * number:.3f}%"


def comparisons(result):
    records = []
    for name, row in result["results"].items():
        if row is None:
            records.append({"Portfolio": name, "Verdict": "PAUSE", "Net estimate": "—",
                            "Annual volatility": "—", "BIL": "—", "Reason": result["stop"]})
        else:
            records.append({"Portfolio": name, "Verdict": row["verdict"],
                            "Net estimate": pct(row["net"]), "Annual volatility": pct(row["risk"]),
                            "BIL": pct(row["reserve"]), "Reason": "; ".join(row["rules"]) or "All modeled rules pass"})
    return pd.DataFrame(records)


for name, value in engine.BASE.items():
    st.session_state.setdefault(name, value)

with st.sidebar:
    st.header("Scenario inputs")
    st.caption("Change one assumption to see the allocation and verdict recalculate.")
    st.button("Reset to approved base", on_click=reset_base, width="stretch")
    st.number_input("Annual net return objective (%)", 0.0, 40.0, None, .05, key="target", format="%.2f")
    st.number_input("Maximum annual volatility (%)", .5, 50.0, None, .5, key="vol_limit")
    st.number_input("Minimum BIL (%)", 0.0, 100.0, None, 1.0, key="reserve")
    st.selectbox("Monthly returns in estimate", [59, 48, 36, 24], key="window")
    st.number_input("Cost per dollar switched (bp)", 0.0, 200.0, None, 1.0, key="cost_bp")
    st.number_input("QQQ return estimate shift (percentage points)", -15.0, 15.0, None, .25, key="qqq_shift")
    st.selectbox("Additional signal delay (calendar days)", [0, 15, 30, 60, 90], key="lag")
    st.caption("Starting holdings and policy benchmark are equal weight. Only BIL counts toward the reserve.")
settings = {name: st.session_state[name] for name in engine.BASE}
try:
    engine.verify_inputs()
    fingerprint = engine.input_hashes()
    with st.spinner("Checking eligible allocations…"):
        current = run_scenario(settings, fingerprint)
        base = run_scenario(engine.BASE, fingerprint)
except (ValueError, OSError, KeyError, TypeError) as error:
    st.error(f"PAUSE · Input evidence needs review. {error}")
    st.stop()

chosen = current["results"].get("Constrained")
changed = [f"{name} = {settings[name]}" for name in settings if settings[name] != engine.BASE[name]]
if changed:
    st.caption("Scenario differs from approved base · " + " · ".join(changed))

if chosen:
    st.markdown('<div class="committee"><div class="eyebrow">Committee action</div><h2>Pilot on paper</h2>'
                '<p>Track the selected mix and actual costs. Seek committee review when a fund moves at least 20 percentage points across windows. '
                'A funded allocation needs confirmed loss tolerance and observed forward results after costs.</p></div>', unsafe_allow_html=True)
else:
    st.warning(current["stop"])
    st.markdown('<div class="committee"><div class="eyebrow">Committee action</div><h2>Pause allocation</h2>'
                '<p>The current settings cannot produce an eligible proposal. Review the mandate or missing evidence before allocating.</p></div>', unsafe_allow_html=True)

decision, stress, calculations, sources, validation, mandate = st.tabs(
    ["Decision", "Stress results", "Calculations", "Sources & timing", "Validation", "Mandate"])

with decision:
    if chosen:
        metrics = st.columns(4)
        metrics[0].metric("First-year net estimate", pct(chosen["net"]))
        metrics[1].metric("Annual volatility", pct(chosen["risk"]))
        metrics[2].metric("Target cushion", f"{(chosen['net'] - settings['target']/100)*10000:+.2f} bp")
        metrics[3].metric("BIL reserve", f"{chosen['reserve']:.0%}")
    if current["results"]:
        st.subheader("Mandate verdicts")
        st.dataframe(comparisons(current), hide_index=True, width="stretch")
        st.caption("PASS applies to modeled return, volatility, reserve, full-investment and long-only rules. Estimated standard deviation does not cap losses.")
        left, right = st.columns([1, 1])
        with left:
            st.subheader("Return earned for estimated risk")
            points = pd.DataFrame([{"Portfolio": name, "Net estimate (%)": row["net"]*100,
                                   "Annual volatility (%)": row["risk"]*100, "Verdict": row["verdict"]}
                                  for name, row in current["results"].items() if row])
            plot = alt.Chart(points).mark_point(filled=True,size=220).encode(
                x=alt.X("Annual volatility (%):Q", scale=alt.Scale(zero=True)),
                y=alt.Y("Net estimate (%):Q", scale=alt.Scale(zero=True)),
                color=alt.Color("Portfolio:N", scale=alt.Scale(domain=["Equal weight", "Inverse volatility", "Constrained"],
                                                            range=["#426a91", "#bf8850", "#15796d"])),
                shape="Verdict:N", tooltip=list(points.columns))
            target_line = alt.Chart(pd.DataFrame({"target":[settings["target"]]})).mark_rule(strokeDash=[5,5],color="#a05f2b").encode(y=alt.Y("target:Q",title="Net estimate (%)"))
            cap_line = alt.Chart(pd.DataFrame({"limit":[settings["vol_limit"]]})).mark_rule(strokeDash=[5,5],color="#a05f2b").encode(x=alt.X("limit:Q",title="Annual volatility (%)"))
            st.altair_chart((plot + target_line + cap_line).properties(height=270), width="stretch")
            st.caption("Dashed lines show the net return target and maximum volatility.")
        with right:
            st.subheader("Allocation by fund")
            weights = pd.DataFrame([{"Portfolio":name, "Fund":fund, "Weight (%)":weight*100}
                                   for name,row in current["results"].items() if row
                                   for fund,weight in row["weights"].items()])
            allocation_chart = alt.Chart(weights).mark_bar().encode(
                x=alt.X("Weight (%):Q", stack="zero", scale=alt.Scale(domain=[0,100])),
                y=alt.Y("Portfolio:N", sort=["Equal weight","Inverse volatility","Constrained"],title=None),
                color=alt.Color("Fund:N", scale=alt.Scale(domain=engine.FUNDS, range=["#294f78","#718db1","#dca86c","#187e70","#9aafa2","#b9aa95"])),
                tooltip=["Portfolio","Fund",alt.Tooltip("Weight (%):Q",format=".2f")]).properties(height=270)
            st.altair_chart(allocation_chart, width="stretch")
        st.dataframe(pd.DataFrame({name:{f:100*w for f,w in row["weights"].items()}
                                  for name,row in current["results"].items() if row}).round(2), width="stretch")
        st.caption(f"Monthly return window {current['estimate_start']} to {current['estimate_end']}. "
                   f"Effective BIL minimum {current['floor']:.1%}. Risk ceiling {settings['vol_limit']:.1f}%. "
                   f"{current['feasible']:,} eligible mixes on a five-percentage-point grid.")
    export = dict(disclosure=engine.NOTICE, decision_as_of=engine.AS_OF, mandate_updated="2026-11-18",
                  inputs=settings, source_sha256=fingerprint, output=current)
    st.download_button("Download this scenario",json.dumps(export,indent=2),"committee-scenario.json","application/json")
    st.caption("The download contains the controls currently displayed, their result, the decision date and source fingerprints.")

with stress:
    st.subheader("How much does the decision move?")
    st.write("Each row starts at the approved base and changes only the named setting. Window changes recalculate every mean and covariance.")
    rows=[]
    reference=base["results"]["Constrained"]
    for name,out in standard_stresses(fingerprint).items():
        result=out["results"].get("Constrained")
        rows.append({"Changed input":name,"Verdict":result["verdict"] if result else "PAUSE",
                     "Net estimate (%)":result["net"]*100 if result else None,
                     "Net change (bp)":(result["net"]-reference["net"])*10000 if result else None,
                     "Volatility (%)":result["risk"]*100 if result else None,
                     "BIL (%)":result["reserve"]*100 if result else None,
                     "Largest weight move (pp)":max(abs(result["weights"][f]-reference["weights"][f])*100 for f in engine.FUNDS) if result else None})
    st.dataframe(pd.DataFrame(rows).round(3),hide_index=True,width="stretch")
    windows = [("59 months",base)] + [(f"{n} months",standard_stresses(fingerprint)[f"{n}-month window"]) for n in [48,36]]
    window_weights=pd.DataFrame([{"Window":label,"Fund":fund,"Weight (%)":100*weight}
                                for label,out in windows for fund,weight in out["results"]["Constrained"]["weights"].items()])
    st.altair_chart(alt.Chart(window_weights).mark_bar().encode(
        x=alt.X("Weight (%):Q",scale=alt.Scale(domain=[0,100])),y=alt.Y("Window:N",sort=["59 months","48 months","36 months"]),
        color=alt.Color("Fund:N",scale=alt.Scale(domain=engine.FUNDS,range=["#294f78","#718db1","#dca86c","#187e70","#9aafa2","#b9aa95"])),
        tooltip=["Window","Fund","Weight (%)"]).properties(height=170),width="stretch")
    st.info("Committee review · A 20-point weight change meets the escalation trigger. "
            "Across these windows the paired paper allocations are 65–85% BIL and 35–15% equity.")
    st.write("Pause on an infeasible mandate, invalid input evidence or no eligible CPI vintage. "
             "The 90% BIL requirement is a demonstrated stop case.")
    st.caption("The 7.49% target was set from the original six-fund historical average. Its closeness to equal weight is mechanical. "
               "The CPI floor is below the selected BIL weight at base, so this run establishes no CPI timing benefit.")

with calculations:
    st.subheader("Follow a dollar through the model")
    data=engine.estimates(settings["window"])
    estimates=pd.DataFrame([{"Fund":s["name"],"Annual mean estimate (%)":s["return"]*100,
                            "Annual sample volatility (%)":s["volatility"]*100} for s in data["sleeves"]])
    estimates.loc[estimates["Fund"]=="QQQ","Annual mean estimate (%)"] += settings["qqq_shift"]
    st.dataframe(estimates.round(3),hide_index=True,width="stretch")
    st.write("Monthly return = current adjusted close ÷ previous adjusted close − 1. "
             "Annual mean = monthly arithmetic mean × 12. Annual sample covariance = monthly sample covariance × 12.")
    st.latex(r"\sigma_p = \sqrt{\sum_i\sum_j w_i w_j\sigma_i\sigma_j\rho_{ij}}")
    with st.expander("Inspect the estimated correlations"):
        st.dataframe(pd.DataFrame(data["correlations"],index=engine.FUNDS,columns=engine.FUNDS).round(4),width="stretch")
    st.caption("The three equity funds overlap heavily. Historical means and covariance depend on the selected window.")
    if chosen:
        st.subheader("Return and switching-cost bridge")
        bridge=pd.DataFrame([{"Component":"Weighted annual gross estimate","Percentage points":chosen["gross"]*100},
                             {"Component":"Initial switching cost","Percentage points":-chosen["cost"]*100},
                             {"Component":"First-year net estimate","Percentage points":chosen["net"]*100}])
        st.dataframe(bridge.round(6),hide_index=True,width="stretch")
        st.write(f"One-way turnover = half the sum of absolute weight changes from equal weight = **{chosen['turnover']:.2%}**. "
                 f"On an illustrative USD 100,000 account, **USD 100,000 × {chosen['turnover']:.6f} × "
                 f"{settings['cost_bp']/10000:.6f} = USD {100000*chosen['cost']:,.2f}**.")
        st.caption("The assumed cost includes the two legs of switching once. Taxes, ongoing fees, later rebalances and market impact require separate review.")
    with st.expander("How the search decides"):
        st.write("Distribute twenty 5% units across six funds. Compute each mix’s after-cost return, reserve and annual volatility. "
                 "Reject any rule failure. Keep the lowest volatility among the eligible mixes. Ties keep the first mix in fund order.")
        st.code("net = gross - cost_rate * one_way_turnover(weights, starting_weights)\n"
                "eligible = (net >= target and BIL >= reserve_floor and volatility <= risk_limit)",language="python")
        st.caption("This displayed summary uses the same decision rules as portfolio.py and analysis.py. The search finds a minimum on the 5% grid.")

with sources:
    st.subheader("What was knowable on the decision date?")
    signal=current["signal"]
    if signal:
        st.write(f"Measured month **{signal['month'][:7]}** · selected archived vintage **{signal['vintage']}** · cutoff **{signal['cutoff']}**")
        st.write(f"**100 × ({signal['level']} ÷ {signal['prior']} − 1) = {signal['yoy']:.3f}%** annual CPI inflation.")
        st.write(f"The 3% inflation trigger calls for a 10% BIL floor. Effective minimum for this scenario is **{current['floor']:.1%}**.")
    else:
        st.warning("No eligible archived CPI vintage at this cutoff.")
    ledger=json.loads((engine.DATA/"source-ledger.json").read_text())
    st.dataframe(pd.DataFrame([{"Fund":f["ticker"],"Downloaded":f["downloaded_at"],"Source":f["source_page"]} for f in ledger["funds"]]),
                 hide_index=True,width="stretch",column_config={"Source":st.column_config.LinkColumn("Source")})
    with st.expander("Data card and publication limits"):
        st.markdown((engine.ROOT/"docs/data-card.md").read_text(encoding="utf-8"))
    with st.expander("Archived input fingerprints"):
        st.json(fingerprint)
    st.caption("November 18 review date and mandate approval are later than the October 30 historical snapshot. "
               "This is a retrospective paper exercise. A forward record starts only after the process is frozen.")

with validation:
    st.subheader("Evidence behind the decision")
    path=engine.ROOT/"outputs/training-reconciliation.json"
    if path.exists():
        reconciliation=json.loads(path.read_text())
        st.dataframe(pd.DataFrame(reconciliation["checks"]),hide_index=True,width="stretch")
        st.caption("Published course answers are stored separately from engine calculations. Sources and tolerances appear in the reconciliation record.")
    source_path=engine.ROOT/"outputs/source-check.json"
    if source_path.exists():
        check=json.loads(source_path.read_text())
        st.write("Automated ALFRED comparison · " + ", ".join(f"{x['vintage']} {x['status']}" for x in check["cpi"]))
    st.write("Independent numerical validation recomputes sample covariance and enumerates the allocation grid through a separate calculation.")
    st.warning("Student evidence still needed · personal source check, AI-off prediction and later result, final transcripts and access checks.")
    st.caption("Partner report: Aj Chapman, November 19, 9:00 AM; fresh download confirmed by Matt; 15 minutes; no problems; displayed base results match. No fix needed for the reported run. Exact version and a changed-control observation remain unspecified.")

with mandate:
    st.markdown((engine.ROOT/"docs/mandate.md").read_text(encoding="utf-8"))
