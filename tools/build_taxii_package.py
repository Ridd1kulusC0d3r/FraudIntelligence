#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib, sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent)); from export_stix import build_bundle
ROOT=pathlib.Path(__file__).resolve().parents[1]
def main():
    p=argparse.ArgumentParser(); p.add_argument('--out',default='dist/taxii'); a=p.parse_args(); out=pathlib.Path(a.out); out=out if out.is_absolute() else ROOT/out; out.mkdir(parents=True,exist_ok=True)
    bundle=build_bundle(); collection={'id':'fraudintelligence-public-cti','title':'FraudIntelligence Public CTI','description':'Public TLP:CLEAR FraudIntelligence STIX 2.1 collection','can_read':True,'can_write':False,'media_type':'application/taxii+json;version=2.1'}
    envelope={'more':False,'objects':bundle['objects']}; (out/'collection.json').write_text(json.dumps(collection,indent=2)+'\n',encoding='utf-8'); (out/'objects.json').write_text(json.dumps(envelope,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); print(f"wrote TAXII-ready fixture with {len(bundle['objects'])} objects to {out}")
if __name__=='__main__': main()