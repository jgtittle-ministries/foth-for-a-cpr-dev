# GS Week 13 cleanup: diff rewrite + remaining role words.
import io, sys, re
f = 'docs/getting-started/week-13-rhythm.md'
s = io.open(f, encoding='utf-8').read()
fail = 0

G = [
 ('The rotation leader hands it to the adult instantly', 'The rotation leader hands it to the Companion instantly'),
 ('Question two — Which of the four kinds of dry have I been in, and when? Every adult on this team has walked',
  'Question two — Which of the four kinds of dry have I been in, and when? Everyone on this team has walked'),
 ('honor it briefly and hand it to the adult after the close', 'honor it briefly and hand it to the Companion after the close'),
 ('2. The adult Companion moves quietly to sit beside the person. No announcement, no spotlight.',
  '2. The experienced Companion moves quietly to sit beside the person. No announcement, no spotlight.'),
 ('Same as every week — and the senior speaks it tonight. In Week 15 they will speak it as a commissioned FC',
  'Same as every week — and the rotation leader speaks it tonight. In Week 15 they will speak it as one of the commissioned'),
 ('- The senior taught rather than performed — the room looked at the cards, not at the leader. That is what',
  '- The leader taught rather than performed — the room looked at the cards, not at the leader. That is what'),
 ('- The senior read the scripts flat, or performed them big. Either way, the feedback round should have cau',
  '- The leader read the scripts flat, or performed them big. Either way, the feedback round should have cau'),
 ('- **The readiness confirmation.** The parent + Lead Companion sign-off conversation for each rotation lea',
  '- **The readiness confirmation.** The covering + convening leader discernment conversation about the coho'),
]
for old, new in G:
    m = re.search(re.escape(old) + r'[^\n]*', s)
    if not m:
        print(f'!! not found: {old[:55]}'); fail += 1; continue
    line = m.group(0)
    tail = line[len(old):]
    s = s.replace(line, new + tail, 1)

# fix truncation-completed replacements that may have broken words: re-run precise
s = s.replace('hands it to the adult instantly', 'hands it to the Companion instantly')

i = s.index('## **Junior teens (12–14)**')
j = s.index('# **Closing') if '# **Closing' in s else s.index('# Closing')
new_diff = '''## Those doing this work for the first time

- The build: coach toward the starter plan's floor — the morning question and the evening note, six minutes total. A member with two honest daily practices and a named weekly person has a complete Rhythm Card. Resist the urge to make anyone's card fuller than their life can hold.
- Watch for the member who hears the dry-season teaching and worries retroactively — "was that gray stretch the bad kind?" Reassure simply: the ache question, and the reminder that worrying about it is itself the good sign.

## The veterans

For veterans this session is live equipment, not seeds. Some are in a dry season now; all of them will hold this card set for someone else within the year.

- Signs Card: this lands hardest and matters most here. A member who can hold the sorting question is carrying real pastoral equipment — and misreading a dry season is the first hazard of shepherding.
- Watch for the member who intellectualizes the four columns — sorting hypothetical people instead of sitting in their own. Redirect: "Your column first."
- Watch for the member for whom the desire question lands with a thud — the one who is honestly not sure they still ache for God. Receive without alarm; that honesty is the beginning of the way back, and the card says so.
- Path Home Card: veterans know people who have already left — a grown child, an old friend, half a former congregation. Expect the quiet weight of names.

## The ordained and the staff

Many of the ordained are in, or freshly out of, a dry season — and most have never had language for it, having spent it producing sermons about abundance.

- The build: the temptation is the over-built card (guilt inflates ambition) or the deferred card ("after this season"). Both are answered the same way: the floor is enough, and it starts this week.
- Signs Card: expect recognition — a leader realizing that a gray stretch of years finally has a name and was not disqualification.
- Watch for the member who reaches for the card as a diagnostic for the congregation. Rule 1, warmly but firmly: your own heart first, and one trusted person to help you read it.
- Path Home Card: some carry old departures — their own, or a grown child's. The card's word to Companions stands: the path home is real, and nobody walks it under diagnosis.
- The gap: for some households the holidays are the dry season — grief anniversaries, hard relatives, empty chairs. If the calendar puts a break here, name it warmly from the front.

'''
s = s[:i] + new_diff + s[j:]

io.open(f, 'w', encoding='utf-8').write(s)
hits = re.findall(r'\b(teens?|parents?|juniors?|seniors?|adults?|CCA)\b', s, re.I)
print('W13b failures:', fail, '| remaining role words:', hits)
for m in re.finditer(r'^.*\b(teens?|parents?|seniors?|adults?|CCA)\b.*$', s, re.M | re.I):
    if 'Adult edition' in m.group(0): continue
    print('  LINE:', m.group(0)[:110])
sys.exit(1 if fail else 0)
