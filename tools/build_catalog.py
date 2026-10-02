#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib, sys
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs' / 'data' / 'catalog.json'

def read_yaml(path):
    with path.open('r', encoding='utf-8') as fh:
        return yaml.safe_load(fh) or {}

def collect(directory, key):
    rows = []
    for path in sorted(directory.glob('*.yml')):
        rows.extend(read_yaml(path).get(key, []))
    return rows

def build_payload():
    frameworks = read_yaml(ROOT/'knowledge/frameworks.yml').get('frameworks', [])
    actors = collect(ROOT/'knowledge/actors', 'actors')
    threats = collect(ROOT/'knowledge/threats', 'threats')
    campaigns = collect(ROOT/'knowledge/campaigns', 'campaigns')
    requirements = read_yaml(ROOT/'knowledge/intelligence-requirements.yml').get('requirements', [])
    watches = read_yaml(ROOT/'knowledge/watch-warning.yml').get('watch_items', [])
    items = []
    for x in frameworks:
        items.append({'id':x['id'],'name':x['name'],'type':'reference','category':x['kind'],'scope':x['scope'],'status':x['status'],'source':x['source']})
    for x in actors:
        items.append({'id':x['id'],'name':x['name'],'type':'actor','category':x['type'],'scope':', '.join(x.get('focus',[])),'status':x['status'],'source':x['source'],'region':x.get('region'),'confidence':x.get('confidence'),'featured':bool(x.get('featured',False)),'aliases':x.get('aliases',[])})
    for x in threats:
        items.append({'id':x['id'],'name':x['name'],'type':'threat','category':x['class'],'scope':', '.join(x.get('defensive_relevance',[])),'status':x['status'],'source':x['source']})
    for x in campaigns:
        items.append({'id':x['id'],'name':x['name'],'type':'campaign','category':'campaign','scope':x['objective'],'status':x['status'],'source':x['source_refs'][0],'region':' / '.join(x.get('regions',[])),'confidence':x.get('confidence')})
    for x in requirements:
        items.append({'id':x['id'],'name':x['title'],'type':'requirement','category':'priority-intelligence-requirement','scope':x['decision_supported'],'status':x['status'],'source':'../knowledge/intelligence-requirements.yml'})
    for x in watches:
        items.append({'id':x['id'],'name':x['title'],'type':'watch','category':'watch-and-warning','scope':x['threshold'],'status':x['status'],'source':'../knowledge/watch-warning.yml'})
    return {'version':'0.4','count':len(items),'items':sorted(items,key=lambda x:(x['type'],x['name'].lower()))}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--check',action='store_true'); args=p.parse_args()
    payload=build_payload()
    if args.check:
        if not OUT.exists():
            print(f'ERROR: missing {OUT}'); return 1
        committed=json.loads(OUT.read_text(encoding='utf-8'))
        keyed=lambda d:{(i['type'],i['id']):i for i in d.get('items',[])}
        if committed.get('version')!=payload['version'] or committed.get('count')!=payload['count'] or keyed(committed)!=keyed(payload):
            print('ERROR: docs/data/catalog.json is stale.'); return 1
        print(f"catalog is current ({payload['count']} items)"); return 0
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(f"wrote {OUT} ({payload['count']} items)"); return 0

if __name__=='__main__': sys.exit(main())