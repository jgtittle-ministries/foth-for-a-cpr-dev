# GS Week 3 adult re-authoring.
import io, sys
f = 'docs/getting-started/week-03-story.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')

# QRC
R('**Between-session practice.** The Joint Footprints exercise: each parent and teen pair sits together once this week and walks each other through the footprints question. Twenty minutes total.',
  '**Between-session practice.** The Shared Footprints exercise: each member sits once this week with their spouse or one person close to them and they walk each other through the footprints question. Twenty minutes total.')

# WATCH FOR
R('- Unanticipated crisis disclosures. This is the session where they happen if they happen. Suicidal ideation, self-harm, eating disorders, abuse history, parental violence, addiction in the household. Section 6 of the Handbook is the protocol; have it printed in the room.',
  '- Unanticipated crisis disclosures. This is the session where they happen if they happen. Suicidal ideation, self-harm, abuse history, violence, addiction in the household. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy) is the protocol; have it printed in the room.')
R('- Fixing in the listener role. Teens — and parents — will want to fix, advise, or relate-back. The listener role is to receive and bless. That is the practice.',
  '- Fixing in the listener role. Leaders most of all will want to fix, advise, or relate-back — it is what they are practiced at. The listener role is to receive and bless. That is the practice.')
R('- Parent stories that name family events the teen is processing in another room. Plan in advance for parents whose stories may need to be sequenced with what their teen is hearing or telling.',
  '- Stories that interweave. Spouses in the same cohort, staff who share a history, elders who lived the same church season — plan circle assignments in advance so nobody tells a story about someone sitting three feet away.')
R('- First time the cohort circles have run without the Lead Companion in them. Each cohort circle needs an experienced Co-Companion.',
  '- First time the circles have run without the convening leader in them. Each circle needs a prepared Co-Companion.')

# CRISIS CONTINGENCIES
R('**Week 3 is the highest-probability session for crisis disclosures. Every Companion in every circle reads Handbook Section 6 within the 48 hours before this session, not as review but as preparation.**',
  '**Week 3 is the highest-probability session for crisis disclosures. Every Companion in every circle reads the safeguarding frame (Leadership Year Handbook §7 and the host church’s policy) within the 48 hours before this session, not as review but as preparation.**')
R('**If a participant discloses suicidal ideation.** Stay in the circle. Do not move them out alone. At the end of the block, the Cohort Companion and one other Companion (two-adult rule) walk with them to a private space. The pastoral / clinical backup is called within the hour. Parents are notified per Handbook §6 protocol.',
  '**If a participant discloses suicidal ideation.** Stay in the circle. Do not move them out alone. At the end of the block, the circle Companion and one other Companion (two adults, always) walk with them to a private space. The pastoral / clinical backup is called within the hour, and the door out is real that same night.')
R('**If a teen discloses abuse.** Affirm them in the circle. Do not interrogate. Do not promise confidentiality. After the session, the Cohort Companion and the Lead Companion step aside with the teen. Mandatory reporting timeline begins within 24 hours per Virginia Code §63.2-1509.',
  '**If a member discloses abuse — their own history, or harm involving a minor.** Affirm them in the circle. Do not interrogate. Do not promise confidentiality you cannot keep: a disclosure involving a minor may carry mandatory-reporting duties for some in the room, and the host church’s policy and counsel govern the timeline. After the session, the circle Companion and the convening leader step aside with the member.')

# Session at a glance / why
R('The work of Week 3 is double. First, that each participant practices being known by a few specific people — a thing many of them have never done. Second, that each participant practices being a listener who blesses rather than fixes — a thing all of them have to learn. Both halves are the practice.',
  'The work of Week 3 is double. First, that each participant practices being known by a few specific people — a thing many leaders have never done, however long they have served. Second, that each participant practices being a listener who blesses rather than fixes — the discipline leaders find hardest, because fixing is their trade. Both halves are the practice.')
R('This is the first session in which the cohort circles run independently of the Lead Companion. Each cohort circle is held by a Co-Companion who has prepared. The Lead Companion floats; the role is to notice rather than to lead.',
  'This is the first session in which the circles run independently of the convening leader. Each circle is held by a Co-Companion who has prepared. The convening leader floats; the role is to notice rather than to lead.')
R('- Week 2: cohort circles have functioned once. The lift this week is that each cohort circle now runs longer and with deeper material. If Week 2’s circles were unsteady, slow Week 3’s opening to re-anchor before splitting.',
  '- Week 2: the circles have functioned once. The lift this week is that each circle now runs longer and with deeper material. If Week 2’s circles were unsteady, slow Week 3’s opening to re-anchor before splitting.')

