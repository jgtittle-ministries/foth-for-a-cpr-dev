# GS Week 5 adult re-authoring.
import io, sys
f = 'docs/getting-started/week-05-known.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')
R('- Teens who quietly admit they don’t have a friendship that has any of the four conditions. This is real data, not a problem. Receive it. Do not rescue. The recognition is the first step.',
  '- Members who quietly admit they don’t have a friendship that has any of the four conditions. This is real data, not a problem — and it is common in ministry. Receive it. Do not rescue. The recognition is the first step.')
R('- Parents who lecture about friendship choices. The parent cohort is mapping their own adult friendships, not coaching their kids by proxy.',
  '- Members who lecture about friendship in general. The cohort is mapping its own adult friendships, not diagnosing the congregation’s by proxy.')
R('- The seniors who name a specific friendship as missing all four conditions and are sitting next to that person in the room. Use anonymizing language: “one of my friendships,” not names.',
  '- Members who name a specific friendship as missing all four conditions while sitting next to that person in the room — in a leadership cohort this is likely. Use anonymizing language: “one of my friendships,” not names.')
R('*Week 5 is unlikely to surface an acute crisis. The risk profile is closer to Week 2 than Week 3. But “I don’t have a single friend who knows me” from a teen is its own quiet emergency — receive it, follow up offline within 48 hours, and watch them in Weeks 6–15. Default to Section 6 of the Handbook for any disclosure that crosses the safety threshold.*',
  '*Week 5 is unlikely to surface an acute crisis. The risk profile is closer to Week 2 than Week 3. But “I don’t have a single friend who knows me” from a church leader is its own quiet emergency — more common in ministry than anyone says aloud. Receive it, follow up offline within 48 hours, and watch them through the rest of the series. Default to the safeguarding frame (Leadership Year Handbook §7) for any disclosure that crosses the safety threshold.*')
R('2. Print three Friendship Map worksheets (H5.2 junior, H5.3 senior, H5.4 parent).',
  '2. Print the Friendship Map worksheet (H5.2), one per member.')
R('| T-15 min | Door opens. Same arrival rhythm. | Co-Comp (Teen) |',
  '| T-15 min | Door opens. Same arrival rhythm. | Co-Comp |')
R('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags, phone-box. |',
  '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags, phone-box. |')
R('| 8:11–8:19 | Block 7: Between-session practice | Shared circle | Co-Comp (Parent) | Pick one friendship; pick one condition; practice it this week. |',
  '| 8:11–8:19 | Block 7: Between-session practice | Shared circle | Co-Comp | Pick one friendship; pick one condition; practice it this week. |')
R('*“Last week we told stories in our cohort circles, and the between-session practice was the Joint Footprints exercise — some parent-and-teen pairs sitting together for twenty minutes with the footprints question. Some of you got to it. Some didn’t. Both are fine. Anyone want to say one sentence about how that landed for you?”*',
  '*“Last week we completed the round of stories, and the between-session practice was the Shared Footprints exercise — twenty minutes with your spouse or one person close to you, walking the footprints question. Some of you got to it. Some didn’t. Both are fine. Anyone want to say one sentence about how that landed for you?”*')
R('*“We are not naming names tonight. ‘One of my friends’ is fine. ‘My senior-year best friend’ is too specific. We are looking at the conditions, not exposing anyone in our lives.”*',
  '*“We are not naming names tonight. ‘One of my friends’ is fine. ‘My college roommate who lives in Ohio’ is too specific. We are looking at the conditions, not exposing anyone in our lives.”*')
R('*“Junior teens with [name]. Senior teens with [name]. Parents with [name]. Twenty-eight minutes. We come back here at 8:00. Go.”*',
  '*“[Name]’s circle, this side. [Name]’s circle, that side. Twenty-eight minutes. We come back here at 8:00. Go.”*')
R('- If a teen says, “I don’t have any friendships with any of these conditions,” receive it. Do not rescue. Mark it for the team debrief and follow up with the Lead Companion after the session.',
  '- If a member says, “I don’t have any friendships with any of these conditions,” receive it. Do not rescue. Mark it for the team debrief and follow up with the convening leader after the session.')
