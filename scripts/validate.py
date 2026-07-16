#!/usr/bin/env python3
from pathlib import Path
import json,re,csv,hashlib,sys
from jsonschema import Draft202012Validator, FormatChecker
root=Path(__file__).resolve().parents[1]
results=[]
def add(name,ok,detail): results.append({'check':name,'status':'pass' if ok else 'fail','detail':detail})
# requirements
spec=(root/'specification/governance-authority-assurance-metamodel.md').read_text()
ids=re.findall(r'\*\*(GAAM-[A-Z]+-\d{3}):\*\*',spec)
idx=list(csv.DictReader((root/'matrices/normative-requirements-index.csv').open()))
idxids=[r['requirement_id'] for r in idx]
add('requirement-uniqueness',len(ids)==len(set(ids)),f'{len(ids)} requirements')
add('requirement-index',ids==idxids,f'{len(idxids)} indexed requirements')
# schemas
schemas={p.stem.replace('.schema',''):json.loads(p.read_text()) for p in (root/'schemas').glob('*.schema.json')}
for name,obj in schemas.items():
 try: Draft202012Validator.check_schema(obj); add('schema:'+name,True,'valid Draft 2020-12 schema')
 except Exception as e: add('schema:'+name,False,str(e))
# profile manifests
pids=set(ids)
for p in (root/'profiles/manifests').glob('*.json'):
 o=json.loads(p.read_text()); v=Draft202012Validator(schemas['profile-manifest'],format_checker=FormatChecker()); errs=list(v.iter_errors(o))
 missing=[x for x in o['requirements'] if x not in pids]
 depok=(p.stem=='foundation' and not o['dependencies']) or (p.stem!='foundation' and 'gaam:profile:foundation:0.5.0' in o['dependencies'])
 add('profile:'+p.stem,not errs and not missing and depok,f'{len(o["requirements"])} requirements; dependency closure={depok}')
# examples
for d in sorted((root/'examples').iterdir()):
 if not d.is_dir(): continue
 for p in d.glob('*.valid.json'):
  typ=json.loads(p.read_text()).get('type'); key={'authority':'authority','decision-receipt':'decision-receipt'}.get(typ)
  errs=list(Draft202012Validator(schemas[key],format_checker=FormatChecker()).iter_errors(json.loads(p.read_text()))) if key else [1]
  add('valid-fixture:'+d.name+'/'+p.name,not errs,'accepted as expected' if not errs else str(errs[0]))
 for p in d.glob('*.invalid.json'):
  o=json.loads(p.read_text()); key='authority'; errs=list(Draft202012Validator(schemas[key],format_checker=FormatChecker()).iter_errors(o)); add('invalid-fixture:'+d.name+'/'+p.name,bool(errs),'rejected as expected' if errs else 'unexpectedly accepted')
 claim=d/'conformance-claim.json'
 errs=list(Draft202012Validator(schemas['conformance-claim'],format_checker=FormatChecker()).iter_errors(json.loads(claim.read_text())))
 add('claim:'+d.name,not errs,'valid conformance claim')
# links - local markdown links
bad=[]
for p in root.rglob('*.md'):
 if any(x in p.parts for x in ['.git','validation']): continue
 txt=p.read_text(errors='ignore')
 for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',txt):
  if target.startswith(('http:','https:','#','mailto:')): continue
  clean=target.split('#')[0]
  if not clean: continue
  q=(p.parent/clean).resolve()
  if not q.exists(): bad.append(f'{p.relative_to(root)} -> {target}')
add('local-links',not bad,'all local links resolve' if not bad else '; '.join(bad[:10]))
# package integrity checksums
files=[]
for base in ['schemas','vocabularies','profiles/manifests']:
 for p in sorted((root/base).glob('*.json')):
  files.append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(root/'packages/gaam-v0.5.0/checksums.json').write_text(json.dumps({'algorithm':'sha-256','files':files},indent=2)+'\n')
# output
out=root/'validation'; out.mkdir(exist_ok=True)
summary={'gaamVersion':'0.5.0','status':'pass' if all(r['status']=='pass' for r in results) else 'fail','checks':len(results),'passed':sum(r['status']=='pass' for r in results),'failed':sum(r['status']=='fail' for r in results),'results':results}
(out/'validation-report.json').write_text(json.dumps(summary,indent=2)+'\n')
md=['# GAAM v0.5.0 Validation Report','',f"**Status:** {summary['status'].upper()}",f"**Checks:** {summary['checks']}  ",f"**Passed:** {summary['passed']}  ",f"**Failed:** {summary['failed']}",'','| Check | Status | Evidence |','|---|---|---|']
md += [f"| `{r['check']}` | {r['status'].upper()} | {r['detail'].replace('|','/')} |" for r in results]
(root/'VALIDATION_REPORT.md').write_text('\n'.join(md)+'\n')
print(json.dumps({k:summary[k] for k in ['status','checks','passed','failed']},indent=2))
sys.exit(0 if summary['status']=='pass' else 1)
