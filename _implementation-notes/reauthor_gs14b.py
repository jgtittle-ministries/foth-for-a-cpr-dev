# GS Week 14 residual sweep: contingencies, pre-work, email, run sheet, rehearsal.
import io, sys, re
f = 'docs/getting-started/week-14-sending.md'
s = io.open(f, encoding='utf-8').read()
E = [
('- The blessing-as-performance. Some parents will arrive with prepared speeches that are too long, too polished, or too preachy. The form is one specific witnessed sentence — not a speech. Frame this twice before the commissioning.',
 '- The blessing-as-performance. Some members will arrive with prepared speeches that are too long, too polished, or too preachy — leaders write speeches for a living. The form is one specific witnessed sentence — not a speech. Frame this twice before the blessings.'),
('- The teen whose blessing for their parent surfaces unexpected family material. Honor it. Do not interpret. Pastoral 1:1 follow-up.',
 '- The blessing that surfaces unexpected household material. Honor it. Do not interpret. Pastoral 1:1 follow-up.'),
('- Going Deeper drift. Some families will be ready; some will be ambivalent; some will not continue. Tonight is a sending, not a recruiting pitch. Frame the bridge to Going Deeper briefly and clearly; let participants decide on their own time.',
 '- Going Deeper drift. Some members will be ready; some will be ambivalent; some will not continue. Tonight is a sending, not a recruiting pitch. Frame the bridge to Going Deeper briefly and clearly; let participants decide on their own time.'),
('**If a teen breaks down during their blessing of their parent.** Stop. Sit them down. The Cohort Companion goes with them. Do not push them through the blessing. The community can speak the blessing in their place. Follow up offline within 48 hours.',
 '**If a member breaks down during their blessing.** Stop. Allow it. A Companion moves close. Do not push them through. The community can speak the blessing in their place. Follow up offline within 48 hours.'),
('**If a parent breaks down during their blessing of their teen.** Stop. Allow the silence. Many parents will recover and complete the blessing in their own time. If they cannot, the Lead Companion names what they were trying to say briefly: ‘What I think your dad wants you to know is \\_\\_\\_\\_\\_.’ Pastoral 1:1 follow-up.',
 '**If a guest breaks down while blessing back.** Stop. Allow the silence. Many recover and complete the blessing in their own time. If they cannot, the convening leader names it gently: ‘What I think they want you to know is \\_\\_\\_\\_\\_.’ Nothing is required of guests; standing close was already the blessing.'),
('**If a family surfaces unresolved conflict during the commissioning (e.g., a teen says something pointed; a parent reacts).** Stop the commissioning. Do not interpret in front of the room. The Lead Companion and one Co-Companion step aside with the family. Pastoral / clinical backup called within the hour. Section 6 protocol.',
 '**If a household surfaces unresolved conflict during the blessing (something pointed said; a reaction).** Stop the blessing. Do not interpret in front of the room. The convening leader and one Co-Companion step aside with the household. Pastoral / clinical backup called within the hour. The safeguarding frame applies.'),
('**If the absent-parent situation produces visible grief.** Honor it. The cohort can stand for the absent parent; a Co-Companion may stand in. Pre-plan with the family before the night; do not improvise.',
 '**If an absence produces visible grief.** Honor it. The cohort can stand for the absent one; a Co-Companion may stand in. Pre-plan with the member before the night; do not improvise.'),
('**If a teen surfaces something previously undisclosed (abuse, suicidal ideation) in the heat of the commissioning emotion.** Section 6 protocol. Two-adult rule. Pastoral / clinical backup. Mandatory reporting if applicable. Getting Started has not closed if a teen is in crisis.',
 '**If anyone surfaces something previously undisclosed (abuse, suicidal ideation) in the heat of the night’s emotion.** The safeguarding frame. Two Companions. Pastoral / clinical backup. Mandatory reporting if a minor is involved. Getting Started has not closed if someone is in crisis.'),
('- Week 12: the gifts inventory and downhill mission are part of tonight’s blessing material. Each parent’s blessing of their teen draws on what they have specifically witnessed across Getting Started; each teen’s blessing of their parent draws on what they have noticed.',
 '- Week 12: the gifts inventory and downhill mission are part of tonight’s blessing material. Each member’s blessing of their household draws on what the year has taught them to see.'),
('- Joint Footprints (Wk 3): the parent-and-teen dyad has done at least one cross-generational practice together. Tonight is the public form of what they began privately.',
 '- Shared Footprints (Wk 3): each member has done at least one telling-and-blessing practice at home. Tonight is the public form of what they began privately.'),
('The point is not to rehearse a tool. The point is to let the form get into your bones before you teach it. The teens will not be moved by a teaching about commissioning; they will be moved by a team that is visibly doing it themselves.',
 'The point is not to rehearse a tool. The point is to let the form get into your bones before you teach it. The room will not be moved by a teaching about blessing; it will be moved by a team that is visibly doing it themselves.'),
('2. Family review. Each family pre-considered: are both parents coming? Is the teen safe? Has anything from Wks 9–13 surfaced that needs care tonight? For families with absent parents (divorce, deployment, bereavement, estrangement), pre-plan the commissioning for that family specifically.',
 '2. Household review. Each member pre-considered: who is coming? Has anything from Wks 9–13 surfaced that needs care tonight? For members with absent households (distance, bereavement, estrangement, living alone), pre-plan that member’s blessing specifically.'),
('3. Blessing rehearsal. Each Cohort Companion pairs with another Companion and speaks an actual blessing over them — the form, brief, specific, witnessed. The team must have done it themselves before they ask families to do it.',
 '3. Blessing rehearsal. Each Companion pairs with another Companion and speaks an actual blessing over them — the form, brief, specific, witnessed. The team must have done it themselves before they ask the room to do it.'),
('## **Family pre-work — sent to families one week before Week 14**\n\nThe team sends an email to all families one week before Week 14 with the following content:',
 '## **Member pre-work — sent to members one week before Week 14**\n\nThe team sends an email to all members one week before Week 14 with the following content:'),
('*“Dear families: Next Tuesday is Week 14 — the Family Commissioning. (One gathering follows it: the Week 15 commissioning of our Companions-in-Formation.) Please plan as follows.”*',
 '*“Dear friends: next week is Week 14 — the Household Blessing Night. (One gathering follows it: the Week 15 commissioning, where the covering sends this cohort.) Please plan as follows.”*'),
('*“Your pre-work: each parent-and-teen dyad in the program prepares one specific witnessed blessing for the other. Three sentences. (1) What I have specifically seen God doing in you across Getting Started. (2) What I am specifically blessing in you tonight. (3) What I am specifically committing to in our relationship moving forward. The Cohort Companion will email a worksheet (Handout H14.1) by Friday — use it.”*',
 '*“Your pre-work: prepare one specific witnessed blessing for each person of your household — or one for your household together. Three sentences. (1) What I have specifically seen God doing in you, or seen freshly about you, across this year. (2) What I am specifically blessing in you tonight. (3) What I am specifically committing to in our relationship moving forward. A worksheet (Handout H14.1) comes by Friday — use it.”*'),
('*“If there is anything difficult in your family situation — an absent parent, a recent loss, a relationship that is fragile — please reach out to the team this week. We will pre-plan with you. Nothing about tonight should be a surprise to anyone.”*',
 '*“If there is anything difficult in your household situation — an absence, a recent loss, a relationship that is fragile, a house of one — please reach out to the team this week. We will pre-plan with you. Nothing about tonight should be a surprise to anyone.”*'),
('1. Print the Family Commissioning Worksheet (H14.1) — one per parent-and-teen dyad, mailed/emailed Friday.',
 '1. Print the Household Blessing Worksheet (H14.1) — one per member, mailed/emailed Friday.'),
('| 1 week before | Email families with Week 14 logistics. Send H14.1 worksheet by Friday. | Lead Comp |',
 '| 1 week before | Email members with Week 14 logistics. Send H14.1 worksheet by Friday. | Lead Comp |'),
('| 6:45–6:55 | Block 2: Brief blessing rehearsal | Shared circle | Lead Comp | Walk the form aloud. Two Companions demo a brief commissioning. Q&A from families. |',
 '| 6:45–6:55 | Block 2: Brief blessing rehearsal | Shared circle | Lead Comp | Walk the form aloud. Two Companions demo a brief blessing. Q&A from the room. |'),
('| 7:05–8:00 | Block 4: Family commissionings | Shared circle, central space | Lead Companion + Co-Comp | Each family in turn. Parent and teen stand center. Each speaks blessing. Community speaks Aaronic over family. ~5–7 min per family. |',
 '| 7:05–8:00 | Block 4: The household blessings | Shared circle, central space | Lead Companion + Co-Comp | Each member in turn, with their household. The member blesses; the household may bless back. Community speaks Aaronic over each. ~5–7 min per household. |'),
('| 8:15–8:25 | Block 6: Rhythm Card and Going Deeper bridge | Shared circle | Co-Comp (Parent) | Walk H14.3 and H14.4. Distribute Post-Series Survey (H14.5). |',
 '| 8:15–8:25 | Block 6: Rhythm Card and Going Deeper bridge | Shared circle | Co-Comp | Walk H14.3 and H14.4. Distribute Post-Series Survey (H14.5). |'),
('Walk the form aloud. Two Companions demo a real blessing. Brief Q&A from families. The goal is to lower the activation energy for parents and teens who have never spoken a blessing aloud before.',
 'Walk the form aloud. Two Companions demo a real blessing. Brief Q&A from the room. The goal is to lower the activation energy for anyone who has never spoken a blessing aloud over their own people before.'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:64]}'); fail += 1; continue
    s = s.replace(old, new)
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W14b: {len(E)} edits, {fail} failures')
res = [m.group(0)[:100] for m in re.finditer(r'^.*\b(teens?|parents?|dyads?|famil(?:y|ies)|CCA)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:20]: print('  ', r)
sys.exit(1 if fail else 0)
