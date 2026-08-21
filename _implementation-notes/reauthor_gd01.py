# GD Week 1 adult re-authoring: register conversion (family/teen -> leadership cohort).
import io, sys, re
f = 'docs/going-deeper/week-01-welcome-back.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Shared circle the whole session. NO cohort split tonight. The whole room is one cohort for Week 1.',
 '**Mode.** Shared circle the whole session. NO circle split tonight. The whole cohort is one circle for Week 1.'),
('- Reunion vibes overrunning the work. Some returning families will arrive eager to catch up with each other.',
 '- Reunion vibes overrunning the work. Some returning members will arrive eager to catch up with each other.'),
('The room has eight Tuesdays of memory the new participants do not share.',
 'The room has fifteen Tuesdays of memory the new participants do not share.'),
('- The teen whose parent isn’t continuing (or vice versa). This will be present in the room. Acknowledge briefly: ‘Some of you are here without the family member who walked Getting Started with you. Welcome. The cohort is your cohort tonight.’',
 '- The member whose spouse or closest Getting Started companion isn’t continuing. This will be present in the room. Acknowledge briefly: ‘Some of you are here without someone who walked Getting Started beside you. Welcome. The cohort is your cohort tonight.’'),
('**Default.** Section 6 of the Going Deeper Handbook covers anything that crosses the safety threshold. Pastoral / clinical backup is on call.',
 '**Default.** The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy) covers anything that crosses the safety threshold. Pastoral / clinical backup is on call.'),
('Eight to ten weeks have passed since Getting Started closed — the Wk 14 family commissioning, then the Wk 15 commissioning of the Companions. The gap was deliberate',
 'A few weeks have passed since Getting Started closed — the Wk 14 household blessing night, then the Wk 15 commissioning rite. The gap was deliberate'),
('Tonight is the first time the room comes together as Going Deeper, with returning families plus new participants who completed the two-evening onboarding two weeks ago.',
 'Tonight is the first time the room comes together as Going Deeper, with returning members plus any new participants who completed the two-evening onboarding.'),
('1. Re-read your own Wk 10 commissioning blessing from Getting Started (if you have it). Notice what has held across the interlude, and what has thinned.',
 '1. Re-read your own Wk 15 commissioning from Getting Started — the blessing spoken over the cohort, and the three rules. Notice what has held across the interlude, and what has thinned.'),
('3. Family review — every family that completed Getting Started is reviewed: confirmed for Going Deeper, declined, or unclear.',
 '3. Member review — everyone who completed Getting Started is reviewed: confirmed for Going Deeper, declined, or unclear.'),
('| 5 days before | Team pre-meet (90 min). Family and new-participant review. | All Companions |',
 '| 5 days before | Team pre-meet (90 min). Member and new-participant review. | All Companions |'),
('| T-15 min | Door opens. Welcome each participant by name. Pair each new participant with a familiar veteran. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name. Pair each new participant with a familiar veteran. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. Veterans paired with new participants. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. Veterans paired with new participants. |'),
('| 7:23–7:33 | Block 3: Re-introducing the four conditions | Shared circle | Co-Comp (Parent) |',
 '| 7:23–7:33 | Block 3: Re-introducing the four conditions | Shared circle | Co-Comp |'),
('| 8:16–8:21 | Block 7: Between-session practice | Shared circle | Co-Comp (Parent) |',
 '| 8:16–8:21 | Block 7: Between-session practice | Shared circle | Co-Comp |'),
('*“Some of you have been gone from this room for two months. Some of you have been gone for two weeks (since onboarding). Some of you are here for the first time. All of you are welcome.”*',
 '*“Some of you have been gone from this room for a few weeks. Some of you were last here at the onboarding evenings. Some of you are here for the first time. All of you are welcome.”*'),
('Co-Companion (parent cohort) leads this block. The teaching is brief;',
 'A Co-Companion leads this block. The teaching is brief;'),
('*“Two months ago, this room operated on four conditions. Some of you have not thought about them since Getting Started; some of you heard them named once, two weeks ago at onboarding.',
 '*“A few weeks ago, this room operated on four conditions. Some of you have not thought about them since Getting Started; some of you heard them named once, at onboarding.'),
('5. Confirm room layout for one large circle of 20–32 chairs.',
 '5. Confirm room layout for one large circle — a chair for every member of the cohort.'),
('- Chairs in ONE large single circle, room enough for 20–32. No cohort sub-spaces tonight.',
 '- Chairs in ONE large single circle, one for every member. No circle sub-spaces tonight.'),
('- Time blowout on the share round. With 20–32 people in one room, the math is unforgiving.',
 '- Time blowout on the share round. With the whole cohort in one room, the math is unforgiving.'),
('# **Differentiation by Cohort**\n\nTonight there is no cohort split.',
 '# **Differentiation Notes**\n\nTonight there is no circle split.'),
('- Watch for: the returning teen whose parent isn’t continuing (or vice versa). The Cohort Companion follows up offline within the week.',
 '- Watch for: the returning member whose spouse or closest Getting Started companion isn’t continuing. The Cohort Companion follows up offline within the week.'),
