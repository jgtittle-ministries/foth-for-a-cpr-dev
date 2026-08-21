# GO Week 6 adult re-authoring: the vocational witness.
import io, sys, re
f = 'docs/going-out/week-06-vocational.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Workplace, school, daily-rhythm contexts — where most members spend the bulk of their hours and where the three modes of witness are most visibly tested*',
 '*Workplace, ministry, daily-rhythm contexts — where most members spend the bulk of their hours and where the three modes of witness are most visibly tested*'),
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('**Aim.** Engage the vocational domain — workplace (parents), school (teens), professional and daily-rhythm contexts — as a specific sent-context for each cohort member.',
 '**Aim.** Engage the vocational domain — workplace, ministry, professional and daily-rhythm contexts — as a specific sent-context for each cohort member.'),
('**Mode.** Whole-room. The vocational domain spans cohort lines (parents have workplaces; teens have schools; both share the structure of a daily-rhythm context with non-believing or differently-believing colleagues). Cross-cohort visibility is again the pedagogical centre.',
 '**Mode.** Whole-room. The vocational domain spans the whole body (a teacher’s classroom, a contractor’s sites, a pastor’s church office — all share the structure of a daily-rhythm context with non-believing or differently-believing colleagues). Cross-member visibility is again the pedagogical centre.'),
('**Vocational-type comparison. The senior teen whose school is a small Christian community hears the parent whose workplace is hostile to faith; comparison shame surfaces in either direction. The Lead Companion frames at the start: every vocational context is its own witness terrain; faithfulness is contextual.**',
 '**Vocational-type comparison. The member whose workplace is a small Christian business hears the member whose workplace is hostile to faith; comparison shame surfaces in either direction. The Lead Companion frames at the start: every vocational context is its own witness terrain; faithfulness is contextual.**'),
('**Teen academic pressure. A senior teen whose vocational context is academic preparation (college applications, AP testing) and whose witness practice has been suppressed by performance pressure. Receive cleanly; pastoral 1:1 to surface what is real.**',
 '**Professional performance pressure. A member whose vocational context is in a high-stakes season (a licensure exam, a review cycle, a business at risk) and whose witness practice has been suppressed by performance pressure. Receive cleanly; pastoral 1:1 to surface what is real.**'),
('**School-level conduct issues. A teen Tell surfaces material involving peer abuse, bullying, school-conduct issues, or staff misconduct. Mandatory-reporting law applies where relevant; school-level conduct processes may apply; pastoral support immediately.**',
 '**Institutional conduct issues. A Tell surfaces material involving abuse, bullying, or misconduct inside an institution — a school, a church, a workplace. Mandatory-reporting law applies where relevant (disclosures about minors especially); the institution’s own conduct processes may apply; pastoral support immediately.**'),
('**If school-level abuse or conduct issues surface (teen Tell): mandatory-reporting law applies where relevant. The teen Companion stays close; pastoral safety planning; school-level conduct processes engaged as appropriate.**',
 '**If institutional abuse or conduct issues surface: mandatory-reporting law applies where relevant. The Cohort Companion stays close; pastoral safety planning; the institution’s conduct processes engaged as appropriate.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1 (carried forward).**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('A parent’s 40–60 hour workweek; a senior teen’s 35-hour school week plus extracurriculars; a junior teen’s school week; the people each member sees most often.',
 'A 40–60 hour workweek; a ministry’s seven-day rhythm; a household’s caregiving hours; the people each member sees most often.'),
('Tonight’s architecture is whole-room. Vocational contexts span cohort lines structurally — a parent’s workplace witness and a senior’s school witness share the structure of long-term daily presence with non-believing or differently-believing colleagues. The cross-cohort visibility lets each cohort learn from the others. Junior teens hear what vocational witness becomes over decades; parents hear what school-context witness asks of the next generation.',
 'Tonight’s architecture is whole-room. Vocational contexts span the body structurally — a teacher’s classroom, a nurse’s ward, and a pastor’s church office share the structure of long-term daily presence with non-believing or differently-believing colleagues. The cross-member visibility lets the body learn from itself. Newer members hear what vocational witness becomes over decades; the long-tenured hear what a fresh context asks of a witness just arriving.'),
('**3.** Cohort review. Each Cohort Companion reports vocational dynamics in their cohort: members in burnout, members in vocational discernment, members whose vocational context surfaced acute material in the household work. (15 min)',
 '**3.** Cohort review. Each Cohort Companion reports vocational dynamics in their circle: members in burnout, members in vocational discernment, members whose vocational context surfaced acute material in the household work. (15 min)'),
('**4.** Walk the run sheet. The whole-room structure tonight; the cross-cohort sharing; the Lead’s pattern naming; the bridge to Wks 7–9. Time discipline. (10 min)',
 '**4.** Walk the run sheet. The whole-room structure tonight; the cross-member sharing; the Lead’s pattern naming; the bridge to Wks 7–9. Time discipline. (10 min)'),
('**5.** Special cases: members at vocational rupture points; teens under acute academic pressure; members in workplaces with active harassment or conduct issues. (5 min)',
 '**5.** Special cases: members at vocational rupture points; members under acute performance pressure; members in workplaces with active harassment or conduct issues. (5 min)'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs; flip chart visible to whole circle.',
 '**•** Confirm room layout: ONE large circle — a chair for every member; flip chart visible to whole circle.'),
('‘Holy Spirit, you have been at work in our daily-rhythm contexts — our workplaces, our schools, the rooms where we spend most of our hours.',
 '‘Holy Spirit, you have been at work in our daily-rhythm contexts — our workplaces, our ministries, the rooms where we spend most of our hours.'),
