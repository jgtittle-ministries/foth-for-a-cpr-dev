# GO Week 10 adult re-authoring: what Going Out produced (individual integration).
import io, sys, re
f = 'docs/going-out/week-10-what-going-out-produced.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('the standing pair work in cohort-shared space (16 min per direction); the cohort circle hears patterns briefly.',
 'the standing pair work in the shared space (16 min per direction); the cohort hears patterns briefly.'),
('**Senior teens leaving the cohort. A senior’s articulation of what Going Out produced is shaped by the upcoming graduation or move. Honour the layered grief and possibility; pastoral 1:1 to walk the transition.**',
 '**Members in transition. A member’s articulation of what Going Out produced may be shaped by an upcoming move, role change, or life transition. Honour the layered grief and possibility; pastoral 1:1 to walk the transition.**'),
('**Cross-cohort family material. A teen’s articulation about what Going Out formed may include parental dynamics; a parent’s articulation may include teen dynamics. Initials only; cross-cohort awareness held by Companions privately.**',
 '**Cross-spouse material. A member’s articulation about what Going Out formed may include their spouse in the room. Initials only where another member is involved; cross-circle awareness held by Companions privately.**'),
('**If a senior’s articulation reveals significant graduation/transition crisis: pastoral 1:1; the cohort space holds without trying to resolve; Going Out will not adjudicate transition specifics.**',
 '**If a member’s articulation reveals significant transition crisis (a move, a role ending, a season collapsing): pastoral 1:1; the room holds without trying to resolve; Going Out will not adjudicate transition specifics.**'),
('**If a teen’s articulation surfaces material involving their parent (in another cohort) requiring pastoral cross-cohort attention: cross-cohort conversation outside the session; mandatory-reporting law applies if abuse or harm is involved.**',
 '**If a member’s articulation surfaces material involving their spouse in the room requiring pastoral attention: conversation with each spouse outside the session; mandatory-reporting law applies if abuse or harm is involved.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('Second — review your cohort’s members one by one. What do you remember about each member’s Wk 3 sentence;',
 'Second — review your circle’s members one by one. What do you remember about each member’s Wk 3 sentence;'),
('**2.** Cohort review by Companion. Each Cohort Companion reports their cohort’s members’ trajectories — known Going Out high-points; known unfinished work; members likely to surface acute material; cross-cohort family dynamics. (20 min)',
 '**2.** Cohort review by Companion. Each Cohort Companion reports their circle’s members’ trajectories — known Going Out high-points; known unfinished work; members likely to surface acute material; cross-spouse dynamics. (20 min)'),
('**4.** Special cases: members whose Going Out produced calling crisis; members whose Going Out revealed unfinished household work; senior teens in transition; the Wk 10 Discerner from Going Deeper whose calling has been worked through Going Out. (10 min)',
 '**4.** Special cases: members whose Going Out produced calling crisis; members whose Going Out revealed unfinished household work; members in transition; the Wk 10 Discerner from Going Deeper whose calling has been worked through Going Out. (10 min)'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs, with space for pairs to sit beside each other.',
 '**•** Confirm room layout: ONE large circle — a chair for every member — with space for pairs to sit beside each other.'),
('| 7:59–8:12 | Block 5: Cohort circle pattern surfacing | Shared circle | Lead Companion | Each member 30–40 sec; ONE pattern from pair work; flip chart capture. |',
 '| 7:59–8:12 | Block 5: Cohort pattern surfacing | Shared circle | Lead Companion | Each member 30–40 sec; ONE pattern from pair work; flip chart capture. |'),
('**Block 5 — Cohort Circle Pattern Surfacing (7:59–8:12, 13 min)**',
 '**Block 5 — Cohort Pattern Surfacing (7:59–8:12, 13 min)**'),
('**If a member’s pattern reveals cross-cohort dynamics: indirect language; non-identifying capture.**',
 '**If a member’s pattern reveals cross-circle dynamics: indirect language; non-identifying capture.**'),
