import {useState} from 'react';
import {Pencil,Check,X,RotateCcw} from 'lucide-react';
import {useApp} from '../context';
import {editMeaning} from '../word-edits';
import type {Word} from '../types';

export function WordMeaning({word}:{word:Word}) {
  const {state,content,update,notify}=useApp();
  const [editing,setEditing]=useState(false),[draft,setDraft]=useState('');
  const original=content.words.find(w=>w.id===word.id)??state.customWords.find(w=>w.id===word.id);
  const personal=state.wordEdits?.[word.id]?.meaning!==undefined;
  const save=()=>{
    if(!draft.trim()||draft.trim().length>10000)return;
    update(s=>editMeaning(s,word.id,draft.trim()===original?.meaning?undefined:draft));
    setEditing(false);notify('释义已保存；词库、复习和自测将使用此版本');
  };
  const reset=()=>{update(s=>editMeaning(s,word.id,undefined));setEditing(false);notify('已恢复默认释义');};
  return <div className="meaning-section">
    <div className="meaning-line">
      <p className="word-meaning"><span className="pos">{word.pos}</span>{word.meaning}</p>
      <button className="meaning-edit" aria-label={'编辑 '+word.term+' 的释义'} title="编辑释义" onClick={()=>{setDraft(word.meaning);setEditing(true);}}><Pencil size={13}/></button>
    </div>
    {editing&&<div className="meaning-editor">
      <label className="field-label">个人中文释义<textarea aria-label="个人中文释义" rows={4} value={draft} maxLength={10000} onChange={e=>setDraft(e.target.value)} onKeyDown={e=>{if(e.key==='Escape')setEditing(false);if(e.key==='Enter'&&(e.ctrlKey||e.metaKey)){e.preventDefault();save();}}}/></label>
      <p className="tiny muted">保存后用于本词的词库、每日学习、复习和自测，随完整备份保存。不会更改学习进度。</p>
      <div className="button-row"><button className="secondary" disabled={!draft.trim()} onClick={save}><Check size={14}/>保存</button><button className="text-button small" onClick={()=>setEditing(false)}><X size={13}/>取消</button>{personal&&<button className="text-button small meaning-reset" onClick={reset}><RotateCcw size={12}/>恢复默认</button>}</div>
    </div>}
    {personal&&!editing&&<details className="personal-meaning-note"><summary>个人释义 · 查看默认版本</summary><p>{original?.meaning??'原词条暂不可用，个人释义仍保留。'}</p><button className="text-button small" onClick={reset}>恢复默认释义</button></details>}
  </div>;
}
