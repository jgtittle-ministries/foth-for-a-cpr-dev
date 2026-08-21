# GS Week 14 adult re-authoring: the family commissioning becomes the
# household blessing night — the year turned homeward.
import io, sys, re
f = 'docs/getting-started/week-14-sending.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')
R('**Aim.** Integration of all four Connects (Self, Others, God, Mission) through a family commissioning. Each parent-and-teen dyad stands in the center of the room; each speaks a specific blessing over the other; the whole community speaks the Aaronic blessing over each family. The family commissioning sends the cohort into the interlude with a clear bridge into the Going Deeper series; the series\' one remaining gathering, Week 15, commissions the Companions-in-Formation.',
  '**Aim.** Integration of all four Connects (Self, Others, God, Mission) through the household blessing. Tonight the leadership-first year turns homeward: each member stands in the center with their household — the people this year has been forming them for — and speaks a specific blessing over them; the whole community speaks the Aaronic blessing over each household. The night sends the cohort into the interlude with a clear bridge into the Going Deeper series; the one remaining gathering, Week 15, is the commissioning, where the covering sends the cohort.')
R('**Mode.** Shared circle the entire session. Parents and teens together intentionally for the family commissioning — NO cohort split tonight.',
  '**Mode.** Shared circle the entire session. Members and their households together intentionally for the blessing — NO circle split tonight, and the room is full of guests.')
R('**Center.** Family commissioning. Each parent-and-teen dyad stands in the center of the circle. Each speaks a specific witnessed blessing over the other. The whole community speaks the Aaronic blessing over each family. Final reflection circle: each person’s one specific takeaway and one specific next commitment. Post-Series Survey distributed for completion that week.',
  '**Center.** The household blessing. Each member stands in the center of the circle with their household. The member speaks a specific witnessed blessing over each of their people; household members who wish may speak one back. The whole community speaks the Aaronic blessing over each household. Final reflection circle: each person’s one specific takeaway and one specific next commitment. Post-Series Survey distributed for completion that week.')
R('- The teen whose parent is not present. Some families will not have both parents in the room; some teens come from divorce, bereavement, or estrangement. Pre-plan with each affected family. The cohort may stand for the absent parent; a Co-Companion may stand in; or the teen may receive the community blessing without a family commissioning. Decide in advance, never on the night.',
  '- The member whose household is not present. Some households cannot come; some members live alone; some carry estrangement or grief. Pre-plan with each affected member. The cohort stands as household — this room has been one all year — or a chosen stand-in receives the blessing on the household’s behalf. Decide in advance, never on the night.')
R('- Emotional flooding. Tears tonight are common, appropriate, and welcome — from teens, from parents, from Companions. Plan for this; do not be surprised by it.',
  '- Emotional flooding. Tears tonight are common, appropriate, and welcome — from members, from guests, from Companions. Plan for this; do not be surprised by it.')
R('- Logistics overwhelm. Tonight has more moving parts than any prior session: extended start time, family members new to the room, food, blessing rehearsals, the commissioning itself, the survey, the bridge to Going Deeper. The team must not let logistics consume what should be a sacred close.',
  '- Logistics overwhelm. Tonight has more moving parts than any prior session: extended start time, households new to the room, food, blessing rehearsals, the blessings themselves, the survey, the bridge to Going Deeper. The team must not let logistics consume what should be a sacred close.')
R('*“For those of you new tonight: phones in the box, please. Find a seat with your family.”*',
  '*“For those of you new tonight: phones in the box, please. Find a seat with your person.”*')
R('*“So tonight we are going to do something specific. Each parent-and-teen pair from Getting Started is going to stand in the center of this circle. Each of you is going to speak a specific witnessed blessing over the other. The whole community is going to speak the Aaronic blessing over each family. We are going to send each other into what comes next.”*',
  '*“So tonight we are going to do something specific. Each member of this cohort is going to stand in the center of this circle with the people they came with — the people this whole year has been for. Each member is going to speak a specific witnessed blessing over their own household, in front of us all. And the whole community is going to speak the Aaronic blessing over each household. First for ourselves, then for the people we love: tonight is the turn.”*')
R('*Watch for: the demo is critical. Parents who have never spoken a blessing aloud will calibrate against this. Be brief. Be specific. Do not preach.*',
  '*Watch for: the demo is critical. Members who have never spoken a blessing aloud over their own family will calibrate against this. Be brief. Be specific. Do not preach.*')
R('Bless every family in this room with the words your servants will speak over them. Receive the work of Getting Started; multiply it across what comes next. Amen.”*',
  'Bless every household in this room with the words your servants will speak over them. Receive the work of Getting Started; multiply it across what comes next. Amen.”*')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}'); fail += 1; continue
    s = s.replace(old, new)

