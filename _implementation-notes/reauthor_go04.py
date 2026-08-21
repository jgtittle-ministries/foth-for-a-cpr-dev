# GO Week 4 adult re-authoring: the daily Tells (data review night).
import io, sys, re
f = 'docs/going-out/week-04-daily-tells.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('**Mode.** Whole-room. The cohort’s daily-Tells data is shared across cohort lines tonight; junior teens, senior teens, and parents all hear each other’s actual witness data. The cross-cohort visibility is the pedagogical centre.',
 '**Mode.** Whole-room. The cohort’s daily-Tells data is shared across the whole body tonight; first-timers, veterans, and the ordained all hear each other’s actual witness data. The cross-member visibility is the pedagogical centre.'),
('**Comparison and shame. A junior teen hears a parent’s vocational Tell and feels their school-friend Tell is small. A parent hears another parent’s costly family-of-origin Tell and feels their workplace Tell is shallow. The Lead Companion frames at the start: scale of context is not scale of faithfulness. The daily Tell to a sibling or classmate carries the same weight as a vocational Tell to a colleague.**',
 '**Comparison and shame. A member hears the pastor’s congregational Tell and feels their lunchroom Tell is small. A member hears another’s costly family-of-origin Tell and feels their workplace Tell is shallow. The Lead Companion frames at the start: scale of context is not scale of faithfulness. The daily Tell to a sibling or a neighbour carries the same weight as a vocational Tell to a colleague.**'),
('Refer; pastoral 1:1; clinical referrals as appropriate. Mandatory-reporting law applies as relevant for teen receivers.**',
 'Refer; pastoral 1:1; clinical referrals as appropriate. Mandatory-reporting law applies as relevant where the receiver is a minor.**'),
('**Cross-cohort family-Tell exposure. A teen’s Tell about their parent (in a different cohort) surfaces. A parent’s Tell about their teen surfaces. The architecture protects: initials only; the cross-cohort person does not enter the discussion in identifying detail; cross-cohort Companions hold the dynamic privately.**',
 '**Cross-circle spouse-Tell exposure. A member’s Tell about their spouse (seated elsewhere in the room) surfaces. The architecture protects: initials only; the spouse does not enter the discussion in identifying detail; the Companions hold the dynamic privately.**'),
('**If a teen’s Tell-receiver is in active self-harm or crisis. Section 6 protocol immediately. Mandatory-reporting law applies where relevant. The teen Companion stays close to the teen for the rest of the session.**',
 '**If a member’s Tell-receiver is in active self-harm or crisis. The safeguarding frame governs (Leadership Year Handbook §7 and the host church’s policy). Mandatory-reporting law applies where relevant — a minor receiver especially. The Cohort Companion stays close to the member for the rest of the session.**'),
('Mandatory-reporting law applies (Virginia CPS for minor victims; Virginia APS for vulnerable-adult victims). Two-adult rule for any reporting conversation.',
 'Mandatory-reporting law applies (child-protective services for minor victims; adult-protective services for vulnerable-adult victims, per the jurisdiction). Two-adult rule for any reporting conversation.'),
('**If the cohort’s data review reveals significant cross-cohort family material (a teen’s Tell of a parent, then the parent’s defensive response in their own contribution). Lead Companion holds the architecture; no adjudication in the cohort space; cross-cohort pastoral conversation outside the session.**',
 '**If the cohort’s data review reveals significant cross-spouse material (one spouse’s Tell of the other, then the other’s defensive response in their own contribution). Lead Companion holds the architecture; no adjudication in the room; pastoral conversation with each spouse outside the session.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1 (carried forward).**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('The cross-cohort visibility tonight is intentional. Wks 5 and 6 will split the cohort to engage household and vocational witness with developmentally-appropriate texture. But Wk 4 needs the body to see itself as one body — junior teens hearing what parents’ Tells look like, parents hearing what teens’ Tells look like, the senior cohort hearing both. The diversity of contexts is itself formation; the senior teen learns from the parent’s family-of-origin Tell that this kind of witness is also legitimate; the parent learns from the junior teen’s playground Tell that small daily witness counts.',
 'The cross-member visibility tonight is intentional. Wks 5 and 6 will split the cohort into circles to engage household and vocational witness with texture. But Wk 4 needs the body to see itself as one body — the first-timer hearing what the pastor’s Tells look like, the pastor hearing what the first-timer’s Tells look like, the veterans hearing both. The diversity of contexts is itself formation; the first-timer learns from another member’s costly family-of-origin Tell that this kind of witness is also legitimate; the pastor learns from the lunchroom Tell that small daily witness counts.'),
('Second — review your cohort’s past three weeks of Tell reports (whatever you have heard in pair conversations and pastoral 1:1s). Where are the patterns within your cohort?',
 'Second — review your circle’s past three weeks of Tell reports (whatever you have heard in pair conversations and pastoral 1:1s). Where are the patterns within your circle?'),
