"""Rebuild base and expansions in order; restore already-released weekly packs."""
import subprocess,json,sys
from pathlib import Path
for script in ['seed-content.py','seed-listening.py','seed-production.py','seed-vocab.py','expand-reading.py','expand-listening.py','expand-production.py','expand-vocabulary.py']:
 subprocess.run([sys.executable,str(Path('scripts')/script)],check=True)
p=Path('src/data/papers.json');papers=json.loads(p.read_text(encoding='utf-8'))
history=Path('content-reserve/released.json')
for name in json.loads(history.read_text()) if history.exists() else []:
 for paper in json.loads((history.parent/name).read_text(encoding='utf-8')):
  if not any(x['id']==paper['id'] for x in papers):papers.append(paper)
p.write_text(json.dumps(papers,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
