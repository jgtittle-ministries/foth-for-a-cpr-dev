# GS Week 15 adult re-authoring: the rite becomes the exit gate of the
# leadership-first year — the covering commissions the cohort.
import io, sys, re
f = 'docs/getting-started/week-15-commissioning.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')
R('**Aim.** The Companions-in-Formation are commissioned as FC1 — Formation Companion, Level One. Not a ceremony appended to the series close: an exit gate run as a witnessed rite. Four movements: the final rep (the container opened and closed from memory, publicly); the three rules read aloud to the whole room; the covering named; the commissioning — with the first Leader Lab of the spring serving cycle scheduled before anyone leaves. The seniors leave this room having *begun*, not merely finished.',
  '**Aim.** The cohort is commissioned as the host church’s Formation Companion team. Not a ceremony appended to the series close: the exit gate of the leadership-first challenge, run as a witnessed rite. Four movements: the final rep (the container opened and closed from memory, publicly); the three rules read aloud to the whole room; the covering named — the pastor or elders publicly taking spiritual authority over the family year; the commissioning — with the family year’s first date on the calendar before anyone leaves. The cohort leaves this room having *begun*, not merely finished.')
R("**Connect focus.** All four. The seniors' own formation (Self), the community that witnesses (Others), the calling confirmed (God), the serving cycle entered (Mission).",
  '**Connect focus.** All four. The cohort’s own formation (Self), the community that witnesses (Others), the calling confirmed (God), the family year entered (Mission).')
R("**Mode.** Shared circle the entire session. The whole cohort and the families are present as witnesses — but this is the seniors' night. The seniors lead; the adults confirm and bless; the cohort witnesses.",
  '**Mode.** Shared circle the entire session. The households are present as witnesses, and the covering is in the room — this is the cohort’s sending. The cohort leads; the covering confirms and sends; the households witness.')
R("**Between-session practice.** For the new FC1s: the Leader Lab rhythm begins — bring one vital-signs observation from tonight's room to Lab 1 of the serving cycle. For everyone: the Rhythm Card and the Going Deeper interlude practices.",
  '**Between-session practice.** For the new Companions: the family year’s preparation begins — bring one vital-signs observation from tonight’s room to the team’s first planning call. For everyone: the Rhythm Card and the Going Deeper interlude practices.')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! QRC count={n}: {old[:64]}'); fail += 1; continue
    s = s.replace(old, new)

# Block 1 rewrite
i = s.index('*"Welcome to the last gathering of Getting Started.')
j = s.index('## **Block 2 — The Final Rep')
new_b1 = '''*"Welcome to the last gathering of Getting Started. Phones in the box — you know the drill better than any group I have ever asked."*

*"Last week we blessed the households. Tonight the church commissions this cohort — and I want to be careful about the word, because this is not a graduation. Nobody is leaving. A graduation sends you out of a room; tonight opens a door further in. This cohort took a challenge a year ago: walk it yourselves before you ask any family to trust it. Tonight the covering says out loud what the year has shown, and commissions this team for the year that was the point all along. They are not finishing something tonight. They are beginning something."*

*"Here is the shape of the night — four movements. First, the final rep: members of this cohort will open this container the way it has been opened all year — from memory, no script — because that is the spine of what a Companion is. Second, we will read aloud the three rules that never bend, so that every household in this room knows exactly the boundaries this team keeps. Third, the covering is named: [pastor's/the elders'] authority over what comes next, said publicly, and each Companion's own covering with it. And fourth, the commissioning: the covering sends this team, we bless them, all of us — and before anyone leaves this room, the family year's first date will be on the calendar. Watch for that last part. It is the proof that tonight is a beginning."*

*"One more thing. These people have led each other all year. Tonight, lean in one more time — because what you are watching is a church deciding, in public, who holds its most delicate work, and true things deserve witnesses. Cohort: the room is yours."*

'''
s = s[:i] + new_b1 + s[j:]

