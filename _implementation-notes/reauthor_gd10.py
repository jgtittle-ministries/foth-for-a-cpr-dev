# GD Week 10 adult re-authoring: Acts 13 calling discernment to the leadership register.
import io, sys, re
f = 'docs/going-deeper/week-10-calling-discernment.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Whole-room. No cohort split.',
 '**Mode.** Whole-room. No circle split.'),
('**Family-across-cohorts implications. If the Discerner’s calling has direct family implications (a teen choosing a college far from home; a parent considering a vocational change that affects the family; a parent considering a ministry that pulls from family time), pastoral 1:1 with all family members across cohorts within 48 hours.**',
 '**Household implications. If the Discerner’s calling has direct household implications (a vocational change that affects the family; a ministry that pulls from family time; a move), pastoral 1:1 with the household — spouse in the cohort or not — within 48 hours.**'),
('**If a teen Discerner’s calling involves significant separation from family (college far away, a ministry plan parents are concerned about). The teen’s parent in another cohort hears it in real time. Pre-handled per the team pre-meet protocol; pastoral 1:1 with the family within 48 hours.**',
 '**If the Discerner’s calling involves significant separation (a move, a ministry plan their spouse has concerns about) and the spouse hears it named in real time. Pre-handled per the team pre-meet protocol; pastoral 1:1 with the couple within 48 hours.**'),
('**Default. Section 6 of the Going Deeper Handbook covers anything that crosses the safety threshold.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy) covers anything that crosses the safety threshold.**'),
('The pilot cohort is unlikely to be at Level 5 sustainably; we are attempting it tonight for one specific moment.',
 'A first cohort is unlikely to be at Level 5 sustainably; we are attempting it tonight for one specific moment.'),
('**The Cohort Companions identify, at the Wk 9 pre-meet, one or two prospective Discerners per cohort whose emerging calling is at a discernment point.',
 '**The Cohort Companions identify, at the Wk 9 pre-meet, one or two prospective Discerners per circle whose emerging calling is at a discernment point.'),
('A teen Discerner whose calling involves leaving home far away — this is real and the cohort can hold it. A parent Discerner whose calling is a marital separation that has not yet been disclosed',
 'A Discerner whose calling involves leaving a long-held role — this is real and the cohort can hold it. A Discerner whose calling is a marital separation that has not yet been disclosed'),
('**The team selects ONE Discerner across the three cohorts.',
 '**The team selects ONE Discerner across the circles.'),
('**5.** Family-across-cohorts review. If the Discerner’s calling has direct family implications for someone in another cohort, the team plans the cross-cohort pastoral conversation for after Tuesday. (10 min)',
 '**5.** Household review. If the Discerner’s calling has direct household implications for someone else in the cohort — a spouse above all — the team plans the pastoral conversation for after Tuesday. (10 min)'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs with the Discerner’s chair in the geometric centre and the Lead Companion’s chair beside it.',
 '**•** Confirm room layout: ONE large circle — a chair for every member — with the Discerner’s chair in the geometric centre and the Lead Companion’s chair beside it.'),
('**•** Chairs in ONE large single circle, 20–32 chairs, with the Discerner’s chair in the geometric centre and the Lead Companion’s chair beside it (forming the centre dyad).',
 '**•** Chairs in ONE large single circle, one per member, with the Discerner’s chair in the geometric centre and the Lead Companion’s chair beside it (forming the centre dyad).'),
('| T-15 min | Door opens. Welcome each participant by name. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. |'),
('| 8:19–8:23 | Block 8: Between-session practice | Shared circle | Co-Comp (Parent) | Each member journals what they did NOT speak. Standing-pair check-in. |',
 '| 8:19–8:23 | Block 8: Between-session practice | Shared circle | Co-Comp | Each member journals what they did NOT speak. Standing-pair check-in. |'),
('## Script — Co-Companion (parent cohort) leads',
 '## Script — a Co-Companion leads'),
('**•** Any teen whose parent is the Discerner (or vice versa). Family-across-cohorts pastoral support.',
 '**•** Any member whose spouse is the Discerner. Household pastoral support.'),
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

*Tonight there is no circle split. The room’s members listen and contribute as one body. The Cohort Companions read their circles’ members across the session and follow up offline as needed.*

**Those doing this work for the first time**

## Adjustments

**First-timers often hear concrete impressions for the Discerner — a specific image, a specific phrase, a specific encouragement. Concrete is good; the Lead Companion does not push anyone to abstract their hearing.**

**Watch for: the member whose contribution is about themselves rather than the Discerner. Redirect: ‘What did you hear FOR [Discerner’s name]?’**

**Watch for: the member for whom the silent listening is destabilizing. The 22-minute silence is significantly longer than the cohort has practiced; Cohort Companion follow-up offline within 24 hours.**

**Watch for: the member who finds the laying-on-of-hands moment unfamiliar. If commissioning happens, the Cohort Companion invites participation gently — anyone can lay hands, with no obligation. The architecture is open to all members.**

**The veterans**

## Adjustments

**Veterans often hear vocational and identity impressions for the Discerner — connections to role, season, relationships. These can be sharp; let the Discerner weigh them.**

**Watch for: the veteran whose own calling discernment is acute and is activated by witnessing the Discerner’s. The Wk 10 work for the Discerner becomes formation work for the witness; pastoral 1:1 within the week.**

**Watch for: the veteran whose contribution sounds prophetic and certain. ‘God told me you should \\_\\_\\_\\_\\_.’ Receive humbly; redirect to humble form: ‘what came to me was, in your own words.’ Prophetic certainty often reveals more about the speaker than about the Discerner.**

**Watch for: the veteran whose contribution names a specific path the veteran is currently considering for themselves. Receive without commenting. Pastoral support if they are using the Wk 10 listening to test their own emerging calling.**

**The ordained and the staff**

## Adjustments

**The ordained often hear long-arc impressions for the Discerner — connections to family-of-origin, life-stage, vocation history. The Lead Companion weights these contributions equally with everyone else’s; calling discernment does not privilege office or experience.**

**Watch for: pastoral counsel dressed as hearing. ‘What I heard is that you should reconsider the timing.’ Redirect: ‘Speak humbly: what came to you for [Discerner’s name]?’ Sometimes seasoned wisdom IS the hearing; sometimes it is the counselor’s own concern. The architecture sorts this through humility of form.**

**Watch for: the leader who hears the church’s interests in the Discerner’s calling (‘if [Discerner] goes, who leads their ministry?’). The organizational question is real and belongs at another table. Tonight the body listens for the Discerner, not for the org chart.**

**Watch for: the member who is the spouse of the Discerner. Pre-handled per the team pre-meet protocol — a married Discerner has the spouse’s explicit consent before bringing the calling into the cohort, and the spouse remains a silent witness during the surfacing.**

**Watch for: the leader whose Wk 10 listening produces clarity about their OWN calling. The cohort’s formation work for the Discerner is also each member’s formation. Pastoral 1:1 if a parallel discernment is sensed.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD10: {len(E)}+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
