# GS Week 8 adult re-authoring (PROAPT II, the second rotation night).
# W8's vocabulary is uniform enough for per-file globals + a residual sweep.
import io, sys, re
f = 'docs/getting-started/week-08-proapt-2.md'
s = io.open(f, encoding='utf-8').read()

G = [
 ('Pilot edition — Covenant Christian Academy of Warrenton', 'Adult edition — the leadership-first year (FotH for a CPR)'),
 ('Companion-in-Formation’s', 'rotation leader’s'),
 ('Companion-in-Formation', 'rotation leader'),
 ('Comp-in-Formation', 'rotation leader'),
 ('Teen-led end to end, adult in the room', 'Member-led end to end, an experienced Companion in the room'),
 ('teen-led', 'member-led'),
 ('Co-Comp (Teen)', 'Co-Comp'),
 ('the teens will know', 'the room will know'),
 ('the senior', 'the rotation leader'),
 ('The senior', 'The rotation leader'),
 ('a senior', 'a member'),
 ('one senior', 'one member'),
 ('the adults hold anything heavy', 'the experienced Companions hold anything heavy'),
 ('never counts as one of the two adults', 'never counts as one of the two Companions for a disclosure'),
 ('two adults are in the room', 'two Companions are in the room'),
 ('adults out of the circle during the walk-through, eyes on the rotation leader, no rescuing', 'Companions out of the circle during the walk-through, eyes on the rotation leader, no rescuing'),
 ('A ten-second stumble the rotation leader recovers from is worth more to their formation than a smooth block an adult saved.',
  'A ten-second stumble the rotation leader recovers from is worth more to their formation than a smooth block a Companion saved.'),
 ('the bright line of Section 11.2 governs the night', 'the bright line governs the night'),
 ('The three rules that never bend (Handbook 11.6) are in force', 'The three rules that never bend are in force'),
 ('Standard Section 6 protocols apply', 'The standard safeguarding frame applies'),
 ('(it was Day 6 on the junior sheet)', '(it was Day 6 on the Track One sheet)'),
 ('catch the adult’s eye', 'catch the Companion’s eye'),
 ('The room learns who is leading from where the adults look.', 'The room learns who is leading from where the Companions look.'),
]
for old, new in G:
    n = s.count(old)
    print(f'{n:2d}x {old[:58]}')
    s = s.replace(old, new)

io.open(f, 'w', encoding='utf-8').write(s)
# residual sweep report
res = []
for m in re.finditer(r'^.*\b([Tt]eens?|[Pp]arents?|[Jj]unior|[Ss]enior|[Kk]ids?|CCA)\b.*$', s, re.M):
    res.append(m.group(0)[:110])
print('--- residual lines:', len(res))
for r in res[:20]:
    print('   ', r)
