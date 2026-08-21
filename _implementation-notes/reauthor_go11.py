# GO Week 11 adult re-authoring: where the cohort lands as a body (five-level assessment).
import io, sys, re
f = 'docs/going-out/week-11-cohort-lands.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('**Mode.** Cohort-split into junior teens / senior teens / parents (50 min each, parallel) for honest assessment within developmental peer group. The merge for shared circle integration (15 min).',
 '**Mode.** Circle-split into circles of four to eight (50 min, parallel) for honest assessment within a smaller room. The merge for shared circle integration (15 min).'),
('Cohort-split honest assessment using H11.1 worksheet (30 min). Cohort circle articulates the cohort’s landing on the five-level taxonomy (15 min). Merge into shared circle; Lead Companion integrates the three cohort assessments into a body-level reading (15 min).',
 'Circle-split honest assessment using H11.1 worksheet (30 min). Each circle articulates its landing on the five-level taxonomy (15 min). Merge into shared circle; Lead Companion integrates the circle assessments into a body-level reading (15 min).'),
('**Cross-cohort divergence. Junior teens land at Level 3; senior teens land at Level 4-with-tension; parents land at Level 3-with-Level-4-emerging. The body’s overall level is set by the lowest stable common practice, not by the average. The merge integrates honestly; the body lands at one level, even when cohorts saw it differently.**',
 '**Cross-circle divergence. One circle lands at Level 3; another at Level 4-with-tension; a third at Level 3-with-Level-4-emerging. The body’s overall level is set by the lowest stable common practice, not by the average. The merge integrates honestly; the body lands at one level, even when the circles saw it differently.**'),
('**The cohort that diverges sharply from each other’s readings. Three cohorts arrive at three different levels with no shared frame. This may indicate the cohorts have been in different formation environments — or that one cohort’s reading is unrealistic. The merge’s discipline is honest weighing.**',
 '**The circles that diverge sharply from each other’s readings. The circles arrive at different levels with no shared frame. This may indicate the circles have been in different formation environments — or that one circle’s reading is unrealistic. The merge’s discipline is honest weighing.**'),
('**Honest no for further continuation. The cohort’s assessment may surface that some members are not continuing into Going Deeper round 2 or any further formal cohort work.',
 '**Honest no for further continuation. The cohort’s assessment may surface that some members are not continuing into what follows the year — the family-year team or any further formal cohort work.'),
('**Cross-cohort family material. A teen and parent in different cohorts arrive at significantly different cohort assessments because their experience of the cohort’s body has been shaped by different cohort spaces. The architecture honors both readings; cross-cohort dynamics held privately.**',
 '**Cross-circle spouse material. Two spouses in different circles arrive at significantly different assessments because their experience of the body has been shaped by different circle spaces. The architecture honors both readings; the dynamics held privately.**'),
('mandatory-reporting law applies where relevant; Section 6 protocol; pastoral / leadership / clinical referrals immediately.**',
 'mandatory-reporting law applies where relevant; the safeguarding frame governs; pastoral / leadership / clinical referrals immediately.**'),
('**If a senior’s assessment surfaces grief about leaving the cohort just as the cohort has reached a meaningful level: honour the grief; pastoral support for the transition; the cohort’s sending will hold the senior in continued connection.**',
 '**If a member’s assessment surfaces grief about leaving the cohort just as it has reached a meaningful level (a move, a role change): honour the grief; pastoral support for the transition; the cohort’s sending will hold them in continued connection.**'),
('**If a parent’s assessment surfaces material involving their teen’s formation that crosses pastoral thresholds: cross-cohort pastoral conversation outside the session; mandatory-reporting law applies if appropriate.**',
 '**If a member’s assessment surfaces material involving another member’s formation or conduct that crosses pastoral thresholds: pastoral conversation outside the session; mandatory-reporting law applies if appropriate.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('The honest assessment then was the foundation for Going Out’s Going Out — the cohort started where it actually landed, not where it imagined itself to be.',
 'The honest assessment then was the foundation for Going Out — the cohort started where it actually landed, not where it imagined itself to be.'),
('The cohort split tonight is honest — each developmental cohort assesses within its own peer group first, because experiences of the body differ across cohorts. Junior teens experienced the cohort’s shared circle and their own cohort’s smaller circle differently than parents did; senior teens at the threshold of leaving experienced the body differently than parents who will likely continue. The merge integrates the three cohort assessments into one body-level reading honestly.',
 'The circle split tonight is honest — each circle assesses within its own smaller room first, because experiences of the body differ across the room. A first-timer experienced the shared circle and their own circle differently than a twenty-year elder did; a member in transition experienced the body differently than one who will likely continue. The merge integrates the circle assessments into one body-level reading honestly.'),
