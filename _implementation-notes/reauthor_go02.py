# GO Week 2 adult re-authoring: what it means to be sent.
import io, sys, re
f = 'docs/going-out/week-02-body-sent.md'
s = io.open(f, encoding='utf-8').read()
E = [
('*Pilot edition — Covenant Christian Academy of Warrenton*',
 '*Adult edition — the leadership-first year (FotH for a CPR)*'),
('**Generational projection. A parent says ‘our kids today don’t know how to witness.’ A senior teen says ‘our parents do witness wrong.’ Same redirect as in Going Deeper — the witness each member is being formed for is theirs; cross-generational pronouncement is almost always projection.**',
 '**Positional projection. A pastor says ‘our congregation doesn’t know how to witness.’ A member says ‘the leadership does witness wrong.’ Same redirect as in Going Deeper — the witness each member is being formed for is theirs; cross-positional pronouncement is almost always projection.**'),
('**If a teen’s Tell crossed a safety threshold (a peer disclosed self-harm; a friend disclosed abuse). Section 6 protocol immediately. Mandatory-reporting law applies as relevant.**',
 '**If a member’s Tell crossed a safety threshold (someone disclosed self-harm; someone disclosed abuse). The safeguarding frame governs (Leadership Year Handbook §7 and the host church’s policy); a disclosure about a minor, brought by an adult, may still carry reporting duties. Mandatory-reporting law applies as relevant.**'),
('**Default. Section 6 of the Going Deeper Handbook v1.1 (carried forward).**',
 '**Default. The safeguarding frame (Leadership Year Handbook §7 and the host church’s policy).**'),
('**•** Confirm room layout: ONE large circle of 20–32 chairs.',
 '**•** Confirm room layout: ONE large circle — a chair for every member.'),
('**If a teen’s Tell involved a peer in distress: receive briefly, follow up in pastoral 1:1; mandatory-reporting protocols if applicable.**',
 '**If a member’s Tell involved someone in distress: receive briefly, follow up in pastoral 1:1; mandatory-reporting protocols if applicable — disclosures about minors especially.**'),
('## Script — Co-Companion (Parent) leads',
 '## Script — Co-Companion leads'),
('**•** Any teen whose Tell involved a peer in distress.',
 '**•** Any member whose Tell involved someone in distress.'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
for old, new, want in [
    ('| Co-Companion (Teen) |', '| Co-Companion |', 1),
    ('| Co-Companion (Parent) |', '| Co-Companion |', 1),
]:
    n = s.count(old)
    if n != want:
        print(f'!! count={n} (want {want}): {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)
DA = '**Differentiation by Cohort**'
DB = '**Closing Practice in Detail**'
NEWDIFF = '''**Differentiation Notes**

*Tonight there is no circle split. The Cohort Companions read their own circle’s members across the session.*

**Those doing this work for the first time**

## Adjustments

**First-timers often experience witness as awkward by default — any ‘I noticed something and want to share something true’ conversation feels risky. Receive the awkwardness as data, not failure.**

**Watch for: the first-timer whose Tell happened at home — with a spouse, a child, a parent — rather than at work or beyond. Honour. Witness is not less when it is at home.**

**Watch for: the first-timer whose Tell didn’t happen because they couldn’t identify anyone outside the cohort. Re-frame: ‘Family count. Colleagues count. Neighbours count. The people you already see count, even if you did not name what you said as a Tell.’**

**Watch for: the first-timer whose Tell surfaced something concerning in the receiver (a disclosure of self-harm, of harm at home). Receive briefly; pastoral 1:1 immediately after the session; the safeguarding frame governs.**

**Watch for: the first-timer whose framing of witness is shaped by a church culture they have inherited (perhaps an evangelistic urgency that doesn’t fit them). The three distinctions help; receive without contradicting their tradition aggressively.**

**The veterans**

## Adjustments

**Veterans often have more developed witness frames — some from ministry exposure, some from academic engagement, some from prior evangelism training. Receive the framing each veteran brings; the three distinctions can be used to refine without overriding.**

**Watch for: the veteran whose Tell was theologically substantive (‘my friend asked me about the resurrection’). Honour. Specific theological witness is real and Spirit-led.**

**Watch for: the veteran whose Tell was relationally substantive without being verbally evangelistic (‘I sat with my friend who lost her mother’). Honour. The body’s ministry of presence is witness too.**

**Watch for: the veteran whose Tell involved someone in a shared context — the workplace, the congregation — where the Tell may have ongoing consequences. Pastoral 1:1 within the week to walk what may unfold.**

**Watch for: the veteran whose framing is anti-evangelism (a counter-reaction to a tradition they came from). The three distinctions affirm broader witness without dismissing evangelism; the veteran may need to hear evangelism as ONE form of witness, not the totality.**

**The ordained and the staff**

## Adjustments

**The ordained often have the broadest witness landscape — congregation, colleagues, neighbours, extended family, professional contacts — and the greatest risk of counting professional output as the week’s Tell. A sermon is not a Tell. The practice asks for a witness as a person, not as the office.**

**Watch for: the leader whose Tell happened with their adult child or their spouse. Honour the household-level witness; the cohort is one of many places witness happens.**

**Watch for: the leader whose Tell revealed an older relational rupture (a former colleague, an estranged family member). Receive without making it the cohort’s focus; pastoral 1:1 if welcomed for the relational complexity.**

**Watch for: the leader whose Tell was vocationally substantive (a witness conversation that touched faith and work). Honour; this is often where a leader’s most consequential witness happens — and notice whether it happened inside the role or beside it.**

**Watch for: the leader whose Tell crossed into territory their church culture would not affirm. Receive without prescribing; pastoral support if welcomed.**

**Watch for: the leader who had no Tell because their week was simply consumed (a congregant crisis, a child’s illness, an aging parent). Honour. Some weeks the witness is simply faithful presence in difficult conditions.**

'''
if s.count(DA) == 1 and s.count(DB) == 1 and s.index(DA) < s.index(DB):
    s = s[:s.index(DA)] + NEWDIFF + s[s.index(DB):]
else:
    print('!! differentiation splice anchors wrong'); fail += 1
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO02: {len(E)}+2 counted + splice, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|famil(?:y|ies)|CCA|Warrenton|junior|senior|Section 6|Virginia|Asker|registration|chaperone|generational)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:15]: print('  ', r)
sys.exit(1 if fail else 0)
