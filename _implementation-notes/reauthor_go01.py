# GO Week 1 adult re-authoring: welcome back / returning to the sent body.
import io, sys, re
f = 'docs/going-out/week-01-welcome-back.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('**Mode.** Whole-room. No cohort split tonight.',
 '**Mode.** Whole-room. No circle split tonight.'),
('The interlude have produced different kinds of landings',
 'The interlude has produced different kinds of landings'),
('If they decide to continue, registration logistics handled briefly outside the session.**',
 'If they decide to continue, that is a conversation with the convening leader, handled briefly outside the session — not a form.**'),
('The interlude have been pastorally covered',
 'The interlude has been pastorally covered'),
('**If a participant’s spouse or family member is present unexpectedly (a teen brought a parent; a parent brought a spouse). The cohort architecture is for committed cohort members. Welcome the visitor briefly; explain Going Out registration logistics; pastoral conversation about the family member’s possible engagement separately.**',
 '**If a member’s spouse or a friend is present unexpectedly. The cohort architecture is for committed cohort members. Welcome the visitor briefly; explain how the year is entered — at the entry gate, in conversation with the convening leader; pastoral conversation about the visitor’s possible engagement separately.**'),
('**Default. Section 6 of the Going Deeper Handbook (carried forward into Going Out). Pastoral / clinical backup confirmed by name and number for the night.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy). Pastoral / clinical backup confirmed by name and number for the night.**'),
('The cohort was sent; the interlude were intentional; tonight reopens with the sending honoured.',
 'The cohort was sent; the interlude was intentional; tonight reopens with the sending honoured.'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs (smaller if some non-continuers; larger if new continuers).',
 '**•** Confirm room layout: ONE large circle — a chair for every member (adjusted for any non-continuers or new continuers).'),
('**•** Chairs in ONE large single circle, 20–32 chairs depending on cohort composition.',
 '**•** Chairs in ONE large single circle, one per member.'),
('*“Tonight is Wk 1 of Going Out. The Going Out series. We have walked',
 '*“Tonight is Wk 1 of Going Out. We have walked'),
('## Script — Co-Companion (Parent) leads',
 '## Script — Co-Companion leads'),
('**•** Any non-continuer who reconsidered tonight — confirm the registration logistics or honour the decision either way.',
 '**•** Any non-continuer who reconsidered tonight — walk the conversation with the convening leader, or honour the decision either way.'),
('**•** Any parent whose teen had a hard gap, or vice versa.',
 '**•** Any member whose spouse in the room had a hard gap, or vice versa.'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
# Counted global replaces: run-sheet role columns
for old, new, want in [
    ('Co-Companion (Teen)', 'Co-Companion', 2),
    ('Co-Companion (Parent) | Refreshed Rhythm Card', 'Co-Companion | Refreshed Rhythm Card', 1),
]:
    n = s.count(old)
    if n != want:
        print(f'!! count={n} (want {want}): {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

*Tonight there is no circle split. The Cohort Companions read their own circle’s members across the session.*

**Those doing this work for the first time (new continuers)**

## Adjustments

**New continuers arrive without Going Deeper’s shared history. The introduction block and the pastoral 1:1 held before tonight carry them; the Cohort Companion sits near them and confirms by Friday that the welcome was felt.**

**Watch for: the new continuer for whom the gap-landing round feels like everyone else’s reunion. Brief re-frame from the Cohort Companion: ‘Your landing counts tonight too — where are you arriving from?’**

**Watch for: the first-timer for whom Going Out’s outward orientation feels intimidating (‘I don’t know how to be a witness’). Re-frame: ‘Tonight is reopening, not witness yet. We will walk what witness means together across Going Out.’**

**Watch for: the new continuer without an obvious pair partner. The provisional pairing is made tonight and refined by Wk 2 if needed.**

**The veterans**

## Adjustments

**Veterans carry the whole Going Deeper arc into tonight. Most will land cleanly; some will discover the interlude took more than they noticed. Receive without alarm; Going Out re-roots quickly.**

**Watch for: the veteran whose gap landing involved a calling moment (‘I think I know what I am supposed to do’ or ‘I have been resisting what I think I am supposed to do’). Honour without rushing. Pastoral 1:1 within the week if welcomed.**

**Watch for: the veteran whose H11.3 question has been suppressed across the interlude because work or household pressure intensified. Receive without analysis; Going Out will surface what is meant to surface.**

**Watch for: the veteran whose schedule shifts across Going Out (a move, a job transition, a travel-heavy season). The twelve weeks may not all be accessible; the team holds the real schedule honestly. Brief planning conversation outside the session about what participation looks like.**

**Watch for: the veteran whose Wk 10 Discerner role from Going Deeper produced a calling decision. The integration window may still be active; the cohort holds without pressing for resolution.**

**The ordained and the staff**

## Adjustments

**The ordained often arrive with the longer arc of the work in view. The interlude may have produced significant adjustments — vocational shifts, marital conversations, ministry recalibrations. Receive without rushing.**

**Watch for: the leader whose gap landing involves vocational rupture or transition (a role ending; a calling re-emerging; a sabbatical considered). Receive; Going Out engages this in Wks 4–9. Pastoral support for the immediate decisions.**

**Watch for: the leader whose H11.3 question intensified across the interlude rather than resolving. The intensification may itself be data. Going Out will engage what is meant to be engaged.**

**Watch for: the member whose spouse in the room had a hard gap. The couple’s landing is theirs; neither adjudicates the other’s Going Out participation publicly tonight.**

**Watch for: the member whose marriage worked or did not work across the interlude. The cohort is not the venue for marital adjudication; pastoral support outside the session.**

**Watch for: the leader who is reconsidering whether to continue at all. Some return to Wk 1 having decided across the interlude that they need a different kind of support. Pastoral 1:1; honest non-continuation is honoured — a conversation with the convening leader, not a form.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO01: {len(E)}+2 counted + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|CCA|Warrenton|junior|senior|Section 6|Virginia|Asker|registration|chaperone)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
