"""AI-assisted coursework presentation. Educational only; not investment advice."""
from pathlib import Path
import csv
import hashlib
import html
import json
import math
import re

ROOT = Path(__file__).resolve().parent
NOTICE = 'Built with OpenAI Codex assistance. Educational only; not financial or investment advice.'


def build():
    record = json.loads((ROOT/'outputs/committee-run.json').read_text(encoding='utf-8'))
    base = record['base']
    chosen = base['results']['Constrained']
    changed = json.loads((ROOT/'outputs/cost15-changed.json').read_text(encoding='utf-8'))['output']['results']['Constrained']
    raw = (ROOT/'data/prices.csv').read_text(encoding='utf-8-sig')
    prices = list(csv.DictReader(line for line in raw.splitlines() if line and not line.startswith('#')))
    p0, p1 = float(prices[-2]['QQQ']), float(prices[-1]['QQQ'])
    monthly = (p1/p0-1)*100
    # Refuse to retain stale spoken figures if the evidence changes.
    assert f'{chosen["net"]*100:.3f}' == '7.498'
    assert f'{chosen["risk"]*100:.3f}' == '7.241'
    assert f'{changed["risk"]*100:.3f}' == '7.245'
    assert f'{chosen["cost"]*100000:.2f}' == '48.33'
    assert base['feasible'] == 655 and f'{base["signal"]["yoy"]:.2f}' == '3.72'
    assert f'{monthly:.2f}' == '3.32'

    scenes = [
      dict(nav='Inputs', time='0:00–0:40', title='A decision begins with its boundaries.',
           label='APPROVED BASE', metric='7.49% / 10%', detail='Net return target / annual volatility ceiling',
           facts=[('Universe', '6 funds'), ('Information cutoff', '30 Oct 2026'), ('Mandate approval', '18 Nov 2026')],
           note='A retrospective paper exercise. File fingerprints identify the saved input snapshot.',
           blocks=[('analysis.py', [(14,18),(122,126)])],
           cue='Point to FUNDS, AS_OF and BASE, then the fingerprint check.',
           speech=["I used OpenAI Codex to build, test, and help explain this app. The analysis and decision are mine.",
                   "This is an educational project, not financial or investment advice.",
                   "I'll trace the actual code from prices to the portfolio verdict. These six funds are the universe. The base sets a 7.49 percent net return target and a ten percent volatility ceiling. The information cutoff is October thirtieth; the mandate approval came later. This is a retrospective paper exercise. The fingerprint check refuses an undocumented change to the saved data."]),
      dict(nav='Returns', time='0:40–1:15', title='Prices become estimates, not promises.',
           label='QQQ · SEPTEMBER 2026', metric=f'+{monthly:.2f}%', detail='One monthly return from adjusted closes',
           facts=[('August month-end', f'${p0:,.2f}'), ('September month-end', f'${p1:,.2f}'), ('Prices → returns', f'{len(prices)} → {len(prices)-1}')],
           note='The model uses full precision. The two prices shown here are rounded to cents.',
           blocks=[('portfolio.py',[(325,331),(337,340)])],
           cue='Point to current / prior − 1, then mean × 12 and stdev × √12.',
           speech=["Here, current price divided by prior price, minus one, gives a monthly return. My checked QQQ example goes from 716.01 to 739.77, about 3.32 percent. Sixty prices give 59 returns. The code annualizes the average by multiplying by twelve, and sample standard deviation by the square root of twelve. It estimates correlations over the same months. These are historical estimates, not promised returns."]),
      dict(nav='Risk', time='1:15–1:45', title='Risk includes how the funds move together.',
           label='BASE PORTFOLIO RISK', metric=f'{chosen["risk"]*100:.3f}%', detail='Annualized standard deviation of the mix',
           facts=[('Covariance', 'Correlation × both volatilities'), ('Variance', 'Sum every weighted pair'), ('Volatility', 'Square root of variance')],
           note='A 10% volatility ceiling is not a guarantee that losses stay below 10%.',
           blocks=[('portfolio.py',[(88,92),(127,135)])],
           cue='Trace correlation × volatility × volatility, both weights, and the square root.',
           speech=["Correlation times both volatilities gives covariance. The next block multiplies every covariance by both portfolio weights and adds all the pairs, including each fund with itself. The square root gives portfolio volatility. Funds that move together can add similar risk, even with different tickers. The base is 7.241 percent. The ten percent ceiling limits this estimate; it does not guarantee a maximum loss."]),
      dict(nav='CPI cutoff', time='1:45–2:20', title='Use the vintage available at the cutoff.',
           label='ARCHIVED CPI SIGNAL', metric=f'{base["signal"]["yoy"]:.2f}%', detail='September year-over-year CPI inflation',
           facts=[('Returned vintage', base['signal']['vintage']), ('Decision cutoff', base['signal']['cutoff']), ('Effective BIL floor', f'{base["floor"]:.0%}')],
           note='The rule uses the latest eligible saved vintage. It does not claim an intraday release time.',
           blocks=[('analysis.py',[(40,45),(64,64),(67,67),(78,78)])],
           cue='Point to ≤ cutoff, max eligible vintage, year-over-year change, and max reserve floor.',
           speech=["The CPI function first removes archived vintages after the cutoff, then selects the latest eligible one. Both index levels come from that same vintage. September inflation is 3.72 percent. That activates the ten percent BIL floor instead of the normal three percent minimum. Missing eligible evidence pauses the search. The date is the archived vintage, not a claim about the first release time. At base, 65 percent BIL already exceeds this floor."]),
      dict(nav='Costs', time='2:20–2:55', title='Charge the dollars switched, once.',
           label='PERSONAL CALCULATION CHECK', metric=f'${chosen["cost"]*100000:.2f}', detail='Initial switching cost on a $100,000 account',
           facts=[('One-way turnover', f'{chosen["turnover"]:.3%}'), ('Base cost rate', '10 bp = 0.001'), ('Net = gross − cost', f'{chosen["gross"]*100:.3f}% − {chosen["cost"]*100:.5f} pp')],
           note='The assumption covers the switch once. Taxes, later rebalances and ongoing fees need separate review.',
           blocks=[('portfolio.py',[(227,230)]),('analysis.py',[(86,86),(90,95)])],
           cue='Point to absolute weight changes ÷ 2, bp ÷ 10,000, cost, then net.',
           speech=["Starting holdings are equal weight. One-way turnover is half the sum of absolute weight changes, so the buy and sell sides are not counted twice. The base switches 48.333 percent. Ten basis points becomes 0.001. Multiply turnover by that rate and a hundred-thousand-dollar account: 48 dollars and 33 cents. Subtract the cost from gross expected return. This is the initial switch; it does not cover every future expense."]),
      dict(nav='Search', time='2:55–3:45', title='Reject failures. Keep the lowest-risk survivor.',
           label='ELIGIBLE BASE MIXES', metric=f'{base["feasible"]:,}', detail=f'From {math.comb(25,5):,} fully invested, long-only mixes',
           facts=[('Weight increment', '5 percentage points'), ('Eligibility', 'Net return + reserve + risk'), ('Objective', 'Lowest estimated volatility')],
           note='This is the minimum on a 5-point grid. It is not a continuous optimum or full suitability approval.',
           blocks=[('portfolio.py',[(266,280)])],
           cue='Trace weights → net → continue → risk → continue → best. Click a line to highlight it.',
           speech=["The loop distributes twenty units across six funds. Each unit is five percentage points, so weights add to one hundred percent without shorting. For each candidate, it calculates return, reserve, costs, and risk. Continue skips a failing mix. The best variable changes only when an eligible mix has lower volatility. Of 53,130 candidates, 655 pass at base. This is the best mix on the grid, not every possible allocation. My fifteen-basis-point test reran this whole search. It moved five points from VUG to ONEQ and produced 7.245 percent volatility."]),
      dict(nav='Verdict', time='3:45–4:25', title='A failed search is a visible decision.',
           label='BASE MANDATE VERDICT', metric='PASS · PILOT', detail=f'{chosen["net"]*100:.3f}% net · {chosen["risk"]*100:.3f}% volatility · {chosen["reserve"]:.0%} BIL',
           facts=[('Equal weight', 'FAIL · risk above 10%'), ('Inverse volatility', 'FAIL · return below target'), ('Require 90% BIL', 'PAUSE · no eligible mix')],
           note='43 published training checks passed. Passing modeled rules supports a paper pilot, not automatic funding.',
           blocks=[('app.py',[(89,91),(102,103),(113,114),(153,155)])],
           cue='Point to input-error stop, the no-mix warning, displayed results and exported settings.',
           speech=["The app displays the engine's results and exports the actual settings with the output. Equal weight fails the risk ceiling; inverse volatility misses the return target. The constrained mix passes, but its return cushion is thin. Requiring ninety percent BIL leaves no eligible mix, so the app says pause. Invalid input evidence also stops the app. Forty-three published training checks passed, and the cost test was independently recalculated. I still recommend a paper pilot, with forward results and the stated review triggers before funding."]),
    ]
    source_hashes={}
    for scene in scenes:
        scene['code']=[]
        for name,ranges in scene.pop('blocks'):
            lines=(ROOT/name).read_text(encoding='utf-8').splitlines()
            source_hashes[name]=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            entries=[]
            for k,(lo,hi) in enumerate(ranges):
                if k: entries.append(dict(number=None,text='… omitted lines …'))
                entries += [dict(number=n,text=lines[n-1]) for n in range(lo,hi+1)]
            scene['code'].append(dict(file=name,lines=entries))
    speech='\n\n'.join(p for s in scenes for p in s['speech'])+'\n'
    words=len(speech.split())
    payload=json.dumps(scenes,ensure_ascii=False).replace('</','<\\/')
    page=TEMPLATE.replace('%%CSS%%',CSS).replace('%%DATA%%',payload).replace('%%JS%%',JS)
    (ROOT/'Video-2-Dashboard.html').write_text(page,encoding='utf-8')
    (ROOT/'docs/video-2-word-for-word-script.md').write_text(speech,encoding='utf-8')
    guide=f'''I used OpenAI Codex to prepare this code walkthrough and verify its displayed source excerpts. The analysis and decision are mine.

This is an educational project, not financial or investment advice.

# Video 2 — Code walkthrough and recording guide

Updated November 19, 2026. **Draft narration, not an actual transcript.** {words} words. Aim for **4:25–4:45** including clicks; hard maximum **5:00**. Rehearse your actual pace before recording.

## Open and prepare

1. Open `Video-2-Dashboard.html` in your Project 2 folder, or [the local preview](http://127.0.0.1:8507/Video-2-Dashboard.html) while the preview server is running. This is a saved code walkthrough; Video 3 is the live app demonstration.
2. Click **Reset** then **Full screen**. Start on **Inputs**. The source excerpts and line numbers come directly from the current Python files; skipped lines are explicitly marked. Click any source line to highlight it while explaining. **Full source** opens the complete file in a dialog for rehearsal; it is not a required timed click.
3. In OBS, capture this browser window, turn on your microphone and webcam, and place the webcam over the reserved box on the right. Keep your face visible for the whole recording. The box itself does not turn on a camera.
4. Open the [word-for-word spoken script](video-2-word-for-word-script.md) on a second screen or print it. Only read the spoken paragraphs; do not read click instructions. Use **Show script** during rehearsal, then hide it for the final take.
5. Record a short audio/face/readability check. Turn off notifications. Start OBS recording, then click **Start rehearsal** and read the first disclosure immediately. The dashboard timer does not record or advance the scenes.

## Exact click route

Click the next named tab after finishing the current passage. Right Arrow and **Next →** follow the same route. The times are rehearsal targets, not measured recording timestamps.

| Target time | Click | Point at |
|---|---|---|
'''
    for s in scenes:
        guide+=f'| {s["time"]} | **{s["nav"]}** | {s["cue"]} |\n'
    guide+='\n## Say exactly\n\n'
    for s in scenes:
        guide+=f'### {s["time"]} · {s["nav"]}\n\n**Click:** {s["nav"]}. **Point:** {s["cue"]}\n\n**Say exactly:**\n\n'+'\n\n'.join(s['speech'])+'\n\n'
    guide+='''## Finish and submit

After the final sentence, stop OBS before 5:00. Your face must stay visible throughout. Replay the recording to check readable code, audio and actual runtime. Upload it to YouTube as Unlisted, publish corrected captions, and check the link while signed out. Send the actual video link and exported captions for correction; the completed transcript belongs at `docs/transcript-video-2.txt`. Do not rename this rehearsal script as the recorded transcript.

The video should show you explaining how the code works. Each screen includes a financial interpretation, source lines and a calculated result. Do not claim that volatility caps losses, that the grid explores every possible weight, or that the archived vintage is the first release timestamp.

## Evidence and reproducibility

[Base and stresses](../outputs/committee-run.json) · [Locked test result](../outputs/cost15-changed.json) · [Personal source/calculation check](student-evidence.md) · [Training reconciliation](training-reconciliation.md) · [Point-in-time data card](data-card.md) · [Manifest](manifest.md)

`build_video2.py` rebuilds this dashboard, narration and guide from saved results and current source excerpts. It does not change model assumptions, financial source files or the locked prediction. The source fingerprints in `outputs/video2-presentation-sources.json` identify the displayed implementation.

[Project 2 directions](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md) · [Length and submission checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md)
'''
    (ROOT/'docs/video-2-recording-guide.md').write_text(guide,encoding='utf-8')
    manifest=dict(disclosure=NOTICE,prepared='2026-11-19',spoken_words=words,source_sha256=source_hashes,
                  inputs={str(p):hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['outputs/committee-run.json','outputs/cost15-changed.json','data/prices.csv']})
    (ROOT/'outputs/video2-presentation-sources.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(NOTICE)
    print(f'Built seven scenes, {words} spoken words, matching guide and source fingerprints.')


CSS = '''
*{box-sizing:border-box}html{color-scheme:light}body{margin:0;background:#eef1ed;color:#15363c;font:15px/1.4 'Segoe UI',Arial,sans-serif;font-variant-numeric:tabular-nums}button,a{touch-action:manipulation}button{font:inherit;cursor:pointer;border:1px solid #b8cac3;background:#fffdf6;color:#173a3f;border-radius:6px;padding:7px 12px}button:hover{background:#e3eee7}button:focus-visible,a:focus-visible{outline:3px solid #b97535;outline-offset:3px}button:disabled{opacity:.4;cursor:default}header{background:#12343b;color:#fffdf5;border-bottom:3px solid #bf8c51}.head{max-width:1450px;margin:auto;display:flex;align-items:center;justify-content:space-between;padding:10px 24px;gap:15px}.brand{letter-spacing:.12em;font-size:12px;font-weight:700}.controls{display:flex;gap:7px;align-items:center}.controls button{background:#244a50;color:#fff;border-color:#547475;font-size:12px}.timer{font:24px Georgia,serif;min-width:54px}.timer.warn{color:#ffcf8a}.timer.over{color:#ff9d9d}.limit{font-size:10px;letter-spacing:.1em;color:#b9cdc9}main{max-width:1450px;margin:auto;padding:15px 24px 0}nav{display:flex;gap:6px}nav button{border:0;background:transparent;padding:8px 13px;font-size:13px;font-weight:600}nav button[aria-current=step]{background:#194e51;color:white}nav small{opacity:.6;margin-right:7px}.metadata{display:flex;justify-content:space-between;font-size:10px;letter-spacing:.06em;color:#60726b;margin:9px 0 12px}.heading{display:flex;justify-content:space-between;align-items:center;margin:0 0 10px}h1{font:normal clamp(27px,2.7vw,41px)/1.1 Georgia,serif;letter-spacing:-.025em;margin:0}.step{font:italic 27px Georgia,serif;color:#9aab9f}h2{font-size:18px}.layout{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:20px;align-items:stretch}.mainpane{min-width:0}.code{background:#12343b;color:#f5f4e9;border-radius:9px;border:1px solid #315159;height:402px;overflow:auto;padding:12px 14px;scrollbar-color:#547375 #12343b}.filename{display:flex;justify-content:space-between;align-items:center;color:#b0dacf;font:12px Consolas,monospace;border-bottom:1px solid #35565b;padding:0 0 8px;margin-bottom:8px}.filename a{color:#b0dacf;text-decoration:none}.filename:not(:first-child){margin-top:12px}.code button{padding:1px 8px;color:#d4eae1;background:#234a50;border-color:#4d7073;font-size:11px}.line{display:grid;grid-template-columns:29px 1fr;gap:12px;padding:0 5px;border-radius:3px;cursor:pointer}.line .n{font:12px/20px Consolas,monospace;color:#8eaeb0;text-align:right;user-select:none}.line code{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/20px Consolas,'Courier New',monospace}.line.active{background:#365c58;box-shadow:inset 3px 0 #e7bc7b}.kw{color:#edc38b}.str{color:#b1d9c0}.comment{color:#8faeae}.gap{font:11px Consolas,monospace;color:#91aaa8;padding:4px 46px}.under{margin:8px 0 0;display:flex;gap:10px;justify-content:space-between;font-size:11px;color:#61746c}.cue{background:#f8f5e9;border-left:3px solid #b98345;padding:10px 13px;margin-top:9px;font-size:13px}.aside{display:flex;flex-direction:column;min-width:0}.card{background:#fcfcf6;border:1px solid #cedbd0;border-radius:8px;padding:16px}.eyebrow{font-size:10px;font-weight:700;letter-spacing:.11em;color:#5c7770}.metric{font:32px/1.1 Georgia,serif;margin:8px 0;color:#155452}.detail{font-size:13px;color:#52716c;margin:0 0 10px}.fact{display:flex;justify-content:space-between;gap:14px;padding:7px 0;border-bottom:1px solid #e1e6dd;font-size:12px}.fact:last-child{border:0}.fact strong{text-align:right}.note{font-size:12px;line-height:1.45;padding:10px 2px;margin:0;color:#536d64}.webcam{height:127px;flex-shrink:0;margin-top:auto;border:1px dashed #799d8e;border-radius:8px;background:#e4ebe1;display:grid;place-content:center;text-align:center;color:#45675c}.webcam strong{font-size:13px}.webcam small{font-size:10px;display:block;margin-top:5px}.disclosure{font-size:11px;color:#5b6f65;margin:9px 0}.footer{display:flex;justify-content:space-between;align-items:center;margin:9px 0 12px;gap:10px}.footer small{color:#61756c;font-size:11px}#next{background:#175654;color:white}.intro{font-size:12px;border-left:3px solid #bc8b50;padding-left:10px;margin:0 0 10px}.intro p{margin:2px 0}.notes{position:fixed;right:18px;top:66px;bottom:20px;width:min(450px,92vw);overflow:auto;z-index:10;background:#fffdf4;border:1px solid #aabeb2;box-shadow:0 8px 50px #142d3d55;border-radius:10px;padding:22px}.notes p{font-size:17px;line-height:1.65}.notes button{float:right}dialog{width:min(1000px,94vw);max-height:88vh;border:1px solid #708f85;border-radius:10px;background:#fffdf5;color:#14343b;padding:22px}dialog::backdrop{background:#102b35aa}dialog pre{white-space:pre-wrap;font:14px/1.5 Consolas,monospace}dialog button{float:right}[hidden]{display:none!important}.sr-only{position:absolute;left:0;top:0;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}@media(min-width:1000px) and (max-height:800px){main{padding-top:10px}.metadata{margin:6px 0 9px}.code{height:369px}.layout{min-height:487px}.line code{font-size:13px;line-height:18px}.line .n{line-height:18px}.intro{font-size:11px}.webcam{height:113px}.card{padding:13px}.metric{font-size:29px}.note{font-size:11px}.cue{padding:8px 12px}}@media(min-height:801px){.layout{min-height:520px}}@media(max-width:850px){.head{flex-wrap:wrap}.layout{grid-template-columns:1fr}.code{height:auto;max-height:500px}nav{flex-wrap:wrap}.metadata{flex-wrap:wrap}.webcam{margin-top:10px}.heading{gap:15px}.controls{flex-wrap:wrap}h1{font-size:29px}main{padding:12px}.intro{font-size:12px}}
'''

TEMPLATE='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Project 2 · Video 2 · Inside the engine</title><style>%%CSS%%</style></head><body>
<header><div class="head"><div class="brand">PORTFOLIO COMMITTEE &nbsp; / &nbsp; INSIDE THE ENGINE</div><div class="controls"><span class="limit">LIMIT 5:00</span><span id="timer" class="timer">0:00</span><button id="start">Start rehearsal</button><button id="reset">Reset</button><button id="notes-toggle" aria-pressed="false">Show script</button><button id="full">Full screen</button></div></div></header>
<main><nav id="nav" aria-label="Recording scenes"></nav><div class="metadata"><span>VIDEO 2 · ACTUAL SOURCE WALKTHROUGH</span><span>INFORMATION SNAPSHOT 30 OCT 2026 · PREPARED 19 NOV 2026</span></div><div class="heading"><h1 id="title"></h1><span class="step" id="step"></span></div>
<div class="layout"><section class="mainpane"><div id="intro" class="intro"><p>I used OpenAI Codex to build, test, and help explain this app. The analysis and decision are mine.</p><p>This is an educational project, not financial or investment advice.</p></div><div class="code" id="code" aria-label="Python source excerpts"></div><div class="under"><span>Exact source lines · omitted lines marked · click a line to highlight</span><span id="range"></span></div><div class="cue" id="cue"></div></section><aside class="aside"><div class="card"><div class="eyebrow" id="label"></div><div class="metric" id="metric"></div><p class="detail" id="detail"></p><div id="facts"></div></div><p class="note" id="note"></p><div class="webcam"><strong>Your webcam here</strong><small>Use your actual camera overlay · face visible throughout</small></div></aside></div>
<p class="disclosure">AI-assisted educational demonstration · Not financial or investment advice · Saved source and results; the live app demonstration is Video 3.</p><div class="footer"><small>← → scenes · N script · T timer · Reset between takes</small><div><button id="back">Back</button> <button id="next">Next →</button></div></div></main>
<aside id="notes" class="notes" hidden><button id="close-notes">Close script</button><h2 id="notes-title"></h2><div id="speech"></div></aside><dialog id="source-dialog"><button id="close-source">Close source</button><h2 id="source-title"></h2><p>Full file from the source snapshot used to build this presentation.</p><pre id="full-source"></pre></dialog><div id="status" class="sr-only" aria-live="polite"></div>
<script id="scene-data" type="application/json">%%DATA%%</script><script>%%JS%%</script></body></html>'''

JS='''
const scenes=JSON.parse(document.getElementById('scene-data').textContent),$=id=>document.getElementById(id);let index=0,elapsed=0,running=false,started=0;
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
function syntax(s){return esc(s).replace(/(&quot;.*?&quot;|'.*?'|\\b(?:return|if|else|for|in|def|None|True|False|or|and|not|with|as|try|except|raise|continue)\\b)/g,t=>`<span class="${t.startsWith('&quot;')||t.startsWith("'")?'str':'kw'}">${t}</span>`)}
scenes.forEach((s,i)=>{let b=document.createElement('button');b.innerHTML=`<small>${String(i+1).padStart(2,'0')}</small>${esc(s.nav)}`;b.onclick=()=>show(i);$('nav').append(b)});
function show(i){index=Math.max(0,Math.min(i,scenes.length-1));let s=scenes[index];['title','label','metric','detail','note','cue'].forEach(k=>$(k).textContent=s[k]);$('step').textContent=`0${index+1} / 07`;$('range').textContent=s.time+' · rehearsal target';$('intro').hidden=index!==0;$('facts').innerHTML=s.facts.map(([a,b])=>`<div class="fact"><span>${esc(a)}</span><strong>${esc(b)}</strong></div>`).join('');$('code').innerHTML=s.code.map(b=>`<div class="filename"><a href="${esc(b.file)}" target="_blank">${esc(b.file)}</a><button data-file="${esc(b.file)}">Full source</button></div>`+b.lines.map(l=>l.number===null?`<div class="gap">${esc(l.text)}</div>`:`<div class="line" data-file="${esc(b.file)}" data-line="${l.number}"><span class="n">${l.number}</span><code>${syntax(l.text)}</code></div>`).join('')).join('');$('code').scrollTop=0;$('code').querySelectorAll('.line').forEach(l=>l.onclick=()=>{document.querySelectorAll('.line.active').forEach(x=>x.classList.remove('active'));l.classList.add('active')});$('code').querySelectorAll('button[data-file]').forEach(b=>b.onclick=()=>openSource(b.dataset.file));$('notes-title').textContent=s.nav;$('speech').innerHTML=s.speech.map(p=>`<p>${esc(p)}</p>`).join('');$('notes').scrollTop=0;[...$('nav').children].forEach((b,j)=>j===index?b.setAttribute('aria-current','step'):b.removeAttribute('aria-current'));$('back').disabled=index===0;$('next').disabled=index===scenes.length-1;$('status').textContent=`Scene ${index+1}: ${s.nav}`;window.scrollTo(0,0)}
function notes(){let open=$('notes').hidden;$('notes').hidden=!open;$('notes-toggle').textContent=open?'Hide script':'Show script';$('notes-toggle').setAttribute('aria-pressed',String(open))}
function toggleTimer(){if(running){elapsed+=(Date.now()-started)/1000;running=false}else{started=Date.now();running=true}$('start').textContent=running?'Pause timer':'Resume timer';tick()}
function tick(){let s=Math.floor(elapsed+(running?(Date.now()-started)/1000:0));$('timer').textContent=`${Math.floor(s/60)}:${String(s%60).padStart(2,'0')}`;$('timer').classList.toggle('warn',s>=275&&s<300);$('timer').classList.toggle('over',s>=300)}
$('start').onclick=toggleTimer;$('reset').onclick=()=>{running=false;elapsed=0;$('start').textContent='Start rehearsal';tick();if(!$('notes').hidden)notes();show(0)};$('notes-toggle').onclick=notes;$('close-notes').onclick=notes;$('back').onclick=()=>show(index-1);$('next').onclick=()=>show(index+1);$('full').hidden=!document.fullscreenEnabled;$('full').onclick=()=>document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen();document.addEventListener('fullscreenchange',()=>{$('full').textContent=document.fullscreenElement?'Exit full screen':'Full screen'});document.addEventListener('keydown',e=>{if(e.ctrlKey||e.altKey||e.metaKey||$('source-dialog').open)return;if(e.key==='ArrowRight'){e.preventDefault();show(index+1)}if(e.key==='ArrowLeft'){e.preventDefault();show(index-1)}if(e.key.toLowerCase()==='n')notes();if(e.key.toLowerCase()==='t')toggleTimer()});setInterval(tick,250);$('close-source').onclick=()=>$('source-dialog').close();
function openSource(file){$('source-title').textContent=file;$('full-source').textContent=sourceFiles[file];$('source-dialog').showModal()}
const sourceFiles=%%SOURCES%%;
show(0);
'''

if __name__ == '__main__':
    sources={name:(ROOT/name).read_text(encoding='utf-8') for name in ['analysis.py','portfolio.py','app.py']}
    JS=JS.replace('%%SOURCES%%',json.dumps(sources,ensure_ascii=False).replace('</','<\\/'))
    build()
