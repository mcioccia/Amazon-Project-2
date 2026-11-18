"""Reproducibility and regression checks. AI-assisted education, not investment advice."""
import copy
import io
import itertools
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

import numpy as np
import pandas as pd
from streamlit.testing.v1 import AppTest
import analysis as a
import portfolio as p
from reconcile import reconcile


def refused(call, message):
    try:
        call()
    except ValueError as error:
        assert message in str(error), str(error)
    else:
        raise AssertionError("Expected refusal: "+message)


def main():
    print(a.NOTICE)
    a.verify_inputs()
    assert all(row["Status"]=="PASS" for row in reconcile()["checks"])
    print("PASS published Week 2, Lab 14 and Lab 15 reconciliations.")
    prices=pd.read_csv(a.DATA/"prices.csv",comment="#",index_col=0)
    monthly=prices.pct_change(fill_method=None).dropna()
    means=monthly.mean().to_numpy()*12
    cov=monthly.cov().to_numpy()*12
    bars=np.array(list(itertools.combinations(range(25),5)))
    grid=np.diff(np.column_stack([np.full(len(bars),-1),bars,np.full(len(bars),25)]),axis=1)/20-1/20
    assert len(grid)==53130 and np.allclose(grid.sum(axis=1),1)
    turnover=abs(grid-1/6).sum(axis=1)/2
    net=grid@means-.001*turnover
    risk=np.sqrt(np.einsum("ij,jk,ik->i",grid,cov,grid))
    eligible=(net>=.0749-1e-12)&(grid[:,3]>=.10-1e-12)&(risk<=.10+1e-12)
    winner=grid[np.argmin(np.where(eligible,risk,np.inf))]
    base=a.calculate(**a.BASE); chosen=base["results"]["Constrained"]
    np.testing.assert_allclose(winner,list(chosen["weights"].values()),atol=1e-12)
    assert eligible.sum()==base["feasible"]==655
    assert abs(np.sqrt(winner@cov@winner)-chosen["risk"])<1e-12
    equal=base["results"]["Equal weight"]
    assert abs(equal["net"]-means.mean())<1e-12 and equal["turnover"]==0
    assert equal["verdict"]=="FAIL" and equal["rules"]==["Annual volatility above limit"]
    assert base["results"]["Inverse volatility"]["verdict"]=="FAIL"
    assert chosen["verdict"]=="PASS"
    print("PASS independent 53,130-mix enumeration, covariance, risk ceiling and 655 feasible mixes.")
    latest=a.signal();prior=a.signal(30)
    assert prior["month"]=="2026-08-01" and latest["month"]=="2026-09-01"
    assert latest["vintage"]=="2026-10-28" and prior["vintage"]<=prior["cutoff"]
    assert abs(latest["yoy"]-100*(336.298/324.245-1))<1e-10
    assert a.signal(60) is None
    assert a.calculate(**(a.BASE|{"reserve":90}))["results"]["Constrained"] is None
    refused(lambda:p.estimate_from_csv(io.StringIO("Date,QQQ\n2026-01-31,10\n2026-03-31,11")),"consecutive")
    refused(lambda:p.validate_correlations([[1,.9,.9],[.9,1,-.9],[.9,-.9,1]],3),"positive semidefinite")
    refused(lambda:p.one_way_turnover([.5,.5],[1]),"one finite")
    refused(lambda:a.calculate(vol_limit=float("nan")),"bounds")
    with TemporaryDirectory() as folder:
        temporary=Path(folder)
        text=(a.DATA/"prices.csv").read_text()
        # A defect before the chosen 24 months must also be refused.
        damaged=text.replace("2021-10-29","2021-09-29")
        (temporary/"prices.csv").write_text(damaged)
        with patch.object(a,"DATA",temporary):
            refused(lambda:a.estimates(24),"consecutive")
        (temporary/"prices.csv").write_text(text)
        archive=json.loads((a.DATA/"cpi-vintages.json").read_text())
        newest=max(archive["snapshots"],key=lambda row:row["effective_vintage"])
        newest["data"].append({"date":"2026-10-01","value":None})
        (temporary/"cpi-vintages.json").write_text(json.dumps(archive))
        with patch.object(a,"DATA",temporary):
            assert a.signal()["month"]=="2026-09-01"
        newest["data"].append({"date":"2026-09-01","value":336.298})
        (temporary/"cpi-vintages.json").write_text(json.dumps(archive))
        with patch.object(a,"DATA",temporary):
            refused(lambda:a.signal(),"Duplicate CPI")
    print("PASS failures: missing month, impossible covariance, invalid weights/risk, duplicate CPI; trailing missing CPI handled.")
    snap=json.loads((a.ROOT/"outputs/committee-run.json").read_text())
    assert snap["base"]==base and snap["stresses"]==a.stress_runs()
    assert snap["source_sha256"]==a.input_hashes()
    before=copy.deepcopy(a.BASE)
    exported=a.scenario_record(a.BASE|{"window":36})
    assert exported["inputs"]["window"]==36 and exported["output"]["results"]["Constrained"]["reserve"]==.85
    assert a.BASE==before
    print("PASS saved evidence reproducibility, actual changed-scenario export and independent base settings.")
    app=AppTest.from_file(str(a.ROOT/"app.py")).run(timeout=90)
    assert not app.exception,app.exception
    assert app.metric[0].value=="7.498%"
    assert app.dataframe[0].value["Verdict"].tolist()==["FAIL","FAIL","PASS"]
    app.selectbox(key="window").select(36).run(timeout=60)
    assert not app.exception and app.metric[3].value=="85%"
    app.button[0].click().run(timeout=60)
    assert app.selectbox(key="window").value==59 and app.metric[3].value=="65%"
    app.number_input(key="reserve").set_value(90.0).run(timeout=60)
    assert not app.exception and any("No eligible allocation" in w.value for w in app.warning)
    app.selectbox(key="lag").select(60).run(timeout=60)
    assert not app.exception and any("No eligible CPI" in w.value for w in app.warning)
    app.button[0].click().run(timeout=60)
    assert not app.exception and app.metric[0].value=="7.498%"
    print("PASS app base, 36-month window, infeasible mandate, missing vintage and full reset.")


if __name__=="__main__":
    main()