# Block 4 core restructure
i = s.index('## **Block 4 — Family Commissionings (7:05–8:00, 55 min)**')
j = s.index('## **Block 5 — Final Reflection Circle (8:00–8:15, 15 min)**')
new_b4 = '''## **Block 4 — The Household Blessings (7:05–8:00, 55 min)**

This is the heart of the night. Each member in turn, with their household. The convening leader calls each forward; a Co-Companion helps with timing and transitions. Approximately five to seven minutes per household. Do not rush; do not run long.

### **The structure inside each blessing**

## Per household (≈ 5–7 min)

**1. The convening leader calls the member forward. “[Name], bring your people to the center.” The member stands with their household; if the household is large, they gather close.**

**2. Brief framing. The convening leader speaks one sentence about the member: ‘We have walked with [name] through Getting Started; we have seen \\_\\_\\_\\_\\_.’ 30–60 seconds.**

**3. The member blesses their household. Each person briefly, or the household together — pre-planned on the worksheet. Three sentences per blessing: what I see in you, what I bless in you, what I commit to you. ≈ 60–90 seconds per person; brevity is the discipline.**

**4. The household may bless back. Any household member who wishes — a spouse, a child of any age, a parent — speaks a blessing or a sentence over the member. Extemporaneous is fine; one true sentence is enough; nothing is required of guests. ≈ 60–90 seconds.**

**5. Community blessing. The convening leader: ‘Household of [name], the community now blesses you.’ The whole room speaks the Aaronic blessing aloud together, slowly. Hands may extend; some households hold each other.**

**6. The household returns to seats. 30 seconds of breath before the next is called.**

## The convening leader: when to intervene

- If a member freezes or cannot read their blessing — quietly: “Take your time.” Do not push. A leader who has blessed rooms for years may find their own kitchen table the hardest audience of their life. That difficulty is the point of the night; give it room.
- If a guest is overwhelmed — silence. Wait. If a child cannot speak, a smile and a standing-close is a complete blessing.
- If a blessing surfaces unexpected household material — do not interpret in the room. Complete the blessing if possible. Pastoral 1:1 follow-up.
- If a member arrived without the worksheet — an extra minute, or extemporaneous: ‘Just one specific thing you have seen God doing in your wife, your son, your mother. One thing.’
- If the time-keeper signals you are running long — compress the framing for subsequent households to one sentence. Do not compress the blessings themselves.
- Watch the absent-household situations — these were pre-planned in team meeting 2. Stick to the plan.

### **Time math — do this in advance**

With 55 minutes and approximately 6 minutes per household, the room can hold 8–9 blessings. If you have more members, lengthen Block 4 by 10–15 minutes and shorten Block 6. If fewer, add a brief silence or a brief reading at the end of Block 4 to honor the space.

'''
s = s[:i] + new_b4 + s[j:]

