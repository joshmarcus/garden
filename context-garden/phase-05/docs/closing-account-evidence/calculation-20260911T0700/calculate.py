"""Read-only closing calculation using the accepted product implementation."""
import hashlib,json,sys,subprocess
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path

directory=Path(__file__).resolve().parent
source=directory/'source'
source_head=subprocess.check_output(['git','-C',str(source),'rev-parse','HEAD'],text=True).strip()
assert source_head=='5d88157d1fd5d9a15fcd746a888d05e179c75543'
assert not subprocess.check_output(['git','-C',str(source),'status','--porcelain'],text=True).strip()
sys.path.insert(0,str(source/'src'))
from garden.store import Store
from garden.events import EventLog,metrics
from garden.outcomes import acceptance_cohort,canonical_phase_key
from garden.operator_spend import read_records,to_cost_events,attributed_summary

root=Path('/home/joshua/garden'); output=directory/'calculation.json';assert not output.exists()
cutoff=datetime.now(timezone.utc).isoformat()
store=Store(root);tasks=store.tasks()
event_path=root/'.garden/events.jsonl';ledger_path=root/'context-garden/docs/operator-spend.jsonl'
event_bytes=event_path.read_bytes();ledger_bytes=ledger_path.read_bytes()
# Keep exact private input bytes so later ordinary work cannot move this cutoff.
(directory/'events.snapshot.jsonl').write_bytes(event_bytes)
(directory/'operator-spend.snapshot.jsonl').write_bytes(ledger_bytes)
events=EventLog(directory/'events.snapshot.jsonl').read()
ledger=read_records(directory/'operator-spend.snapshot.jsonl')
operator_events=to_cost_events(ledger)
event_kinds={'dispatch','transition','review','run_finished','automerged','tick','ci_status'}
relevant=[e for e in events if e.get('kind') in event_kinds and str(e.get('at') or '')<cutoff]
combined=relevant+operator_events
sections={}
for label,phase,since in [('phase04_lifetime','phase-04',''),('phase05_lifetime','phase-05',''),('phase05_since_reopening','phase-05','2026-09-10T13:16:29+00:00')]:
    selected={tid:t for tid,t in tasks.items() if t.product=='context-garden' and t.phase==phase}
    data=metrics(combined,selected,since=since,until=cutoff)
    cohort=acceptance_cohort(combined,selected,since=since,until=cutoff)
    data['accepted_cohort']=cohort
    data['current_task_statuses']=dict(Counter(t.status.value for t in selected.values()))
    data['window']={'since':since or None,'until_exclusive':cutoff,'membership':'current product/phase assignment; acceptance completion in window; all task runs through acceptance'}
    phase_key='context-garden/'+phase
    data['operator_ledger']=attributed_summary(ledger,since=since,include=lambda r: str(r.get('at') or '')<cutoff and r.get('product')=='context-garden' and canonical_phase_key(str(r.get('product') or ''),str(r.get('phase') or ''))==phase_key)
    members=cohort['tasks'];reviewed=[m for m in members if m['first_review']]
    data['accepted_first_pass']={'approved':sum(m['first_review']=='approve' for m in reviewed),'reviewed':len(reviewed),'unreviewed':len(members)-len(reviewed),'rate':sum(m['first_review']=='approve' for m in reviewed)/len(reviewed) if reviewed else None}
    data['agent_rebases_per_counted_merge']=data['rebase']['agent']/data['merges'] if data['merges'] else None
    data['tick_scope']='shared controller tick observations in the selected time window; not uniquely phase-attributed'
    sections[label]=data
selected_ids={tid for tid,t in tasks.items() if t.product=='context-garden' and t.phase in ('phase-04','phase-05')}
allowed={'at','kind','task','run','mode','model','harness','pool_member','cost_usd','from','to','base_merged','verdict','criteria_met','criteria_total','how','duration_s','actor','by','product','phase','activity','state','stale','exists_for_sha'}
projection=[]
for e in relevant:
    if e.get('task') not in selected_ids and e.get('kind')!='tick':continue
    row={k:v for k,v in e.items() if k in allowed}
    # Preserve the native acceptance predicate without publishing arbitrary free text.
    note=str(e.get('note') or '')
    if note.startswith('PR merged'):row['note']='PR merged [remaining note omitted]'
    elif note.startswith('parent ') and "this task's commits are now on " in note:row['note']="parent [omitted]; this task's commits are now on [omitted]"
    elif note:row['note']='[non-acceptance note omitted]'
    projection.append(row)
sessions={};sanitized_ledger=[]
for r in ledger:
    sid=str(r.get('session') or '');sessions.setdefault(sid,'operator-session-'+str(len(sessions)+1))
    row={k:r[k] for k in ('at','kind','list_price_usd','turns','product','phase') if k in r}
    row['session']=sessions[sid]
    if row.get('product') not in ('context-garden','',None):row['product']='other-product'
    sanitized_ledger.append(row)
task_projection={tid:{'id':tid,'difficulty':tasks[tid].difficulty,'status':tasks[tid].status.value,'product':tasks[tid].product,'phase':tasks[tid].phase,'key':tasks[tid].key} for tid in sorted(selected_ids)}
inputs={'cutoff':cutoff,'events':projection,'operator_ledger':sanitized_ledger,'tasks':task_projection}
input_path=directory/'calculation-input.json';input_path.write_text(json.dumps(inputs,indent=2)+'\n')
result={'cutoff':cutoff,'source_head':source_head,'source_files':{name:hashlib.sha256((source/'src/garden'/name).read_bytes()).hexdigest() for name in ('events.py','outcomes.py','operator_spend.py')},'input_hashes':{'private_event_snapshot':hashlib.sha256(event_bytes).hexdigest(),'private_operator_snapshot':hashlib.sha256(ledger_bytes).hexdigest(),'public_projection':hashlib.sha256(input_path.read_bytes()).hexdigest()},'event_rows':len(events),'sections':sections,'native_state_mutations':False}
output.write_text(json.dumps(result,indent=2,default=str)+'\n')
print(json.dumps({'path':str(output),'cutoff':cutoff,'event_rows':len(events),'summary':{label:{'cohort':{k:v for k,v in data['accepted_cohort'].items() if k!='tasks'},'first_pass':data['accepted_first_pass'],'merges':data['merges'],'queue_merges':data['queue_merges'],'hand_merges':data['hand_merges'],'rebase':data['rebase'],'agent_rebases_per_merge':data['agent_rebases_per_counted_merge'],'operator':data['operator'],'operator_ledger':data['operator_ledger'],'statuses':data['current_task_statuses'],'tiers':data['by_difficulty']} for label,data in sections.items()}},default=str))
