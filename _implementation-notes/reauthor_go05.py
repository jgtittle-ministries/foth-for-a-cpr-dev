# GO Week 5 adult re-authoring: the household witness (life roles KEPT; room machinery converted).
import io, sys, re
f = 'docs/going-out/week-05-household.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('**Mode.** Cohort-split into junior teens / senior teens / parents (60 min each, parallel). The merge for shared circle close (10 min).',
 '**Mode.** Circle-split into circles of four to eight (60 min, parallel). The merge for shared circle close (10 min).'),
('Standing pair work in cohort spaces — each pair walks the household witness substantively (15 min per direction). Cohort circle hears patterns from the pair work (10 min).',
 'Standing pair work in circle spaces — each pair walks the household witness substantively (15 min per direction). Each circle hears patterns from the pair work (10 min).'),
('This week’s outside-cohort Tell shifts to the VOCATIONAL domain (workplace, school, professional context).',
 'This week’s outside-cohort Tell shifts to the VOCATIONAL domain (workplace, ministry, professional context).'),
('**Cross-cohort family Tells. A teen’s household Tell involves their parent who is in another cohort, or vice versa. The cohort split tonight protects the developmental space; cross-cohort awareness is held privately by Companions; pastoral conversation outside the session as needed.**',
 '**Cross-circle spouse Tells. A member’s household Tell involves their spouse who is in another circle. The circle split tonight protects the pair space; cross-circle awareness is held privately by Companions; pastoral conversation outside the session as needed.**'),
('**Parenting material that involves a teen in the cohort. A parent’s household witness work surfaces concerns about their own teen who is in another cohort. The architecture refuses adjudication; pastoral cross-cohort conversation OUTSIDE the session.**',
 '**Parenting material with a spouse in the room. A member’s household witness work surfaces parenting concerns their spouse — seated in another circle tonight — carries differently. The architecture refuses adjudication; pastoral conversation with the couple OUTSIDE the session.**'),
('**Domestic violence material. If a member’s household Tell or pair work reveals current or recent domestic abuse, Section 6 protocol immediately. The cohort space is not the venue; pastoral and clinical referrals required; safety is the first concern.**',
 '**Domestic violence material. If a member’s household Tell or pair work reveals current or recent domestic abuse, the safeguarding frame governs immediately (Leadership Year Handbook §7 and the host church’s policy). The room is not the venue; pastoral and clinical referrals required; safety is the first concern.**'),
('**If domestic violence is disclosed (current or recent): Section 6 protocol immediately. Pastoral / clinical / law enforcement referrals as appropriate.',
 '**If domestic violence is disclosed (current or recent): the safeguarding frame governs immediately (Leadership Year Handbook §7 and the host church’s policy). Pastoral / clinical / law enforcement referrals as appropriate.'),
('**If a member’s household witness work surfaces acute mental-health crisis (their own or a household member’s): pastoral 1:1 immediately; clinical referrals; Section 6 protocol.**',
 '**If a member’s household witness work surfaces acute mental-health crisis (their own or a household member’s): pastoral 1:1 immediately; clinical referrals; the safeguarding frame governs.**'),
('**If a marriage in the cohort surfaces material across both members’ cohorts (one in parent cohort, one in another — unusual but possible) that suggests rupture: cross-cohort pastoral conversation with both partners separately; couples’ therapy referral as appropriate; the cohort space is not the venue.**',
 '**If a marriage in the cohort surfaces material across both spouses’ circles that suggests rupture: pastoral conversation with both partners separately; couples’ therapy referral as appropriate; the room is not the venue.**'),
