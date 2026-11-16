import {describe,it,expect} from 'vitest';
import {grade,wordCount,schedule,DAY,freshState,parseBackup,mergeBackup,parseCSV,escapeCSV,bandEstimate,validatePaper} from './engine';
import {papers,words,writing,speaking} from './data';
describe('answer marking',()=>{
 const q={id:'x',type:'text' as const,prompt:'x',answers:['garden studio'],maxWords:2,evidence:'x',explanation:'x'};
 it('normalises case, width and whitespace without changing the answer',()=>{expect(grade(q,' GARDEN　studio ')).toBe(true);expect(grade(q,'garden studios')).toBe(false);expect(grade(q,'studio garden')).toBe(false);expect(grade(q,'')).toBe(false);});
 it('accepts explicit alternatives only and respects word limits',()=>{expect(grade({...q,answers:['14 May','May 14']},'May 14')).toBe(true);expect(grade({...q,maxWords:1},'garden studio')).toBe(false);expect(grade({...q,answers:['75']},'£75')).toBe(false);});
 it('counts hyphenated words, contractions and numbers',()=>{expect(wordCount("A five-year plan isn't easy in 2026.")).toBe(7);});
 it('treats decimal numbers and times as one answer token',()=>{expect(wordCount('75.00')).toBe(1);expect(wordCount('6:30')).toBe(1);});
 it('does not extrapolate drills or uncalibrated sets to IELTS bands',()=>{expect(bandEstimate(9,10)).toBeNull();expect(bandEstimate(35,40)).toBeNull();});
});
describe('spaced repetition',()=>{
 it('reschedules forgotten cards after ten minutes',()=>{const c=schedule(undefined,'again',1000);expect(c.due).toBe(601000);expect(c.lapses).toBe(1);});
 it('first good and easy ratings wait one and four days',()=>{expect(schedule(undefined,'good',0).due).toBe(DAY);expect(schedule(undefined,'easy',0).due).toBe(4*DAY);});
 it('grows stable intervals, records repetitions and bounds ease',()=>{let c=schedule(undefined,'good',0);for(let i=0;i<20;i++)c=schedule(c,'good',i*DAY);expect(c.interval).toBeGreaterThan(10);expect(c.reps).toBe(21);for(let i=0;i<30;i++)c=schedule(c,'again',0);expect(c.ease).toBeGreaterThanOrEqual(1.3);expect(c.due).toBe(600000);});
});
describe('backup and import integrity',()=>{
 it('round-trips complete state, including essays, files and recordings',()=>{const s=freshState();s.drafts.a={id:'a',text:'My own essay',updated:4,history:[{at:3,text:'Old version'}]};s.recordings.push({id:'r',topic:'t',at:3,name:'recording',mime:'audio/webm',data:'data:audio/webm;base64,YQ=='});s.files.push({id:'f',at:3,name:'notes.txt',mime:'text/plain',data:'data:text/plain;base64,YQ=='});const restored=parseBackup(JSON.stringify(s));expect(restored.updated).toBeGreaterThanOrEqual(s.updated);expect({...restored,updated:s.updated}).toMatchObject(s);});
 it('rejects unknown versions, corrupt cards and prototype keys',()=>{expect(()=>parseBackup('{"version":2}')).toThrow();const s=freshState();expect(()=>parseBackup(JSON.stringify({...s,cards:{x:{due:'tomorrow'}}}))).toThrow();expect(()=>parseBackup(JSON.stringify(s).replace('"notes":{}','"notes":{"__proto__":{}}'))).toThrow();});
 it('merges by ID and chooses newer drafts and cards without losing current sessions',()=>{const a=freshState(),b=freshState();a.drafts.x={id:'x',text:'old',updated:1,history:[]};b.drafts.x={id:'x',text:'new',updated:2,history:[]};a.reviews.push({id:'r',wordId:'x',rating:'good',at:1});b.reviews=[...a.reviews];const s=mergeBackup(a,b);expect(s.drafts.x.text).toBe('new');expect(s.reviews).toHaveLength(1);});
 it('supports older version-one backups without customPapers',()=>{const s={...freshState()} as Record<string,unknown>;delete s.customPapers;expect(parseBackup(JSON.stringify(s)).customPapers).toEqual([]);});
 it('reads CSV with quoted commas, line breaks and literal quotes',()=>{const val='A comma, a "quote"\nand a new line';expect(parseCSV('term,meaning\r\nhello,'+escapeCSV(val))).toEqual([['term','meaning'],['hello',val]]);expect(()=>parseCSV('"unfinished')).toThrow();});
 it('rejects unsafe audio and invalid multiple-choice answers',()=>{const p=structuredClone(papers[0]);p.passages[0].audio='javascript:alert(1)';expect(validatePaper(p)).toBe(false);});
});
describe('content as a usable question bank',()=>{
 it('contains two 40-question sets for each objective skill',()=>{expect(papers.length).toBeGreaterThanOrEqual(7);for(const p of papers){expect(validatePaper(p)).toBe(true);expect(p.passages.flatMap(p=>p.questions).length).toBeGreaterThanOrEqual(6);for(const q of p.passages.flatMap(p=>p.questions))for(const a of q.answers)expect(grade(q,a),q.id+' '+a).toBe(true);}});
 it('has unique IDs and useful production content',()=>{expect(words.length).toBeGreaterThanOrEqual(763);expect(new Set(words.map(w=>w.term.toLowerCase())).size).toBe(words.length);expect(writing).toHaveLength(40);expect(speaking).toHaveLength(20);expect(writing.filter(t=>t.sample)).toHaveLength(5);for(const p of papers)for(const q of p.passages.flatMap(p=>p.questions)){expect(q.evidence.length).toBeGreaterThan(5);expect(q.explanation.length).toBeGreaterThan(8);}});
});
