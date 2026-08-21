# GD Week 6 adult re-authoring: PROAPT extended; cross-circle Tell; fix 'Going Deeperback' corruption.
import io, sys, re
f = 'docs/going-deeper/week-06-proapt.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Shared teaching of extended PROAPT (15 min). Cohort circles for the extended PROAPT itself (25 min). MERGE for the Tell step — each participant tells one specific person OUTSIDE their cohort what they heard (20 min).',
 '**Mode.** Shared teaching of extended PROAPT (15 min). Circles for the extended PROAPT itself (25 min). MERGE for the Tell step — each participant tells one specific person OUTSIDE their circle what they heard (20 min).'),
('‘I’m going to tell my husband.’ (Husband is in another cohort tonight; that counts.)',
 '‘I’m going to tell my husband.’ (Husband is in another circle tonight; that counts.)'),
('**The cross-cohort Tell creating awkwardness. The Tell is to someone OUTSIDE your cohort — by design. Some participants find this exposing. The structure is intentional: the Tell across cohorts strengthens the whole room and prevents the within-cohort echo chamber. The teaching frames this; the practice walks it.**',
 '**The cross-circle Tell creating awkwardness. The Tell is to someone OUTSIDE your circle — by design. Some participants find this exposing. The structure is intentional: the Tell across circles strengthens the whole room and prevents the within-circle echo chamber. The teaching frames this; the practice walks it.**'),
('**The teen telling a parent (or vice versa) who is in another cohort. This is intended; it is also asymmetrical. The protocol on H6.3 names the family case explicitly: brief, specific, no follow-on conversation tonight — the Tell stands as it is spoken.**',
 '**The member telling their spouse in another circle. This is intended; it is also different in kind. The protocol on H6.3 names the household case explicitly: brief, specific, no follow-on conversation tonight — the Tell stands as it is spoken.**'),
('**If a teen’s Tell to a parent (or vice versa) opens material that exceeds the moment. The Cohort Companion overseeing the Tell pairs follow-up briefly with both family members at the close:',
 '**If a spouse-to-spouse Tell opens material that exceeds the moment. The Cohort Companion overseeing the Tell pairs follows up briefly with both at the close:'),
('**Default. Section 6 of the Going Deeper Handbook covers anything that crosses the safety threshold. Pastoral / clinical backup confirmed by name and number for the night.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy) covers anything that crosses the safety threshold. Pastoral / clinical backup confirmed by name and number for the night.**'),
('It worked: most cohorts reported by Getting Started’s Wk 6 that PROAPT had become a habit for at least three or four days a week.',
 'It worked: most cohorts reported by the close of Getting Started’s PROAPT weeks that the practice had become a habit for at least three or four days a week.'),
('Each participant does extended PROAPT in their cohort circle; then the whole room merges; then each participant finds a specific partner from a DIFFERENT cohort and Tells that partner what they heard. The cross-cohort design prevents the within-cohort echo chamber and strengthens the whole room as a hearing community.',
 'Each participant does extended PROAPT in their circle; then the whole room merges; then each participant finds a specific partner from a DIFFERENT circle and Tells that partner what they heard. The cross-circle design prevents the within-circle echo chamber and strengthens the whole room as a hearing community.'),
('**•** Wk 4’s co-processing. Tonight’s cohort PROAPT is silent and individual, but the cohort space is co-processing the Spirit’s word in parallel — the Wk 4 frame applies.',
 '**•** Wk 4’s co-processing. Tonight’s circle PROAPT is silent and individual, but the circle space is co-processing the Spirit’s word in parallel — the Wk 4 frame applies.'),
('The standing pair is NOT the Tell partner tonight. The Tell partner is from a DIFFERENT cohort.',
 'The standing pair is NOT the Tell partner tonight. The Tell partner is from a DIFFERENT circle.'),
('Make sure the team has the same vocabulary the cohort circles will use. (10 min)',
 'Make sure the team has the same vocabulary the circles will use. (10 min)'),
