# GS Week 1 adult re-authoring. Exact-match edits; loud failures.
import io, sys
f = 'docs/getting-started/week-01-welcome.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new):
    E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')

# WATCH FOR
R('- First-night nerves. Some teens will be there because Mom said. That is fine. Do not pressure them to engage beyond their willingness in Week 1.',
  '- First-night nerves. Some members will be there because the pastor asked and they did not feel free to say no. That is fine. Do not pressure them to engage beyond their willingness in Week 1.')
R('- Parents trying to chaperone. The first time you see a parent moving toward managing their kid, gently redirect. “Tonight we are all participants. Let me hold the space.”',
  '- Members sliding into staff mode. The first time you see a leader start running the room — watching the door, managing the evening, hosting — gently redirect. “Tonight we are all participants. Let me hold the space.”')

# Dependencies / orientation
R('**Dependencies.** Week 1 depends only on the Family Orientation Night having happened.',
  '**Dependencies.** Week 1 depends only on the entry gate having been passed: the covering’s blessing given, the year on the calendar, the covenant signed.')
R('The Family Orientation Night two weeks earlier was the real on-ramp.',
  'The covering conversation and the entry gate were the real on-ramp.')

# Pre-work
R('### For parent-and-teen, separately (5 minutes, in the car on the way)\n\nParent and teen do not coordinate on this. Each, separately, finishes this sentence in their own head:',
  '### For every member, privately (5 minutes, on the way)\n\nDo not compare notes with anyone. Each member, separately, finishes this sentence in their own head:')

# Materials
R('- Aaronic blessing card — one per family — see Handout H1.2.',
  '- Aaronic blessing card — one per member — see Handout H1.2.')

# Prep timeline + run sheet lead labels
R('| T-15 min | Door opens. One Co-Companion at the door welcoming, handing out name tags, pointing to the phone-box. | Co-Comp (Teen) |',
  '| T-15 min | Door opens. One Co-Companion at the door welcoming, handing out name tags, pointing to the phone-box. | Co-Comp |')
R('| 6:45 | Door opens. Greet, name tags, phone-box, light snacks. | Open | Teen Comp | 15 |',
  '| 6:45 | Door opens. Greet, name tags, phone-box, light snacks. | Open | Co-Comp | 15 |')
R('| 8:05 | Between-session practice introduced. | Shared | Parent Comp | 5 |',
  '| 8:05 | Between-session practice introduced. | Shared | Co-Comp | 5 |')

# Block 1 script
R('“Two. This is not a youth group with parent permission. Every single person in this room — teens, parents, all of us — is here as a participant. There are no chaperones tonight. There are no observers. We are all in this.',
  '“Two. Nobody in this room is on duty tonight. Every single person here — pastor, elder, veteran, newcomer — is a participant. There are no staff tonight. There are no observers. We are all in this.')
R('Watch for: parents who try to keep their phones for “emergencies.” If asked, say: “Your spouse and your school have the building’s number. If something is on fire, someone will come and get you. The phone goes in the box.”',
  'Watch for: members who keep their phones for “church emergencies.” If asked, say: “The church has the building’s number. If something is truly on fire, someone will come and get you. The phone goes in the box.”')

# Block 2 script
R('“Here’s what this is. This is a structured chance to do real interior work as a family and as a community.',
  '“Here’s what this is. This is a structured chance to do real interior work as a team and as a community.')
R('It isn’t a youth group where you play games and have a snack and go home. It isn’t therapy.',
  'It isn’t a leadership seminar where you take notes on something you will administer to other people. It isn’t therapy.')

# Block 3 watch-for
R('Watch for: junior teens checking out during teaching. Use vivid, concrete language. “Your neighbor knowing your interior life” — not abstract. “The person sitting at your lunch table at school knowing what’s actually going on inside you” — concrete.',
  'Watch for: the room checking out during teaching — adults do it politely, which makes it harder to see. Use vivid, concrete language. “Your neighbor knowing your interior life” — not abstract. “The person who serves beside you every Sunday knowing what’s actually going on inside you” — concrete.')

