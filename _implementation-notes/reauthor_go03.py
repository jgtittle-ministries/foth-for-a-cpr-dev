# GO Week 3 adult re-authoring: where am I being sent (circle-split discernment).
import io, sys, re
f = 'docs/going-out/week-03-where-sent.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Cohort-split discernment — each member articulates a specific sent-context using the language of gift, shadow, calling, and witness*',
 '*Circle-split discernment — each member articulates a specific sent-context using the language of gift, shadow, calling, and witness*'),
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('**Mode.** Cohort-split into junior teens / senior teens / parents (45 min each, parallel). The merge for shared circle close (15 min). Standing pairs do their work first within each cohort space.',
 '**Mode.** Circle-split into circles of four to eight (45 min, parallel). The merge for shared circle close (15 min). Standing pairs do their work first within each circle space.'),
('The standing pair walks the sentence with each other (12 min per direction). The cohort circle hears each member’s sentence around the room (15–20 min).',
 'The standing pair walks the sentence with each other (12 min per direction). Each circle hears each member’s sentence around the room (15–20 min).'),
('**Senior-teen vocational projection. A senior teen names a sent-context that is actually their parent’s vocational projection (‘I’m sent to study medicine to help people’, when the medicine framing is the parent’s, not the teen’s). Cohort Companion notices; pastoral 1:1 outside the session.**',
 '**Borrowed vocational projection. A member names a sent-context that is actually someone else’s projection for them (‘I’m sent to lead the men’s ministry’, when the framing is the senior pastor’s, not theirs). Cohort Companion notices; pastoral 1:1 outside the session.**'),
('**Parent re-deployment of Going Deeper calling. A parent’s Wk 10 Discerner role from Going Deeper sometimes becomes a default sent-context for Going Out.',
 '**Re-deployment of the Going Deeper calling. A member’s Wk 10 Discerner role from Going Deeper sometimes becomes a default sent-context for Going Out.'),
('**Cross-cohort overlap. A parent’s sent-context and their teen’s sent-context may overlap (a parent sent to family-of-origin while their teen is sent to extended family). Cross-cohort awareness held by Companions; not adjudicated in the cohort space.**',
 '**Cross-circle overlap. Spouses’ sent-contexts may overlap (one sent to family-of-origin while the other is sent to the same extended family). Cross-circle awareness held by Companions; not adjudicated in the circle space.**'),
('**If a senior teen’s sent-context surfaces a parent-teen tension publicly (the parent in a different cohort would not affirm the sentence). Gentle redirect; Cohort Companion holds the tension privately; pastoral cross-cohort conversation outside the session.**',
 '**If a member’s sent-context surfaces a spousal tension publicly (the spouse in a different circle would not affirm the sentence). Gentle redirect; Cohort Companion holds the tension privately; pastoral conversation with each spouse outside the session.**'),
('the receiver is named in initials only or as ‘a family member’; the cross-cohort person does not enter the discernment publicly.**',
 'the receiver is named in initials only or as ‘a family member’; the person does not enter the discernment publicly.**'),
('**If a teen names a sent-context that crosses a safety threshold (the teen is being called to confront an abusive family member, or to engage a peer in active crisis). Section 6 protocol immediately. Mandatory-reporting law applies as relevant.**',
 '**If a member names a sent-context that crosses a safety threshold (being called to confront an abusive family member, or to engage someone in active crisis). The safeguarding frame governs (Leadership Year Handbook §7 and the host church’s policy); a disclosure about a minor may still carry reporting duties. Mandatory-reporting law applies as relevant.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1 (carried forward).**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('The cohort split allows each cohort space to handle the developmental texture of its members — junior teens hold the discernment differently than senior teens, who hold it differently than parents. The merge at the close brings the body together to receive the named contexts as a body. Wks 4–9 build from this body of contexts.',
 'The circle split gives each member a small room to walk the discernment in — a circle of four to eight can hear a working sentence with an attention the whole room cannot. The merge at the close brings the body together to receive the named contexts as a body. Wks 4–9 build from this body of contexts.'),
('**5.** Special cases discussed: members whose H11.3 question is interior rather than missional; members whose sent-context is likely to involve cross-cohort family members; members whose discernment supports outside the cohort are weak. (15 min)',
 '**5.** Special cases discussed: members whose H11.3 question is interior rather than missional; members whose sent-context is likely to involve a spouse or family member in the room; members whose discernment supports outside the cohort are weak. (15 min)'),
('**•** Three flip charts — one in each cohort space — with markers, for capturing each cohort’s named sent-contexts.',
 '**•** A flip chart in each circle space, with markers, for capturing each circle’s named sent-contexts.'),
('**•** Confirm room layout: three cohort spaces (junior, senior, parent) plus shared circle at the close. The transition between cohort split and merge needs visible flow.',
 '**•** Confirm room layout: circle spaces for circles of four to eight, plus shared circle at the close. The transition between circle split and merge needs visible flow.'),