('**3.** Walk the passage choices. Romans 12 vs. Psalm 32. Decide together: do all three cohorts work the same passage, or does junior get one and senior/parent another? Most pilots default to: juniors and new participants get Psalm 32; senior teens and parents who completed Getting Started get Romans 12. Confirm. (10 min)',
 '**3.** Walk the passage choices. Romans 12 vs. Psalm 32. Decide together: do all circles work the same passage, or is a default named by experience? Most cohorts default to: new participants get Psalm 32; veterans of Getting Started get Romans 12. Confirm. (10 min)'),
('**4.** Walk the cross-cohort Tell pairings. The pairings are NOT pre-assigned; they’re self-chosen in the merge. But the Cohort Companions identify in advance any participant who would struggle to find a Tell partner naturally (a teen whose only natural cross-cohort person is their parent and that’s acute right now, a parent whose teen isn’t in the program). The team has a fallback option for each. (10 min)',
 '**4.** Walk the cross-circle Tell pairings. The pairings are NOT pre-assigned; they’re self-chosen in the merge. But the Cohort Companions identify in advance any participant who would struggle to find a Tell partner naturally (a member whose only natural cross-circle person is their spouse and that’s acute right now, a new participant with little informal contact beyond their own circle). The team has a fallback option for each. (10 min)'),
('**•** Confirm cohort spaces — each space needs quiet writing time for 25 minutes;',
 '**•** Confirm circle spaces — each space needs quiet writing time for 25 minutes;'),
('**•** Chairs in main room as one large circle for opening; three cohort spaces ready for the split; back to one large circle for the Tell merge.',
 '**•** Chairs in main room as one large circle for opening; circle spaces ready for the split; back to one large circle for the Tell merge.'),
('**•** Tissues in each cohort space and main room.',
 '**•** Tissues in each circle space and main room.'),
('**•** Multiple copies of large-print Bibles (ESV) in each cohort space — enough for participants who don’t bring their own.',
 '**•** Multiple copies of large-print Bibles (ESV) in each circle space — enough for participants who don’t bring their own.'),
('**•** Wall clock or visible timer in each cohort space; the Lead Companion carries one as well for the merge.',
 '**•** Wall clock or visible timer in each circle space; the Lead Companion carries one as well for the merge.'),
('| 48 hr before | Team pre-meet (60 min). Passage decision. Cross-cohort Tell fallback list. | All Companions |',
 '| 48 hr before | Team pre-meet (60 min). Passage decision. Cross-circle Tell fallback list. | All Companions |'),
('| Day before | Walk every cohort space and main room. Confirm pastoral / clinical backup. | Lead Comp |',
 '| Day before | Walk every circle space and main room. Confirm pastoral / clinical backup. | Lead Comp |'),
('| T-30 min | Cohort Companions prep their cohort spaces. Handouts placed. Pens at every chair. | All Companions |',
 '| T-30 min | Cohort Companions prep their circle spaces. Handouts placed. Pens at every chair. | All Companions |'),
('| T-15 min | Door opens. Welcome each participant by name. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags, pens at every chair. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags, pens at every chair. |'),
('| 7:33–7:56 | Block 5: Extended PROAPT in cohort circles | Cohort circles (silent + brief share) | Cohort Facs | 20 min silent extended PROAPT; 5 min very brief cohort share — ONE specific thing each heard. |',
 '| 7:33–7:56 | Block 5: Extended PROAPT in circles | Circles (silent + brief share) | Cohort Comps | 20 min silent extended PROAPT; 5 min very brief circle share — ONE specific thing each heard. |'),
('| 7:56–8:15 | Block 6: Merge for the Tell step | Shared circle → cross-cohort pairs | Lead Comp | Frame the Tell. Cross-cohort pairing — each finds a partner from a DIFFERENT cohort. 12 min in pairs (each Tells; each receives). 4 min: voluntary public Tells (2–3). |',
 '| 7:56–8:15 | Block 6: Merge for the Tell step | Shared circle → cross-circle pairs | Lead Comp | Frame the Tell. Cross-circle pairing — each finds a partner from a DIFFERENT circle. 12 min in pairs (each Tells; each receives). 4 min: voluntary public Tells (2–3). |'),
