"""Reproducible original learning content. No scraped books or exam papers."""
import json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'src'/'data'; OUT.mkdir(parents=True,exist_ok=True)
DATE='2026-11-13'
def write(name,data): (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
OFFICIAL='https://ielts.org/take-a-test/preparation-resources/sample-test-questions/academic-test'
resources=[]
def resource(title,publisher,skills,url,reason,cost='免费',account='无需账号',official=True,stage='熟悉考试 → 专项 → 模考',language='英文',format='教程 / 练习'):
 resources.append(dict(id='res-'+str(len(resources)+1),title=title,publisher=publisher,official=official,skills=skills.split(','),stage=stage,language=language,cost=cost,account=account,url=url,checked=DATE,reason=reason,format=format))
resource('Academic 官方样题与机考体验','IELTS.org','规则,听力,阅读,写作,口语',OFFICIAL,'先核对考试结构，再按题型体验。页面提供听力题目、答案、文本及写作与口语样题；外链材料不离线缓存。')
resource('官方 Academic 免费练习','British Council','听力,阅读,写作,口语','https://takeielts.britishcouncil.org/prepare/ielts-free-practice-mock-tests/academic','四科官方练习入口。用来校验本站原创练习与正式材料的差别；完成后按原站答案复盘。')
resource('IELTS Ready','British Council','听力,阅读,写作,口语','https://takeielts.britishcouncil.org/prepare/ielts-ready','官方备考平台。免费层、报名附赠与付费层权益不同，按所在地和当前账号页面确认。','免费 + 可选付费','部分内容需注册')
resource('官方书籍与课程总览','Cambridge English','规则,听力,阅读,写作,口语','https://www.cambridgeenglish.org/exams-and-tests/ielts/preparation/','汇集 Guide、Mindset、IELTS 21 Academic 及官方样卷。真题训练用原书配套音频；本站仅提供原始入口。','公开介绍免费，书籍付费','样题无需账号，数字包依产品')
resource('The Official Cambridge Guide to IELTS','Cambridge University Press & Assessment','听力,阅读,写作,口语','https://www.cambridge.es/en/catalogue/exams/courses/the-official-cambridge-guide-to-ielts','适合作为自学主线：先技能讲解，再做练习。书含 A/G 内容，只使用 Academic 阅读写作章节。','书籍付费','购买配套资源依版本',True,'系统入门 / 巩固','英文','书籍')
resource('IELTS 21 Academic / 真题系列','Cambridge University Press & Assessment','听力,阅读,写作,口语','https://www.cambridge.es/en/catalogue/exams/practice-material/practice-tests/ielts','剑桥官方出版练习卷，用作考前校准。2026 版为 IELTS 21；购买时确认 Academic 与配套数字包。','书籍付费','数字包依版本',True,'阶段检测 / 考前','英文','书籍 / 配套音频')
resource('Mindset for IELTS','Cambridge English','听力,阅读,写作,口语','https://www.cambridgeenglish.org/exams-and-tests/ielts/preparation/','分级课程适合补齐技能。按当前水平选择，避免同时堆叠多套主教材。','课程教材付费','依产品',True,'系统学习','英文','分级课程')
resource('雅思考试官方指南（第二版）','British Council / 中国雅思官网','听力,阅读,写作,口语','https://www.chinaielts.org/prepare/official-guide','中文母语自学的导学选择。查阅官方样章、音视频入口；与 Cambridge Guide 是不同书籍。','样章公开，整书付费','音视频按原站',True,'系统入门','中英双语','书籍 / 样章 / 音视频')
resource('IELTSx 系统课','The University of Queensland / UQ College','听力,阅读,写作,口语','https://uqcollege.uq.edu.au/study/english-studies/ieltsx','大学提供的四科视频和练习课程。UQ 页面介绍免费学习；edX 访问周期、证书及升级权益以课程页为准。','免费旁听 / 可选升级','edX 注册',True,'系统学习','英文','大学课程')
resource('IELTS Coach','British Council','听力,阅读,写作,口语','https://learnenglish.britishcouncil.org/ielts-preparation/ielts-coach','需要真人纠正和结构化课时再选择。与免费资源区分，本站功能无需购买课程。','付费','需账号',True,'需真人指导','英文','教师课程')
resource('IELTS Live Sessions','British Council','规则,听力,阅读,写作,口语','https://takeielts.britishcouncil.org/prepare/ielts-preparation-materials/live-sessions','官方公开讲座和社交平台直播入口，按当期日程观看，适合补充题型策略。','免费','按直播平台',True,'专项策略','英文','讲座')
resource('Academic 备考中心','IDP IELTS','规则,听力,阅读,写作,口语','https://ielts.idp.com/prepare/academic-and-ukvi','考试主办方的学术类资料入口；地区跳转、账号与免费内容以当地页面为准。','免费 + 可选产品','部分需账号')
resource('Listening 题型与官方练习','British Council','听力','https://takeielts.britishcouncil.org/prepare/ielts-free-practice-mock-tests/academic/listening','按填空、匹配、地图等题型训练；先听后核对文本，记录定位、干扰项、拼写三类错因。')
resource('B2 / C1 Audio Zone','British Council LearnEnglish','听力,词汇','https://learnenglish.britishcouncil.org/free-resources/general/audio-zone','不同口音的真实英语，带文本和理解练习。适合听辨与复述，不将其当作 IELTS 标准模考。')
resource('分级听力','British Council LearnEnglish','听力','https://learnenglish.britishcouncil.org/free-resources/listening','选择 B1/B2/C1 难度进行精听，听懂后口头总结；难度标签是课程级别。')
resource('Writing 官方备考与评分资料','IELTS.org','写作','https://ielts.org/take-a-test/preparation-resources/writing-test-resources','对照官方任务说明和评分标准。Task 1 不发表个人观点；Task 2 覆盖题目全部指令。')
resource('Writing Band Descriptors','IELTS.org','写作','https://ielts.org/cdn/ielts-guides/ielts-writing-band-descriptors.pdf','公开评分标准 PDF。区分任务完成、连贯、词汇、语法；用具体原文证据自评。','免费','无需账号',True,'所有阶段','英文','公开 PDF')
resource('Speaking Band Descriptors','IELTS.org','口语','https://ielts.org/cdn/ielts-guides/ielts-speaking-band-descriptors.pdf','公开评分标准 PDF。流利与连贯、词汇、语法、发音四项；仅有文字稿无法判断发音。','免费','无需账号',True,'所有阶段','英文','公开 PDF')
resource('评分标准下载与教学指引','British Council','规则,写作,口语','https://takeielts.britishcouncil.org/teach-ielts/test-information/assessment','核对评分量表，并学习各档表现差异。本站自评与模型建议均非正式考试成绩。')
resource('口语示例与考官讲评','IELTS.org','口语','https://ielts.org/organisations/ielts-for-organisations/understanding-ielts-scoring/resources-for-setting-your-ielts-scores','观看带考官说明的示例，比较同一标准下的表现，不以背诵范文代替表达训练。')
resource('Oxford 3000 / 5000','Oxford Learner’s Dictionaries','词汇','https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000','通用英语分级词表，用于查词和校准难度，不是雅思官方必考词。本库为独立编写的主题选词。','词表免费，部分功能付费','按功能',False,'B1+ / B2 / 常用 C1','英文','词典 / 词表')
resource('词义、用法与发音查询','Cambridge Dictionary','词汇,语法','https://dictionary.cambridge.org/','查清具体义项、可数性与搭配，再迁移到自己的句子。词典权威性不等于雅思主办方身份。','免费','无需账号',False,'所有阶段','英文 / 中英','词典')
resource('分级语法练习','British Council LearnEnglish','语法,写作,口语','https://learnenglish.britishcouncil.org/grammar','围绕真实错误补课：冠词、主谓一致、从句和时态。每次只选一个问题，随后用到作文和口语。')
resource('IELTS Liz 免费课程','IELTS Liz','听力,阅读,写作,口语','https://ieltsliz.com/','非官方教师补充资料，适合查题型技巧；考试规则与评分仍核对官方来源。','大量免费 + 付费课程','免费页无需账号',False,'专项巩固')
resource('IELTS Advantage 免费课程','IELTS Advantage','听力,阅读,写作,口语','https://www.ieltsadvantage.com/ielts-courses-and-resources/','非官方教学机构，先使用免费基础课和写作讲解。商业课程不构成本站必要依赖。','免费 + 付费课程','部分需注册',False,'专项巩固')
resource('机考 Familiarisation','British Council','规则,听力,阅读,写作','https://takeielts.britishcouncil.org/prepare/ielts-free-practice-mock-tests/ielts-familiarisation-test','考前熟悉机考界面。听读结果与写作口语反馈的提供方式不同，以页面说明为准。')
write('resources.json',resources)

def tq(prompt,answer,evidence,explanation='',maxWords=2,**kw):return dict(type='text',prompt=prompt,answers=answer if isinstance(answer,list) else [answer],maxWords=maxWords,evidence=evidence,explanation=explanation or '答案由所列原文直接支持；先定位证据，再检查题目限制。',**kw)
def sq(prompt,answer,options,evidence,explanation,**kw):
 if answer not in options:
  matches=[x for x in options if x.startswith(answer+':')]
  if len(matches)!=1:raise ValueError((prompt,answer))
  answer=matches[0]
 if len(explanation)<=8:explanation+=' 作答依据应来自该段信息。'
 return dict(type='select',prompt=prompt,answers=[answer],options=options,evidence=evidence,explanation=explanation,**kw)
def tf(prompt,answer,evidence,explanation):return sq(prompt,answer,['TRUE','FALSE','NOT GIVEN'],evidence,explanation,trap='False：原文明确相反；Not Given：原文不足以确认或否定。')
def yn(prompt,answer,evidence,explanation):return sq(prompt,answer,['YES','NO','NOT GIVEN'],evidence,explanation,trap='这里判断作者观点；未表达该观点不等于反对。')
readings=[]
def passage(title,text,questions):
 paragraphs=[dict(label=chr(65+i),text=t.strip()) for i,t in enumerate(text.strip().split('\n\n'))]
 return dict(title=title,paragraphs=paragraphs,questions=questions)
readings.append(passage('Cooling the city, one street at a time', '''Urban heat is often discussed as if it were a single temperature covering an entire city. Yet a person waiting beside a broad road may experience very different conditions from someone sitting in a nearby shaded courtyard. Sunlight warms roofs and paving; these surfaces then release stored energy after sunset. The term urban heat island describes the contrast between built areas and their rural surroundings, but that average can conceal important differences within the city. For people planning short walking routes, street-level conditions may matter more than the city-wide figure.

In a small, fictional pilot in the city of Merrow, planners compared twelve streets rather than choosing one showcase neighbourhood. Sensors were mounted at pedestrian height, and a mobile team repeated measurements at the same time on comparable summer days. The investigators recorded air temperature as well as the temperature of nearby surfaces. They also asked walkers where they felt comfortable. These measures did not always agree: an exposed pavement could feel unpleasant even when a nearby air sensor registered only a modest change. The pilot was designed to guide local decisions, not establish a universal cooling figure.

Trees were useful, but counting them was a poor substitute for mapping their shade. A young tree and a mature tree each counted as one item in the inventory, despite offering very different protection. The time of day mattered too. A canopy that sheltered a morning queue might leave an afternoon bus stop exposed. Merrow therefore mapped shade at hourly intervals. The resulting maps helped planners identify gaps along routes to schools and clinics, where even a short stretch without shelter could discourage walking.

Another proposal involved reflective paving, which sends a greater proportion of incoming sunlight away from the ground. This can reduce surface temperature. However, a cooler surface does not necessarily mean a more comfortable pedestrian: reflected radiation can reach the body or nearby windows. The team recommended testing a small area and gathering feedback before committing an entire street to the material. They rejected the idea of ranking every cooling measure by a single number, because its effects depended on where it was installed and who used the space.

Maintenance placed limits on the planting scheme. Some locations lacked enough soil for roots, and new trees needed watering during establishment. A grant could pay for planting while leaving no dependable budget for later care. The council therefore required a five-year maintenance plan before approving each group of trees. In the pilot, residents reported comfort and access problems, but they were not responsible for technical inspections. Their observations complemented professional checks rather than replacing them.

The final proposal combined shaded routes, selective planting and modest trials of new paving. It prioritised access to essential services over producing an impressive total number of trees. A public dashboard displayed observations and the uncertainty around them. The authors argued that a useful heat strategy should be assessed by the journeys it makes possible, as well as by environmental measurements. They did not claim that the pilot would remove the need for wider efforts to reduce emissions.''',[
tf('All parts of a city experience the same temperature.','FALSE','A: very different conditions','原文明确比较道路和庭院的不同，与 all / same 相反。'),
tf('Measurements in Merrow were taken at pedestrian height.','TRUE','B: Sensors were mounted at pedestrian height','题干与原文一致。'),
tf('The sensors used in Merrow were cheaper than those in other cities.','NOT GIVEN','B: 描述了安装方式，没有传感器价格','没有价格比较，不能推断贵或便宜。'),
tq('Complete: Pavements release stored energy after ____.','sunset','A: release stored energy after sunset',maxWords=1,paraphrase='stored energy = accumulated heat'),
tq('Complete: Planners mapped tree ____ rather than relying on tree counts.','shade','C: counting them was a poor substitute for mapping their shade',maxWords=1),
tq('Complete: New trees needed ____ during establishment.','watering','E: new trees needed watering during establishment',maxWords=1),
sq('Choose the best heading for paragraph C.','Timing and location of shade',['The cost of sensors','Timing and location of shade','A ban on street trees','Rural climate trends'],'C: time of day mattered too','整段讨论遮阴在不同位置和时间的效果，而不是单纯树木数量。'),
sq('Which paragraph explains why surface cooling may fail to improve comfort?','D',list('ABCDEF'),'D: reflected radiation can reach the body','反射路面的副作用在 D，不要只看到 B 的温度词。'),
sq('Which paragraph discusses responsibility for future care?','E',list('ABCDEF'),'E: a five-year maintenance plan','maintenance 与 future care 同义。'),
sq('What was the purpose of the Merrow pilot?','B',['A: prove one global cooling figure','B: inform local planning','C: replace all air sensors','D: close roads permanently'],'B: designed to guide local decisions','not establish a universal figure 排除 A。'),
sq('Why did investigators also ask walkers about comfort?','C',['A: to calculate planting costs','B: to measure rural temperatures','C: to complement instrument readings','D: to choose sensor brands'],'B: These measures did not always agree','体感与仪器读数不同，须综合考虑。'),
tq('Complete: Each group of trees needed a ____ maintenance plan.',['five-year','five year'],'E: required a five-year maintenance plan',maxWords=2),
yn('The author believes counting trees alone is enough to evaluate a heat strategy.','NO','F: assessed by the journeys it makes possible, as well as by environmental measurements','作者明确提出多维评估，反对单一总量。')]))
readings.append(passage('What a seed bank can and cannot save', '''A seed bank is often described as a library for future agriculture. The comparison is helpful because both depend on careful cataloguing and continued access, but seeds are living material rather than stable pages. Collections must be checked and, when necessary, regenerated by growing plants and harvesting a fresh generation. Keeping seeds cold and dry can slow deterioration; it cannot make every sample immortal. A package in a freezer is therefore the beginning of a conservation process, not its completion.

Many crop species produce orthodox seeds, which tolerate drying and low temperatures. Other species produce seeds that are damaged by those conditions. Such collections may require living plants or techniques that preserve small pieces of plant tissue. The choice is biological rather than merely financial: buying a larger freezer will not make unsuitable seeds tolerate conventional storage. A conservation programme may consequently use several methods for different species, rather than selecting one technology for everything.

Documentation is another essential resource. If a sample lacks reliable information about where it was collected, researchers may struggle to decide how to use it. A hillside population and a lowland population of the same species can carry different traits. Labels also need to survive staff changes and software replacement. In a fictional regional collection at Alder Farm, curators kept both digital records and printed summaries. The printed copies were a precaution against temporary access problems, not a claim that paper records could replace the full database.

Access involves people as well as storage. Farmers who maintain diverse crops in their fields continually select plants for local conditions and preferences. Their knowledge can help curators interpret a collection, while the bank may supply material after a local loss. However, the two approaches are not interchangeable. A stored collection captures particular samples; a farming population continues to change. Agreements about sharing material and recognising contributors are therefore part of conservation, rather than administrative details to be considered only at the end.

Before releasing a small sample to a researcher, a bank may check whether enough viable seeds remain. Germination tests use a portion of the collection, so staff must balance information gained against material consumed. If viability falls, regeneration may be necessary. But growing a new generation carelessly can itself change the collection: only plants that flower under the chosen conditions will contribute seeds. Curators therefore document the conditions and try to preserve the range represented by the original sample.

Seed banks offer valuable insurance against loss, but insurance is not a substitute for maintaining habitats and farming knowledge. A diverse collection can expand future options without predicting exactly which trait a future crop will need. The strongest argument for this work is not that every stored sample will be used. It is that a range of possibilities should remain available. Assessing success solely by the number of packets stored risks rewarding accumulation while neglecting viability, documentation and fair access.''',[
tf('Cold storage guarantees that every seed sample will survive forever.','FALSE','A: it cannot make every sample immortal','guarantees 与 cannot 相反。'),
tf('All species can use the same storage technology.','FALSE','B: several methods for different species','生物差异决定不同方法。'),
tf('Alder Farm is the largest seed collection in its region.','NOT GIVEN','C: a fictional regional collection','没有规模排名信息。'),
tq('Seeds that tolerate conventional drying are described as ____.','orthodox','B: orthodox seeds, which tolerate drying',maxWords=1),
tq('Alder Farm kept printed ____ alongside its digital records.','summaries','C: digital records and printed summaries',maxWords=1),
tq('Tests of ____ consume some of the stored collection.','germination','E: Germination tests use a portion of the collection',maxWords=1),
sq('Which paragraph addresses recognition of people who provide material?','D',list('ABCDEF'),'D: recognising contributors','contributor 指贡献者，与 farmers 关系对应。'),
sq('Which paragraph describes a risk caused by renewing a collection?','E',list('ABCDEF'),'E: growing a new generation carelessly can itself change the collection','regeneration 并非无风险。'),
sq('Best heading for paragraph B?','Biological limits on storage',['The history of farm libraries','Biological limits on storage','Replacing curators with software','The value of more packets'],'B: choice is biological rather than merely financial','主旨是不同种子的储存适应性。'),
sq('What distinguishes crops in farmers’ fields from stored samples?','C',['A: field crops never face loss','B: stored samples change faster','C: field populations continue to change','D: farmers require no documentation'],'D: a farming population continues to change','抓住 continues to change 的对比。'),
yn('The author sees packet numbers as a sufficient measure of success.','NO','F: risks rewarding accumulation while neglecting viability','作者反对仅数包数。'),
yn('The author expects every conserved sample to have a specific future use.','NO','F: not that every stored sample will be used','作者明确否定 every，而不是仅缺少信息。'),
tq('Summary: A collection needs viability, documentation and fair ____.','access','F: viability, documentation and fair access',maxWords=1)]))
readings.append(passage('The hidden work of making research repeatable', '''A surprising result attracts attention, but the work needed to check it is often less visible. Repeating a study can reveal whether a finding depends on a particular sample, an analytical decision or an unnoticed feature of the original setting. It does not follow that a result which fails to repeat was fraudulent. Small samples, random variation and differences in measurement can all matter. Treating every unsuccessful repetition as proof of dishonesty discourages the careful comparisons that research needs.

For clarity, some researchers distinguish reproducing an analysis from replicating a study. Reproduction in this sense means using the same data and code to see whether the published result can be obtained. Replication collects new data to test a related question. Terminology varies across disciplines, so a report should state what was actually done instead of relying only on a label. A reader needs to know whether new participants were recruited, whether the original materials were used and which choices were changed.

Sharing a spreadsheet is not always sufficient. Variables may have unclear names, missing values may be coded in unusual ways, or a processing step may exist only in a former researcher’s memory. A data dictionary explains what each variable represents and how it was measured. Versioned code records changes to analysis, while a record of software dependencies helps another team reconstruct the environment. These practices require time, especially when a project was not organised for sharing from the beginning.

In a fictional study of library reminders, two teams tested whether a message increased the return of overdue books. Team North sent messages in the morning; Team South sent them in the evening. Their results differed. Rather than immediately attributing the gap to time of day, the teams compared who received the messages, how overdue was defined and whether the notices were successfully delivered. Only a controlled comparison could separate these possible explanations. A plausible story about a difference was not itself a test of that story.

Preregistration can help by recording a question and an analysis plan before the results are examined. It makes it easier to distinguish planned tests from exploratory ones. Exploration remains valuable: an unexpected pattern may suggest a better question. The problem arises when an exploratory finding is presented as though it had been predicted all along. Preregistration also cannot guarantee that a measurement is meaningful or that a sample represents the population. Transparency is useful without being a complete quality certificate.

Incentives shape whether these practices become routine. If institutions reward only novel positive findings, researchers have little time for careful verification. Journals, funders and employers can recognise well-designed replications, shared methods and the maintenance of reusable datasets. The author’s proposal is not to replace discovery with checking, but to treat both as necessary parts of cumulative knowledge. A field becomes more trustworthy when uncertainty can be examined openly rather than hidden behind a tidy final narrative.''',[
yn('The author regards every failed replication as evidence of fraud.','NO','A: It does not follow ... fraudulent','明确反对将不重复等同造假。'),
yn('Researchers should explain their methods rather than trust terminology alone.','YES','B: state what was actually done','作者主张具体描述。'),
yn('The author believes Team North had more participants than Team South.','NOT GIVEN','D: 两队时间不同，没有人数','未讨论样本量比较，不可推断。'),
tq('Using the same data and code is called ____ in the distinction described.','reproduction','B: Reproduction ... using the same data and code',maxWords=1),
tq('A ____ explains the meaning and measurement of variables.','data dictionary','C: A data dictionary explains what each variable represents',maxWords=2),
tq('Team South sent notices in the ____.','evening','D: Team South sent them in the evening',maxWords=1),
sq('Which paragraph discusses institutional rewards?','F',list('ABCDEF'),'F: Journals, funders and employers can recognise','机构激励在 F。'),
sq('Which paragraph lists practical obstacles to reuse?','C',list('ABCDEF'),'C: unclear names ... unusual ways ... memory','列出复用数据面临的障碍。'),
sq('Choose the best heading for paragraph E.','A useful tool with limits',['A useful tool with limits','Why exploration must end','A guaranteed quality stamp','Changing library opening times'],'E: useful without being a complete quality certificate','整段既述好处也说明限制。'),
sq('What would establish whether message timing caused the difference?','B',['A: a convincing story','B: a controlled comparison','C: a positive headline','D: a larger spreadsheet file'],'D: Only a controlled comparison','故事合理不等于因果证据。'),
tf('Preregistration makes exploratory research worthless.','FALSE','E: Exploration remains valuable','明确承认探索有价值。'),
tf('Every discipline uses the same definitions of replication.','FALSE','B: Terminology varies across disciplines','varies 反对 same。'),
tq('Summary: The author supports both discovery and ____.','checking','F: not to replace discovery with checking ... both',maxWords=1),
sq('What is the main purpose of the passage?','C',['A: accuse one library of misconduct','B: prohibit new scientific questions','C: explain practices that make checking research possible','D: compare software prices'],'A–F: 反复强调验证方法、限制和激励','文章范围涵盖研究可验证性，而非个别实验结论。')]))
readings.append(passage('Libraries beyond the book count', '''A public library can lend fewer printed books while becoming more useful to its community. This possibility complicates the familiar practice of measuring performance mainly through circulation figures. Some visitors come for quiet study, others for internet access, language groups or help with unfamiliar forms. These activities do not make books irrelevant. They show that one transaction count cannot represent the full range of services that a shared public space provides.

In the fictional town of Westhaven, librarians began their review by observing how different rooms were used. They recorded occupancy at several points during the day rather than only at closing time. The large reading room was busiest after school, while small meeting rooms were more popular in the mornings. A survey then asked visitors what had brought them in. Staff avoided collecting names because the purpose was service planning, not tracking individual readers. Even so, they recognised that the survey would miss people who never entered the building.

Non-users offered a different perspective. Some could not visit during opening hours; others found the entrance difficult to navigate or assumed that all services required a paid membership. The library tested a later opening on one evening each week and improved signs near the entrance. It also explained which services were free. These changes addressed identified barriers, but staff did not assume that a single trial would resolve every reason for staying away. They planned to review participation before making the extended hours permanent.

Digital services introduced a further complication. An online renewal saved a trip, but the number of renewals said little about whether a reader could find useful information. Meanwhile, staff spent time helping visitors judge the reliability of websites. This work was hard to reduce to a simple count. The review combined short visitor accounts with service statistics, while removing details that could identify individuals. A personal story could illustrate an issue without being treated as proof that every visitor had the same experience.

Changes to space required negotiation. Quiet study and lively group activities could conflict when placed too close together. Instead of declaring one type of use more valuable, staff created quieter zones and scheduled some group sessions outside peak study hours. Flexible furniture helped, but moving tables alone could not solve poor sound separation. The building’s physical limits meant that not every activity could be accommodated at the same time. Clear information about where and when to find each service became part of the solution.

Westhaven’s report retained book loans as one indicator while adding measures of access, participation and user experience. It warned against equating a busy room with a successful service: overcrowding may signal inadequate provision. Equally, a small specialist session may offer substantial value to a few people. The report argued for interpreting numbers in context and revisiting them as needs changed. Its goal was a library that could explain why its choices helped the public, rather than simply report the largest possible totals.''',[
tf('The passage argues that printed books have become irrelevant.','FALSE','A: These activities do not make books irrelevant','原文明示否定。'),
tf('Westhaven recorded occupancy only at closing time.','FALSE','B: at several points during the day','only 与 multiple times 相反。'),
tf('Most Westhaven residents supported the extended opening trial.','NOT GIVEN','C: 介绍试点，没有居民支持比例','没有 most 或调查支持率。'),
tq('The reading room was most crowded after ____.','school','B: busiest after school',maxWords=1),
tq('To protect visitors, the survey did not collect ____.','names','B: avoided collecting names',maxWords=1),
tq('The library improved ____ near the entrance.','signs','C: improved signs near the entrance',maxWords=1),
sq('Which paragraph discusses the limits of moving furniture?','E',list('ABCDEF'),'E: moving tables alone could not solve poor sound separation','家具可灵活，隔音仍有限。'),
sq('Which paragraph discusses help with assessing online information?','D',list('ABCDEF'),'D: judge the reliability of websites','assessing 与 judge 同义。'),
sq('Best heading for paragraph C?','Responding to barriers to access',['Responding to barriers to access','Ending all membership','The price of new books','A new digital survey platform'],'C: opening hours, entrance, membership assumption','共同主旨是降低使用障碍。'),
sq('Why did the library consult non-users?','B',['A: to sell paid memberships','B: to identify barriers missed by an in-building survey','C: to cancel all group activities','D: to increase closing-time statistics'],'B–C: survey would miss people who never entered','调查盲点使非使用者意见有价值。'),
yn('The author thinks every crowded room indicates success.','NO','F: overcrowding may signal inadequate provision','拥挤也可能表示资源不足。'),
tq('The report combined statistics with short visitor ____.','accounts','D: combined short visitor accounts with service statistics',maxWords=1),
tq('Summary: Performance numbers should be interpreted in ____.','context','F: interpreting numbers in context',maxWords=1)]))
readings.append(passage('Repairing a product, preserving a choice', '''Repair is sometimes presented as a simple matter of persuading owners to keep products longer. Motivation matters, but a willing owner may still face practical barriers. A replacement part might be unavailable, a case difficult to open, or instructions limited to authorised workshops. Whether a product remains in use therefore depends on a system of design, information, skills and incentives. Asking only whether consumers care about waste overlooks many of the choices made before a device reaches them.

A repairability score tries to make some of these barriers visible before purchase. Depending on its design, it might consider access to parts, the tools needed for disassembly and the availability of instructions. Yet a single score compresses several different issues. One buyer may need a battery replacement, while another is concerned about a broken screen. A transparent scoring system should therefore show its components rather than hide them behind a large number on a label. Consumers can then judge which features matter for the way they use the product.

Independent workshops provide expertise that many owners lack. In the fictional district of Elmbrook, a community repair event paired volunteers with residents, but it excluded work on mains electrical components. Organisers described the event as a place to learn basic diagnosis and safe maintenance, not a replacement for qualified specialists. Participants were encouraged to explain the fault before anyone opened a case. Sometimes the apparent failure was a setting or a damaged cable rather than the main device, so careful diagnosis could avoid unnecessary intervention.

Parts supply remained a difficulty even for skilled repairers. A cheap component might be sold only as part of a much larger assembly. This could make replacement expensive and waste functioning material. Standard fasteners and modular parts could reduce such problems, although modular design also involves trade-offs in size, weight and manufacturing. The passage does not assume that every modular product will last longer; durable construction and continuing support still matter. Design choices should be assessed against actual repair needs rather than promoted as universal solutions.

Software can determine a product’s useful life as strongly as hardware. A device that still works physically may lose important functions when updates or associated services stop. Clear information about the support period helps buyers make a decision before purchase. It does not guarantee that every future threat can be solved, but it makes an important dependency visible. A repair policy that considers only screws and spare parts may therefore overlook a major cause of premature replacement.

Repair is not automatically the best environmental option in every case. An old appliance may use much more energy than a suitable replacement, and the balance depends on how often it is used, how it is powered and what producing a new model requires. Claims should compare the whole situation rather than assume that either repair or replacement always wins. For many everyday products, however, removing unnecessary barriers gives owners a choice they currently lack. The aim is to enable an informed decision, not impose a single answer on every household.''',[
yn('The author believes consumer motivation is the only barrier to repair.','NO','A: a willing owner may still face practical barriers','作者承认动机但强调系统障碍。'),
yn('Repair scores should reveal the criteria behind them.','YES','B: should ... show its components','明确赞成透明组成。'),
yn('The author says Elmbrook volunteers were all retired engineers.','NOT GIVEN','C: volunteers，无职业背景','不能因能维修就推断职业。'),
tq('The event excluded work on ____ electrical components.','mains','C: excluded work on mains electrical components',maxWords=1),
tq('A small part might be sold only within a larger ____.','assembly','D: part of a much larger assembly',maxWords=1),
tq('Buyers need information about the software ____ before purchase.','support period','E: information about the support period',maxWords=2),
sq('Which paragraph considers energy consumption?','F',list('ABCDEF'),'F: use much more energy','后段比较修理与换新的生命周期影响。'),
sq('Which paragraph warns that one headline number hides important differences?','B',list('ABCDEF'),'B: a single score compresses several different issues','headline number 即综合评分。'),
sq('Best heading for paragraph E?','An invisible limit to product life',['An invisible limit to product life','Why batteries never fail','Training workshop volunteers','Energy labels for new homes'],'E: Software ... updates ... services stop','软件支持停更是非物理限制。'),
sq('What should participants do before a case is opened?','A',['A: describe the fault','B: buy a larger assembly','C: remove all software','D: choose a new appliance'],'C: explain the fault before anyone opened a case','describe 与 explain 同义。'),
tf('The passage claims modular design always increases product life.','FALSE','D: does not assume that every modular product will last longer','always 明确被否定。'),
tq('Standard ____ can help reduce repair obstacles.','fasteners','D: Standard fasteners and modular parts',maxWords=1),
sq('What is the author’s main recommendation?','C',['A: replace every old product','B: repair every product regardless of cost','C: remove avoidable barriers so owners can decide','D: ban independent workshops'],'F: enable an informed decision','核心是选择权和知情决策，而非永远修或换。')]))
readings.append(passage('Why a forecast needs more than a number', '''A forecast can be useful without being certain. Weather services, transport planners and public-health teams all make decisions before the future is known. A single predicted value is easy to communicate, but it can conceal the range of outcomes that remain plausible. For someone deciding whether to protect equipment from rain, the chance of a severe event may matter more than the most likely rainfall total. Good forecasting is therefore connected to the decision being made, not simply to the appeal of a precise-looking number.

One method uses an ensemble: a collection of model runs with varied starting conditions or assumptions. If these runs produce different outcomes, their spread can reveal sensitivity to uncertainty. However, agreement does not prove accuracy. All members may share a missing process or a biased input. A narrow range can then create confidence without justification. Forecast designers need to compare predictions with later observations, not merely admire agreement among models. Variety has value when it captures meaningful differences, rather than cosmetic changes to the same assumptions.

Calibration asks whether stated probabilities match observed frequencies over many comparable cases. If events assigned a probability of seventy per cent occur roughly seventy per cent of the time, that set of forecasts is well calibrated in this respect. It does not mean that any individual event was guaranteed. Nor is calibration the only useful property: a forecast that always gives a broad average may fail to distinguish high-risk situations from ordinary ones. Users also need information that changes appropriately when conditions change.

In a fictional coastal authority, two teams considered closing a waterfront path. The maintenance team cared about damage to temporary barriers, while the visitor team cared about safe access. They agreed to discuss consequences and available actions before selecting a warning threshold. Closing too often had costs, but failing to close during a dangerous event had different and potentially larger consequences. A decision threshold was therefore not simply a scientific constant; it reflected responsibilities, resources and the severity of possible harm.

Communication shaped the response. A coloured map attracted attention, but some residents interpreted the boundary of a warning area as an exact physical border. The authority added a short explanation that conditions changed gradually and local exposure varied. It also stated when the forecast would be updated. Providing uncertainty did not require listing every possible outcome. It required explaining which differences mattered and what people could reasonably do next, while making clear that new observations could alter the advice.

After each event, staff reviewed both the forecast and the decision. A sensible precaution could be followed by harmless weather; that alone did not prove the precaution unreasonable. Equally, a lucky outcome could conceal poor reasoning. The review used information available at the time, along with later observations, to improve future practice. The broader lesson is that judging a forecast solely by whether one dramatic event happened confuses the quality of a process with the result of a single uncertain case.''',[
tf('All ensemble members can agree and still be wrong.','TRUE','B: agreement does not prove accuracy ... share a missing process','多模型可共享偏差。'),
tf('A seventy per cent probability guarantees a particular event.','FALSE','C: does not mean that any individual event was guaranteed','概率长期频率不是单次保证。'),
tf('The coastal authority used exactly twenty model runs.','NOT GIVEN','D: two teams，不是模型数量','团队数量不能替代运行次数。'),
tq('A collection of model runs is called an ____.','ensemble','B: an ensemble: a collection of model runs',maxWords=1),
tq('Probability statements are checked against observed ____ over many cases.','frequencies','C: match observed frequencies',maxWords=1),
tq('The authority decided on a warning ____ after discussing consequences.','threshold','D: before selecting a warning threshold',maxWords=1),
sq('Which paragraph describes misunderstanding a map?','E',list('ABCDEF'),'E: interpreted the boundary ... exact physical border','边界误读在 E。'),
sq('Which paragraph warns against judging a decision by luck?','F',list('ABCDEF'),'F: a lucky outcome could conceal poor reasoning','好结果不保证好决策。'),
sq('Best heading for paragraph C?','Probabilities tested across many events',['A forecast with no uncertainty','Probabilities tested across many events','Protecting temporary barriers','Why all models are identical'],'C: Calibration asks whether ... over many comparable cases','校准需要多事件频率验证。'),
sq('Why did the coastal teams discuss actions first?','B',['A: to eliminate all uncertainty','B: because consequences and responsibilities affect a threshold','C: to guarantee no closure costs','D: to replace weather observations'],'D: reflected responsibilities, resources and severity','阈值须结合决策损失，而非固定科学常数。'),
yn('The author favours reviewing the information available when a decision was taken.','YES','F: used information available at the time','作者支持从决策当时信息出发评估。'),
yn('The author recommends omitting uncertainty to simplify advice.','NO','E: explaining which differences mattered','作者主张解释有用的不确定性。'),
tq('The authority told residents when the forecast would be ____.','updated','E: stated when the forecast would be updated',maxWords=1),
sq('What is the central argument?','D',['A: a single correct prediction proves a model','B: warnings should never change','C: all uncertainty prevents decisions','D: forecasts should support decisions and communicate uncertainty'],'A–F: 决策、校准、传播与复盘','全文从预测的决策用途展开，而非只追求数字精确。')]))
papers=[]
for setno in range(2):
 parts=readings[setno*3:setno*3+3];n=0
 for pi,p in enumerate(parts):
  p['id']=f'r{setno+1}-p{pi+1}'
  for q in p['questions']:n+=1;q['id']=f'r{setno+1}-q{n}'
 papers.append(dict(id=f'reading-{setno+1}',skill='reading',title=['城市、自然与研究','公共空间、维修与预测'][setno],subtitle='3 篇 · 40 题 · 原文证据与逐题解析',minutes=60,source='本站原创教学模拟材料；虚构研究明确标记，不作为科学事实来源。',kind='原创练习',review='答案已核对原文，未经过真人考官或试题测量校准；篇幅较正式考试精简。',updated=DATE,difficulty='学术主题与 B2 常见论述；题目难度未标准化',passages=parts))
write('papers.json',papers)
print('resources',len(resources),'reading papers',len(papers),'reading questions',sum(len(p['questions']) for paper in papers for p in paper['passages']))
