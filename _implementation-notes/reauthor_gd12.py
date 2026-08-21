# GD Week 12 adult re-authoring: sending and bridge; registration -> entry-gate year commitment.
import io, sys, re
f = 'docs/going-deeper/week-12-sending-and-bridge.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Pilot edition — Covenant Christian Academy of Warrenton',
 'Adult edition — the leadership-first year (FotH for a CPR)'),
('**Mode.** Whole-room. No cohort split tonight.',
 '**Mode.** Whole-room. No circle split tonight.'),
('The Rhythm Card continues across the the interlude before Going Out begins.',
 'The Rhythm Card continues across the interlude before Going Out begins.'),
('**Hidden refusal of the ending. Some members will resist closing because Going Out is months away and the interlude feels exposing.',
 '**Hidden refusal of the ending. Some members will resist closing because Going Out is weeks away and the interlude feels exposing.'),
('**Family-across-cohorts public emotion. Teen-parent moments may surface in the cohort blessing block. Receive without preventing or amplifying; the family’s relationship is theirs to walk; the cohort holds the moment briefly without making it the central frame.**',
 '**Household public emotion. Spouse-to-spouse moments may surface in the cohort blessing block. Receive without preventing or amplifying; the couple’s relationship is theirs to walk; the cohort holds the moment briefly without making it the central frame.**'),
('Receive without rushing; pastoral 1:1 immediately following the session; the interlude have full pastoral coverage.**',
 'Receive without rushing; pastoral 1:1 immediately following the session; the interlude has full pastoral coverage.**'),
('**If a teen leaves the closing session distressed because their parent (or vice versa) said something hard during cohort blessing. Cohort Companions stay with both, separately; pastoral 1:1 within the week.**',
 '**If a member leaves the closing session distressed because their spouse said something hard during cohort blessing. Cohort Companions stay with both, separately; pastoral 1:1 within the week.**'),
('**Default. Section 6 of the Going Deeper Handbook. Pastoral / clinical backup confirmed by name and number. The interlude have full coverage — the team is on call between Wk 12 and Going Out Wk 1.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy). Pastoral / clinical backup confirmed by name and number. The interlude has full coverage — the team is on call between Wk 12 and Going Out Wk 1.**'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs. Standing pairs sit beside each other (Cohort Companions arrange seating before doors open).',
 '**•** Confirm room layout: ONE large circle — a chair for every member. Standing pairs sit beside each other (Cohort Companions arrange seating before doors open).'),
('Coordinated by Co-Comp (Teen) or a volunteer.',
 'Coordinated by a Co-Companion or a volunteer.'),
('**•** Chairs in ONE large single circle, 20–32 chairs. Standing pairs pre-arranged side by side.',
 '**•** Chairs in ONE large single circle, one per member. Standing pairs pre-arranged side by side.'),
('| Saturday before | Cohort Companions write personal blessing on each member’s sending card (H12.3). | Cohort facs |',
 '| Saturday before | Cohort Companions write personal blessing on each member’s sending card (H12.3). | Cohort Comps |'),
('| T-15 min | Door opens. Welcome each participant by name; warm. | Co-Comp (Teen) |',
 '| T-15 min | Door opens. Welcome each participant by name; warm. | Co-Comp |'),
('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags. Warm welcome — last session. |',
 '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags. Warm welcome — last session. |'),
('| 7:35–7:55 | Block 5: Standing pair blessing | Shared circle (in pairs) | Cohort Facs supervise |',
 '| 7:35–7:55 | Block 5: Standing pair blessing | Shared circle (in pairs) | Cohort Comps supervise |'),
('| 7:55–8:10 | Block 6: Cohort blessing — sending each member | Shared circle | Lead Companion + Cohort Facs | Cohort Companions distribute pre-written sending cards. Each Cohort Companion speaks brief blessing over their cohort. |',
 '| 7:55–8:10 | Block 6: Cohort blessing — sending each member | Shared circle | Lead Companion + Cohort Comps | Cohort Companions distribute pre-written sending cards. Each Cohort Companion speaks brief blessing over their circle. |'),
('Two — some of you are continuing into the Going Out series (the Going Out series); some are not. Both are honest.',
 'Two — some of you are continuing into the Going Out series; some are not. Both are honest.'),
('**Block 4 — Brief Shares: The Question Carried into Spring (7:25–7:35, 10 min)**',
 '**Block 4 — Brief Shares: The Question Carried into Going Out (7:25–7:35, 10 min)**'),
('**While distribution happens, each Cohort Companion (one at a time) speaks brief blessing over their cohort. Junior teen cohort first. Then senior teen. Then parent.**',
 '**While distribution happens, each Cohort Companion (one at a time) speaks brief blessing over their circle, in turn.**'),
('**Each cohort blessing: about 90 seconds. ‘I have walked with you for twelve weeks. I have seen this cohort \\_\\_\\_\\_\\_. The specific gift this cohort carries is \\_\\_\\_\\_\\_. The discipline ahead is \\_\\_\\_\\_\\_. My blessing for the [junior teens / senior teens / parents] of this cohort is \\_\\_\\_\\_\\_.’**',
 '**Each circle blessing: about 90 seconds. ‘I have walked with you for twelve weeks. I have seen this circle \\_\\_\\_\\_\\_. The specific gift this circle carries is \\_\\_\\_\\_\\_. The discipline ahead is \\_\\_\\_\\_\\_. My blessing for this circle is \\_\\_\\_\\_\\_.’**'),