('**If a teen’s household Tell reveals their parent is the source of harm: mandatory-reporting law applies. The teen Companion stays close to the teen; pastoral safety planning; clinical referrals; the cohort space supports the teen without exposing the family dynamics in the room.**',
 '**If a member’s household Tell reveals someone in their home is the source of harm: safety first; mandatory-reporting law applies where a minor or vulnerable adult is at risk. The Cohort Companion stays close to the member; pastoral safety planning; clinical referrals; the room supports the member without exposing the family dynamics.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1 (carried forward).**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('Tonight’s cohort-split lets each developmental stage engage the household with appropriate texture. Junior teens engage parents and siblings; senior teens engage the household they are about to leave (or have just left); parents engage spouse, children, and extended family-of-origin. The standing pair work — substantive, 15 minutes per direction — carries most of the formation tonight.',
 'Tonight’s circle split gives each member a small room for costly material. The household configurations in an adult cohort differ widely — a spouse and children at home; an empty nest; a single household; family-of-origin at a distance; an aging parent being cared for in the home. The standing pair work — substantive, 15 minutes per direction — carries most of the formation tonight.'),
('**•** Going Out WWks 1–4. Body-sent architecture; sent-context sentence; three modes; daily-Tells data.',
 '**•** Going Out Wks 1–4. Body-sent architecture; sent-context sentence; three modes; daily-Tells data.'),
('Second — review your cohort’s members one by one with their household configuration in mind. Who is married? Who has a complex family-of-origin? Who is in active estrangement? Who is in long caregiving? Who has cross-cohort family material? Bring the cohort-mapping to the team meeting.',
 'Second — review your circle’s members one by one with their household configuration in mind. Who is married? Who has a complex family-of-origin? Who is in active estrangement? Who is in long caregiving? Whose spouse is in the room? Bring the circle-mapping to the team meeting.'),
('**3.** Cohort-by-cohort review. Each Cohort Companion reports their cohort’s household configurations and known dynamics. The team holds these together. (25 min)',
 '**3.** Circle-by-circle review. Each Cohort Companion reports their circle’s household configurations and known dynamics. The team holds these together. (25 min)'),
('members with cross-cohort family material; members with childhood-abuse history;',
 'members whose spouse is in the room; members with childhood-abuse history;'),
('**5.** Walk the run sheet. Cohort-split rhythm; substantive pair work; cohort circle pattern surfacing; brief merge. Time discipline. (10 min)',
 '**5.** Walk the run sheet. Circle-split rhythm; substantive pair work; circle pattern surfacing; brief merge. Time discipline. (10 min)'),
('**•** Three flip charts — one per cohort space — with markers, for capturing patterns.',
 '**•** A flip chart in each circle space, with markers, for capturing patterns.'),
('**•** Confirm room layout: three cohort spaces; shared circle space at the close.',
 '**•** Confirm room layout: circle spaces for circles of four to eight; shared circle space at the close.'),
('**•** Three cohort spaces with chairs in small circles. Shared circle for opening / closing.',
 '**•** Circle spaces with chairs in small circles. Shared circle for opening / closing.'),
('**•** Three flip charts.',
 '**•** Flip charts (one per circle).'),
('**•** Wall clock or timer in each cohort space.',
 '**•** Wall clock or timer in each circle space.'),
('| 7:20–7:25 | Transition to cohort spaces | All | All Companions | Move into cohort circles. |',
 '| 7:20–7:25 | Transition to circle spaces | All | All Companions | Move into the circles. |'),
('| 7:25–7:53 | Block 3: Standing pair work | Cohort circles (in pairs) | Cohort Companions float | 15 min per direction; 30 min total. |',
 '| 7:25–7:53 | Block 3: Standing pair work | Circles (in pairs) | Cohort Companions float | 15 min per direction; 30 min total. |'),
('| 7:53–8:06 | Block 4: Cohort circle pattern surfacing | Cohort circles | Cohort Companions | Each member briefly: ONE pattern. Companion captures on flip chart. |',
 '| 7:53–8:06 | Block 4: Circle pattern surfacing | Circles | Cohort Companions | Each member briefly: ONE pattern. Companion captures on flip chart. |'),
('| 8:06–8:11 | Transition + bring flip charts to shared space | All | All Companions | Cohorts merge. |',
 '| 8:06–8:11 | Transition + bring flip charts to shared space | All | All Companions | Circles merge. |'),
('| Lead Companion | Lead names cross-cohort patterns; brief weighing. |',
 '| Lead Companion | Lead names cross-circle patterns; brief weighing. |'),
