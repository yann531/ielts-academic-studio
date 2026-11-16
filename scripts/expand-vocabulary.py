import pathlib,json,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1];path=ROOT/'src/data/vocab.json'
base=[w for w in json.loads(path.read_text(encoding='utf8')) if not w['id'].startswith('x-')];words=list(base);seen={w['term'].lower() for w in words}
def add(w):
 if w['term'].lower() not in seen:words.append(w);seen.add(w['term'].lower())
for line in (ROOT/'scripts/vocabulary-extra.tsv').read_text(encoding='utf8').splitlines():
 if not line or line.startswith('#'):continue
 topic,term,pos,meaning,collocation,example=line.split('|')
 add(dict(id='x-word-'+hashlib.sha256(term.encode()).hexdigest()[:12],term=term,pos=pos,meaning=meaning,topic=topic,collocation=collocation,example=example,register='自然场景英语' if topic=='听说场景' else '中性 / 学术议题',error='注意具体义项、搭配和词形；先准确表达，再考虑句式变化。',kind='phrase' if ' ' in term else 'word',source='本站独立编写，AI 辅助；未逐条标准化 CEFR 定级，非官方必考词。'))
lookup={w['term']:w for w in base}
for line in (ROOT/'scripts/collocations-extra.tsv').read_text(encoding='utf8').splitlines():
 if not line or line.startswith('#'):continue
 parent,meaning=line.split('|');w=lookup[parent];term=w['collocation']
 # Do not make cards from placeholders which cannot be recalled naturally as a complete answer.
 if any(x in term for x in ['…','something','someone','clauses with','follow two figures']):continue
 add(dict(**{**w,'id':'x-phrase-'+hashlib.sha256(term.encode()).hexdigest()[:12],'term':term,'pos':'搭配 / 短语','meaning':meaning,'kind':'phrase','error':w['error']+' 练习时将名词、代词或时态替换为自己的情境。','source':'本站独立编写的搭配卡，与母词共享原创例句；搭配与单词分别计数。'}))
path.write_text(json.dumps(words,ensure_ascii=False,indent=2),encoding='utf8')
print('Vocabulary',len(words),'=',len(base),'base +',len(words)-len(base),'new; words',sum(w['kind']=='word' for w in words),'phrases',sum(w['kind']=='phrase' for w in words))
