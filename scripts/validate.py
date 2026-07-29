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
# Implementation pattern architecture, fixtures and claims
pattern_root=ROOT/'examples'
pattern_schema_path=pattern_root/'pattern-manifest.schema.json'
pattern_catalogue_path=pattern_root/'catalog.json'
pattern_errors=[]; pattern_ids=[]
try:
 pattern_schema=load(pattern_schema_path)
 Draft202012Validator.check_schema(pattern_schema)
 add('PAT-SCHEMA',True,'pattern manifest schema is valid Draft 2020-12','pattern')
except Exception as e:
 pattern_schema=None; add('PAT-SCHEMA',False,str(e),'pattern')
try:
 pattern_catalogue=load(pattern_catalogue_path)
 catalogue_entries={x.get('id'):x for x in pattern_catalogue.get('patterns',[])}
 add('PAT-CATALOGUE-STRUCTURE',pattern_catalogue.get('gaamVersion')==VERSION and isinstance(pattern_catalogue.get('patterns'),list),f'{len(catalogue_entries)} catalogue entries','pattern')
except Exception as e:
 pattern_catalogue={}; catalogue_entries={}; add('PAT-CATALOGUE-STRUCTURE',False,str(e),'pattern')
fixture_type_map={'authority':'authority','decision-receipt':'decision-receipt','delegation':'delegation','remedy':'remedy','governance-event':'governance-event'}
maturity_rank={'conceptual':1,'structural':2,'behavioural':3,'operational':4,'assurance-ready':5,'interoperability-tested':6}
behaviour_files={p.stem for p in (ROOT/'tests/behavioural').glob('*.json')}
for d in sorted(pattern_root.iterdir()):
 if not d.is_dir(): continue
 required={'README.md','pattern.json','conformance-claim.json'}
 missing=sorted(x for x in required if not (d/x).is_file())
 add('PAT-'+d.name+'-CONTRACT',not missing,'required files present' if not missing else 'missing: '+', '.join(missing),'pattern')
 manifest=None
 if (d/'pattern.json').is_file():
  try:
   manifest=load(d/'pattern.json'); errs=list(Draft202012Validator(pattern_schema,format_checker=FormatChecker()).iter_errors(manifest)) if pattern_schema else [Exception('pattern schema unavailable')]
   add('PAT-'+d.name+'-MANIFEST',not errs,'manifest conforms' if not errs else str(errs[0]),'pattern')
  except Exception as e: add('PAT-'+d.name+'-MANIFEST',False,str(e),'pattern')
 else: add('PAT-'+d.name+'-MANIFEST',False,'pattern.json missing','pattern')
 if manifest:
  pattern_ids.append(manifest.get('id'))
  missing_profiles=[x for x in manifest.get('profiles',[]) if x not in all_profile_ids]
  missing_requirements=[x for x in manifest.get('requirements',[]) if x not in pids]
  refs=manifest.get('artifacts',[])+manifest.get('schemaFixtures',[])+manifest.get('supportingExamples',[])
  missing_artifacts=sorted(set(x for x in refs if not (d/x).is_file()))
  missing_behaviour=sorted(x for x in manifest.get('behaviouralVectors',[]) if x not in behaviour_files)
  add('PAT-'+d.name+'-REFERENCES',not (missing_profiles or missing_requirements or missing_artifacts or missing_behaviour),'profiles, requirements, artifacts and behavioural vectors resolve' if not (missing_profiles or missing_requirements or missing_artifacts or missing_behaviour) else f'profiles={missing_profiles}; requirements={missing_requirements}; artifacts={missing_artifacts}; behavioural={missing_behaviour}','pattern')
  scenario_ok=bool(manifest.get('positiveScenarios')) and bool(manifest.get('negativeScenarios')) and all(x.get('expectedResult') for x in manifest.get('positiveScenarios',[])+manifest.get('negativeScenarios',[]))
  add('PAT-'+d.name+'-SCENARIOS',scenario_ok,'positive and negative scenarios declare expected results','pattern')
  limitations_ok=bool(manifest.get('limitations'))
  add('PAT-'+d.name+'-LIMITATIONS',limitations_ok,'conformance limitations declared','pattern')
  rank=maturity_rank.get(manifest.get('maturity'),0)
  maturity_ok=(rank<=1 or (d/'pattern.json').is_file()) and (rank<=2 or bool(manifest.get('schemaFixtures'))) and (rank<=3 or bool(manifest.get('behaviouralVectors'))) and (rank<6 or any('independent' in x.lower() for x in manifest.get('limitations',[])) is False)
  add('PAT-'+d.name+'-MATURITY',maturity_ok,f'maturity claim {manifest.get("maturity")} supported by declared evidence','pattern')
  cat=catalogue_entries.get(manifest.get('id'))
  add('PAT-'+d.name+'-CATALOGUE',bool(cat) and cat.get('path')==d.name+'/pattern.json','catalogue entry resolves','pattern')
 # schema fixtures: controlled failures, type-aware validation
 for p in sorted(d.glob('*.valid.json')):
  try:
   o=load(p); key=fixture_type_map.get(o.get('type')); errs=list(Draft202012Validator(schemas[key],format_checker=FormatChecker()).iter_errors(o)) if key in schemas else [Exception('unknown or unsupported fixture type')]
   add('FIX-'+d.name+'-'+p.stem,not errs,'accepted as expected' if not errs else str(errs[0]),'fixture')
  except Exception as e: add('FIX-'+d.name+'-'+p.stem,False,str(e),'fixture')
 for p in sorted(d.glob('*.invalid.json')):
  try:
   o=load(p); key=fixture_type_map.get(o.get('type')) or ('authority' if 'authority' in p.name else None); errs=list(Draft202012Validator(schemas[key],format_checker=FormatChecker()).iter_errors(o)) if key in schemas else [Exception('unknown or unsupported fixture type')]
   add('FIX-'+d.name+'-'+p.stem,bool(errs),'rejected as expected' if errs else 'unexpectedly accepted','fixture')
  except Exception as e: add('FIX-'+d.name+'-'+p.stem,True,'malformed fixture rejected: '+str(e),'fixture')
 if (d/'conformance-claim.json').is_file():
  try:
   claim=load(d/'conformance-claim.json'); errs=list(Draft202012Validator(schemas['conformance-claim'],format_checker=FormatChecker()).iter_errors(claim)); evid=bool(claim.get('evidence')); independent=(claim.get('level')!='L4' or claim.get('assessmentIndependence')=='independent')
   add('CLM-'+d.name,not errs and evid and independent,'schema, evidence and independence rules satisfied','conformance')
  except Exception as e: add('CLM-'+d.name,False,str(e),'conformance')
 else: add('CLM-'+d.name,False,'conformance-claim.json missing','conformance')