more = [
("The heart of the gate. Container fluency — establishing and holding Safe, Present, Clear, Intentional from memory, under mild pressure, without a script — is FC1's spine competency, and tonight it is demonstrated publicly. This is not a pop quiz. Every senior has run this protocol repeatedly since Week 5; the gate was passed across the arc. Tonight is the witness of it.",
 'The heart of the gate. Container fluency — establishing and holding Safe, Present, Clear, Intentional from memory, under mild pressure, without a script — is a Companion’s spine competency, and tonight it is demonstrated publicly. This is not a pop quiz. The rotation leaders have run this protocol repeatedly all year; the gate was passed across the arc. Tonight is the witness of it.'),
('- **One senior opens the container**', '- **One member opens the container**'),
("- **One senior will close the container** in Block 8 — held in reserve; tell them tonight's close is theirs.",
 "- **One member will close the container** in Block 8 — held in reserve; tell them tonight's close is theirs."),
('- **Every other senior speaks one container condition from memory** — Safe, Present, Clear, or Intentional — in their own words, with one short true story of holding that condition while leading this year. ("Clear means no unaddressed conflict in the room. The week I led PROAPT II, two of the junior guys came in mid-argument, and here is what I did...") Sixty to ninety seconds each. Assign the conditions in the team meeting; more seniors than conditions simply means conditions are shared, each with a different story.',
 '- **Every other rotation leader speaks one container condition from memory** — Safe, Present, Clear, or Intentional — in their own words, with one short true story of holding that condition while leading this year. ("Clear means no unaddressed conflict in the room. The week I led PROAPT II, two of us came in carrying an unfinished argument, and here is what I did...") Sixty to ninety seconds each. Assign the conditions in the team meeting; more leaders than conditions simply means conditions are shared, each with a different story.'),
('- If there are only two seniors, one opens and one closes, and each also speaks one condition with a story. If there is one senior, the night is theirs entirely — they open and close both, and the conditions live inside their opening.',
 '- If only two members led this year, one opens and one closes, and each also speaks one condition with a story. If one, the night’s reps are theirs — and the conditions live inside their opening.'),
('If a senior freezes: the Lead Companion, calm and warm, from their seat: *"Take a breath. You have opened this container more times than anyone in this room but me. Start with Safe."* Give them the first word; they will find the rest — they almost always do.',
 'If a member freezes: the convening leader, calm and warm, from their seat: *"Take a breath. You have opened this container more times than anyone in this room but me. Start with Safe."* Give them the first word; they will find the rest — they almost always do.'),
('If they cannot continue: the Lead Companion stands, puts a hand on their shoulder, and tells the room the truth: *"Here is what you need to know. [Name] has opened or closed this container [eight, ten] times since October, under every condition a Tuesday can throw at a room. The gate this rite witnesses was passed weeks ago. Tonight has more witnesses than usual, and witnesses are heavy. [Name], stand with me and we will finish it together."*',
 'If they cannot continue: the convening leader stands, puts a hand on their shoulder, and tells the room the truth: *"Here is what you need to know. [Name] has opened or closed this container [eight, ten] times this year, under every condition an evening can throw at a room. The gate this rite witnesses was passed weeks ago. Tonight has more witnesses than usual, and witnesses are heavy. [Name], stand with me and we will finish it together."*'),
('*"Two scriptures over tonight. The first is the architecture of everything we are doing. The second is for our seniors specifically."*',
 '*"Two scriptures over tonight. The first is the architecture of everything we are doing. The second is for this team specifically."*'),
('*"Let no one despise you for your youth, but set the believers an example in speech, in conduct, in love, in faith, in purity."*\n\n— 1 Timothy 4:12 (ESV)',
 '*"Shepherd the flock of God that is among you, exercising oversight, not under compulsion, but willingly, as God would have you; not for shameful gain, but eagerly; not domineering over those in your charge, but being examples to the flock."*\n\n— 1 Peter 5:2–3 (ESV)'),
('*"And the second verse: Paul wrote it to a young leader who had every reason to wonder if he was too young for the work. Let no one despise you for your youth. Tonight this room does the opposite of despising."*',
 '*"And the second verse: Peter wrote it to elders — to exactly the kind of people in this circle — and notice what it asks and what it forbids. Willingly, not under compulsion. Examples, not lords. That is the whole leadership-first idea in apostolic form: you can only shepherd a flock into what you have walked yourself."*'),
('*"Father, You heard these seniors say yes in the fall, and You have been forming them every Tuesday since. Tonight we do in public what You have been doing in private. Confirm what You have started. Guard what we entrust. And let the generations in Your word keep unrolling through this room. Amen."*',
 '*"Father, You heard this cohort say yes a year ago, and You have been forming them every week since. Tonight we do in public what You have been doing in private. Confirm what You have started. Guard what we entrust. And let the generations in Your word keep unrolling through this room. Amen."*'),
("The bright line made public. The whole cohort — the room these seniors will serve — hears exactly the boundaries its young leaders keep. This is part of everyone's safety, not just the seniors'.",
 'The bright line made public. The households in this room — the first families the new team will serve — hear exactly the boundaries this team keeps. This is part of everyone’s safety, not just the team’s.'),
('*"Before we commission anyone, the whole room is going to hear the three rules our teen leaders live under. We read these out loud on purpose. You have signed covenants in this room; you know that the promises are not the opposite of freedom — they are what makes the work safe enough to do. The Measurement Covenant is that kind of promise. These three rules are that kind of promise. They are not a leash on our seniors. They are the frame that lets a sixteen-year-old lead a room like this one and lets every parent in this circle sleep at night. Hear them, and know them, because these boundaries protect you and your kids as much as they protect the leaders."*',
 '*"Before anyone is commissioned, the whole room is going to hear the three rules this team will live under. We read these out loud on purpose. Promises are not the opposite of freedom — they are what makes the work safe enough to do. These three rules are that kind of promise. They are not a leash on this team. They are the frame that lets a church hand its families to a fellowship like this one and sleep at night. Hear them, and know them, because these boundaries protect you and your households as much as they protect the leaders."*'),
('''**1. A Companion-in-Formation never counts as one of the two adults.** The supervision rule is unchanged. "Co-lead" means an adult Companion in the room — not nearby, in the room.

**2. A Companion-in-Formation never takes a disclosure.** If something heavy surfaces while they are leading, their only job is to hand it to the adult immediately. They are not a junior counselor.

**3. Lead only a block you have first received.** See it, then lead it. Never lead a process you have not first experienced as a participant.''',
 '''**1. Two Companions, always.** Nobody on this team holds a disclosure, a crisis, or a closed door alone. The second Companion is not a formality; it is the shape of safety.

**2. Hand what belongs to the qualified across the line.** This work may be therapeutic; it is not therapy. The door out and the referral list are this team's to keep real, and handing a heavy thing across the line is the strong, faithful move — never a failure.

**3. Lead only a block you have first received.** See it, then lead it. Never lead a process you have not first experienced as a participant — which is what this whole year was.'''),
('''*"Those three rules are the whole of a teen leader's safety, and they never bend — not for talent, not for maturity, not for a night when we are short-handed. Seniors, when you keep these rules, you are not being kept small. You are being kept safe, and you are keeping this room safe, and handing the heavy thing to your adult is the strong, faithful move — never a failure. The card in your hands tonight has all three. Carry it when you lead."*''',
 '''*"Those three rules never bend — not for experience, not for ordination, not for a night when we are short-handed. Team: when you keep these rules, you are not being kept small. You are being kept safe, and you are keeping every room you will ever hold safe. The card in your hands tonight has all three. Carry it when you lead."*'''),
]
for old, new in more:
    n = s.count(old)
    if n != 1:
        print(f'!! (more) count={n}: {old[:64]}'); fail += 1; continue
    s = s.replace(old, new)