('*“Go to your cohort spaces. Junior teens with [Cohort Companion]. Senior teens with [Cohort Companion]. Parents with [Cohort Companion]. The pair work begins after a brief settling.”*',
 '*“Go to your circle spaces — assignments are on the wall, circles of four to eight, each with its Companion. The pair work begins after a brief settling.”*'),
('**Block 3 — Standing Pair Work (7:25–7:53, 28 min, cohort-split)**',
 '**Block 3 — Standing Pair Work (7:25–7:53, 28 min, circle-split)**'),
('If a pair surfaces material indicating active domestic violence, abuse, or safety threshold crossing: Cohort Companion stays close immediately; pastoral 1:1 within minutes of the session’s close; Section 6 protocol.**',
 'If a pair surfaces material indicating active domestic violence, abuse, or safety threshold crossing: Cohort Companion stays close immediately; pastoral 1:1 within minutes of the session’s close; the safeguarding frame governs.**'),
('**Time discipline. At 15 min: switch. At 30 min: stop. The cohort circle’s pattern surfacing needs its time.**',
 '**Time discipline. At 15 min: switch. At 30 min: stop. The circle’s pattern surfacing needs its time.**'),
('**Block 4 — Cohort Circle Pattern Surfacing (7:53–8:06, 13 min, cohort-split)**',
 '**Block 4 — Circle Pattern Surfacing (7:53–8:06, 13 min, circle-split)**'),
('*“Around our cohort circle. Each of us, briefly — about 30–40 seconds. ONE pattern from your pair work.',
 '*“Around our circle. Each of us, briefly — about 30–40 seconds. ONE pattern from your pair work.'),
('*“I will capture key patterns on the flip chart so the merge can see what our cohort is bringing.”*',
 '*“I will capture key patterns on the flip chart so the merge can see what our circle is bringing.”*'),
('*(Around the cohort. 30–40 seconds per member. Cohort Companion captures on flip chart.)*',
 '*(Around the circle. 30–40 seconds per member. Cohort Companion captures on flip chart.)*'),
('*“Good. We hold our cohort’s body of household witness. The shared circle merge follows.”*',
 '*“Good. We hold our circle’s body of household witness. The shared circle merge follows.”*'),
('**If a member’s pattern reveals cross-cohort dynamics (a parent in another cohort): use indirect language; the Companion captures it on the flip chart in non-identifying form.**',
 '**If a member’s pattern reveals cross-circle dynamics (a spouse in another circle): use indirect language; the Companion captures it on the flip chart in non-identifying form.**'),
('*“Three flip charts. Three cohorts. The body of household witness patterns. Let me read what surfaced — patterns, not detail.”*',
 '*“The flip charts — one from each circle. The body of household witness patterns. Let me read what surfaced — patterns, not detail.”*'),
('*(Lead Companion stands by the three flip charts; reads briefly across them; names 3–5 patterns. Specific. Drawn from what was actually shared.)*',
 '*(Lead Companion stands by the flip charts; reads briefly across them; names 3–5 patterns. Specific. Drawn from what was actually shared.)*'),
('‘Multiple cohorts surfaced the same pattern: the household witness most needed is the one most avoided.',
 '‘Multiple circles surfaced the same pattern: the household witness most needed is the one most avoided.'),
('*“Good. Wk 6 is the vocational witness. This week’s Tell is in workplace, school, or vocational context. Bring your honest engagement.”*',
 '*“Good. Wk 6 is the vocational witness. This week’s Tell is in workplace, ministry, or professional context. Bring your honest engagement.”*'),
('**•** The merge integrated three cohort flip charts into a body-of-household-witness picture.',
 '**•** The merge integrated the circles’ flip charts into a body-of-household-witness picture.'),
('**•** Cross-cohort family material was held privately; no adjudication in the cohort space.',
 '**•** Cross-circle spouse material was held privately; no adjudication in the room.'),
('**•** Cross-cohort family material surfaced in the merge inadequately handled.',
 '**•** Cross-circle spouse material surfaced in the merge inadequately handled.'),
('**•** Anyone whose pair work surfaced active domestic violence, abuse, or safety threshold crossing — Section 6 protocol.',
 '**•** Anyone whose pair work surfaced active domestic violence, abuse, or safety threshold crossing — the safeguarding frame governs.'),
