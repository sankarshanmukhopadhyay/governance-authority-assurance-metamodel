#!/usr/bin/env python3
from pathlib import Path
import json, sys
root=Path(__file__).resolve().parents[1]
site=root/'_site'
required=[
 'index.html','specification/index.html','profiles/index.html','schemas/index.html',
 'vocabularies/index.html','docs/index.html','conformance/index.html','releases/index.html',
 'threat-model/index.html','validation-report/index.html'
]
errors=[]
for rel in required:
    if not (site/rel).is_file(): errors.append(f'missing rendered page: {rel}')
for srcdir in ('schemas','vocabularies'):
    for src in (root/srcdir).glob('*.json'):
        out=site/srcdir/src.name
        if not out.is_file(): errors.append(f'missing published artifact: {srcdir}/{src.name}')
        else:
            try: json.loads(out.read_text())
            except Exception as exc: errors.append(f'invalid published JSON {out}: {exc}')
for schema in (root/'schemas').glob('*.json'):
    data=json.loads(schema.read_text())
    sid=data.get('$id','')
    marker='/governance-authority-assurance-metamodel/'
    if marker in sid:
        rel=sid.split(marker,1)[1]
        if not (site/rel).is_file(): errors.append(f'$id has no rendered artifact: {sid}')
if errors:
    print('Pages validation: FAIL')
    for e in errors: print('-',e)
    sys.exit(1)
print(f'Pages validation: PASS ({len(required)} required pages; canonical JSON artifacts published)')
