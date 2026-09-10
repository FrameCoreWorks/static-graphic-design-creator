#!/usr/bin/env python3
"""Offline validation of this repository's JSON Schema vocabulary and handoffs.

This intentionally supports only the schema keywords used here and rejects new
unsupported keywords. It is not a general JSON Schema implementation or an LLM
routing evaluator. Full host behavior and visual/copy quality need forward tests.
"""
import copy
import json
import re
from pathlib import Path
from test_skill import ROOT, SKILL, UniqueLoader, read_json, require
import yaml

SCHEMA = read_json(SKILL / 'references/design-contract.schema.json')
KEYWORDS = {'$schema', '$defs', '$ref', 'title', 'description', 'type', 'enum', 'const',
            'properties', 'required', 'additionalProperties', 'items', 'minItems',
            'minLength', 'allOf', 'anyOf', 'not', 'if', 'then'}

class Invalid(ValueError):
    pass

def check_vocabulary(s):
    if isinstance(s, bool):
        return
    unknown = set(s) - KEYWORDS
    if unknown:
        raise RuntimeError(f'Unsupported schema keywords: {unknown}')
    for k in ('$defs', 'properties'):
        for child in s.get(k, {}).values():
            check_vocabulary(child)
    for k in ('items', 'additionalProperties', 'not', 'if', 'then'):
        if k in s:
            check_vocabulary(s[k])
    for k in ('allOf', 'anyOf'):
        for child in s.get(k, []):
            check_vocabulary(child)

def valid_type(value, kind):
    return {'object':lambda:isinstance(value,dict), 'array':lambda:isinstance(value,list),
            'string':lambda:isinstance(value,str), 'boolean':lambda:type(value) is bool,
            'integer':lambda:type(value) is int, 'null':lambda:value is None}[kind]()

def equal(a, b):
    return type(a) is type(b) and a == b

def validate(value, s=SCHEMA, path='$'):
    if isinstance(s, bool):
        if not s:
            raise Invalid(path + ': disallowed')
        return
    if '$ref' in s:
        require(s['$ref'].startswith('#/$defs/'), 'Only local schema references supported')
        validate(value, SCHEMA['$defs'][s['$ref'].split('/')[-1]], path)
    if 'type' in s:
        types=s['type'] if isinstance(s['type'],list) else [s['type']]
        if not any(valid_type(value,t) for t in types):
            raise Invalid(path + ': wrong type')
    if 'const' in s and not equal(value,s['const']):
        raise Invalid(path + ': const mismatch')
    if 'enum' in s and not any(equal(value,x) for x in s['enum']):
        raise Invalid(path + ': enum mismatch')
    if isinstance(value,str) and len(value)<s.get('minLength',0):
        raise Invalid(path + ': empty string')
    if isinstance(value,dict):
        if not set(s.get('required',[])) <= set(value):
            raise Invalid(path + ': missing required field')
        props=s.get('properties',{})
        for k,v in value.items():
            if k in props:
                validate(v,props[k],path+'.'+k)
            elif 'additionalProperties' in s:
                validate(v,s['additionalProperties'],path+'.'+k)
    if isinstance(value,list):
        if len(value)<s.get('minItems',0):
            raise Invalid(path + ': insufficient items')
        for i,v in enumerate(value):
            if 'items' in s:
                validate(v,s['items'],f'{path}[{i}]')
    for child in s.get('allOf',[]):
        validate(value,child,path)
    if 'anyOf' in s:
        errors=[]
        for child in s['anyOf']:
            try:
                validate(value,child,path)
                break
            except Invalid as error:
                errors.append(error)
        else:
            raise Invalid(path + ': no anyOf alternative matched')
    if 'not' in s:
        try:
            validate(value,s['not'],path)
        except Invalid:
            pass
        else:
            raise Invalid(path + ': prohibited state')
    if 'if' in s:
        try:
            validate(value,s['if'],path)
        except Invalid:
            pass
        else:
            validate(value,s.get('then',True),path)