('| 8:15–8:19 | Block 7: Between-session practice | Shared circle | Co-Comp (Parent) | Daily extended PROAPT this week. One Tell each weekday. |',
 '| 8:15–8:19 | Block 7: Between-session practice | Shared circle | Co-Comp | Daily extended PROAPT this week. One Tell each weekday. |'),
('We are going to do extended PROAPT in our cohorts; then we are going to merge; then each of you is going to tell ONE specific person from a DIFFERENT cohort what you specifically heard.',
 'We are going to do extended PROAPT in our circles; then we are going to merge; then each of you is going to tell ONE specific person from a DIFFERENT circle what you specifically heard.'),
('**Tonight makes the Tell happen IN the room. Each of you is going to find a partner from a DIFFERENT cohort — deliberately not your own cohort, deliberately not your standing pair — and Tell that partner what you specifically heard during cohort PROAPT.**',
 '**Tonight makes the Tell happen IN the room. Each of you is going to find a partner from a DIFFERENT circle — deliberately not your own circle, deliberately not your standing pair — and Tell that partner what you specifically heard during the circle PROAPT.**'),
('*“The cross-cohort Tell is design, not accident. Within-cohort echoes are real — you have heard each other six weeks of Tuesdays. Telling a teen, parent, or peer in another cohort makes the Tell land differently and strengthens the room as a hearing community. Wk 7’s corporate listening prayer and Wk 8’s group-hearing depend on this room being a cross-cohort hearing community; tonight is the first time we practice it.”*',
 '*“The cross-circle Tell is design, not accident. Within-circle echoes are real — you have heard each other six weeks of Tuesdays. Telling someone from another circle makes the Tell land differently and strengthens the room as a hearing community. Wk 7’s corporate listening prayer and Wk 8’s group-hearing depend on this room being a whole-cohort hearing community; tonight is the first time we practice it.”*'),
('*“Junior teens with [name] — default Psalm 32. Senior teens with [name] — default Romans 12. Parents with [name] — default Romans 12. Twenty-five minutes. Go.”*',
 '*“Circle assignments are on the wall. First-time participants — default Psalm 32; veterans — default Romans 12. Twenty-five minutes. Go.”*'),
('**Block 5 — Extended PROAPT in Cohort Circles (7:33–7:56, 23 min)**\nEach cohort circle works in parallel. The structure is identical.',
 '**Block 5 — Extended PROAPT in Circles (7:33–7:56, 23 min)**\nEach circle works in parallel. The structure is identical.'),
('**Inside the cohort circle — Companion script**',
 '**Inside the circle — Companion script**'),
('*“Twenty minutes silent extended PROAPT. Five minutes brief share — ONE specific thing each of you heard, around the circle.”*',
 '*“Twenty minutes silent extended PROAPT. Five minutes brief share — ONE specific thing each of you heard, around the circle.”*'),
('Default for our cohort is [Psalm 32 / Romans 12].',
 'Default for our circle is [Psalm 32 / Romans 12].'),
('## Cohort share (5 min)',
 '## Circle share (5 min)'),
('(Around the circle. With 8 people that is 4 minutes; with 12 people that is 6 minutes. If the cohort is large, only 2/3 share.)',
 '(Around the circle. With 8 people that is 4 minutes; with 12 people that is 6 minutes. If the circle is large, only 2/3 share.)'),
('We merge with the other cohorts in a moment for the Tell step.”*',
 'We merge with the other circles in a moment for the Tell step.”*'),
('Cohort Companion notes for pastoral 1:1; do not engage in the cohort circle.',
 'Cohort Companion notes for pastoral 1:1; do not engage in the circle.'),
('The merge for the Tell step is the formation centre of the night; do not let the cohort share run long.',
 'The merge for the Tell step is the formation centre of the night; do not let the circle share run long.'),
('All three cohorts return to the main room. Chairs are loose; the geometry is open for free movement.',
 'All circles return to the main room. Chairs are loose; the geometry is open for free movement.'),
('*“Find a partner from a DIFFERENT cohort. NOT your own cohort. NOT your standing pair. NOT your spouse if your spouse is in another cohort tonight (we will name a different protocol for that case in a moment). Look for a teen if you are a parent; look for a parent if you are a teen; look across the room.”*',
 '*“Find a partner from a DIFFERENT circle. NOT your own circle. NOT your standing pair. NOT your spouse (we will name a protocol for that case in a moment). Look across the room for the person you have worked with least.”*'),
