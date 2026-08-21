# GS Week 15 part 3: blocks 7-8, differentiation, practice, debrief, handouts.
import io, sys, re
f = 'docs/getting-started/week-15-commissioning.md'
s = io.open(f, encoding='utf-8').read()
fail = 0
def sub(old, new, label=''):
    global s, fail
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {(label or old)[:60]}'); fail += 1; return
    s = s.replace(old, new)

sub('*The Lead Companion reads the first line of each rule; the seniors, together, may read them back — decide in the team meeting which way carries more weight for this group.*',
    '*The convening leader reads the first line of each rule; the cohort, together, may read them back — decide in the team meeting which way carries more weight for this group.*')
sub('## Per senior (≈ 4–5 min)', '## Per Companion (≈ 4–5 min)')
sub('## **Block 7 — The First Lab Scheduled (7:45–7:50, 5 min) — MOVEMENT FOUR, part two**',
    '## **Block 7 — The Family Year Dated (7:45–7:50, 5 min) — MOVEMENT FOUR, part two**')
sub('*"The first Leader Lab of the spring serving cycle is [day], [date], at [time], at [place]. New FC1s, that is your gathering — the Lab rhythm you have known all fall continues, now as serving leaders in the new cycle. Write it down now. Your assignment for Lab 1 is already set: bring one vital-signs observation from this room, tonight — something you saw with the lens you were just charged with."*',
    '*"The family year begins [day], [date] — the first permission conversations, and the opening night behind them. New Companions, that is your work now — the rhythm you have known all year continues, turned outward. Write it down now. Your assignment for the first planning call is already set: bring one vital-signs observation from this room, tonight — something you saw with the lens you were just charged with."*')
sub("The reserved senior closes the container from memory — the full protocol: the standing circle, the one-word landing, the one thing, the one practice, the blessing round, the closing prayer and sending. The rite that opened in a senior's voice ends in a senior's voice. That symmetry is the design: the last words of Getting Started are spoken by the generation it raised.",
    "The reserved member closes the container from memory — the full protocol: the standing circle, the one-word landing, the one thing, the one practice, the blessing round, the closing prayer and sending. The rite that opened in a member's voice ends in a member's voice. That symmetry is the design: the last words of Getting Started are spoken by the team it formed.")
sub("*Lead Companion: resist the urge to add anything after the senior's sending. If the senior sends the room, the room is sent. The final word of the series belongs to a new FC1, and the team's silence after it is the loudest confirmation in the room.*",
    "*Convening leader: resist the urge to add anything after the member's sending. If they send the room, the room is sent. The final word of the series belongs to a new Companion, and the silence after it is the loudest confirmation in the room.*")
sub('*One note for the closing senior, given privately beforehand: in the blessing round, expect the room to bless you and your fellow FC1s more than usual. Receive it. Then finish the protocol. Ending well under a full heart is the most FC1 thing you will do all night.*',
    '*One note for the closing member, given privately beforehand: in the blessing round, expect the room to bless you and your fellow Companions more than usual. Receive it. Then finish the protocol. Ending well under a full heart is the most Companion-like thing you will do all night.*')
sub("The keepsake sheets (H15.3) are on the side table with pens. As the room lingers over dessert, everyone — cohort, parents, siblings, Companions — signs each new FC1's keepsake, the way you sign a Bible flyleaf. Names, not messages; the charge and the blessing are already printed, and the names are the witnesses. Teens keep these for decades. Do not let anyone leave without signing.",
    "The keepsake sheets (H15.3) are on the side table with pens. As the room lingers over dessert, everyone — cohort, households, guests — signs each new Companion's keepsake, the way you sign a Bible flyleaf. Names, not messages; the charge and the blessing are already printed, and the names are the witnesses. People keep these for decades. Do not let anyone leave without signing.")
sub("Stay. Some families will not leave for an hour. The work after the closing is sometimes the work — tonight more than ever, because the younger teens who watched with hunger will be the ones lingering near the seniors, and what they say to each other at the dessert table is the pipeline forming in real time.",
    "Stay. Some households will not leave for an hour. The work after the closing is sometimes the work — tonight more than ever, because the guests who watched with hunger will be the ones lingering near the new Companions, and what they say to each other at the dessert table is the next cohort forming in real time.")

