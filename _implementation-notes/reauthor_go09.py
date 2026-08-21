# GO Week 9 adult re-authoring: the body sent beyond (laying-on-of-hands, re-entry week).
import io, sys, re
f = 'docs/going-out/week-09-body-sent-beyond.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('The cohort split, if it happens at all tonight, is brief and only if Landing 2 (individual sending) requires cohort-specific preparation.',
 'The circle split, if it happens at all tonight, is brief and only if Landing 2 (individual sending) requires circle-specific preparation.'),
('**Cross-cohort family negotiation. A teen’s yes for a shared engagement requires parental consent the parent (in another cohort) is uncertain about. The architecture protects: cross-cohort dynamics are managed by Companions privately; the cohort space holds the teen’s discernment.**',
 '**Cross-spouse negotiation. A member’s yes for a shared engagement needs a household support their spouse (in another circle) is uncertain about. The architecture protects: the dynamics are managed by Companions privately; the room holds the member’s discernment while the couple’s own conversation happens at home.**'),
('**Senior teens leaving the cohort soon. A senior’s upcoming graduation or move means their participation in any sending will be brief or partial. Receive cleanly; the senior’s sending is theirs whether the cohort-level engagement extends past their participation or not. Honour the brief participation as real.**',
 '**Members leaving the cohort soon. A member’s upcoming move or role transition means their participation in any sending will be brief or partial. Receive cleanly; the sending is theirs whether the cohort-level engagement extends past their participation or not. Honour the brief participation as real.**'),
('**If a member’s yes to a shared engagement reveals that their household will not support it (spouse’s objection, parents’ objection for a teen): pastoral cross-cohort conversation outside the session; the cohort space holds the member’s discernment without making the household the obstacle.**',
 '**If a member’s yes to a shared engagement reveals that their household will not support it (a spouse’s objection, a household season that cannot absorb it): pastoral conversation outside the session; the room holds the member’s discernment without making the household the obstacle.**'),
('(a vocational move, a family relocation, a calling that pulls them out of CCA Warrenton): receive cleanly;',
 '(a vocational move, a family relocation, a calling that pulls them out of the host church’s orbit): receive cleanly;'),
('**If a teen’s sending reveals their parent’s household has not supported their formation across Going Out (a parent in another cohort whose engagement has been minimal or oppositional): the architecture protects the teen; cross-cohort pastoral attention; mandatory-reporting law applies if abuse or harm is involved.**',
 '**If a member’s sending reveals their household has not supported their formation across Going Out (a spouse whose engagement has been minimal or oppositional): the architecture protects the member; pastoral attention to the couple, separately if needed; mandatory-reporting law applies if abuse or harm is involved.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('**3.** Cohort review by landing. Each Cohort Companion reports what their cohort’s pair conversations across the week have produced — honest yes/no/limited responses; cost concerns; cross-cohort family dynamics; concerns about specific members. (25 min)',
 '**3.** Cohort review by landing. Each Cohort Companion reports what their circle’s pair conversations across the week have produced — honest yes/no/limited responses; cost concerns; cross-spouse dynamics; concerns about specific members. (25 min)'),
('**5.** Special cases: members whose cost-counting revealed prohibitive cost; members whose households are uncertain about the engagement; senior teens leaving the cohort; the Wk 10 Discerner from Going Deeper whose calling intersects. (15 min)',
 '**5.** Special cases: members whose cost-counting revealed prohibitive cost; members whose households are uncertain about the engagement; members leaving the cohort soon; the Wk 10 Discerner from Going Deeper whose calling intersects. (15 min)'),
('## Cohort circle pattern surfacing (4 min)',
 '## Cohort pattern surfacing (4 min)'),
('**•** Cross-cohort family material was inadequately handled.',
 '**•** Cross-spouse material was inadequately handled.'),
('**•** Any senior whose sending was partial or brief because of upcoming transition.',
 '**•** Any member whose sending was partial or brief because of upcoming transition.'),
('**•** Any teen whose cost-walking revealed parental ambiguity.',
 '**•** Any member whose cost-walking revealed a household’s ambiguity.'),
('**•** Any parent whose sending intersects with significant vocational direction.',
 '**•** Any member whose sending intersects with significant vocational direction.'),
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

*Tonight there is no circle split. The Cohort Companions read their own circle’s members through the cost-walking and the laying-on-of-hands.*

**Those doing this work for the first time**

## Adjustments

**For some first-timers the laying-on-of-hands will be entirely new. Walk the shape before it happens; participation is voluntary; the architecture honors discomfort without treating it as refusal.**

**Watch for: the first-timer whose laying-on-of-hands moment surfaces unexpected emotion. Receive cleanly; the moment is real; pastoral support if the emotion crosses thresholds.**

**Watch for: the first-timer whose individual sent-context (Landing 2) is concrete-relational — a specific neighbour, a specific colleague. Honour; the sending is real even at this scale.**

**Watch for: the first-timer whose cost-walking surfaced a household whose support is uncertain. Pastoral conversation outside the session; the room holds their discernment without making the household the obstacle.**

**The veterans**

## Adjustments

**Veterans may have experienced laying-on-of-hands in other contexts (prayer-team commissioning, healing services, a past ordination in the room). Receive the prior experience as helpful, but the architecture tonight is distinct — the cohort’s specific corporate confirmation of Going Out’s discernment.**

**Watch for: the veteran whose sending will be brief or partial because of an upcoming move or transition. The architecture honors the brief participation as real; the sending continues into their next context.**

**Watch for: the veteran whose sending intersects with the Wk 10 Discerner role from Going Deeper. The continuity across the formation arc is real; the laying-on-of-hands tonight may be a confirmation of what Going Deeper began.**

**Watch for: the veteran whose cost-walking revealed prohibitive constraint (caregiving demands, vocational pressure, financial limit). Receive the no-for-now cleanly; their individual sent-context (Landing 2) may be different from the shared engagement; honour the difference.**

**The ordained and the staff**

## Adjustments

**The ordained have stood on the other side of this moment many times — they have laid hands at ordinations, commissionings, hospital beds. Tonight they receive. Being prayed for, rather than praying, is its own formation; some will find receiving harder than any cost on the worksheet.**

**Watch for: the leader who manages the moment instead of receiving it — adjusting the logistics, coaching the blessings, staying in liturgical-director mode. Gentle release: the body has this; your part tonight is to be sent.**

**Watch for: the leader in vocational position to drive the engagement’s logistics (board membership, professional connection, ministry leadership). Honour the gift while watching the dominance dynamic; the cohort’s sending is not the connected leader’s project.**

**Watch for: the leader whose laying-on-of-hands moment surfaces calling material beyond what the room can adjudicate (sensing a call to a different work, a different place). Pastoral 1:1 within the week; spiritual-direction support beyond the cohort; the covering belongs in that longer discernment.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO09: {len(E)} pairs + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|cross-cohort|school|cohort circle)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
