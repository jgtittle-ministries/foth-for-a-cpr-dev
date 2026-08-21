# GS Week 2 adult re-authoring: collapse junior/senior/parent splits into
# adult circles built on the parent-circle base; one handout; table retimed
# to the woven headings (the weave missed W2's single-time table format).
import io, sys
f = 'docs/getting-started/week-02-soil.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')

# QRC
R('**Mode.** Shared teaching block, then SPLIT into three cohort circles for the diagnostic, MERGE for closing.',
  '**Mode.** Shared teaching block, then SPLIT into circles of six to eight for the diagnostic, MERGE for closing.')
R('**Center.** Heart Soil diagnostic: four gentle questions about where each kind of soil shows up in my life. Age-adapted for junior, senior, and parent cohorts. Not a test — a mirror.',
  '**Center.** Heart Soil diagnostic: four gentle questions about where each kind of soil shows up in my life, at adult depth. Not a test — a mirror.')

# WATCH FOR
R('''- The first parallel-circle split. Some seniors will be self-conscious about their parents being in another room. Frame it confidently. “You’re doing the same work. Different rooms is for honesty, not for hiding.”
- Junior teens defaulting to “social media” for everything. Push gently for one specific incident, not a category.
- Parents trying to perform competence. Honest parents this week create permission for honest teens in Week 3.
- Treating the diagnostic as a test. It is not a test. It is a mirror. Re-frame any time someone starts grading themselves.
- Surfacing material that needs more than the diagnostic can hold. If a 13-year-old says “rocky soil is when my parents fight,” that is real and may need follow-up. Note it; follow up after.''',
  '''- The first circle split. Some members will be self-conscious about colleagues being in another circle. Frame it confidently. “You’re doing the same work. Smaller circles is for honesty, not for hiding.”
- Members defaulting to categories — “busyness,” “the phone,” “ministry load.” Push gently for one specific incident this week, not a category.
- Leaders trying to perform competence. Honest leaders this week create permission for an honest room in Week 3 — the engine of this year working in the open.
- Treating the diagnostic as a test. It is not a test. It is a mirror. Re-frame any time someone starts grading themselves.
- Surfacing material that needs more than the diagnostic can hold. If someone says “rocky soil is my marriage right now,” that is real and may need follow-up. Note it; follow up after.''')

# CRISIS CONTINGENCIES
R('''The diagnostic is gentle by design but can surface heavier material than expected, especially with juniors disclosing family or peer dynamics. Default to Section 6 of the Handbook if you encounter:

- Disclosure of physical or sexual abuse, current or past.
- Suicidal ideation or self-harm, even hinted.
- Family violence or active addiction in the home.
- Anything that triggers your gut to say “this kid needs more than I can give them in this circle right now.”

Two-adult rule for any post-session pastoral conversation with a teen. Pastoral / clinical backup person should be on-call tonight. Lead Companion and one Co-Companion handle disclosure together; the rest of the team stays with the cohort.''',
  '''The diagnostic is gentle by design but can surface heavier material than expected — adults carry decades. Default to the safeguarding frame (Leadership Year Handbook §7 and the host church’s policy) if you encounter:

- Disclosure of abuse, current or past — and remember that a disclosure *about* a minor, made by an adult in this room, may carry reporting duties.
- Suicidal ideation or self-harm, even hinted.
- Violence or active addiction in the home.
- Anything that triggers your gut to say “this person needs more than I can give them in this circle right now.”

Two adults for any post-session pastoral conversation, per the host church’s practice. Pastoral / clinical backup person should be on-call tonight. The convening leader and one Co-Companion handle a disclosure together; the rest of the team stays with the cohort.''')

# Pre-work joint section
R('''### For parent and teen, jointly (5 minutes, in the car)

This is the only joint pre-work this week. Each, separately, picks one of the four soils that they suspect they’ll talk about tonight. Do not tell each other which one. The point is to pre-warm the noticing, not to coordinate the answers.''',
  '''### For every member, privately (5 minutes, on the way)

Each member, separately, picks one of the four soils they suspect they’ll talk about tonight. Do not compare notes with anyone. The point is to pre-warm the noticing, not to coordinate the answers.''')

