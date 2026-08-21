# GD Week 5 adult re-authoring: confession and restoration to the leadership register.
import io, sys, re
f = 'docs/going-deeper/week-05-confession.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Shared teaching of the architecture (15 min). Cohort circles for the standing-pair work (60 min, including bridge and prayer).',
 '**Mode.** Shared teaching of the architecture (15 min). Circles for the standing-pair work (60 min, including bridge and prayer).'),
('**The teen whose sin pattern crosses a mandatory-reporting threshold. Section 6 protocol applies. The Cohort Companion (and Lead Companion) intervenes immediately; pastoral / clinical / legal protocols engage.**',
 '**The confession that crosses a reporting threshold — harm involving a minor above all. The safeguarding frame applies. The Cohort Companion (and Lead Companion) intervenes immediately; pastoral / clinical / legal protocols engage.**'),
('**If the confessed pattern crosses mandatory-reporting thresholds (current abuse of a minor, intent to harm self or others, ongoing illegal activity involving a third party). Virginia law applies without exception.',
 '**If the confessed pattern crosses mandatory-reporting thresholds (current abuse of a minor, intent to harm self or others, ongoing illegal activity involving a third party). The mandatory-reporting law applies without exception.'),
('**If a confession surfaces material larger than confession is for (trauma, dissociation, panic). Stop the pair work. Cohort Companion stays. Pastoral / clinical referral within 48 hours. Section 6 protocol.**',
 '**If a confession surfaces material larger than confession is for (trauma, dissociation, panic). Stop the pair work. Cohort Companion stays. Pastoral / clinical referral within 48 hours. The safeguarding frame applies.**'),
('Cohort Companion stays; Co-Companion (if available) continues holding the cohort. Brief offer to step out.**',
 'Cohort Companion stays; Co-Companion (if available) continues holding the circle. Brief offer to step out.**'),
('**If a participant’s confessed pattern involves another participant in the program (a spouse, a teen, a friend).',
 '**If a participant’s confessed pattern involves another participant in the program (a spouse, a colleague, a friend).'),
('**Default. Section 6 of the Going Deeper Handbook covers anything that crosses the safety threshold. Pastoral / clinical backup confirmed by name and number.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy) covers anything that crosses the safety threshold. Pastoral / clinical backup confirmed by name and number.**'),
('The Getting Started’s Wk 5 introduced confession in the cohort circle at the level of ‘name a place where you want to walk in greater honesty.’',
 'Getting Started’s Wk 6 introduced confession in the circle at the level of ‘name a place where you want to walk in greater honesty.’'),
('**•** Getting Started Wk 6 (foundational) — cohort circle confession of one place to walk in greater honesty.',
 '**•** Getting Started Wk 6 (foundational) — circle confession of one place to walk in greater honesty.'),
('each pair is held by the other pairs in the cohort space, even though the pairs themselves are private.',
 'each pair is held by the other pairs in the circle space, even though the pairs themselves are private.'),
('Make sure the team has the same vocabulary the cohort circles will use. (10 min)',
 'Make sure the team has the same vocabulary the circles will use. (10 min)'),
('**•** Confirm cohort spaces — each space needs room for pairs to sit knee-to-knee',
 '**•** Confirm circle spaces — each space needs room for pairs to sit knee-to-knee'),
('**•** Chairs in main room as one large circle for opening; three cohort spaces ready for the split.',
 '**•** Chairs in main room as one large circle for opening; circle spaces ready for the split.'),
('**•** Within each cohort space: enough buffer for pairs to sit knee-to-knee at least 6 feet apart. Some cohorts may need to use additional rooms; if so, two-adult rule applies (no pair in a fully closed-off room without a Cohort Companion within sight or earshot).',
 '**•** Within each circle space: enough buffer for pairs to sit knee-to-knee at least 6 feet apart. Some circles may need to use additional rooms; if so, the two-Companions practice applies (no pair in a fully closed-off room without a Cohort Companion within sight or earshot).'),
