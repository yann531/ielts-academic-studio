import {describe,it,expect} from 'vitest';
import {freshState} from './engine';
import {localDate,weekStart,makeWeek,parsePlan} from './planner';
import {bundledContent,validateContent} from './content-updates';
import b1 from '../content-reserve/batch-001.json';
import b2 from '../content-reserve/batch-002.json';
import b3 from '../content-reserve/batch-003.json';
import b4 from '../content-reserve/batch-004.json';
import type {Paper} from './types';
import {validatePaper,grade} from './engine';
describe('weekly learning plan',()=>{
 it('ships four distinct valid reserve batches with markable answers',()=>{const bank=[...b1,...b2,...b3,...b4] as Paper[];expect(bank).toHaveLength(4);const ids=new Set();for(const p of bank){expect(validatePaper(p)).toBe(true);expect(ids.has(p.id)).toBe(false);ids.add(p.id);for(const q of p.passages.flatMap(x=>x.questions))for(const a of q.answers)expect(grade(q,a)).toBe(true);}});
 it('uses local Mondays across month boundaries',()=>{expect(localDate(weekStart(new Date(2026,10,1,23)))).toBe('2026-10-26');expect(localDate(weekStart(new Date(2026,10,2)))).toBe('2026-11-02');});
 it('builds seven days with real launch references and both production skills',()=>{const p=makeWeek(freshState(),bundledContent,new Date(2026,10,16));expect(p.days).toHaveLength(7);expect(p.days[6].date).toBe('2026-11-22');expect(p.days.every(d=>d.tasks[0].skill==='vocab')).toBe(true);for(const t of p.days.flatMap(d=>d.tasks)){if(t.part)expect(bundledContent.papers.find(p=>p.id===t.ref)?.passages.some(p=>p.id===t.part)).toBe(true);}expect(p.days.flatMap(d=>d.tasks).some(t=>t.skill==='writing')).toBe(true);expect(parsePlan(JSON.stringify(p))?.week).toBe(p.week);});
 it('prioritises weaker objective results and preserves daily new-word preference',()=>{const s=freshState();s.settings.dailyNew=8;s.attempts=[{id:'r',paperId:'r',at:0,skill:'reading',answers:{},correct:9,total:10,mistakes:[],mode:'practice'},{id:'l',paperId:'l',at:0,skill:'listening',answers:{},correct:2,total:10,mistakes:[],mode:'practice'}];const p=makeWeek(s,bundledContent,new Date(2026,10,16));expect(p.focus).toBe('listening');expect(p.dailyNew).toBe(8);});
 it('rejects a malformed public bank without changing bundled content',()=>{expect(validateContent(bundledContent)).toBe(true);expect(validateContent({...bundledContent,papers:[]})).toBe(false);expect(parsePlan('bad')).toBeNull();});
});