('**2.** Cohort review by Companion. Each Cohort Companion reports what they have heard in their cohort’s past three weeks. Patterns? Gaps? Concerning Tells? Cross-cohort dynamics? (20 min)',
 '**2.** Cohort review by Companion. Each Cohort Companion reports what they have heard in their circle’s past three weeks. Patterns? Gaps? Concerning Tells? Cross-circle dynamics? (20 min)'),
('**5.** Special cases: cross-cohort family material expected; teens with Tell-receivers in active crisis; members who have lapsed on the practice. (5 min)',
 '**5.** Special cases: cross-spouse material expected; members with Tell-receivers in active crisis; members who have lapsed on the practice. (5 min)'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs; flip chart visible to whole circle.',
 '**•** Confirm room layout: ONE large circle — a chair for every member; flip chart visible to whole circle.'),
('The classroom Tell carries the same weight as the boardroom Tell.”*',
 'The kitchen-table Tell carries the same weight as the boardroom Tell.”*'),
('**If a member’s contribution is exposing of someone in another cohort (cross-cohort family Tell): use initials only; do not let identifying detail enter the room.**',
 '**If a member’s contribution is exposing of someone else in the room (a spouse-Tell especially): use initials only; do not let identifying detail enter the room.**'),
('Most receivers were colleagues or classmates. Most contexts were ordinary work or school.',
 'Most receivers were colleagues or family. Most contexts were ordinary work or home.'),
('**•** No comparison shame visibly took root; the frame held across all three cohorts.',
 '**•** No comparison shame visibly took root; the frame held across the whole room.'),
('**•** A teen’s Tell-receiver was in active crisis and the team’s response was inadequate.',
 '**•** A member’s Tell-receiver was in active crisis and the team’s response was inadequate.'),
('**•** Cross-cohort family material surfaced inadequately handled.',
 '**•** Cross-spouse material surfaced inadequately handled.'),
('**•** Any cross-cohort family material that surfaced; pastoral conversation with both the teen and the parent separately.',
 '**•** Any cross-spouse material that surfaced; pastoral conversation with each spouse separately.'),
('**•** Any senior whose Tell crossed into theological depth they were not prepared for.',
 '**•** Any member whose Tell crossed into theological depth they were not prepared for.'),
('## WHO. Workplace colleagues (parents). School classmates and teachers (teens). Business partners, professional contacts, regular service relationships.',
 '## WHO. Workplace colleagues. Ministry staff and volunteers. Business partners, professional contacts, regular service relationships.'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
for old, new, want in [
    ('colleague / classmate / family / neighbour / friend / service provider / other',
     'colleague / family / neighbour / friend / service provider / other', 2),
]:
    n = s.count(old)
    if n != want:
        print(f'!! count={n} (want {want}): {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

*Tonight there is no circle split. The Cohort Companions read their own circle’s members across the survey.*

**Those doing this work for the first time**

## Adjustments

**First-timers often have Tells that look small in the room and feel large to them. The Lead Companion’s frame at the start (scale of context is not scale of faithfulness) is for the first-timers specifically.**

**Watch for: the first-timer whose Tell-receiver is in distress (a friend’s crisis, harm at home, a mental-health concern). Pastoral 1:1 immediately; mandatory-reporting where a minor is involved.**

**Watch for: the first-timer whose Tell-mode was almost entirely relational presence. That is an honest starting place; do not push toward intentional initiative prematurely.**

**Watch for: the first-timer whose Tell did not happen because they had no language for what to say. Receive cleanly; H4.2’s three-mode card opens new vocabulary.**

**The veterans**

## Adjustments

**Veterans often span all three modes already; the data review may surface that one mode dominates and the others are underdeveloped. Honour without pressing.**

**Watch for: the veteran whose Tell-receiver was someone in active crisis (a relational rupture, a vocational collapse, a mental-health concern). Pastoral 1:1 within the week.**

**Watch for: the veteran whose Tell crossed into theological depth they had not been prepared for (a friend asked the resurrection question; the veteran froze; the moment passed). Pastoral 1:1 to walk what to do with the next opening.**

**Watch for: the veteran whose Tell was performative — reported to land well in the room. Cohort Companion notices privately.**

**The ordained and the staff**

## Adjustments

**The ordained often have Tells across multiple domains in any given week (household + congregational + professional). The discipline tonight is choosing ONE for the survey — and noticing whether every Tell chosen happened inside the role. A pastoral visit is the office at work; the practice asks where the witness happened as a person.**

**Watch for: the leader whose Tell happened with their adult child outside the cohort. Honour; this is often where a leader’s most consequential household witness happens.**

**Watch for: the leader whose Tell happened with their spouse IN the room. Initials only; no identifying detail; cross-circle awareness held privately.**

**Watch for: the leader whose Tell-pattern is heavy on responsive defense (responding to questions; rarely initiating as a person rather than as the office). Receive without judgment; Wk 6 will surface vocational opportunity for intentional initiative.**

**Watch for: the leader whose Tell crossed into long-running marital tension or family-of-origin material that surfaces tonight publicly. Brief redirect; pastoral 1:1.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO04: {len(E)}+1 counted + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|classmates?|cross-cohort|cohort space|school)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
