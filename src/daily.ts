import {planVocabulary,balancedWords,activeWord} from './vocab-state';
import type {AppState,Word} from './types';
import type {ContentBank} from './content-updates';
import {localDate,weekStart,makeWeek,parsePlan} from './planner';
export interface DailyItem {id:string;kind:'new'|'main'|'reflect';origin:string;title:string;skill:string;ref?:string;part?:string;wordId?:string;doneAt?:string}
export interface DailyCourse {version:1;anchor:string;through:string;items:DailyItem[];days:Record<string,string[]>;reviews:Record<string,{ids:string[];done:string[]}>}
export const COURSE_KEY='daily-course-v1';
export function datePlus(date:string,n:number){const d=new Date(date+'T12:00:00');d.setDate(d.getDate()+n);return localDate(d);}
export function readCourse(state:AppState):DailyCourse|null{try{const c=JSON.parse(state.notes[COURSE_KEY]??'null');return c?.version===1&&Array.isArray(c.items)&&c.days&&c.reviews?c:null;}catch{return null;}}
export function arrangeDaily(state:AppState,content:ContentBank,words:Word[],today=localDate(new Date())):DailyCourse{
 const old=readCourse(state),c:DailyCourse=old?structuredClone(old):{version:1,anchor:today,through:datePlus(today,-1),items:[],days:{},reviews:{}};
 const end=datePlus(today,13),limit=state.settings.dailyNew;
 // Materialise every missed calendar day too. No background timer is needed.
 for(let date=datePlus(c.through,1);date<=end;date=datePlus(date,1)){
  const monday=weekStart(new Date(date+'T12:00:00')),key='plan:'+localDate(monday),plan=parsePlan(state.notes[key])??makeWeek(state,content,monday),index=(new Date(date+'T12:00:00').getDay()+6)%7;
  for(const t of plan.days[index].tasks.filter(t=>t.id!=='vocab')){const id='daily-'+date+'-'+t.id;if(!c.items.some(x=>x.id===id))c.items.push({id,kind:t.id==='reflect'?'reflect':'main',origin:date,title:t.title,skill:t.skill,ref:t.ref,part:t.part,doneAt:state.completed.includes(`${key}:${index}:${t.id}`)?date:undefined});}
 }
 c.through=end>c.through?end:c.through;
 const vocab=state.vocabulary??planVocabulary(state,words,today),bank=new Map(words.map(w=>[w.id,w]));
 const ensureItem=(id:string)=>{const w=bank.get(id);if(!w)return;let item=c.items.find(t=>t.wordId===id);if(!item){item={id:'daily-word-'+id,kind:'new',origin:vocab.tasks[id]?.origin??today,title:w.term,skill:'vocab',wordId:id};c.items.push(item);}if(vocab.tasks[id])item.origin=vocab.tasks[id].origin;item.doneAt=vocab.tasks[id]?.doneAt??(vocab.progress[id]?.firstLearned?today:undefined);};
 for(const day of Object.values(vocab.days))for(const id of day.newIds)ensureItem(id);
 const projected=new Set(Object.values(vocab.days).filter(d=>d.date<=today).flatMap(d=>d.newIds));
 const pending=Object.entries(vocab.tasks).filter(([id,t])=>!t.doneAt&&!vocab.days[today]?.newIds.includes(id)&&activeWord(bank.get(id),vocab)).sort((a,b)=>a[1].origin.localeCompare(b[1].origin)).map(([id])=>bank.get(id)!);
 const futureWords=[...pending,...balancedWords(words.filter(w=>activeWord(w,vocab)&&!vocab.progress[w.id]?.firstLearned&&!vocab.tasks[w.id]&&!projected.has(w.id)),today+'-preview')];
 const assigned=new Set<string>();
 for(let date=today;date<=end;date=datePlus(date,1)){
  const finished=c.items.filter(t=>t.kind!=='new'&&t.doneAt===date),ids=finished.map(t=>t.id);
  for(const [kind,capacity] of [['main',1],['reflect',1]] as const){const slots=Math.max(0,capacity-finished.filter(t=>t.kind===kind).length);const pending=c.items.filter(t=>t.kind===kind&&!t.doneAt&&t.origin<=date&&!assigned.has(t.id)).sort((a,b)=>a.origin.localeCompare(b.origin));for(const t of pending.slice(0,slots)){ids.push(t.id);assigned.add(t.id);}}
  const wordIds=date===today?(vocab.days[date]?.newIds??[]):futureWords.splice(0,limit).map(w=>w.id);
  for(const id of wordIds)ensureItem(id);
  c.days[date]=[...wordIds.map(id=>'daily-word-'+id),...ids];
 }
 const review=vocab.days[today];c.reviews[today]={ids:review?.reviewIds??[],done:review?.reviewDone??[]};
 return c;
}
export function finishDaily(state:AppState,id:string,today=localDate(new Date())){const c=readCourse(state),t=c?.items.find(t=>t.id===id);if(c&&t&&!t.doneAt){t.doneAt=today;state.notes[COURSE_KEY]=JSON.stringify(c);}}