# Differentiation section
i = s.index('## **The new FC1s**')
j = s.index('# **Closing Practice in Detail**')
new_diff = '''## **The new Companions**

- Each knows their exact final-rep slot before the night. Rehearsed dignity, never ambush.
- Each has decided their covering name before the night. The public naming confirms; it does not discover.
- If a member is a naturally quiet leader, their condition-story in Block 2 can be two sentences. Fluency is not volume.

## **The households and guests**

- They witness — and some of them are watching their own future. Say one sentence to them from the front in Block 7: *"Some of you watching tonight will one day stand where this team is standing. Watch how they begin."* No promises, no selection talk; just the door left visibly open.
- In the blessing round of the close, guests often bless the new Companions in ways the cohort cannot. Give the round room.
- A household member gets one sentence in the blessing block — the discipline protects them from the speech they may want to give and preserves the sentence the Companion will keep.

## **The covering**

- The confirming word in Block 5 is theirs, and it carries the night. Some coverings will need to hear beforehand that a few plain sentences spoken with authority carry more than a homily.
- The covering hands the cards in Block 6. The church's hands, not the curriculum's.

## **The room as witnesses**

- Nobody tonight is a spectator; they are the witnesses the rite requires. The Aaronic over each Companion belongs to the whole room, and the keepsake signing includes every hand present.

'''
s = s[:i] + new_diff + s[j:]

sub("The three-layer closing pattern of the series runs one last time — and for the first time, all of it is in a senior's hands. The landing word, the one thing, the one practice, the blessing round, the sending: the closing senior holds the whole shape from memory. The team's discipline is to let them. The container was the first thing the seniors ever led, back in the fall; it is the right thing for them to lead last.",
    "The three-layer closing pattern of the series runs one last time — all of it in a member's hands. The landing word, the one thing, the one practice, the blessing round, the sending: the closing member holds the whole shape from memory. The team's discipline is to let them. The container was the first thing this cohort ever led; it is the right thing for them to lead last.")
sub('## For the new FC1s — the Leader Lab rhythm begins',
    '## For the new Companions — the family year begins')
sub("- Come to Lab 1 of the serving cycle on the announced date with **one vital-signs observation from tonight's room**: a costly telling you noticed, what the room did in the first ten seconds when weight arrived, or someone going quiet and who moved toward them. One observation, seen with the lens from the charge. This is the first rep of the FC1's ongoing work: watching a room like a shepherd, never scoring it.",
    "- Come to the first planning call on the announced date with **one vital-signs observation from tonight's room**: a costly telling you noticed, what the room did in the first ten seconds when weight arrived, or someone going quiet and who moved toward them. One observation, seen with the lens from the charge. This is the first rep of a Companion's ongoing work: watching a room like a shepherd, never scoring it.")
sub("- Keep your own four-Connects rhythm going. The Lab's last word stands: you cannot lead from an empty well.",
    "- Keep your own four-Connects rhythm going. The year's last word stands: you cannot lead from an empty well.")
sub('### **The new FC1s — the honest read**', "### **The new Companions — the honest read**")
sub('- For each new FC1: what did the rite confirm about their readiness, and what did it surface? Where is each one strong — container, process, blessing, the handing reflex — and what is the one growth edge the spring serving cycle should work first?',
    '- For each new Companion: what did the rite confirm about their readiness, and what did it surface? Where is each one strong — container, process, blessing, the handing reflex — and what is the one growth edge the family year should work first?')
sub('- Write a short coaching plan per FC1 for the serving cycle: which slots they lead next, what the Lab should give them, what their covering person should know to watch for. Three sentences each is enough; the point is that the team is still forming them, and commissioning was the start of that, not the end.',
    '- Write a short growth plan per Companion for the family year: which sessions they lead first, what the planning rhythm should give them, what their covering person should know to watch for. Three sentences each is enough; the point is that the team keeps forming itself, and commissioning was the start of that, not the end.')
sub("- If a senior's commissioning was deferred to the next cycle: how did tonight land for them and their family? What is the specific, dated path to their commissioning, and who owns walking it with them?",
    "- If a member's discernment landed on a different role: how did tonight land for them and their household? Is their place in the family year named, dated, and dignified — and who owns walking it with them?")
sub("- Which younger teens watched with hunger? Name them. They are the next cycle's Companions-in-Formation forming in front of us — the fourth generation in the verse. No approaches yet; just names, noted, prayed over, and revisited when the next cycle's discernment begins.",
    "- Which guests watched with hunger? Name them. They are the next cohort forming in front of us — the fourth generation in the verse. No approaches yet; just names, noted, prayed over, and revisited when the next cohort's discernment begins.")
