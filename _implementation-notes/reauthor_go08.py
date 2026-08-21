# GO Week 8 adult re-authoring: cohort-level missional discernment.
import io, sys, re
f = 'docs/going-out/week-08-discernment.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('Lead Companion floats the room with attention; explicit invitations to specific cohorts (‘Junior teens, what surfaced for you in the pair conversation?’) at need.**',
 'Lead Companion floats the room with attention; explicit invitations to the quieter voices (‘Let me hear from someone who has not spoken yet — what surfaced for you in the pair conversation?’) at need.**'),
('**Cross-cohort family material. A teen and parent in different cohorts had separate pair conversations whose outputs intersect. The cohort space holds without adjudication; cross-cohort dynamics are managed by Companions privately.**',
 '**Cross-spouse material. Two spouses in different pairs had separate pair conversations whose outputs intersect. The room holds without adjudication; the dynamics are managed by Companions privately.**'),
('**If a senior teen’s pair-discerned possibility involves engagement beyond their parents’ ability to consent (overnight travel, financial commitment, geographic relocation): cross-cohort pastoral conversation outside the session; the cohort space honors the senior’s discernment without making the parent the obstacle.**',
 '**If a member’s pair-discerned possibility involves engagement beyond their household’s current capacity to absorb (overnight travel, financial commitment, geographic relocation): pastoral conversation outside the session — and a spouse’s own yes belongs in that conversation; the room honors the member’s discernment without making the household the obstacle.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1.**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('Optional, not mandatory; not all members are physically able; teen members’ fasting is parental discretion.',
 'Optional, not mandatory; not all members are physically able; medical conditions and medication schedules take precedence.'),
('Up to 30 seconds of silence is appropriate; if longer, the Lead may invite specifically: ‘Junior teens, what do you sense?’**',
 'Up to 30 seconds of silence is appropriate; if longer, the Lead may invite specifically: ‘Let me hear from a voice we have not heard tonight — what do you sense?’**'),
('**•** A member’s acute material (calling crisis, cross-cohort family rupture, politicized engagement) was inadequately handled.',
 '**•** A member’s acute material (calling crisis, cross-spouse rupture, politicized engagement) was inadequately handled.'),
('**•** Any senior whose contribution surfaced cross-cohort tension.',
 '**•** Any member whose contribution surfaced cross-spouse tension.'),
('**•** Any parent whose contribution surfaced significant personal vocational direction.',
 '**•** Any member whose contribution surfaced significant personal vocational direction.'),
('**•** Any teen whose contribution revealed a peer-context concern requiring follow-up.',
 '**•** Any member whose contribution revealed a concern about someone in their context requiring follow-up.'),
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

*Tonight there is no circle split. The Cohort Companions read their own circle’s members across the contributions and the weighing.*

**Those doing this work for the first time**

## Adjustments

**First-timers often hold corporate-discernment work less easily than those who have done it before. Their pair conversations may have produced concrete-project possibilities (‘our cohort should serve at the shelter’) without the discernment texture the architecture asks for. Receive cleanly; the cohort’s weighing will engage what each contribution actually is.**

**Watch for: the first-timer whose contribution echoes a stronger voice’s contribution. Honour the contribution; the weighing will sort what is genuinely theirs and what is deference.**

**Watch for: the first-timer whose pair conversation produced honest blank. ‘My pair partner and I didn’t come up with anything.’ Receive as honest data; the body holds without grading.**

**Watch for: the first-timer whose contribution surfaces a concern about a specific person in their context (‘we should reach out to the family on my street that is struggling’). Receive; pastoral attention to specifics outside the session.**

**The veterans**

## Adjustments

**Veterans often arrive with developed missional vocabulary; their contributions may be theologically articulate. Receive cleanly; the body’s weighing applies to a veteran’s contribution as much as to anyone’s.**

**Watch for: the veteran whose contribution names a specific cause aligned with their own long-running personal engagement (justice work, recovery ministry, refugee support). Receive without dismissing; the weighing sorts whether this is a personal calling or a possible cohort engagement.**

**Watch for: the veteran whose contribution names a specific population they have professional experience with (clinical, educational, social services). The professional knowledge is real and useful; the discernment is whether the cohort is being called there.**

**Watch for: the veteran carrying the Wk 10 Discerner role from Going Deeper whose calling-integration has reached a moment where the cohort is being asked to support their personal sending rather than be sent together. Receive cleanly; Landing 2 exists precisely for this.**

**The ordained and the staff**

## Adjustments

**The ordained often have the most developed corporate-discernment capacity, having sat in more rooms that have done corporate work. Their contributions carry weight; they can also dominate without meaning to. Lead Companion floats with attention.**

**Watch for: the org-chart pull. A pastor’s contribution can land as an announcement even when offered humbly, because the room is trained to treat their words as direction. The leader helps the architecture by naming their offering explicitly: ‘This is one offering; the body weighs it like any other.’ The Lead Companion reinforces if the room starts assenting rather than weighing.**

**Watch for: the leader in vocational position to drive a cohort engagement (board membership, ministry leadership, a professional connection that could make Landing 1 easy). Honour while watching the dominance dynamic; an engagement the connected leader could deliver is not therefore the engagement the Spirit is naming. The cohort’s discernment is the cohort’s.**

**Watch for: the leader in a life-stage or role-load that limits cohort engagement participation (caregiving, a church season that consumes everything, professional crisis). The contribution may be specific direction, with explicit acknowledgment that the leader themselves cannot participate. Honour both the contribution and the constraint.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO08: {len(E)} pairs + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|cross-cohort|school)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