('**•** Tissues in every cohort space.',
 '**•** Tissues in every circle space.'),
('**•** Large-print Bible (ESV) in each cohort space.',
 '**•** Large-print Bible (ESV) in each circle space.'),
('**•** Wall clock or visible timer in each cohort space; the Lead Companion carries one as well.',
 '**•** Wall clock or visible timer in each circle space; the Lead Companion carries one as well.'),
('| Day before | Walk every cohort space. Confirm pair-buffer geometry. Confirm pastoral / clinical backup. | Lead Comp |',
 '| Day before | Walk every circle space. Confirm pair-buffer geometry. Confirm pastoral / clinical backup. | Lead Comp |'),
('| T-30 min | Cohort Companions prep their cohort spaces. Handouts placed. Pairs identified. | All Companions |',
 '| T-30 min | Cohort Companions prep their circle spaces. Handouts placed. Pairs identified. | All Companions |'),
('| T-15 min | Door opens. Welcome each participant by name. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. |'),
('| 7:34–8:12 | Block 5: Confession-and-restoration in standing pairs | Cohort circles → pairs | Cohort Facs |',
 '| 7:34–8:12 | Block 5: Confession-and-restoration in standing pairs | Circles → pairs | Cohort Comps |'),
('| 8:19–8:23 | Block 7: Between-session practice | Shared circle | Co-Comp (Parent) |',
 '| 8:19–8:23 | Block 7: Between-session practice | Shared circle | Co-Comp |'),
('**FOUR — To one trusted pair partner. Not the cohort circle. Not the spouse who is in another cohort. Your standing pair, who has held the partnership across two weeks of check-ins.**',
 '**FOUR — To one trusted pair partner. Not the circle. Not your spouse across the room. Your standing pair, who has held the partnership across two weeks of check-ins.**'),
('If what surfaces is that someone is mistreating or abusing them — especially a minor describing a parent, caregiver, or adult — do **not** redirect them to “confess your own reaction.”',
 'If what surfaces is that someone is mistreating or abusing them — or that a minor in their world is being harmed — do **not** redirect them to “confess your own reaction.”'),
('Receive it, do not assign them responsibility for another’s sin, and follow the Crisis Contingencies / Section 6 and mandatory-reporting steps.',
 'Receive it, do not assign them responsibility for another’s sin, and follow the Crisis Contingencies, the safeguarding frame, and the mandatory-reporting steps.'),
('*“In the cohort space, the Cohort Companion will walk you through the protocol once more, briefly.',
 '*“In the circle space, the Cohort Companion will walk you through the protocol once more, briefly.'),
('*“Junior teens with [name]. Senior teens with [name]. Parents with [name]. Forty minutes of pair work plus protocol time. Go.”*',
 '*“Circle assignments are on the wall. Forty minutes of pair work plus protocol time. Go.”*'),
('Each cohort circle splits into the standing pairs. The Cohort Companion floats; intervenes only when needed.',
 'Each circle splits into the standing pairs. The Cohort Companion floats; intervenes only when needed.'),
('**Inside the cohort circle — Companion script**',
 '**Inside the circle — Companion script**'),
('**•** If a confession crosses safety thresholds — stop the pair. Cohort Companion stays. Section 6 protocol; pastoral / clinical / legal as needed.',
 '**•** If a confession crosses safety thresholds — stop the pair. Cohort Companion stays. The safeguarding frame; pastoral / clinical / legal as needed.'),
('even if the cohort circle ends 5 minutes late.',
 'even if the circle ends 5 minutes late.'),
('## Script — Co-Companion (parent cohort) leads',
 '## Script — a Co-Companion leads'),
('**•** Anyone whose confession involved someone in the program. Cross-cohort follow-up by the appropriate Companions.',
 '**•** Anyone whose confession involved someone in the program. Cross-circle follow-up by the appropriate Companions.'),
('**•** Any teen whose confession crossed a mandatory-reporting threshold. Engage protocols immediately.',
 '**•** Any confession that crossed a mandatory-reporting threshold. Engage protocols immediately.'),