sub("- What did the parents of non-senior teens say afterward? A commissioning like this recruits the imagination of a whole community, or fails to. Which was it?",
    "- What did the households say afterward? A commissioning like this recruits the imagination of a whole community, or fails to. Which was it?")
sub("- The pilot's discovery, in the handbook's words: when a teenager stood up and led their peers, the rest of the room leaned in like nothing else. Did it happen again tonight? Where exactly — the final rep, the covering, the closing? Write it down; this is the observation the whole FC1 track is built on, and every cycle either confirms it or corrects it. Bring it to John for the IJH project.",
    "- The prototype's discovery: when one of the room's own stood up and led, the rest of the room leaned in like nothing else. Did it happen again tonight? Where exactly — the final rep, the covering, the closing? Write it down; this is the observation the whole rotation is built on, and every cycle either confirms it or corrects it. Send it back to the project.")
sub("- Was tonight a gate or a ceremony, honestly? The test is not how it felt at 8:00 PM; the test is who shows up to Lab 1. Put the Lab 1 attendance question on the next team agenda now.",
    "- Was tonight a gate or a ceremony, honestly? The test is not how it felt at 8:00 PM; the test is who shows up to the first planning call. Put that attendance question on the next team agenda now.")
sub("Three handouts for Week 15. H15.1 and H15.2 are handed to each new FC1 during the rite; H15.3 is signed by the room after the close.",
    "Three handouts for Week 15. H15.1 and H15.2 are handed to each new Companion during the rite; H15.3 is signed by the room after the close.")
sub('- H15.1 — FC1 Commissioning Card (one per senior, cardstock)', '- H15.1 — Companion Commissioning Card (one per member, cardstock)')
sub('- H15.2 — The Limits Card (Appendix I reprint, one per senior)', '- H15.2 — The Limits Card (Appendix I reprint, one per member)')
sub('- H15.3 — The Keepsake: the Charge and the Blessing (one per senior, heavy paper, signed by the room)',
    '- H15.3 — The Keepsake: the Charge and the Blessing (one per member, heavy paper, signed by the room)')
sub('**Handout H15.1 — FC1 Commissioning Card**\n\n*Cardstock. Handed to each new FC1 in the commissioning. One card they keep.*\n\n## FORMATION COMPANION, LEVEL ONE',
    '**Handout H15.1 — Companion Commissioning Card**\n\n*Cardstock. Handed to each new Companion in the commissioning, by the covering. One card they keep.*\n\n## FORMATION COMPANION')
sub('''## The three rules that never bend

1. **A Companion-in-Formation never counts as one of the two adults.** The supervision rule is unchanged. "Co-lead" means an adult Companion in the room — not nearby, in the room.
2. **A Companion-in-Formation never takes a disclosure.** If something heavy surfaces while they are leading, their only job is to hand it to the adult immediately. They are not a junior counselor.
3. **Lead only a block you have first received.** See it, then lead it. Never lead a process you have not first experienced as a participant.''',
    '''## The three rules that never bend

1. **Two Companions, always.** Nobody on this team holds a disclosure, a crisis, or a closed door alone.
2. **Hand what belongs to the qualified across the line.** This work may be therapeutic; it is not therapy. The door out and the referral list are yours to keep real.
3. **Lead only a block you have first received.** See it, then lead it. Never lead a process you have not first experienced as a participant.''')
sub('## What an FC1 can do', '## What a Companion can do')
sub('- Know the edge of FC1 — what they can hold, and what they must hand to an adult — and do the handing without hesitation or heroics.',
    '- Know the edge — what they can hold, and what they must hand across the line — and do the handing without hesitation or heroics.')
sub('*FC1 is a real and honorable place to stand. A teen who stays at FC1 for the rest of their life and leads a faithful group has arrived, not stalled.*',
    '*Companion is a real and honorable place to stand. One who holds a faithful room for the rest of their life has arrived, not stalled.*')
sub('**Commissioned:** \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ (date) — *in the presence of many witnesses (2 Tim. 2:2)*',
    '**Commissioned by the church:** \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ (date) — *in the presence of many witnesses (2 Tim. 2:2)*')
sub('## The serving cycle begins\n\n**First Leader Lab: \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ (date, time, place)** — bring one vital-signs observation from commissioning night.',
    '## The family year begins\n\n**First date: \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ (date, time, place)** — bring one vital-signs observation from commissioning night.')

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W15 part 3: done, {fail} failures')
res = re.findall(r'\b(teens?|parents?|seniors?|juniors?|FC1s?|Lab)\b', s)
print('remaining role words:', res)
sys.exit(1 if fail else 0)