# Materials
R('''- Junior Heart Soil Diagnostic handout (H2.1) — enough copies for the junior cohort.
- Senior Heart Soil Diagnostic handout (H2.2) — enough for the senior cohort.
- Parent Heart Soil Diagnostic handout (H2.3) — enough for parents.''',
  '- Heart Soil Diagnostic handout (H2.1) — one per member.')
R('- Chairs in single circle for the open and close. Three separate circle areas (or rooms) for the parallel split.',
  '- Chairs in single circle for the open and close. Two or three separate circle areas (or rooms) for the split, sized so each circle holds six to eight.')

# Room arrangement
R('''Three separate circles. Ideal: three different rooms. Acceptable: one large room with three corners marked off, far enough apart that each circle can hear its own voice, not its neighbor’s. The senior teens should not feel they are within earshot of their parents during the diagnostic share.

Each cohort circle has a Companion. Recommended: a male and female Companion pair in the senior circle if the senior cohort is mixed-gender. The junior circle and parent circle each have one Companion. The Lead Companion floats between rooms during the split, doing nothing except being present.''',
  '''Two or three circles of six to eight. Ideal: separate rooms. Acceptable: one large room with corners marked off, far enough apart that each circle can hear its own voice, not its neighbor’s. Nobody should feel within earshot of another circle during the diagnostic share.

Each circle has a Companion. Circle composition — mixed or single-gender — is the host church’s call, made before tonight, not improvised at the split. The convening leader floats between circles during the split, doing nothing except being present.''')

# Prep timeline
R('| Week before | Each Cohort Companion does the diagnostic on themselves. They bring one specific real example to share if they go first in their cohort. Print all three diagnostic handouts. | Each Co-Comp |',
  '| Week before | Each circle Companion does the diagnostic on themselves. They bring one specific real example to share when they go first in their circle — the engine, prepared. Print the diagnostic handout. | Each Co-Comp |')
R('| T-15 min | Door opens. | Teen Comp |', '| T-15 min | Door opens. | Co-Comp |')

# Run sheet table — retime to the woven headings and de-family the labels
R('''| 6:30 | Setup. All Companions in the room. | — | Team | 30 |
| 6:45 | Door opens. Greet, phone-box, light snacks. | Open | Teen Comp | 15 |
| 7:00 | Opening container — full eight-step protocol. | Shared | Lead Comp | 10 |
| 7:10 | Check-in on Week 1 between-session practice. | Shared | Parent Comp | 5 |
| 7:15 | Teaching: Mark 4 and the four soils. | Shared | Lead Comp | 20 |
| 7:35 | Transition to split. Move to cohort circles. | Transition | Lead Comp | 2 |
| 7:37 | SPLIT: Heart Soil diagnostic in cohort circles. | Parallel | Each Co-Comp | 28 |
| 8:05 | Re-merge. Return to single circle. | Transition | Lead Comp | 3 |
| 8:08 | Shared debrief and re-reading of Mark 4:20. | Shared | Lead Comp | 12 |
| 8:20 | Between-session practice introduced. | Shared | Parent Comp | 5 |
| 8:25 | Closing container + Aaronic blessing. | Shared | Lead Comp | 5 |
| 8:30 | End. | — | — | — |''',
  '''| 6:30 | Setup. All Companions in the room. | — | Team | 30 |
| 6:45 | Door opens. Greet, phone-box, light snacks. | Open | Co-Comp | 15 |
| 7:00 | Opening container — full eight-step protocol. | Shared | Lead Comp | 8 |
| 7:08 | Practice check-in + One True Sentence. | Shared | Co-Comp | 8 |
| 7:16 | Teaching: Mark 4 and the four soils. | Shared | Lead Comp | 17 |
| 7:33 | Transition to split. Move to circles. | Transition | Lead Comp | 2 |
| 7:35 | SPLIT: Heart Soil diagnostic in circles. | Circles | Each Co-Comp | 28 |
| 8:03 | Re-merge. Return to single circle. | Transition | Lead Comp | 3 |
| 8:06 | Shared debrief and re-reading of Mark 4:20. | Shared | Lead Comp | 10 |
| 8:16 | Between-session practice introduced. | Shared | Co-Comp | 5 |
| 8:21 | Feedback round + closing container + Aaronic blessing. | Shared | Lead Comp | 9 |
| 8:30 | End. | — | — | — |''')