('*“Wk 11 will be cohort-split (junior teen / senior teen / parent), then merged — same shape as Going Deeper Wk 11, allowing each cohort’s developmental texture to be honored before the body integrates.”*',
 '*“Wk 11 will be circle-split, then merged — same shape as Going Deeper Wk 11, giving each circle a smaller room for the honest read before the body integrates.”*'),
('**•** Cross-cohort family material surfaced inadequately.',
 '**•** Cross-spouse material surfaced inadequately.'),
('**•** Any senior whose integration surfaced significant vocational clarity or transition crisis.',
 '**•** Any member whose integration surfaced significant vocational clarity or transition crisis.'),
('**•** Any teen whose integration involved cross-cohort family dynamics.',
 '**•** Any member whose integration involved a spouse in the room.'),
('**•** Any parent whose integration revealed significant unfinished work.',
 '**•** Any member whose integration revealed significant unfinished work.'),
('**Cohort-split (junior teen / senior teen / parent), then merged. Each cohort’s developmental texture is honored before the body integrates.**',
 '**Circle-split, then merged. Each circle gets a smaller room for the honest read before the body integrates.**'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
for old, new, want in [
    ('**•** Going Out WWk ', '**•** Going Out Wk ', 5),
]:
    n = s.count(old)
    if n != want:
        print(f'!! count={n} (want {want}): {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

*Tonight there is no circle split. The Cohort Companions read their own circle’s members through the writing, the pair work, and the surfacing.*

**Those doing this work for the first time**

## Adjustments

**First-timers often integrate Going Out concretely — specific relational moments, specific household exchanges, specific witness experiences. Concrete is exactly right; the pair partner draws out what the moments add up to.**

**Watch for: the first-timer whose H11.3 question from Going Deeper feels distant or unrecognizable now. Receive cleanly; a first formation year moves fast, and the question may have been displaced by what Going Out formed instead.**

**Watch for: the first-timer whose integration reveals difficult household dynamics. Pastoral conversation outside the session.**

**Watch for: the first-timer whose integration surfaces dynamics involving abuse, harm, or crisis. Mandatory-reporting law applies where relevant; the safeguarding frame governs.**

**The veterans**

## Adjustments

**Veterans often integrate Going Out with a transition as the dominant frame — a move, a role change, a season turning. Receive cleanly; the integration is real even when colored by transition.**

**Watch for: the veteran whose integration surfaces vocational clarity that has firmed across the Going Out series. Pastoral 1:1 to walk what is unfolding.**

**Watch for: the veteran whose integration reveals that the cohort’s Going Out shape did not fit them — they engaged the architecture but the formation went elsewhere. Honour the honesty; Going Out’s shape isn’t for everyone in equal measure.**

**Watch for: the veteran whose Wk 10 Discerner role from Going Deeper has now produced calling clarity that feels significant. Pastoral support; spiritual-direction beyond the cohort if welcomed.**

**The ordained and the staff**

## Adjustments

**The ordained often integrate across multiple domains simultaneously — household, vocational, third-place, missional, plus their own continuing formation work — and carry an occupational reflex: the year arrives pre-polished, articulated as a report or a sermon illustration rather than as their own life. The pulpit knows how to make a year preach. The pair asks what it actually cost.**

**Watch for: the leader whose integration reveals significant household work still unfinished. Pastoral 1:1 if welcomed; the long obedience continues past the Going Out series.**

**Watch for: the leader whose vocational integration surfaces rupture or transition that has accelerated across the Going Out series. Pastoral support; clinical / vocational counsel as appropriate; the covering belongs in the longer discernment.**

**Watch for: the leader whose spouse is in the room and figures in the integration. Initials only; cross-circle awareness; pastoral conversation with the couple outside the session if needed.**

**Watch for: the leader whose integration reveals genuine Going Out-produced fruit in long-running family-of-origin material. Honour without rushing toward closure; the long obedience continues.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO10: {len(E)}+1 counted + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|cross-cohort|WWk|cohort circle|cohort-split)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