('**•** Three cohort spaces, each with chairs in a small circle. Shared circle space at the close (the chairs may not need to move — cohort circles can flow into the larger shared circle).',
 '**•** Circle spaces, each with chairs in a small circle. Shared circle space at the close (the chairs may not need to move — the circles can flow into the larger shared circle).'),
('**•** Three flip charts (one per cohort) with markers.',
 '**•** Flip charts (one per circle) with markers.'),
('*Times below assume a 7:00 PM start. The cohort split runs blocks 3–6. The merge at the close is the architectural pivot from individual discernment to shared body of contexts.*',
 '*Times below assume a 7:00 PM start. The circle split runs blocks 3–5. The merge at the close is the architectural pivot from individual discernment to shared body of contexts.*'),
('| 7:20–7:25 | Transition to cohort spaces | All | All Companions | Brief move into cohort circles. |',
 '| 7:20–7:25 | Transition to circle spaces | All | All Companions | Brief move into the circles. |'),
('| 7:59–8:12 | Block 5: Cohort circle hears each member | Cohort circles | Cohort Companions | Each member shares the sentence around the cohort circle. Companion captures on flip chart. |',
 '| 7:59–8:12 | Block 5: The circle hears each member | Circles | Cohort Companions | Each member shares the sentence around the circle. Companion captures on flip chart. |'),
('| 8:12–8:16 | Transition + bring flip charts to shared space | All | All Companions | Cohorts merge in the shared circle; flip charts visible. |',
 '| 8:12–8:16 | Transition + bring flip charts to shared space | All | All Companions | Circles merge in the shared circle; flip charts visible. |'),
('| Lead Companion | Lead names patterns across the three flip charts; brief weighing; the body holds the body of contexts. |',
 '| Lead Companion | Lead names patterns across the flip charts; brief weighing; the body holds the body of contexts. |'),
('**•** The cohort split tonight is so each member has cohort-specific room to walk the architecture with peers facing similar developmental textures. The merge at the close brings the body together to receive the named contexts as a body.',
 '**•** The circle split tonight is so each member has a small room to walk the architecture in, with peers close enough to hear the specifics. The merge at the close brings the body together to receive the named contexts as a body.'),
('**ONE — You will write a working sentence in your cohort space. 12 minutes silent.**',
 '**ONE — You will write a working sentence in your circle space. 12 minutes silent.**'),
('**THREE — The cohort circle hears each member’s sentence around the room. Brief; specific; each sentence captured on a flip chart by the Cohort Companion.**',
 '**THREE — Your circle hears each member’s sentence around the room. Brief; specific; each sentence captured on a flip chart by the Cohort Companion.**'),
('**FOUR — The cohort merges. The three flip charts come into the shared circle. The body sees the body of contexts together.**',
 '**FOUR — The circles merge. The flip charts come into the shared circle. The body sees the body of contexts together.**'),
('*“Go now to your cohort spaces. Junior teens with [Cohort Companion]. Senior teens with [Cohort Companion]. Parents with [Cohort Companion]. Take a few minutes to settle into the cohort space; then begin Block 3.”*',
 '*“Go now to your circle spaces — circle assignments are on the wall, circles of four to eight, each with its Companion. Take a few minutes to settle into the circle space; then begin Block 3.”*'),
('**Block 5 — Cohort Circle Hears Each Member (7:59–8:12, 13 min, cohort-split)**',
 '**Block 5 — The Circle Hears Each Member (7:59–8:12, 13 min, circle-split)**'),
('*“Around our cohort circle. Each of us reads the working sentence aloud, briefly — about 30 seconds. I will capture each on the flip chart so the merge can see all of our cohort’s contexts together.”*',
 '*“Around our circle. Each of us reads the working sentence aloud, briefly — about 30 seconds. I will capture each on the flip chart so the merge can see all of our circle’s contexts together.”*'),
('*(Around the cohort. 30–40 seconds per member. Cohort Companion captures on flip chart — brief phrase or paraphrase, not full sentence.)*',
 '*(Around the circle. 30–40 seconds per member. Cohort Companion captures on flip chart — brief phrase or paraphrase, not full sentence.)*'),
('*“Good. We hold our cohort’s body of contexts. The shared circle merge follows.”*',
 '*“Good. We hold our circle’s body of contexts. The shared circle merge follows.”*'),
('*“Three flip charts. Three cohorts. The body of Going Out sent-contexts. Let me read what surfaced — not every sentence, but the patterns I see.”*',
 '*“The flip charts — one from each circle. The body of Going Out sent-contexts. Let me read what surfaced — not every sentence, but the patterns I see.”*'),
('*(Lead Companion stands by the three flip charts; reads briefly across them; names 3–5 patterns. Specific.)*',
 '*(Lead Companion stands by the flip charts; reads briefly across them; names 3–5 patterns. Specific.)*'),