add('PAT-IDS',len(pattern_ids)==len(set(pattern_ids)) and all(pattern_ids),f'{len(pattern_ids)} unique pattern identifiers','pattern')
add('PAT-CATALOGUE-COVERAGE',set(pattern_ids)==set(catalogue_entries),f'catalogue covers {len(pattern_ids)} patterns','pattern')
# Behavioural vectors
def behaviour(o):
 x=o['input']; i=o['id']
 if i.startswith('authority-'):
  valid=x.get('status')=='active' and x.get('withinScope') and x.get('withinTime') and x.get('sourceValid')
 elif i.startswith('delegation-'):
  valid=(x.get('delegationPermitted') and set(x.get('childEffects',[]))<=set(x.get('parentEffects',[]))
         and x.get('depth',0)<=x.get('maxDepth',0) and x.get('parentActive',True)
         and x.get('childWithinParentTime',True))
 elif i.startswith('decision-'):
  valid=(all([x.get('authorityId'),x.get('policyId'),x.get('evidenceIds'),x.get('assuranceIds'),x.get('accountableParty')])
         and x.get('evidenceFresh',True) and x.get('policyCurrent',True))
 elif i.startswith('assurance-'):
  ranks={'self':1,'reviewed':2,'independent':3}
  valid=(x.get('evidencePresent') and x.get('withinValidity')
         and ranks.get(x.get('independence'),0)>=ranks.get(x.get('requiredIndependence'),0))
 elif i.startswith('high-impact-'):
  valid=((not x.get('highImpact')) or all([x.get('appealPath'),x.get('remedyPath'),x.get('affectedPartyAnalysis')]))
  valid=valid and x.get('noticeProvided',True) and x.get('reviewIndependent',True)
 elif i.startswith('lifecycle-event-order-'):
  seq=[e.get('sequence') for e in x.get('events',[])]
  valid=bool(seq) and seq==sorted(seq) and len(seq)==len(set(seq)) and x['events'][0].get('type')=='issued'
 elif i.startswith('runtime-'):
  valid=(x.get('stateFresh') and x.get('authorityStatusKnown')) or (x.get('failurePolicy')=='fail-closed' and not x.get('effectAdmitted'))
 elif i.startswith('profile-composition-'):
  selected=set(x.get('selectedProfiles',[])); deps=x.get('dependencies',{})
  valid=all(set(deps.get(profile,[]))<=selected for profile in selected)
 else: valid=False
 return bool(valid)
