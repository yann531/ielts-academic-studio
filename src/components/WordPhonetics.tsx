import type {Word} from '../types';

export const wordVoice=(word:Word)=>word.pronunciation?'en-GB':'en-US';

export function WordPhonetics({word}:{word:Word}) {
  if(word.pronunciation)return <p className="word-phonetics"><span>英</span> {word.pronunciation}</p>;
  if(word.pronunciationUS)return <p className="word-phonetics"><span>美</span> {word.pronunciationUS}</p>;
  if(word.pronunciationParts?.length)return <div className="word-phonetics word-phonetic-parts" aria-label="美式逐词音标">
    <span className="phonetic-label">美 · 逐词音标</span>
    {word.pronunciationParts.map((part,i)=><span className="phonetic-part" key={i}><small>{part.term}</small>{part.ipa}</span>)}
  </div>;
  return <p className="word-phonetics"><a href={'https://dictionary.cambridge.org/search/english/direct/?q='+encodeURIComponent(word.term)} target="_blank" rel="noreferrer">查看词典音标</a></p>;
}