('- If a friend brought a friend, or a teen showed up because their sibling is here — welcome warmly.',
 '- If a friend brought a friend, or a leader arrived because the covering asked them that morning — welcome warmly.'),
('- The Lead Companion schedules a 1:1 within 72 hours to run the most critical onboarding content individually, under the two-adult rule (Section 7 protocol).',
 '- The Lead Companion schedules a 1:1 within 72 hours to run the most critical onboarding content individually — two Companions in the conversation, per the cohort’s own rule.'),
('- If interlude shares were performance-dominated, Wk 2’s opening can name this gently:',
 '- If interlude shares were performance-dominated, Wk 2’s opening can name this gently:'),
('- If new participants felt sidelined, Wk 2’s cohort split lets the Cohort Companions give them more direct attention. Brief them on this.',
 '- If new participants felt sidelined, Wk 2’s circle split lets the Cohort Companions give them more direct attention. Brief them on this.'),
('- Junior teens stayed engaged through the teaching block.',
 '- The ordained stayed members of the room, not chaplains of it, through the teaching block.'),
('- Any teen whose parent isn’t continuing — personal warm contact within 48 hours.\n- Any parent whose teen isn’t continuing — same warm contact.',
 '- Anyone continuing without the person who walked Getting Started closest beside them — personal warm contact within 48 hours.'),
('- H1.2 — Recommitment Card (junior, senior, and parent versions)',
 '- H1.2 — Recommitment Card'),
('- Weeks 1, 4, 7, 8, 10, and 12 are whole-room sessions — no cohort split.',
 '- Weeks 1, 4, 7, 8, 10, and 12 are whole-room sessions — no circle split.'),
('- Weeks 2, 3, 5, 6, 9, and 11 split into your three cohorts — junior, senior, parent.',
 '- Weeks 2, 3, 5, 6, 9, and 11 split into circles of four to eight.'),
('**WITNESSES — the cloud around us. The cohort itself, the families that walked Getting Started, the tradition we are part of. Wks 1, 4, 11.**',
 '**WITNESSES — the cloud around us. The cohort itself, everyone who walked Getting Started, the tradition we are part of. Wks 1, 4, 11.**'),
]
# Junior-teens differentiation block -> the ordained and the staff
E.append((
'''## **Junior teens within the shared circle**

## Adjustments

- Junior teens (12–14) may find the whole-room circle overwhelming — especially if there are 24+ people.
- Place junior teens between two veterans or between their parent and a Cohort Companion. Not isolated.
- Watch for: junior teens checking out during the Hebrews 12 teaching block. Engage briefly when possible: ‘What are you hearing right now?’ Brief, not a quiz.
- The recommitment card for juniors uses simpler language. See H1.2 (junior version).''',
'''## **The ordained and the staff within the shared circle**

## Adjustments

- The ordained may re-enter the room in staff mode — hosting the reunion instead of joining it. The opening blocks are where the mode is caught, gently.
- Watch for: the pastor receiving the Hebrews 12 teaching as a colleague reviewing a sermon rather than a member under the text. Engage briefly when possible: ‘Which clause is most alive for you right now?’ Brief, not a quiz.
- The recommitment card is theirs too. A signed card from the covering’s own hand steadies the whole room.'''))
# Parents differentiation block -> spouses
E.append((
'''## **Parents within the shared circle**

## Adjustments

- Parents may notice that their teen is in the same room — a different dynamic from Getting Started’s split cohorts. The Lead Companion briefly normalizes: ‘Tonight we are one circle; from Week 2 forward, we split.’
- Watch for: parents who hover protectively over their teens during the interlude share. Gently signal — sometimes by physical placement before 7:00 — that parents and teens sit in their own area of the circle, not adjacent.
- Parents whose teen isn’t continuing: warm contact within 48 hours. The continuing parent is a parent without their Getting Started companion.''',
'''## **Spouses within the shared circle**

## Adjustments

- Married members may notice their spouse is in the room in a new way tonight — the deeper series raises the stakes of being heard by the person who lives with you. The Lead Companion briefly normalizes: ‘Tonight we are one circle; from Week 2 forward, we split, and spouses land in different circles by design.’
- Watch for: a member editing their interlude share because their spouse is listening. Gently signal — sometimes by physical placement before 7:00 — that spouses sit in different areas of the circle, not adjacent.
- A member whose spouse isn’t continuing: warm contact within 48 hours. The continuing member is walking without their closest Getting Started companion.'''))
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
# H1.2: collapse three card versions to one adult card (parent version is the base)
JH = '## **Junior version (ages 12–14)**'
PH = '## **Parent version**\n\n## My recommitment'
if s.count(JH) == 1 and s.count(PH) == 1 and s.index(JH) < s.index(PH):
    s = s[:s.index(JH)] + s[s.index(PH):]
    s = s.replace(PH, '## My recommitment', 1)
else:
    print('!! H1.2 splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD01: {len(E)}+splice edits, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
