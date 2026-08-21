# GS Week 12 adult re-authoring (Mission).
import io, sys, re
f = 'docs/getting-started/week-12-mission.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')
R('- Performance instincts. Senior teens and parents will be tempted to give the polished, college-essay version of their gifts. Push for specificity.',
  '- Performance instincts. Leaders will be tempted to give the polished, ministry-résumé version of their gifts. Push for specificity.')
R('- The teen who says “I don’t have any gifts.” This is rarely true and often the inversion of pride. Honor it; do not rescue. Ask the cohort: “What do the rest of us notice about [name]?”',
  '- The member who says “I don’t have any gifts.” This is rarely true and often the inversion of pride. Honor it; do not rescue. Ask the cohort: “What do the rest of us notice about [name]?”')
R('- The parent who turns the exercise into vocational guidance for their teen-in-another-room. Tonight is your own mission, not your kid’s.',
  '- The member who turns the exercise into vocational guidance for someone else — a child, a mentee, the congregation. Tonight is your own mission, not theirs.')
R('- The senior who already knows their mission and presents a polished answer. Affirm, then ask the harder question: “What does the room get when you’re not performing that mission — just being you?”',
  '- The member who already knows their mission and presents a polished answer — in a leadership cohort, most of the room. Affirm, then ask the harder question: “What does the room get when you’re not performing that mission — just being you?”')
R('**If a teen surfaces that they feel they have no gifts and seems anxious.** Affirm: “You do. You may not have language for them yet. Tonight we ask the cohort to help.” Invite the cohort to name what they see. Brief warm follow-up within the week.',
  '**If a member surfaces that they feel they have no gifts and seems anxious.** Affirm: “You do. You may not have language for them yet. Tonight we ask the cohort to help.” Invite the cohort to name what they see. Brief warm follow-up within the week.')
R('**If a parent surfaces deep mid-life vocational grief.** Honor it. Do not promise resolution. Pastoral 1:1 within the week if welcomed.',
  '**If a member surfaces deep mid-life vocational grief — including grief about the ministry itself.** Honor it. Do not promise resolution. Pastoral 1:1 within the week if welcomed.')
R('5. Begin printing for Week 14 — Family Commissioning. (Some Week 14 prep takes lead-time; see Week 14 plan.)',
  '5. Begin printing for Week 14 — the Household Blessing Night. (Some Week 14 prep takes lead-time; see Week 14 plan.)')
R('| T-15 min | Door opens. | Co-Comp (Teen) |', '| T-15 min | Door opens. | Co-Comp |')
R('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags, phone-box. |',
  '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags, phone-box. |')
R('| 8:14–8:21 | Block 7: Between-session practice and closing-weeks logistics | Shared circle | Co-Comp (Parent) | One small action. Then the road ahead: Wk 13 Rhythm, Wk 14 family commissioning (bring family), Wk 15 Companion commissioning. |',
  '| 8:14–8:21 | Block 7: Between-session practice and closing-weeks logistics | Shared circle | Co-Comp | One small action. Then the road ahead: Wk 13 Rhythm, Wk 14 household blessing night (bring your household), Wk 15 the commissioning. |')
R('*Watch for: be brief and be specific. The teens will calibrate against your honesty. Do not give the resume version. Give the version your spouse would recognize.*',
  '*Watch for: be brief and be specific. The room will calibrate against your honesty. Do not give the résumé version. Give the version your spouse would recognize.*')
R('*“Junior teens with [name]. Senior teens with [name]. Parents with [name]. Forty minutes. Go.”*',
  '*“[Name]’s circle, this side. [Name]’s circle, that side. Forty minutes. Go.”*')
R('*“Second — the road from here. Next Tuesday, Week 13, is the Rhythm week: we build the practices you will carry when the Tuesdays stop, and we finish tonight’s mission work. Then Week 14 is the family commissioning — bring your whole family, even family members who have not been here. Spouses, siblings, grandparents who can come — invite them. And Week 15 is the commissioning of our Companions-in-Formation — the seniors who have been leading us. That one is their night; come to witness it.”*',
  '*“Second — the road from here. Next week, Week 13, is the Rhythm week: we build the practices you will carry when the meetings stop, and we finish tonight’s mission work. Then Week 14 is the household blessing night — bring your household, the people this year has been forming you for. Spouses, kids, parents who can come — invite them. And Week 15 is the commissioning — the covering sends this cohort. That night, we are the ones being sent.”*')
R('*“See you Tuesday — 6:30 — with your family.”*',
  '*“See you next week — 6:30 — and start inviting your household for Week 14.”*')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}'); fail += 1; continue
    s = s.replace(old, new)

i = s.index('## **Junior teens (12–14)**')
j = s.index('# **Closing Practice') if '# **Closing Practice' in s else s.index('# Closing Practice')
new_diff = '''## Those doing this work for the first time

- The Gifts and Passions inventory works with concrete prompts: what people thank you for, what you would do without being paid, where you lose track of time.
- Watch for: the member who can’t name a single gift. The circle is the gift here — the cohort can name what it has seen. “[Name], I’ve noticed you’re the one who notices when somebody is left out.” Receive specifics from the room.
- Watch for: performing modesty (“I don’t really have any gifts” as social code). Affirm: “Tonight isn’t bragging. It’s noticing what God put in. Try one.”

## The veterans

- Veterans are the most likely to have already constructed a polished version of their gifts — years of introductions and bios do it. Push for the unpolished, downhill version.
- Watch for: the member with a mission statement. Affirm; ask the harder question: “When you’re not running that mission — just being you — what does the room get?”
- Watch for: the downhill answer that reveals shadow mission (gifts directed inward, performance-shaped). The Companion names this gently if it surfaces clearly: “What I want to bless is the gift. The shadow direction is yours to keep watching in Going Deeper.”

## The ordained and the staff

- The ordained may surface grief about gifts long unused — the thing they came alive doing before the role swallowed it — or seasons of shadow mission. This is part of the work. Honor without rushing.
- Watch for: mission framed as the job. Re-frame: “Mission in scripture is bigger than the role. What does the room get when you’re at your best, regardless of what you’re paid to do?”
- Watch for: the downhill answer that is entirely about others (“when I’m at my best, the congregation gets \\_\\_\\_\\_\\_”). This is real. Honor it — and then ask what *they* get, because a mission that never feeds its carrier is a candidate for the shadow.

'''
s = s[:i] + new_diff + s[j:]

io.open(f, 'w', encoding='utf-8').write(s) if fail == 0 else None
print(f'W12: {len(E)} pair edits + diff rewrite, {fail} failures')
res = [m.group(0)[:100] for m in re.finditer(r'^.*\b(teens?|parents?|juniors?|seniors?|CCA|famil(?:y|ies))\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:14]: print('  ', r)
sys.exit(1 if fail else 0)
