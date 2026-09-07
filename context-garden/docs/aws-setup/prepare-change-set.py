"""Prepare, but never execute, the reviewed infrastructure change set with an explicit admin profile."""
import argparse,json,subprocess,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--profile',required=True);a=p.parse_args()
if a.profile in ('default','garden-provisioner','garden-login'):
 raise SystemExit('Use an explicitly configured non-root infrastructure administrator profile.')
base=['aws','--profile',a.profile,'--region','us-east-1']
def call(*args):
 return subprocess.check_output(base+list(args),text=True)
identity=json.loads(call('sts','get-caller-identity','--output','json'))
if identity['Account']!='350111791226' or identity['Arn'].endswith(':root'):
 raise SystemExit('Wrong account or root identity; no change set created.')
source=Path(__file__).with_name('infrastructure.template.json').resolve()
call('cloudformation','validate-template','--template-body',source.as_uri(),'--output','json')
# CREATE only: refuse automatic updates or replacement of existing named resources.
name='garden-phase05-'+time.strftime('%Y%m%dT%H%M%SZ',time.gmtime())
print(call('cloudformation','create-change-set','--stack-name','context-garden-phase05-infrastructure','--change-set-name',name,'--change-set-type','CREATE','--capabilities','CAPABILITY_NAMED_IAM','--template-body',source.as_uri(),'--tags','Key=ManagedBy,Value=context-garden','Key=Pool,Value=phase05','--output','json'))
print('Created reviewable change set only. Inspect it and existing resource collisions before execution. No instance is defined.')
