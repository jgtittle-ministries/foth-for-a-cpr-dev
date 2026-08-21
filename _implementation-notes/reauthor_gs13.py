# GS Week 13 adult re-authoring (Rhythm — the fourth rotation lift).
import io, sys, re
f = 'docs/getting-started/week-13-rhythm.md'
s = io.open(f, encoding='utf-8').read()

G = [
 ('Pilot edition — Covenant Christian Academy of Warrenton', 'Adult edition — the leadership-first year (FotH for a CPR)'),
 ('In the CCA calendar this is likely the last session before Christmas break, with Weeks 14–15 in January — which means the cohort is about to carry these practices across a real gap before anyone commissions them.',
  'Depending on the host church’s calendar this may fall near a natural break, with Weeks 14–15 on the far side — which means the cohort may be about to carry these practices across a real gap before anyone commissions them.'),
 ('Teen-led marquee — the fourth and final senior-led block', 'Rotation marquee — the fourth and final member-led block'),
 ('Companion-in-Formation', 'rotation leader'),
 ('The adult holds anything the cards surface.', 'The experienced Companion holds anything the cards surface.'),
 ('- The teen leader turning teaching into performance.', '- The rotation leader turning teaching into performance.'),
 ('- The family for whom the Christmas-gap timing lands hard — a house where the holidays are the dry season.',
  '- The household for whom a holiday-gap timing lands hard — a house where the holidays are the dry season.'),
 ('a parent sorting their teen into a column, a teen diagnosing a friend',
  'a leader sorting a congregant into a column, a member diagnosing a friend'),
 ('the senior finishes the teaching point; the adult Companion moves quietly to the person',
  'the leader finishes the teaching point; the experienced Companion moves quietly to the person'),
 ('And it is why the fourth teen-led marquee is this session.', 'And it is why the fourth rotation marquee is this session.'),
 ('is carrying the most important pastoral equipment an FC1 will ever hold — because misreading a dry season is the first hazard of peer leadership',
  'is carrying the most important pastoral equipment a Companion will ever hold — because misreading a dry season is the first hazard of shepherding'),
 ('The senior works H13.1', 'The leader works H13.1'),
 ('The senior must be able to say', 'The leader must be able to say'),
 ('and the senior practices finishing the teaching point cleanly while the adult moves',
  'and the leader practices finishing the teaching point cleanly while the Companion moves'),
 ('and any family for whom the Christmas gap itself is the hard season', 'and any household for whom the gap itself is the hard season'),
 ('4. Confirm the Week 15 readiness conversation is calendared: the parent + Lead Companion sign-off conversation for each rotation leader happens *this week*, so that Week 15\'s commissioning confirms a decision already made rather than making one on the night.',
  '4. Confirm the Week 15 discernment conversation is calendared: the covering + convening leader conversation about the cohort’s readiness happens *this week*, so that Week 15’s commissioning confirms a discernment already made rather than making one on the night.'),
 ("Senior's two rehearsals of the teaching arc", "The leader's two rehearsals of the teaching arc"),
 ('| Day before | Senior runs the arc once more, alone, aloud. Lead Companion walks the room. | CiF / Lead Comp |',
  '| Day before | The leader runs the arc once more, alone, aloud. Lead Companion walks the room. | Leader / Lead Comp |'),
 ('| Lead Comp + CiF |', '| Lead Comp + leader |'),
 ('Co-Comp (Teen)', 'Co-Comp'),
 ("Section 11.7 — the senior's final in-cohort round; looks back across all four leads.",
  "The leader's final in-cohort round; looks back across all four leads."),
 ("are the rotation leader's, delivered from H13.1", "are the rotation leader's, delivered from H13.1"),
 ('The senior opens from memory — this is their ninth or tenth container rep since Week 5, and Week 15 will ask for it in public. The Lead Companion sits where the senior can find their eyes.',
  'The rotation leader opens from memory — this is their ninth or tenth container rep, and Week 15 will ask for it in public. The convening leader sits where they can find their eyes.'),
 ("so the senior's arc stays clean", "so the leader's arc stays clean"),
 ('For teens the parent is a legitimate first answer; so is a cohort friend from this room.',
  'A spouse is a legitimate first answer; so is a cohort friend from this room.'),
 ("This is the center of the senior's teaching lift.", "This is the center of the leader's teaching lift."),
 ("1. The Lead Companion catches the senior's eye and gives the small nod. The senior **finishes the teaching point they are on** — cleanly, no trailing off.",
  "1. The convening leader catches the rotation leader's eye and gives the small nod. The leader **finishes the teaching point they are on** — cleanly, no trailing off."),
 ('3. **The teaching continues.** The senior proceeds to the next point as if nothing happened, because as far as the room is concerned, nothing did.',
  '3. **The teaching continues.** The leader proceeds to the next point as if nothing happened, because as far as the room is concerned, nothing did.'),
 ('4. The adult stays with the person through the close and opens the follow-up conversation before the family leaves. The 48-hour follow-up stands regardless.',
  '4. The Companion stays with the person through the close and opens the follow-up conversation before they leave. The 48-hour follow-up stands regardless.'),
 ("The senior's only job in the moment is the clean finish and the calm continue.",
  "The rotation leader's only job in the moment is the clean finish and the calm continue."),
 ('If "planning for failure" resistance surfaces (it usually comes from a parent)',
  'If "planning for failure" resistance surfaces (it usually comes from a veteran)'),
 ('1. The team names what the senior did well tonight', '1. The team names what the leader did well tonight'),
 ('3. Ask the leader: "Would you like feedback from the group too?" The senior decides. No pressure, no exposure.',
  '3. Ask the leader: "Would you like feedback from the group too?" They decide. No pressure, no exposure.'),
 ('a senior teen taught this cohort the most important pastoral equipment in the series',
  'one of this cohort taught it the most important pastoral equipment in the series'),
]
for old, new in G:
    n = s.count(old)
    print(f'{n:2d}x {old[:56]}')
    s = s.replace(old, new)
io.open(f, 'w', encoding='utf-8').write(s)
res = [m.group(0)[:105] for m in re.finditer(r'^.*\b(teens?|parents?|juniors?|seniors?|adults?|CCA|famil(?:y|ies)|kids?)\b.*$', s, re.M | re.I)]
print('--- residual lines:', len(res))
for r in res[:30]: print('  ', r)