# Pre-work
R('Before this session, the Lead Companion and every Cohort Companion writes out their own four-question story. Not to read aloud — to know it. The teens will know within thirty seconds whether their Companion has done this work.',
  'Before this session, the convening leader and every circle Companion writes out their own four-question story. Not to read aloud — to know it. The room will know within thirty seconds whether its Companion has done this work. This is the engine at its most literal: the leader tells first, and the telling is only as real as the private writing behind it.')
R('2. Each Cohort Companion names the participants in their circle and identifies one or two who they are watching for. “Watching for” is not predicting harm; it is noticing who has been quieter, who hinted at hard material in Week 2, who emailed the Lead Companion this week.',
  '2. Each circle Companion names the participants in their circle and identifies one or two who they are watching for. “Watching for” is not predicting harm; it is noticing who has been quieter, who hinted at hard material in Week 2, who emailed the convening leader this week.')
R('1. Re-read Handbook Section 6 in full. Out loud. Together.',
  '1. Re-read the safeguarding frame in full. Out loud. Together.')
R('''1. Confirm cohort circle assignments. Junior teens (12–14) in one circle. Senior teens (15–18) in one or two circles depending on size. Parents in one circle.
2. If the senior teen group is over six, split into two senior circles and assign two Co-Companions. Six is the upper bound for a story circle that can finish in forty minutes.
3. Print the three storytelling cards (junior / senior / parent), the listener’s role card, and the joint footprints handout. See handouts at the back of this document.
4. Confirm that each cohort circle has a separate physical space that is private (no door windows; no traffic). Map it before the night of.''',
  '''1. Confirm circle assignments in advance — circles of four to five, composition per the host church’s call, arranged so no story lands on the person it is about.
2. If a circle would exceed six, split it and assign another Co-Companion. Six is the upper bound for a story circle that can finish in forty minutes.
3. Print the storytelling card, the listener’s role card, and the Shared Footprints handout. See handouts at the back of this document.
4. Confirm that each circle has a separate physical space that is private (no door windows; no traffic). Map it before the night of.''')

# Materials
R('''- Storytelling cards: H3.1 junior version, H3.2 senior version, H3.3 parent version. One per participant in their cohort.
- Listener’s role card: H3.4. One per participant, all cohorts.
- Joint footprints handout: H3.5. One per family.
- Three private spaces for cohort circles — a separate room or clearly bounded section per cohort. Chairs in each room set in a small tight circle.
- Tissues in every cohort space.''',
  '''- Storytelling card: H3.1. One per participant.
- Listener’s role card: H3.2. One per participant.
- Shared Footprints handout: H3.3. One per member.
- A private space per circle — a separate room or clearly bounded section. Chairs in each set in a small tight circle.
- Tissues in every circle space.''')
R('- A wall clock or visible timer in each cohort space, only the Cohort Companion needs to see it.',
  '- A wall clock or visible timer in each circle space, only the circle Companion needs to see it.')
R('Open in the main room as a single circle (Weeks 1 and 2). After the bridge, each cohort moves to its own space. The Lead Companion does not have a circle; the Lead Companion floats and is reachable.',
  'Open in the main room as a single circle (Weeks 1 and 2). After the bridge, each circle moves to its own space. The convening leader does not have a circle; the convening leader floats and is reachable.')
R('In each cohort space, chairs are in a tight circle, knees almost touching. The intimacy of the geometry is intentional. There is no table in the middle. No phones. The Cohort Companion sits in the circle, not at the head.',
  'In each circle space, chairs are in a tight circle, knees almost touching. The intimacy of the geometry is intentional. There is no table in the middle. No phones. The Companion sits in the circle, not at the head.')

# Prep timeline + run sheet labels
R('| Week before | Confirm cohort assignments and room assignments. Print all handouts. Verify pastoral / clinical backup availability. | Lead Comp |',
  '| Week before | Confirm circle assignments and room assignments. Print all handouts. Verify pastoral / clinical backup availability. | Lead Comp |')
R('| T-30 min | Each Cohort Companion sets up their cohort space — chair circle, tissues, handouts at each chair, timer. | All Companions |',
  '| T-30 min | Each circle Companion sets up their space — chair circle, tissues, handouts at each chair, timer. | All Companions |')
R('| T-15 min | Door opens. Same arrival rhythm as Weeks 1–2. | Co-Comp (Teen) |',
  '| T-15 min | Door opens. Same arrival rhythm as Weeks 1–2. | Co-Comp |')
