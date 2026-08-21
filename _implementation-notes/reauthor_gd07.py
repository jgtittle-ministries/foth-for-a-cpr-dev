# GD Week 7 adult re-authoring: corporate listening prayer to the leadership register.
import io, sys, re
f = 'docs/going-deeper/week-07-corporate-listening.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Whole-room. No cohort split.',
 '**Mode.** Whole-room. No circle split.'),
('The Bringer disclosing material that exceeds what corporate prayer can hold (active suicidality, current abuse, mandatory-reporting territory). Section 6 protocol activates; the listening prayer pivots to crisis support; pastoral / clinical backup engaged.**',
 'The Bringer disclosing material that exceeds what corporate prayer can hold (active suicidality, current abuse, mandatory-reporting territory). The safeguarding frame activates; the listening prayer pivots to crisis support; pastoral / clinical backup engaged.**'),
('**Junior teens watching parents speak prophetically into other parents (or vice versa). Cross-cohort dynamics multiply. The team is briefed on which families are present and which speakings could land sideways; Cohort Companions watch their cohort members in real time.**',
 '**Members watching their spouse speak prophetically into another member — or the room watching its own pastor spoken into. The dynamics multiply. The team is briefed on which couples are present and which speakings could land sideways; Cohort Companions watch their circles’ members in real time.**'),
('the room is dismissed briefly to a side room; pastoral / clinical backup engaged within 15 minutes. Section 6 protocol.**',
 'the room is dismissed briefly to a side room; pastoral / clinical backup engaged within 15 minutes. The safeguarding frame applies.**'),
('**Default. Section 6 of the Going Deeper Handbook. Pastoral / clinical backup confirmed by name and number. Lead Companion carries phone access in the room.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy). Pastoral / clinical backup confirmed by name and number. Lead Companion carries phone access in the room.**'),
('**4.** Cross-family review. Identify in advance any teen whose parent is in the room and whose speaking-back to the Bringer could land cross-cohort awkwardly; same in reverse. Cohort Companions are responsible for watching their cohort’s members during the round. (10 min)',
 '**4.** Cross-household review. Identify in advance any member whose spouse is in the room and whose speaking-back to the Bringer could land awkwardly at home; note whether the Bringer’s spouse is present. Cohort Companions are responsible for watching their circles’ members during the round. (10 min)'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs with the Bringer’s chair in the centre,',
 '**•** Confirm room layout: ONE large circle — a chair for every member — with the Bringer’s chair in the centre,'),
('**•** Chairs in ONE large single circle, 20–32 chairs with ONE chair in the geometric centre for the Bringer.',
 '**•** Chairs in ONE large single circle, one per member, with ONE chair in the geometric centre for the Bringer.'),
('| T-15 min | Door opens. Welcome each participant by name. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door; remind: phones off tonight, not silent. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door; remind: phones off tonight, not silent. |'),
('| 8:20–8:23 | Block 8: Between-session practice | Shared circle | Co-Comp (Parent) | Each member journals what they did NOT speak. Bringer journals daily. |',
 '| 8:20–8:23 | Block 8: Between-session practice | Shared circle | Co-Comp | Each member journals what they did NOT speak. Bringer journals daily. |'),
('## Script — Co-Companion (parent cohort) leads',
 '## Script — a Co-Companion leads'),
('**•** Any listener whose speaking-back was for a Bringer who is their own family member in another cohort — pastoral 1:1 within the week if the cross-family dynamic surfaced anything heavy.',
 '**•** Any listener whose speaking-back was for a Bringer who is their own spouse — pastoral 1:1 within the week if the household dynamic surfaced anything heavy.'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

*Tonight there is no circle split. The room’s members are doing this differently inside the same circle. The Cohort Companions read their circles’ members across the session and follow up offline as needed.*

**Those doing this work for the first time**

## Adjustments

**First-timers may struggle to listen FOR the Bringer (rather than for themselves) for 20 silent minutes. Coach before Tuesday, not in front of the room: ‘When the silent listen starts, pray for [Bringer] by name. Then ask: what is on God’s heart for [Bringer]? Sit with what comes.’**

**First-timers often speak short and concrete (‘I heard the word "steady" for you’) rather than long and abstract. Honor the concrete; affirm the brevity.**

**Watch for: the member who is silent in the speaking-back round but visibly emotional. Cohort Companion follow-up offline; the unspoken hearing may be significant.**

**Watch for: the member who says nothing came and feels like they failed. Affirm aggressively. ‘Silence in the round is not failure; silence is one of the honest answers. Some weeks you will speak; some weeks you will hold what came in the silent listen for your own walking.’**

**The veterans**

## Adjustments

**Veterans are more likely to drift articulate-but-not-FOR-the-Bringer. ‘I have a long thought about how [Bringer]’s situation reminds me of a passage I read last week.’ Lead Companion catches: ‘Specifically what came to you FOR [Bringer]?’**

**Watch for: the veteran who has read enough about prophecy to want to demonstrate prophetic hearing. ‘I am getting a strong word for [Bringer].’ Affirm the openness; gently constrain: ‘Whatever the strength, frame in I-heard language. The Bringer weighs.’**

**Watch for: the veteran who tries to use the speaking-back to address something between them and the Bringer that is unaddressed elsewhere. Pastoral 1:1 within the week; do NOT use the speaking-back for relational work.**

**The ordained and the staff**

## Adjustments

**The ordained are most at risk of drifting authoritative. Years of pulpit language and pastoral-counsel language can produce ‘God is calling you to’ phrasing without the speaker noticing. Lead Companion catches each instance; the team is briefed to expect it.**

**Watch for: the member whose spouse is the Bringer. The spouse is briefed in advance to consider passing, or to hold their hearing for the at-home conversation rather than the public round — spousal hearing in this format is hard to land cleanly.**

**Watch for: the speaking-back that is heavy with the speaker’s own life context. ‘I heard what I have been hearing for myself this season — \\_\\_\\_\\_\\_.’ The parallel may be real; speaking it FOR the Bringer requires confidence that it is for the Bringer specifically. If unsure, pass.**

**Watch for: the leader who tries to offer pastoral counsel in the speaking-back. Lead Companion: ‘Counsel is for offline. Tonight: only what came to you while you were listening, framed in I-heard.’**

**Watch for: the Bringer who, when weighing, tries to set aside what was said too quickly because it is uncomfortable. The Lead Companion does not push the Bringer to receive; but during the Saturday pre-brief, the Lead Companion can name in advance: ‘Weighing is not the same as setting aside what is hard to hear. Sit with discomfort before deciding.’**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD07: {len(E)}+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