('**•** Any cross-cohort family material; pastoral conversation with both teen and parent separately.',
 '**•** Any cross-circle spouse material; pastoral conversation with each spouse separately.'),
('**•** Any senior whose pair work surfaced significant material about preparing to leave the household.',
 '**•** Any member whose pair work surfaced significant material about a household transition under way (a move, a separation, a child leaving home).'),
('**ONE — This week’s outside-cohort Tell is in the VOCATIONAL domain. Workplace (parents). School / classmates / teachers (teens). The daily-rhythm context where you spend the bulk of your hours.**',
 '**ONE — This week’s outside-cohort Tell is in the VOCATIONAL domain. Workplace, ministry, professional context — the daily-rhythm context where you spend the bulk of your hours.**'),
('tell your Cohort Companion or another trusted adult — that is not disloyalty; it is the brave and faithful thing.**',
 'tell your Cohort Companion or someone you trust outside the room — that is not disloyalty; it is the brave and faithful thing.**'),
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

*Tonight splits into circles of four to eight. Every member holds the same discipline: ONE relational dyad for the pair work, not the household-as-system. The Cohort Companions read their own circle’s members through the pair work and the pattern surfacing.*

**Those doing this work for the first time**

## Adjustments

**First-timers often find the household witness is mostly silent presence. Honour. Verbal witness in the closest relationships develops slowly; the witness of years of ordinary faithfulness is already real.**

**Watch for: the first-timer whose household is in active rupture (a divorce in process, a family crisis, a recent bereavement). The pair work surfaces this; pastoral 1:1 within 24 hours.**

**Watch for: the first-timer whose household includes step-family, blended-family, or non-biological caregiving relationships. The architecture honors the household as it is, not as it might be.**

**Watch for: the first-timer whose pair work surfaces harm in the home — theirs or someone else’s. The safeguarding frame governs; safety first; pastoral 1:1 immediately after the session.**

**The veterans**

## Adjustments

**Veterans are often in households whose structure is changing — children leaving home, a move under consideration, retirement approaching, an aging parent moving in. The household witness is layered with the question of transition: how does witness change as the relational structure changes?**

**Watch for: the veteran whose witness has been suppressed in the household for years because the dynamics have not allowed it. Wk 5 may be the first time they name what could be possible. Honour without rushing toward action.**

**Watch for: the veteran whose Tell-receiver was a sibling. The witness is real; the sibling relationship is often where the most consequential family-of-origin witness happens.**

**Watch for: the veteran whose pair work surfaces unresolved family-of-origin material from decades ago. Pastoral 1:1 within the week; clinical referral if significant trauma is surfacing.**

**The ordained and the staff**

## Adjustments

**The ordained often carry the most complex household domain — spouse, children, family-of-origin, sometimes caregiving — plus a dynamic no one else in the room has: a household that lives with the office. A pastor’s family is watched by a congregation; the home can quietly become an extension of the church. The household witness tonight is as a person — the spouse and children have already seen through everything else.**

**Watch for: the leader whose pair work surfaces marital tension. The architecture protects: pattern, not detail; the spouse is not the pair partner; the Cohort Companion supports the pair without intervening in the marriage.**

**Watch for: the leader whose spouse is IN the room tonight, in another circle. Cross-circle awareness held privately; pastoral conversation with the couple outside the session if the pair work surfaces material both carry.**

**Watch for: the leader in active caregiving for an aging parent or an ill family member. The witness in long faithfulness is real; sabbath-rhythm conversation in pastoral 1:1.**

**Watch for: the leader whose Tell-receiver was their own adult child. Honour; this is often where a leader’s most consequential household witness happens.**

**Watch for: the leader in a single / non-traditional household configuration (single, divorced, widowed). The architecture applies; the household domain is whatever the actual household is, not what congregational expectations imagine.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO05: {len(E)} pairs + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|junior|senior|CCA|Warrenton|Section 6|Virginia|classmates?|cross-cohort|cohort space|cohort circle|cohort-split|school)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
