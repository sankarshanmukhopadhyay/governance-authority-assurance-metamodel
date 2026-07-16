#!/usr/bin/env python3
from pathlib import Path
import json, zipfile
root=Path(__file__).resolve().parents[1]
version=(root/'VERSION').read_text().strip()
out=root/'dist'; out.mkdir(exist_ok=True)
target=out/f'governance-authority-assurance-metamodel-v{version}.zip'
exclude={'.git','dist','__pycache__'}
files=[p for p in root.rglob('*') if p.is_file() and not any(x in p.parts for x in exclude)]
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files,key=lambda x:str(x.relative_to(root))):
  info=zipfile.ZipInfo(str(Path(f'governance-authority-assurance-metamodel-v{version}')/p.relative_to(root)),date_time=(2026,7,16,0,0,0))
  info.external_attr=0o644<<16
  z.writestr(info,p.read_bytes())
print(target)