('*“Special cases. If a teen Tells a parent (or vice versa) in another cohort, the Tell is brief, specific, and complete — no follow-on conversation tonight; the Tell stands as it is spoken; you can revisit at home if welcomed. If a spouse Tells a spouse in another cohort, same protocol — the Tell stands tonight; conversation continues at home.”*',
 '*“Special case. If a spouse Tells a spouse from another circle, the Tell is brief, specific, and complete — no follow-on conversation tonight; the Tell stands as it is spoken; the conversation continues at home if welcomed.”*'),
('## Cross-cohort pair Tell (12 min total)',
 '## Cross-circle pair Tell (12 min total)'),
('**Six minutes additional for participants without an obvious partner. Lead Companion and one Cohort Companion visibly available to help anyone unpaired find someone. Going Deeperback list from team pre-meet is engaged here.**',
 '**Six minutes additional for participants without an obvious partner. Lead Companion and one Cohort Companion visibly available to help anyone unpaired find someone. The Tell Buddies fallback list from team pre-meet is engaged here.**'),
('**If a Tell exceeds the moment (a teen telling a parent something heavy and the parent flooding, or vice versa), Cohort Companion gently intervenes:',
 '**If a Tell exceeds the moment (a spouse telling a spouse something heavy and the receiver flooding), Cohort Companion gently intervenes:'),
('what was it like to Tell it across cohorts to someone you don’t usually work with?”*',
 'what was it like to Tell it across circles to someone you don’t usually work with?”*'),
('‘This room is becoming a hearing community across cohorts.’ Or: ‘Several of you said the cross-cohort Tell felt different from a within-cohort share.’',
 '‘This room is becoming a hearing community across circles.’ Or: ‘Several of you said the cross-circle Tell felt different from a within-circle share.’'),
('## Script — Co-Companion (parent cohort) leads',
 '## Script — a Co-Companion leads'),
('**•** Each cohort circle had at least one participant whose Apply was specific (a verse, a thing, for tonight, for them).',
 '**•** Each circle had at least one participant whose Apply was specific (a verse, a thing, for tonight, for them).'),
('**•** The cohort share landed in 5 minutes. The Cohort Companion held the time.',
 '**•** The circle share landed in 5 minutes. The Cohort Companion held the time.'),
('**•** The cross-cohort merge produced visible cross-pairings — teens with parents, junior with senior, parent with teen-not-their-own — not within-cohort echo pairings.',
 '**•** The cross-circle merge produced visible cross-pairings — members paired with the people they have worked with least — not within-circle echo pairings.'),
('**•** The cohort share ran long; the cross-cohort merge got compressed.',
 '**•** The circle share ran long; the cross-circle merge got compressed.'),
('**•** Participants paired within cohorts despite the cross-cohort instruction. The teaching frame did not hold.',
 '**•** Participants paired within circles despite the cross-circle instruction. The teaching frame did not hold.'),
('**•** A teen-parent Tell exceeded the moment without the Cohort Companion noticing.',
 '**•** A spouse-to-spouse Tell exceeded the moment without the Cohort Companion noticing.'),
('**•** Several participants left without completing a Tell. Going Deeperback list was not engaged.',
 '**•** Several participants left without completing a Tell. The Tell Buddies fallback list was not engaged.'),
('**•** If cross-cohort pairing did not hold, Wk 8’s structure (the cohort hearing about itself) can re-anchor the cross-cohort architecture explicitly.',
 '**•** If cross-circle pairing did not hold, Wk 8’s structure (the cohort hearing about itself) can re-anchor the cross-circle architecture explicitly.'),
('**•** Anyone whose cross-cohort Tell created cross-family material (teen-parent, spouse-spouse) that requires pastoral support to land well at home. Pastoral 1:1 within 48 hours.',
 '**•** Anyone whose cross-circle Tell created household material (spouse to spouse) that requires pastoral support to land well at home. Pastoral 1:1 within 48 hours.'),