FINAL_ACTIONS={'return_prompt','native_render','report_unavailable','report_generation_failed','review'}

def validate_state(state):
    validate(state)
    for key,items in [('copy.items',state['copy']['items']),('copy.options',state['copy']['options']),
                      ('copy.claims',state['copy']['claims']),('references',state['references']),('qa.checks',state['qa']['checks'])]:
        ids=[x['id'] for x in items]
        if len(ids)!=len(set(ids)):
            raise Invalid('Duplicate ID in '+key)
    item_ids={x['id'] for x in state['copy']['items']}
    for claim in state['copy']['claims']:
        if not set(claim['item_ids']) <= item_ids:
            raise Invalid('Claim points to missing copy item')
    if state['reference_status']=='ready' and not state['references']:
        raise Invalid('Ready reference list is empty; use none')
    prompt_copy_ids = item_ids
    if 'edit_scope' in state:
        if state['task_mode'] != 'edit':
            raise Invalid('Edit scope on a non-edit task')
        edit=state['edit_scope']
        changed,protected=edit['changed_copy_ids'],edit['protected_copy_ids']
        if len(set(changed))!=len(changed) or len(set(protected))!=len(protected) or set(changed)&set(protected):
            raise Invalid('Ambiguous or duplicate edit copy scope')
        if set(changed)|set(protected) != item_ids:
            raise Invalid('Edit scope does not account for every copy item')
        refs={ref['id']:ref for ref in state['references']}
        source=refs.get(edit['source_reference_id'])
        if state['action'] in FINAL_ACTIONS and (not source or not source['available'] or source['conflict'] or 'edit_source' not in source['roles']):
            raise Invalid('Scoped edit lacks its available image source')
        prompt_copy_ids=set(changed)
    if state['action'] in FINAL_ACTIONS:
        for item in state['copy']['items']:
            if item['id'] in prompt_copy_ids and item['text'] not in state['prompt']:
                raise Invalid('Final prompt lost exact copy: '+item['id'])
        for key in ('objective','visual_thesis','output_format'):
            if not state['strategy'][key].strip():
                raise Invalid('Final strategy unresolved: '+key)
        if not state['strategy']['attention_order']:
            raise Invalid('Final attention order unresolved')
    if state['qa']['status']=='pass':
        checks={c['id']:c for c in state['qa']['checks']}
        required={'concept','hierarchy','copy','legibility','references','additions','delivery'}
        if not required <= checks.keys():
            raise Invalid('QA pass lacks a required check')
        must_pass={'concept','hierarchy','additions','delivery'}
        if state['copy']['items']:
            must_pass |= {'copy','legibility'}
        if state['references']:
            must_pass.add('references')
        if any(checks[k]['status']!='pass' for k in must_pass):
            raise Invalid('Applicable required check did not pass')
        if any(not c['evidence'].strip() or c['evidence'].strip().lower() in {'unknown','pending'} for c in checks.values()):
            raise Invalid('QA evidence is unresolved')
    if state['qa']['critical_failures'] and state['qa']['status']!='fail':
        raise Invalid('Critical failure without failed QA')

def validate_transition(before,after,approved_copy_changes=(),concept_change_approved=False,approved_reference_changes=()):
    """Compare actual before/after records. Approvals are supplied by test/task evidence."""
    validate_state(after)
    final_items={i['id']:i for i in after['copy']['items']}
    if after['task_mode']=='edit' and 'edit_scope' in after:
        declared=set(after['edit_scope']['changed_copy_ids'])
        old_items={i['id']:i for i in before['copy']['items']}
        actual={k for k in old_items.keys() | final_items.keys() if old_items.get(k,{}).get('text')!=final_items.get(k,{}).get('text')}
        if not actual <= declared:
            raise Invalid('Copy change is outside declared edit scope')
    for item in before['copy']['items']:
        if item['authority'] in {'user_locked','source_locked','user_selected'} and item['id'] not in approved_copy_changes:
            if item['id'] not in final_items or any(final_items[item['id']][key]!=item[key] for key in ('text','authority','source','required','allowed_changes')):
                raise Invalid('Protected text changed or removed: '+item['id'])
    if before['concept']['status'] in {'selected','locked'} and not concept_change_approved:
        if before['concept']['lock']!=after['concept']['lock']:
            raise Invalid('Concept lock changed without approval')
    previous_refs={ref['id']:ref for ref in before['references']}
    next_refs={ref['id']:ref for ref in after['references']}
    for ref_id in previous_refs.keys() | next_refs.keys():
        if ref_id in approved_reference_changes:
            continue
        old,new=previous_refs.get(ref_id),next_refs.get(ref_id)
        if old is None or new is None or any(old[k]!=new[k] for k in ('source','roles','properties')):
            raise Invalid('Reference authority changed without approval: '+ref_id)