# Block 2 lead
R('**Co-Comp (Parent) leads.** This is short by design.', '**A Co-Companion leads.** This is short by design.')
R('(Co-Comp (Parent) goes first. Models a true sentence. Examples: “I noticed I checked my phone before I asked the question almost every day this week.” “I noticed that the evening sentence was harder than the morning question because I had to be specific.” “I noticed nothing for four days, and then on Saturday I noticed my son needed help and I didn’t miss it.”)',
  '(The Co-Companion goes first. Models a true sentence. Examples: “I noticed I checked my phone before I asked the question almost every day this week.” “I noticed that the evening sentence was harder than the morning question because I had to be specific.” “I noticed nothing for four days, and then on Saturday I noticed my son needed help and I didn’t miss it.”)')

# Block 3 bridge script
R('''“In a minute we’re going to split into three smaller circles — our junior teens with \\_\\_\\_\\_\\_, our senior teens with \\_\\_\\_\\_\\_ and \\_\\_\\_\\_\\_, and our parents with \\_\\_\\_\\_\\_. Each circle will work through the same four questions, adapted slightly. We’ll come back together at 8:08 to share what surfaced and re-read one verse together.

“One thing before we move. The container conditions still apply in the small circles — maybe more so. Safe, present, clear, intentional. What is shared in the small circle stays in the small circle, including from your parents and your teens. We do not bring tonight’s sharing home as ammunition. Are we all clear on that?”

(Wait for nods or verbal yes from each cohort. Do not move forward until you have it.)

“Okay. Junior teens with \\_\\_\\_\\_\\_, this side. Senior teens with \\_\\_\\_\\_\\_, that side. Parents with \\_\\_\\_\\_\\_, follow me. Take your journal and your handout. We have twenty-eight minutes.”''',
  '''“In a minute we’re going to split into smaller circles of six to eight, each with a Companion. Every circle works through the same four questions. We’ll come back together at 8:06 to land what surfaced and re-read one verse together.

“One thing before we move. The container conditions still apply in the small circles — maybe more so. Safe, present, clear, intentional. What is shared in the small circle stays in the small circle, including from the people you serve beside every week. We do not carry tonight’s sharing into the parking lot, the staff meeting, or the elders’ room. Are we all clear on that?”

(Wait for nods or verbal yes from the room. Do not move forward until you have it.)

“Okay. \\_\\_\\_\\_\\_’s circle, this side. \\_\\_\\_\\_\\_’s circle, that side. Take your journal and your handout. We have twenty-eight minutes.”''')

