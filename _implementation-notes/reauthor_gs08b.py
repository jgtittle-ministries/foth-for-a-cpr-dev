# GS Week 8 residual cleanup.
import io, sys
f = 'docs/getting-started/week-08-proapt-2.md'
s = io.open(f, encoding='utf-8').read()
fail = 0
E = [
('| Week before | Confirm passage and senior. Senior begins daily PROAPT on the passage. Print all handouts. |',
 '| Week before | Confirm passage and leader. The rotation leader begins daily PROAPT on the passage. Print all handouts. |'),
('| Day before | Senior PROAPTs the passage a final time. Lead Companion walks the room. | Both |',
 '| Day before | The rotation leader PROAPTs the passage a final time. Lead Companion walks the room. | Both |'),
('PRAY through the passage as a team. Senior sets the space.',
 'PRAY through the passage as a team. The rotation leader sets the space.'),
('*"Parents and teens each fill out your own. Don\'t compare answers unless you want to — although honestly, that',
 None),  # placeholder; replaced below with exact match after read
]
# handle the pulse line with flexible quotes
import re
m = re.search(r'\*“?"?Parents and teens each fill out your own[^\n]*\n', s)
if m:
    s = s.replace(m.group(0), '*“Each of you fills out your own. Don’t compare answers unless you want to — although honestly, comparing them over coffee this week might be the best conversation you have.”*\n', 1)
    print('OK  pulse line')
else:
    print('!! pulse line'); fail += 1
E = [e for e in E if e[1] is not None]
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)

i = s.index('## **Junior teens (12–14)**')
j = s.index('# **Closing Practice in Detail**')
new_diff = '''## Those doing this work for the first time

The second running lands well with first-timers — the structure is now familiar, and familiarity frees attention for the hearing itself.

- Mark 2:1–12 was Day 6 on the Track One sheet, so many will have seen it. Lean into the second-hearing frame rather than apologizing for it.
- The Apply prompts on the card (on the mat / one of the four / the roof) are concrete. Use them verbatim.
- Pulse: assure the room the 1–10 question is not a grade and nobody is in trouble for a low number. “4 — I keep thinking about the budget meeting” is gold for the team.

## The veterans

Tonight one of their own is at the front. That changes the room for every member in it, whether they are leading or watching.

- The members not leading tonight are watching their own future — several of them will take a later slot. Name it privately: “Watch how this goes. Your slot is coming.”
- Watch for the member who competes with the leader — the too-sharp Observe, the show-off Apply. Redirect to specificity, which is humbling in the right way.
- Tell step: veterans still hesitate to claim God said something specific. Same gentle affirmation as Week 7 — “what you heard counts even if you’re not 100% sure it was Him.”
- Pulse: the most useful Q3 answers come when pushed past “participate more.” Ask for behavior: what, when, how often.

## The ordained and the staff

One of the cohort leading the room is, for some of the ordained, the most persuasive thing this series will ever show them about what the year is building.

- The hardest differentiation of the night: the rotation leader’s spouse or closest colleague is in the room. Brief them beforehand — no coaching from the circle, no beaming commentary, no rescue. Receive the leadership like everyone else’s.
- Watch for members who direct answers to the Companions during the walk-through. The Companions redirect with their eyes: look at the rotation leader.
- Pulse: honest Q1 answers (“body in the room, mind on the mortgage”) are exactly what the instrument is for. Say so.
- The ride-home conversation after tonight — a member telling their spouse what they saw in the one who led — is between-session gold. Suggest it.

'''
s = s[:i] + new_diff + s[j:]

more = [
('- The room deferred to the adults; the walk-through was teen-fronted but adult-led.',
 '- The room deferred to the Companions; the walk-through was member-fronted but Companion-led.'),
("- The rotation leader's parent — a two-minute word about what the team saw in their teen.",
 "- The rotation leader's spouse, if they are in the cohort — a two-minute word about what the team saw in the one who led."),
]
for old, new in more:
    n = s.count(old)
    if n != 1:
        print(f'!! (more) count={n}: {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W8b: done, {fail} failures')
sys.exit(1 if fail else 0)
