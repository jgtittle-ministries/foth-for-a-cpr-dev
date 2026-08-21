# GD Week 9 adult re-authoring: shadow mission to the leadership register.
import io, sys, re
f = 'docs/going-deeper/week-09-shadow-mission.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Shared teaching of gifts and shadow (19 min). Cohort circles for the standing-pair shadow conversation (38 min).',
 '**Mode.** Shared teaching of gifts and shadow (19 min). Circles for the standing-pair shadow conversation (38 min).'),
('**The teen-parent across cohorts naming each other’s shadow at home. The shadow named tonight in the cohort STAYS in the cohort. Family members do not deploy it as a corrective at home this week. Pastoral 1:1 if the dynamic is acute.**',
 '**Spouses across circles naming each other’s shadow at home. The shadow named tonight in the cohort STAYS in the cohort. Household members do not deploy it as a corrective at home this week. Pastoral 1:1 if the dynamic is acute.**'),
('the shadow naming is the threshold of the work, not the conclusion. Section 6 protocol if patterns crossed thresholds in the past.**',
 'the shadow naming is the threshold of the work, not the conclusion. The safeguarding frame applies if patterns crossed thresholds in the past.**'),
('**Generational projection. A parent’s shadow analysis becomes ‘kids these days have a shadow of\\_\\_\\_\\_\\_.’ A senior teen’s shadow analysis becomes ‘parents have a shadow of\\_\\_\\_\\_\\_.’ The shadow is your OWN, in your OWN life, with your OWN pair. Cohort Companion redirects.**',
 '**Positional projection. A pastor’s shadow analysis becomes ‘the congregation has a shadow of\\_\\_\\_\\_\\_.’ A member’s becomes ‘the leadership has a shadow of\\_\\_\\_\\_\\_.’ The shadow is your OWN, in your OWN life, with your OWN pair. Cohort Companion redirects.**'),
('**If a teen names a shadow that suggests current self-harm, suicidality, or harm to others. Section 6 protocol. Two-adult rule. Mandatory-reporting law applies as relevant.**',
 '**If anyone names a shadow that suggests current self-harm, suicidality, or harm to others. The safeguarding frame. Two Companions. The mandatory-reporting law applies wherever a minor is involved.**'),
('**If two participants in different cohorts name shadows that converge on each other (a parent’s controlling shadow + their teen’s avoidant shadow). The Cohort Companions do not name this to either side in the cohorts. Pastoral 1:1 with both within the week; family-level conversation only with explicit consent and pastoral support.**',
 '**If two participants in different circles name shadows that converge on each other (one spouse’s controlling shadow + the other’s avoidant shadow). The Cohort Companions do not name this to either side in the circles. Pastoral 1:1 with both within the week; a couple-level conversation only with explicit consent and pastoral support.**'),
('**Default. Section 6 of the Going Deeper Handbook. Pastoral / clinical backup confirmed by name and number.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy). Pastoral / clinical backup confirmed by name and number.**'),
('**4.** Cross-cohort awareness. Identify in advance any teen-parent dynamic where the named shadow tonight could become a corrective at home. Brief the Cohort Companions to watch for it; pastoral 1:1 follow-up if needed. (5 min)',
 '**4.** Cross-circle awareness. Identify in advance any marriage dynamic where the named shadow tonight could become a corrective at home. Brief the Cohort Companions to watch for it; pastoral 1:1 follow-up if needed. (5 min)'),
('**•** Confirm cohort spaces — pairs need to sit knee-to-knee with at least 6 feet of buffer between pairs.',
 '**•** Confirm circle spaces — pairs need to sit knee-to-knee with at least 6 feet of buffer between pairs.'),
('**•** Chairs in main room as one large circle for opening; three cohort spaces ready for the split.',
 '**•** Chairs in main room as one large circle for opening; circle spaces ready for the split.'),
('**•** Tissues in every cohort space.',
 '**•** Tissues in every circle space.'),
('**•** Large-print Bible (ESV) in each cohort space.',
 '**•** Large-print Bible (ESV) in each circle space.'),
('**•** Wall clock or visible timer in each cohort space.',
 '**•** Wall clock or visible timer in each circle space.'),
('| 48 hr before | Team pre-meet (60 min). Walk gifts framework. Cross-cohort awareness review. | All Companions |',
 '| 48 hr before | Team pre-meet (60 min). Walk gifts framework. Cross-circle awareness review. | All Companions |'),
('| Day before | Walk every cohort space. Confirm pastoral / clinical backup. | Lead Comp |',
 '| Day before | Walk every circle space. Confirm pastoral / clinical backup. | Lead Comp |'),
('| T-30 min | Cohort Companions prep their cohort spaces. Handouts placed. | All Companions |',
 '| T-30 min | Cohort Companions prep their circle spaces. Handouts placed. | All Companions |'),
('| T-15 min | Door opens. Welcome each participant by name. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. |'),
('| 7:35–8:11 | Block 5: Standing-pair shadow conversation | Cohort circles → pairs | Cohort Facs | 18 min one direction; 18 min the other; 2 min pair signature on H9.3. |',
 '| 7:35–8:11 | Block 5: Standing-pair shadow conversation | Circles → pairs | Cohort Comps | 18 min one direction; 18 min the other; 2 min pair signature on H9.3. |'),
('| 8:18–8:22 | Block 7: Between-session practice | Shared circle | Co-Comp (Parent) | Daily noticing. ‘There it is again’ as the discipline. |',
 '| 8:18–8:22 | Block 7: Between-session practice | Shared circle | Co-Comp | Daily noticing. ‘There it is again’ as the discipline. |'),