('that is not your sin to confess — it is something to tell your Cohort Companion or a trusted adult. Being wronged is never the thing you confess.*',
 'that is not your sin to confess — it is something to tell your Cohort Companion, or the named adult outside the cohort (the door the year keeps open). Being wronged is never the thing you confess.*'),
('**For the youngest (12–14): default to the simpler gratitude-led three-beat used in Getting Started and on the Rhythm Card — Awareness, Gratitude (three specific gifts), and one forward sentence with God — and let the named-pattern movements be optional. Gratitude leads; the pattern noticing is never the point of the prayer.**',
 '**If the named-pattern movements grow heavy: default to the simpler gratitude-led three-beat from Getting Started and the Rhythm Card — Awareness, Gratitude (three specific gifts), and one forward sentence with God — and let the pattern movements rest for a day. Gratitude leads; the pattern noticing is never the point of the prayer.**'),
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

**Those doing this work for the first time**

## Adjustments

**The architecture in plain words if the vocabulary stalls: ‘a pattern in me’ — one thing, owned, laid down. The five elements still apply.**

**Watch for: the member whose pattern is about someone else rather than themselves. Re-frame: ‘What’s YOUR pattern, regardless of what they do?’**

**But first discern: if the “they” is genuinely harming the member, do NOT re-frame to “your pattern” — being harmed is not a sin to confess. Receive it and follow the safeguarding frame, with the mandatory-reporting steps if a minor is involved.**

**Watch for: the member whose pattern is generic (‘I sin sometimes’). Help them find specificity: ‘Pick ONE specific thing you did this week that you wish you had not done.’**

**Watch for: the pair partner who is uncomfortable speaking the specific blessing of restoration. The Cohort Companion coaches the partner in the moment, modeling phrasing if needed: ‘In Christ, this is forgiven. The Father loves you and is making you whole.’**

**Watch for: the member who is genuinely flooded. Cohort Companion stays. Pastoral / clinical backup notified that night.**

**The veterans**

## Adjustments

**Full IJH architecture. Pair turns are 25 minutes each.**

**Watch for: the veteran who treats confession as performance. ‘My deepest sin pattern is...’ with a polished narrative. The Cohort Companion redirects gently: ‘What’s the smaller, more specific version of that?’**

**Watch for: the veteran who attempts to confess on behalf of someone else in the room. Stop immediately. ‘Confession is for your own pattern, not anyone else’s.’**

**Watch for: the veteran whose confession involves another member of the cohort. Receive without naming them. Brief the other circle’s Cohort Companion confidentially. Pastoral 1:1 within the week if the dynamic is acute.**

**The ordained and the staff**

## Adjustments

**Watch for: the leader whose confession surfaces a long-held pattern that has been hidden for years. ‘I have been hiding \\_\\_\\_\\_\\_ for fifteen years and have never named it aloud.’ Receive without rushing. The naming is significant work; the architecture holds. Pastoral 1:1 within the week if welcomed.**

**Watch for: the leader whose confession involves their spouse. Receive without naming the spouse. The relational adjudication is a different conversation; pastoral 1:1 within 24 hours.**

**Watch for: the leader whose confession involves the congregation or a colleague. The leader’s pattern is the confession; what was named is not a license to re-open it with the third party this week. Pastoral 1:1 first.**

**Watch for: the confession that reveals ongoing infidelity, financial fraud, or abuse where a third party is being harmed. The Cohort Companion does not adjudicate in the room. Pastoral 1:1 within 24 hours; the path to addressing the harm is part of the restoration, not a postscript.**

**Watch for: the intellectualized confession (‘I have a pattern of failing to operationalize my stated values’). The ordained are fluent enough to hide inside their fluency. Help find the concrete behavior: ‘What’s the specific behavior that you would name as the pattern?’**

**Watch for: the leader who realizes mid-confession that the pattern is rooted in a knot they did not name in Wk 3. Honour the discovery; the pattern is the confession; the knot is for the standing pair this week.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD05: {len(E)}+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