# Block 5 rewrite — the covering named
i = s.index('Each new FC1 names, aloud, the adult they will call')
j = s.index('## **Block 6 — The Commissioning')
new_b5 = '''The covering is named at two levels, and neither is discovered tonight. The exit discernment — the covering and the convening leader reading the year together — happened in Week 13's week; tonight is public confirmation, not decision.

## Script (the frame)

*"A Companion team never serves uncovered. Two coverings are named tonight, out loud, because a covering that is public is a covering that holds."*

## The church's covering (≈ 3 min)

**1. The pastor or elders stand.** The convening leader: *"[Name(s)], this cohort has walked the year you blessed at its beginning. The discernment is yours: does the church send this team?"*

**2. The covering speaks it plainly** — in their own words, brief: that they have watched the year, that they take spiritual authority over the family year this team will lead, and that the church sends them. This is the moment the leadership-first challenge was pointed at from its first evening; give it the room's full weight.

**3. The convening leader confirms:** *"And I confirm it — the year has shown what it has shown, and it is enough."*

## Per Companion (≈ 60 sec each)

**1. Each member stands and says it plainly:** *"When I am over my head, I call \\_\\_\\_\\_\\_."* Name, and relationship — the convening leader, a fellow Companion, the pastor, a mentor. If the covering person is in the room, they stand where they are.

**2. The member writes the covering name on their Commissioning Card (H15.1), there in the circle.** Ink, not intention.

### **Contingency — a member whose discernment landed elsewhere**

This was handled privately in Week 13's week; it never surfaces as news tonight. The year reads people honestly, and some members' year said: not session-leading — hosting, watching, praying, scribing, the roles the family year needs as much as it needs leaders. That member was told, with warmth and a plan, what tonight will and will not include for them. Tonight, in Block 6, the convening leader honors them by name and specifically for what they carried this year — the blessing they receive is as real as anyone's — and their role in the family year is named with the same dignity as any other. A discernment that can say not-this-role is the only kind whose yes means anything — handled rightly, this member leaves the room honored and placed, not exposed.

'''
s = s[:i] + new_b5 + s[j:]

