import {describe,it,expect} from 'vitest';
import {readQuestions,makeQuestionPrompt,CHATGPT_URL,questionWindowFeatures} from './online-assistant';
import {freshState,parseBackup} from './engine';
describe('online ChatGPT handoff',()=>{
 it('keeps the official destination free of prompts, tokens and private context',()=>{expect(CHATGPT_URL).toBe('https://chatgpt.com/');expect(new URL(CHATGPT_URL).search).toBe('');const p=makeQuestionPrompt(' Why Not Given? ','Some original evidence.');expect(p).toContain('Why Not Given?');expect(p).toContain('Some original evidence.');expect(p).toContain('不要编造证据');});
 it('rejects malformed notes, preserves recent ones and survives full backup',()=>{expect(readQuestions('bad')).toEqual([]);expect(readQuestions('[null,{},1]')).toEqual([]);const notes=Array.from({length:65},(_,i)=>({id:String(i),at:i,page:'reading',question:'Question '+i,context:'original passage',answer:'my note'}));const s=freshState();s.notes['assistant-online-questions']=JSON.stringify(notes);const restored=parseBackup(JSON.stringify(s));expect(readQuestions(restored.notes['assistant-online-questions'])).toHaveLength(60);expect(readQuestions(restored.notes['assistant-online-questions'])[0].id).toBe('5');});
 it('uses an isolated popup and keeps its position inside the available desktop',()=>{const f=questionWindowFeatures(-100,0,1200,900);expect(f).toContain('noopener,noreferrer');expect(f).toContain('width=540');expect(f).toContain('left=560');expect(questionWindowFeatures(0,0,320,600)).toContain('left=0');});
});
