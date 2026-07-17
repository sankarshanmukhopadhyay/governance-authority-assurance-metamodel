#!/usr/bin/env python3
from pathlib import Path
import json,re,csv,hashlib,sys,urllib.parse
from jsonschema import Draft202012Validator, FormatChecker
ROOT=Path(__file__).resolve().parents[1]
REL=json.loads((ROOT/'release.json').read_text()); VERSION=REL['version']; results=[]
def add(cid,ok,detail,kind='structural'):
 results.append({'id':cid,'kind':kind,'status':'pass' if ok else 'fail','evidence':detail})
def load(p): return json.loads(p.read_text())
# Release coherence: active artifacts only
active=[]
for base in ['README.md','index.md','VERSION','release.json','specification','profiles','schemas','vocabularies','examples','docs','mappings','matrices','threat-model']:
 p=ROOT/base
 active += [p] if p.is_file() else list(p.rglob('*'))
stale=[]
for p in active:
 if p.is_file() and p.suffix in {'.md','.json','.csv','.txt'}:
  t=p.read_text(errors='ignore')
  if re.search(r'(?<![\d.])0\.5\.0(?![\d.])|v0\.5\.0',t) and 'migration-v0.5.0' not in str(p) and p.name not in {'migration-v0.5.0-to-v0.9.0.md','README.md'}: stale.append(str(p.relative_to(ROOT)))
add('PUB-001-version-source',(ROOT/'VERSION').read_text().strip()==VERSION,f'authoritative version={VERSION}','publication')
add('PUB-002-active-version-coherence',not stale,'no stale active v0.5.0 references' if not stale else ', '.join(stale),'publication')
spec=(ROOT/REL['normativeSpecification']).read_text()
add('PUB-003-specification-identity',f'**Version:** {VERSION}' in spec and '**Status:** Candidate Specification' in spec,'normative specification identifies candidate release','publication')
# Requirements
ids=re.findall(r'\*\*(GAAM-[A-Z]+-\d{3}):\*\*',spec)
idx=list(csv.DictReader((ROOT/'matrices/normative-requirements-index.csv').open())); idxids=[r['requirement_id'] for r in idx]
add('REQ-001-unique',len(ids)==len(set(ids)),f'{len(ids)} identifiers','normative')
add('REQ-002-index-exact',ids==idxids,f'{len(idxids)} indexed requirements','normative')
add('REQ-003-normative-language',all(any(k in r['requirement'] for k in ['MUST','SHALL','SHOULD','MAY']) for r in idx),f'{len(idx)} indexed statements classified','normative')
# Schemas
schemas={p.stem.replace('.schema',''):load(p) for p in (ROOT/'schemas').glob('*.schema.json')}
base=REL['schemaBase']; ids_seen=[]
for name,obj in schemas.items():
 try: Draft202012Validator.check_schema(obj); ok=True; detail='valid Draft 2020-12 schema'
 except Exception as e: ok=False; detail=str(e)
 add('SCH-'+name,ok,detail,'schema'); ids_seen.append(obj.get('$id'))
add('SCH-IDS',len(ids_seen)==len(set(ids_seen)) and all(x.startswith(base) for x in ids_seen),f'{len(ids_seen)} unique canonical identifiers','schema')
cat=load(ROOT/'schemas/catalog.json'); add('SCH-CATALOG',len(cat['schemas'])==len(schemas) and {x['id'] for x in cat['schemas']}==set(ids_seen),'catalog covers all schemas','schema')
# Vocabularies
for p in sorted((ROOT/'vocabularies').glob('*.json')):
 o=load(p); vals=o.get('values',o.get('terms',[])); normalized=[json.dumps(x,sort_keys=True) for x in vals]
 add('VOC-'+p.stem,o.get('version')==VERSION and o.get('status')=='candidate' and o.get('extensionPolicy') in {'closed','controlled-extensible','profile-extensible','implementation-defined'} and len(normalized)==len(set(normalized)),f'{len(vals)} governed values','vocabulary')
# Profiles
pids=set(ids); manifests={}
for p in sorted((ROOT/'profiles/manifests').glob('*.json')):
 o=load(p); manifests[o['id']]=o
 errs=list(Draft202012Validator(schemas['profile-manifest'],format_checker=FormatChecker()).iter_errors(o)); missing=[x for x in o['requirements'] if x not in pids]
 depok=(p.stem=='foundation' and not o['dependencies']) or (p.stem!='foundation' and f'gaam:profile:foundation:{VERSION}' in o['dependencies'])
 doc=ROOT/'profiles'/(p.stem+'-profile.md'); doceq=doc.exists() and f'**Version:** {VERSION}' in doc.read_text()
 add('PRO-'+p.stem,not errs and not missing and depok and doceq,f'{len(o["requirements"])} requirements; dependencies={depok}; document={doceq}','profile')
