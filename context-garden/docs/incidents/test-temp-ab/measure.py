import argparse, json, os, pathlib, subprocess, time
P=pathlib.Path
ap=argparse.ArgumentParser();ap.add_argument('variant',choices=['ram','disk']);a=ap.parse_args()
results=P('/home/joshua/work/operator-test-tmp/io-ab-20260906');temp=(P('/tmp') if a.variant=='ram' else results)/('garden-io-ab-'+a.variant+'-'+str(os.getpid()));temp.mkdir()
cgroup=P('/sys/fs/cgroup')/P('/proc/self/cgroup').read_text().split('::',1)[1].strip().lstrip('/')
def read(p):
 try:return p.read_text()
 except OSError:return ''
def kv(p):
 out={}
 for l in read(p).splitlines():
  f=l.split()
  if len(f)==2:
   try:out[f[0]]=int(f[1])
   except ValueError:pass
 return out
def pressure(p):
 return {l.split()[0]:{k:float(v) for k,v in (x.split('=') for x in l.split()[1:])} for l in read(p).splitlines()}
def snap():
 mem=kv(cgroup/'memory.stat');disks={}
 for l in read(P('/proc/diskstats')).splitlines():
  f=l.split()
  if f[2].startswith(('sd','nvme','vd')):disks[f[2]]=[int(x) for x in f[3:]]
 return {'at':time.monotonic(),'cpu':kv(cgroup/'cpu.stat'),'memory':int(read(cgroup/'memory.current') or 0),'swap':int(read(cgroup/'memory.swap.current') or 0),'memstat':{k:mem.get(k,0) for k in ['anon','file','shmem','kernel']},'events':kv(cgroup/'memory.events'),'pressure':{k:pressure(cgroup/(k+'.pressure')) for k in ['cpu','memory','io']},'host_io':pressure(P('/proc/pressure/io')),'vm':{k:v for k,v in kv(P('/proc/vmstat')).items() if k in ['pswpin','pswpout','pgmajfault']},'disks':disks,'io_stat':read(cgroup/'io.stat')}
env=os.environ.copy();env['TMPDIR']=str(temp);env['PYTEST_DEBUG_TEMPROOT']=str(temp);env['PYTHONPATH']='src';env.pop('GARDEN_ROOT',None)
cmd=['/home/joshua/work/worktrees/CG-322/.venv/bin/python','-m','pytest','-q','--tb=short','--basetemp',str(temp/'pytest')]
log=(results/(a.variant+'-pytest.log')).open('w');samples=(results/(a.variant+'-samples.jsonl')).open('w')
start=snap();peakmem=peakswap=0;peakparts={};last=start
print(json.dumps({'variant':a.variant,'temp':str(temp),'cgroup':str(cgroup),'command':cmd}),flush=True)
p=subprocess.Popen(cmd,env=env,stdout=log,stderr=subprocess.STDOUT)
while True:
 s=snap();samples.write(json.dumps(s)+'\n');samples.flush();peakmem=max(peakmem,s['memory']);peakswap=max(peakswap,s['swap'])
 for k,v in s['memstat'].items():peakparts[k]=max(peakparts.get(k,0),v)
 last=s
 if p.poll() is not None:break
 time.sleep(1)
log.close();samples.close();elapsed=last['at']-start['at']
result={'variant':a.variant,'exit_code':p.returncode,'seconds':elapsed,'peak_memory_bytes':peakmem,'kernel_peak_bytes':int(read(cgroup/'memory.peak') or 0),'peak_swap_bytes':peakswap,'peak_parts_bytes':peakparts,'cpu_delta':{k:last['cpu'].get(k,0)-v for k,v in start['cpu'].items()},'memory_events_delta':{k:last['events'].get(k,0)-v for k,v in start['events'].items()},'stall_percent':{k:{mode:(v['total']-start['pressure'][k][mode]['total'])/(elapsed*1e6)*100 for mode,v in modes.items()} for k,modes in last['pressure'].items()},'vm_delta':{k:last['vm'].get(k,0)-v for k,v in start['vm'].items()},'temp':str(temp),'disk_delta':{k:{'read_MiB':(v[2]-start['disks'][k][2])*512/1048576,'write_MiB':(v[6]-start['disks'][k][6])*512/1048576,'busy_percent':(v[9]-start['disks'][k][9])/(elapsed*10)} for k,v in last['disks'].items()}}
result['temp_bytes']=int(subprocess.check_output(['du','-sb',str(temp)],text=True).split()[0]);result['test_tail']=(results/(a.variant+'-pytest.log')).read_text()[-2500:]
(results/(a.variant+'-result.json')).write_text(json.dumps(result,indent=2));print(json.dumps(result),flush=True)