('**After all three cohort blessings, Lead Companion brief blessing over the whole room. About 2 minutes. Drawing on the integrated picture from Wk 11.**',
 '**After the circle blessings, Lead Companion brief blessing over the whole room. About 2 minutes. Drawing on the integrated picture from Wk 11.**'),
('*“THREE — Going Out continuation. Some of you have already decided whether you are continuing; some are still discerning. Both are honest. Continuation registration opens [date] and closes [date]. Honest non-continuers — we want to be in contact with you across the interlude if welcomed; the cohort has walked with you and does not stop because you are not continuing in formal sessions.”*',
 '*“THREE — Going Out continuation. The year you committed at the entry gate runs through Going Out, and most of you will simply keep walking. If the interlude finds you discerning that you cannot continue, that is a conversation, not a form — talk with the convening leader before Wk 1. Attrition in this year is data, read honestly, never scored. Honest non-continuers — we want to be in contact with you across the interlude if welcomed; the cohort has walked with you and does not stop because you are not continuing in formal sessions.”*'),
('‘Going Deeper closed with more sentiment than honest assessment supported. Spring asks for honest engagement from the start.’',
 '‘Going Deeper closed with more sentiment than honest assessment supported. Going Out asks for honest engagement from the start.’'),
('the team commits to a specific repair conversation in the the interlude before Going Out begins.',
 'the team commits to a specific repair conversation in the interlude before Going Out begins.'),
('**•** Honest non-continuers — brief warm contact at week 1 of the gap; week 4; week 8 if the gap is longer.',
 '**•** Honest non-continuers — brief warm contact at week 1 of the gap, and again before Going Out Wk 1.'),
('''**Going Out continuation registration opens: \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ (date)**

**Going Out continuation registration closes: \\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_\\_ (date)**''',
 '**If the interlude finds you discerning not continuing: a conversation with the convening leader before Going Out Wk 1 — not a form. The year was committed at the entry gate; honest attrition is read, never scored.**'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
n_ask = s.count('Asker')
s = s.replace('Asker', 'Discerner')
print(f'Asker->Discerner: {n_ask} replacements')
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

*Tonight there is no circle split. Each circle is closed differently inside the same room, with the Cohort Companions speaking specifically to their circle during Block 6.*

**Those doing this work for the first time**

## Adjustments

**First-timers often experience the close as significant in ways they cannot fully articulate. The personal sending card from the Cohort Companion is the primary anchor; many will read it later in the week and the words will land then.**

**Watch for: the pair blessing that stays awkward (pairs from the same long-standing friendship group especially). The Cohort Companion coaches: ‘Specific. What have you seen in them?’ Pre-rehearsal at the Saturday team meeting can help.**

**Watch for: the member whose closing produces unexpected affect (tears, withdrawal). Cohort Companion stays close; brief 1:1 at the end of the session.**

**Watch for: the member who experiences the after-session food / drink time as the most meaningful part. Honor; informal time matters.**

**The veterans**

## Adjustments

**Veterans often process closings cognitively first; the affect may come later in the interlude. The sending card written by the Cohort Companion is often where the closing lands.**

**Watch for: the veteran whose pair partner is moving away or leaving the church. The pair release is structural, not relational; honor specifically.**

**Watch for: the veteran whose closing produces a specific calling clarity (‘I think I know what Going Out is for me’). Honor; do not pressure for resolution; pastoral support if welcomed.**

**Watch for: the veteran who critiques the closing architecture (‘this felt too neat’). Receive; the architecture is not the experience; the experience is what each member walks.**

**The ordained and the staff**

## Adjustments

**The ordained often experience the close as the integration of a longer arc — not just twelve weeks but the whole leadership year so far, plus the larger formation arc of decades. Honor the longer arc.**

**Watch for: the member whose pair partner has been a significant relationship across Going Deeper, and whose closing produces specific gratitude or loss. Honor without rushing.**

**Watch for: the couple closing differently — one spouse visibly moved, the other flat. Each closing belongs to its person; observation happens outside the session, not adjudication inside it.**

**Watch for: the leader who is reconsidering vocational or ministry choices because of Going Deeper’s formation. Honor; pastoral support across the interlude is critical; sometimes the formation produces decisions that cannot be acted on within the cohort window.**

**Watch for: the member who feels the cohort’s closing keenly because their primary adult community has been here — for some leaders, this room has been the only place all year they were not in charge. Receive; the interlude has full pastoral coverage.**

**Watch for: the leader who is moved to make a public commitment about supporting the cohort’s Going Out or a specific other member. Honor; the commitment becomes specific outside the session with Cohort Companion support.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GD12: {len(E)}+1 splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|dyads?|CCA|Warrenton|junior|senior|Section 6|Virginia|Asker|Spring|registration)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
