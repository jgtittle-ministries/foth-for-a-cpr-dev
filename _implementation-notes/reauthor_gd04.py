# GD Week 4 adult re-authoring: co-processing; leader tells first in the centre chairs.
import io, sys, re
f = 'docs/going-deeper/week-04-co-processing.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Whole-room. No cohort split tonight.',
 '**Mode.** Whole-room. No circle split tonight.'),
('**Center.** Two participants — one teen, one parent — bring a short piece of their named knot from Wk 3 (≤8 minutes each) into the centre of the circle, supported by the Lead Companion.',
 '**Center.** Two volunteers — a Companion first, because the leader tells first, then a cohort member — bring a short piece of their named knot from Wk 3 (≤8 minutes each) into the centre of the circle, supported by the Lead Companion.'),
('**Cross-cohort exposure. Tonight a teen may see a parent doing real work; a parent may see a teen doing real work. This is intended, but it carries weight. Watch for any teen whose own parent’s visible work activates them; same in reverse. The Cohort Companion reads the room.**',
 '**Spouse exposure. Tonight a member may see their spouse doing real work — and the room may see one of its own leaders doing real work. This is intended, but it carries weight. Watch for anyone whose spouse’s visible work activates them, and for the member unsettled by seeing a leader under the work. The Cohort Companion reads the room.**'),
('**If a teen sees a parent doing visible work and is activated mid-session. The parent’s Cohort Companion (not the teen’s) is briefed in advance to watch for this. The teen’s Cohort Companion quietly checks in at the close. Pastoral 1:1 within the week if welcomed.**',
 '**If a member sees their spouse doing visible work and is activated mid-session. The volunteer’s Cohort Companion (not the spouse’s) is briefed in advance to watch for this. The spouse’s Cohort Companion quietly checks in at the close. Pastoral 1:1 within the week if welcomed.**'),
('**If a parent sees their own teen do visible work. Same protocol in reverse. The parent is checked on at the close; the teen is treated as a volunteer who has done a brave piece of work, not as a child whose parent watched. Boundary discipline.**',
 '**If the room sees its own pastor do visible work. The instinct will be to protect, or to marvel; both miss it. The pastor is treated as a volunteer who has done a brave piece of work, not as a leader whose room watched. Boundary discipline.**'),
('**Default. Section 6 of the Going Deeper Handbook covers anything that crosses the safety threshold. Pastoral / clinical backup confirmed by name and number for the night.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy) covers anything that crosses the safety threshold. Pastoral / clinical backup confirmed by name and number for the night.**'),
('The cohort split has been the architecture for Wks 2 and 3; tonight the whole cohort works as one.',
 'The circle split has been the architecture for Wks 2 and 3; tonight the whole cohort works as one.'),
('Third — confirm the two volunteers. The Lead Companion and one Cohort Companion have, by Saturday, identified two participants — one teen, one parent — who would bring a right-sized piece of work tonight.',
 'Third — confirm the two volunteers. The first is one of the Companions — the leader tells first, and tonight the room needs to see it. The Lead Companion and one Cohort Companion have, by Saturday, also identified one cohort member who would bring a right-sized piece of work tonight.'),
('The whole-room layout is unfamiliar; cohort spaces are not in use tonight.',
 'The whole-room layout is unfamiliar; circle spaces are not in use tonight.'),
('**5.** Cross-cohort exposure protocol. Identify in advance any teen whose parent’s visible work could activate them, and any parent whose teen’s visible work could activate them. The Cohort Companions NOT working with the volunteer that round are responsible for watching their own cohort’s members during the centre work. (5 min)',
 '**5.** Spouse-exposure protocol. Identify in advance anyone whose spouse’s visible work could activate them. The Cohort Companions NOT working with the volunteer that round are responsible for watching their own circles’ members during the centre work. (5 min)'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs with TWO empty chairs face-to-face in the centre, ready for the volunteer pieces.',
 '**•** Confirm room layout: ONE large circle — a chair for every member — with TWO empty chairs face-to-face in the centre, ready for the volunteer pieces.'),
('**•** Chairs in ONE large single circle, 20–32 chairs with two additional chairs face-to-face in the geometric centre.',
 '**•** Chairs in ONE large single circle, one per member, with two additional chairs face-to-face in the geometric centre.'),
