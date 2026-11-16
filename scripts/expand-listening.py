import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1];P=ROOT/'src/data/papers.json'
papers=[p for p in json.loads(P.read_text(encoding='utf8')) if p['id']!='x-listening-3']
def t(prompt,answer,evidence,maxWords=2):return dict(type='text',prompt=prompt,answers=answer if isinstance(answer,list) else [answer],maxWords=maxWords,evidence=evidence,explanation='按录音最终确认的信息作答，结合证据核对拼写、单复数与字数。')
def s(prompt,answer,options,evidence,explanation):return dict(type='select',prompt=prompt,answers=[answer],options=options,evidence=evidence,explanation=explanation)
parts=[]
def add(title,script,questions,visual=None):
 p=dict(title=title,paragraphs=[dict(label='Transcript',text=script)],questions=questions,audioKind='Microsoft Zira 离线合成教学音频，非官方真人录音')
 if visual:p['visual']=visual
 parts.append(p)
add('Part 1 · A field course booking', '''This is an original teaching exercise, part one. A student books a weekend field course.
Coordinator: Hello, Northbank field centre. How may I help?
Student: I would like to join the weekend course. I first looked at birdwatching, but I have decided on coastal geology. The dates fit my schedule better.
Coordinator: Fine. May I have your surname?
Student: Mercer. M, E, R, C, E, R.
Coordinator: Thank you. The course begins on the eighteenth of September. The website previously showed the eleventh, but we changed it when the tutor became unavailable.
Student: Where should we meet? At the centre?
Coordinator: Not this time. Meet at the station entrance. Our minibus will collect the group there at eight forty-five. The course itself starts at nine thirty, so please use the collection time when planning your journey.
Student: Is accommodation included?
Coordinator: The basic fee includes transport during the course and the teaching materials, but not accommodation. We can give you a list of local places to stay. The field centre has no spare rooms that weekend.
Student: What should I bring?
Coordinator: A notebook is essential. We lend the measuring equipment, so there is no need to buy anything specialised. Bring waterproof clothing too. The route is mostly level, but the ground can be wet.
Student: How much is the deposit?
Coordinator: Twenty pounds. The balance is due a week before the course. If we cancel because of unsafe conditions, we refund the full payment. If you cancel, the conditions depend on how much notice you give; I will include those in the confirmation.
Student: I have a student card. Is there a reduced rate?
Coordinator: Yes, but we need a copy before issuing the final invoice. Please send it by email. Do not send your original card through the post.
Student: Will lunch be provided?
Coordinator: No, bring a packed lunch. There may be no shop near the field site. Drinking water is available at the centre before departure.
Student: That is clear. Please reserve a place.
Coordinator: I will send confirmation this afternoon.
This is the end of part one.''',[
t('Surname','Mercer','M, E, R, C, E, R',1),t('Start date',['18 September','September 18'],'eighteenth of September'),t('Meeting point','station entrance','Meet at the station entrance'),t('Collection time',['8:45','8.45','eight forty-five'],'collect ... eight forty-five'),t('Essential writing item','notebook','A notebook is essential',1),t('Deposit (£, number)',['20','twenty'],'Twenty pounds',1),
s('Which course has the student finally chosen?','Coastal geology',['Birdwatching','Coastal geology','Marine photography'],'decided on coastal geology','birdwatching 是最初考虑后放弃的课程。'),
s('What is excluded from the basic fee?','Accommodation',['Transport during the course','Teaching materials','Accommodation'],'but not accommodation','对比 includes 与 but not。'),
s('How should the student submit the card copy?','By email',['By post','At the field site','By email'],'Please send it by email','不要寄原件，排除邮寄。'),
s('What should participants do about lunch?','Bring it themselves',['Buy it at the field site','Bring it themselves','Collect a free meal'],'bring a packed lunch','可能没有商店，不能假设现场购买。')])
add('Part 2 · The learning garden', '''This is an original teaching exercise, part two. A guide describes a learning garden. Use the labelled grid displayed with the questions. North is at the top. Rows run from west to east.
Welcome to the learning garden. You enter through the central gate at the south edge of the site. Before we explore, look at the simple plan. The squares are labelled A to I. A, B and C form the north row. D, E and F form the middle row, and G, H and I form the south row. The gate is at H.
The greenhouse is at B, in the centre of the north row. Some older leaflets put it in the northeast corner, but that space, C, now contains the pond. Please use the current plan rather than those leaflets.
Our tool store is at G, immediately west of the entrance gate. The compost area is at D, directly north of the tool store. The outdoor classroom occupies F, east of the central beds. These five places are the locations you need to mark.
Now for the activities. The first demonstration begins at ten fifteen. We used to begin at ten, but the earlier bus no longer runs, so we moved the start time. You can walk around beforehand, provided you remain on the paths.
The workshop today is free, although places must be reserved because space is limited. Donations are welcome, but they are not a condition of taking part. At the end, visitors can take home a packet of seeds. Please choose one packet per household so that there is enough for everyone.
If you bring children, remember that an adult must stay with them. Our staff lead activities, but the garden is not a drop-off childcare service. Near the pond, please keep younger children within reach.
We also ask everyone to stay on the marked paths. This protects the planting beds and helps us keep clear routes for other visitors. The paths may be wet, so shoes with a good grip are useful. If weather makes the outdoor classroom unsuitable, we will move the activity into the greenhouse and announce the change at the gate.
This is the end of part two.''',[
*[s(f'Map: locate the {name}.',letter,list('ABCDEFGHI'),ev,ex) for name,letter,ev,ex in [('greenhouse','B','greenhouse is at B','北侧中央，对应 B，不要使用旧传单的东北角。'),('pond','C','space, C, now contains the pond','当前东北角为池塘。'),('tool store','G','tool store is at G','地图以北朝上，入口位于南侧中央；入口左侧即西侧，对应 G 格。'),('compost area','D','compost area is at D','工具房正北侧，位置 D。'),('outdoor classroom','F','classroom occupies F','中央种植区东侧为 F。')]],
t('First demonstration begins at',['10:15','10.15','ten fifteen'],'begins at ten fifteen'),
s('What is required to join the free workshop?','A reservation',['A compulsory donation','A reservation','A gardening qualification'],'places must be reserved','免费不代表不用预约，捐款非强制。'),
t('Visitors may take one packet of ____ per household.','seeds','packet of seeds',1),
s('What responsibility do adults accompanying children have?','They must remain with the children.',['They must remain with the children.','They must leave after registration.','They must lead every activity.'],'an adult must stay with them','工作人员带领活动不等于提供托管。'),
s('Why are visitors asked to stay on paths?','To protect beds and keep routes clear',['To finish the tour faster','To protect beds and keep routes clear','To avoid all contact with staff'],'protects ... beds ... clear routes','两个并列目的都在录音中。')],visual={'title':'Learning garden · North ↑（格位不按比例）','grid':[['A','B','C'],['D','E: central beds','F'],['G','H: entrance gate','I']]})
add('Part 3 · Choosing a research method', '''This is an original teaching exercise, part three. Two students discuss a small investigation with a supervisor.
Supervisor: You wanted to study how people use the library. What have you narrowed the question to?
Iris: We first thought about book borrowing, but the transaction data would be difficult to access. We now want to study how people choose study spaces.
Noah: We can observe which spaces are occupied at different times and then ask a few short questions about why people chose them.
Supervisor: Consider what each method can tell you. Observation can show where people sit, but not necessarily their reasons. Interviews can reveal reasons, but people may offer explanations that sound better than their actual decision process.
Iris: So we should compare the two rather than assume they will agree.
Supervisor: Yes. What is your sampling plan?
Noah: We will observe in the morning and the evening. We cannot cover the full day, so we will explain that limitation in the report. Initially we planned to study only during exam week, but that would be an unusual period. We will collect the main data during an ordinary teaching week instead.
Iris: Our pilot showed another problem. We both counted an occupied desk differently. I counted a bag as evidence that someone was using the space, but Noah counted only people who were physically present.
Supervisor: You need a shared definition. Record desks with unattended belongings separately from desks with a person present. Do not silently mix those categories.
Noah: We will revise the observation sheet before collecting more data.
Supervisor: Good. And how will you handle interviews?
Iris: Participation will be voluntary. We will not record names or student numbers. We will ask permission to quote an anonymous response in the report.
Supervisor: Keep the questions neutral. Instead of asking why the quiet room is obviously better, ask which features mattered in the choice. Also make clear that you are students doing an assignment, not library staff checking whether people belong there.
Noah: We will do that. Our deadline is Friday, but we can send the revised questions by Tuesday.
Supervisor: Please send them on Tuesday. That gives us time to review them before recruitment.
This is the end of part three.''',[
s('What is the final topic?','Choice of study space',['Book borrowing','Choice of study space','Library staff recruitment'],'how people choose study spaces','借书数据获取困难，研究已转为选座。'),
s('What limitation of observation is identified?','It may not reveal reasons.',['It cannot record location.','It may not reveal reasons.','It always requires names.'],'not necessarily their reasons','坐在哪里可以观察，为什么不能直接观察。'),
s('Why combine observation and interviews?','They provide different kinds of evidence.',['They guarantee agreement.','They remove the need for a sample.','They provide different kinds of evidence.'],'compare the two rather than assume they will agree','互补证据，不保证结果一致。'),
t('The main data will come from an ordinary ____ week.','teaching','ordinary teaching week',1),
s('What problem did the pilot reveal?','Different definitions of an occupied desk',['A lack of empty rooms','Different definitions of an occupied desk','Missing examination results'],'counted an occupied desk differently','两人操作性定义不同，会影响可比性。'),
t('Desks with unattended ____ will form a separate category.','belongings','unattended belongings separately',1),
t('Interview participation is ____.','voluntary','Participation will be voluntary',1),
s('Which detail will NOT be recorded?','Student numbers',['Features affecting a choice','Anonymous responses with permission','Student numbers'],'not record names or student numbers','不收身份标识，而不是不记录回答。'),
s('How should the questions be worded?','Neutrally',['To favour the quiet room','Neutrally','As an inspection by library staff'],'Keep the questions neutral','不能预设 quiet room obviously better。'),
t('Revised questions should be sent by ____.','Tuesday','send ... by Tuesday',1)])
add('Part 4 · The work of an urban archive', '''This is an original teaching exercise, part four. A lecturer discusses the organisation of a fictional city archive.
An archive is not simply a room full of old objects. It is a collection whose value depends heavily on context. A photograph without a date or location may still be interesting, but it can be harder to use as evidence. Archivists therefore preserve information about an item as well as the item itself.
One important concept is provenance: the record of where material came from and how it entered the collection. This helps later users evaluate what the material can support. It should not be confused with proof that every statement in the material is true. A well-documented personal diary can contain mistakes, memories or opinions.
Cataloguing makes material discoverable. A useful catalogue may include subject terms and an explanation of the original arrangement. However, modern labels can introduce assumptions that were absent from the original records. Staff should distinguish their description from language found in the source, especially where historical terms require explanation.
Digitisation can widen access, but it does not remove the need for conservation. The original may still contain physical evidence that an image fails to capture. Digital files also need maintenance: storage systems change, files can become damaged and formats may become difficult to open. Backup copies should be checked, not merely created and forgotten.
In our fictional example, volunteers helped transcribe handwritten letters. The project used shared examples to explain how to handle uncertain words. Volunteers marked uncertainty rather than silently guessing. A second reader checked the work before a transcription was released as verified. This method did not eliminate every error, but it made checking part of the process.
Access also involved ethical choices. Some collections contained personal information about people who might still be affected by publication. The archive reviewed restrictions and explained why certain items were not available online. Making everything searchable immediately would not automatically have been responsible access.
Finally, the archive kept a revision history for catalogue entries. When new evidence changed an interpretation, readers could see what had changed and why. The collection was not less valuable because its descriptions developed. Its credibility depended partly on preserving a clear route from the surviving material to the claims made about it.
This is the end of part four.''',[
t('An archive preserves an item and its ____.','context','value depends heavily on context',1),
t('The history of where material came from is its ____.','provenance','provenance: the record of where material came from',1),
s('What does good provenance NOT guarantee?','That every statement in a source is true',['That the origin can be investigated','That every statement in a source is true','That the route into the archive is documented'],'not ... proof ... every statement ... true','出处可靠不等于内容所有断言都真实。'),
t('A catalogue helps make material ____.','discoverable','Cataloguing makes material discoverable',1),
s('Why may the original still need conservation after digitisation?','It can contain evidence the image misses.',['Digital files never require maintenance.','It can contain evidence the image misses.','It has no connection with the digital image.'],'physical evidence that an image fails to capture','扫描不能替代全部物理信息。'),
t('Volunteers worked on handwritten ____.','letters','transcribe handwritten letters',1),
s('What were volunteers asked to do with uncertain words?','Mark uncertainty',['Guess silently','Remove the entire letter','Mark uncertainty'],'marked uncertainty rather than silently guessing','保留不确定性便于复核。'),
t('Before verification, the work was checked by a second ____.','reader','A second reader checked the work',1),
s('Why were some items restricted online?','Publication could affect people’s privacy.',['No item had been catalogued.','Publication could affect people’s privacy.','All volunteers objected.'],'personal information ... affected by publication','伦理限制与个人信息有关，不等于目录缺失。'),
t('Changes to catalogue descriptions were kept in a revision ____.','history','kept a revision history',1)])
for pi,p in enumerate(parts):
 p['id']=f'x-l3-p{pi+1}';p['audio']=f'audio/{p["id"]}.wav'
 for qi,q in enumerate(p['questions']):q['id']=f'x-l3-q{pi*10+qi+1}'
papers.append(dict(id='x-listening-3',skill='listening',title='野外课程、花园与档案',subtitle='4 Parts · 40 题 · 选择、地图与填空组合',minutes=30,source='本站 AI 辅助原创脚本与问题；离线合成音，非官方录音。',kind='原创练习',review='文本内证据和答案一致性检查，未考官校准；合成声线、时长非真实考试。',updated='2026-11-16',difficulty='加入修正信息、地图定位和方法论观点辨别；未标准化定级',passages=parts))
P.write_text(json.dumps(papers,ensure_ascii=False,indent=2),encoding='utf8')
(ROOT/'scripts/audio-extra.json').write_text(json.dumps([dict(id=p['id'],text=p['paragraphs'][0]['text']) for p in parts],ensure_ascii=False,indent=2),encoding='utf8')
print('Added listening: 4 parts, 40 questions')
