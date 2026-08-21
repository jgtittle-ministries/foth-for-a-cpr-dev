# GS Week 6 handout consolidation + follow-up line.
import io, sys
f = 'docs/getting-started/week-06-brave.md'
s = io.open(f, encoding='utf-8').read()
fail = 0

old = '- Any family where parent and teen confessions, considered together, suggest tender home dynamics this week.'
new = '- Any household where confessions from two members of the cohort, considered together, suggest tender home dynamics this week. The team says nothing to anyone; it prays and watches.'
if s.count(old) == 1:
    s = s.replace(old, new)
else:
    print('!! follow-up line'); fail += 1

old = '- H6.1 — The Place I Want to Walk in Greater Honesty (Junior, Senior, Parent)'
new = '- H6.1 — The Place I Want to Walk in Greater Honesty'
if s.count(old) == 1:
    s = s.replace(old, new)
else:
    print('!! handout list'); fail += 1

# drop junior + senior variants, keep the parent body as THE card
i = s.index('**Handout H6.1 — The Place (Junior, ages 12–14)**')
j = s.index('**Handout H6.1 — The Place (Parent)**')
s = s[:i] + s[j:]
old = '**Handout H6.1 — The Place (Parent)**'
new = '**Handout H6.1 — The Place**'
s = s.replace(old, new, 1)

old = '*Your kids are doing the same practice. The most generous thing you can do for them is to be honest in this room.*'
new = '*The room this cohort will one day lead is shaped by the honesty of this circle. The most generous thing you can do for the people you serve is to be honest in this room.*'
if s.count(old) == 1:
    s = s.replace(old, new)
else:
    print('!! kids-doing-same line'); fail += 1

old = '- The way I parent from my own woundedness rather than from the Father’s heart.'
new = '- The way I parent — or lead — from my own woundedness rather than from the Father’s heart.'
if s.count(old) == 1:
    s = s.replace(old, new)
else:
    print('!! parenting line'); fail += 1

old = 'an affair, an addiction, financial concealment, a pattern of harm to your kids you have not addressed. Name the place at the level you can. After the session, talk to a Companion. Pastoral 1:1 within the week. The team is ready.*'
new = 'an affair, an addiction, financial concealment, a pattern of harm you have not addressed. Name the place at the level you can. After the session, talk to a Companion. Pastoral 1:1 within the week. The team is ready.*'
if s.count(old) == 1:
    s = s.replace(old, new)
else:
    print('!! larger-surfaces line'); fail += 1

old = '*If what you are carrying is something that mandatory-reporting law obligates the team to address, the Lead Companion will tell you so directly and walk with you through the next step. The team’s job is to walk you toward freedom, not to manage your secret.*'
new = '*If what you are carrying is something the law or the host church’s safeguarding policy obligates the team to address — harm involving a minor above all — the convening leader will tell you so directly and walk with you through the next step. The team’s job is to walk you toward freedom, not to manage your secret.*'
if s.count(old) == 1:
    s = s.replace(old, new)
else:
    print('!! reporting line'); fail += 1

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W6b: done, {fail} failures')
sys.exit(1 if fail else 0)