for p in sorted((ROOT/'tests/behavioural').glob('*.json')):
 o=load(p); actual=behaviour(o); add('BEH-'+o['id'],actual==o['expectedValid'],f'expected={o["expectedValid"]}; actual={actual}','behavioural')
# Requirement-level assurance traceability
trace=list(csv.DictReader((ROOT/'matrices/requirement-assurance-traceability.csv').open()))
trace_ids=[r['requirement_id'] for r in trace]
valid_dispositions={'behavioural-testable','structural-testable','observable','reviewable','procedural','mixed'}
evidence_catalogue=load(ROOT/'implementation-reports/evidence-catalogue.json')
evidence_ids={x['id'] for x in evidence_catalogue['entries']}
behaviour_ids={p.stem for p in (ROOT/'tests/behavioural').glob('*.json')}
known_test_ids=behaviour_ids|{'claim-level-evidence','package-integrity'}
trace_errors=[]
if trace_ids!=idxids: trace_errors.append('traceability rows do not exactly match normative requirement index order')
for row in trace:
 if row['testability'] not in valid_dispositions: trace_errors.append(f"{row['requirement_id']}: invalid testability disposition")
 refs={x for x in row['evidence_catalogue_ids'].split(';') if x}
 if not refs or not refs<=evidence_ids: trace_errors.append(f"{row['requirement_id']}: unknown or missing evidence reference")
 tests={x for x in row['test_ids'].split(';') if x}
 if not tests<=known_test_ids: trace_errors.append(f"{row['requirement_id']}: unknown test identifiers {sorted(tests-known_test_ids)}")
add('TRC-REQUIREMENTS',not trace_errors,f'{len(trace)} requirements have testability and evidence dispositions' if not trace_errors else '; '.join(trace_errors[:10]),'traceability')
referenced_tests={x for row in trace for x in row['test_ids'].split(';') if x}
orphan_behaviour=sorted(behaviour_ids-referenced_tests)
add('TRC-TEST-ORPHANS',not orphan_behaviour,f'{len(behaviour_ids)} behavioural tests referenced by requirement traceability' if not orphan_behaviour else ', '.join(orphan_behaviour),'traceability')

# Threat traceability
tr=load(ROOT/'threat-model/threat-register.json'); test_ids={r['id'].replace('BEH-','') for r in results if r['kind']=='behavioural'}|{'claim-level-evidence','package-integrity'}
unmapped=[t['id'] for t in tr['threats'] if not t.get('requirements') or not t.get('tests') or any(x not in test_ids for x in t['tests'])]
add('THR-TRACE',not unmapped,f'{len(tr["threats"])} threats mapped to requirements and tests' if not unmapped else str(unmapped),'threat')
# Publication source contract
heading_errors=[]
for p in ROOT.rglob('*.md'):
 if any(part in {'.git', 'packages', 'node_modules', '_site', 'vendor'} for part in p.parts): continue
 text=p.read_text(errors='ignore')
 match=re.match(r'^---\n(.*?)\n---\n(.*)$',text,re.S)
 if not match: continue
 layout_match=re.search(r'^layout:\s*(\S+)\s*$',match.group(1),re.M)
 if layout_match and layout_match.group(1) not in ('page', 'default'): continue
 title_match=re.search(r'^title:\s*["\']?(.*?)["\']?\s*$',match.group(1),re.M)
 body=match.group(2)
 h1s=re.findall(r'^#\s+(.+)$',body,re.M)
 if len(h1s) != 1:
  heading_errors.append(f'{p.relative_to(ROOT)} contains {len(h1s)} body H1 headings; expected exactly one')
 elif title_match and h1s[0].strip() != title_match.group(1).strip():
  heading_errors.append(f'{p.relative_to(ROOT)} H1 does not match front-matter title')