('**•** All twelve weeks of Going Out Going Out.',
 '**•** All twelve weeks of Going Out.'),
('**3.** Cohort review. Each Cohort Companion reports their cohort’s likely reading; the team discusses likely cross-cohort divergence. (20 min)',
 '**3.** Cohort review. Each Cohort Companion reports their circle’s likely reading; the team discusses likely cross-circle divergence. (20 min)'),
('**5.** Special cases: members likely to dissent from cohort consensus; cohorts likely to land at significantly different levels; the cohort regression scenario; the gnostic-community concern. (15 min)',
 '**5.** Special cases: members likely to dissent from the working consensus; circles likely to land at significantly different levels; the cohort regression scenario; the gnostic-community concern. (15 min)'),
('**•** Three flip charts — one per cohort space.',
 '**•** A flip chart in each circle space.'),
('**•** Confirm room layout: three cohort spaces; shared circle for opening / closing / merge.',
 '**•** Confirm room layout: circle spaces for circles of four to eight; shared circle for opening / closing / merge.'),
('**•** Three cohort spaces with chairs in small circles. Shared circle for opening / closing / merge.',
 '**•** Circle spaces with chairs in small circles. Shared circle for opening / closing / merge.'),
('**•** Three flip charts.',
 '**•** Flip charts (one per circle).'),
('**•** Wall clock or timer in each cohort space.',
 '**•** Wall clock or timer in each circle space.'),
('| 7:20–7:25 | Transition to cohort spaces | All | All Companions | Move into cohort circles. |',
 '| 7:20–7:25 | Transition to circle spaces | All | All Companions | Move into the circles. |'),
('| 7:25–7:53 | Block 3: Cohort-split honest assessment | Cohort circles | Cohort Companions | 30 min: each cohort assesses honestly using H11.1; flip chart capture. |',
 '| 7:25–7:53 | Block 3: Circle-split honest assessment | Circles | Cohort Companions | 30 min: each circle assesses honestly using H11.1; flip chart capture. |'),
('| 7:53–8:06 | Block 4: Cohort circle articulates landing | Cohort circles | Cohort Companions | Each cohort lands on its assessment of the body; flip chart final. |',
 '| 7:53–8:06 | Block 4: The circle articulates its landing | Circles | Cohort Companions | Each circle lands on its assessment of the body; flip chart final. |'),
('| 8:06–8:11 | Transition + bring flip charts to shared space | All | All Companions | Cohorts merge. |',
 '| 8:06–8:11 | Transition + bring flip charts to shared space | All | All Companions | Circles merge. |'),
('| Shared circle | Lead Companion | Lead integrates three cohort assessments into one body-level reading. |',
 '| Shared circle | Lead Companion | Lead integrates the circle assessments into one body-level reading. |'),
('*“Go to your cohort spaces. Junior teens with [Cohort Companion]. Senior teens with [Cohort Companion]. Parents with [Cohort Companion]. The cohort assessment begins after a brief settling.”*',
 '*“Go to your circle spaces — assignments are on the wall, circles of four to eight, each with its Companion. The circle assessment begins after a brief settling.”*'),
('**Block 3 — Cohort-Split Honest Assessment (7:25–7:53, 28 min, cohort-split)**',
 '**Block 3 — Circle-Split Honest Assessment (7:25–7:53, 28 min, circle-split)**'),
('*“Your cohort space. Thirty minutes of honest assessment. H11.1 has the worksheet.”*',
 '*“Your circle space. Thirty minutes of honest assessment. H11.1 has the worksheet.”*'),
('TWO — cohort circle: 15 minutes for each of us to share briefly — 30–40 seconds — where we read the cohort’s landing AND where we see the cohort’s honest level. THREE — cohort working consensus: 8 minutes to weigh, surface divergence honestly, land on the cohort’s reading of the body’s level. I will capture on flip chart.”*',
 'TWO — around the circle: 15 minutes for each of us to share briefly — 30–40 seconds — where we read the body’s landing AND where we see its honest level. THREE — the circle’s working consensus: 8 minutes to weigh, surface divergence honestly, land on this circle’s reading of the body’s level. I will capture on flip chart.”*'),
('AND — honest range: this cohort’s reading may differ from the others; the merge will integrate.”*',
 'AND — honest range: this circle’s reading may differ from the others; the merge will integrate.”*'),
('**During cohort circle sharing: captures readings on flip chart in three columns:',
 '**During the circle sharing: captures readings on flip chart in three columns:'),