('| 48 hr before | Team pre-meet (60 min). Volunteer review. Cross-cohort exposure protocol. | All Companions |',
 '| 48 hr before | Team pre-meet (60 min). Volunteer review. Spouse-exposure protocol. | All Companions |'),
('| T-15 min | Door opens. Welcome each participant by name. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. |'),
('| 7:30–7:45 | Block 4: Demonstration round 1 (teen volunteer) | Shared circle | Lead Companion + Volunteer |',
 '| 7:30–7:45 | Block 4: Demonstration round 1 (Companion volunteer) | Shared circle | Lead Companion + Volunteer |'),
('| 7:53–8:08 | Block 6: Demonstration round 2 (parent volunteer) | Shared circle | Lead Companion + Volunteer |',
 '| 7:53–8:08 | Block 6: Demonstration round 2 (member volunteer) | Shared circle | Lead Companion + Volunteer |'),
('| 8:16–8:21 | Block 8: Between-session practice | Shared circle | Co-Comp (Parent) |',
 '| 8:16–8:21 | Block 8: Between-session practice | Shared circle | Co-Comp |'),
('*“One. The whole room is one circle tonight. No cohort split. The cohort itself is the working instrument tonight, not the cohort circle. You will see why over the next ninety minutes.”*',
 '*“One. The whole room is one circle tonight. No circle split. The cohort itself is the working instrument tonight, not the small circle. You will see why over the next ninety minutes.”*'),
('*“Two. Two of you have agreed to bring brief pieces of your knot work into the centre of the circle tonight. You know who they are.',
 '*“Two. Two of us — one of the team first, because the leader tells first, then one of the cohort — have agreed to bring brief pieces of our knot work into the centre of the circle tonight. You know who they are.'),
('**Block 4 — Demonstration Round 1 (Teen Volunteer) (7:30–7:45, 15 min)**\nThe teen volunteer comes to one of the two centre chairs. The Lead Companion takes the other.',
 '**Block 4 — Demonstration Round 1 (Companion Volunteer) (7:30–7:45, 15 min)**\nThe Companion volunteer comes to one of the two centre chairs — the leader tells first, and the depth the room will risk tonight is licensed by what this Companion actually brings. The Lead Companion takes the other.'),
('**Block 6 — Demonstration Round 2 (Parent Volunteer) (7:53–8:08, 15 min)**\nIdentical structure to Block 4. The parent volunteer takes the centre chair; the Lead Companion takes the other.',
 '**Block 6 — Demonstration Round 2 (Member Volunteer) (7:53–8:08, 15 min)**\nIdentical structure to Block 4. The member volunteer takes the centre chair; the Lead Companion takes the other.'),
('**•** Junior teens may activate around a parent’s visible work in a way they did not around a teen volunteer’s. The Cohort Companion for the junior cohort is watching; offline contact at the close as needed.',
 '**•** A spouse may activate around their partner’s visible work in a way they did not around round 1. The spouse’s Cohort Companion is watching; offline contact at the close as needed.'),
('**•** The surfacing round may be different. Often parents in round 2 surface different material than teens did in round 1. Honour the difference; do not impose round 1’s pattern on round 2.',
 '**•** The surfacing round may be different. A member’s work often surfaces different material in the room than a Companion’s did in round 1. Honour the difference; do not impose round 1’s pattern on round 2.'),
('## Script — Co-Companion (parent cohort) leads',
 '## Script — a Co-Companion leads'),
('**•** A teen activated by a parent’s visible work was not followed up with at the close.',
 '**•** A member activated by a spouse’s visible work was not followed up with at the close.'),
('**•** Any junior teen who looked overwhelmed during round 2. Cohort Companion within 24 hours.',
 '**•** Anyone who looked overwhelmed during round 2. Cohort Companion within 24 hours.'),
('**•** Any teen whose own parent was the volunteer (or vice versa). Cohort Companion follow-up; pastoral 1:1 if welcomed.',
 '**•** Any member whose spouse was a volunteer. Cohort Companion follow-up; pastoral 1:1 if welcomed.'),