R('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags, phone-box. Lead Companion greets each participant by name. |',
  '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags, phone-box. The convening leader greets each participant by name. |')
R('| 8:17–8:21 | Block 8: Between-session practice | Shared circle | Co-Comp (Parent) | Joint Footprints assigned. Each family takes one handout. |',
  '| 8:17–8:21 | Block 8: Between-session practice | Shared circle | Co-Comp | Shared Footprints assigned. Each member takes one handout. |')

# Block 5 bridge split naming
R('*“Junior teens, you’re with [name]. Senior teens, with [name]. Parents, with [name]. Forty minutes. We come back here at 8:12. Go.”*',
  '*“[Name]’s circle, this side. [Name]’s circle, that side. Forty minutes. We come back here at 8:10. Go.”*')

# Block 6 internals
R('### Inside the cohort circle — Companion script', '### Inside the circle — Companion script')
R('**Story (5–7 minutes). The teller speaks. Nobody interrupts. Even with silence in the middle. The Cohort Companion watches the timer privately. At six minutes, if the teller is still going, gentle eye contact. At seven, gentle: “Let’s land it together.” Almost never necessary if the demo was well-modeled.**',
  '**Story (5–7 minutes). The teller speaks. Nobody interrupts. Even with silence in the middle. The Companion watches the timer privately. At six minutes, if the teller is still going, gentle eye contact. At seven, gentle: “Let’s land it together.” Almost never necessary if the demo was well-modeled.**')
R('**Blessing round (1–2 minutes total). The Cohort Companion goes first or invites the next person on the right.',
  '**Blessing round (1–2 minutes total). The Companion goes first or invites the next person on the right.')
R('## Cohort Companion: when to intervene', '## Circle Companion: when to intervene')
R('- If something heavy surfaces (suicidal ideation, abuse, family violence) — receive it in the circle. Affirm. Bless gently. Do not rush. After the circle ends, you and one other Companion step aside with the participant. Crisis protocol begins.',
  '- If something heavy surfaces (suicidal ideation, abuse, violence) — receive it in the circle. Affirm. Bless gently. Do not rush. After the circle ends, you and one other Companion step aside with the participant. The safeguarding frame begins.')
R('If you finish before 8:12, do not start a new topic. Sit with what was said. Optional: Cohort Companion offers one closing sentence.',
  'If you finish before 8:10, do not start a new topic. Sit with what was said. Optional: the Companion offers one closing sentence.')

# Block 8 practice
R('This is the first session in which the practice is explicitly relational and explicitly cross-generational. The Joint Footprints exercise is a parent-and-teen pair sitting together once during the week and walking each other through the footprints question. Twenty minutes.',
  'This is the first session in which the practice is explicitly relational and explicitly leaves the room. The Shared Footprints exercise is each member sitting once this week with their spouse or one person close to them, the two walking each other through the footprints question. Twenty minutes.')
R('''*“One practice between now and next Tuesday. Each family takes one of these handouts.” (Hold up H3.5.)*

*“Here’s what it is. Sometime between now and Tuesday, each parent and teen pair sits together for twenty minutes — not in the car, not at dinner, not while the TV is on. At a table or on a porch. Phones away.”*

*“One of you walks the other through the first question on the storytelling card — the footprints question. Just that one. Where did you grow up, who shaped you, what places and people made you who you are. Five minutes telling. The other person listens, asks one or two follow-up questions, and at the end says one sentence: ‘What I love about your footprints is...’”*

*“Then swap. The other person tells their footprints, the first person listens and blesses.”*

*“Two rules. The teen does not have to disclose anything they didn’t disclose tonight. The parent does not turn this into a lecture or a teaching moment. We are practicing what we did tonight, in our own homes, with the most important relationship in this room.”*

*“The handout has the questions and the rules in writing. Take one per family.”*''',
  '''*“One practice between now and next week. Each of you takes one of these handouts.” (Hold up H3.3.)*

*“Here’s what it is. Sometime this week, sit for twenty minutes with your spouse, or with one person close to you — not in the car, not at dinner, not while the TV is on. At a table or on a porch. Phones away.”*

*“One of you walks the other through the first question on the storytelling card — the footprints question. Just that one. Where did you grow up, who shaped you, what places and people made you who you are. Five minutes telling. The other person listens, asks one or two follow-up questions, and at the end says one sentence: ‘What I love about your footprints is...’”*

*“Then swap. The other person tells their footprints, the first person listens and blesses.”*

*“Two rules. Nobody has to disclose anything they didn’t disclose tonight. And neither of you turns it into advice or a counseling session. We are practicing what we did tonight, at home, with someone who matters.”*

*“The handout has the questions and the rules in writing. Take one each.”*''')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}')
        fail += 1
        continue
    s = s.replace(old, new)

