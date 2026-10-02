#!/usr/bin/env python3
from __future__ import annotations
import json, pathlib, sys
import yaml
from jsonschema import Draft202012Validator

ROOT=pathlib.Path(__file__).resolve().parents[1]

def load_yaml(path):
    with path.open('r',encoding='utf-8') as fh: return yaml.safe_load(fh) or {}

def schema(name):
    return json.loads((ROOT/'schemas'/name).read_text(encoding='utf-8'))

def validate_yaml_files():
    errors=[]
    for path in ROOT.rglob('*.yml'):
        if '.cache' in path.parts: continue
        try: load_yaml(path)
        except Exception as exc: errors.append(f'{path}: YAML parse failed: {exc}')
    return errors

def validate_json_schemas():
    errors=[]
    for path in (ROOT/'schemas').glob('*.schema.json'):
        try: Draft202012Validator.check_schema(json.loads(path.read_text(encoding='utf-8')))
        except Exception as exc: errors.append(f'{path}: invalid schema: {exc}')
    return errors

def validate_items(paths,key,schema_name):
    errors=[]; validator=Draft202012Validator(schema(schema_name)); seen={}
    for path in paths:
        for idx,item in enumerate(load_yaml(path).get(key,[])):
            for err in validator.iter_errors(item): errors.append(f'{path}:{idx}: {err.message}')
            item_id=item.get('id') or item.get('source_id')
            if item_id in seen: errors.append(f'{path}:{idx}: duplicate id {item_id}; first in {seen[item_id]}')
            elif item_id: seen[item_id]=path
    return errors

def validate_registry(paths,key,required):
    errors=[]; seen={}
    for path in paths:
        for idx,item in enumerate(load_yaml(path).get(key,[])):
            missing=sorted(required-set(item))
            if missing: errors.append(f'{path}:{idx}: missing {missing}')
            item_id=item.get('id')
            if item_id in seen: errors.append(f'{path}:{idx}: duplicate id {item_id}; first in {seen[item_id]}')
            elif item_id: seen[item_id]=path
            source=item.get('source')
            if source and not source.startswith('https://'): errors.append(f'{path}:{idx}: source must use https')
    return errors

def integrity():
    errors=[]
    actors={x['id'] for p in (ROOT/'knowledge/actors').glob('*.yml') for x in load_yaml(p).get('actors',[])}
    threats={x['id'] for p in (ROOT/'knowledge/threats').glob('*.yml') for x in load_yaml(p).get('threats',[])}
    campaigns={x['id'] for p in (ROOT/'knowledge/campaigns').glob('*.yml') for x in load_yaml(p).get('campaigns',[])}
    pirs={x['id'] for x in load_yaml(ROOT/'knowledge/intelligence-requirements.yml').get('requirements',[])}
    hypotheses={x['id'] for p in (ROOT/'knowledge/hypotheses').glob('*.yml') for x in load_yaml(p).get('hypotheses',[])}
    for p in (ROOT/'knowledge/campaigns').glob('*.yml'):
        for x in load_yaml(p).get('campaigns',[]):
            for ref in x.get('actor_refs',[]):
                if ref not in actors: errors.append(f'{p}: unknown actor_ref {ref}')
    for p in (ROOT/'knowledge/hypotheses').glob('*.yml'):
        for x in load_yaml(p).get('hypotheses',[]):
            if x.get('pir_id') not in pirs: errors.append(f"{p}: unknown pir_id {x.get('pir_id')}")
    for x in load_yaml(ROOT/'knowledge/watch-warning.yml').get('watch_items',[]):
        if x.get('pir_id') not in pirs: errors.append(f"watch-warning: unknown pir_id {x.get('pir_id')}")
        for ref in x.get('hypothesis_refs',[]):
            if ref not in hypotheses: errors.append(f'watch-warning: unknown hypothesis_ref {ref}')
    for x in load_yaml(ROOT/'knowledge/collection-plans.yml').get('collection_plans',[]):
        if x.get('pir_id') not in pirs: errors.append(f"collection-plan: unknown pir_id {x.get('pir_id')}")
    known=actors|threats|campaigns
    for x in load_yaml(ROOT/'knowledge/detection-coverage.yml').get('coverage_records',[]):
        if x.get('subject_ref') not in known: errors.append(f"detection-coverage: unknown subject_ref {x.get('subject_ref')}")
    return errors

def main():
    errors=validate_yaml_files()+validate_json_schemas()
    errors+=validate_registry([ROOT/'knowledge/frameworks.yml'],'frameworks',{'id','name','kind','scope','status','source','source_class','confidence'})
    errors+=validate_registry(sorted((ROOT/'knowledge/actors').glob('*.yml')),'actors',{'id','name','type','region','status','confidence','source'})
    errors+=validate_registry(sorted((ROOT/'knowledge/threats').glob('*.yml')),'threats',{'id','name','class','status','confidence','source'})
    errors+=validate_items(sorted((ROOT/'knowledge/campaigns').glob('*.yml')),'campaigns','campaign.schema.json')
    errors+=validate_items(sorted((ROOT/'knowledge/hypotheses').glob('*.yml')),'hypotheses','hypothesis.schema.json')
    errors+=validate_items([ROOT/'knowledge/watch-warning.yml'],'watch_items','watch-warning.schema.json')
    errors+=validate_items([ROOT/'knowledge/collection-plans.yml'],'collection_plans','collection-plan.schema.json')
    errors+=validate_items([ROOT/'knowledge/source-assessments.yml'],'source_assessments','source-assessment.schema.json')
    errors+=validate_items([ROOT/'knowledge/detection-coverage.yml'],'coverage_records','coverage-record.schema.json')
    errors+=integrity()
    if errors:
        for e in errors: print('ERROR:',e)
        return 1
    print('FraudIntelligence v0.4 knowledge validation passed.')
    return 0

if __name__=='__main__': sys.exit(main())