('The daily-rhythm context where most of us spend the bulk of our hours — workplace, school, professional context.',
 'The daily-rhythm context where most of us spend the bulk of our hours — workplace, ministry, professional context.'),
('TWO — cross-cohort visibility. Workplace witness and school witness share more structure than they look like; the cohorts learn from each other.”*',
 'TWO — cross-member visibility. One member’s vocational terrain and another’s share more structure than they look like; the body learns from itself.”*'),
('The colleague who has watched you for ten years; the classmate who has been in your honors classes since 9th grade. The body’s love made visible in faithful work, integrity under pressure, presence under deadlines. Most vocational witness is in this mode.**',
 'The colleague who has watched you for ten years; the board member who has served beside you since the old building. The body’s love made visible in faithful work, integrity under pressure, presence under deadlines. Most vocational witness is in this mode.**'),
('The colleague who, after years of watching, finally asks the question. The classmate who notices something different and asks why.',
 'The colleague who, after years of watching, finally asks the question. The co-worker who notices something different and asks why.'),
('*“Cross-cohort visibility tonight is intentional. Junior teens, listen to parents’ contributions and notice what vocational witness becomes over decades. Parents, listen to teen contributions and notice what school-context witness asks of the next generation.”*',
 '*“Cross-member visibility tonight is intentional. If you are newer to this work, listen to the long-tenured contributions and notice what vocational witness becomes over decades. If you have been at this for years, listen to the newer voices and notice what a fresh context asks of a witness just arriving.”*'),
('**•** The cohort sharing produced honest cross-cohort visibility — junior teens heard parents’ vocational data; parents heard teens’ school data; mutual learning was visible.',
 '**•** The sharing produced honest cross-member visibility — newer members heard decades-long vocational data; the long-tenured heard fresh-context data; mutual learning was visible.'),
('**•** Any senior whose Tell crossed into academic-pressure crisis or post-graduation transition material.',
 '**•** Any member whose Tell crossed into performance-pressure crisis or vocational transition material.'),
('**•** Any teen whose Tell surfaced school-level conduct issues or peer crisis.',
 '**•** Any member whose Tell surfaced institutional conduct issues or a receiver in crisis.'),
('Initials: \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ Relationship (colleague / classmate / supervisor / teacher / vendor / other): \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_',
 'Initials: \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ Relationship (colleague / supervisor / staff member / client / vendor / other): \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_'),
('Vocational context type (workplace / school / professional / volunteer / other): \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_',
 'Vocational context type (workplace / ministry / professional / volunteer / other): \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_'),
('## WHAT IT IS. The colleague who has watched you for ten years. The classmate who has been in your AP classes since freshman year. The body’s love made visible in faithful work, integrity under pressure, presence under deadlines, the quality of how you treat the person who cleans the office or the substitute teacher.',
 '## WHAT IT IS. The colleague who has watched you for ten years. The volunteer who has served beside you since the old building. The body’s love made visible in faithful work, integrity under pressure, presence under deadlines, the quality of how you treat the person who cleans the office or covers the front desk.'),
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

*Tonight there is no circle split. The Cohort Companions read their own circle’s members across the sharing.*

**Those doing this work for the first time**

## Adjustments

**First-timers’ vocational witness is often heavy on quiet integrity — not yet much verbal witness. Honour. The Daniel paradigm applies; the words come after the presence has been earned.**

**Watch for: the first-timer whose workplace is hostile to faith. Receive cleanly; pastoral support; honour the cost.**

**Watch for: the first-timer whose Tell-receiver is a colleague in crisis (a rupture at home, a health fear, a livelihood at risk). Pastoral support for what the member is now carrying; mandatory-reporting where a minor is involved.**

**Watch for: the first-timer whose Tell did not happen because they had no language for the vocational context. Receive cleanly; H6.2’s vocational mapping opens vocabulary.**

**The veterans**

## Adjustments

**Veterans carry long tenures — the colleague who has watched them for ten years, the context where the witness has been present but unnamed for a decade. The data look may surface how invisible the long witness has become.**

**Watch for: the veteran in active vocational rupture (job loss, transition, professional crisis). Pastoral 1:1 within the week.**

**Watch for: the veteran whose vocational context is exhausting and whose witness practice is being eroded by burnout. Sabbath-rhythm conversation; the Tell practice may need adjustment for this season.**

**Watch for: the veteran whose vocational witness is most consequential in supervisory or leadership roles. The Daniel paradigm applies; pastoral support for the integrity work.**

**Watch for: the veteran whose Tell crossed into theological depth they were not prepared for (a colleague asking the hard question after years of watching). Pastoral 1:1 to walk what to do with the next opening.**

**The ordained and the staff**

## Adjustments

**For the ordained, the vocational domain risks collapsing entirely into the office — the church IS the workplace, and every conversation there is professionally a witness. The discipline tonight: where in the vocational context did the witness happen as a person? The hospital hallway conversation with the nurse, not the patient; the contractor renovating the fellowship hall; the barista who knows the order but not the person. Receive without simplifying — the texture is genuinely different.**

**Watch for: the leader whose church workplace carries active harassment, conduct, or HR-level material. Refer — the church’s own conduct processes and the covering have their role; the cohort does not adjudicate; pastoral 1:1.**

**Watch for: the leader in retirement, sabbatical, or an out-of-paid-work season. The vocational context is whatever the daily-rhythm context is now — caregiving, volunteer work, study. The architecture applies.**

**Watch for: the leader whose vocational Tell work surfaces that the role itself may be wrong (‘I am called somewhere else’). Receive cleanly; this is not Wk 6’s adjudication; pastoral 1:1; the entry-gate commitments and the covering belong in that longer discernment.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO06: {len(E)} pairs + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|classmates?|cross-cohort|school)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
