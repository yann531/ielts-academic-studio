import pathlib,json,hashlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
rows=[]
errors={
 'evidence':'通常为不可数名词：some evidence，不说 an evidence / evidences。',
 'feedback':'通常不可数：some feedback，不说 a feedback。',
 'equipment':'不可数：a piece of equipment，不说 equipments。',
 'tuition':'表示学费常见 tuition fees；tuition 也可指教学。',
 'percentage point':'从 20% 到 25% 为 5 个百分点；相对增幅为 25%。',
 'respectively':'顺序必须与前文两个或多个项目一一对应。',
 'whereas':'连接两个分句；不要仅用 whereas 加一个孤立名词。',
 'significant':'日常的“显著/重要”不自动等于 statistically significant。',
 'account for':'图表中表示“占”；不要写成 account of。',
 'rise':'动词 rise 不及物，raise 及物。',
 'correlation':'相关不自动证明因果，不能据此写 caused。',
 'data breach':'breach 是泄露/违规事件，避免与 break 混写。',
 'come in handy':'口语中自然，正式学术论述可改为 prove useful。',
 'give someone a hand':'口语表达；someone 可替换为真实人称，不能照抄占位词。'
}
for line in (ROOT/'scripts'/'vocabulary.tsv').read_text(encoding='utf-8').splitlines():
 if not line or line.startswith('#'):continue
 topic,term,pos,meaning,collocation,example=line.split('|')
 rows.append(dict(id='v-'+hashlib.sha256(term.encode()).hexdigest()[:12],term=term,pos=pos,meaning=meaning,topic=topic,collocation=collocation,example=example,register='自然口语 / 场景英语' if topic=='听说场景' else '中性 / 学术与公共议题',error=errors.get(term,'结合义项和搭配使用；不要只为显得高级替换原本准确的词。'),kind='phrase' if ' ' in term else 'word',source='本站独立选编与原创例句；主题难度面向 B1+–C1 常用表达，非官方雅思词表。'))
assert len(rows)==300,len(rows)
(ROOT/'src'/'data'/'vocab.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
print('Vocabulary entries:',len(rows))
