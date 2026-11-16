import {readFile,writeFile,mkdir} from 'node:fs/promises';
const resources=JSON.parse(await readFile('src/data/resources.json','utf8'));
const results=[];
// Sequential and low-volume. A 403/429 is a manual-review item, never proof of a dead link.
for(const r of resources){let status,error;try{const response=await fetch(r.url,{method:'HEAD',redirect:'follow',signal:AbortSignal.timeout(15000),headers:{'User-Agent':'IELTS-Academic-Studio-Link-Check/1.0'}});status=response.status;if([404,405,410].includes(status)){const retry=await fetch(r.url,{signal:AbortSignal.timeout(15000)});status=retry.status;await retry.body?.cancel();}}catch(e){error=String(e);}const review=!error&&(status===404||status===410)?'broken':!error&&status&&status>=200&&status<400?'reachable':'manual-review';results.push({id:r.id,url:r.url,status,error,review,checked:new Date().toISOString()});console.log(r.id,status??'network error',review);}
await mkdir('reports',{recursive:true});await writeFile('reports/link-check.json',JSON.stringify(results,null,2));
if(results.some(r=>r.review==='broken'))process.exitCode=1;
