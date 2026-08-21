# GD Week 8 adult re-authoring: the group hears itself; positional projection replaces generational.
import io, sys, re
f = 'docs/going-deeper/week-08-group-hears-itself.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Whole-room. No cohort split. The cohort sits as one circle with no centre chair tonight — the cohort itself is the subject of the hearing.',
 '**Mode.** Whole-room. No circle split. The cohort sits as one circle with no centre chair tonight — the cohort itself is the subject of the hearing.'),
('**Political or generational projection. A parent says ‘God is saying our young people need to\\_\\_\\_\\_\\_.’ A senior teen says ‘God is saying our parents have to\\_\\_\\_\\_\\_.’ These are almost always projection.',
 '**Political or positional projection. A pastor says ‘God is saying the congregation needs to\\_\\_\\_\\_\\_.’ A lay member says ‘God is saying the leadership has to\\_\\_\\_\\_\\_.’ These are almost always projection.'),
('**If a contribution opens material about active harm or abuse within the cohort. Section 6 protocol immediately.',
 '**If a contribution opens material about active harm or abuse within the cohort. The safeguarding frame immediately.'),
('**If a teen-parent dynamic surfaces in the contributions cross-cohort. Receive without naming the family. Pastoral support outside the session.**',
 '**If a marriage dynamic surfaces in the contributions. Receive without naming the couple. Pastoral support outside the session.**'),
('**Default. Section 6 of the Going Deeper Handbook covers anything that crosses the safety threshold. Pastoral / clinical backup confirmed by name and number for the night.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy) covers anything that crosses the safety threshold. Pastoral / clinical backup confirmed by name and number for the night.**'),
('Level 3 — people who do real work together (the cohort circle level, where most of Going Deeper has operated).',
 'Level 3 — people who do real work together (the circle level, where most of Going Deeper has operated).'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs. NO centre chair tonight.',
 '**•** Confirm room layout: ONE large circle — a chair for every member. NO centre chair tonight.'),
('**•** Chairs in ONE large single circle, 20–32 chairs. NO centre chair.',
 '**•** Chairs in ONE large single circle, one per member. NO centre chair.'),
('| T-15 min | Door opens. Welcome each participant by name. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. |'),
('| 8:16–8:21 | Block 7: Between-session practice | Shared circle | Co-Comp (Parent) | Journal what was heard. Standing-pair check-in. |',
 '| 8:16–8:21 | Block 7: Between-session practice | Shared circle | Co-Comp | Journal what was heard. Standing-pair check-in. |'),
('## Script — Co-Companion (parent cohort) leads',
 '## Script — a Co-Companion leads'),
('**•** Any teen-parent dynamic that surfaced during contributions. Cross-cohort follow-up by the appropriate Companions.',
 '**•** Any marriage dynamic that surfaced during contributions. Cross-circle follow-up by the appropriate Companions.'),
]
# pairs expected to appear exactly twice (teaching block + handout card)
E2 = [
('**LEVEL 3 — People who do real work together. The cohort circle level. Specific work surfaces in specific members; the room holds it. Wks 2–7 of Going Deeper have operated here.**',
 '**LEVEL 3 — People who do real work together. The circle level. Specific work surfaces in specific members; the room holds it. Wks 2–7 of Going Deeper have operated here.**'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
for old, new in E2:
    n = s.count(old)
    if n != 2:
        print(f'!! count={n} (expected 2): {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

*Tonight there is no circle split. The room’s members are doing this differently inside the same circle. The Cohort Companions read their circles’ members across the session and follow up offline as needed.*

**Those doing this work for the first time**

## Adjustments

**First-timers often hear concrete, embodied things in corporate listening. ‘We need more silence in the room.’ ‘We are kinder to each other than we were at the start.’ Concrete is good; the Lead Companion does not push anyone to abstract their hearing.**

**Watch for: the member whose contribution names a specific cohort member positively (‘[Name] is so kind’). Quietly: ‘Hold the kindness about them; what did you hear about US, the body?’ The redirect is gentle; the kindness is not undone by being held.**

**Watch for: the member who, at the integration block, looks uncertain whether what they heard counts. Cohort Companion affirms their contribution by name during the surfacing if it is being underweighted in the body’s weighing.**

**Watch for: the member who passes during the surfacing and is activated by the cohort’s integration block. Some only find their voice once they hear others weighing. Cohort Companion invites: ‘Anything you want to add now?’ No pressure.**

**Watch for: the member for whom the silent listening was destabilizing. Cohort Companion follow-up offline within 24 hours.**

**The veterans**

## Adjustments

**Veterans often hear systemic patterns — what the cohort is doing well, where it is performing, where it is shrinking from harder work. The Lead Companion weights these contributions equally, especially when they critique the cohort.**

**Watch for: the veteran who hears something about the cohort’s relationship to Christ that is theologically sharp (‘we are good at the work and not as good at the worship’). Honour. Let the cohort weigh it.**

**Watch for: the veteran who passes because they think their hearing might offend. Cohort Companion briefly checks: ‘Anything for the body you held back?’ No pressure; the offer is the support.**

**Watch for: the veteran whose hearing crosses thresholds (a sense that the cohort is doing harm, a sense of withdrawal). Pastoral 1:1 within 48 hours; the discernment may be real.**

**The ordained and the staff**

## Adjustments

**The ordained often hear the cohort’s long-term arc — what has shifted across the year, what has stayed stuck, what is just beginning to form. The Lead Companion gives these contributions weight without letting the office impose them on the body’s weighing.**

**Watch for: the positional projection in either direction (‘God is saying the congregation needs to \\_\\_\\_\\_\\_’; ‘God is saying the leadership has to \\_\\_\\_\\_\\_’). Same redirect as the WATCH FOR section: almost always projection. Receive without commentary; reflect to the cohort during integration without naming the speaker.**

**Watch for: the leader who hears something specific about the cohort’s relationship to the broader church or community. Honour; the cohort is not isolated, and the Spirit may speak about how the body relates to the bodies it is part of.**

**Watch for: the leader who hears something they sense the congregation needs to receive. The hearing is for the body in this room; the leader does not appropriate it as sermon material. Discernment with the covering first, if it persists.**

**Watch for: the member whose hearing is about the team itself — the Companions. Receive humbly. The team is part of the cohort; what is heard about US includes us. The team commits in advance not to deflect this category of hearing.**

**Watch for: the leader whose hearing produces an action item (‘we need to start doing X’). The cohort tonight is not a decision-making body; the hearing is held, weighed, and revisited at Wk 11. The leader’s impulse to act is normal; the discipline is to hold.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD08: {len(E)}+{len(E2)}x2+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