# --- Differentiation section rewrite ---
i = s.index('# Differentiation by Cohort')
j = s.index('# Closing Practice in Detail')
new_diff = '''# Differentiation in the Circles

## Those doing this work for the first time

The four-question frame stands, but a first-timer may need the Companion’s help finding the door.

- The Companion may briefly help with prompts: “Tell us where you grew up first — the place you remember most.” Then pause and let them go.
- Watch for the member who tells the story they think the room wants to hear. Affirm specificity over polish: “The specific thing you just said — about your grandfather’s shed — that’s the gold.”
- Watch for the member who narrates someone else’s story instead of their own — a spouse’s, a child’s, a congregation’s. Gentle: “That sounds like an important part of your life. Where are *you* in this story?”
- Watch for the member who says nothing. They are listening; they are learning. Do not pressure them. They may speak in Week 6 or Week 9. Do not make Week 3 the test of their participation.

## The veterans

Veterans are old enough for the gravity of the IJH words — footprints, wounds, battles, victories — and practiced enough to need watching for polish.

- Watch for the over-discloser — the one who turns the circle into a confession. Affirm what they said and gently time-bound. “Thank you for trusting us. Let’s pause and let your circle bless you, and we’ll honor what you said by not pulling more out tonight.”
- Watch for the performative story — the testimony told so many times it has lost its blood. Affirm and ask one specific question: “What was the worst part of that for you?” Often the real story is one layer below.
- A veteran may surface material that involves another member of the cohort. The Companion does not bring it back to the room; the convening leader may follow up offline within 48 hours.

## The ordained and the staff

The ordained have the hardest task tonight. They have to tell true stories without performing competence to a room they may one day lead — or already do. The circle Companion goes first and goes honestly.

- Frame at the start, if needed: “The room this cohort leads next year is shaped by the room we sit in tonight. The most generous thing you can do for the people you serve is be honest in here.”
- Watch for the sermonizer — the story that becomes a lesson for the room. Affirm the experience and gently invite the personal: “What did that cost you, specifically?”
- Watch for the story told about the congregation — “this is why I worry about our young people.” Honor the love and gently redirect: “Tonight we’re telling our own stories. Theirs are theirs to tell.”
- If someone breaks down, slow the room. Tears in this circle in Week 3 are normal and not a problem. Often they are a turning point.

'''
s = s[:i] + new_diff + s[j:]

# --- Practice list + debrief conversions ---
more = [
('- The Joint Footprints exercise (20 min, once this week, parent-and-teen pair) — NEW this week. See Handout H3.5.',
 '- The Shared Footprints exercise (20 min, once this week, with a spouse or one close person) — NEW this week. See Handout H3.3.'),
('If a parent or teen reports back that they did not get to the Joint Footprints, this is data, not failure. Note it for the team debrief and do not shame in Week 4. The work is real even when the practice is uneven.',
 'If a member reports back that they did not get to the Shared Footprints, this is data, not failure. Note it for the team debrief and do not shame in Week 4. The work is real even when the practice is uneven.'),
('- Every participant in every cohort told a story. Even the briefest, most cautious version is success in Week 3.',
 '- Every participant in every circle told a story. Even the briefest, most cautious version is success in Week 3.'),
('- Cohort Companions report at least one moment of real disclosure in their circle — a sentence that the participant probably had not said out loud before.',
 '- Circle Companions report at least one moment of real disclosure — a sentence that the participant probably had not said out loud before.'),
('- Parents and teens left treating each other with more attention than usual. Watch the parking lot.',
 '- Members left treating each other with more attention than usual. Watch the parking lot.'),
('- The merge felt rushed or cheerful. Cheerful means the cohort circles did not actually go deep, or the Lead Companion imposed lightness on a heavy room. Both are issues.',
 '- The merge felt rushed or cheerful. Cheerful means the circles did not actually go deep, or the convening leader imposed lightness on a heavy room. Both are issues.'),
('- If a circle ran out of time, the team must reach out to the participant who did not tell within 24 hours. Offer a 1:1 with the Cohort Companion within the week.',
 '- If a circle ran out of time, the team must reach out to the participant who did not tell within 24 hours. Offer a 1:1 with the circle Companion within the week.'),
('- If a Cohort Companion was struggling, do not change them mid-series. Pair them more closely with the Lead Companion for Week 4. Reassess at the Week 8 mid-point.',
 '- If a circle Companion was struggling, do not change them mid-series. Pair them more closely with the convening leader for Week 4. Reassess at the mid-point.'),
('- Anyone who disclosed crisis-level material — within 24 hours per Section 6 protocol.',
 '- Anyone who disclosed crisis-level material — within 24 hours per the safeguarding frame.'),
('- Anyone whose parent (or whose teen) surfaced something that may resonate at home this week. Do not break confidentiality across the cohort line, but the team can pray and watch.',
 '- Anyone whose spouse or close colleague in the cohort surfaced something that may resonate at home or at church this week. Do not break confidentiality across circle lines, but the team can pray and watch.'),
('- Anyone who stayed silent in their cohort circle. Brief, warm, no pressure check-in: “How did Tuesday land for you?”',
 '- Anyone who stayed silent in their circle. Brief, warm, no-pressure check-in: “How did it land for you?”'),
('- Anyone whose Cohort Companion noticed a moment they want the Lead Companion aware of.',
 '- Anyone whose circle Companion noticed a moment they want the convening leader aware of.'),
('- If a listener offers advice or relates back — “Let’s come back to blessing. We can talk about parallels later. Right now we’re receiving.”',
 '- If a listener offers advice or relates back — “Let’s come back to blessing. We can talk about parallels later. Right now we’re receiving.” Expect this most from the most experienced pastors in the room; receive their correction of the habit as part of their formation.'),
]
for old, new in more:
    n = s.count(old)
    if n != 1:
        print(f'!! (more) count={n}: {old[:60]}')
        fail += 1
        continue
    s = s.replace(old, new)

