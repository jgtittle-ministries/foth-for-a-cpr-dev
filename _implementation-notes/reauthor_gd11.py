# GD Week 11 adult re-authoring: honest assessment; Asker->Discerner consistency; de-CCA miss fixed.
import io, sys, re
f = 'docs/going-deeper/week-11-where-is-our-cohort.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Cohort-split. Each cohort circle assesses itself first using the worksheet (35 min). Then merge for cross-cohort integration (25 min). The merge does the harder work of combining three honest cohort-level pictures into one cohort-level picture.',
 '**Mode.** Circle-split. Each circle assesses itself first using the worksheet (35 min). Then merge for cross-circle integration (25 min). The merge does the harder work of combining the circles’ honest pictures into one cohort-level picture.'),
('**Center.** Each cohort uses H11.1 and H11.2 to walk eleven weeks together — what was attempted, what was lived, where the cohort actually is on the five-level taxonomy. The merge surfaces commonalities and divergences across the three cohorts;',
 '**Center.** Each circle uses H11.1 and H11.2 to walk eleven weeks together — what was attempted, what was lived, where the cohort actually is on the five-level taxonomy. The merge surfaces commonalities and divergences across the circles;'),
('**Generational scapegoating. ‘Our cohort would have been at Level 4 if it weren’t for the [teens / parents].’ Stop. The cohort is one body; the assessment is one body’s assessment. Cohort Companion redirects firmly.**',
 '**Scapegoating a circle. ‘Our cohort would have been at Level 4 if it weren’t for [that circle / the staff / the newcomers].’ Stop. The cohort is one body; the assessment is one body’s assessment. Cohort Companion redirects firmly.**'),
('Pastoral 1:1 within 24 hours; clinical referral as appropriate. Section 6 protocol if the harm crossed thresholds.**',
 'Pastoral 1:1 within 24 hours; clinical referral as appropriate. The safeguarding frame applies if the harm crossed thresholds.**'),
('**If a teen-parent dynamic surfaces during cross-cohort merge. Cohort Companions handle outside the session.**',
 '**If a marriage dynamic surfaces during the merge. Cohort Companions handle outside the session.**'),
('**Default. Section 6 of the Going Deeper Handbook. Pastoral / clinical backup confirmed by name and number for the night.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy). Pastoral / clinical backup confirmed by name and number for the night.**'),
('The team triangulates — do all three Cohort Companions see roughly the same level, or do they see differently? (20 min)',
 'The team triangulates — do the Cohort Companions see roughly the same level, or do they see differently? (20 min)'),
('**3.** Walk the run sheet. The cohort circles produce three honest pictures (35 min); the merge integrates (25 min).',
 '**3.** Walk the run sheet. The circles produce their honest pictures (35 min); the merge integrates (25 min).'),
('**•** Confirm room layout: main room single circle for opening; three cohort spaces for the assessment block; back to single circle for the merge.',
 '**•** Confirm room layout: main room single circle for opening; circle spaces for the assessment block; back to single circle for the merge.'),
('**•** Chairs in main room as one large circle for opening; three cohort spaces ready for the split; back to one circle for the merge.',
 '**•** Chairs in main room as one large circle for opening; circle spaces ready for the split; back to one circle for the merge.'),
('**•** In each cohort space: a flip chart or large sheet of paper for the cohort to write its assessment as it forms (this is the artifact the Cohort Companion brings back to the merge).',
 '**•** In each circle space: a flip chart or large sheet of paper for the circle to write its assessment as it forms (this is the artifact the Cohort Companion brings back to the merge).'),
('**•** Tissues in each cohort space and main room.',
 '**•** Tissues in each circle space and main room.'),
('**•** Wall clock or visible timer in each cohort space.',
 '**•** Wall clock or visible timer in each circle space.'),
('confirm willingness to attend and to speak briefly if welcomed. | Cohort facs |',
 'confirm willingness to attend and to speak briefly if welcomed. | Cohort Comps |'),
('| Day before | Walk every cohort space and main room. Confirm flip charts. Confirm pastoral / clinical backup. | Lead Comp |',
 '| Day before | Walk every circle space and main room. Confirm flip charts. Confirm pastoral / clinical backup. | Lead Comp |'),
('| T-30 min | Cohort Companions prep their cohort spaces. Handouts placed. | All Companions |',
 '| T-30 min | Cohort Companions prep their circle spaces. Handouts placed. | All Companions |'),
('| T-15 min | Door opens. Welcome each participant by name. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. |'),
('| 7:30–8:03 | Block 5: Cohort circles assess themselves | Cohort circles | Cohort Facs | 35 min using H11.2. Each cohort produces a flip-chart assessment. |',
 '| 7:30–8:03 | Block 5: Circles assess themselves | Circles | Cohort Comps | 35 min using H11.2. Each circle produces a flip-chart assessment. |'),
