# GS Week 11 adult re-authoring (Any Doubts?).
import io, sys, re
f = 'docs/getting-started/week-11-doubts.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')
R('- Junior teens drifting into hypotheticals. “What if dinosaurs?” Redirect: “One thing you say you believe, that something in you isn’t fully sure about. Not a debate question — a heart question.”',
  '- Drifting into hypotheticals and debate questions. Redirect: “One thing you say you believe, that something in you isn’t fully sure about. Not a debate question — a heart question.”')
R('- Parents importing apologetics-class instincts. Especially in CCA’s context, parents may feel responsible to argue their children out of doubts. The Any Doubts? practice is the opposite of that. The team must model receiving without arguing.',
  '- Importing apologetics-class instincts. Leaders especially may feel responsible to argue a partner out of doubts — it is what they are trained for. The Any Doubts? practice is the opposite of that. The team must model receiving without arguing.')
R('**If a teen surfaces material that suggests trauma underneath the doubt.** Receive. Bless. Do not interpret. Section 6 protocol if it crosses the safety threshold. Pastoral 1:1 within the week.',
  '**If a member surfaces material that suggests trauma underneath the doubt.** Receive. Bless. Do not interpret. The safeguarding frame if it crosses the safety threshold. Pastoral 1:1 within the week.')
R('Do not skip this. The teens will know within thirty seconds whether you have done your own version of what you are about to ask them to do.',
  'Do not skip this. The room will know within thirty seconds whether you have done your own version of what you are about to ask them to do.')
R('''- In the parent cohort: do not pair spouses with each other. Pair each parent with another parent.
- In the senior cohort: avoid pairing dating couples or close best-friends if possible. Some emotional separation makes the practice work better.
- In the junior cohort: pair across friendship groups when possible. Two best friends doing this together can drift into giggles or self-protection.''',
  '''- Do not pair spouses with each other, and avoid pairing closest friends or long-standing ministry partners where possible. Some emotional separation makes the practice work better.
- Pair across the cohort’s natural clusters — staff with lay, veteran with newer. The slight stretch serves the honesty.''')
R('| T-15 min | Door opens. | Co-Comp (Teen) |', '| T-15 min | Door opens. | Co-Comp |')
R('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags, phone-box. |',
  '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags, phone-box. |')
R('| 8:20–8:23 | Block 8: Between-session practice | Shared circle | Co-Comp (Parent) | Personal Doubts Inventory: one page in journal this week. |',
  '| 8:20–8:23 | Block 8: Between-session practice | Shared circle | Co-Comp | Personal Doubts Inventory: one page in journal this week. |')
R('*“Junior teens with [name]. Senior teens with [name]. Parents with [name]. Thirty-five minutes. Go.”*',
  '*“[Name]’s circle, this side. [Name]’s circle, that side. Thirty-five minutes. Go.”*')
R('*“One note: next Tuesday is Week 12 — we turn outward to Mission. After that comes the Rhythm week, and then the two closing gatherings: the family commissioning and the commissioning of our Companions-in-Formation. Plan to bring your whole family to those last two. We are heading toward the sending.”*',
  '*“One note: next week is Week 12 — we turn outward to Mission. After that comes the Rhythm week, and then the two closing gatherings: the household blessing night and the commissioning. Plan to bring your households to the first of those. We are heading toward the sending.”*')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}'); fail += 1; continue
    s = s.replace(old, new)

i = s.index('## **Junior teens (12–14)**')
j = s.index('# **Closing Practice') if '# **Closing Practice' in s else s.index('# Closing Practice')
new_diff = '''## Those doing this work for the first time

- Watch for drifting into hypotheticals. Redirect to a heart-doubt: “Something you say you believe — about you, about God — that something inside you isn’t fully sure about.”
- Watch for the member who insists they have no doubts and seems anxious about it. Affirm: “Only the most honest people I know name doubts. You’re in good company either way.”
- Sample scriptures (H11.3): Psalm 139:14, Romans 8:38–39, 1 John 4:19, Matthew 11:28–30 remain good first texts.

## The veterans

- Sample scriptures (H11.3) include texts the seasoned often quietly doubt: Romans 8:28, Jeremiah 29:11, Psalm 23:1, John 14:1–3, James 1:5, Philippians 4:6–7.
- Watch for: the member who wants to debate their partner’s doubt. Redirect: “You’re not the apologetics class tonight. Read, listen, re-read.”
- Watch for: the member whose doubt is bigger than the exercise. (“I’m not sure I believe any of this anymore.”) Receive without alarm — a leader saying this aloud has carried it alone a long time. The Companion does not chase it. The convening leader follows up within 48 hours. Real doubts of that scale deserve real conversation, and the door out is real.
- Watch for: the member who performs honesty — a doubt that sounds impressive but is not actually theirs. Gently: “That sounds true in general. What’s the smaller, more personal version of that?”

## The ordained and the staff

- Watch for: the member who imports apologetics. “You know, scholars have shown that \\_\\_\\_\\_\\_.” Redirect: “You are not the answer-man tonight. You are the witness.”
- Watch for: the member whose doubt centers on someone they love. “I doubt God will protect my daughter from \\_\\_\\_\\_\\_.” This is real and appropriate; honor it. The pair partner just listens and re-reads.
- Watch for: the member who realizes mid-practice that they have been carrying a significant doubt about a specific painful event — a church split, a death, an unanswered prayer — for years. The naming may be heavy. The Companion stays close; the convening leader follows up within the week.
- The pulpit corollary, named at the debrief if it showed: some of the ordained have preached certainty over a private doubt for years. Tonight’s naming is the beginning of relief, not a crisis. Treat it that way.

'''
s = s[:i] + new_diff + s[j:]

io.open(f, 'w', encoding='utf-8').write(s) if fail == 0 else None
print(f'W11: {len(E)} pair edits + diff rewrite, {fail} failures')
res = [m.group(0)[:100] for m in re.finditer(r'^.*\b(teens?|parents?|juniors?|seniors?|CCA)\b.*$', s, re.M | re.I)]
print('residual lines:', len(res))
for r in res[:12]: print('  ', r)
sys.exit(1 if fail else 0)
