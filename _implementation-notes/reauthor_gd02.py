# GD Week 2 adult re-authoring: soils diagnostic to the leadership register.
import io, sys, re
f = 'docs/going-deeper/week-02-soils.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Shared teaching first; SPLIT into cohort circles for the diagnostic exercise; MERGE for closing.',
 '**Mode.** Shared teaching first; SPLIT into circles of four to eight for the diagnostic exercise; MERGE for closing.'),
('- The teen who maps too much hard-path soil onto their parent. ‘My dad is hard-path right now.’ Re-frame: tonight is your interior, not your parent’s. ‘Where IN YOU is hard-path soil right now — maybe with regard to your dad?’',
 '- The member who maps too much hard-path soil onto someone else. ‘My spouse is hard-path right now.’ Re-frame: tonight is your interior, not theirs. ‘Where IN YOU is hard-path soil right now — maybe with regard to your spouse?’'),
('- The parent who maps too much thorny soil onto their teen. Same redirect: where in you is the thorny soil operating?',
 '- The leader who maps too much thorny soil onto the ministry. Same redirect: where in you is the thorny soil operating?'),
('Most of what surfaces tonight is workable in the cohort circle; some will need offline follow-up.',
 'Most of what surfaces tonight is workable in the circle; some will need offline follow-up.'),
('The Cohort Companion stays with the participant briefly after the cohort circle.',
 'The Cohort Companion stays with the participant briefly after the circle.'),
('**If a participant’s mapping reveals trauma underneath what looked like ordinary soil hardness.** Section 6 protocol of the Going Deeper Handbook. Do not interpret in the room. Pastoral / clinical referral if welcomed.',
 '**If a participant’s mapping reveals trauma underneath what looked like ordinary soil hardness.** The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy). Do not interpret in the room. Pastoral / clinical referral if welcomed.'),
('3. Family review: anyone the team is watching for after Wk 1’s interlude share? Brief. (5 min)',
 '3. Member review: anyone the team is watching for after Wk 1’s interlude share? Brief. (5 min)'),
('4. Confirm room setup: one large circle for opening, three cohort spaces for the split.',
 '4. Confirm room setup: one large circle for opening, circle spaces for the split.'),
('- Chairs in main room as one large circle for opening; three cohort spaces ready for the split.',
 '- Chairs in main room as one large circle for opening; circle spaces ready for the split.'),
('- Three cohort spaces, each with: large-print Bible, tissues, wall clock, room enough for cohort circle plus quiet writing time.',
 '- Each circle space with: large-print Bible, tissues, wall clock, room enough for the circle plus quiet writing time.'),
('| Day before | Walk the room. Confirm cohort spaces. | Lead Comp |',
 '| Day before | Walk the room. Confirm circle spaces. | Lead Comp |'),
('| T-30 min | Each Cohort Companion preps their cohort space. | All Companions |',
 '| T-30 min | Each Cohort Companion preps their circle space. | All Companions |'),
('| T-15 min | Door opens. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. |'),
('| 7:34–8:10 | Block 5: The four-places mapping in cohort circles | Cohort circles | Cohort Facs | 20 min quiet writing; 18 min sharing in the cohort circle. |',
 '| 7:34–8:10 | Block 5: The four-places mapping in circles | Circles | Cohort Comps | 20 min quiet writing; 18 min sharing in the circle. |'),
('| 8:10–8:18 | Block 6: Merge and surface | Shared circle | Lead Comp | One observation per cohort. Brief integration. |',
 '| 8:10–8:18 | Block 6: Merge and surface | Shared circle | Lead Comp | One observation per circle. Brief integration. |'),
('| 8:18–8:23 | Block 7: Between-session practice | Shared circle | Co-Comp (Parent) | Sit with one soil region 30 min this week. |',
 '| 8:18–8:23 | Block 7: Between-session practice | Shared circle | Co-Comp | Sit with one soil region 30 min this week. |'),
('*“In your cohort circle, your Companion will walk the exercise.',
 '*“In your circle, your Companion will walk the exercise.'),
('*“Junior teens with [name]. Senior teens with [name]. Parents with [name]. Thirty-five minutes. Go.”*',
 '*“Circle assignments are on the wall — circles of four to eight, each with its Companion. Thirty-five minutes. Go.”*'),
('## **Block 5 — The Four-Places Mapping in Cohort Circles (7:34–8:10, 36 min)**\nEach cohort circle works in parallel. The structure is identical.',
 '## **Block 5 — The Four-Places Mapping in Circles (7:34–8:10, 36 min)**\nEach circle works in parallel. The structure is identical.'),
('### **Inside the cohort circle — Companion script**',
 '### **Inside the circle — Companion script**'),
('the level of specificity the Cohort Companion brings is the level the cohort will match.)',
 'the level of specificity the Cohort Companion brings is the level the circle will match.)'),
('- If a participant maps too much soil onto another person (‘my dad is hard-path right now’) — redirect: ‘Tonight is your interior. Where in YOU is hard-path soil right now — maybe with regard to your dad?’',
 '- If a participant maps too much soil onto another person (‘my spouse is hard-path right now’) — redirect: ‘Tonight is your interior. Where in YOU is hard-path soil right now — maybe with regard to your spouse?’'),
('- If the cohort wants to coach each other',
 '- If the circle wants to coach each other'),
('I’m going to ask each Cohort Companion to name one general thing they noticed about their cohort — not a specific person, the cohort.”*',
 'I’m going to ask each Cohort Companion to name one general thing they noticed about their circle — not a specific person, the circle.”*'),
