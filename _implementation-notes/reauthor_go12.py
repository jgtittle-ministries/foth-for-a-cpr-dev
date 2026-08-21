# GO Week 12 adult re-authoring: sending into the long obedience (the year's close).
# Continuation frame: 'Going Deeper round 2' -> the family year (host church's decision, per the seriousness gate).
import io, sys, re
f = 'docs/going-out/week-12-long-obedience.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('receive the H12.1 sending card; bridge to whatever continues (Going Deeper round 2 for some; honest non-continuation for others; long obedience for all).',
 'receive the H12.1 sending card; bridge to whatever continues (the family year for some; honest non-continuation for others; long obedience for all).'),
('**Mode.** Whole-room. The cohort sits as one body for the closing. No cohort split tonight.',
 '**Mode.** Whole-room. The cohort sits as one body for the closing. No circle split tonight.'),
('Members continuing to Going Deeper round 2 (when offered) re-engage at that point. Members not continuing carry the year’s formation into their individual contexts.',
 'Members confirmed for the family-year team re-engage when that work begins. Members not continuing carry the year’s formation into their individual contexts.'),
('**Members not continuing into Going Deeper round 2. The bridge block engages this honestly.',
 '**Members not continuing into the family-year team. The bridge block engages this honestly.'),
('**The senior teen leaving for college or post-graduation. Wk 12 carries the senior’s departure layered with the cohort’s formal close. Two grief vectors operate; honor both; pastoral support for the layered transition.**',
 '**The member leaving — a move, a role change, a season ending. Wk 12 carries their departure layered with the cohort’s formal close. Two grief vectors operate; honor both; pastoral support for the layered transition.**'),
('(sensing they are being called away from CCA, sensing a vocational rupture, sensing a marital or family rupture)',
 '(sensing they are being called away from the host church, sensing a vocational rupture, sensing a marital or family rupture)'),
('**If a senior’s closing reveals significant transition crisis (unable to imagine post-graduation life without the cohort, family conflict about post-graduation direction): pastoral 1:1; spiritual-direction support; family conversation outside the cohort space.**',
 '**If a member’s closing reveals significant transition crisis (unable to imagine the next season without the cohort’s weekly rhythm, household conflict about the direction ahead): pastoral 1:1; spiritual-direction support; household conversation outside the room.**'),
('**If a teen’s closing reveals concerns about returning to a household where Going Out’s formation has produced family-system tension: cross-cohort pastoral conversation; mandatory-reporting law applies if abuse or harm is involved.**',
 '**If a member’s closing reveals concerns about a household where the year’s formation has produced family-system tension: pastoral conversation with the household in view, spouses separately if needed; mandatory-reporting law applies if abuse or harm is involved.**'),
('**If a member’s decision about Going Deeper round 2 continuation produces acute distress (member who wants to continue but cannot for life-stage reasons; member who feels pressured by the cohort to continue when they need to step out): pastoral 1:1; the architecture protects honest non-continuation.**',
 '**If a member’s decision about the family-year team produces acute distress (a member who wants to serve but cannot for life-stage reasons; a member who feels pressured to continue when they need to step out): pastoral 1:1; the architecture protects honest non-continuation — the host church’s discernment is a covering, not a draft.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1. The team’s pastoral availability extends beyond the formal series’ close for at least 30 days as transition support.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy). The team’s pastoral availability extends beyond the formal series’ close for at least 30 days as transition support.**'),
('A year of weekly cohort meetings ends tonight — Getting Started (15 weeks, when applicable), 12 weeks of Going Deeper, the interlude, 12 weeks of Going Out.',
 'A year of weekly cohort meetings ends tonight — fifteen weeks of Getting Started, twelve of Going Deeper, twelve of Going Out, with the practice holds and the breaks between.'),
('The bridge to what continues is honest. Some members will continue to Going Deeper round 2 (when offered); some will not.',
 'The bridge to what continues is honest. Some members will go on to the family-year team, as the host church’s discernment confirms; some will not continue.'),