# Blocks 4 + 4b + 4c -> one adult block built on the parent base
old_splits_start = '## Block 4 — Split: Junior Cohort Diagnostic (7:35–8:03, 28 min)'
old_splits_end = '## Block 5 — Re-Merge and Shared Debrief (8:06–8:16, 10 min)'
i = s.index(old_splits_start)
j = s.index(old_splits_end)
new_block4 = '''## Block 4 — Split: Heart Soil Diagnostic in Circles (7:35–8:03, 28 min)
**Each circle Companion:** Run the diagnostic in your circle. Aim for 28 minutes total. Use Handout H2.1. The Companion goes first on the first question — the engine — with the specific real example prepared this week.

## Script (in each circle)

“Something I want to name out loud. Some of you have not done this kind of work in a long time. Some of you have never done it — years of leading it for other people is not the same thing. Some of you do this regularly with a small group. Whatever your starting point, the four questions are the same.

“What we have going for us tonight is decades of life to draw from, which means we get to be specific. The deceitfulness of riches isn’t a category for us — it is something that has actually deceived us for years and we know it by name. The cares of the world aren’t abstract — we are carrying them right now, this week.

“Two container reminders. First, this circle stays in this circle, including from the people you serve beside. Second, remember why this year exists: the room we lead next year will only ever be as honest as we are willing to be tonight. I’ll go first.

“Okay. Four questions. Two minutes journaling, four to five minutes sharing. We start.”

### The four questions

1. **Path soil.** Where in my life right now is the ground hard — where does God’s word arrive and not penetrate? In what specific area have I stopped expecting God to actually speak? Marriage. Parenting. Ministry. Career. Body. Money. A specific old wound. Pick one and be specific.
2. **Rocky soil.** Where in my life have I had spiritual seasons that didn’t last? What was the sun that came up that revealed the shallowness? A difficult life event. A career transition. A loss. Disillusionment with a church or a leader. The fatigue of midlife. Be specific about the season and about what burned away.
3. **Thorny soil.** What is choking me right now? Cares of the world: ministry load, career intensity, financial pressure, kids’ schedules, aging parents, marriage strain. Deceitfulness of riches: the achievements I have pursued that have not satisfied the way I thought they would. Desires for other things: what am I privately wishing for that, if I got it, would crowd out what God is trying to grow?
4. **Good soil.** Where has there been real fruit in my life that I could not have produced myself? Not what looks good from the outside — actual fruit. A character change. A repaired relationship. An overcome addiction or compulsion. A capacity that wasn’t there ten years ago. Name one and notice that God planted it.

### Circle facilitation notes

- The Companion goes first on question one, with something real. The circle will go exactly as deep as that first answer licenses — the engine, working.
- Some members will try to give the answer that is about someone else (“the rocky soil is watching my son walk away from his faith”). That is a valid answer but it is about someone else. Gently: “What’s the rocky soil in your own heart, separate from theirs?”
- Some members will be doing this for the first time. Honor it. “Thanks for going. That was a real answer.”
- Ministry answers can be a hiding place: “thorny soil is how busy the church keeps me” may be true and still not the truer answer. Gently: “And underneath the busyness?”
- If someone surfaces marital strain or addiction or grief that is heavier than the circle can hold: acknowledge briefly, plan to follow up after, do not turn the circle into a counseling session.
- If a member is more practiced than the rest of the circle and wants to teach or expand, gently: “Save that for the merge. For now, just one specific answer to the question.”

'''
s = s[:i] + new_block4 + s[j:]
print('OK  blocks 4/4b/4c collapsed')

# Closing block Aaronic line
R('- Blessing. The Aaronic blessing spoken parent-to-teen, teen-to-parent, as in Week 1. By Week 2 the cohort knows the form.',
  '- Blessing. The Aaronic blessing spoken member to member, face to face, as in Week 1. By Week 2 the cohort knows the form.')

# Differentiation Notes -> adult form
old_diff_start = '## Junior cohort (12–14)\n\n- Concrete, specific, this-week language.'
i = s.index(old_diff_start)
j = s.index('# Closing Practice Details')
new_diff = '''## Those doing this work for the first time

- Concrete, specific, this-week language. “Name one specific thing that happened on Tuesday” rather than “tell me about your spiritual life.”
- Watch for the member who gives the “right” answer because they are at church — in a leadership cohort the church answer arrives fluently. Gently: “That’s a great church answer. What’s a more real one?”
- First-timers may be the most concrete and incisive in the room. Honor it when it happens — do not assume the newest are the shallowest.

## The veterans

- Veterans can hold abstraction, and abstraction is their hiding place. The thorny soil question is the most diagnostic for this group — spend the most time there if you have to choose.
- Veterans may want to debate the parable (“Is the path soil saved or not?”). Redirect quickly. “Good question for another day. Tonight we’re working on noticing.”
- Veterans have real spiritual work behind them and language for it. Let them use it — and listen for the difference between language that carries experience and language that replaces it.

## The ordained and the staff

- The ordained need permission to be honest, especially about marriage, money, and the ministry itself. Say it plainly in the circle if needed: “There is no report being filed tonight. The covering signed on for exactly this.”
- Watch for the answer that is really about the congregation (“my thorny soil is what the elders are dealing with”). Redirect to the person’s own heart.
- Members recovering from losses or old wounds may surface deep material. Honor it without turning the circle into a recovery group.
- If someone’s answers consistently feel surfacy, do not force depth in Week 2. The trust is still building. Week 6 (confession and restoration) is the natural place for deeper work.

'''
s = s[:i] + new_diff + s[j:]
print('OK  differentiation rewritten')