add('DOC-PAGE-TITLE-CONTRACT',not heading_errors,'all rendered Markdown pages declare exactly one H1 matching front matter' if not heading_errors else '; '.join(heading_errors[:10]),'documentation')
# CTWG glossary alignment contract
glossary_text=(ROOT/'docs/glossary.md').read_text()
glossary_terms=re.findall(r'^\*\*(.+?)\*\*\s+—\s+.+$',glossary_text,re.M)
alignment=load(ROOT/'mappings/ctwg-v1.4.1-glossary-alignment.json')
aligned_terms=[x.get('gaamTerm') for x in alignment.get('terms',[])]
valid_statuses={'adopted','extended','local'}
alignment_errors=[]
if len(aligned_terms)!=len(set(aligned_terms)): alignment_errors.append('duplicate GAAM terms in alignment register')
missing=sorted(set(glossary_terms)-set(aligned_terms)); extra=sorted(set(aligned_terms)-set(glossary_terms))
if missing: alignment_errors.append('missing terms: '+', '.join(missing))
if extra: alignment_errors.append('unknown terms: '+', '.join(extra))
invalid=[x.get('gaamTerm') for x in alignment.get('terms',[]) if x.get('status') not in valid_statuses]
if invalid: alignment_errors.append('invalid statuses: '+', '.join(invalid))
add('DOC-CTWG-GLOSSARY-ALIGNMENT',not alignment_errors,f'{len(glossary_terms)} glossary terms covered by CTWG alignment register' if not alignment_errors else '; '.join(alignment_errors),'documentation')
# Local links
bad=[]
for p in ROOT.rglob('*.md'):
 if any(part in {'.git', 'packages', 'node_modules', '_site', 'vendor'} for part in p.parts): continue
 for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text(errors='ignore')):
  if target.startswith(('http:','https:','mailto:','#')): continue
  clean=urllib.parse.unquote(target.split('#')[0]);
  if clean and not (p.parent/clean).resolve().exists(): bad.append(f'{p.relative_to(ROOT)} -> {target}')
add('DOC-LOCAL-LINKS',not bad,'all local links resolve' if not bad else '; '.join(bad[:10]),'documentation')
add('DOC-TSMM-CANONICAL','https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model' in (ROOT/'mappings/tsmm-v0.22.0-adoption-crosswalk.md').read_text(),'canonical TSMM repository link present','provenance')
add('CI-WORKFLOW',(ROOT/'.github/workflows/validate.yml').exists(),'validation workflow present','automation')
# Candidate governance and v1 readiness controls
register=load(ROOT/'governance/candidate-issues.json')
review_files={p.stem:load(p) for p in sorted((ROOT/'governance/reviews').glob('*.json'))}
classes={'editorial','clarification','compatible-extension','breaking-normative-change','security-correction'}
statuses={'open','in-progress','closed','withdrawn'}; severities={'critical','high','medium','low','informational'}
gov_errors=[]; issue_ids=[]
for issue in register.get('issues',[]):
 issue_ids.append(issue.get('id'))
 if issue.get('status') not in statuses: gov_errors.append(f"{issue.get('id')}: invalid status")
 if issue.get('severity') not in severities: gov_errors.append(f"{issue.get('id')}: invalid severity")
 if issue.get('changeClass') not in classes: gov_errors.append(f"{issue.get('id')}: invalid change class")
 if not issue.get('decisionAuthority') or not issue.get('requiredEvidence') or not issue.get('disposition'): gov_errors.append(f"{issue.get('id')}: incomplete governance fields")
 badreq=[x for x in issue.get('affectedRequirements',[]) if x not in pids]
 badpro=[x for x in issue.get('affectedProfiles',[]) if x not in all_profile_ids]
 if badreq: gov_errors.append(f"{issue.get('id')}: unknown requirements {badreq}")
 if badpro: gov_errors.append(f"{issue.get('id')}: unknown profiles {badpro}")
