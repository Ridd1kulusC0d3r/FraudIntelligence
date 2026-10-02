#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib
import yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]; STAMP='2026-10-01T00:00:00.000Z'; BUNDLE_ID='bundle--0f9af5fe-63b7-4a7a-a492-510fa44a16aa'
def load(path): return yaml.safe_load(path.read_text(encoding='utf-8')) or {}
def all_rows(directory,key):
    rows=[]
    for p in sorted(directory.glob('*.yml')): rows.extend(load(p).get(key,[]))
    return rows
def stix_time(v):
    if len(v)==4: v+='-01-01'
    elif len(v)==7: v+='-01'
    return v+'T00:00:00.000Z'
def build_bundle():
    ids=load(ROOT/'interoperability/stix/id-map.yml').get('ids',{}); objects=[]
    for x in all_rows(ROOT/'knowledge/actors','actors'):
        if x['id'] not in ids: continue
        objects.append({'type':'intrusion-set','spec_version':'2.1','id':'intrusion-set--'+ids[x['id']],'created':STAMP,'modified':STAMP,'name':x['name'],'aliases':x.get('aliases',[]),'external_references':[{'source_name':'FraudIntelligence source','url':x['source']}],'x_fraudintelligence_id':x['id'],'x_fraudintelligence_region':x.get('region'),'x_fraudintelligence_confidence':x.get('confidence'),'x_fraudintelligence_focus':x.get('focus',[])})
    for x in all_rows(ROOT/'knowledge/campaigns','campaigns'):
        if x['id'] not in ids or x.get('tlp')!='TLP:CLEAR': continue
        obj={'type':'campaign','spec_version':'2.1','id':'campaign--'+ids[x['id']],'created':STAMP,'modified':STAMP,'name':x['name'],'description':x['objective'],'first_seen':stix_time(x['first_seen']),'external_references':[{'source_name':'FraudIntelligence source','url':u} for u in x.get('source_refs',[])],'x_fraudintelligence_id':x['id'],'x_fraudintelligence_actor_refs':x.get('actor_refs',[]),'x_fraudintelligence_tlp':x.get('tlp')}
        if x.get('last_seen'): obj['last_seen']=stix_time(x['last_seen'])
        objects.append(obj)
    return {'type':'bundle','id':BUNDLE_ID,'objects':objects}
def main():
    p=argparse.ArgumentParser(); p.add_argument('--out',default='dist/stix/fraudintelligence-bundle.json'); a=p.parse_args(); out=pathlib.Path(a.out); out=out if out.is_absolute() else ROOT/out; out.parent.mkdir(parents=True,exist_ok=True)
    bundle=build_bundle(); out.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8'); print(f"wrote {out} ({len(bundle['objects'])} STIX objects)")
if __name__=='__main__': main()