more = [
('*“You can pass. Visiting family members can pass; you can also share if you want to. The Cohort Companions go first.”*',
 '*“You can pass. Guests can pass; you can also share if you want to. The Companions go first.”*'),
('*(Cohort Companions go first to model. Then around the circle. Lead Companion listens; receives without commentary; eye contact; slight nod. Do not summarize.)*',
 '*(The Companions go first to model. Then around the circle. The convening leader listens; receives without commentary; eye contact; slight nod. Do not summarize.)*'),
('Weekly — a brother or sister or family member who knows what you are working on.',
 'Weekly — a brother or sister or household member who knows what you are working on.'),
('*“Three: the Post-Series Survey. H14.5. We need your honest read on what worked and what didn’t. Complete it this week and email it back. The next group of families benefits from your honesty. Five questions; take fifteen minutes.”*',
 '*“Three: the Post-Series Survey. H14.5. We need your honest read on what worked and what didn’t. Complete it this week and email it back. The next cohort benefits from your honesty. Five questions; take fifteen minutes.”*'),
('The last five minutes. The whole community speaks the Aaronic blessing over the whole community. The families are sent; Week 15\'s commissioning of the Companions remains.',
 "The last five minutes. The whole community speaks the Aaronic blessing over the whole community. The households are sent; Week 15's commissioning remains."),
('*“One last thing. We have spoken the Aaronic blessing over each family tonight. Now the whole community speaks it over the whole community.”*',
 '*“One last thing. We have spoken the Aaronic blessing over each household tonight. Now the whole community speaks it over the whole community.”*'),
('*“You are sent. Walk gently. He who began this work in you will bring it to completion. One more gathering remains: next Tuesday we commission our Companions-in-Formation — the seniors who led us this year. It is their night, and you are all wanted in the room for it. Go.”*',
 '*“You are sent. Walk gently. He who began this work in you will bring it to completion. One more gathering remains: next week is the commissioning — the covering sends this cohort into what the year was for. It is our sending, and you are all wanted in the room for it. Go.”*'),
]
for old, new in more:
    n = s.count(old)
    if n != 1:
        print(f'!! (more) count={n}: {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)

# Differentiation section rewrite
i = s.index('# **Differentiation by Cohort**')
j = s.index('# **Closing Practice in Detail**')
new_diff = '''# **Differentiation by Household Situation**

Tonight there is no circle split. Members and their households are intentionally together. The differentiation tonight is by household situation, and every situation was pre-planned in team meeting 2 — never decided on the night.

## **Households with several present**

- The member may bless each person briefly, or the household together — pre-planned on the worksheet. Time budget: ≈7–8 minutes for larger households.
- Children of any age may bless back in one sentence, or simply stand close. Nothing is required of guests.

## **Members whose spouse alone is present**

- Standard blessing, both directions if the spouse wishes. Time budget ≈5–6 minutes.
- If the marriage has walked through this year’s confession or doubt work, the blessing may carry more than the room knows. The Companion team receives it without comment.

## **Members whose household cannot come, or who live alone**

- Pre-decided: the cohort stands as household — this room has been one all year — or a chosen stand-in (a cohort friend, a Companion) receives the blessing on the household’s behalf: ‘what I want my family to know is \\_\\_\\_\\_\\_.’
- The community blessing follows in full. Nobody is sent unwitnessed.
- This is heavy for some. Pastoral / clinical backup is informed in advance. Pastoral 1:1 the next day.

## **Households carrying estrangement or grief**

- If an absence is grief (death, deployment, estrangement), the convening leader may briefly honor it by name in the framing — pre-discussed with the member, never sprung.
- The cohort may stand for the absent one. The convening leader invites this gently.

## **Guests unfamiliar with all of this**

- Some household members have never seen this room and have no words for it. Their job is to bear witness; their presence is the gift — say so from the front, warmly, twice.
- A guest asked to receive a blessing needs only to stand and hear it. Coach members beforehand: do not ask your household to perform.

'''
s = s[:i] + new_diff + s[j:]

more2 = [
('- Every family commissioning was completed. Every teen heard a blessing from a parent or stand-in; every parent heard a blessing from a teen.',
 '- Every household blessing was completed. Every member spoke; every household was witnessed; nobody was sent unblessed.'),
('- Visiting family members who had not been here engaged — received, witnessed, sometimes spoke.',
 '- Guests who had never been here engaged — received, witnessed, sometimes spoke.'),
('- Several families lingered after; the room emptied slowly.', '- Several households lingered after; the room emptied slowly.'),
('- At least three families have asked specific questions about Going Deeper.',
 '- Several members and guests have asked specific questions about Going Deeper.'),
('- A family’s commissioning had to be cut short for time.', '- A household’s blessing had to be cut short for time.'),
('- A teen could not complete their blessing and the Cohort Companion did not have a graceful recovery.',
 '- A member could not complete their blessing and the team did not have a graceful recovery.'),
('- Visiting family members felt lost or uncertain.', '- Guests felt lost or uncertain.'),
('- Every family. Personal note (text or email) within 48 hours. “Thank you for tonight. What I noticed about your family is \\_\\_\\_\\_\\_.” Specific.',
 '- Every member. Personal note (text or email) within 48 hours. “Thank you for tonight. What I noticed about your household is \\_\\_\\_\\_\\_.” Specific.'),
('- Any teen whose blessing surfaced significant material. Pastoral 1:1 within the week.',
 '- Any member whose blessing surfaced significant material. Pastoral 1:1 within the week.'),
('- Any family with absent-parent situation — special check-in.', '- Any member with an absent-household situation — special check-in.'),
('- Which families are most likely to continue? Which need a personal invitation?',
 '- Which members are most likely to continue? Which need a personal invitation?'),
('(Bring this to John for the IJH project.)', '(Send it back to the project — the curriculum grows by exactly this kind of report.)'),
('- H14.1 — Family Commissioning Worksheet (sent to families the Friday before)',
 '- H14.1 — Household Blessing Worksheet (sent to members the Friday before)'),
('- H14.2 — Aaronic Blessing Card (one per family present)', '- H14.2 — Aaronic Blessing Card (one per household present)'),
('**Handout H14.1 — Family Commissioning Worksheet**', '**Handout H14.1 — Household Blessing Worksheet**'),
('*Sent to families the Friday before Week 14*', '*Sent to members the Friday before Week 14*'),
('*Each parent and each teen prepares a three-sentence blessing for the other before Tuesday. Use this worksheet. Bring it back Tuesday — you may read from it during the commissioning.*',
 '*Each member prepares a three-sentence blessing for each person of their household — or one for the household together — before the night. Use this worksheet. Bring it back — you may read from it during the blessing. Household members who wish to speak one back may use the same three sentences; nothing is required of guests.*'),
('H14.1 is distributed to families one week before; the rest are distributed at the door.',
 'H14.1 is distributed to members one week before; the rest are distributed at the door.'),
]
for old, new in more2:
    n = s.count(old)
    if n != 1:
        print(f'!! (more2) count={n}: {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W14: {len(E)+len(more)+len(more2)} pair edits + 2 section rewrites, {fail} failures')
res = [m.group(0)[:100] for m in re.finditer(r'^.*\b(teens?|parents?|juniors?|seniors?|dyads?|CCA)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:20]: print('  ', r)
sys.exit(1 if fail else 0)