('*(Examples: ‘Multiple junior teens are sent to friends in their school context, with the witness being honesty about hard things. Multiple senior teens are sent to college decisions or post-graduation transitions, with the witness being trust under uncertainty. Multiple parents are sent to family-of-origin or to vocational contexts, with the witness being faithful presence under long pressure.’)*',
 '*(Examples: ‘Several of us are sent to our workplaces, with the witness being honesty under pressure. Several are sent to family-of-origin, with the witness being faithful presence under long cost. Several are sent inside the congregation itself, with the witness being truth spoken as a person, not from the office.’)*'),
('**•** Each cohort produced a flip chart of working sentences, with most members naming specific contexts and the small set without sentences naming honest obstacles.',
 '**•** Each circle produced a flip chart of working sentences, with most members naming specific contexts and the small set without sentences naming honest obstacles.'),
('**•** The merge surfaced cross-cohort patterns the Lead Companion named cleanly.',
 '**•** The merge surfaced cross-circle patterns the Lead Companion named cleanly.'),
('**•** Time pressure compressed the cohort-circle sharing or the merge.',
 '**•** Time pressure compressed the circle sharing or the merge.'),
('**•** Cross-cohort dynamics surfaced in the merge that should have been handled privately.',
 '**•** Cross-circle dynamics surfaced in the merge that should have been handled privately.'),
('**•** Any senior teen whose sent-context is in tension with parent expectations.',
 '**•** Any member whose sent-context is in tension with a spouse’s expectations.'),
('**•** Any parent whose sent-context overlaps with a teen-in-the-cohort’s context.',
 '**•** Any member whose sent-context overlaps with their spouse-in-the-room’s context.'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
for old, new, want in [
    ('12 min, cohort-split)**', '12 min, circle-split)**', 1),
    ('22 min, cohort-split)**', '22 min, circle-split)**', 1),
    ('| Cohort circles | Cohort Companions |', '| Circles | Cohort Companions |', 1),
    ('| Cohort circles (in pairs) | Cohort Companions float |', '| Circles (in pairs) | Cohort Companions float |', 1),
]:
    n = s.count(old)
    if n != want:
        print(f'!! count={n} (want {want}): {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

*Tonight splits into circles of four to eight. The Cohort Companions read their own circle’s members through the writing, the pair work, and the sharing.*

**Those doing this work for the first time**

## Adjustments

**First-timers often arrive at sent-context naming with concrete relational worlds (the workplace team, the neighbourhood, a sibling, a small group). The concrete is exactly right; work for specificity inside it.**

**Watch for: the first-timer whose sent-context is named in the language of an inherited church culture (‘I am sent to be a witness to my unsaved friends’). Receive without contradicting; gently work for specificity (‘Which friend, specifically? What does the witness look like in your actual week?’).**

**Watch for: the first-timer whose sent-context is family-of-origin (‘my father,’ ‘my sister’). Honour. Often the most consequential witness in the room. Pastoral support for the cost.**

**Watch for: the first-timer who cannot yet name a sent-context. Receive cleanly; the obstacle sentence is honest data, and for many the first season’s work is the discernment itself.**

**Watch for: the first-timer whose sent-context surfaces something that crosses a safety threshold. The safeguarding frame governs; pastoral 1:1 immediately after the session.**

**The veterans**

## Adjustments

**Veterans often arrive with vocational discernment as the dominant frame — a role transition, a long-held question about their work, an emerging call. The Spirit’s sending often intersects with this; receive both.**

**Watch for: the veteran whose sent-context names a vocational direction. Honour AND push for specificity (‘What does the witness look like inside the work? Inside that role’s relational world?’).**

**Watch for: the veteran whose sent-context is a relational world that may not last (a team being reorganized, a friendship circle dissolving, a season ending). Honour; Going Out’s witness is real even in temporary contexts.**

**Watch for: the veteran who carries the Wk 10 Discerner role from Going Deeper and whose Going Out sent-context is the integration of that calling. Honour cleanly.**

**Watch for: the veteran whose sentence is performative — named to land well in the circle. Cohort Companion notices privately; pastoral 1:1 outside the session.**

**The ordained and the staff**

## Adjustments

**The ordained face a specific temptation tonight: a sent-context that is simply the job description. ‘I am sent to my congregation’ may be the Spirit — or the office speaking. Push gently for a context beside the role, or a quality of witness the role cannot supply: ‘Where are you sent as a person, where nobody is paying you to be there?’**

**Watch for: the leader whose sent-context is a marital or family-of-origin context with cost. Honour; pastoral support for the cost; the circle holds without prescribing.**

**Watch for: the leader whose sent-context is in tension with a spouse’s expectations, or overlaps with a spouse-in-the-room’s context. Cross-circle awareness held privately by Companions; pastoral conversation with each spouse if needed.**

**Watch for: the leader whose sent-context surfaces vocational rupture or transition (a role ending; a calling re-emerging; a resignation being weighed). Receive cleanly tonight; pastoral 1:1 within the week to walk the larger discernment.**

**Watch for: the leader who names too many sent-contexts. Gentle redirect to ONE for Going Out. ‘The other contexts are real; Going Out’s work is one.’**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO03: {len(E)}+4 counted + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|Asker|cohort space|cohort split|cohort-split|cohort circle|three flip)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