R('If a participant chooses a friendship that is in the room — e.g., a teen choosing a parent in the parent cohort — that is fine, but the practice is theirs alone. The other person does not need to know they are being practiced upon.',
  'If a participant chooses a friendship that is in the room — likely, in a leadership cohort — that is fine, but the practice is theirs alone. The other person does not need to know they are being practiced upon.')
R('- Any parent who realizes their marriage maps mostly to the absence of conditions. Pastoral 1:1 within the week if welcomed.',
  '- Any member who realizes their marriage maps mostly to the absence of conditions. Pastoral 1:1 within the week if welcomed.')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}'); fail += 1; continue
    s = s.replace(old, new)

# Differentiation rewrite
i = s.index('## Junior teens (12–14)')
j = s.index('# Closing Practice')
new_diff = '''## Those doing this work for the first time

- Concrete language. The Companion’s model turn should be especially specific — abstract language wastes the exercise; the room needs to hear what each condition sounds like in a real story.
- “Friendship” may honestly include a sibling, a mentor, an old pastor. Allow it; it is honest.
- Watch for the member with no real friendship in any condition. Receive without panic. Note for the convening leader.

## The veterans

- Veterans are often closest to noticing the absence of conditions — decades supply the evidence. Honor it with specificity.
- Watch for the member performing wisdom. “I think a lot of people don’t have real friendships these days.” Redirect: “You — not other people. Where is each condition in your friendships?”
- Some will name a friendship that ended badly, or a ministry friendship lost to a church season. Honor it; do not press.
- Watch for the member mapping a friendship with someone sitting in the room. The Companion may help: “Let’s use ‘one of my friendships’ here.”

## The ordained and the staff

- Members will often name friendships that changed shape — “the friendship I had ten years ago that we don’t have anymore,” or the friendships a call to ministry quietly cost. Honor these.
- Watch for the member who maps their marriage. Allow it; marriage is a friendship, and the four conditions apply. Do not let it become a marriage workshop.
- Watch for the member who turns the exercise into a critique of someone else’s friendships — their kids’, the congregation’s. Redirect: “Your friendships, not theirs.”
- Members who realize they don’t have a single friendship with all four conditions — this is common in ministry and not pathological. The naming is the gift.

'''
s = s[:i] + new_diff + s[j:]

# Handouts: consolidate maps
more = [
('''Five handouts for Week 5.

- H5.1 — The Four Conditions Card (all cohorts)
- H5.2 — Friendship Map Worksheet (Junior, ages 12–14)
- H5.3 — Friendship Map Worksheet (Senior, ages 15–18)
- H5.4 — Friendship Map Worksheet (Parent)
- H5.5 — Between-Session Practice Card''',
'''Three handouts for Week 5.

- H5.1 — The Four Conditions Card
- H5.2 — Friendship Map Worksheet
- H5.3 — Between-Session Practice Card'''),
('**Handout H5.4 — Friendship Map (Parent)**\n\n*Tonight in your circle, you’ll talk through these four questions — one for each condition. Think about your real adult friendships: a close friend, your marriage, a friendship that has changed shape over the years, a work friendship, a friendship from before you had kids. No names. “One of my friendships” is the language.*',
 '**Handout H5.2 — Friendship Map**\n\n*Tonight in your circle, you’ll talk through these four questions — one for each condition. Think about your real adult friendships: a close friend, your marriage, a friendship that has changed shape over the years, a work friendship, a friendship from before you had kids. No names. “One of my friendships” is the language.*'),
('**Handout H5.5 — Between-Session Practice (Week 5)**',
 '**Handout H5.3 — Between-Session Practice (Week 5)**'),
]
for old, new in more:
    n = s.count(old)
    if n != 1:
        print(f'!! (more) count={n}: {old[:60]}'); fail += 1; continue
    s = s.replace(old, new)

# delete junior + senior map bodies
i = s.index('**Handout H5.2 — Friendship Map (Junior, ages 12–14)**')
j = s.index('**Handout H5.2 — Friendship Map**')
if i < j:
    s = s[:i] + s[j:]
    print('OK  junior+senior maps removed')
else:
    print('!! map order unexpected'); fail += 1

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W5: done, {fail} failures')
sys.exit(1 if fail else 0)
