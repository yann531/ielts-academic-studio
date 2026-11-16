import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1];OUT=ROOT/'src'/'data'
parts=[]
def add(title,part,script,rows):
 qs=[]
 for row in rows:
  prompt,answer,evidence,*rest=row
  qs.append(dict(type='text',prompt=prompt,answers=answer if isinstance(answer,list) else [answer],maxWords=rest[0] if rest else 2,evidence=evidence,explanation='依据录音中的直接信息作答。注意转折与修正，答案须符合字数限制；所列证据可在下方全文中查找。',trap='先听清最终确定的信息，不能看到相关词就作答。'))
 parts.append(dict(title=title,part=part,paragraphs=[dict(label='Transcript',text=script)],questions=qs,audioKind='离线合成教学音频 · Microsoft Zira · 单一美式声线；非官方真人录音'))
add('Part 1 · Joining a community workshop',1,'''This is an original listening exercise. Part one. A visitor is asking about a community workshop. Read questions one to ten before listening.

Receptionist: Hello, welcome to the Riverside workshop centre. How can I help?
Visitor: I would like to join the practical course. I saw an advertisement for painting, but it is actually the pottery course that interests me.
Receptionist: Certainly. May I take your surname?
Visitor: It is Bennett. That is B, E, N, N, E, T, T. The final letter is T.
Receptionist: Thank you. The next course starts on the fourteenth of May. The old leaflet says the seventh, but that session has been moved.
Visitor: The fourteenth is fine. Is it held every Monday?
Receptionist: No, that is the advanced group. Your group meets on Thursday. Classes begin at six thirty in the evening. We suggest arriving a little earlier the first time, so you can find the room.
Visitor: And how much does the course cost? Someone mentioned sixty pounds.
Receptionist: Sixty is the reduced student price. The standard fee for the whole course is seventy-five pounds. That includes the tools and clay. You do not need to purchase those separately.
Visitor: I am not a student, so I will pay the standard fee. Should I bring anything with me?
Receptionist: Please bring an apron. We provide tools, but your clothes may get dirty. Some visitors bring gloves, though those are not required.
Visitor: Where exactly is the classroom?
Receptionist: It is in the garden studio. Go past the main office and follow the path. The upstairs studio is used for drawing, so do not go there.
Visitor: Can I come by bus?
Receptionist: Yes, take the number twenty-four. It stops outside the centre. The number forty-two goes to a different part of town.
Visitor: Wonderful. I have never done this before. Is that a problem?
Receptionist: Not at all. This group is for beginners. You can move to the intermediate class later if you wish. I will reserve your place and send the payment instructions today.
Visitor: Thank you very much.
This is the end of part one. Check your answers.''',[
('Course selected','pottery','Visitor: it is actually the pottery course',1),('Visitor’s surname','Bennett','B, E, N, N, E, T, T',1),('Start date (day and month)',['14 May','May 14','fourteenth May'],'starts on the fourteenth of May',2),('Day of weekly classes','Thursday','Your group meets on Thursday',1),('Start time',['6:30','6.30','six thirty','18:30'],'six thirty in the evening',2),('Standard fee (£, write a number)',['75','75.00'],'standard fee ... seventy-five pounds',1),('Item to bring','apron','Please bring an apron',1),('Teaching room','garden studio','It is in the garden studio',2),('Bus number',['24','twenty-four'],'number twenty-four',1),('Level of group','beginners','This group is for beginners',1)])
add('Part 2 · A visitor centre tour',2,'''This is an original listening exercise. Part two. A guide introduces a visitor centre. Read the questions before listening.

Good morning, everyone, and welcome to the Meadow visitor centre. Before you explore, I will explain how the site works. The building opens at nine, but our first guided walk starts at ten. Please do not confuse the opening time with the walk time. If you want to join, register here at reception rather than waiting outside.
The walk takes ninety minutes. Some older notices describe a two-hour route, but that path is closed for maintenance. Our current route is shorter and avoids the steep steps. It is suitable for people who prefer a gentle walk, although everyone should wear suitable shoes.
Now, imagine a simple plan of the centre. You are standing in the entrance at the southern end. Immediately to your left is the cafe. On your right is the shop, where local artists sell postcards and small prints. If you walk straight ahead from the entrance, the exhibition room is at the north end of the corridor. Do visit it before you leave; it explains how the nearby river has changed.
You can borrow binoculars from the desk beside the exhibition room. We do not charge for borrowing them, but you need to leave a deposit of ten pounds. It is returned when you bring the equipment back. Please return everything before four thirty, when the equipment desk closes.
If you have brought children, there is a special activity this afternoon. They will make paper birds, not wooden boats as announced last month. The session starts after lunch and is supervised by two members of staff. Each child should still be accompanied by an adult.
There is also a short talk for adults about river restoration. It will be given by a local ecologist. She will discuss recent changes to the riverbank and explain which observations visitors can contribute. You do not need any scientific training to attend.
One final request: the outdoor path can be muddy after rain. Please wear boots if you have them. There is no need to bring a helmet because we are walking, not cycling. Maps are available on this desk, and I am happy to answer questions. Thank you, and enjoy your visit.
This is the end of part two.''',[
('First guided walk starts at',['10','10:00','ten'],'first guided walk starts at ten',1),('Register for the walk at','reception','register here at reception',1),('Walk duration (minutes)',['90','ninety'],'walk takes ninety minutes',1),('Place immediately left of the entrance','cafe','Immediately to your left is the cafe',1),('Room at the north end','exhibition room','exhibition room is at the north end',2),('Equipment visitors can borrow','binoculars','borrow binoculars',1),('Refundable deposit (£)',['10','ten'],'deposit of ten pounds',1),('Children will make','paper birds','make paper birds',2),('Profession of the talk’s speaker','ecologist','given by a local ecologist',1),('Recommended footwear','boots','Please wear boots',1)])
add('Part 3 · Planning a student investigation',3,'''This is an original listening exercise. Part three. Two students discuss a research assignment with their tutor.

Tutor: You have chosen a topic for the assignment. Tell me how it has developed.
Maya: We first considered food waste in student kitchens. But we could not get reliable access to the kitchens, so we changed the topic to bicycle parking on campus.
Leo: We want to know why people leave bicycles outside the marked spaces. There may not be enough spaces, or the existing ones may be inconvenient.
Tutor: Good. How will you collect evidence?
Maya: We will begin with observations at different times, rather than sending out a questionnaire immediately. That should show us where the problem actually occurs.
Tutor: Which locations will you use?
Leo: Three sites: the library, the sports centre and the science building. We considered the main gate, but the construction work there would distort the results.
Maya: At each site we will observe for thirty minutes in the morning and again in the afternoon. A full hour at each visit would be difficult with our class schedule.
Tutor: How long will the study run?
Leo: Two weeks. A single day would be too dependent on the weather. We will record weather conditions as part of the observation sheet.
Tutor: You should test that sheet first.
Maya: Yes, we plan a pilot on Friday. It should reveal whether our categories are clear enough. We may need to distinguish bicycles attached to railings from bicycles blocking a path.
Tutor: What about asking users why they parked there?
Leo: We could conduct short interviews after the pilot, if the ethics process allows it. We will not collect names. The information sheet explains that participation is voluntary.
Tutor: Remember that people may give answers they think you want. Compare interviews with observations instead of treating either as the whole picture.
Maya: For the presentation, we thought of using a table for every measurement.
Tutor: A table is useful in the appendix, but a map will make the location differences clearer in the main presentation.
Leo: That makes sense. When is the final report due?
Tutor: The draft is due on the twelfth of June, and the final version on the nineteenth. Do not confuse the two dates. Please send the observation sheet before your pilot, so I can comment on it.
This is the end of part three.''',[
('Topic finally selected','bicycle parking','changed the topic to bicycle parking',2),('First evidence-gathering method',['observations','observation'],'begin with observations',1),('Location excluded','main gate','considered the main gate, but ... construction',2),('Minutes at each visit',['30','thirty'],'thirty minutes',1),('Study length',['two weeks','2 weeks'],'Two weeks',2),('Day of the pilot','Friday','pilot on Friday',1),('Personal detail that will not be collected','names','We will not collect names',1),('Participation must be','voluntary','participation is voluntary',1),('Recommended main visual','map','a map will make the location differences clearer',1),('Final report date',['19 June','June 19','nineteenth June'],'final version on the nineteenth [of June]',2)])
add('Part 4 · Managing rain where it falls',4,'''This is an original listening exercise. Part four. A lecturer discusses rain gardens. The lecture is a simplified teaching example, not a report of a real study.

Today I will discuss small urban landscapes designed to manage rainwater. A rain garden is a shallow planted depression that temporarily holds runoff. Unlike a decorative pond, it is not intended to remain filled with water permanently. The water gradually soaks into the soil, and the plants tolerate alternating wet and dry conditions.
The primary aim is to reduce runoff entering drains during rainfall. That can help a drainage system cope with short periods of heavy flow. A rain garden should not, however, be described as a solution to every kind of flooding. Its performance depends on the site, the soil and the volume of water reaching it.
Site selection begins with understanding the soil. A simple infiltration test measures how readily water enters the ground. Where infiltration is poor, the design may need an underdrain or a different location. Positioning a garden close to a building without checking local guidance could create problems, so technical advice remains important.
The surface is planted, but much of the work happens below it. A layer of gravel may provide space for temporary water storage and support drainage. Designers must consider where excess water will go during a very large storm. An overflow route sends that water to a planned destination rather than allowing it to find an accidental path.
Plant choice also matters. Native plants can be suitable when their needs match the conditions, but the label native alone is not enough. The design must consider tolerance of both short wet periods and longer dry periods. In our fictional demonstration garden, the team chose a mixture of grasses and flowering plants rather than a single species.
Maintenance is often underestimated. Litter can block the inlet, which is the point where runoff enters. Removing that litter and checking the inlet after storms helps keep the system working. Staff also inspect for erosion and replace failed plants when necessary. These tasks need a named person or team, not just a note in the original design.
Finally, evaluation should look at several outcomes. Measuring water levels can show how quickly the garden drains. Recording maintenance hours reveals the work required. Observing insects may provide information about habitat value, although one visit cannot describe an entire season. A useful report should combine these observations and state the limits of its evidence. The garden is part of a wider drainage strategy, not a substitute for every other measure.
This is the end of part four.''',[
('A rain garden is a planted','depression','shallow planted depression',1),('Main flow reduced','runoff','reduce runoff entering drains',1),('Initial test measures','infiltration','infiltration test',1),('Possible subsurface storage layer','gravel','layer of gravel',1),('Planned path for excess water','overflow route','An overflow route sends that water',2),('Plants must tolerate wet and ____ periods.','dry','short wet periods and longer dry periods',1),('Demonstration garden included grasses and ____ plants.','flowering','grasses and flowering plants',1),('Litter can block the','inlet','Litter can block the inlet',1),('Evaluation records maintenance','hours','Recording maintenance hours',1),('Habitat observations include','insects','Observing insects',1)])
add('Part 1 · Reserving a study room',1,'''This is an original listening exercise. Part one. A student calls a university building to reserve a room.

Assistant: Good afternoon, learning centre reception.
Student: Hello. I need a room for a small project meeting. My surname is Patel, P, A, T, E, L. I have used the centre before, but not the meeting rooms.
Assistant: When would you like to come?
Student: On the twenty-second of October. We originally planned the twenty-first, but one member has a laboratory class that day.
Assistant: There is a room available at two fifteen in the afternoon. The two o'clock slot is already booked.
Student: Two fifteen will work. There will be six of us. We might invite another student next week, but only six will attend this meeting.
Assistant: Then the Cedar room should be suitable. It has eight chairs, so you will have enough space. The smaller Birch room only has four.
Student: Is a projector available?
Assistant: Yes. I will reserve one for you. The screen is fixed in the room. Please bring your own laptop, because we do not lend those for meetings.
Student: Fine. Where do I collect the key?
Assistant: From the security desk, not this reception. The security desk is beside the east entrance. You will need to show your student card when you collect it.
Student: How long can we stay?
Assistant: The maximum booking is two hours. You can book a shorter session, but you cannot go beyond two hours because another group may need the room.
Student: Is there any fee?
Assistant: Not for registered students. If you no longer need the booking, please give us at least twenty-four hours' notice. We can then offer it to somebody else.
Student: I will let you know. Could you send the details in writing?
Assistant: Of course. The confirmation will be sent by email, usually within an hour. Check your spam folder if it does not arrive. Please reply if the date or time is wrong, and we will correct it.
Student: Thank you for your help.
This is the end of part one.''',[
('Student’s surname','Patel','P, A, T, E, L',1),('Meeting date',['22 October','October 22'],'twenty-second of October',2),('Start time',['2:15','2.15','14:15','two fifteen'],'two fifteen in the afternoon',2),('People attending (number)',['6','six'],'only six will attend',1),('Room name','Cedar','the Cedar room',1),('Equipment reserved','projector','a projector ... reserve one',1),('Key collection point','security desk','From the security desk',2),('Maximum booking length',['two hours','2 hours'],'maximum booking is two hours',2),('Cancellation notice (hours)',['24','twenty-four'],'twenty-four hours notice',1),('Confirmation sent by','email','sent by email',1)])
add('Part 2 · Helping at the local museum',2,'''This is an original listening exercise. Part two. A museum coordinator welcomes new volunteers.

Welcome to the local history museum. I am glad you can help us this season. Your first training session will be on Saturday. We considered Sunday, but the trainer is unavailable then. Please come to the education room, which is upstairs beside the small library.
The entrance for volunteers is on the west side of the building. Visitors use the main entrance at the front, but it may still be locked when you arrive. The west door opens earlier. Ring the bell if no member of staff is there to welcome you.
During training, you will receive a blue badge. Please wear it whenever you are volunteering, so visitors know whom to approach. Green badges are for our permanent staff. If you lose your badge, tell the coordinator rather than borrowing somebody else's.
Your initial shift will last three hours. We ask new volunteers not to sign up for a full day until they know the role. There will be time for a break, and you can use the staff kitchen for drinks. The cafe is for visitors and can get busy at lunchtime.
Photography is allowed in most rooms, but flash is not permitted because some objects are sensitive to light. If visitors ask you about photographs, please explain that distinction. Do not tell them that all photography is banned.
For questions about access or facilities, use the radio. A member of staff can give current information. Please do not leave a busy room unattended to search for someone. If a visitor has lost something, send them to reception, where staff keep the lost property record.
We encourage you to ask questions yourself. On your first visit, you will work with a mentor. This person can show you how to describe objects without touching them and how to respond when you do not know an answer. It is better to check than invent a fact about an object.
Finally, if you cannot attend your shift, contact us by telephone. Email is useful for routine questions, but we may not read it quickly enough on a busy morning. Please call as early as possible. Thank you for giving your time; your help makes the museum more welcoming.
This is the end of part two.''',[
('Training day','Saturday','first training session ... Saturday',1),('Volunteer entrance on the ____ side','west','west side of the building',1),('Badge colour','blue','receive a blue badge',1),('Initial shift length',['three hours','3 hours'],'initial shift will last three hours',2),('Place for volunteers’ drinks','staff kitchen','staff kitchen for drinks',2),('Type of photography not allowed','flash','flash is not permitted',1),('Device for contacting staff','radio','use the radio',1),('Lost property enquiries go to','reception','send them to reception',1),('New volunteers work with a','mentor','work with a mentor',1),('Urgent absence reported by',['telephone','phone'],'contact us by telephone',1)])
add('Part 3 · Improving a survey',3,'''This is an original listening exercise. Part three. Two students review a survey with their supervisor.

Supervisor: Let us review the survey before you send it out. What question are you investigating?
Nora: How students use the campus cafe as a study space. At first we called the project student diet, but that was much broader than our actual questions.
Sam: Our respondents will be first-year students. We cannot claim that they represent every student, but this is the group our assignment focuses on.
Supervisor: How many responses do you hope to receive?
Nora: Eighty. We originally wrote one hundred and fifty in the plan, but that would be unrealistic in the time available. Eighty is our revised target, not a result we have already achieved.
Supervisor: Good distinction. Now, your second question asks whether the cafe is cheap and convenient. That combines two different judgments.
Sam: So we should separate them into two questions. A student might find it convenient but expensive.
Supervisor: Exactly. And avoid suggesting the answer. Ask neutrally rather than saying that the cafe is obviously too noisy.
Nora: We will include an option for people who never use it. Otherwise the survey might force them to express an opinion they do not have.
Supervisor: Test the revised form with a small group.
Sam: We can run the pilot with five students tomorrow. We will ask them to describe any question they find confusing.
Nora: For recruitment, we planned to approach people outside the cafe, but that could miss students who avoid it. We will use the course mailing list instead.
Supervisor: Remember to ask permission to use that list. Your introduction should explain the purpose, the time required and how responses will be used.
Sam: We estimate that completion will take four minutes. The pilot will help us check that estimate.
Nora: We will report results as percentages as well as actual counts, so readers can see the size of the sample. For the main figure, would a pie chart work?
Supervisor: A bar chart would make comparison between response categories easier. Explain how many people answered each question because some may leave items blank.
Sam: When do you need the revised survey?
Supervisor: By Wednesday, please. Then there will be time to comment before distribution. Do not start collecting full responses until the form has been approved.
This is the end of part three.''',[
('Place studied','campus cafe','campus cafe as a study space',2),('Target group','first-year students','respondents will be first-year students',2),('Revised target responses',['80','eighty'],'Eighty is our revised target',1),('Questions combining judgments should be',['separated','separate'],'separate them into two questions',1),('Number of pilot students',['5','five'],'pilot with five students',1),('Recruitment channel','mailing list','course mailing list instead',2),('Estimated completion time',['four minutes','4 minutes'],'take four minutes',2),('Results shown as counts and','percentages','as percentages as well as actual counts',1),('Suggested main figure','bar chart','A bar chart',2),('Revised survey due by','Wednesday','By Wednesday',1)])
add('Part 4 · Light and daily rhythms',4,'''This is an original listening exercise. Part four. A lecturer explains daily rhythms in a simplified teaching talk. This is not medical advice.

Today we are considering how light helps coordinate daily biological rhythms. A circadian rhythm is an approximately daily pattern. The word approximately is important: without environmental signals, an individual's internal cycle may not match exactly the twenty-four hours of the day. Light is one of the signals that helps the internal system stay aligned with the environment.
Information about light enters through the retina, the light-sensitive tissue at the back of the eye. This does not mean that every response to light is the same as forming a visual image. Biological timing involves specialised pathways as well as ordinary sight. For our purposes, remember that timing depends on signals, not simply on deciding to feel awake.
The effect of light depends partly on its timing. Morning light and late-evening light can influence the daily cycle differently. Brightness and duration also matter, so it is misleading to discuss a device only by the colour of its screen. A short, dim exposure and a long, bright exposure are not equivalent situations.
In a fictional classroom demonstration, students kept a sleep diary for a week. The aim was to notice patterns, not diagnose a disorder. Each diary recorded bedtime, waking time and the student's sense of alertness. The group also noted caffeine use, because that could influence how awake people felt independently of the light conditions.
Wearable devices were discussed as another source of information. They can estimate activity and rest over time, but their measurements are not identical to a clinical sleep assessment. Students were asked to compare their diary with the device's output rather than assume the device was always correct. An apparent disagreement could reflect the limits of either source.
Consistency was another theme. A very different weekend schedule can complicate the relationship between social commitments and biological timing. Yet simply telling everyone to follow one schedule ignores shift work, caring responsibilities and individual variation. Public advice needs to recognise those constraints instead of blaming people for every difficulty.
Finally, the lecturer stressed uncertainty. The class demonstration was observational. It could identify associations, but it could not prove that one factor caused a change in sleep. A controlled experiment would require a more careful design. Anyone experiencing persistent sleep problems should seek appropriate professional advice rather than treat this teaching exercise as a diagnosis. The useful lesson is to record context, question simple explanations and distinguish a pattern from a causal conclusion.
This is the end of part four.''',[
('Daily biological rhythm described as','circadian','A circadian rhythm',1),('Light-sensitive tissue','retina','through the retina',1),('Exposure factors include brightness and','duration','Brightness and duration also matter',1),('Students kept a sleep','diary','kept a sleep diary',1),('Additional substance recorded','caffeine','noted caffeine use',1),('Wearables estimate activity and','rest','estimate activity and rest',1),('A changing ____ schedule can complicate timing.','weekend','different weekend schedule',1),('One social constraint is ____ work.','shift','shift work',1),('The demonstration was','observational','demonstration was observational',1),('Patterns alone do not prove','causation','distinguish a pattern from a causal conclusion',1)])
papers=json.loads((OUT/'papers.json').read_text(encoding='utf-8'));audio_dir=ROOT/'public'/'audio';audio_dir.mkdir(parents=True,exist_ok=True)
for si in range(2):
 group=parts[si*4:si*4+4];num=0
 for pi,p in enumerate(group):
  p['id']=f'l{si+1}-p{pi+1}';p.pop('part');p['audio']=f'audio/{p["id"]}.wav'
  for q in p['questions']:num+=1;q['id']=f'l{si+1}-q{num}'
 papers.append(dict(id=f'listening-{si+1}',skill='listening',title=['社区、校园与雨水','学习空间、调查与节律'][si],subtitle='4 Parts · 40 题 · 合成音频教学套练',minutes=30,source='本站原创对话与讲座，Microsoft Zira 离线语音合成；不是官方真人录音。',kind='原创练习',review='答案已核对文本，未考官校准。单一合成声线、语速与时长均不代表真实考试；当前以填空题为主，选择与地图题请使用官方样题。',updated='2026-11-13',difficulty='日常场景到学术讲座，按 Part 组织，尚无试题难度测量',passages=group))
(OUT/'papers.json').write_text(json.dumps(papers,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'scripts'/'audio-scripts.json').write_text(json.dumps([{'id':p['id'],'text':p['paragraphs'][0]['text']} for p in parts],ensure_ascii=False,indent=2),encoding='utf-8')
print('listening',len(parts),'parts / 80 questions; run scripts/make-audio.ps1')