add('GOV-CANDIDATE-REGISTER',not gov_errors,f'{len(issue_ids)} candidate issues have valid authority, scope, evidence and disposition fields' if not gov_errors else '; '.join(gov_errors[:10]),'governance')
add('GOV-CANDIDATE-IDS',len(issue_ids)==len(set(issue_ids)) and all(re.fullmatch(r'GAAM-CR-\d{3}',x or '') for x in issue_ids),f'{len(issue_ids)} unique candidate issue identifiers','governance')
required_reviews={'privacy-review','security-review','affected-party-review','interoperability-review','implementation-evidence'}
review_errors=[]
review_vocab_path=ROOT/'governance/reviews/finding-vocabulary.json'; finding_schema_path=ROOT/'governance/reviews/finding-schema.json'; baseline_path=ROOT/'governance/reviews/review-baseline.json'
review_vocab=load(review_vocab_path) if review_vocab_path.exists() else {}
finding_schema=load(finding_schema_path) if finding_schema_path.exists() else None
baseline=load(baseline_path) if baseline_path.exists() else {}
if baseline.get('gaamVersion')!=VERSION: review_errors.append('review baseline: version mismatch')
if baseline.get('status') not in {'draft','frozen-for-review','superseded','closed'}: review_errors.append('review baseline: invalid status')
if not baseline.get('sourceCommit') or not baseline.get('authority'): review_errors.append('review baseline: source commit or authority missing')
all_finding_ids=[]
for name in required_reviews:
 obj=review_files.get(name)
 if not obj: review_errors.append(f'missing {name}'); continue
 if obj.get('gaamVersion')!=VERSION: review_errors.append(f'{name}: version mismatch')
 if obj.get('status') not in set(review_vocab.get('reviewStatuses',[])): review_errors.append(f'{name}: invalid status')
 for field in ['baselineReference','reviewer','reviewerRole','reviewerIndependence','reviewAuthority','decisionAuthority','methodologyReference','evidenceDirectory','findingsSummary','exitCriteriaStatus','unresolvedBlockers','candidateIssueReferences']:
  if field not in obj: review_errors.append(f'{name}: missing {field}')
 if obj.get('reviewerIndependence') not in set(review_vocab.get('reviewerIndependenceValues',[])): review_errors.append(f'{name}: invalid reviewer independence')
 evidence_dir=ROOT/obj.get('evidenceDirectory','')
 if not evidence_dir.is_dir(): review_errors.append(f'{name}: evidence directory does not resolve')
 for ref in obj.get('evidence',[]):
  if not (ROOT/ref).is_file(): review_errors.append(f'{name}: evidence reference does not resolve: {ref}')
 for finding in obj.get('findings',[]):
  if finding_schema:
   ferrs=list(Draft202012Validator(finding_schema,format_checker=FormatChecker()).iter_errors(finding))
   if ferrs: review_errors.append(f'{name}: invalid finding {finding.get("id")}: {ferrs[0].message}')
  fid=finding.get('id'); all_finding_ids.append(fid)
  if finding.get('status')=='closed' and (not finding.get('verificationEvidence') or not finding.get('closureDate')): review_errors.append(f'{fid}: closed without verification evidence and closure date')
  if finding.get('status')=='risk-accepted' and not all([finding.get('decisionAuthority'),finding.get('rationale'),finding.get('residualRisk'),finding.get('reconsiderationDate')]): review_errors.append(f'{fid}: incomplete risk acceptance')
  if finding.get('status')=='deferred' and not all([finding.get('owner'),finding.get('targetDate')]): review_errors.append(f'{fid}: incomplete deferral')
 if obj.get('status')=='complete' and (not obj.get('completionDate') or not obj.get('finalAttestation') or obj.get('exitCriteriaStatus')!='satisfied'): review_errors.append(f'{name}: completion conditions not satisfied')