all_profile_ids=set(manifests)
missingdeps=[d for o in manifests.values() for d in o['dependencies'] if d not in all_profile_ids]
add('PRO-DEPENDENCIES',not missingdeps,'all profile dependencies resolve' if not missingdeps else str(missingdeps),'profile')
# Fixtures and claims
for d in sorted((ROOT/'examples').iterdir()):
 if not d.is_dir(): continue
 for p in d.glob('*.valid.json'):
  o=load(p); key={'authority':'authority','decision-receipt':'decision-receipt'}.get(o.get('type')); errs=list(Draft202012Validator(schemas[key],format_checker=FormatChecker()).iter_errors(o)) if key else [Exception('unknown type')]
  add('FIX-'+d.name+'-'+p.stem,not errs,'accepted as expected' if not errs else str(errs[0]),'fixture')
 for p in d.glob('*.invalid.json'):
  errs=list(Draft202012Validator(schemas['authority'],format_checker=FormatChecker()).iter_errors(load(p))); add('FIX-'+d.name+'-'+p.stem,bool(errs),'rejected as expected' if errs else 'unexpectedly accepted','fixture')
 claim=load(d/'conformance-claim.json'); errs=list(Draft202012Validator(schemas['conformance-claim'],format_checker=FormatChecker()).iter_errors(claim)); evid=bool(claim.get('evidence')); independent=(claim.get('level')!='L4' or claim.get('assessmentIndependence')=='independent')
 add('CLM-'+d.name,not errs and evid and independent,'schema, evidence and independence rules satisfied','conformance')
# Behavioural vectors
def behaviour(o):
 x=o['input']; i=o['id']
 if i.startswith('authority-'): valid=x.get('status')=='active' and x.get('withinScope') and x.get('withinTime') and x.get('sourceValid')
 elif i.startswith('delegation-'): valid=x.get('delegationPermitted') and set(x.get('childEffects',[]))<=set(x.get('parentEffects',[])) and x.get('depth',0)<=x.get('maxDepth',0)
 elif i.startswith('decision-'): valid=all([x.get('authorityId'),x.get('policyId'),x.get('evidenceIds'),x.get('assuranceIds'),x.get('accountableParty')])
 elif i.startswith('high-impact-'): valid=(not x.get('highImpact')) or all([x.get('appealPath'),x.get('remedyPath'),x.get('affectedPartyAnalysis')])
 else: valid=False
 return bool(valid)
for p in sorted((ROOT/'tests/behavioural').glob('*.json')):
 o=load(p); actual=behaviour(o); add('BEH-'+o['id'],actual==o['expectedValid'],f'expected={o["expectedValid"]}; actual={actual}','behavioural')
# Threat traceability
tr=load(ROOT/'threat-model/threat-register.json'); test_ids={r['id'].replace('BEH-','') for r in results if r['kind']=='behavioural'}|{'claim-level-evidence','package-integrity'}
unmapped=[t['id'] for t in tr['threats'] if not t.get('requirements') or not t.get('tests') or any(x not in test_ids for x in t['tests'])]
add('THR-TRACE',not unmapped,f'{len(tr["threats"])} threats mapped to requirements and tests' if not unmapped else str(unmapped),'threat')
# Publication source contract
heading_errors=[]
for p in ROOT.rglob('*.md'):
 if '.git' in p.parts or 'packages' in p.parts: continue
 text=p.read_text(errors='ignore')
 match=re.match(r'^---\n(.*?)\n---\n(.*)$',text,re.S)
 if not match: continue
 layout_match=re.search(r'^layout:\s*(\S+)\s*$',match.group(1),re.M)
 if layout_match and layout_match.group(1) != 'page': continue
 body=match.group(2)
 h1s=re.findall(r'^#\s+.+$',body,re.M)
 if h1s: heading_errors.append(f'{p.relative_to(ROOT)} contains body H1: {h1s[0]}')
