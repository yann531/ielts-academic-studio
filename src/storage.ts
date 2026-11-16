import {freshState,parseBackup} from './engine';
import type {AppState} from './types';
const open=()=>new Promise<IDBDatabase>((resolve,reject)=>{const r=indexedDB.open('ielts-academic-studio',2);r.onupgradeneeded=()=>{for(const name of ['state','content'])if(!r.result.objectStoreNames.contains(name))r.result.createObjectStore(name);};r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error);r.onblocked=()=>reject(Error('请关闭旧版本学习页面后刷新，以完成存储升级。'));});
let database:Promise<IDBDatabase>|undefined;
const db=()=>database??=open();
export async function loadState():Promise<AppState>{const d=await db();return new Promise((resolve,reject)=>{const r=d.transaction('state').objectStore('state').get('main');r.onsuccess=()=>{try{resolve(r.result?parseBackup(JSON.stringify(r.result)):freshState());}catch(e){reject(e);}};r.onerror=()=>reject(r.error);});}
let queue=Promise.resolve();
export async function readContentCache():Promise<unknown>{const d=await db();return new Promise((resolve,reject)=>{const r=d.transaction('content').objectStore('content').get('bank');r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error);});}
export async function writeContentCache(value:unknown){const d=await db();return new Promise<void>((resolve,reject)=>{const tx=d.transaction('content','readwrite');tx.objectStore('content').put(value,'bank');tx.oncomplete=()=>resolve();tx.onerror=()=>reject(tx.error);});}
export function saveState(state:AppState){queue=queue.catch(()=>{}).then(async()=>{const d=await db();return new Promise<void>((resolve,reject)=>{const tx=d.transaction('state','readwrite');tx.objectStore('state').put(state,'main');tx.oncomplete=()=>resolve();tx.onerror=()=>reject(tx.error);tx.onabort=()=>reject(tx.error);});});return queue;}
export function download(name:string,data:Blob|string,type='application/json'){const blob=typeof data==='string'?new Blob([data],{type}):data;const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),3000);}
export function fileData(file:Blob):Promise<string>{return new Promise((resolve,reject)=>{const r=new FileReader();r.onload=()=>resolve(String(r.result));r.onerror=()=>reject(r.error);r.readAsDataURL(file);});}