('| 8:03–8:21 | Block 6: Merge — three pictures into one | Shared circle | Lead Comp | Each Cohort Companion presents their cohort’s picture (3 min each). Lead reflects integration. Cohort weighs. |',
 '| 8:03–8:21 | Block 6: Merge — the pictures into one | Shared circle | Lead Comp | Each Cohort Companion presents their circle’s picture (3 min each). Lead reflects integration. Cohort weighs. |'),
('| 8:21–8:23 | Block 7: Between-session practice | Shared circle | Co-Comp (Parent) | Personal reflection sheet (H11.3) for Wk 12. |',
 '| 8:21–8:23 | Block 7: Between-session practice | Shared circle | Co-Comp | Personal reflection sheet (H11.3) for Wk 12. |'),
('we share aggregated findings with Anthony and the CCA pastoral team without identifying individuals.”*',
 'we share aggregated findings with the covering and the host church’s pastoral leadership without identifying individuals.”*'),
('*“In cohort circles, you will use H11.2 — the assessment worksheet. The worksheet has six questions; the cohort works through them together. Your cohort will produce a flip-chart picture by 8:05 that the Cohort Companion brings back to the merge. Three honest pictures merge into one.”*',
 '*“In your circles, you will use H11.2 — the assessment worksheet. The worksheet has six questions; the circle works through them together. Your circle will produce a flip-chart picture by 8:05 that the Cohort Companion brings back to the merge. The honest pictures merge into one.”*'),
('*“In your cohort circle, work the worksheet together. The Cohort Companion may name the first observation; the cohort takes over from there. Honest. Specific. Not generic. The Cohort Companion is part of the cohort, not the assessor of it.”*',
 '*“In your circle, work the worksheet together. The Cohort Companion may name the first observation; the circle takes over from there. Honest. Specific. Not generic. The Cohort Companion is part of the circle, not the assessor of it.”*'),
('*“Junior teens with [name]. Senior teens with [name]. Parents with [name]. Thirty-five minutes. Go.”*',
 '*“Circle assignments are on the wall. Thirty-five minutes. Go.”*'),
('**Block 5 — Cohort Circles Assess Themselves (7:30–8:03, 33 min)**\nEach cohort circle works in parallel. The structure is identical.',
 '**Block 5 — Circles Assess Themselves (7:30–8:03, 33 min)**\nEach circle works in parallel. The structure is identical.'),
('**Inside the cohort circle — Companion script**',
 '**Inside the circle — Companion script**'),
('**•** If members blame the team or another cohort — receive without defending; capture the observation on the flip chart honestly; redirect: ‘And what about the cohort itself — not the team, not the other cohort.’',
 '**•** If members blame the team or another circle — receive without defending; capture the observation on the flip chart honestly; redirect: ‘And what about the cohort itself — not the team, not the other circle.’'),
('*“Welcome back. Three cohorts each produced an honest picture; we merge.”*',
 '*“Welcome back. Each circle produced an honest picture; we merge.”*'),
('*“Each Cohort Companion will present their cohort’s picture briefly — three minutes each. The cohort itself can add briefly if something was missed. Then I will reflect what I see across the three pictures — not synthesize, reflect. The room then weighs whether what I reflected matches what the cohorts named.”*',
 '*“Each Cohort Companion will present their circle’s picture briefly — three minutes each. The circle itself can add briefly if something was missed. Then I will reflect what I see across the pictures — not synthesize, reflect. The room then weighs whether what I reflected matches what the circles named.”*'),
('*“This is not a competition. The three pictures may be similar or different; both are honest data.”*',
 '*“This is not a competition. The pictures may be similar or different; both are honest data.”*'),
('**Junior teen Cohort Companion presents first. Walks the flip chart briefly. Names where the junior cohort assessed itself on the steady state and what evidence they cited. Brief.**\n\n**Senior teen Cohort Companion presents second. Same.**\n\n**Parent Cohort Companion presents third. Same.**\n\n**After each, brief space (30 sec) for cohort members to add what was missed in the summary.**',
 '**Each Cohort Companion presents in turn. Walks the flip chart briefly. Names where their circle assessed itself on the steady state and what evidence they cited. Brief.**\n\n**After each, brief space (30 sec) for circle members to add what was missed in the summary.**'),
('*“Three pictures. Here is what I see across them.”*',
 '*“The pictures are up. Here is what I see across them.”*'),
('*(Lead Companion names 2–4 patterns that surface across the three cohorts. Specific. Drawn from what was actually presented, not invented.)*',
 '*(Lead Companion names 2–4 patterns that surface across the circles. Specific. Drawn from what was actually presented, not invented.)*'),