# Block 4 container script
R('The teen knows they will not be embarrassed. The parent knows they will not be made fun of. The kid knows the parents won’t fix them. The parent knows the kids won’t roll their eyes.',
  'The newest member knows they will not be embarrassed. The pastor knows this room is not evaluating the pastor. Nobody gets fixed. Nobody gets managed.')
R('“Clear means there’s nothing unaddressed between people in the room. If you and your daughter had a fight in the car on the way over, you don’t have to fix it now — but you do have to silently set it down so you can be present. Same for kids and parents. Same for friends. Same for any of you who are mad at me about something I haven’t addressed yet.',
  '“Clear means there’s nothing unaddressed between people in the room. If two of you carried a hard conversation in the door — a church matter, a family matter, a decision that did not go your way — you don’t have to fix it now, but you do have to silently set it down so you can be present. Same for any two of you with unfinished business. Same for any of you who are mad at me about something I haven’t addressed yet.')

# Block 5 OTS
R('“If you’re here because Mom said you had to be, that is a true sentence. Say that.',
  '“If you’re here because the pastor asked and you didn’t feel free to say no, that is a true sentence. Say that.')
R('- “I’m here because at fifteen I needed someone to ask me what I actually thought about God, and nobody did, and I’d like to be that for the kids in this room.”',
  '- “I’m here because years ago I needed someone to ask me what I actually thought about God, and nobody did, and I want this church to become the place where somebody asks.”')
R('''- Junior teens may freeze. Have a small sentence stem ready: “One reason I’m here tonight is \\_\\_\\_.” Offer it gently if a 12-year-old goes silent for more than 5 seconds.
- Senior teens may try to be funny or deflect. Honor it briefly, then gently: “Is there a true sentence under that one?”
- Parents may try to give a speech. After the second sentence, hold up two fingers gently — “one sentence.”''',
  '''- Someone may freeze. Have a small sentence stem ready: “One reason I’m here tonight is \\_\\_\\_.” Offer it gently if the silence passes five seconds.
- Someone may go funny or deflect. Honor it briefly, then gently: “Is there a true sentence under that one?”
- Someone will begin a small sermon — the polished, pulpit-ready sentence is the adult deflection. After the second sentence, hold up two fingers gently — “one sentence.”''')

# Block 7
R('**Co-Companion (Parent) leads this block.** It is important that the parent Co-Companion introduce this practice, because the parents need to hear that they are doing it too.',
  '**A Co-Companion leads this block, not the convening leader.** The room needs to hear, from the first week, that this year is carried by more than one voice — and that everyone, the convening leader included, is doing the practice too.')
R('That’s it. Five minutes morning, one minute evening, every day. Parents, you are doing this too. We’ll check in next week.”',
  'That’s it. Five minutes morning, one minute evening, every day. All of us are doing this — the whole team, the convening leader included. We’ll check in next week.”')

# Block 9 Aaronic
R('“Teens, turn and face your parent. Parents, place a hand on your teen’s shoulder if they’re comfortable with that. Read it together with me, looking at the person in front of you.”',
  '“Turn and face the person beside you. Place a hand on their shoulder if they’re comfortable with it. Read it together with me, looking at the person in front of you.”')

