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
 const reserved=new Set(c.items.flatMap(t=>t.wordId?[t.wordId]:[]));
 for(const w of words)if(!reserved.has(w.id)&&(!state.cards[w.id]||(state.cards[w.id].status==='learning'&&state.cards[w.id].reps===0))){c.items.push({id:'daily-word-'+w.id,kind:'new',origin:today,title:w.term,skill:'vocab',wordId:w.id});reserved.add(w.id);}
 // Learning in the free word bank also counts; suspended/mastered cards are not forced back into lessons.
 for(const t of c.items)if(t.kind==='new'&&!t.doneAt&&t.wordId){const card=state.cards[t.wordId];if(card&&(card.reps>0||card.status!=='learning'))t.doneAt=today;}
 const assigned=new Set<string>();
 for(let date=today;date<=end;date=datePlus(date,1)){
  const finished=c.items.filter(t=>t.doneAt===date),ids=finished.map(t=>t.id);
  for(const [kind,capacity] of [['new',limit],['main',1],['reflect',1]] as const){const slots=Math.max(0,capacity-finished.filter(t=>t.kind===kind).length);const pending=c.items.filter(t=>t.kind===kind&&!t.doneAt&&t.origin<=date&&!assigned.has(t.id)).sort((a,b)=>a.origin.localeCompare(b.origin));for(const t of pending.slice(0,slots)){ids.push(t.id);assigned.add(t.id);}}
  c.days[date]=ids;
 }
 const review=c.reviews[today]??={ids:[],done:[]};
 review.done=[...new Set([...review.done,...state.reviews.filter(r=>localDate(new Date(r.at))===today).map(r=>r.wordId)])];
 const due=words.filter(w=>{const card=state.cards[w.id];return card?.status==='learning'&&card.reps>0&&card.due<=Date.now()&&!review.ids.includes(w.id)&&!review.done.includes(w.id);}).sort((a,b)=>state.cards[a.id].due-state.cards[b.id].due);
 review.ids.push(...due.slice(0,Math.max(0,30-review.ids.length)).map(w=>w.id));
 return c;
}
export function finishDaily(state:AppState,id:string,today=localDate(new Date())){const c=readCourse(state),t=c?.items.find(t=>t.id===id);if(c&&t&&!t.doneAt){t.doneAt=today;state.notes[COURSE_KEY]=JSON.stringify(c);}}
