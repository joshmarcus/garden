"""Replay the public sanitized calculation inputs against the exact accepted implementation."""
import json,sys,hashlib
from types import SimpleNamespace
from pathlib import Path
from datetime import datetime,timezone
d=Path(__file__).resolve().parent
sys.path.insert(0,str(d/'source/src'))
from garden.events import metrics
from garden.outcomes import acceptance_cohort,canonical_phase_key
from garden.operator_spend import to_cost_events,attributed_summary
original=json.loads((d/'calculation.json').read_text())
data=json.loads((d/'calculation-input.json').read_text())
for file,digest in original['source_files'].items():assert hashlib.sha256((d/'source/src/garden'/file).read_bytes()).hexdigest()==digest
tasks={tid:SimpleNamespace(**{**row,'status':row['status']}) for tid,row in data['tasks'].items()}
events=data['events']+to_cost_events(data['operator_ledger']);out=[]
for label,phase,since in [('phase04_lifetime','phase-04',''),('phase05_lifetime','phase-05',''),('phase05_since_reopening','phase-05','2026-09-10T13:16:29+00:00')]:
 selected={tid:t for tid,t in tasks.items() if t.phase==phase and t.product=='context-garden'}
 expected=dict(original['sections'][label])
 cohort=acceptance_cohort(events,selected,since=since,until=data['cutoff'])
 calculated=metrics(events,selected,since=since,until=data['cutoff'])
 for key in ('accepted_cohort','accepted_first_pass','agent_rebases_per_counted_merge','current_task_statuses','window','operator_ledger','tick_scope'):expected.pop(key,None)
 difference=[k for k,v in expected.items() if calculated.get(k)!=v]
 if difference:
  for k in difference:
   if k=='tasks':
    aa={r['id']:r for r in expected[k]};bb={r['id']:r for r in calculated[k]}
    for tid in aa:
     if aa[tid]!=bb.get(tid):print('FIRST_DIFFERENCE',label,tid,{f:(aa[tid][f],bb.get(tid,{}).get(f)) for f in aa[tid] if aa[tid][f]!=bb.get(tid,{}).get(f)});break
 assert not difference,(label,difference[:10])
 assert cohort==original['sections'][label]['accepted_cohort']
 out.append({'section':label,'metrics_exact':True,'accepted':cohort['accepted'],'known_cost_usd':cohort['known_cost_usd'],'complete':cohort['cost_complete'],'average':cohort['cost_per_accepted_task']})
receipt={'at':datetime.now(timezone.utc).isoformat(),'status':'passed','source_head':original['source_head'],'public_projection_sha256':hashlib.sha256((d/'calculation-input.json').read_bytes()).hexdigest(),'sections':out,'native_state_mutations':False}
p=d/'replay-verification.json';assert not p.exists();p.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
