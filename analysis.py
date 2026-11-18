"""Project 2 committee analysis. AI-assisted coursework. Not financial or investment advice."""
import argparse
import math
import hashlib
from datetime import date, timedelta
import io
import json
from pathlib import Path

import portfolio as lab

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
FUNDS = ["QQQ", "ONEQ", "VUG", "BIL", "IEF", "LQD"]
BENCH = [1 / 6] * 6
AS_OF = "2026-10-30"
NOTICE = lab.AI_NOTICE + " " + lab.EDUCATIONAL_NOTICE
BASE = dict(target=7.49, reserve=3.0, window=59, cost_bp=10.0, qqq_shift=0.0, lag=0, vol_limit=10.0)
STRESSES = {"QQQ estimate −1 point": {"qqq_shift": -1.0},
            "36-month window": {"window": 36}, "48-month window": {"window": 48},
            "Cost 50 bp": {"cost_bp": 50.0}, "BIL minimum 90%": {"reserve": 90.0},
            "Prior CPI vintage (30-day lag)": {"lag": 30}}


def estimates(window):
    rows = [s for s in (DATA/"prices.csv").read_text(encoding="utf-8-sig").splitlines()
            if s.strip() and not s.startswith("#")]
    if not 12 <= window <= len(rows) - 2:
        raise ValueError("Window must fit the available monthly returns.")
    # Reject defects anywhere in the input panel before selecting a shorter window.
    lab.estimate_from_csv(io.StringIO("\n".join(rows)))
    if rows[0].split(",") != ["Date"] + FUNDS:
        raise ValueError("Unexpected fund universe or ordering.")
    if rows[-1].split(",")[0] > AS_OF:
        raise ValueError("Price date exceeds the decision cutoff.")
    return lab.estimate_from_csv(io.StringIO("\n".join([rows[0], *rows[-(window+1):]])))


def signal(lag=0):
    cutoff = date.fromisoformat(AS_OF) - timedelta(days=lag)
    archive = json.loads((DATA/"cpi-vintages.json").read_text(encoding="utf-8"))
    eligible = [s for s in archive["snapshots"] if date.fromisoformat(s["effective_vintage"]) <= cutoff]
    if not eligible:
        return None
    snap = max(eligible, key=lambda s:s["effective_vintage"])
    points = {}
    for row in snap["data"]:
        observed = date.fromisoformat(row["date"])
        value = row["value"]
        if value is None:
            continue
        if not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
            raise ValueError("CPI levels must be finite and positive.")
        if observed.isoformat() in points:
            raise ValueError("Duplicate CPI observation in one vintage.")
        if observed <= cutoff:
            points[observed.isoformat()] = value
    if not points:
        return None
    end = max(points)
    prior = (date.fromisoformat(end).replace(year=int(end[:4])-1)).isoformat()
    if prior not in points or points[prior] <= 0:
        return None
    yoy = 100 * (points[end] / points[prior] - 1)
    return dict(vintage=snap["effective_vintage"],requested=snap["vintage"],download=snap["downloaded_at"],
                cutoff=str(cutoff),month=end,level=points[end],prior_month=prior,prior=points[prior],yoy=yoy,
                floor=10.0 if yoy >= 3.0 else 0.0,source=snap["url"])


def calculate(target=7.49, reserve=3.0, window=59, cost_bp=10.0, qqq_shift=0.0, lag=0, vol_limit=10.0):
    if not (0 <= target <= 40 and 0 <= reserve <= 100 and 0 <= cost_bp <= 200
            and -15 <= qqq_shift <= 15 and 0 <= lag <= 90
            and 0 < vol_limit <= 50):
        raise ValueError("Setting outside committee scenario bounds.")
    sig = signal(lag)
    if sig is None:
        return dict(signal=None, results={}, floor=None, stop="No eligible CPI vintage. Pause the search.")
    floor = max(reserve, sig["floor"]) / 100
    data = estimates(window)
    sleeves = [dict(s, reserve_eligible=(s["name"]=="BIL")) for s in data["sleeves"]]
    sleeves[0]["return"] += qqq_shift / 100
    vols = [s["volatility"] for s in sleeves]
    means = [s["return"] for s in sleeves]
    cov = lab.build_covariance_matrix(vols, data["correlations"])
    start = lab.equal_weights(len(sleeves))
    cost_rate = cost_bp / 10000
    mix = lab.search_portfolios(sleeves, data["correlations"], target/100, floor,
                                starting_weights=start, switching_cost=cost_rate, volatility_limit=vol_limit/100)
    def measure(weights):
        gross = lab.portfolio_return(weights, means)
        turnover = lab.one_way_turnover(weights,start)
        cost = turnover * cost_rate
        net = gross - cost
        bil = lab.reserve_eligible_weight(weights,sleeves)
        risk = lab.portfolio_volatility(weights,cov)
        failed = []
        if not lab.meets_objective(net,target/100):
            failed.append("First-year net return below objective")
        if bil + lab.TOLERANCE < floor:
            failed.append("BIL below effective reserve minimum")
        if risk > vol_limit/100 + lab.TOLERANCE:
            failed.append("Annual volatility above limit")
        return dict(weights=dict(zip(FUNDS, weights)), gross=gross, net=net, risk=risk,
                    reserve=bil, turnover=turnover, cost=cost, verdict="FAIL" if failed else "PASS", rules=failed)
    results = {"Equal weight":measure(start),"Inverse volatility":measure(lab.inverse_volatility_weights(vols)),
               "Constrained":measure(mix["weights"]) if mix else None}
    return dict(signal=sig,floor=floor,results=results,
                feasible=mix["feasible"] if mix else 0, estimate_start=data["return_start"],
                estimate_end=data["return_end"], stop=None if mix else "No eligible allocation. Pause allocation.")


def stress_runs():
    return {name:calculate(**(BASE | change)) for name,change in STRESSES.items()}



def input_hashes():
    return {name: hashlib.sha256((DATA / name).read_bytes()).hexdigest()
            for name in ("prices.csv", "cpi-vintages.json")}


def verify_inputs():
    ledger = json.loads((DATA / "source-ledger.json").read_text(encoding="utf-8"))
    for name, actual in input_hashes().items():
        if ledger["files"][name]["sha256"] != actual:
            raise ValueError(f"{name} differs from the documented snapshot. Review its provenance before use.")


def scenario_record(settings):
    verify_inputs()
    return dict(disclosure=NOTICE, decision_as_of=AS_OF,
                mandate_updated="2026-11-18", inputs=dict(settings),
                source_sha256=input_hashes(), output=calculate(**settings))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--target",type=float,default=BASE["target"])
    p.add_argument("--reserve",type=float,default=BASE["reserve"])
    p.add_argument("--window",type=int,default=BASE["window"])
    p.add_argument("--cost-bp",type=float,default=BASE["cost_bp"])
    p.add_argument("--qqq-shift",type=float,default=BASE["qqq_shift"])
    p.add_argument("--lag",type=int,default=BASE["lag"])
    p.add_argument("--vol-limit",type=float,default=BASE["vol_limit"])
    args = vars(p.parse_args())
    verify_inputs()
    print(json.dumps(scenario_record(args),indent=2))

if __name__ == "__main__":
    main()
