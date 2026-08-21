# GS Week 7 adult re-authoring (PROAPT I).
import io, sys
f = 'docs/getting-started/week-07-proapt.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')
R('- The teen who comes back to Week 7 still carrying Week 6. Honor that. Pull them aside before the session if possible.',
  '- The member who comes back to Week 7 still carrying Week 6. Honor that. Pull them aside before the session if possible.')
R('Every Companion does PROAPT on at least three different passages in the week before this session. The goal is not to prepare the demo but to be a current practitioner. The teens will know within sixty seconds whether you are someone who has done PROAPT this week or someone who is teaching it from notes.',
  'Every Companion does PROAPT on at least three different passages in the week before this session. The goal is not to prepare the demo but to be a current practitioner. The room will know within sixty seconds whether you are someone who has done PROAPT this week or someone who is teaching it from notes.')
R('| T-15 min | Door opens. Standard arrival. | Co-Comp (Teen) |',
  '| T-15 min | Door opens. Standard arrival. | Co-Comp |')
R('| 6:45–7:00 | Arrival window | Forming | Co-Comp (Teen) | Standard arrival. |',
  '| 6:45–7:00 | Arrival window | Forming | Co-Comp | Standard arrival. |')
R('*“For what to read — if you don’t already have a plan, the handout (hold up H7.3) has age-tiered passage suggestions. Junior cohort: simple Gospel passages, one a day. Senior cohort: Sermon on the Mount or Romans 8 worked through one passage at a time. Parents: same options or pick from your current reading.”*',
  '*“For what to read — if you don’t already have a plan, the handout (hold up H7.3) has passage suggestions: a Gospel walked one story a day, the Sermon on the Mount or Romans 8 worked slowly, or a Psalm-and-Gospel pairing. Already have a reading plan? Stay with it and layer PROAPT on top.”*')
R('- Next week is PROAPT II — a Companion-in-Formation leads the full walk-through. If tonight was thin on Apply, coach the senior this week to slow the Apply step and use the specific-situation prompt.',
  '- Next week is PROAPT II — a rotation leader leads the full walk-through. If tonight was thin on Apply, coach them this week to slow the Apply step and use the specific-situation prompt.')
R('- H7.3 — Passage Suggestions for the Week (Junior, Senior, Parent)',
  '- H7.3 — Passage Suggestions for the Week')
R('*One passage per day for the next seven days. Pick from your cohort’s list, or stay with one Gospel and go in order.*',
  '*One passage per day for the next seven days. Pick a track below, or stay with one Gospel and go in order.*')
R('## **Junior cohort (12–14) — Mark 1–2**\n\n*Short narrative passages. Each one is a complete story. Five to seven minutes for the whole PROAPT.*',
  '## **Track one — Mark 1–2, a story a day**\n\n*Short narrative passages. Each one is a complete story. A good first track: five to seven minutes for the whole PROAPT while the practice is new.*')
R('## **Senior cohort (15–18) — Sermon on the Mount or Romans 8**\n\n*Pick one. Stay in it. The Sermon (Matthew 5–7) reads as one passage of teaching; Romans 8 reads as one extended argument. Ten to fifteen minutes per session.*',
  '## **Track two — Sermon on the Mount or Romans 8**\n\n*Pick one. Stay in it. The Sermon (Matthew 5–7) reads as one passage of teaching; Romans 8 reads as one extended argument. Ten to fifteen minutes per session.*')
R('## **Parent cohort — your choice or a Psalm-and-Gospel pairing**\n\n*Many parents already have a reading plan. Stay with it; layer PROAPT on top of what you are already reading. If you want a fresh path, try one of these:*',
  '## **Track three — your current reading, or a Psalm-and-Gospel pairing**\n\n*Many of you already have a reading plan. Stay with it; layer PROAPT on top of what you are already reading. If you want a fresh path, try this pairing:*')
R('*Tell step counts even if it is just to your spouse, sibling, or Cohort Companion by text. Speak what you heard.*',
  '*Tell step counts even if it is just to your spouse, a friend, or your circle Companion by text. Speak what you heard.*')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}'); fail += 1; continue
    s = s.replace(old, new)

i = s.index('## **Junior teens (12–14)**')
j = s.index('# **Closing Practice')
new_diff = '''## Those doing this work for the first time

- Short passages, complete stories. Five to seven minutes for the whole PROAPT while it is new.
- Tell step works well — first-timers often surprise themselves with what comes out when they say it aloud.
- Watch for the Sunday-school answer in Apply. Push gently for one specific thing from this week.

## The veterans

- PROAPT scales fully. Veterans can hold longer passages and deeper Apply work.
- Watch for the member whose Observe is sophisticated but whose Apply is generic — decades of Bible study make excellent hiding. Push for specificity.
- Watch for the member who treats PROAPT as a Bible study technique they already know. Frame it as a hearing practice that is different in kind from analysis.
- Tell step is often the hardest — mature believers hesitate to claim that God said something specific to them. Affirm gently. “What you heard counts even if you’re not 100% sure it was Him.”

## The ordained and the staff

- Many have done a version of this. Some have not. The challenge is distinguishing PROAPT from the study-for-Sunday habit: hearing for yourself, not preparing for others.
- Watch for the member whose Apply is always about the congregation, their kids, or their spouse. Redirect: “Apply this to YOU first. They are doing their own work.”
- Watch for the member who treats PROAPT as one more thing on the to-do list. Frame it as the most important fifteen minutes of their day, not the last.
- Tell step works powerfully told peer to peer — in the circle, in a marriage, or with a friend from the cohort.

'''
s = s[:i] + new_diff + s[j:]

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W7: {len(E)} pair edits + diff rewrite, {fail} failures')
sys.exit(1 if fail else 0)