('**•** All of Going Out Going Out.',
 '**•** All of Going Out.'),
('**3.** Cohort review. Each Cohort Companion reports their cohort’s state heading into closing — members continuing to Going Deeper round 2; members not continuing; pairs that struggled; pairs that produced significant material; acute pastoral situations. (20 min)',
 '**3.** Cohort review. Each Cohort Companion reports their circle’s state heading into closing — members likely headed to the family-year team; members not continuing; pairs that struggled; pairs that produced significant material; acute pastoral situations. (20 min)'),
('**5.** Special cases: pair partnerships that struggled; members not continuing; senior teens in transition; the Wk 10 Discerner from Going Deeper; members whose Wk 11 assessment surfaced unresolved material. (15 min)',
 '**5.** Special cases: pair partnerships that struggled; members not continuing; members in transition; the Wk 10 Discerner from Going Deeper; members whose Wk 11 assessment surfaced unresolved material. (15 min)'),
('| Lead Companion | Honest framing of continuation possibilities; Going Deeper round 2; long obedience. |',
 '| Lead Companion | Honest framing of continuation possibilities; the family year; long obedience. |'),
('**RELEASING, NOT DISSOLVING. The body is released to continued formation in different rhythms. Going Deeper round 2 is offered to those who want it. The long obedience continues for everyone. The cohort is not dissolving; it is being released.**',
 '**RELEASING, NOT DISSOLVING. The body is released to continued formation in different rhythms. The family year opens for those the discernment confirms. The long obedience continues for everyone. The cohort is not dissolving; it is being released.**'),
('*“ONE — GOING DEEPER ROUND 2. For those who want to continue with another formal cohort cycle, Going Deeper round 2 will be offered [confirm timing per CCA pilot calendar]. Registration logistics will be handled outside this session. The architecture is not assumed; some members will continue, some will not, both are honest.”*',
 '*“ONE — THE FAMILY YEAR. For those whom the exit discernment and the host church confirm for the family-year team, that work opens [confirm timing per the host church’s calendar]. The discernment and the decision belong to the host church; those conversations happen outside this session. The architecture is not assumed; some members will serve, some will not, both are honest.”*'),
('**•** The bridge to what continues honored honest range — some continuing to round 2; some not; long obedience for all.',
 '**•** The bridge to what continues honored honest range — some toward the family year; some not; long obedience for all.'),
('**•** The bridge to round 2 became implicit pressure to continue.',
 '**•** The bridge to the family year became implicit pressure to continue.'),
('**•** Any senior in significant transition crisis.',
 '**•** Any member in significant transition crisis.'),
('**•** Any member whose continuation to round 2 was decided in tension or under pressure.',
 '**•** Any member whose continuation toward the family year was decided in tension or under pressure.'),
('**•** Any parent whose closing surfaced cross-cohort dynamics requiring further pastoral conversation.',
 '**•** Any member whose closing surfaced cross-circle dynamics requiring further pastoral conversation.'),
('Some Companions may continue to round 2; some may step out for a season; team composition for round 2 is named in a separate team conversation across the next two weeks.',
 'Some Companions may continue into the family year; some may step out for a season; team composition for what follows is named in a separate team conversation across the next two weeks.'),
('**•** Document what worked and what didn’t across the formation arc for future cohort cycles. The pilot edition has been a working text; Going Out revisions inform what becomes the next version.',
 '**•** Document what worked and what didn’t across the formation arc for future cohort cycles. The adult edition has been a working text; Going Out revisions inform what becomes the next version.'),
('**SEASONALLY — What round of formation are you in? Going Deeper round 2 (if continuing); informal continuing connection (if pair-rhythm continues); long obedience (regardless of structured cohort).**',
 '**SEASONALLY — What round of formation are you in? The family-year team (if confirmed); informal continuing connection (if pair-rhythm continues); long obedience (regardless of structured cohort).**'),
('## WHAT ROUND OF FORMATION? Going Deeper round 2 (if continuing); informal continuing connection; long obedience (regardless of structured cohort).',
 '## WHAT ROUND OF FORMATION? The family-year team (if confirmed); informal continuing connection; long obedience (regardless of structured cohort).'),