('*“In your cohort circle, the standing-pair conversation. 18 minutes one direction, 18 minutes the other.”*',
 '*“In your circle, the standing-pair conversation. 18 minutes one direction, 18 minutes the other.”*'),
('*“Junior teens with [name]. Senior teens with [name]. Parents with [name]. Thirty-eight minutes of pair work plus signature. Go.”*',
 '*“Circle assignments are on the wall. Thirty-eight minutes of pair work plus signature. Go.”*'),
('Each cohort circle splits into the standing pairs. The Cohort Companion floats. Pairs sit knee-to-knee with at least 6 feet of buffer.',
 'Each circle splits into the standing pairs. The Cohort Companion floats. Pairs sit knee-to-knee with at least 6 feet of buffer.'),
('**Inside the cohort circle — Companion script**',
 '**Inside the circle — Companion script**'),
('**•** If a named shadow reveals an active pattern of harm to another person — Cohort Companion stays with the pair after the cohort circle. Pastoral 1:1 within 24 hours.',
 '**•** If a named shadow reveals an active pattern of harm to another person — Cohort Companion stays with the pair after the circle. Pastoral 1:1 within 24 hours.'),
('## Script — Co-Companion (parent cohort) leads',
 '## Script — a Co-Companion leads'),
('*“Three. The named shadow does NOT become a corrective at home. The teen does not deploy what their parent named in the parent’s cohort; the parent does not deploy what their teen named. What was named in the cohort stays in the cohort.”*',
 '*“Three. The named shadow does NOT become a corrective at home. One spouse does not deploy what the other named in their circle; nobody preaches anyone’s shadow back to them. What was named in the cohort stays in the cohort.”*'),
('**Boundary discipline: the named shadow does NOT become a corrective at home for family across cohorts.**\n\n**Companion Debrief Prompts**',
 '**Boundary discipline: the named shadow does NOT become a corrective at home — or in the church office.**\n\n**Companion Debrief Prompts**'),
('**•** A teen-parent dynamic surfaced in the cohort circles without the team noticing.',
 '**•** A marriage dynamic surfaced in the circles without the team noticing.'),
('**•** If a teen-parent dynamic surfaced, pastoral support outside the session before Wk 10.',
 '**•** If a marriage dynamic surfaced, pastoral support outside the session before Wk 10.'),
('**•** Any teen-parent dynamic that surfaced. Cross-cohort follow-up by the appropriate Companions.',
 '**•** Any marriage dynamic that surfaced. Cross-circle follow-up by the appropriate Companions.'),
('The shadow named tonight is NOT for deployment as a corrective at home for any family member across cohorts.**',
 'The shadow named tonight is NOT for deployment as a corrective at home, in the office, or anywhere else.**'),
('**FIVE — Boundary discipline: the named shadow does NOT become a corrective at home for family across cohorts.**',
 '**FIVE — Boundary discipline: the named shadow does NOT become a corrective at home or anywhere else.**'),
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

**First-timers often name the gift in concrete terms: ‘I am good at making people feel better when they’re sad.’ ‘I am good at explaining things to people who don’t get it.’ The four-by-four archetypes are useful but not required — the concrete gift is what matters.**

**Watch for: the member whose named shadow is about someone else (‘my gift is patience, my shadow is when my husband does X’). Re-frame: ‘Your shadow is your direction in YOU; what they do is theirs. What does YOUR patience turn into when stretched?’**

**Watch for: the member whose self-flagellation is heavy. Re-frame: ‘Naming is observation. “There it is again” is the practice.’**

**Watch for: the member who claims to have no shadow. ‘Possibly. Where does your gift get tired? Where does it overreach? Where does its energy go under stress?’**

**Watch for: the pair partner who cannot speak the witness sentence. Cohort Companion coaches in the moment, modeling: ‘I heard your gift is X; the shadow direction is Y; the discipline is Z. I receive it as honest data.’**

**The veterans**

## Adjustments

**Watch for: the veteran whose gift is genuinely emerging (a gift just becoming visible in a new season or role). Affirm; the gift is real even if not yet named in the four-by-four categories.**

**Watch for: the veteran whose shadow is rooted in identity (a relational or private shadow they are afraid to name). Receive without rushing. Pastoral 1:1 within 48 hours.**

**Watch for: the veteran whose named shadow is about another member of the cohort. Receive without naming them. Cross-circle follow-up if needed.**

**Watch for: the veteran whose primary gift has been suppressed for years (a gift not used in current vocation or life-stage). The named shadow may be of a gift that has not had room to operate; the discipline is partly about recovering the gift, not only managing the shadow.**

**The ordained and the staff**

## Adjustments

**Watch for: the intellectualized shadow analysis (‘my prophetic gift’s shadow is epistemic certainty’). Push for concrete: ‘Where, with whom, recently?’**

**Watch for: the leader whose named shadow connects to the ministry itself — a controlling-administrator shadow in the church office, a condemnation-prophet shadow in the pulpit, an enabling-shepherd shadow that has never let a congregant face anything. Receive; the work-life implications are real and may take months to walk.**

**Watch for: the leader whose named shadow connects to parenting or marriage (a controlling shadow with adult children, a rescuing shadow with a struggling child, a shadow that lives at home). Same protocol as Wk 5 — receive without naming the family member; pastoral 1:1; the relational adjudication is a different conversation.**

**Watch for: the member whose pair partner’s named shadow lands hard for them (because the partner’s shadow has affected their own life; because it is similar to a shadow they have been on the receiving end of elsewhere). Cohort Companion stays close.**

**Watch for: the leader who tries to name a congregant’s or colleague’s shadow during the pair work. Stop immediately. ‘Your shadow is yours; theirs is theirs, and it is not named here.’**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD09: {len(E)}+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