# --- Handouts: five -> three ---
i = s.index('Five handouts for Week 3.')
j = s.index('**Handout H3.4 — Listener’s Role Card**')
new_handouts_head = '''Three handouts for Week 3. Each is on its own page below. Print as needed.

- H3.1 — Story-Telling Card
- H3.2 — Listener’s Role Card
- H3.3 — Shared Footprints (between-session practice)

**Handout H3.1 — Story-Telling Card**

*Tonight you have about six or seven minutes to tell a piece of your own story to a circle of four or five. The four questions below are a frame, not a script. Use what helps. Skip what doesn’t. Be specific where you would normally generalize.*

## 1. Footprints — the places and people that made you

**Where did you grow up? What kind of family? What was the texture of your parents’ marriage, your church, your town? Who saw you and named what was inside you? Who didn’t? What did you bring out of that childhood that you are still carrying — for good and for ill?**

## 2. Wounds — the hard places

**Where did real damage happen in your story? A parent’s absence or anger. A loss in young adulthood. A betrayal in marriage or friendship or church. A season of depression. A wound you didn’t name for years.**

*You can name the existence of a wound without giving details you don’t want in this room. Honor your own boundaries; honor the others in the circle.*

## 3. Battles — what you are fighting now

**Not abstract. What are you actually fighting now? The marriage you have versus the one you imagined. The work pressure, or the ministry’s. Aging parents. The shape of your own faith now versus the certainty you used to feel. The question of whether you have given the people you love what they actually need. Quiet despair. The deceitfulness of comfort.**

*Tell what is actually contested. The room will know if you are tidying.*

## 4. Victories — where the fruit is real

**Where has there been actual fruit in your life that you didn’t produce yourself? A character change. A repaired relationship. An overcome pattern. A capacity that was not there at twenty-five. A way you love people that you didn’t inherit and had to learn.**

## Specificity is the door

*“My parents fought” is not specific. “I grew up reading the slammed cabinet door” is. “I struggle with anxiety” is not specific. “I stopped sleeping the spring the church split, and I haven’t fully gotten that back” is. The circle can receive the second; the first leaves us nodding.*

*If you find yourself generalizing, stop and pick one specific scene, person, or moment. That’s the door into the room.*

**Handout H3.2 — Listener’s Role Card**'''
s = s[:i] + new_handouts_head + s[j + len('**Handout H3.4 — Listener’s Role Card**'):]

# H3.5 -> H3.3 rename in the tail (the Shared Footprints handout header, if present)
s = s.replace('**Handout H3.5 — Joint Footprints', '**Handout H3.3 — Shared Footprints')

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W3: {len(E) + len(more)} pair edits + 2 section rewrites, {fail} failures')
sys.exit(1 if fail else 0)
