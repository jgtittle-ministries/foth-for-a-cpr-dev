# GD Week 3 adult re-authoring: knots and lies to the leadership register.
import io, sys, re
f = 'docs/going-deeper/week-03-knots.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Shared teaching of the knot taxonomy and the lie mechanism. SPLIT into cohort circles for paired diagnostic work with standing-pair partners (announced tonight). MERGE for closing.',
 '**Mode.** Shared teaching of the knot taxonomy and the lie mechanism. SPLIT into circles of four to eight for paired diagnostic work with standing-pair partners (announced tonight). MERGE for closing.'),
('- The teen who maps trauma. Some teens will surface trauma material disguised as a knot. Receive without interpretation; pastoral / clinical referral within 48 hours. Section 6 of the handbook applies.',
 '- The member who maps trauma. Some adults will surface trauma material disguised as a knot — decades old and never told. Receive without interpretation; pastoral / clinical referral within 48 hours. The safeguarding frame applies.'),
('- The parent who maps a knot tied to a specific person in the room. ‘My anger knot is about my husband, who is in the parent cohort.’',
 '- The member who maps a knot tied to a specific person in the room. ‘My anger knot is about my husband, who is in another circle.’'),
('**If a minor names current or ongoing harm from a parent or caregiver, this is a safety matter, not a forgiveness exercise — follow Section 6 and the mandatory-reporting steps.**',
 '**If anyone names current or ongoing harm — their own, or harm involving a minor in their household — this is a safety matter, not a forgiveness exercise: follow the safeguarding frame and, where a minor is involved, the mandatory-reporting steps.**'),
('- The new participant whose two-evening onboarding didn’t cover the soil-and-knot architecture. Pair them with a veteran for the cohort exercise; the Cohort Companion floats nearby.',
 '- The new participant whose two-evening onboarding didn’t cover the soil-and-knot architecture. Pair them with a veteran for the circle exercise; the Cohort Companion floats nearby.'),
('**If a participant surfaces trauma material (specific abuse, dissociation, panic response).** Stop the cohort’s work for that participant.',
 '**If a participant surfaces trauma material (specific abuse, dissociation, panic response).** Stop the circle’s work for that participant.'),
('No narrative-construction in the cohort. Pastoral 1:1 within 48 hours; clinical referral as appropriate. Section 6 protocol.',
 'No narrative-construction in the circle. Pastoral 1:1 within 48 hours; clinical referral as appropriate. The safeguarding frame applies.'),
('**If a teen surfaces material that suggests current abuse.** Virginia mandatory-reporting protocol applies. Two-adult rule. The team follows the law without exception. Lead Companion and Cohort Companion step aside with the teen; pastoral / clinical backup called immediately.',
 '**If a disclosure suggests current abuse — of the member, or of a minor in anyone’s household.** The mandatory-reporting law applies wherever a minor is involved. Two Companions. The team follows the law without exception. Lead Companion and Cohort Companion step aside with the member; pastoral / clinical backup called immediately.'),
('Cohort Companion stays with the participant; Co-Companion continues holding the cohort’s work.',
 'Cohort Companion stays with the participant; Co-Companion continues holding the circle’s work.'),
('**If a participant names a specific person in the cohort (cross-cohort: ‘my mom is the source of my fear knot’ when mom is in parent cohort).** Receive without naming. Do NOT engage cross-cohort during the session. Brief the involved parent-Cohort Companion after the session.',
 '**If a participant names a specific person in the cohort (‘my spouse is the source of my fear knot’ when the spouse is in another circle).** Receive without naming. Do NOT engage across circles during the session. Brief the other circle’s Cohort Companion after the session.'),
('**If you, the Companion, find yourself activated by what surfaces in your cohort.**',
 '**If you, the Companion, find yourself activated by what surfaces in your circle.**'),
('The pair work happens in cohort circles with standing-pair partners (announced tonight at close);',
 'The pair work happens in circles with standing-pair partners (announced tonight at close);'),
('Make sure the team has the same vocabulary the cohort circles will use. (15 min)',
 'Make sure the team has the same vocabulary the circles will use. (15 min)'),
('Each Cohort Companion names one specific concern about how the exercise will land in their cohort. (15 min)',
 'Each Cohort Companion names one specific concern about how the exercise will land in their circle. (15 min)'),
('1. Print the Knot Type Reference Card (H3.1) — one per participant. Junior, senior, parent versions on one shared card.',
 '1. Print the Knot Type Reference Card (H3.1) — one per participant.'),
('- Three private spaces for cohort circles; within each, room for pairs to sit knee-to-knee with buffer space between pairs.',
 '- Private spaces for the circles; within each, room for pairs to sit knee-to-knee with buffer space between pairs.'),
('- Tissues in every cohort space.',
 '- Tissues in every circle space.'),
('- Large-print Bible (ESV) in each cohort space.',
 '- Large-print Bible (ESV) in each circle space.'),
('- Wall clock or visible timer in each cohort space.',
 '- Wall clock or visible timer in each circle space.'),
('- Match within cohort, not across.',
 '- Match within the circle, not across.'),
('- Dating couples in the senior cohort do not pair with each other.',
 '- Engaged and dating couples do not pair with each other.'),
('- If a cohort has an odd number, one triad of three works.',
 '- If a circle has an odd number, one triad of three works.'),
('| T-30 min | Cohort Companions prep cohort spaces. Handouts placed. | All Companions |',
 '| T-30 min | Cohort Companions prep circle spaces. Handouts placed. | All Companions |'),