def main():
    check_vocabulary(SCHEMA)
    fixtures=read_json(ROOT/'tests/fixtures/design-contract-cases.json')
    for case in fixtures['cases']:
        try:
            if 'before' in case:
                validate_transition(case['before'],case['state'],case.get('approved_copy_changes',()),case.get('concept_change_approved',False),case.get('approved_reference_changes',()))
            else:
                validate_state(case['state'])
        except Invalid:
            actual=False
        else:
            actual=True
        require(actual is case['valid'],f'Contract case failed: {case["id"]}')
    for path in (SKILL/'templates').glob('*.md'):
        for text in re.findall(r'```yaml\n(.*?)```',path.read_text(),re.S):
            state=yaml.load(text,Loader=UniqueLoader)
            validate_state(state)
            round_trip=json.loads(json.dumps(state,ensure_ascii=False))
            require(state==round_trip,'Round-trip lost data')
            validate_state(round_trip)
    # The multi-asset project and a single raster operation remain independent
    # records: a later editable title is not silently dropped or painted on a background.
    from layer_assets import validate_plan
    plan = read_json(SKILL/'templates/layer-plan.json')
    preserved_plan = copy.deepcopy(plan)
    source = (SKILL/'templates/prompt-pack.md').read_text()
    state = yaml.load(re.search(r'```yaml\n(.*?)```', source, re.S).group(1), Loader=UniqueLoader)
    state['strategy'].update(objective='Create the background element', visual_thesis='Cool empty square supports a later warm figure',
                             attention_order=['Open ground plane'], composition='environment', type_image_relationship='Title belongs to a separate editor element')
    state['concept']['lock'].update(premise='Night poster environment', mechanism='Cool space for later warm figure',
                                  distinctive_hook='Human absence in the background asset', forbidden_substitutions=['Text or figures on this asset'])
    state['copy'].update(route='no_copy', selection_status='not_required', items=[], options=[], claims=[])
    state['prompt']='Create only the cool empty night-square background. Keep upper title space calm. No lettering, person or fog.'
    validate_state(state)
    validate_plan(plan)
    require(plan == preserved_plan, 'Asset-level no-copy changed project inventory')
    title_state = yaml.load(re.search(r'```yaml\n(.*?)```', source, re.S).group(1), Loader=UniqueLoader)
    title_state['copy']['items'][0]['text'] = plan['composition']['copy'][0]['text']
    title_state['prompt']='Create one raster artistic title asset reading exactly AFTER HOURS. No other lettering.'
    validate_state(title_state)
    title_state['prompt']='Create a title asset without any lettering.'
    try:
        validate_state(title_state)
    except Invalid:
        pass
    else:
        raise AssertionError('Asset routing bypassed its own exact-copy gate')
    # A new unsupported keyword fails visibly rather than weakening validation.
    try:
        check_vocabulary({'unevaluatedProperties':False})
    except RuntimeError:
        pass
    else:
        raise AssertionError('Unsupported keyword silently ignored')
    print(f'{len(fixtures["cases"])} design-state/transition cases, both actual templates and 3 layered handoff checks passed. No model or image evaluation claimed.')

if __name__=='__main__':
    main()
