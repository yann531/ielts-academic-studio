"""Apply authored, reviewable vocabulary batches without changing legacy IDs.
Run after the legacy generators. This script is deterministic and idempotent.
"""
import json,hashlib,re,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'src/data/vocab.json'; folder=ROOT/'content/vocabulary'
words=json.loads((folder/'legacy-base.json').read_text(encoding='utf-8'))
def rows(name):
 for n,line in enumerate((folder/name).read_text(encoding='utf-8').splitlines(),1):
  if line and not line.startswith('#'):yield n,line.split('|')
norm=lambda s:re.sub(r'\s+',' ',s.casefold().strip())
original=[w for w in words if not w['id'].startswith('academic-')]
before=ROOT/'reports/vocabulary-before.json'
if not before.exists():
 before.write_text(json.dumps({'total':len(original),'topics':dict(collections.Counter(w['topic'] for w in original)),'kinds':dict(collections.Counter(w['kind'] for w in original)),'duplicateTerms':[t for t,n in collections.Counter(norm(w['term']) for w in original).items() if n>1],'uniqueExamples':len(set(w['example'] for w in original)),'genericUsageNotes':sum('结合义项' in w['error'] or '先准确表达' in w['error'] for w in original)},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lookup={norm(w['term']):w for w in original}
quality={}
for name in ['quality-core.tsv','quality-social.tsv']:
 for line,r in rows(name):
  assert len(r)==5,(name,line,len(r));term,meaning,coll,translation,note=r
  assert norm(term) in lookup,term
  quality[norm(term)]=(meaning,coll,translation,note)
for line,r in rows('quality-extra.tsv'):
 assert len(r)==4,(line,len(r));term,coll,translation,note=r
 assert norm(term) in lookup,term
 quality[norm(term)]=(lookup[norm(term)]['meaning'],coll,translation,note)
assert len(quality)==526,len(quality)
for _,r in rows('meanings-extra.tsv'):
 term,meaning=r;q=quality[norm(term)];quality[norm(term)]=(meaning,*q[1:])
# Parent phrase cards share the original author's contextual example. Keep their IDs,
# but explain the full phrase and provide the same correctly aligned translation.
parents={(w['collocation'],w['example']):w for w in original if not w['id'].startswith('x-phrase-')}
for w in original:
 if w['id'].startswith('x-phrase-'):
  parent=parents.get((w['collocation'],w['example']))
  assert parent,(w['term'],w['example'])
  q=quality[norm(parent['term'])]
  quality[norm(w['term'])]=(q[1],q[1],q[2],q[3])
for w in original:
 meaning,coll,translation,note=quality[norm(w['term'])]
 w.update(meaning=meaning,error=note,collocations=[{'text':w['collocation'],'meaning':coll}],examples=[{'text':w['example'],'translation':translation}])
words=original
seen={norm(w['term']) for w in words};added=[];existing_additions=[]
for line,r in rows('additions.tsv'):
 assert len(r)==9,(line,len(r))
 topic,term,pos,meaning,coll,collzh,example,translation,note=r
 if norm(term) in seen:
  # Enrich the legacy card instead of creating a duplicate.
  w=lookup[norm(term)];existing_additions.append(term)
 else:
  w={'id':'academic-'+hashlib.sha256(norm(term).encode()).hexdigest()[:12],'term':term,'kind':'phrase' if ' ' in term else 'word'}
  words.append(w);seen.add(norm(term));added.append(term)
 w.update(topic=topic,pos=pos,meaning=meaning,collocation=coll,example=example,error=note,register='中性 / 学术及公共议题',collocations=[{'text':coll,'meaning':collzh}],examples=[{'text':example,'translation':translation}])
# Improve terse or misleading legacy examples with concrete academic contexts.
for _,r in [*rows('example-revisions.tsv'),*rows('examples-academic.tsv'),*rows('examples-core.tsv')]:
 assert len(r)==3,r
 term,example,translation=r;w=next(w for w in words if norm(w['term'])==norm(term));old=w['example']
 for card in words:
  if card['example']==old:card['example']=example;card['examples']=[{'text':example,'translation':translation}]
retired={'depend on','take part in','give back','give someone a hand','make time for','be keen on','get around','figure out','sort out','opposite','allow extra time','solvency','remuneration','succession planning','interoperability','amenities'}
meta={r[0]:r[1:] for _,r in rows('pronunciation-forms.tsv')}
phonetics=json.loads((folder/'phonetics-us.json').read_text(encoding='utf-8'))
phonetic_entries={**phonetics['entries'],**{r[0]:r[1] for _,r in rows('phonetics-supplement.tsv')}}
for w in words:
 w['contentVersion']='2026-11-17.1'
 w['source']='本站主题选编；中文释义、搭配释义与例句译文为独立整理；非雅思官方词表。'
 w['sources']=[{'title':'Cambridge 学习词典（供逐条查证，非逐页核验声明）','url':'https://dictionary.cambridge.org/search/english/direct/?q='+__import__('urllib.parse',fromlist=['quote']).quote(w['term']),'kind':'lookup'}]
 w['tags']=[w['topic'],'IELTS Academic','搭配' if w['kind']=='phrase' else '核心词义']
 if w['term'] in meta:
  ipa,forms,variants=meta[w['term']];
  if ipa:w['pronunciation']=ipa
  if forms:w['forms']=forms.split(';')
  if variants:w['spellingVariants']=variants.split(';')
 term=w['term'].lower()
 if term in phonetic_entries:w['pronunciationUS']=phonetic_entries[term]
 else:
  components=re.findall(r"[a-z]+(?:'[a-z]+)?",term)
  assert all(p in phonetic_entries for p in components),('Missing IPA',term,[p for p in components if p not in phonetic_entries])
  w['pronunciationParts']=[{'term':p,'ipa':phonetic_entries[p]} for p in components]
 w['sources'].append({'title':'美式音标：ipa-dict / CMUdict；短语为逐词读音，补充项另见项目说明','url':'https://github.com/open-dict-data/ipa-dict/blob/972cd67dd5f96bc5660e28070cde26e3928abcd7/data/en_US.txt','kind':'reference'})
 parent=parents.get((w['collocation'],w['example'])) if w['id'].startswith('x-phrase-') else None
 if w['term'] in retired or (parent and parent['term'] in retired):w.update(retired=True,retirementReason='难度或主题价值优先级较低，或与现有词形重复；保留旧 ID 和历史，不再派发。')
 # Specific quality statements only; no generated generic advice.
 assert '结合义项' not in w['error'] and w['collocations'][0]['meaning'] and w['examples'][0]['translation'],w['term']
assert len({norm(w['term']) for w in words})==len(words)
path.write_text(json.dumps(words,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
active=[w for w in words if not w.get('retired')]
report={'total':len(words),'active':len(active),'retainedLegacy':len(words)-len(active),'added':len(added),'enrichedInsteadOfDuplicated':existing_additions,'topics':dict(sorted(collections.Counter(w['topic'] for w in active).items())),'kinds':dict(collections.Counter(w['kind'] for w in active)),'translatedEntries':len(words),'withUKIPA':sum(bool(w.get('pronunciation')) for w in words),'withForms':sum(bool(w.get('forms')) for w in words),'duplicateTerms':[],'sourcePolicy':'Selection: IELTS lexical resource criteria, AWL, Academic Phrasebank. Individual dictionary URLs are lookup links, not claims of individual web verification. Definitions/examples/translations are independently authored and not certified by IELTS.'}
baseline=json.loads((folder/'legacy-base.json').read_text(encoding='utf-8'))
current={w['id']:w for w in words}
report.update(legacyIdsPreserved=all(w['id'] in current for w in baseline),rewrittenLegacyExamples=sum(w['example']!=current[w['id']]['example'] for w in baseline),distinctExamples=len(set(w['example'] for w in words)),genericUsageNotes=0,withIPA=sum(bool(w.get('pronunciation') or w.get('pronunciationUS') or w.get('pronunciationParts')) for w in words),withUSIPA=sum(bool(w.get('pronunciationUS')) for w in words),withComponentIPA=sum(bool(w.get('pronunciationParts')) for w in words))
(ROOT/'reports/vocabulary-after.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
