import type {AppState,Paper,Word,WritingTask,SpeakingTopic} from './types';
export interface PlanTask {id:string;skill:string;title:string;detail:string;minutes:number;ref?:string;part?:string}
export interface WeeklyPlan {version:1;week:string;created:number;dailyNew:number;focus:string;days:{date:string;tasks:PlanTask[]}[]}
export const localDate=(d:Date)=>`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
export function weekStart(date=new Date()){const d=new Date(date);d.setHours(0,0,0,0);d.setDate(d.getDate()-(d.getDay()+6)%7);return d;}
export function makeWeek(state:AppState,content:{papers:Paper[];words:Word[];writing:WritingTask[];speaking:SpeakingTopic[]},start:Date):WeeklyPlan {
 const latest=state.attempts.slice(-12),ratios=(skill:string)=>{const a=latest.filter(a=>a.skill===skill);return a.length?a.reduce((n,a)=>n+a.correct/a.total,0)/a.length:0;};
 const focus=ratios('reading')<=ratios('listening')?'reading':'listening';const seed=Math.floor(Date.UTC(start.getFullYear(),start.getMonth(),start.getDate())/86400000/7);const rotation=[focus,focus==='reading'?'listening':'reading','writing','speaking',focus,'writing','speaking'];
 const days=rotation.map((skill,i)=>{const d=new Date(start);d.setDate(d.getDate()+i);const tasks:PlanTask[]=[{id:'vocab',skill:'vocab',title:'到期复习 + 新表达',detail:`先复习到期卡，再学最多 ${state.settings.dailyNew} 个新词/短语。用其中 2 个造句。`,minutes:12}];
 if(skill==='reading'||skill==='listening'){const bank=content.papers.filter(p=>p.skill===skill);if(bank.length){const p=bank[(seed+i)%bank.length],part=p.passages[(seed+i)%p.passages.length];tasks.push({id:'main',skill,title:part.title,detail:skill==='reading'?'完成单篇，交卷后逐题对照证据。':'完成一部分，先独立听，再核对改口、干扰项与拼写。',minutes:skill==='reading'?20:15,ref:p.id,part:part.id});}}
 else if(skill==='writing'){const bank=content.writing.filter(t=>t.task===(i===2?1:2));const t=bank[(seed+i)%bank.length];if(t)tasks.push({id:'main',skill,title:t.title,detail:`Task ${t.task}：先审题列提纲，再完成一稿；保留版本后重写最弱的一段。`,minutes:t.task===1?20:40,ref:t.id});}
 else{const t=content.speaking[(seed+i)%content.speaking.length];if(t)tasks.push({id:'main',skill,title:t.title,detail:'完成 Part 1–3，录音回放，选一题重说。',minutes:12,ref:t.id});}
 tasks.push({id:'reflect',skill:'review',title:i===6?'本周回顾与下周调整':'把错因带走',detail:i===6?'回看错题和复习量，确认下周强度；不要只追求完成数量。':'写下一个具体错因或表达问题，把相关词组加入词库。',minutes:5});return {date:localDate(d),tasks};});
 return {version:1,week:localDate(start),created:Date.now(),dailyNew:state.settings.dailyNew,focus,days};
}
export function parsePlan(value:string|undefined):WeeklyPlan|null{try{const p=JSON.parse(value??'null');return p?.version===1&&typeof p.week==='string'&&Array.isArray(p.days)&&p.days.length===7&&p.days.every((d:unknown)=>!!d&&typeof d==='object'&&'date' in d&&'tasks' in d&&Array.isArray(d.tasks))?p:null;}catch{return null;}}
