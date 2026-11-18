"""Published training reconciliations. AI-assisted education; not investment advice."""
import copy
import csv
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import portfolio as model

ROOT = Path(__file__).resolve().parent
SOURCES = {
    "Week 2": "https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-02/student-handout.md",
    "Lab 14": "https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-09/lab-14-portfolio-baselines.md",
    "Lab 15": "https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/lessons/week-09/lab-15-portfolio-stability.md",
}


def reconcile():
    checks = []

    def check(case, metric, expected, actual, unit, digits):
        passed = round(actual, digits) == round(expected, digits)
        checks.append({"Case":case, "Metric":metric, "Published":expected, "Computed":round(actual,digits),
                       "Unit":unit, "Tolerance":f"Rounded to {digits} decimals", "Status":"PASS" if passed else "FAIL"})
        if not passed:
            raise AssertionError(f"{case} {metric}: {actual} differs from {expected}")

    # Read instructor inputs; expected results remain separate from the arithmetic.
    with (ROOT/"data/training/week02-mini-case.csv").open(newline="") as source:
        values={r["metric"]:float(r["value"]) for r in csv.DictReader(source)}
    fcff=values["ebit"]*(1-values["tax_rate"])+values["depreciation_and_amortization"]-values["capital_expenditures"]-values["increase_in_operating_nwc"]
    equity=values["enterprise_value"]+values["nonoperating_cash"]-values["debt"]-values["noncontrolling_interest"]-values["unfunded_pension"]
    check("Week 2","FCFF",77.5,fcff,"USD millions",1)
    check("Week 2","Equity value",820,equity,"USD millions",1)
    check("Week 2","Per share",8.20,equity/values["diluted_shares"],"USD/share",2)

    answers={"Benchmark":(6.80,10.46,0.0), "Equal weight":(5.20,5.21,50.0),
             "Inverse volatility":(3.77,1.05,90.3)}
    results=model.evaluate_portfolios(model.SLEEVES,model.CORRELATIONS,model.BENCHMARK_WEIGHTS,model.OBJECTIVE_RETURN)
    for name,row in results.items():
        for field,expected,units,digits in zip(["return","volatility","reserve"],answers[name],["%","%","%"],[2,2,1]):
            check("Lab 14 "+name,field,expected,100*row[field],units,digits)
    weights={"Benchmark":[0,0,40,60],"Equal weight":[25,25,25,25],"Inverse volatility":[84.3,6.0,7.0,2.6]}
    for name,row in results.items():
        for i,expected in enumerate(weights[name]):
            check("Lab 14 "+name,f"Weight {i+1}",expected,100*row["weights"][i],"%",1)
    shifted=copy.deepcopy(model.SLEEVES)
    shifted[3]["return"]=.07
    correlation=copy.deepcopy(model.CORRELATIONS)
    correlation[2][3]=correlation[3][2]=.50
    runs=[("Base",model.SLEEVES,model.CORRELATIONS,[0,20,25,55],6.51,9.44),
          ("Equity 7%",shifted,model.CORRELATIONS,[0,10,10,80],6.53,12.94),
          ("Correlation .50",model.SLEEVES,correlation,[0,40,0,60],6.52,9.73)]
    outputs={}
    for name,sleeves,correlations,expected_weights,ret,vol in runs:
        result=model.search_portfolios(sleeves,correlations,.065,.03)
        outputs[name]=result
        for i,expected in enumerate(expected_weights):
            check("Lab 15 "+name,f"Weight {i+1}",expected,100*result["weights"][i],"%",1)
        check("Lab 15 "+name,"Return",ret,100*result["return"],"%",2)
        check("Lab 15 "+name,"Volatility",vol,100*result["volatility"],"%",2)
    change=100*max(abs(x-y) for x,y in zip(outputs["Base"]["weights"],outputs["Equity 7%"]["weights"]))
    check("Lab 15","Largest weight move",25,change,"percentage points",1)
    return {"disclosure":model.AI_NOTICE+" "+model.EDUCATIONAL_NOTICE,
            "executed_at":datetime.now(ZoneInfo("America/New_York")).isoformat(),
            "scope":"Lab 14 and Lab 15 use the application's portfolio engine. Week 2 is a supplementary financial-arithmetic reconciliation.",
            "sources":SOURCES,"checks":checks}


def main():
    output=reconcile()
    (ROOT/"outputs/training-reconciliation.json").write_text(json.dumps(output,indent=2),encoding="utf-8")
    lines=[output["disclosure"],"", "# Published training reconciliation","",output["scope"],"",
           "Executed "+output["executed_at"],"",
           "| Case | Metric | Published | Computed | Unit | Status |",
           "|---|---|---:|---:|---|---|"]
    for row in output["checks"]:
        lines.append("| "+" | ".join(str(row[k]) for k in ["Case","Metric","Published","Computed","Unit","Status"])+" |")
    lines+=["","Each comparison uses the displayed precision in the published answer.",""]
    lines += [f"[{name}]({url})" for name,url in SOURCES.items()]
    (ROOT/"docs/training-reconciliation.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"PASS {len(output['checks'])} published training checks. See docs/training-reconciliation.md.")


if __name__=="__main__":
    main()