more2 = [
('The blessing block. The Week 14 discipline governs: specific, witnessed, true — not generic praise. The room watched these seniors lead for fifteen weeks; the blessings draw on what was actually seen.',
 'The blessing block. The Week 14 discipline governs: specific, witnessed, true — not generic praise. The room watched this cohort lead for a year; the blessings draw on what was actually seen.'),
('**1. The senior stands in the center.** Their family stands behind them.',
 '**1. The member stands in the center.** Their household stands behind them.'),
('**2. Two Companions speak their prepared blessings** — one to three sentences each, drawn from specific moments of leading: the container re-established when the room heated up, the feedback received and visibly acted on, the heavy moment handed to the adult without heroics. What we saw; what we bless; what we see coming.',
 '**2. Two fellow members speak their prepared blessings** — one to three sentences each, drawn from specific moments of the year: the container re-established when the room heated up, the feedback received and visibly acted on, the heavy moment handed across without heroics. What we saw; what we bless; what we see coming.'),
('**3. The parent may add one sentence.** One. It will be the one the teen remembers.',
 '**3. A household member may add one sentence.** One. It will be the one they remember.'),
('**4. The cohort speaks the Aaronic blessing over the new FC1** — the whole room, slowly, hands extended:',
 '**4. The room speaks the Aaronic blessing over the new Companion** — the whole room, slowly, hands extended:'),
('**5. The Lead Companion hands them their Commissioning Card and Limits Card:** *"[Name], the team commissions you as Formation Companion, Level One. Serve the body. Keep the rules. Call your covering. Watch the signs."* The senior returns to the circle — not to a seat apart. In the body.',
 '**5. The covering hands them their Commissioning Card and Limits Card:** *"[Name], the church commissions you as a Formation Companion. Serve the body. Keep the rules. Call your covering. Watch the signs."* The member returns to the circle — not to a seat apart. In the body.'),
("*The Lead Companion, plainly. This is a grandfather's charge; read it slowly or say it in your own words, but keep it brief and keep it true.*",
 "*The convening leader, plainly. This is a grandfather's charge; read it slowly or say it in your own words, but keep it brief and keep it true.*"),
('*"So here is the charge. Keep your own walk first — you cannot lead anyone where you have not been, and FC1 begins with your own four Connects, not your protocol card. Keep the three rules when no one is checking. Call your covering early, not late. And keep the lens we gave you in the Lab: watch for the costly telling, watch what a room does when load arrives, and go after the one who goes quiet. Those three signs are how a shepherd sees, and from tonight, seeing is part of your work."*',
 '*"So here is the charge. Keep your own walk first — you cannot lead anyone where you have not been, and a Companion begins with their own four Connects, not their protocol card. Keep the three rules when no one is checking. Call your covering early, not late. And keep the lens this year gave you: watch for the costly telling, watch what a room does when load arrives, and go after the one who goes quiet. Those three signs are how a shepherd sees, and from tonight, seeing is part of your work."*'),
('*"And hear this last thing, because the world will tell you otherwise. FC1 is not a step you are meant to hurry past. It is a real and honorable place to stand. If you stand at FC1 for the rest of your life and lead a faithful group, you have arrived, not stalled. Some of you will go further — there is a horizon past this, and some of you will one day run this whole journey in a dorm room with no adult anywhere in sight, and that is years of formation from now, and we will walk it with you. But tonight, do not look past the thing you are being given. Let no one despise you for your youth. Set the example. Begin."*',
 '*"And hear this last thing, because the world will tell you otherwise. Companion is not a title you are meant to hurry past toward something larger. It is a real and honorable place to stand. If you hold a faithful room for the rest of your life and never once stand on a platform, you have arrived, not stalled. Some of this work will go further — there is a horizon past this, rooms we cannot see from here, and we will walk toward it together. But tonight, do not look past the thing you are being given. Shepherd the flock that is among you. Set the example. Begin."*'),
]
for old, new in more2:
    n = s.count(old)
    if n != 1:
        print(f'!! (more2) count={n}: {old[:64]}'); fail += 1; continue
    s = s.replace(old, new)

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W15 part 1: {len(E)+len(more)+len(more2)} edits + 2 block rewrites, {fail} failures')
sys.exit(1 if fail else 0)