# Differentiation Notes — full rewrite of the three cohort sections
R('''## Junior cohort (12–14)

- Speak in concrete examples, not abstractions. Instead of “interior life,” say “what’s actually going on inside your head when you’re lying in bed at night.”
- Watch for the 12-year-old who freezes during “one true sentence.” Be ready with the sentence stem.
- Honor passing without ceremony — do not make a 12-year-old feel like passing was a failure. “Thanks. We’re glad you’re here” and move on.
- Eye contact matters. Junior teens read your face more than your words. If you are stressed or rushed, they will mirror it.

## Senior cohort (15–18)

- Senior teens will test you. They want to see if you actually mean what you say about safety, judgment, and being real. The first deflective or sarcastic comment in the circle is a test. Honor it briefly, then gently invite the truth underneath.
- Senior teens may pre-write polished sentences. The first time you hear one, gently: “That’s a great sentence. What’s the truer one underneath it?”
- Senior teens are watching their parents to see how the parents engage. If the parents are real, the teens will be real. If the parents are performing, the teens will perform.
- Several seniors will be self-conscious about the parallel-circles design starting in Week 2. Acknowledge it tonight: “We’ll be in separate circles for some of the work starting next week. That is on purpose. Trust the design.”

## Parents

- The parent’s biggest temptation tonight is to slide into chaperone mode. Catch it early. “Tonight you’re a participant. Let me hold the room.”
- Some parents will be doing this kind of work for the first time in their lives. Do not assume sophistication.
- If a parent gives a polished testimony for their “one true sentence,” the gentle redirect is the same: “What’s the truer one underneath it?”
- Some parents will be more advanced than the Companion team. Do not be intimidated. The container holds for them too.''',
  '''## Those doing this work for the first time

- Speak in concrete examples, not abstractions. Instead of “interior life,” say “what’s actually going on inside your head when you’re lying awake at night.”
- Watch for the member who freezes during “one true sentence.” Be ready with the sentence stem, and honor passing without ceremony — “Thanks. We’re glad you’re here” and move on.
- Years of church service are not the same as this kind of work. Do not assume sophistication, and do not let anyone feel behind for lacking it.

## The veterans

- Seasoned leaders will test you — politely. They want to see if you actually mean what you say about safety, judgment, and being real. The first deflective or wry comment in the circle is a test. Honor it briefly, then gently invite the truth underneath.
- Veterans pre-write polished sentences without knowing it. The first time you hear one, gently: “That’s a great sentence. What’s the truer one underneath it?”
- The room is watching the veterans to see how they engage. If the most senior people are real, the room will be real. If they perform, the room will perform. This is the leader-tells-first engine working in the open — say so at the team debrief, not to the room.
- Several members will be self-conscious about the circles design starting in Week 2. Acknowledge it tonight: “We’ll be in smaller circles for some of the work starting next week. That is on purpose. Trust the design.”

## The ordained and the staff

- The strongest temptation tonight is to slide into staff mode — hosting, managing, watching the room instead of being in it. Catch it early. “Tonight you’re a participant. Let me hold the room.”
- A pastor’s “one true sentence” may arrive as a small homily. The gentle redirect is the same: “What’s the truer one underneath it?”
- Some members will be more practiced at this work than the convening leader. Do not be intimidated. The container holds for them too.''')

# Closing practice layer 3
R('Spoken parent-to-teen and teen-to-parent. Use Numbers 6:24–26. The card goes home with each family. Several families will keep this card on their fridge through the whole series; that is part of the design.',
  'Spoken member to member, face to face. Use Numbers 6:24–26. The card goes home with each member. Several will keep it on the fridge through the whole series; that is part of the design.')

# Debrief prompts
R('- At least one parent said something more honest than they expected to.',
  '- At least one seasoned leader said something more honest than they expected to.')
R('- Parents tried to manage their teens during the session.',
  '- Someone slid into staff mode and ran the room instead of joining it.')
R('- If parents tried to manage teens, name it gently in Week 2 once — then enforce by redirection on the moment.',
  '- If staff mode showed up, name it gently in Week 2 once — then enforce by redirection in the moment.')
R('''- Anyone who said something heavier than expected during “one true sentence” — gentle 1:1 contact within 48 hours. Two adults present if a teen.
- Any teen who froze and could not say a sentence at all — informal contact, not formal. Sometimes a 12-year-old just needs to know you remember they were there.
- Any parent who seemed defensive or dismissive — informal contact from the parent Co-Companion before Week 2. “How did Tuesday land for you?”''',
  '''- Anyone who said something heavier than expected during “one true sentence” — gentle 1:1 contact within 48 hours, per the host church’s care practice.
- Anyone who froze and could not say a sentence at all — informal contact, not formal. Sometimes a person just needs to know you remember they were there.
- Anyone who seemed defensive or dismissive — informal contact from a Co-Companion before Week 2. “How did it land for you?”''')

# Handout H1.2
R('*Print on cardstock, one per family. Cut to wallet or fridge size.*',
  '*Print on cardstock, one per member. Cut to wallet or fridge size.*')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}')
        fail += 1
        continue
    s = s.replace(old, new)
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W1: {len(E)} edits, {fail} failures')
sys.exit(1 if fail else 0)