('## On Tuesday night, while [volunteer name] / the parent volunteer / both volunteers were doing visible work in the centre of the circle, what surfaced in ME?',
 '## On Tuesday night, while the volunteers were doing visible work in the centre of the circle, what surfaced in ME?'),
]
# Spouse-in-the-room protocol block (replaces the teen's-parent adjustment)
E.append((
'''## Adjustment if a teen’s parent is the round-2 volunteer

**In the rare case where a teen’s own parent is the round-2 volunteer, the team has decided in pre-meet whether the teen attends or steps out beforehand. The teen has been consulted in advance. If the teen attends:**

**— The Lead Companion privately, before the round, names this to the teen with a single sentence: ‘Your dad / mom is going to bring something tonight. They cleared it with you. You are free to step out at any moment.’**

**— The teen’s Cohort Companion sits beside them through the centre work.**

**— At the surfacing round, the teen passes by default. They will share, if at all, with their Cohort Companion after the session.**

**This case is rare; in most pilots it will not arise. Plan for it explicitly in the team pre-meet and you will not be improvising.**''',
'''## Adjustment if the round-2 volunteer’s spouse is in the room

**Where the round-2 volunteer’s spouse is a member of the cohort, the team has decided in pre-meet how the evening holds them. The spouse has been consulted in advance. During the round:**

**— The Lead Companion privately, before the round, names this to the spouse with a single sentence: ‘Your husband / wife is going to bring something tonight. They cleared it with you. You are free to step out at any moment.’**

**— The spouse’s Cohort Companion sits beside them through the centre work.**

**— At the surfacing round, the spouse passes by default. They will share, if at all, with their Cohort Companion after the session.**

**This case will be common in a leadership cohort that includes married couples. Plan for it explicitly in the team pre-meet and you will not be improvising.**'''))
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
# Differentiation section (bold-header style in this file)
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

*Tonight there is no circle split, but the room’s members are doing this differently inside the same circle. The Cohort Companions read their own circles’ members across the session and follow up offline as needed.*

**Those doing this work for the first time**

## Adjustments

**First-timers will most often surface concrete things in the surfacing round (‘I felt sad,’ ‘I thought about my grandmother’) rather than abstract things. Honour the concrete.**

**Watch for: the member who treats the volunteer pieces as performances. Affirm the pieces as work, not performance: ‘This was real work, not a show. Did anything come up in you while it was happening?’**

**Watch for: the member whose surfacing share is about someone else, not themselves. Redirect gently: ‘What about in you? Same question.’**

**Watch for: the member whose body language during the centre work is checked-out. Some of this is self-protection; some is dissociation. Cohort Companion notices; offline check-in if it persists.**

**The veterans**

## Adjustments

**Veterans will most often surface accurate but slightly polished material in the surfacing round. The Cohort Companion gently invites the unpolished version: ‘What’s the rougher version of that?’**

**Watch for: the veteran whose surfacing share reveals material beyond what tonight’s round can hold (a current crisis, a specific relational rupture). Receive without rushing; pastoral 1:1 within the week if welcomed.**

**Watch for: the veteran who tries to take over the surfacing round with a long share. Redirect kindly: ‘Hold the rest for your standing pair this week.’**

**Watch for: the veteran who is surprised by what surfaced. The first time co-processing becomes visible, it is often disorienting in a useful way. Affirm: ‘What you just noticed about yourself is data. Bring it to your pair this week.’**

**The ordained and the staff**

## Adjustments

**The ordained will often surface family-of-origin or call-of-origin material in the surfacing round, particularly during round 2. This is data; receive without rushing.**

**Watch for: the member whose spouse is in the room during their visible work. Pre-handled per the protocol; the spouse’s Cohort Companion sits beside them during the work.**

**Watch for: the leader whose surfacing share names another person. ‘When [volunteer] said \\_\\_\\_\\_\\_, my husband’s shame knot surfaced for me.’ Re-frame to interior: ‘What was YOUR knot underneath that?’ Adjudicating anyone else is not what tonight is for; the member’s own surfaced material is.**

**Watch for: the leader who realizes mid-session that the named knot from Wk 3 has shifted across the week and they are now seeing something different. This is the Spirit’s work continuing; honour it. Standing pair conversation this week.**

**Watch for: the leader who wants to turn what surfaced in the room into next Sunday’s sermon. What the room gave tonight is not material. The container covers the pulpit too.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD04: {len(E)}+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
