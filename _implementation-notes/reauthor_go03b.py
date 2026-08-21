# GO Week 3 cleanup: remaining cohort-space/cohort-circle residuals.
import io, sys, re
f = 'docs/going-out/week-03-where-sent.md'
s = io.open(f, encoding='utf-8').read()
E = [
('Second — review your cohort’s members one by one, with what you know of each:',
 'Second — review your circle’s members one by one, with what you know of each:'),
('**4.** Walk the run sheet. The cohort split rhythm; the standing pair work first within each cohort; the cohort circle around the room; the merge. Time pressure is real; team rehearses transitions. (15 min)',
 '**4.** Walk the run sheet. The circle split rhythm; the standing pair work first within each circle; the circle sharing around the room; the merge. Time pressure is real; team rehearses transitions. (15 min)'),
('**•** Wall clock or visible timer in each cohort space.',
 '**•** Wall clock or visible timer in each circle space.'),
('**Time discipline is real. At 12 minutes: switch. At 24 minutes: stop. The cohort circle needs its time.**',
 '**Time discipline is real. At 12 minutes: switch. At 24 minutes: stop. The circle sharing needs its time.**'),
('**The cohort circle hears each sentence briefly rather than weighing each context at length.**',
 '**The circle hears each sentence briefly rather than weighing each context at length.**'),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:72]}'); fail += 1; continue
    s = s.replace(old, new)
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'GO03b: {len(E)} pairs, {fail} failures')
res = [m.group(0)[:110] for m in re.finditer(r'^.*\b(teens?|parents?|junior|senior|CCA|Warrenton|Section 6|Virginia|cohort space|cohort split|cohort-split|cohort circle)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:10]: print('  ', r)
sys.exit(1 if fail else 0)
