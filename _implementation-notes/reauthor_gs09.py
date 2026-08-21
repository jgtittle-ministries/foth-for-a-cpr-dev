# GS Week 9 adult re-authoring (Garden of Your Heart I).
import io, sys, re
f = 'docs/getting-started/week-09-garden.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')
R('*An experiential encounter with Jesus in your interior space — the first guided run; a senior leads the second next week*',
  '*An experiential encounter with Jesus in your interior space — the first guided run; a rotation leader leads the second next week*')
R('- Skepticism of imaginative prayer. Some participants — especially Reformed-leaning parents and intellectually rigorous seniors — will hesitate. Address it at the open. The exercise is not pretending; it is the same faculty by which we read scripture’s images and let them shape us.',
  '- Skepticism of imaginative prayer. Some participants — especially the Reformed-leaning and the intellectually rigorous, which in a leadership cohort may be most of the room — will hesitate. Address it at the open. The exercise is not pretending; it is the same faculty by which we read scripture’s images and let them shape us.')
R('- The senior who treats this as performance art. Gently: “You don’t have to come up with anything. Sit with what is actually there.”',
  '- The member who treats this as performance art. Gently: “You don’t have to come up with anything. Sit with what is actually there.”')
R('We have sequenced them deliberately — with the second garden run (Week 10, senior-led) between them.',
  'We have sequenced them deliberately — with the second garden run (Week 10, member-led) between them.')
R('Do not skip this. The Companion who has not personally walked into their own garden this week cannot lead another person into theirs. The teens will know. They have known since Week 1; tonight they will especially know.',
  'Do not skip this. The Companion who has not personally walked into their own garden this week cannot lead another person into theirs. The room will know. It has known since Week 1; tonight it will especially know.')
R('| T-15 min | Door opens. | Co-Comp (Teen) |', '| T-15 min | Door opens. | Co-Comp |')
R('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags, phone-box. Mid-Series Pulse returns (from Week 8) collected in the bin. Quieter than usual. |',
  '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags, phone-box. Mid-Series Pulse returns (from Week 8) collected in the bin. Quieter than usual. |')
R('| 8:14–8:21 | Block 7: Between-session practice | Shared circle | Co-Comp (Parent) | Three returns to the garden this week. Brief, journaled. |',
  '| 8:14–8:21 | Block 7: Between-session practice | Shared circle | Co-Comp | Three returns to the garden this week. Brief, journaled. |')
R('*“Junior teens with [name]. Senior teens with [name]. Parents with [name]. Thirty minutes. Quieter than usual on the way out.”*',
  '*“[Name]’s circle, this side. [Name]’s circle, that side. Thirty minutes. Quieter than usual on the way out.”*')
R('And it is a good and brave thing to tell a trusted adult about it: your Cohort Companion, a parent, or someone you trust. You are not meant to carry the heavy things alone.”*',
  'And it is a good and brave thing to tell someone about it: your circle Companion, your spouse, or someone you trust. You are not meant to carry the heavy things alone.”*')
R('*Stay accessible after the closing for at least fifteen minutes. Tonight, more than most nights, participants will want to talk individually — with the two-adult rule held for any teen (never one adult alone). Some will need to.*',
  '*Stay accessible after the closing for at least fifteen minutes. Tonight, more than most nights, participants will want to talk individually — two Companions for anything that runs deep, per the host church’s practice. Some will need to.*')
R('- Junior teens reported the exercise felt forced or performative.',
  '- Members reported the exercise felt forced or performative.')
R('- Next week is the second guided run, senior-led (Week 10): whatever was rushed or thin tonight, coach the senior on it this week — the second running exists to complete what the first began.',
  '- Next week is the second guided run, member-led (Week 10): whatever was rushed or thin tonight, coach the rotation leader on it this week — the second running exists to complete what the first began.')
R('**If something heavy or upsetting comes up while you are in the garden, you can stop, open your eyes, and come back another time. Tell a trusted adult about it — your Cohort Companion, a parent, or someone you trust. You are not meant to carry it alone.**',
  '**If something heavy or upsetting comes up while you are in the garden, you can stop, open your eyes, and come back another time. Tell someone about it — your circle Companion, your spouse, or someone you trust. You are not meant to carry it alone.**')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}'); fail += 1; continue
    s = s.replace(old, new)

# Differentiation rewrite
i = s.index('## Junior teens (12–14)')
j = s.index('# Closing Practice') if '# Closing Practice' in s else s.index('# **Closing Practice')
new_diff = '''## Those doing this work for the first time

- Some members have not previously prayed in any way other than words. The exercise will feel novel. Frame it gently before the split: “This may feel new. That’s fine. There’s no wrong way to do it.”
- Watch for the member who reports nothing happened. Do not press. Affirm: “You turned toward Him for fifteen minutes. That is the practice.”
- Whimsical or unexpected imagery — receive without commentary. Do not interpret. The Spirit knows what He is doing.

## The veterans

- Veterans are most likely to surface something specifically tender — an old wound, a place of shame, a doubt grown quiet with age. Honor without amplifying.
- Watch for the member who cannot stop intellectualizing. “I just kept analyzing whether this was real or whether I was making it up.” That is a real experience. Affirm: “The analysis itself is honest. Bring the analysis to Jesus next time and see what He does with it.”
- Some will be relieved to discover that prayer can be image-saturated and not only word-based. Years of testimony from adult IJH groups suggests this is one of the most lasting effects of this session for some participants.
- If a garden image involves someone in the room, do not press for content; honor that it is private.

## The ordained and the staff

- The ordained are most likely to encounter the heart’s actual interior — the place ministry has crowded out. The garden often surfaces a wound they did not realize they were carrying: a regret, a grief, a long-quiet hope.
- They are also most likely to be skeptical at the front — especially in a Reformed-leaning context. The framing block above addresses this. Take it seriously.
- Some will weep. This is appropriate and not catastrophic. The Companion holds the space.
- Watch for the member who turns the encounter into a teaching moment for the circle. “What I think God is showing all of us is \\_\\_\\_\\_\\_.” Gently: “For now, just what you noticed for yourself.”

'''
s = s[:i] + new_diff + s[j:]

# Guided prayer scripts: drop the junior version, keep the adult one
i = s.index('## Script for Junior teens (12–14)')
j = s.index('## Script for Senior teens (15–18) and Parents')
s = s[:i] + s[j:]
s = s.replace('## Script for Senior teens (15–18) and Parents', '## The guided prayer script', 1)
s = s.replace('## Senior / Parent version', '## The script', 1)

io.open(f, 'w', encoding='utf-8').write(s) if fail == 0 else None
print(f'W9: {len(E)} pair edits + diff + script consolidation, {fail} failures')
res = [m.group(0)[:100] for m in re.finditer(r'^.*\b([Tt]eens?|[Pp]arents?|[Jj]uniors?|[Ss]eniors?|CCA)\b.*$', s, re.M)]
print('residual lines:', len(res))
for r in res[:8]: print('  ', r)
sys.exit(1 if fail else 0)