('**Possibility 1 — Going Deeper Round 2**',
 '**Possibility 1 — The Family Year**'),
('## FOR. Members who want another formal cohort cycle; members whose discernment in Wks 10–11 surfaced that the long obedience needs continued formal structure for this season.',
 '## FOR. Members whom the exit discernment and the host church confirm for the family-year team — the work this leadership year exists to prepare.'),
('**WHAT IT IS. Twelve more weeks of the Going Deeper architecture, with Going Out’s formation as the foundation. The cohort may include continuing members, new members, or both. Round 2 is not Getting Started; new pacing per CCA pilot calendar.**',
 '**WHAT IT IS. The family edition of Fellowship of the Heart, run for the households the host church serves, with this year’s formation as the team’s foundation. The host church holds the calendar and the decision.**'),
('**REGISTRATION. Logistics handled outside this session. Pastoral 1:1 across the next 2 weeks if you are uncertain.**',
 '**THE DECISION. It belongs to the host church, with the covering’s read and the year’s evidence in view. Pastoral 1:1 across the next 2 weeks if you are uncertain.**'),
('## FOR. Every member regardless of round 2 status or pair continuation status.',
 '## FOR. Every member regardless of family-year status or pair continuation status.'),
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

*Tonight there is no circle split. The Cohort Companions read their own circle’s members through the blessings and the close.*

**Those doing this work for the first time**

## Adjustments

**First-timers often experience closing concretely — the specific rituals and physical actions are real and significant. The blessing block, the standing-together Aaronic, the sending card are all carried forward as concrete memories.**

**Watch for: the first-timer whose closing produces unexpected grief. Receive cleanly; pastoral 1:1 within the week.**

**Watch for: the first-timer whose pair partnership produced thin material. Cohort Companion supports privately; the architecture honors what is.**

**Watch for: the first-timer whose continuation toward the family year is uncertain because of life-stage. Pastoral support; the architecture protects honest non-continuation.**

**Watch for: the first-timer whose closing surfaces concerning material requiring pastoral / clinical support. The safeguarding frame governs if needed.**

**The veterans**

## Adjustments

**Veterans often carry layered grief at closing — the cohort’s formal end PLUS whatever transition their own season holds. Two grief vectors operate; honor both.**

**Watch for: the veteran whose blessing block produces significant material with their pair partner. Pastoral support; the relationship may continue across whatever transition follows.**

**Watch for: the veteran who is moving away and whose family-year participation is geographically impossible. Pastoral support; honest acknowledgment of the constraint; standing-pair connection across distance is honored.**

**Watch for: the veteran whose Wk 10 Discerner role from Going Deeper has produced a calling now being formally sent at the close. Pastoral 1:1; spiritual-direction beyond the cohort.**

**The ordained and the staff**

## Adjustments

**The ordained have walked the year carrying multiple roles — member, rotation leader, sometimes the covering’s own colleague. Tonight is the closing they cannot run: one more night of receiving, not directing. The Lead Companion holds the room; the leader’s part is to be blessed, to speak one sentence, to stand in the circle like everyone else.**

**Watch for: the leader who feels the family year is obligatory because of the office — that a pastor cannot honestly not continue. The discernment is real and the office is not a draft notice; the host church’s decision covers a no as fully as a yes. Pastoral 1:1 if the pressure operates.**

**Watch for: the leader in position to influence the continuation logistics who begins planning the family year tonight. Honour the gift while naming the discipline: the architecture’s integrity is the closing, not the planning of what follows.**

**Watch for: the leader who has been a strong contributor and whose closing produces unexpected grief. The contribution is real; the grief is honest. Pastoral support for the closing transition.**

**Watch for: the leader whose closing surfaces significant unfinished material from the year. Pastoral 1:1; the long obedience continues.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO12: {len(E)} pairs + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|cross-cohort|round 2|Going Deeper round|cohort split)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