('Brief warm contact: ‘The Tell across cohorts is unusual the first time. The discipline grows; this week’s daily Tells will compound.’',
 'Brief warm contact: ‘The Tell across circles is unusual the first time. The discipline grows; this week’s daily Tells will compound.’'),
('**•** Anyone whose Tell-partner pairing was a teen-parent across cohorts and produced material at home that needs pastoral support. Cross-cohort follow-up by the appropriate Companions.',
 '**•** Anyone whose Tell-partner pairing was spouse-to-spouse across circles and produced material at home that needs pastoral support. Cross-circle follow-up by the appropriate Companions.'),
('## Find a partner from a DIFFERENT cohort. Not your own; not your standing pair; not your spouse only.',
 '## Find a partner from a DIFFERENT circle. Not your own; not your standing pair; not your spouse only.'),
('**Special case — family across cohorts. If you Tell your own teen, parent, or spouse from another cohort: brief, specific, complete tonight — no follow-on conversation in the room. You can revisit at home if welcomed.**',
 '**Special case — your spouse across circles. If you Tell your own spouse from another circle: brief, specific, complete tonight — no follow-on conversation in the room. You can revisit at home if welcomed.**'),
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

**Default passage: Psalm 32 (shorter, narrative, connects to Wk 5’s confession). Romans 12 is dense for a first extended PROAPT in 25 minutes.**

**Watch for: the member who shrinks the passage (‘I just used verse 1’). Gently: ‘Read the whole psalm. The whole thing is the passage tonight.’**

**Watch for: the member whose Apply is moralistic (‘so I should do better at praying’). Push for what was specifically heard: ‘What did the Spirit specifically point out to you tonight, in this passage, about THIS season of your life?’**

**Watch for: the member who hears nothing and feels like they did it wrong. Affirm aggressively. ‘Hearing nothing specific tonight is not failure. The architecture works on faithful presence.’**

**Watch for: the member who, in the cross-circle merge, pairs only with the people they already know. The point is cross-circle. Cohort Companion gently steers toward the least-familiar partner if needed.**

**The veterans**

## Adjustments

**Default passage: Romans 12 (or Psalm 32 if asked). Veterans of Getting Started have done enough PROAPT to handle the longer text. Full structure: 25 minutes; three read-throughs; full Observe and Apply.**

**Watch for: the veteran whose Apply is everything-at-once (‘five things I noticed’). Push to ONE: ‘Of those, which is the ONE for you tonight?’**

**Watch for: the veteran who finds the cross-circle Tell exposing. ‘I don’t really know that circle.’ The Lead Companion and Cohort Companion are visibly available to help; the Tell Buddies fallback list is engaged.**

**Watch for: the veteran whose extended PROAPT surfaces material from Wk 5’s confession that is still working. Cohort Companion: ‘What you heard tonight may be the next layer of last week’s work. Bring it to your standing pair this week.’**

**The ordained and the staff**

## Adjustments

**Watch for: the extended PROAPT that becomes academic (‘Paul is using a chiastic structure here’). The ordained have exegetical reflexes that can outrun their hearing. Affirm; redirect: ‘And what is the SPECIFIC thing the Spirit is highlighting for YOU tonight?’**

**Watch for: the survey Apply (‘Paul says X then Y then Z then —’). Push for ONE specific thing for tonight. The breadth is the read-and-observe steps; the focus is Apply.**

**Watch for: the intellectualized Apply (‘the principle of testing the will of God in v.2 applies to how I evaluate decision-making in my work’). Push toward concrete: ‘What is the SPECIFIC decision the Spirit is naming?’**

**Watch for: the leader whose Tell partner is their spouse from another circle. Brief, specific, complete tonight; conversation continues at home. The Tell is what was heard, not a marital topic.**

**Watch for: the leader who couldn’t finish the Apply step — stuck on Observe and out of time. Cohort Companion: ‘Carry the Apply into your daily PROAPT this week. Same passage; finish the Apply step; Tell someone tomorrow.’**

**Watch for: the leader whose extended PROAPT produces something they sense the congregation needs to hear. Hold. Tonight’s Tell is one person; what the church hears, and when, is discernment work with the covering, not tonight’s exercise.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD06: {len(E)}+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia|Deeperback)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
