# De-CCA pass, tier 1: identity/audience rewrites, seed notices, defect fixes.
import io, sys

edits = []
def ed(f, old, new, label, count=1):
    s = io.open(f, encoding='utf-8').read()
    n = s.count(old)
    if n != count:
        print(f'!! {label}: count={n} (expected {count})')
        edits.append(False); return
    io.open(f, 'w', encoding='utf-8').write(s.replace(old, new))
    edits.append(True); print(f'OK  {label}')

NOTICE = '''!!! note "Adult-edition seed notice"

    This handbook is carried from the family edition as seed material. In the adult year, the [Leadership Year Handbook](../leadership-year-handbook.md) governs wherever the two differ, and the [Adult Register Key](../adult-register-key.md) says how to read family-edition language until this file's adult rewrite lands. In particular, the minors-safeguarding apparatus applies only where minors are present; the adult year's safeguarding frame is the Leadership Year Handbook, with counsel review belonging to the entry gate.

'''

# --- GS handbook ---
f = 'docs/getting-started/handbook.md'
ed(f, '# A Letter to the Companion\n', NOTICE + '# A Letter to the Companion\n', 'GS: top notice')
ed(f, '''The Getting Started series is designed for teens and parents from Covenant Christian Academy of Warrenton and the broader CCA community. The expected mix:''',
'''The adult edition of Getting Started is designed for a church leadership cohort walking the leadership-first challenge: the adults a host church has commissioned to test this work on themselves before offering it to their families. The expected mix:''', 'GS: who-for lead')
s = io.open(f, encoding='utf-8').read()
import re
m = re.search(r'- Teens, ages 12–18.*?\n(?=\n## Group size)', s, re.S)
if not m:
    print('!! GS who-for bullets not found'); edits.append(False)
else:
    new_bullets = '''- Adults, commissioned by their church's covering, attending as themselves rather than as staff on duty. Titles come off at the door.
- Most will already identify as mature believers; the series still invites without coercing, and the honest skeptic in a leadership chair is as welcome here as anywhere in this work.
- A wide range of formation maturity, and that is the point: a room of fifty-year-olds is still a young room in September. Some arrive having never done this kind of interior work; some arrive having done much. Both belong, and the ladder reads the room, not the résumé.
- Leaders at varying comfort with being led. This year asks the shepherds to be sheep first, and for some that will be the hardest practice in the series.
'''
    s = s[:m.start()] + new_bullets + s[m.end():]
    io.open(f, 'w', encoding='utf-8').write(s)
    edits.append(True); print('OK  GS: who-for bullets')
ed(f, '## Respectful of CCA\n\nCovenant Christian Academy is a classical Christian school in the Reformed-evangelical tradition. The Getting Started series is hosted in that environment and should be a good guest. We:',
'## Respectful of the host church\n\nEvery run of this series lives inside a real congregation with a real tradition, and the series should be a good guest there. We:', 'GS: respectful section head')
ed(f, 'Introduce the experiential practices (Garden of Your Heart, Any Doubts?, the simplified hearing prayer in Week 8) gently and with explicit parent informed consent. These are invitations, not requirements.',
 'Introduce the experiential practices (Garden of Your Heart, Any Doubts?, the hearing prayer) gently and with each member’s own informed consent. These are invitations, not requirements — nothing in the year is demanded.', 'GS: consent line')
ed(f, 'Defer to the school’s policies on disputed theological questions. Where IJH and the school’s tradition differ on, e.g., the contemporary operation of certain spiritual gifts, we present scripture and trusted Christian voices on multiple sides and let participants and their families discern.',
 'Defer to the covering on disputed theological questions. Where IJH and the host church’s tradition differ on, e.g., the contemporary operation of certain spiritual gifts, we present scripture and trusted Christian voices on multiple sides and let the cohort and its covering discern.', 'GS: defer line')
ed(f, '## Junior and senior cohorts\n',
 '## Junior and senior cohorts\n\n*Adult edition: there are no age cohorts — circles form per the [Adult Register Key](../adult-register-key.md), and their composition, including the single-gender question, is the host church’s call. The section below is the family edition’s design, kept as seed.*\n', 'GS: cohorts note')
ed(f, '## The parent dimension\n',
 '## The parent dimension\n\n*Adult edition: members’ households are the life this year forms people for, not the room’s configuration — read per the [Adult Register Key](../adult-register-key.md). The section below is the family edition’s design, kept as seed.*\n', 'GS: parent note')

# --- GD / GO / inviting-others handbooks: top notices ---
for f2, anchor in (('docs/going-deeper/handbook.md', None), ('docs/going-out/handbook.md', None), ('docs/going-out/inviting-others-handbook.md', None)):
    s = io.open(f2, encoding='utf-8').read()
    lines = s.split('\n')
    idx = next((i for i, l in enumerate(lines) if l.startswith('# ')), 0)
    lines.insert(idx, NOTICE.rstrip('\n') + '\n')
    io.open(f2, 'w', encoding='utf-8').write('\n'.join(lines))
    edits.append(True); print(f'OK  notice: {f2}')

# --- W14 duplicate arrival row ---
f = 'docs/getting-started/week-14-sending.md'
s = io.open(f, encoding='utf-8').read()
rows = [l for l in s.split('\n') if l.startswith('| 6:00') and 'Arrival window' in l]
if len(rows) == 2:
    s = s.replace(rows[1] + '\n', '', 1)
    io.open(f, 'w', encoding='utf-8').write(s)
    edits.append(True); print('OK  W14 duplicate arrival row removed')
else:
    print(f'!! W14 arrival rows found: {len(rows)}'); edits.append(False)

# --- shared/index.md adult-register line ---
f = 'docs/shared/index.md'
s = io.open(f, encoding='utf-8').read()
lines = s.split('\n')
idx = next((i for i, l in enumerate(lines) if l.startswith('# ')), 0) + 1
lines.insert(idx, '\n*Adult year: these cards still speak in the family edition’s register in places — read them through the [Adult Register Key](../adult-register-key.md), and trust the [Leadership Year Handbook](../leadership-year-handbook.md) where they differ.*')
io.open(f, 'w', encoding='utf-8').write('\n'.join(lines))
edits.append(True); print('OK  shared index note')

print(f'{sum(edits)}/{len(edits)} edits OK')
sys.exit(0 if all(edits) else 1)