('‘We have \\_\\_\\_ readings of Level 3, \\_\\_\\_ of Level 4, \\_\\_\\_ in between. Where does this cohort land in its honest assessment of the body?’ The cohort’s working consensus is what this cohort thinks the BODY is, not what each member is.**',
 '‘We have \\_\\_\\_ readings of Level 3, \\_\\_\\_ of Level 4, \\_\\_\\_ in between. Where does this circle land in its honest assessment of the body?’ The circle’s working consensus is what this circle thinks the BODY is, not what each member is.**'),
('**If member-level dissent surfaces (a member who reads the body significantly lower or higher than the cohort’s working consensus): receive cleanly; capture on flip chart explicitly; the merge holds the dissent.**',
 '**If member-level dissent surfaces (a member who reads the body significantly lower or higher than the circle’s working consensus): receive cleanly; capture on flip chart explicitly; the merge holds the dissent.**'),
('**If the cohort cannot reach working consensus: that is data; capture as ‘Cohort sees body at Level 3 OR Level 4 with honest divergence.’ The merge engages.**',
 '**If the circle cannot reach working consensus: that is data; capture as ‘Circle sees body at Level 3 OR Level 4 with honest divergence.’ The merge engages.**'),
('**Block 4 — Cohort Circle Articulates Landing (7:53–8:06, 13 min, cohort-split)**',
 '**Block 4 — The Circle Articulates Its Landing (7:53–8:06, 13 min, circle-split)**'),
('*“Our cohort’s articulation. We landed on \\_\\_\\_\\_\\_. The supporting data: \\_\\_\\_\\_\\_.',
 '*“Our circle’s articulation. We landed on \\_\\_\\_\\_\\_. The supporting data: \\_\\_\\_\\_\\_.'),
('The cohort’s articulation is not unanimous — it is the cohort’s working consensus held with honest range.”*',
 'The circle’s articulation is not unanimous — it is the circle’s working consensus held with honest range.”*'),
('*(Around the cohort. 30 seconds per member. Cohort Companion captures any dissents on flip chart.)*',
 '*(Around the circle. 30 seconds per member. Cohort Companion captures any dissents on flip chart.)*'),
('*“Good. Our cohort’s flip chart will go to the merge.”*',
 '*“Good. Our circle’s flip chart will go to the merge.”*'),
('**The articulation includes the LEVEL the cohort lands on AND the supporting data AND honest divergence AND comparison to Going Deeper.**',
 '**The articulation includes the LEVEL the circle lands on AND the supporting data AND honest divergence AND comparison to Going Deeper.**'),
('**If a cohort lands at a different level than expected (significantly higher or lower than the team’s pre-meet read): receive cleanly; the cohort’s reading is the cohort’s reading; the merge engages.**',
 '**If a circle lands at a different level than expected (significantly higher or lower than the team’s pre-meet read): receive cleanly; the circle’s reading is the circle’s reading; the merge engages.**'),
('**If the cohort’s articulation reveals significant material the cohort space cannot adjudicate (the cohort sees harm in the formation arc, the cohort sees regression, the cohort sees stagnation): pastoral attention immediately after the session.**',
 '**If the circle’s articulation reveals significant material the circle space cannot adjudicate (the circle sees harm in the formation arc, regression, stagnation): pastoral attention immediately after the session.**'),
('*“Three flip charts. Three cohort assessments. The body’s honest level.”*',
 '*“The flip charts — one from each circle. The body’s honest level.”*'),
('*(Lead Companion stands by the three flip charts; reads the cohort articulations briefly.)*',
 '*(Lead Companion stands by the flip charts; reads the circle articulations briefly.)*'),
('*“Junior teens read the body at \\_\\_\\_\\_\\_. Senior teens read the body at \\_\\_\\_\\_\\_. Parents read the body at \\_\\_\\_\\_\\_. Honest divergence (if any): \\_\\_\\_\\_\\_.”*',
 '*“One circle reads the body at \\_\\_\\_\\_\\_. Another at \\_\\_\\_\\_\\_. Another at \\_\\_\\_\\_\\_. Honest divergence (if any): \\_\\_\\_\\_\\_.”*'),
('*“The body’s honest level. The lowest stable common practice across all three cohorts. What I read across the three flip charts is \\_\\_\\_\\_\\_.”*',
 '*“The body’s honest level. The lowest stable common practice across all the circles. What I read across the flip charts is \\_\\_\\_\\_\\_.”*'),
('*(The Lead Companion names the body’s integrated level honestly. Specific. Drawn from the three cohort assessments. May acknowledge tension where the cohorts genuinely diverge.)*',
 '*(The Lead Companion names the body’s integrated level honestly. Specific. Drawn from the circle assessments. May acknowledge tension where the circles genuinely diverge.)*'),
