# GS Week 10 residual cleanup.
import io, sys, re
f = 'docs/getting-started/week-10-garden-2.md'
s = io.open(f, encoding='utf-8').read()
fail = 0

G = [
 ("The sharing is already the adult's room.", "The sharing is already the Companion's room."),
 ('the garden was opened, adult-led', 'the garden was opened, Companion-led'),
 ('which circle the rotation leader leads, and which adult Cohort Companion holds each',
  'which circle the rotation leader leads, and which experienced Companion holds each'),
 ('H9.1 for any adult-led circle', 'H9.1 for any Companion-led circle'),
 ('H9.1 for adult-led circles', 'H9.1 for Companion-led circles'),
 ('**The rotation leader, turning to the adult, unhurried:', '**The rotation leader, turning to the Companion, unhurried:'),
 ('**The adult, receiving it:', '**The Companion, receiving it:'),
 ('**Adult-led from here.', '**Companion-led from here.'),
 ('hand the room to the adult, out loud, without hurry', 'hand the room to the Companion, out loud, without hurry'),
 ('### Adult Cohort Companion: special considerations', '### The experienced Companion: special considerations'),
 ('The Leader Feedback Round (handbook Section 11.7) runs after the closing container tonight',
  'The Leader Feedback Round runs after the closing container tonight'),
 ('*Stay accessible after the close for at least fifteen minutes, with the two-adult rule held for any teen.',
  '*Stay accessible after the close for at least fifteen minutes, two Companions for anything that runs deep.'),
]
for old, new in G:
    n = s.count(old)
    if n == 0:
        print(f'?? 0x {old[:60]}')
    s = s.replace(old, new)

i = s.index('## Junior teens (12–14)')
j = s.index('# Closing Practice in Detail')
new_diff = '''## Those doing this work for the first time

- Comparing gardens is most likely among first-timers. Land the “no junior varsity garden” line again if needed, privately and lightly.
- Watch for the member whose second visit was flatter than the first and who concludes they “did it wrong.” Affirm: “The garden has quiet weeks. Showing up is the practice.”

## The veterans

- If the rotation leader is leading a circle of their own peers, name the oddness once, lightly, at the settle — “Yes, it’s [name] reading; yes, that’s allowed” — and then treat it as normal, because it is. The circle will follow the Companions’ lead on how seriously to take it.
- Veterans are the most likely to go deeper on the second visit — the intellectual guard that was up in Week 9 has usually come down by now. Be ready for weightier shares, and hold the receive-don’t-interpret line firmly.
- Watch for the member who spent the walk-through evaluating the reader instead of walking. Gently, afterward: “Next visit, let someone else hold the room. You go into the garden.”

## The ordained and the staff

- A pastor watching one of the cohort — possibly someone they mentored — lead the room’s deepest practice will feel something. Let them feel it. More than one prototype-generation participant has named this sight as the moment the whole series made sense.
- The ordained are the most likely to have skipped the between-session returns (“the week got away from me”). No shame; tonight is the return. The second guided run exists partly for exactly this.
- The member whose Week 9 garden surfaced a wound may arrive braced. The pre-session check-in matters most here; the sit-and-pray option exists for them, and they may need explicit permission to take it.

'''
s = s[:i] + new_diff + s[j:]

io.open(f, 'w', encoding='utf-8').write(s)
res = [m.group(0)[:100] for m in re.finditer(r'^.*\b([Tt]eens?|[Pp]arents?|[Jj]uniors?|[Ss]eniors?|[Aa]dults?|CCA)\b.*$', s, re.M)]
print('residual lines:', len(res))
for r in res: print('  ', r)