('(Each Cohort Companion names one general observation, 60 seconds. Examples: ‘Many in our cohort named one relationship as good soil and were surprised by the others.’ Or: ‘Several of us mapped thorny soil at work and didn’t expect that.’ Or: ‘Our cohort had unusual specificity tonight — the diagnostic landed.’)',
 '(Each Cohort Companion names one general observation, 60 seconds. Examples: ‘Many in our circle named one relationship as good soil and were surprised by the others.’ Or: ‘Several of us mapped thorny soil at work and didn’t expect that.’ Or: ‘Our circle had unusual specificity tonight — the diagnostic landed.’)'),
('*“What I notice across all three cohorts is \\_\\_\\_\\_\\_.',
 '*“What I notice across the circles is \\_\\_\\_\\_\\_.'),
('Or: ‘Several cohorts surfaced rocky soil in prayer life specifically — we will engage that in Wk 6.’',
 'Or: ‘Several circles surfaced rocky soil in prayer life specifically — we will engage that in Wk 6.’'),
('- Each cohort circle had at least one participant whose mapping surprised them — a soil condition they didn’t see coming.',
 '- Each circle had at least one participant whose mapping surprised them — a soil condition they didn’t see coming.'),
('- The mappings showed range. If everyone in a cohort produced the same pattern, the cohort is performing rather than diagnosing.',
 '- The mappings showed range. If everyone in a circle produced the same pattern, the circle is performing rather than diagnosing.'),
('- At least one participant in each cohort named a specific hard-path region honestly.',
 '- At least one participant in each circle named a specific hard-path region honestly.'),
('- The merge surfaced patterns that were not obvious before the cohort circles.',
 '- The merge surfaced patterns that were not obvious before the circles.'),
('- Most cohort participants mapped everything as good soil.',
 '- Most of a circle mapped everything as good soil.'),
('- New participants felt sidelined in their cohort circles.',
 '- New participants felt sidelined in their circles.'),
('- Any teen whose mapping revealed hard-path with a parent. Cohort Companion follow-up offline.',
 '- Anyone whose mapping revealed hard-path in their own household. Cohort Companion follow-up offline.'),
('- Any parent whose mapping revealed long-term hard-path with marriage or vocation. Pastoral 1:1 within the week if welcomed.',
 '- Anyone whose mapping revealed long-term hard-path with marriage or vocation. Pastoral 1:1 within the week if welcomed.'),
('- H2.1 — Soil Diagnostic Worksheet (junior, senior, and parent versions)',
 '- H2.1 — Soil Diagnostic Worksheet'),
('*Twenty minutes alone. Three versions on this page — use the one for your cohort. Be specific. The diagnostic only works on truthful data.*',
 '*Twenty minutes alone. Be specific. The diagnostic only works on truthful data.*'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
# Differentiation section: full replacement between anchors
DA = '# **Differentiation by Cohort**'
DB = '# **Closing Practice in Detail**'
NEWDIFF = '''# **Differentiation Notes**

## **Those doing this work for the first time**

## Adjustments

- Simpler on-ramp if the worksheet stalls: ‘four places where life is actually happening for you right now.’ Marriage or a close friendship; work in this season; prayer life; a relationship that is currently hard.
- Watch for: the member who can’t identify four distinct places. ‘Three is enough.’ Don’t force a fourth.
- Watch for: the member whose four places are all church. Affirm; gently invite one place outside church life for the diagnostic. Ministry-only soil mapping can mask other regions.
- Watch for: the member who maps everything as good soil. Performance. Push gently: ‘Of the four — which one is the LEAST like good soil right now?’ The least-like is often the diagnostic gold.

## **The veterans**

## Adjustments

- Veterans of Getting Started have fuller IJH language; let them use it — and watch that the language doesn’t do the work for them.
- Watch for: the mapping that is intellectually polished but emotionally remote. ‘Where in this is YOU — not the analysis of you?’
- Watch for: the veteran whose mapping reveals significant rocky soil in a long relationship they had filed as settled. Receive without coaching.
- Watch for: the veteran who realizes mid-exercise that their friendship-soil is mostly performance. The realization is the work.

## **The ordained and the staff**

## Adjustments

- The adult life-stage prompts apply in full: marriage; one specific friendship; vocation; faith life; family-of-origin; a current relational tension. For the ordained, the vocation line and the faith-life line are two different lines — keep them separate on purpose.
- Watch for: the leader whose mapping reveals that one major place — marriage, vocation, a call grown cold — has been hard-path soil for years and has been suppressed. Receive without rushing. Pastoral 1:1 within the week if welcomed.
- Watch for: the leader who maps thorny everywhere. Mid-life and ministry often read as thorny because the season IS structurally thorny — too many cares competing. Affirm; gently invite the question of which thorn is most worth addressing.
- Watch for: the leader whose mapping centers on the congregation. Re-frame: ‘Where in YOUR interior is this soil — not in the church.’
- Watch for: the leader who maps good soil with their spouse and rocky everywhere else. Often a season-of-life pattern; affirm without minimizing.

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
# H2.1: drop junior and senior versions, keep parent content as the single card
JH = '## **Junior version (ages 12–14)**'
PH = '## **Parent version**\n\n## Four specific places in your life right now'
if s.count(JH) == 1 and s.count(PH) == 1 and s.index(JH) < s.index(PH):
    s = s[:s.index(JH)] + s[s.index(PH):]
    s = s.replace(PH, '## Four specific places in your life right now', 1)
else:
    print('!! H2.1 splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD02: {len(E)}+2 splices, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
