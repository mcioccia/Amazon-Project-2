"""Independent finance and app checks. AI-assisted education. Not financial or investment advice."""
import itertools
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import numpy as np
import pandas as pd
from streamlit.testing.v1 import AppTest
import analysis as a
from portfolio import estimate_from_csv
import io


def main():
    print(a.NOTICE)
    prices = pd.read_csv(a.DATA/"prices.csv",comment="#",index_col=0)
    monthly = prices.pct_change().dropna()
    means = monthly.mean().to_numpy()*12
    cov = monthly.cov().to_numpy()*12
    # Stars and bars: independent enumeration of integer allocations summing to 20.
    bars = np.array(list(itertools.combinations(range(25),5)))
    grid = np.diff(np.column_stack([np.full(len(bars),-1),bars,np.full(len(bars),25)]),axis=1)/20 - 1/20
    assert len(grid)==53130 and np.allclose(grid.sum(axis=1),1)
    turnover = abs(grid - 1/6).sum(axis=1)/2
    net = grid@means - 0.001*turnover
    variance = np.einsum("ij,jk,ik->i",grid,cov,grid)
    eligible = (net>=0.0749-1e-12) & (grid[:,3]>=0.10-1e-12)
    winner = grid[np.argmin(np.where(eligible,variance,np.inf))]
    base = a.calculate(**a.BASE)
    constrained = base["results"]["Constrained"]
    np.testing.assert_allclose(winner,list(constrained["weights"].values()),atol=1e-12)
    assert eligible.sum()==base["feasible"]
    assert abs(np.sqrt(winner@cov@winner)-constrained["risk"])<1e-12
    equal=base["results"]["Equal weight"]
    assert abs(equal["net"]-means.mean())<1e-12 and equal["turnover"]==0
    assert base["results"]["Inverse volatility"]["verdict"]=="FAIL"
    print("PASS independent full grid, risk, costs, baseline and feasibility counts.")
    recovered=a.calculate(**(a.BASE|{"cost_bp":0}))["results"]["Constrained"]
    np.testing.assert_allclose(list(recovered["weights"].values()),[.1,.2,.05,.65,0,0])
    latest=a.signal()
    prior=a.signal(30)
    assert prior["month"]=="2026-08-01" and latest["month"]=="2026-09-01"
    assert latest["vintage"]=="2026-10-28" and prior["vintage"]<=prior["cutoff"]
    assert abs(latest["yoy"]-100*(336.298/324.245-1))<1e-10
    assert a.signal(60) is None
    assert a.calculate(**(a.BASE|{"reserve":90}))["results"]["Constrained"] is None
    try: estimate_from_csv(io.StringIO("Date,QQQ\n2026-01-31,10\n2026-03-31,11"))
    except ValueError: pass
    else: raise AssertionError("missing price month accepted")
    print("PASS Lab 15 parity, same-vintage CPI, publication cutoff, gap refusal and infeasibility.")
    snap=json.loads((a.ROOT/"outputs/committee-run.json").read_text())
    assert snap["base"]==base and snap["stresses"]==a.stress_runs()
    app=AppTest.from_file(str(a.ROOT/"app.py")).run(timeout=90)
    assert not app.exception and app.metric[0].value=="7.498%"
    assert len(app.dataframe[0].value)==3
    app.number_input[1].set_value(90.0).run(timeout=60)
    assert not app.exception and any("No eligible allocation" in w.value for w in app.warning)
    app.selectbox[1].select(60).run(timeout=60)
    assert not app.exception and any("No eligible CPI" in w.value for w in app.warning)
    print("PASS saved output reproducibility and operating the app through its controls.")

if __name__=="__main__":
    main()