# Debrief prompts
R('- Parents and teens left treating each other with more attention than usual. (Watch the parking lot.)',
  '- Members left treating each other with more attention than usual. (Watch the parking lot.)')
R('- At least one participant in each cohort had a moment of recognition — the visible “oh” when something landed.',
  '- At least one participant in each circle had a moment of recognition — the visible “oh” when something landed.')
R('- All the answers in a cohort were generic (“my phone,” “being busy”). Indicates the Companion did not push for specificity.',
  '- All the answers in a circle were generic (“busyness,” “the season we’re in”). Indicates the Companion did not push for specificity.')
R('- The merge debriefed details from the cohort circles, breaking the within-cohort confidentiality.',
  '- The merge debriefed details from the circles, breaking the within-circle confidentiality.')
R('''- Anyone who surfaced material that approached crisis-level (suicidal ideation, abuse hint, eating disorder behavior, family violence). Section 6 protocol within 48 hours, two-adult rule for teens.
- Any parent who broke down or surfaced something heavy. Pastoral 1:1 within the week.
- Any teen whose parent surfaced something heavy in the parent circle — the teen does not know, but the team should be aware that home dynamics may be tender for the next week.
- Any participant who gave only generic answers and seemed to be holding back. Informal contact, no pressure, just “How did Tuesday land?”''',
  '''- Anyone who surfaced material that approached crisis-level (suicidal ideation, abuse disclosure, addiction, violence at home). The safeguarding frame applies within 48 hours — two adults, the host church’s practice.
- Anyone who broke down or surfaced something heavy. Pastoral 1:1 within the week.
- Anyone whose disclosure touches a household the cohort also serves — the team should be aware that dynamics may be tender in the coming week, and says nothing to anyone.
- Any participant who gave only generic answers and seemed to be holding back. Informal contact, no pressure, just “How did it land?”''')
R('- If the split felt unsafe, slow Week 3’s opening. Re-name the container conditions before the split into circles of 4–5.',
  '- If the split felt unsafe, slow Week 3’s opening. Re-name the container conditions before the split into smaller circles.')

# Handouts: three -> one
old_h = 'Three diagnostic handouts — one per cohort. Each is on its own page below. Print as needed.'
i = s.index(old_h)
new_handouts = '''One diagnostic handout, printed for every member.

**Handout H2.1 — Heart Soil Diagnostic**

*This is not a test. It is a way of paying attention. Jesus tells us in Mark 4 that there are four kinds of soil, and we have all four going on at once, in different parts of our lives. The work is to notice where each one shows up — and we get to be specific, because we have decades to draw from.*

*Two minutes journaling per question, one or two sentences each. Specific, not abstract. “I’d rather not share that one” is a complete answer.*

## 1. Path soil

**Where in my life right now is the ground hard — where does God’s word arrive and not penetrate? In what specific area have I stopped expecting God to actually speak? Marriage. Parenting. Ministry. Career. Body. Money. A specific old wound. Pick one and be specific.**

## 2. Rocky soil

**Where in my life have I had spiritual seasons that didn’t last? What was the sun that came up that revealed the shallowness? A difficult life event. A career transition. A loss. Disillusionment with a church or a leader. The fatigue of midlife. Be specific about the season and about what burned away.**

## 3. Thorny soil

**What is choking me right now? Cares of the world: ministry load, career intensity, financial pressure, kids’ schedules, aging parents, marriage strain. Deceitfulness of riches: the achievements I have pursued that have not satisfied the way I thought they would. Desires for other things: what am I privately wishing for that, if I got it, would crowd out what God is trying to grow?**

## 4. Good soil

**Where has there been real fruit in my life that I could not have produced myself? Not what looks good from the outside — actual fruit. A character change. A repaired relationship. An overcome addiction or compulsion. A capacity that wasn’t there ten years ago. Name one and notice that God planted it.**
'''
s = s[:i] + new_handouts
print('OK  handouts consolidated')

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
print(f'W2: {len(E)} pair edits + 3 section rewrites, {fail} failures')
sys.exit(1 if fail else 0)