('| T-15 min | Door opens. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. |'),
('| 7:40–8:09 | Block 6: Diagnostic exercise in cohort circles | Cohort circles → pairs (this-week-only) | Cohort Facs |',
 '| 7:40–8:09 | Block 6: Diagnostic exercise in circles | Circles → pairs (this-week-only) | Cohort Comps |'),
('*“Tonight’s exercise: in cohort circles, you will pair with someone for thirty minutes — NOT your standing pair partner; that comes at the close. This is a one-time pairing for the diagnostic.”*',
 '*“Tonight’s exercise: in your circles, you will pair with someone for thirty minutes — NOT your standing pair partner; that comes at the close. This is a one-time pairing for the diagnostic.”*'),
('*“Junior teens with [name]. Senior teens with [name]. Parents with [name]. Thirty minutes. Go.”*',
 '*“Circle assignments are on the wall. Thirty minutes. Go.”*'),
('## **Block 6 — Diagnostic Exercise in Cohort Circles (7:40–8:09, 29 min)**\nEach cohort circle splits into pairs (this-week-only pairing; standing pairs come at close). Cohort Companion floats; intervenes only when needed.',
 '## **Block 6 — Diagnostic Exercise in Circles (7:40–8:09, 29 min)**\nEach circle splits into pairs (this-week-only pairing; standing pairs come at close). Cohort Companion floats; intervenes only when needed.'),
('### **Inside the cohort circle — Companion script**',
 '### **Inside the circle — Companion script**'),
('- If a participant surfaces material bigger than tonight — stop the pair work. Sit with the participant. Pastoral / clinical referral within 48 hours. Section 6 protocol applies.',
 '- If a participant surfaces material bigger than tonight — stop the pair work. Sit with the participant. Pastoral / clinical referral within 48 hours. The safeguarding frame applies.'),
('- If a participant becomes flooded — stop the pair work. Cohort Companion stays with them. Co-Companion (if available) holds the rest of the cohort.',
 '- If a participant becomes flooded — stop the pair work. Cohort Companion stays with them. Co-Companion (if available) holds the rest of the circle.'),
('- Cohort Companions report at least one specific, honest knot-naming in their cohort — a participant who left with language they did not have at 7:00.',
 '- Cohort Companions report at least one specific, honest knot-naming in their circle — a participant who left with language they did not have at 7:00.'),
('- Any teen whose named knot involves a parent in the program. Pastoral 1:1 with the teen within the week; brief the parent’s Cohort Companion confidentially.\n- Any parent whose named knot involves a spouse in the program (cross-cohort). Pastoral 1:1; brief the spouse’s Cohort Companion.',
 '- Anyone whose named knot involves another member of the program (a spouse or colleague in another circle). Pastoral 1:1; brief the other circle’s Cohort Companion confidentially.'),
('- H3.1 — Knot Type Reference Card (one shared card; junior, senior, parent versions of the entry-point language)',
 '- H3.1 — Knot Type Reference Card'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
# Differentiation section: full replacement between anchors
DA = '# **Differentiation by Cohort**'
DB = '# **Closing Practice in Detail**'
NEWDIFF = '''# **Differentiation Notes**

## **Those doing this work for the first time**

## Adjustments

- Keep the plain-language definitions close: grief is “something you lost that hurts.” Shame is “feeling like there is something wrong with you that you have to hide.” Fear is “something your body is on guard against.” Anger is “something that feels unfair that you can’t let go of.” Decades of church vocabulary can bury these; the plain words find them.
- Watch for: the member who insists they have no knots. Affirm. ‘Sometimes the noticing happens later. Listen for it this week.’
- Watch for: the member hypothesizing about other people’s knots rather than their own. Redirect: ‘We are looking at our own interior tonight.’
- Watch for: the member who is genuinely flooded. Cohort Companion stays with them. Pastoral / clinical backup notified that night.

## **The veterans**

## Adjustments

- The full IJH language is used. The four knot types, the lie-at-the-root mechanism, the entry-point taxonomy.
- Watch for: the veteran who treats tonight as a recap of Getting Started’s Any Doubts? practice. Tonight goes where that session only pointed.
- Watch for: the veteran who performs depth (‘my real shame knot is...’ with a polished narrative). Gently: ‘What’s the smaller, more specific version of that?’
- Watch for: the veteran whose named knot involves their spouse or another specific person in the room. Receive without naming. Brief the other circle’s Cohort Companion after the session.

## **The ordained and the staff**

## Adjustments

- Watch for: the leader who has read enough psychology or theology to want to debate the taxonomy. Affirm; redirect to specifics: ‘We can debate the categories another night. Tonight: which one is operating in your specific life right now?’
- Watch for: the leader whose named knot tracks back to family-of-origin material Getting Started didn’t reach. Receive without rushing. The naming may be heavier than expected. Pastoral 1:1 within the week.
- Watch for: the leader who maps a knot tied to a congregant’s or a colleague’s recent behavior. Re-frame: ‘The knot is in YOU. Their behavior is the trigger; the knot is yours.’
- Watch for: the leader whose named lie is about God specifically. ‘God will not come through this time.’ ‘God didn’t protect me when I was 14, so he won’t now.’ This is real and appropriate — and for the ordained it can be the most guarded sentence in the building. Honor without rushing. Pastoral / spiritual-direction referral if welcomed.
- Watch for: the leader who realizes mid-exercise that they have been carrying a specific knot for decades and has only now named it. The naming is heavy. Cohort Companion stays close; Lead Companion follows up within 48 hours.

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD03: {len(E)}+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
