# GO Week 7 adult re-authoring: the third-place network.
import io, sys, re
f = 'docs/going-out/week-07-third-place.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('**Mode.** Whole-room. The third-place domain spans cohort lines and benefits from cross-cohort visibility.',
 '**Mode.** Whole-room. The third-place domain spans the whole body and benefits from cross-member visibility.'),
('**Cross-cohort third-place exposure. A teen’s third-place network may overlap with a parent’s (same neighbours; same hobby groups; same church). Use indirect language; cross-cohort awareness held privately by Companions.**',
 '**Cross-member third-place exposure. A member’s third-place network may overlap with a spouse’s or another member’s (same neighbours; same hobby groups; same church). Use indirect language; cross-member awareness held privately by Companions.**'),
('**If a teen’s third-place context (hobby group, sports team, social network) reveals abuse or exploitation: Section 6 protocol; mandatory-reporting law applies; school-level or institutional conduct processes engaged.**',
 '**If a member’s third-place context (hobby group, sports league, social network) reveals abuse or exploitation: the safeguarding frame governs (Leadership Year Handbook §7 and the host church’s policy); mandatory-reporting law applies — about minors especially; the institution’s conduct processes engaged.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('**3.** Cohort review. Each Cohort Companion reports their cohort’s third-place texture: who has thick networks, who thin, who has surfaced significant material in past weeks. (15 min)',
 '**3.** Cohort review. Each Cohort Companion reports their circle’s third-place texture: who has thick networks, who thin, who has surfaced significant material in past weeks. (15 min)'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs.',
 '**•** Confirm room layout: ONE large circle — a chair for every member.'),
('**•** The cohort survey produced honest data on third-place texture across all three cohorts.',
 '**•** The cohort survey produced honest data on third-place texture across the whole body.'),
('**•** Any teen whose third-place crossed safety thresholds.',
 '**•** Any member whose third-place crossed safety thresholds.'),
('**•** Any senior whose third-place engagement produced a Spirit-prepared opening that the senior is uncertain how to steward.',
 '**•** Any member whose third-place engagement produced a Spirit-prepared opening they are uncertain how to steward.'),
('**•** Any parent whose third-place engagement is approaching the threshold of formal vocational call.',
 '**•** Any member whose third-place engagement is approaching the threshold of formal vocational call.'),
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

*Tonight there is no circle split. The Cohort Companions read their own circle’s members across the session.*

**Those doing this work for the first time**

## Adjustments

**First-timers’ third-place networks vary widely, and some will discover tonight that theirs is thin — work and family consume the hours, and the rest of life is digital. Receive without inflating; the realization is itself data.**

**Watch for: the first-timer whose third-place involves online community engagement (a forum, a game, a long-running group chat). Receive without dismissing as not-real-third-place; the engagement is real if relational.**

**Watch for: the first-timer whose third-place is church-as-second-family. Distinguish carefully; the church is a third-place candidate but may function differently for some members.**

**Watch for: the first-timer whose third-place engagement crossed into crisis or harm. The safeguarding frame governs; pastoral support immediately.**

**The veterans**

## Adjustments

**Veterans’ third-place is often in transition — a move, an empty nest, a retirement, a new season reshaping the network. Receive what is emerging rather than what used to be.**

**Watch for: the veteran whose third-place revealed a long-running Spirit-prepared encounter (a neighbour engagement that has been brewing for years). The Wk 8 cohort discernment may surface that this engagement is actually a personal calling, not a cohort calling.**

**Watch for: the veteran whose third-place is genuinely thin because of caregiving demands. Honour without shame; the season is what it is; Going Out will not manufacture mission for life-stages that don’t allow it.**

**Watch for: the veteran whose Wk 10 Discerner role from Going Deeper is now informing their third-place engagement. The integration is real and slow.**

**The ordained and the staff**

## Adjustments

**The ordained face a hazard tonight no one else does: many have no third place at all. Every room they enter turns into church — the hobby group discovers what they do, and the witness becomes the office again. Honour the thinness as an occupational reality, not a failure; and treat the recovery of a genuine third place — somewhere they are a person before they are a pastor — as formation in its own right, not just mission terrain.**

**Watch for: the leader whose third-place engagement is ministry-shaped (small group leading, mentoring, church volunteer work). Distinguish carefully: is this third-place mission, or is this household-of-faith vocation? Both are honest categories.**

**Watch for: the leader whose third-place revealed an encounter that is approaching the threshold of formal vocational call. Receive cleanly; the discernment belongs to Wk 8 and beyond, with the covering in view.**

**Watch for: the leader whose spouse shares the same third-place network (same neighbours, same congregation). Cross-member awareness held privately; indirect language in the room.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO07: {len(E)} pairs + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|classmates?|cross-cohort|school)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
