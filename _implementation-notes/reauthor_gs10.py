# GS Week 10 adult re-authoring (Garden II, member-led).
import io, sys, re
f = 'docs/getting-started/week-10-garden-2.md'
s = io.open(f, encoding='utf-8').read()

G = [
 ('Pilot edition — Covenant Christian Academy of Warrenton', 'Adult edition — the leadership-first year (FotH for a CPR)'),
 ('the teen leads the walk-through; the adult holds the debrief', 'the rotation leader leads the walk-through; the experienced Companion holds the debrief'),
 ('a senior teen reads it', 'one of the cohort reads it'),
 ('Companion-in-Formation', 'rotation leader'),
 ('| Lead Comp + CiF |', '| Lead Comp + leader |'),
 ('| CiF + Cohort Comps |', '| Leader + Companions |'),
 ("a teen's to lead once they have received it", "a member's to lead once they have received it"),
 ("(Section 11.2; the three rules, Section 11.6)", '(the bright line; the three rules)'),
 ("It is never the teen's to hold, and tonight the whole cohort watches that line honored in real time. That witness is itself formation: the juniors learn that leadership has a shape, and the seniors learn that the shape is what keeps everyone safe.",
  "It is never the first-time leader's to hold, and tonight the whole cohort watches that line honored in real time. That witness is itself formation: the room learns that leadership has a shape, and its leaders learn that the shape is what keeps everyone safe."),
 ('See one, do one, in the same series, in front of the cohort (handbook Section 11.3).', 'See one, do one, in the same series, in front of the cohort.'),
 ('and the second running is the slot a senior leads, protocol in hand, with an adult in the room',
  'and the second running is the slot a rotation leader leads, protocol in hand, with an experienced Companion in the room'),
 ('one second running, senior-led', 'one second running, member-led'),
 ('for the senior reading the protocol, standing in that slot is a first taste of what Week 12 will name out loud',
  'for the member reading the protocol, standing in that slot is a first taste of what Week 12 will name out loud'),
 ('name, simply, that a senior leads the walk-through tonight', 'name, simply, that one of the cohort leads the walk-through tonight'),
 ('one of our seniors, who has been preparing for this', 'one of us, who has been preparing for this'),
 ('Senior-led guided walk-through', 'Member-led guided walk-through'),
 ('Guided walk-through, senior-led', 'Guided walk-through, member-led'),
 ("Senior's three garden returns confirmed", "The leader's three garden returns confirmed"),
 ('Section 11.7, full order.', 'Full order.'),
 ('The senior', 'The rotation leader'),
 ('the senior', 'the rotation leader'),
 ('the adult Cohort Companion', 'the experienced Companion'),
 ('The adult Cohort Companion', 'The experienced Companion'),
 ('adult-held sharing', 'Companion-held sharing'),
 ('adult-led, and the cohort receives it', 'Companion-led, and the cohort receives it'),
 ('the slot moves to an adult this cycle', 'the slot moves to a Companion this cycle'),
 ('In circles without a rotation leader, the adult leads from H9.1', 'In circles without a rotation leader, the Companion leads from H9.1'),
 ('The adult moves to the person', 'The Companion moves to the person'),
 ('the adult steps to the doorway', 'the Companion steps to the doorway'),
 ("The adult's only job is the one person", "The Companion's only job is the one person"),
 ('the adult receives the handoff', 'the Companion receives the handoff'),
 ('the adult runs the Settle Protocol', 'the Companion runs the Settle Protocol'),
 ('hand it to the adult immediately', 'hand it to the Companion immediately'),
 ('while the adult moves', 'while the Companion moves'),
 ('from senior to adult at the end of the walk-through', 'from leader to Companion at the end of the walk-through'),
 ('passes visibly to the adult for journaling', 'passes visibly to the Companion for journaling'),
 ('and for the senior by name', 'and for the rotation leader by name'),
 ('and for the senior.', 'and for the rotation leader.'),
 ('Co-Comp (Teen)', 'Co-Comp'),
 ('Co-Comp (Parent)', 'Co-Comp'),
 ('Junior teens with [name]. Senior teens with [name]. Parents with [name]. Quieter than usual on the way out.',
  '[Name]’s circle, this side. [Name]’s circle, that side. Quieter than usual on the way out.'),
]
for old, new in G:
    n = s.count(old)
    print(f'{n:2d}x {old[:58]}')
    s = s.replace(old, new)

io.open(f, 'w', encoding='utf-8').write(s)
res = [m.group(0)[:105] for m in re.finditer(r'^.*\b([Tt]eens?|[Pp]arents?|[Jj]uniors?|[Ss]eniors?|[Aa]dults?|CCA)\b.*$', s, re.M)]
print('--- residual lines:', len(res))
for r in res[:30]: print('  ', r)
