"""Package explicit public paths, never private data or dependency stores."""
import pathlib,zipfile,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'releases';OUT.mkdir(exist_ok=True)
name=OUT/'ielts-academic-studio-v1.4.1.zip'
allowed=['content','content-reserve','src','public','scripts','docs','tests','.github','reports','dist']
files=['package.json','pnpm-lock.yaml','pnpm-workspace.yaml','index.html','vite.config.ts','tsconfig.json','.gitignore','AGENTS.md','README.md','LICENSE','THIRD_PARTY.md','CHANGELOG.md','DELIVERY.md','启动网站.cmd']
with zipfile.ZipFile(name,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for d in allowed:
  for f in (ROOT/d).rglob('*'):
   if f.is_file() and '__pycache__' not in f.parts:z.write(f,'ielts-academic-studio/'+f.relative_to(ROOT).as_posix())
 for n in files:
  f=ROOT/n
  if f.is_file():z.write(f,'ielts-academic-studio/'+n)
digest=hashlib.sha256(name.read_bytes()).hexdigest()
(OUT/(name.name+'.sha256')).write_text(digest+'  '+name.name+'\n',encoding='utf-8')
print(name);print('bytes',name.stat().st_size);print('sha256',digest)
