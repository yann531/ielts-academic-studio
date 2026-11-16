import {readdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import path from 'node:path';
const root=path.resolve('dist');
async function files(dir){const out=[];for(const e of await readdir(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())out.push(...await files(p));else if(e.name!=='sw.js')out.push(p);}return out;}
const paths=await files(root),hash=createHash('sha256');for(const p of paths)hash.update(await readFile(p));
const version=hash.digest('hex').slice(0,12),urls=['./',...paths.map(p=>'./'+path.relative(root,p).replaceAll('\\','/'))];
await writeFile(path.join(root,'sw.js'),`/* Opt-in offline cache. Only this site; never external resources or model requests. */
const PREFIX='ielts-studio-'+encodeURIComponent(self.registration.scope)+'-';
const CACHE=PREFIX+${JSON.stringify(version)};
const URLS=${JSON.stringify(urls)};
self.addEventListener('install',event=>{event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(URLS)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith(PREFIX)&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',event=>{if(event.request.method!=='GET'||!event.request.url.startsWith(self.registration.scope))return;
event.respondWith((async()=>{const cache=await caches.open(CACHE);const cached=await cache.match(event.request,{ignoreSearch:true});
if(event.request.headers.has('Range')&&cached){const range=event.request.headers.get('Range');const match=/^bytes=(\\d+)-(\\d*)$/.exec(range);if(match){const bytes=await cached.arrayBuffer(),start=Number(match[1]),end=match[2]?Math.min(Number(match[2]),bytes.byteLength-1):bytes.byteLength-1;if(start> end)return new Response(null,{status:416,headers:{'Content-Range':'bytes */'+bytes.byteLength}});return new Response(bytes.slice(start,end+1),{status:206,headers:{'Content-Type':cached.headers.get('Content-Type')||'audio/wav','Content-Range':'bytes '+start+'-'+end+'/'+bytes.byteLength,'Accept-Ranges':'bytes','Content-Length':String(end-start+1)}});}}
if(event.request.url.endsWith('/content/manifest.json')){try{const r=await fetch(event.request,{cache:'no-store'});if(r.ok)await cache.put(event.request,r.clone());return r;}catch{return cached||new Response('Offline',{status:503});}}
if(event.request.mode==='navigate'){try{return await fetch(event.request);}catch{return cached||await cache.match('./index.html');}}
return cached||fetch(event.request);})());});
`);
console.log('Offline package:',urls.length,'files, version',version);