('**•** The cohort-split assessments produced honest readings within each cohort; flattering self-assessment was named when it appeared and resisted.',
 '**•** The circle-split assessments produced honest readings within each circle; flattering self-assessment was named when it appeared and resisted.'),
('**•** The cohort circle articulations honored honest divergence within each cohort.',
 '**•** The circle articulations honored honest divergence within each circle.'),
('**•** The merge integrated three cohort assessments into one body-level reading honestly.',
 '**•** The merge integrated the circle assessments into one body-level reading honestly.'),
('**•** The cohort-split assessments produced flattering self-assessment that the architecture did not surface.',
 '**•** The circle-split assessments produced flattering self-assessment that the architecture did not surface.'),
('**•** Cross-cohort divergence was suppressed in the merge to produce false consensus.',
 '**•** Cross-circle divergence was suppressed in the merge to produce false consensus.'),
('**•** Any senior whose grief about leaving is significant.',
 '**•** Any member whose grief about leaving is significant.'),
('**•** Any parent whose teen’s formation surfaced concerns in the parent’s assessment.',
 '**•** Any member whose assessment surfaced concerns about another member’s formation or conduct.'),
('**•** Any cohort member whose continuation into Going Deeper round 2 is now in question.',
 '**•** Any cohort member whose continuation into what follows the year is now in question.'),
('standing-pair specific blessings spoken aloud; cohort circle Aaronic spoken together by the body; sending card given; bridge to whatever continues (Going Deeper round 2 for some; honest non-continuation for others; long obedience for all).**',
 'standing-pair specific blessings spoken aloud; the Aaronic spoken together by the body; sending card given; bridge to whatever continues (the family-year team for some; honest non-continuation for others; long obedience for all).**'),
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

*Tonight splits into circles of four to eight for the honest assessment. The Cohort Companions read their own circle’s members through the reading, the sharing, and the working consensus.*

**Those doing this work for the first time**

## Adjustments

**First-timers often read the body concretely — specific weeks that landed, specific Companion moments, specific shared experiences. Honour the concrete reading; it is often the most honest data in the room.**

**Watch for: the first-timer who under-reads the body because they remember confusing weeks more vividly than landed weeks. Cohort Companion offers gentle data: ‘Remember the household week; remember the discernment night — those landed.’**

**Watch for: the first-timer who over-reads the body because the laying-on-of-hands was emotionally significant. Distinguish between event and shared culture; events are real but the level is the shared culture.**

**Watch for: the first-timer whose reading reveals concerns about a specific Companion or member dynamic. Pastoral 1:1; mandatory-reporting law applies if abuse is involved.**

**The veterans**

## Adjustments

**Veterans often have the broadest comparative frame — they have been part of more groups, more communities, more long-running formation contexts. Their reading carries comparative weight.**

**Watch for: the veteran who reads the body lower because of comparison to other formation communities they have been in. Receive cleanly; the comparison may be honest data; may also be unfair to this cohort’s specific shape.**

**Watch for: the veteran who reads the body higher because the mission-far engagement felt significant. The engagement is real; the body’s level is shared culture across the formation arc, not a single arc of weeks.**

**Watch for: the veteran whose upcoming transition colors the assessment — grief about leaving can inflate or deflate the read. Honour both possibilities; pastoral 1:1 if the grief is significant.**

**Watch for: the veteran whose Wk 10 Discerner role from Going Deeper colors the assessment. The Discerner has been deeply embedded in the body’s discernment; their reading may carry weight; may also reflect their own experience more than the body’s.**

**The ordained and the staff**

## Adjustments

**The ordained have often evaluated groups for a living. The credentialed reading carries professional weight; the architecture honors it but does not hand the room to it — the housekeeper’s read of the body counts the same as the consultant’s.**

**Watch for: the leader who reads the body as a report on their own leadership — a low landing arrives as personal failure, a high landing as vindication. The body’s level is not the leader’s grade; the Cohort Companion names the distinction gently if it operates.**

**Watch for: the leader whose vocational connection to the work (church staff, ministry leadership) colors the assessment toward what the program needs the answer to be. Honest reading serves the program better than a flattering one; the architecture says so out loud.**

**Watch for: the leader for whom a low honest landing produces despair about the year. Receive cleanly; a body that lands honestly at Level 3 has done significant work; pastoral support; the long obedience continues.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO11: {len(E)} pairs + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|cross-cohort|cohort space|cohort circle|cohort-split|three cohorts|Going Deeper round)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