add('DOC-PAGE-TITLE-CONTRACT',not heading_errors,'all page-layout documents delegate H1 to front matter' if not heading_errors else '; '.join(heading_errors[:10]),'documentation')
# Local links
bad=[]
for p in ROOT.rglob('*.md'):
 if '.git' in p.parts or 'packages' in p.parts: continue
 for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text(errors='ignore')):
  if target.startswith(('http:','https:','mailto:','#')): continue
  clean=urllib.parse.unquote(target.split('#')[0]);
  if clean and not (p.parent/clean).resolve().exists(): bad.append(f'{p.relative_to(ROOT)} -> {target}')
add('DOC-LOCAL-LINKS',not bad,'all local links resolve' if not bad else '; '.join(bad[:10]),'documentation')
add('DOC-TSMM-CANONICAL','https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model' in (ROOT/'mappings/tsmm-v0.22.0-adoption-crosswalk.md').read_text(),'canonical TSMM repository link present','provenance')
add('CI-WORKFLOW',(ROOT/'.github/workflows/validate.yml').exists(),'validation workflow present','automation')
# Package manifest + integrity
pkg=ROOT/'packages'/f'gaam-v{VERSION}'; pkg.mkdir(parents=True,exist_ok=True)
artifact_paths=[REL['normativeSpecification'],'release.json','schemas/catalog.json','threat-model/threat-register.json','matrices/normative-requirements-index.csv','matrices/requirement-test-coverage.csv','matrices/threat-control-test-matrix.csv']
artifact_paths += [str(p.relative_to(ROOT)) for b in ['schemas','vocabularies','profiles/manifests','tests/behavioural'] for p in sorted((ROOT/b).glob('*.json'))]
manifest={'id':f'urn:gaam:package:{VERSION}','type':'gaam-governance-package','gaamVersion':VERSION,'status':'active','profiles':sorted(manifests),'artifacts':[{'id':Path(x).stem,'path':x,'mediaType':'application/json' if x.endswith('.json') else 'text/markdown' if x.endswith('.md') else 'text/csv'} for x in artifact_paths if not x.startswith(('schemas/','vocabularies/'))], 'schemas':[p.name for p in sorted((ROOT/'schemas').glob('*.schema.json'))], 'vocabularies':[p.name for p in sorted((ROOT/'vocabularies').glob('*.json'))], 'integrity':{'algorithm':'sha-256','manifest':'checksums.json'}}
(pkg/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
perrs=list(Draft202012Validator(schemas['gaam-package']).iter_errors(manifest)); add('PKG-MANIFEST',not perrs,'package manifest conforms','package')
checks=[]
for x in sorted(set(artifact_paths+[f'packages/gaam-v{VERSION}/manifest.json'])):
 p=ROOT/x
 if p.exists(): checks.append({'path':x,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(pkg/'checksums.json').write_text(json.dumps({'algorithm':'sha-256','scope':'declared source artifacts excluding this checksum file','files':checks},indent=2)+'\n')
verified=all(hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256'] for x in checks)
add('PKG-INTEGRITY',verified,f'{len(checks)} checksums verified','package')
# Reports
out=ROOT/'validation'; out.mkdir(exist_ok=True)
summary={'gaamVersion':VERSION,'testSuiteVersion':VERSION,'status':'pass' if all(r['status']=='pass' for r in results) else 'fail','checks':len(results),'passed':sum(r['status']=='pass' for r in results),'failed':sum(r['status']=='fail' for r in results),'results':results}
(out/'validation-report.json').write_text(json.dumps(summary,indent=2)+'\n')
md=['---','title: GAAM v0.9.0 Validation Report','permalink: /validation-report/','nav_exclude: true','artifact_type: Validation evidence','normative_status: Repository generated','---','{% include gaam-meta.html %}','',f'**Status:** {summary["status"].upper()}  ',f'**Checks:** {summary["checks"]}  ',f'**Passed:** {summary["passed"]}  ',f'**Failed:** {summary["failed"]}  ','','This report evidences repository publication, structural and included behavioural checks. It is not an independent L4 assessment.','','| ID | Kind | Status | Evidence |','|---|---|---|---|']
md += [f'| `{r["id"]}` | {r["kind"]} | {r["status"].upper()} | {r["evidence"].replace("|","/")} |' for r in results]
(ROOT/'VALIDATION_REPORT.md').write_text('\n'.join(md)+'\n')
print(json.dumps({k:summary[k] for k in ['status','checks','passed','failed']},indent=2)); sys.exit(0 if summary['status']=='pass' else 1)
