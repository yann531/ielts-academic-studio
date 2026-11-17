import type {AppState,Word,WordEdit} from './types';

// Keep personal meanings separate from the public bank. An empty entry is a
// timestamped reset, so restoring an old backup cannot resurrect a removed edit.
export function editMeaning(state:AppState,id:string,meaning:string|undefined,at=Date.now()) {
  const text=meaning?.trim();
  if(meaning!==undefined&&(!text||text.length>10000))throw Error('释义需为 1–10000 个字符');
  state.wordEdits??={};
  state.wordEdits[id]={...(text?{meaning:text}:{}),updated:at};
}

export function applyWordEdits(words:Word[],edits:AppState['wordEdits']):Word[] {
  return words.map(word=>edits?.[word.id]?.meaning!==undefined
    ? {...word,meaning:edits[word.id].meaning!}:word);
}

export function mergeWordEdits(a:AppState['wordEdits'],b:AppState['wordEdits']) {
  if(!a&&!b)return undefined;
  const result:Record<string,WordEdit>=structuredClone(a??{});
  for(const [id,edit] of Object.entries(b??{}))
    if(!result[id]||edit.updated>result[id].updated)result[id]=structuredClone(edit);
  return result;
}

export function validateWordEdits(value:unknown):value is Record<string,WordEdit> {
  if(!value||typeof value!=='object'||Array.isArray(value))return false;
  return Object.entries(value).every(([id,edit])=>{
    if(!id||id.length>=180||['__proto__','constructor','prototype'].includes(id)
      ||!edit||typeof edit!=='object'||Array.isArray(edit))return false;
    const e=edit as Record<string,unknown>;
    return typeof e.updated==='number'&&Number.isFinite(e.updated)
      &&(e.meaning===undefined||(typeof e.meaning==='string'&&!!e.meaning.trim()&&e.meaning.length<=10000));
  });
}
