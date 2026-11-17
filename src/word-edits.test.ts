import {describe,it,expect} from 'vitest';
import {freshState,parseBackup,mergeBackup,validateWord} from './engine';
import {words} from './data';
import {applyWordEdits,editMeaning} from './word-edits';
import {planVocabulary,markVocabulary} from './vocab-state';
import {renderToStaticMarkup} from 'react-dom/server';
import {createElement} from 'react';
import {WordPhonetics,wordVoice} from './components/WordPhonetics';

describe('personal dictionary meanings',()=>{
 it('falls back to the current bank, overrides by stable ID and does not mutate public data',()=>{
  const s=freshState(),word=words[0],original=word.meaning;
  expect(applyWordEdits([word],s.wordEdits)[0]).toBe(word);
  editMeaning(s,word.id,'课程体系；这是我校正后的释义',100);
  expect(applyWordEdits([word],s.wordEdits)[0].meaning).toBe('课程体系；这是我校正后的释义');
  expect(word.meaning).toBe(original);
  expect(applyWordEdits([{...word,meaning:'更新后的默认版本'}],s.wordEdits)[0].meaning).toBe('课程体系；这是我校正后的释义');
  editMeaning(s,word.id,undefined,200);
  expect(applyWordEdits([{...word,meaning:'更新后的默认版本'}],s.wordEdits)[0].meaning).toBe('更新后的默认版本');
 });
 it('keeps daily IDs, mastery flags, review dates and test records intact',()=>{
  const s=freshState();s.vocabulary=planVocabulary(s,words);const id=s.vocabulary.days[Object.keys(s.vocabulary.days)[0]].newIds[0];
  markVocabulary(s,id,'again',true);const before=JSON.stringify({v:s.vocabulary,c:s.cards,r:s.reviews});
  editMeaning(s,id,'经核对后的个人释义');
  const effective=applyWordEdits(words,s.wordEdits),next=planVocabulary(s,effective);
  expect(JSON.stringify({v:s.vocabulary,c:s.cards,r:s.reviews})).toBe(before);
  expect(next.days).toEqual(planVocabulary(s,words).days);
  expect(effective.find(w=>w.id===id)?.meaning).toBe('经核对后的个人释义');
 });
 it('round-trips edits and merges the latest edit or reset independently from learning records',()=>{
  const a=freshState(),id=words[0].id;editMeaning(a,id,'旧编辑',1);
  const b=parseBackup(JSON.stringify(a));expect(b.wordEdits?.[id].meaning).toBe('旧编辑');
  editMeaning(b,id,'新编辑',2);expect(mergeBackup(a,b).wordEdits?.[id].meaning).toBe('新编辑');
  editMeaning(b,id,undefined,3);const reset=mergeBackup(a,b);
  expect(reset.wordEdits?.[id]).toEqual({updated:3});
  expect(mergeBackup(reset,a).wordEdits?.[id]).toEqual({updated:3});
  expect(applyWordEdits([words[0]],reset.wordEdits)[0].meaning).toBe(words[0].meaning);
 });
 it('accepts old backups and rejects malformed overrides without changing the current state',()=>{
  const s=freshState();expect(parseBackup(JSON.stringify(s)).wordEdits).toBeUndefined();
  expect(()=>parseBackup(JSON.stringify({...s,wordEdits:{x:{meaning:4,updated:2}}}))).toThrow();
  expect(()=>parseBackup(JSON.stringify({...s,wordEdits:JSON.parse('{"__proto__":{"meaning":"x","updated":1}}')}))).toThrow();
  expect(()=>editMeaning(s,'x','  ')).toThrow();expect(s.wordEdits).toBeUndefined();
 });
});

describe('visible, honestly labelled phonetics',()=>{
 it('covers every bundled entry while preserving its ID and meaning',()=>{
  for(const w of words){expect(!!(w.pronunciation||w.pronunciationUS||w.pronunciationParts?.length),w.term).toBe(true);expect(validateWord(w)).toBe(true);}
  expect(words).toHaveLength(767);
 });
 it('labels British entries and chooses a matching speech voice',()=>{
  const w=words.find(w=>w.term==='curriculum')!;
  expect(renderToStaticMarkup(createElement(WordPhonetics,{word:w}))).toContain('英');
  expect(wordVoice(w)).toBe('en-GB');
 });
 it('labels component IPA instead of inventing connected phrase pronunciation',()=>{
  const w=words.find(w=>w.pronunciationParts?.length&&!w.pronunciation)!;
  const html=renderToStaticMarkup(createElement(WordPhonetics,{word:w}));
  expect(html).toContain('美式逐词音标');expect(wordVoice(w)).toBe('en-US');
  expect(w.pronunciationParts!.every(p=>p.term&&p.ipa.startsWith('/'))).toBe(true);
 });
});
