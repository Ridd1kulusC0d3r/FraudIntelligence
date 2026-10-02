#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, pathlib, xml.etree.ElementTree as ET
import yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
def load(p): return yaml.safe_load(p.read_text(encoding='utf-8')) or {}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--json-out',default='dist/graph/fraudintelligence.json'); ap.add_argument('--graphml-out',default='dist/graph/fraudintelligence.graphml'); a=ap.parse_args(); nodes=[]; edges=[]
    for f in (ROOT/'knowledge/actors').glob('*.yml'):
        for x in load(f).get('actors',[]): nodes.append({'id':x['id'],'type':'actor','label':x['name']})
    for x in load(ROOT/'knowledge/intelligence-requirements.yml').get('requirements',[]): nodes.append({'id':x['id'],'type':'requirement','label':x['title']})
    for f in (ROOT/'knowledge/campaigns').glob('*.yml'):
        for x in load(f).get('campaigns',[]):
            nodes.append({'id':x['id'],'type':'campaign','label':x['name'],'first_seen':x['first_seen'],'last_seen':x.get('last_seen')})
            for ref in x.get('actor_refs',[]): edges.append({'source':ref,'target':x['id'],'type':'associated-with'})
    for f in (ROOT/'knowledge/hypotheses').glob('*.yml'):
        for x in load(f).get('hypotheses',[]): nodes.append({'id':x['id'],'type':'hypothesis','label':x['statement']}); edges.append({'source':x['pir_id'],'target':x['id'],'type':'frames'})
    for x in load(ROOT/'knowledge/watch-warning.yml').get('watch_items',[]):
        nodes.append({'id':x['id'],'type':'watch','label':x['title']}); edges.append({'source':x['pir_id'],'target':x['id'],'type':'monitors'})
        for ref in x.get('hypothesis_refs',[]): edges.append({'source':ref,'target':x['id'],'type':'tested-by-signposts'})
    payload={'version':'0.1','nodes':nodes,'edges':edges}; jout=pathlib.Path(a.json_out); jout=jout if jout.is_absolute() else ROOT/jout; jout.parent.mkdir(parents=True,exist_ok=True); jout.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    ns='http://graphml.graphdrawing.org/xmlns'; ET.register_namespace('',ns); root=ET.Element('{%s}graphml'%ns); graph=ET.SubElement(root,'{%s}graph'%ns,edgedefault='directed')
    for n in nodes: ET.SubElement(graph,'{%s}node'%ns,id=n['id'])
    for i,e in enumerate(edges): ET.SubElement(graph,'{%s}edge'%ns,id='e'+str(i),source=e['source'],target=e['target'])
    gout=pathlib.Path(a.graphml_out); gout=gout if gout.is_absolute() else ROOT/gout; gout.parent.mkdir(parents=True,exist_ok=True); ET.ElementTree(root).write(gout,encoding='utf-8',xml_declaration=True); print(f'wrote graph with {len(nodes)} nodes and {len(edges)} edges')
if __name__=='__main__': main()