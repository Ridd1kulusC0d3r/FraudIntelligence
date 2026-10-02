#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib
import yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser(); p.add_argument('--out',default='docs/data/coverage.json'); args=p.parse_args()
    data=yaml.safe_load((ROOT/'knowledge/detection-coverage.yml').read_text(encoding='utf-8')) or {}; rows=data.get('coverage_records',[])
    summary={'version':'0.1','records':len(rows),'coverage':{'covered':0,'partial':0,'gap':0},'maturity':{'concept':0,'draft':0,'tested':0,'operational':0},'items':rows}
    for r in rows: summary['coverage'][r['coverage']]+=1; summary['maturity'][r['maturity']]+=1
    out=pathlib.Path(args.out); out=out if out.is_absolute() else ROOT/out; out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); print(f'wrote {out} ({len(rows)} coverage records)')
if __name__=='__main__': main()