('*“Common — [pattern 1, pattern 2, etc.]. Different — [where the three cohorts diverged].',
 '*“Common — [pattern 1, pattern 2, etc.]. Different — [where the circles diverged].'),
('*“Two or three voluntary contributions. Does the integrated picture match what your cohort named? If not, where does it diverge?”*',
 '*“Two or three voluntary contributions. Does the integrated picture match what your circle named? If not, where does it diverge?”*'),
('## Script — Co-Companion (parent cohort) leads',
 '## Script — a Co-Companion leads'),
('**•** Each cohort produced a flip-chart picture with specific evidence. Generic ‘we grew’ was not the dominant register.',
 '**•** Each circle produced a flip-chart picture with specific evidence. Generic ‘we grew’ was not the dominant register.'),
('**•** Cohorts produced uniformly positive or uniformly negative assessments.',
 '**•** Circles produced uniformly positive or uniformly negative assessments.'),
('**Q6 — What is ahead. What is the question or capacity the cohort needs to engage in Going Out (Going Out)? Specific. (2 min)**',
 '**Q6 — What is ahead. What is the question or capacity the cohort needs to engage in Going Out? Specific. (2 min)**'),
('What capacity does the cohort need to engage in Going Out (Going Out)? Specific.',
 'What capacity does the cohort need to engage in Going Out? Specific.'),
('Going Out is the Going Out series. It will engage missional discernment, vocational outworking, the body sent together.',
 'Going Out is the third series of the year. It will engage missional discernment, vocational outworking, the body sent together.'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
# Seed consistency: W10 names the centre-chair member the Discerner; W11 says Asker.
n_ask = s.count('Asker')
s = s.replace('Asker', 'Discerner')
print(f'Asker->Discerner: {n_ask} replacements')
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

**Those doing this work for the first time**

## Adjustments

**First-timers often assess concretely. ‘We were better at listening by Wk 7 than Wk 1.’ ‘We laughed more in our circle by Wk 6.’ The Cohort Companion builds the assessment from the concrete observations the circle brings.**

**If the taxonomy stalls, translate: ‘Were we mostly people in the same room (Level 1), people who shared information (Level 2), or people who did real work together (Level 3)?’ Many first-year circles land at Level 2 to low Level 3 honestly.**

**Watch for: the member who assesses punitively (‘we were not as good as the other circles’). Re-frame: ‘Circles develop differently; we are assessing OUR circle, and the cohort as one body.’**

**Watch for: the assessment shaped by friendship (‘our circle was great because we became friends’). Honour the friendship; clarify: ‘Friendship is part of what circles produce; the question is also what work we did together.’**

**Watch for: the member who names a specific Companion failure or team failure. Receive without defending; pastoral 1:1 if the issue is acute.**

**The veterans**

## Adjustments

**Veterans often assess sharply. They see structures clearly and may critique with precision. Receive the precision; do not defend.**

**Watch for: the theologically sharp assessment (‘our cohort talked about hearing more than we actually heard’). Honour. Sharpness is real data.**

**Watch for: the veteran who assesses by comparing the cohort to other formation experiences (church groups, retreats, prior programs). Gently re-orient to this cohort’s specific architecture; the comparison may be useful but is not the answer.**

**Watch for: the veteran who critiques the format — the architecture itself, the time, the structure. Receive; capture for handbook revision; honest data.**

**Watch for: the assessment shaped by an unresolved tension with another member or Companion. Receive without adjudicating; pastoral 1:1.**

**The ordained and the staff**

## Adjustments

**The ordained often assess with a longer arc — they have been in formation contexts for decades and have a sense of what works over years. Honour the arc — and watch that the arc does not become a lecture.**

**Watch for: the leader whose assessment quietly grades the congregation the cohort will one day lead (‘this would never work with our people’). Re-frame: ‘Tonight is about US, this room, this year. The family edition’s prospects are a different conversation.’**

**Watch for: the leader who critiques the team’s pastoral coverage. Receive specifically. ‘What did you experience that you needed and did not get?’ Honest data for handbook revision and team development.**

**Watch for: the assessment shaped by a spouse being or not being in the cohort. The structural difference is real; the Cohort Companion names it without solving it.**

**Watch for: the member who realizes during the assessment that Going Deeper produced significant change in them they had not named. Honour; brief space; the personal reflection sheet (H11.3) is where this gets walked.**

**Watch for: the leader who assesses as Level 4 or 5 because the experience felt powerful. Push: ‘The taxonomy is about capacity, not affect. Where is our steady-state CAPACITY, regardless of how powerful Wk 10 felt?’**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD11: {len(E)}+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia|Anthony|Asker)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
