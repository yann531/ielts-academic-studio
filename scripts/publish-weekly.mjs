import {readFile,writeFile,readdir} from 'node:fs/promises';
const read=async p=>JSON.parse(await readFile(p,'utf8'));
const history=await read('content-reserve/released.json');
const files=(await readdir('content-reserve')).filter(f=>/^batch-\d+\.json$/.test(f)).sort();
const next=files.find(f=>!history.includes(f));
if(!next){console.log('Reserve exhausted; author and review more batches.');process.exit(0);}
const batch=await read('content-reserve/'+next),papers=await read('src/data/papers.json');
if(process.argv.includes('--dry-run')){console.log('Next batch:',next,batch.map(p=>p.title));process.exit(0);}
for(const p of batch)if(!papers.some(x=>x.id===p.id))papers.push({...p,updated:new Date().toISOString().slice(0,10)});
await writeFile('src/data/papers.json',JSON.stringify(papers,null,2)+'\n');
await writeFile('content-reserve/released.json',JSON.stringify([...history,next],null,2)+'\n');
console.log('Released:',next);