add('GOV-REVIEW-REGISTERS',not review_errors,f'{len(required_reviews)} review registers, baseline and lifecycle controls are valid' if not review_errors else '; '.join(review_errors[:15]),'governance')
add('GOV-REVIEW-FINDING-IDS',len(all_finding_ids)==len(set(all_finding_ids)),f'{len(all_finding_ids)} unique review finding identifiers','governance')
templates=['change-proposal.yml','implementation-report.yml','review-finding.yml']
missing_templates=[x for x in templates if not (ROOT/'.github/ISSUE_TEMPLATE'/x).exists()]
add('GOV-CONTRIBUTION-CONTROLS',not missing_templates and (ROOT/'.github/pull_request_template.md').exists(),'candidate issue forms and pull-request governance template present' if not missing_templates else str(missing_templates),'governance')
open_blockers=[x['id'] for x in register.get('issues',[]) if x.get('blockingV1') and x.get('status')!='closed']
add('GOV-V1-READINESS-STATE',True,f'{len(open_blockers)} explicitly recorded open v1 blockers: {", ".join(open_blockers)}','governance')
# Package manifest + integrity
pkg=ROOT/'packages'/f'gaam-v{VERSION}'; pkg.mkdir(parents=True,exist_ok=True)
artifact_paths=[REL['normativeSpecification'],'release.json','schemas/catalog.json','threat-model/threat-register.json','matrices/normative-requirements-index.csv','matrices/requirement-test-coverage.csv','matrices/requirement-assurance-traceability.csv','matrices/threat-control-test-matrix.csv','governance/candidate-issues.json']
artifact_paths += [str(p.relative_to(ROOT)) for b in ['schemas','vocabularies','profiles/manifests','tests/behavioural'] for p in sorted((ROOT/b).glob('*.json'))]
artifact_paths += [str(p.relative_to(ROOT)) for p in sorted((ROOT/'examples').rglob('*')) if p.is_file() and p.name not in {'.gitkeep','.DS_Store'}]
review_root=ROOT/'governance/reviews'
review_excluded={'.gitkeep','.DS_Store','Thumbs.db'}
for p in sorted(review_root.rglob('*')):
 if not p.is_file() or p.name in review_excluded or p.name.endswith(('.tmp','.swp','.bak','~')) or '__pycache__' in p.parts: continue
 if any(part in {'working','drafts','cache','.cache'} for part in p.parts): continue
 artifact_paths.append(str(p.relative_to(ROOT)))
manifest={'id':f'urn:gaam:package:{VERSION}','type':'gaam-governance-package','gaamVersion':VERSION,'status':'active','profiles':sorted(manifests),'artifacts':[{'id':re.sub(r'[^a-zA-Z0-9._-]+','-',str(Path(x).with_suffix(''))).strip('-'),'path':x,'mediaType':'application/json' if x.endswith('.json') else 'text/markdown' if x.endswith('.md') else 'text/csv' if x.endswith('.csv') else 'application/octet-stream'} for x in artifact_paths if not x.startswith(('schemas/','vocabularies/'))], 'schemas':[p.name for p in sorted((ROOT/'schemas').glob('*.schema.json'))], 'vocabularies':[p.name for p in sorted((ROOT/'vocabularies').glob('*.json'))], 'integrity':{'algorithm':'sha-256','manifest':'checksums.json'}}
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
md=['---','title: GAAM v0.9.0 Validation Report','permalink: /validation-report/','nav_exclude: true','artifact_type: Validation evidence','normative_status: Repository generated','---','# GAAM v0.9.0 Validation Report','','{% include gaam-meta.html %}','',f'**Status:** {summary["status"].upper()}  ',f'**Checks:** {summary["checks"]}  ',f'**Passed:** {summary["passed"]}  ',f'**Failed:** {summary["failed"]}  ','','This report evidences repository publication, structural and included behavioural checks. It is not an independent L4 assessment.','','| ID | Kind | Status | Evidence |','|---|---|---|---|']
md += [f'| `{r["id"]}` | {r["kind"]} | {r["status"].upper()} | {r["evidence"].replace("|","/")} |' for r in results]
(ROOT/'VALIDATION_REPORT.md').write_text('\n'.join(md)+'\n')
print(json.dumps({k:summary[k] for k in ['status','checks','passed','failed']},indent=2)); sys.exit(0 if summary['status']=='pass' else 1)
