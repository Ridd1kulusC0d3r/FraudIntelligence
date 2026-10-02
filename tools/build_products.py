#!/usr/bin/env python3
from __future__ import annotations
import argparse, pathlib
import yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(p): return yaml.safe_load(p.read_text(encoding='utf-8')) or {}
def collect(d,k):
    rows=[]
    for p in d.glob('*.yml'): rows.extend(load(p).get(k,[]))
    return rows
def write(p,text): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text.strip()+'\n',encoding='utf-8')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='products/generated'); a=ap.parse_args(); out=pathlib.Path(a.out); out=out if out.is_absolute() else ROOT/out
    for x in collect(ROOT/'knowledge/campaigns','campaigns'):
        body=['# Campaign Brief — '+x['name'],'',f"**TLP:** {x['tlp']}  ",f"**As of:** {x['last_reviewed']}  ",f"**Confidence:** {x['confidence']}  ",f"**Campaign ID:** {x['id']}",'','## Key judgment','',x['objective'],'','## Actor references','']+['- '+v for v in x.get('actor_refs',[])]+['','## Targeting','']+['- '+v for v in x.get('targeting',[])]+['','## Uncertainty','','Public-source visibility is incomplete; absence of reporting is not evidence of absence.','','## Sources','']+['- '+v for v in x.get('source_refs',[])]
        write(out/'campaign-briefs'/(x['id']+'.md'),'\n'.join(body))
    for x in load(ROOT/'knowledge/watch-warning.yml').get('watch_items',[]):
        body=['# Watch & Warning — '+x['title'],'',f"**TLP:** {x['tlp']}  ",f"**As of:** {x['last_reviewed']}  ",f"**Severity:** {x['severity']}  ",f"**Status:** {x['status']}  ",f"**PIR:** {x['pir_id']}",'','## Signposts','']+['- '+s for s in x.get('signposts',[])]+['','## Trigger threshold','',x['threshold'],'','## Actions on trigger','']+['- '+s for s in x.get('actions',[])]
        write(out/'watch-warning'/(x['id']+'.md'),'\n'.join(body))
    cov=load(ROOT/'knowledge/detection-coverage.yml').get('coverage_records',[]); body=['# Detection Coverage Assessment','','**TLP:** TLP:CLEAR  ','**As of:** 2026-10-01','']
    for x in cov: body += [f"## {x['id']} · {x['coverage']} / {x['maturity']}",f"Subject: {x['subject_ref']}",f"Behavior: {x['behavior']['name']}",'',x.get('notes',''),'']
    write(out/'detection-coverage.md','\n'.join(body))
    for x in load(ROOT/'knowledge/collection-plans.yml').get('collection_plans',[]):
        body=['# Collection Gap Report — '+x['pir_id'],'','**TLP:** TLP:CLEAR  ',f"**As of:** {x['last_reviewed']}  ",f"**Coverage:** {x['coverage']}",'','## Gaps','']+['- '+g for g in x.get('gaps',[])]+['','## Review cadence','',str(x['review_cycle_days'])+' days']
        write(out/'collection-gaps'/(x['id']+'.md'),'\n'.join(body))
    print(f'generated intelligence products in {out}')
if __name__=='__main__': main()