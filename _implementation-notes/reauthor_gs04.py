# GS Week 4 adult re-authoring: Companion-in-Formation -> the rotation's
# first member-leader; process/care division transfers whole.
import io, sys
f = 'docs/getting-started/week-04-story-2.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')
R('A third copy goes to the Companion-in-Formation with Handout H4.1. Week 4 carries the same disclosure risk as Week 3 and adds a teen leader.',
  'A third copy goes to the rotation leader with Handout H4.1. Week 4 carries the same disclosure risk as Week 3 and adds a first-time leader.')
R('And it is the first marquee slot led by a Companion-in-Formation: a senior teen leads the container open and close, the story facilitation, and the blessing round, protocol card in hand, with the adult Cohort Companion in the room.',
  'And it is the rotation’s first marquee slot: a member leads the container open and close, the story facilitation in their circle, and the blessing round, protocol card in hand, with an experienced Companion in the room.')
R('- The senior teen performing leadership instead of holding space. Watch for the voice that goes announcer-smooth, the eyes that check the adults instead of the teller. The coaching in pre-work is where this gets prevented; the debrief is where it gets named gently.',
  '- The rotation leader performing leadership instead of holding space. Watch for the voice that goes announcer-smooth, the eyes that check the veterans instead of the teller. The coaching in pre-work is where this gets prevented; the debrief is where it gets named gently.')
R('- Adults hovering so closely the senior never actually leads. If the adult Cohort Companion answers questions directed at the senior, restates the senior’s instructions, or visibly monitors, the room learns that the teen is decoration. The adult holds the disclosure-bearing center and otherwise sits on their hands.',
  '- Companions hovering so closely the rotation leader never actually leads. If the experienced Companion answers questions directed at the leader, restates the leader’s instructions, or visibly monitors, the room learns the rotation is decoration. The experienced Companion holds the disclosure-bearing center and otherwise sits on their hands.')
R('- Parents whose teen is the one leading. Pride and anxiety both distort a parent circle. Frame it in pre-work.',
  '- A spouse in the room while their husband or wife leads for the first time. Pride and anxiety both distort a circle. Frame it in pre-work.')
R('**If a heavy disclosure begins while the Companion-in-Formation is facilitating.** The senior’s only job is to catch the adult Cohort Companion’s eye and hand it over — mid-sentence is fine. The handoff is the competence, not a failure. The senior does not probe, does not comfort past a nod, does not try to land the moment themselves. They say the handoff line — *“[Adult’s name], I’d like you to take this”* — and then they keep holding the container: stay seated, stay present, keep their face soft, say nothing more. The adult takes the disclosure instantly and completely. This handoff was rehearsed in pre-work; the night of is the second time, not the first.',
  '**If a heavy disclosure begins while the rotation leader is facilitating.** The leader’s only job is to catch the experienced Companion’s eye and hand it over — mid-sentence is fine. The handoff is the competence, not a failure. The leader does not probe, does not comfort past a nod, does not try to land the moment themselves. They say the handoff line — *“[Companion’s name], I’d like you to take this”* — and then they keep holding the container: stay seated, stay present, keep their face soft, say nothing more. The experienced Companion takes the disclosure instantly and completely. This handoff was rehearsed in pre-work; the night of is the second time, not the first.')
R('**If a participant discloses suicidal ideation.** Stay in the circle. Do not move them out alone. At the end of the block, the Cohort Companion and one other Companion (two-adult rule) walk with them to a private space. The pastoral / clinical backup is called within the hour. Parents are notified per Handbook §6 protocol. The Companion-in-Formation never counts as one of the two adults.',
  '**If a participant discloses suicidal ideation.** Stay in the circle. Do not move them out alone. At the end of the block, the circle Companion and one other Companion (two adults, always) walk with them to a private space. The pastoral / clinical backup is called within the hour, and the door out is real that same night. The rotation leader never counts as one of the two — care belongs to the experienced.')
R('**If a teen discloses abuse.** Affirm them in the circle. Do not interrogate. Do not promise confidentiality. After the session, the Cohort Companion and the Lead Companion step aside with the teen. Mandatory reporting timeline begins within 24 hours per Virginia Code §63.2-1509. If the disclosure surfaced while the senior was facilitating, the senior hands it over as above and is checked on by the Lead Companion the same night — hearing an abuse disclosure is heavy for a seventeen-year-old, even one who did everything right.',
  '**If a member discloses abuse — their own history, or harm involving a minor.** Affirm them in the circle. Do not interrogate. Do not promise confidentiality you cannot keep: a disclosure involving a minor may carry mandatory-reporting duties, and the host church’s policy and counsel govern the timeline. After the session, the circle Companion and the convening leader step aside with the member. If the disclosure surfaced while the rotation leader was facilitating, they hand it over as above and are checked on by the convening leader the same night — hearing an abuse disclosure is heavy for a first-time leader, even one who did everything right.')
R('**If a participant breaks down.** The circle holds the silence. The adult Cohort Companion reaches out a hand or sits closer if welcomed. The senior does not manage the moment; the adult does. After the breakdown passes, the adult quietly checks in within ten minutes.',
  '**If a participant breaks down.** The circle holds the silence. The experienced Companion reaches out a hand or sits closer if welcomed. The rotation leader does not manage the moment; the experienced Companion does. After the breakdown passes, the Companion quietly checks in within ten minutes.')
R('**If something heavy surfaces that is not crisis.** Receive the story. Bless the teller. The Lead Companion follows up within 48 hours offline. The senior does not carry the follow-up.',
  '**If something heavy surfaces that is not crisis.** Receive the story. Bless the teller. The convening leader follows up within 48 hours offline. The rotation leader does not carry the follow-up.')
R('**If you, the Companion, are not okay.** Tap the Co-Companion. Step out. The team is built so this is possible. The same is true for the Companion-in-Formation: if the senior is unsteady, the adult takes the block without ceremony, and nothing is lost. The Lab has more slots; the series has more runnings.',
  '**If you, the Companion, are not okay.** Tap the Co-Companion. Step out. The team is built so this is possible. The same is true for the rotation leader: if they are unsteady, the experienced Companion takes the block without ceremony, and nothing is lost. The rotation has more slots; the series has more runnings.')
R('nobody leaves activated — a Companion stays until their body has settled, and settling that doesn’t come is a same-evening call to the backup. The adult runs the Settle Protocol, never the senior.',
  'nobody leaves activated — a Companion stays until their body has settled, and settling that doesn’t come is a same-evening call to the backup. The experienced Companion runs the Settle Protocol, never the rotation leader.')
R('Week 4 is also the first marquee slot of the Companion-in-Formation track. A willing senior teen — one who told their own story in Week 3, who has walked the protocol in the Leader Lab, and whose parent and the Lead Companion both agreed is ready — leads the container open and close, the story facilitation in their circle, and the blessing round. Protocol card in hand. Adult in the room. This is the second-running mechanism from Handbook Section 11.3: see one, do one, in the same series, in front of the cohort.',
  'Week 4 is also the rotation’s first marquee slot. A willing member — one who told their own story in Week 3, who has walked the protocol with the convening leader, and who discerned with them that they are ready — leads the container open and close, the story facilitation in their circle, and the blessing round. Protocol card in hand. An experienced Companion in the room. This is the second-running mechanism: see one, do one, in the same series, in front of the cohort.')
R('The bright line from Section 11.2 governs everything in this plan. The senior leads process — the scripted, repeatable shape. The adult holds care — the moment when someone’s interior life opens. The rest of this document is largely the working-out of that one sentence.',
  'One bright line governs everything in this plan. The rotation leader leads process — the scripted, repeatable shape. The experienced Companion holds care — the moment when someone’s interior life opens. The rest of this document is largely the working-out of that one sentence.')
R('- The FC1 consent and legal gate (Handbook 11.9) has cleared. If it has not, the adult Companions lead this session exactly as they led Week 3, this plan still runs, and the teen-led elements wait for the next cycle.',
  '- A member has discerned ready for the rotation. If none has, the Companions lead this session exactly as they led Week 3, this plan still runs, and the member-led elements wait for the next running — a role discerned, never required.')
R('- Each family attempted the Joint Footprints exercise. Some did, some did not. Both are data, not grades.',
  '- Each member attempted the Shared Footprints exercise. Some did, some did not. Both are data, not grades.')
R('Same as Week 3: Self leads, Others arrives. The one addition is quiet but real — the cohort watching a peer hold the room is itself a formation experience. The younger teens are learning what they might one day be asked to become.',
  'Same as Week 3: Self leads, Others arrives. The one addition is quiet but real — the cohort watching one of its own hold the room is itself a formation experience. Every member is learning what they may one day be asked to become.')
R('This is the heart of pre-work this week. Sometime in the week before the session — not the night of — the adult Cohort Companion and the senior meet for about an hour:',
  'This is the heart of pre-work this week. Sometime in the week before the session — not the night of — the experienced Companion and the rotation leader meet for about an hour:')
R('1. **The senior walks the protocol aloud. Twice.**', '1. **The leader walks the protocol aloud. Twice.**')
R('2. **Rehearse the disclosure handoff. Once, explicitly.** The adult plays a teller whose story turns heavy mid-sentence. The senior practices the whole move: catch the adult’s eye, say the line — *“[Name], I’d like you to take this”* — and then hold the container in silence while the adult takes over.',
  '2. **Rehearse the disclosure handoff. Once, explicitly.** The Companion plays a teller whose story turns heavy mid-sentence. The leader practices the whole move: catch the Companion’s eye, say the line — *“[Name], I’d like you to take this”* — and then hold the container in silence while the Companion takes over.')
R('3. **Walk the three rules that never bend** (Handbook 11.6): you never count as one of the two adults; you never take a disclosure — you hand it to the adult immediately; you lead only a block you have first received. The senior says them back in their own words.',
  '3. **Walk the three rules that never bend**: you never count as one of the two Companions for a disclosure; you never take a disclosure — you hand it to the experienced Companion immediately; you lead only a block you have first received. The leader says them back in their own words.')
R('4. **Preview the Leader Feedback Round** (Handbook 11.7) so nothing about it surprises them: affirmation first, one growth item, and the group speaks only if the senior consents. The senior can decide in advance, or in the moment. Either is honored.',
  '4. **Preview the Leader Feedback Round** so nothing about it surprises them: affirmation first, one growth item, and the group speaks only if the leader consents. They can decide in advance, or in the moment. Either is honored.')
R('3. Walk the teen-leader handoff scenario aloud, in addition to the four crisis scenarios. The adult Cohort Companion for the senior’s circle says exactly what they will do when the handoff comes.',
  '3. Walk the leader-handoff scenario aloud, in addition to the four crisis scenarios. The experienced Companion for the leader’s circle says exactly what they will do when the handoff comes.')
R('2. Confirm which blocks the Companion-in-Formation leads. If more than one senior is in formation, you may spread the parts — one takes the shared open and close, another facilitates the senior circle — but each block has exactly one leader. Do not co-lead a block between two seniors; that is performing, not holding.',
  '2. Confirm which blocks the rotation leader leads. If more than one member is in the rotation this cycle, you may spread the parts — one takes the shared open and close, another facilitates a circle — but each block has exactly one leader. Do not co-lead a block between two; that is performing, not holding.')
R('3. Reprint the H3.x handouts as needed for this week’s tellers — the storytelling cards (junior / senior / parent), the listener’s role card, and the Joint Footprints handout for the families whose teller told this week.',
  '3. Reprint the H3.x handouts as needed for this week’s tellers — the storytelling card, the listener’s role card, and the Shared Footprints handout for the members who tell this week.')
R('4. Print Handout H4.1 — the Facilitation Card — on cardstock. One for the senior, one spare for the adult Cohort Companion.',
  '4. Print Handout H4.1 — the Facilitation Card — on cardstock. One for the rotation leader, one spare for the experienced Companion.')
R('- Joint Footprints handout H3.5 — one per family whose teller tells this week.',
  '- Shared Footprints handout H3.3 — one per member who tells this week.')
R('- Handout H4.1 — the Companion-in-Formation’s Facilitation Card. On cardstock. In the senior’s hand, not memorized-and-left-home. The card in hand is part of the design: it tells the room the senior is following a form, not improvising with their friends’ stories.',
  '- Handout H4.1 — the Rotation Leader’s Facilitation Card. On cardstock. In the leader’s hand, not memorized-and-left-home. The card in hand is part of the design: it tells the room the leader is following a form, not improvising with the room’s stories.')
R('Identical to Week 3. Open in the main room as a single circle; split to the same cohort spaces; merge to close. In the senior circle, the Companion-in-Formation sits in the circle exactly where the Cohort Companion sat in Week 3 — in it, not at the head — and the adult Cohort Companion sits directly across, where eye contact is one glance, not a search. That geometry is the handoff line.',
  'Identical to Week 3. Open in the main room as a single circle; split to the same circle spaces; merge to close. In the leader’s circle, the rotation leader sits exactly where the Companion sat in Week 3 — in it, not at the head — and the experienced Companion sits directly across, where eye contact is one glance, not a search. That geometry is the handoff line.')
R('| Week before | Coaching session with the Companion-in-Formation: protocol aloud twice, handoff rehearsed once. Confirm teller lists. Print H4.1 and reprint H3.x. | Cohort Comp + senior; Lead Comp |',
  '| Week before | Coaching session with the rotation leader: protocol aloud twice, handoff rehearsed once. Confirm teller lists. Print H4.1 and reprint H3.x. | Companion + leader; Lead Comp |')
R('| Day before | Walk every space. Phone the pastoral / clinical backup. Brief check-in text or call to the senior: “You’re ready. See you tomorrow.” | Lead Companion + Co-Comp |',
  '| Day before | Walk every space. Phone the pastoral / clinical backup. Brief check-in text or call to the rotation leader: “You’re ready. See you tomorrow.” | Lead Companion + Co-Comp |')
R('| T-90 min | Companion team meets in the main room. Re-read crisis scenarios aloud, including the handoff scenario. Pray for each participant and for the senior by name. | All Companions |',
  '| T-90 min | Companion team meets in the main room. Re-read crisis scenarios aloud, including the handoff scenario. Pray for each participant and for the rotation leader by name. | All Companions |')
R('| T-30 min | Each Cohort Companion sets up their cohort space. The senior sets up their own circle’s space alongside the adult — setting the chairs is part of leading. | All Companions + senior |',
  '| T-30 min | Each Companion sets up their circle space. The rotation leader sets up their own circle’s space alongside the Companion — setting the chairs is part of leading. | All Companions + leader |')
R('| T-15 min | Door opens. Same arrival rhythm as Weeks 1–3. | Co-Comp (Teen) |',
  '| T-15 min | Door opens. Same arrival rhythm as Weeks 1–3. | Co-Comp |')
R('| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp (Teen) | Door, name tags, phone-box. Lead Companion greets each participant by name. |',
  '| 6:45–7:00 | Arrival window | Single circle (forming) | Co-Comp | Door, name tags, phone-box. The convening leader greets each participant by name. |')
R('| 7:00–7:08 | Block 1: Welcome and centering | Shared circle | Comp-in-Formation | The senior opens the container: Aaronic blessing, container restated, Week 4 framed. First teen-led block of the series. |',
  '| 7:00–7:08 | Block 1: Welcome and centering | Shared circle | Rotation leader | The rotation leader opens the container: Aaronic blessing, container restated, Week 4 framed. First member-led block of the series. |')
R('| 7:22–7:25 | Block 4: Bridge to the split | Shared circle | Comp-in-Formation | Cards held up, three reminders, prayer, split. Same bridge as Week 3, spoken by the senior. |',
  '| 7:22–7:25 | Block 4: Bridge to the split | Shared circle | Rotation leader | Cards held up, three reminders, prayer, split. Same bridge as Week 3, spoken by the leader. |')
R('| 7:25–8:02 | Block 5: Stories in circles | Cohort circles | Comp-in-Formation (senior circle); Cohort Comps (junior, parent) | The remaining tellers tell. Same turn structure as Week 3. In the senior circle the teen facilitates, card in hand; the adult Cohort Companion sits across, holding the disclosure-bearing center. |',
  '| 7:25–8:02 | Block 5: Stories in circles | Circles | Rotation leader (their circle); Companions (the others) | The remaining tellers tell. Same turn structure as Week 3. In the leader’s circle the member facilitates, card in hand; the experienced Companion sits across, holding the disclosure-bearing center. |')
R('| 8:18–8:23 | Block 8: Between-session practice | Shared circle | Co-Comp (Parent) | Joint Footprints assigned to this week’s tellers’ families. Morning question and journal continue for all. |',
  '| 8:18–8:23 | Block 8: Between-session practice | Shared circle | Co-Comp | Shared Footprints assigned to this week’s tellers. Morning question and journal continue for all. |')
R('| 8:23–8:30 | Block 9: Closing container | Shared circle | Comp-in-Formation | The senior closes: confidentiality restated, help named, Aaronic blessing. |',
  '| 8:23–8:30 | Block 9: Closing container | Shared circle | Rotation leader | The leader closes: confidentiality restated, help named, Aaronic blessing. |')
R('| 8:30+ | After | Floating | Lead Companion + cohort comps | Stay accessible for ten minutes. The Lead Companion finds the senior for a private word before they leave. |',
  '| 8:30+ | After | Floating | Lead Companion + Companions | Stay accessible for ten minutes. The convening leader finds the rotation leader for a private word before they leave. |')
R('The Companion-in-Formation opens the night. The script below is on their Facilitation Card (H4.1); they may say it in their own words, but the pieces — blessing, container, frame — are all required. The Lead Companion sits in the circle as a participant and does not hover.',
  'The rotation leader opens the night. The script below is on their Facilitation Card (H4.1); they may say it in their own words, but the pieces — blessing, container, frame — are all required. The convening leader sits in the circle as a participant and does not hover.')
R('## Script (Companion-in-Formation)\n\n*“Welcome back. Phones in the box, please. Find a seat. We’ll start in ninety seconds.”*',
  '## Script (rotation leader)\n\n*“Welcome back. Phones in the box, please. Find a seat. We’ll start in ninety seconds.”*')
R('*Note to the adult team: the room will register that a teen is leading within the first ten seconds. Let it. Do not introduce the senior, do not explain the arrangement, do not applaud. The most honoring thing the adults can do is receive the opening exactly as they received it from the Lead Companion in Weeks 1–3.*',
  '*Note to the Companion team: the room will register that one of its own is leading within the first ten seconds. Let it. Do not introduce the leader, do not explain the arrangement, do not applaud. The most honoring thing the team can do is receive the opening exactly as it received it from the convening leader in Weeks 1–3.*')
R('## Block 2 — Joint Footprints Check-in (7:08–7:16, 8 min)\nThe Lead Companion takes this block. Brief and low-stakes, same rhythm as prior weeks.',
  '## Block 2 — Shared Footprints Check-in (7:08–7:16, 8 min)\nThe convening leader takes this block. Brief and low-stakes, same rhythm as prior weeks.')
R('*“Last week each family took home the Joint Footprints exercise. Some of you got to it. Some of you didn’t. Both are fine — ‘we didn’t get to it’ is honest, and honest is what we do here. Anyone want to offer one sentence about what it was like? Not what was said — that’s yours — just what it was like. Optional.”*',
  '*“Last week each of you took home the Shared Footprints exercise. Some of you got to it. Some of you didn’t. Both are fine — ‘we didn’t get to it’ is honest, and honest is what we do here. Anyone want to offer one sentence about what it was like? Not what was said — that’s yours — just what it was like. Optional.”*')
R('The Companion-in-Formation takes the bridge — the same three reminders and prayer the Lead Companion spoke in Week 3, from the Facilitation Card.\n\n## Script (Companion-in-Formation)',
  'The rotation leader takes the bridge — the same three reminders and prayer the convening leader spoke in Week 3, from the Facilitation Card.\n\n## Script (rotation leader)')
R('The heart of the night. The junior and parent circles run exactly as they did in Week 3, adult-led. The senior circle is where the new thing happens: the Companion-in-Formation facilitates, and the adult Cohort Companion holds the center.',
  'The heart of the night. The other circles run exactly as they did in Week 3, Companion-led. The leader’s circle is where the new thing happens: the rotation leader facilitates, and the experienced Companion holds the center.')
R('### Inside the senior circle — how the two roles divide',
  '### Inside the leader’s circle — how the two roles divide')
R('**The senior leads the process.** They open the circle (script below), invite each teller in turn, watch the timer, hold the ten seconds of silence, open and steer each blessing round, and close the circle. Card in hand throughout. This is process leadership — the scripted, repeatable shape — and it is fully theirs.',
  '**The rotation leader leads the process.** They open the circle (script below), invite each teller in turn, watch the timer, hold the ten seconds of silence, open and steer each blessing round, and close the circle. Card in hand throughout. This is process leadership — the scripted, repeatable shape — and it is fully theirs.')
R('**The adult holds the care.** The adult Cohort Companion sits directly across from the senior, in the circle, silent through the mechanics. The adult does not restate the senior’s instructions, does not answer questions aimed at the senior, does not visibly monitor. The adult is there for exactly one thing: the moment someone’s interior life opens past what a peer should hold. When that moment comes, the adult takes it — instantly and completely.',
  '**The experienced Companion holds the care.** They sit directly across from the leader, in the circle, silent through the mechanics. They do not restate the leader’s instructions, do not answer questions aimed at the leader, do not visibly monitor. They are there for exactly one thing: the moment someone’s interior life opens past what a first-time leader should hold. When that moment comes, they take it — instantly and completely.')
R('*(Note: the senior does not tell a story tonight — they told in Week 3. Tonight they hold the room the way it was held for them.)*',
  '*(Note: the rotation leader does not tell a story tonight — they told in Week 3. Tonight they hold the room the way it was held for them.)*')
R('*The senior catches the adult’s eye and says: “[Adult’s name], I’d like you to take this.”*',
  '*The leader catches the Companion’s eye and says: “[Name], I’d like you to take this.”*')
R('That is the whole move. Then the senior stays seated, stays present, keeps their face soft, and says nothing more. The adult receives the teller from that word forward — affirms, does not interrogate, does not promise confidentiality, and carries the Section 6 protocol from there. When the moment has been held and the circle is steady again, the adult hands the process back just as simply: *“[Senior’s name], take us on.”* The circle continues. Rehearsed once in pre-work; the room will follow the calm of the two people who knew this could happen.',
  'That is the whole move. Then the leader stays seated, stays present, keeps their face soft, and says nothing more. The Companion receives the teller from that word forward — affirms, does not interrogate, does not promise confidentiality lightly, and carries the safeguarding frame from there. When the moment has been held and the circle is steady again, the Companion hands the process back just as simply: *“[Leader’s name], take us on.”* The circle continues. Rehearsed once in pre-work; the room will follow the calm of the two people who knew this could happen.')
R('### When the senior should intervene (process) and when the adult does (care)',
  '### When the leader intervenes (process) and when the Companion does (care)')
R('- Teller shaming themselves — senior, quietly: “Your story is not in competition with anyone’s. Tell us yours.”',
  '- Teller shaming themselves — leader, quietly: “Your story is not in competition with anyone’s. Tell us yours.”')
R('- Listener fixing or relating back — senior: “Let’s come back to blessing. Right now we’re receiving.”',
  '- Listener fixing or relating back — leader: “Let’s come back to blessing. Right now we’re receiving.”')
R('- Teller freezes — senior: “We’ll wait. Take your time.” Fifteen seconds. Then: “Would you like to come back at the end? You can pass.”',
  '- Teller freezes — leader: “We’ll wait. Take your time.” Fifteen seconds. Then: “Would you like to come back at the end? You can pass.”')
R('- Anything heavy — adult, via the handoff above. The senior does not attempt even the gentle crisis-adjacent moves from Week 3’s plan; those belong to the adult tonight.',
  '- Anything heavy — the Companion, via the handoff above. The rotation leader does not attempt even the gentle crisis-adjacent moves from Week 3’s plan; those belong to the experienced tonight.')
R('- Running out of time — senior compresses the blessing rounds to one sentence each and gets every teller told. Better three minutes late than a participant sent home untold — that rule has not changed.',
  '- Running out of time — the leader compresses the blessing rounds to one sentence each and gets every teller told. Better three minutes late than a participant sent home untold — that rule has not changed.')
R('### Junior and parent circles', '### The other circles')
R('Runs right after the senior has led, while the cohort is present — that timing is the design (Handbook 11.7). The Lead Companion facilitates. The order is fixed: affirmation first, growth second, the group only by the senior’s consent.',
  'Runs right after the rotation leader has led, while the cohort is present — that timing is the design. The convening leader facilitates. The order is fixed: affirmation first, growth second, the group only by the leader’s consent.')
R('*“One more thing tonight, and it’s a good one. [Senior’s name] led for the first time tonight — the opening, a story circle, the close. When one of us leads, we give them a short feedback round. Here’s how it works, and the order matters.”*',
  '*“One more thing tonight, and it’s a good one. [Name] led for the first time tonight — the opening, a story circle, the close. When one of us leads, we give them a short feedback round. Here’s how it works, and the order matters.”*')
R('The parent Co-Companion takes this block, same as Week 3.', 'A Co-Companion takes this block, same as Week 3.')
R('''*“One practice between now and next Tuesday, and it belongs to the families whose teller told tonight. It’s the same Joint Footprints exercise last week’s families did.” (Hold up H3.5.)*

*“Parent and teen, twenty minutes, sometime this week. Not in the car, not in front of a screen. One of you walks the other through the footprints question — five minutes telling, a follow-up question or two, and one sentence: ‘What I love about your footprints is...’ Then swap. The handout has the questions and the rules.”*

*“Same two rules as last week. The teen doesn’t have to disclose anything they didn’t disclose tonight. The parent doesn’t turn it into a lecture. We’re practicing what we did tonight, at home.”*

*“Families who did it last week — you’re done; don’t force a repeat. Everyone keeps the morning question and the evening journal note going. Five minutes in the morning, two at night. That rhythm is quietly doing more than any single Tuesday.”*''',
  '''*“One practice between now and next week, and it belongs to those who told tonight. It’s the same Shared Footprints exercise last week’s tellers did.” (Hold up H3.3.)*

*“You and your spouse, or one person close to you. Twenty minutes, sometime this week. Not in the car, not in front of a screen. One of you walks the other through the footprints question — five minutes telling, a follow-up question or two, and one sentence: ‘What I love about your footprints is...’ Then swap. The handout has the questions and the rules.”*

*“Same two rules as last week. Nobody has to disclose anything they didn’t disclose tonight. And neither of you turns it into advice. We’re practicing what we did tonight, at home.”*

*“Those who did it last week — you’re done; don’t force a repeat. Everyone keeps the morning question and the evening journal note going. Five minutes in the morning, two at night. That rhythm is quietly doing more than any single week.”*''')
R('The Companion-in-Formation closes the night, from the Facilitation Card.\n\n## Script (Companion-in-Formation)',
  'The rotation leader closes the night, from the Facilitation Card.\n\n## Script (rotation leader)')
R('*After the blessing, the adults do not pack up immediately — stay accessible for ten minutes, same as always. The Lead Companion finds the senior privately before they leave: one sentence of thanks, one question — “How are you, after that?” — and a listen. Not more coaching. The coaching waits for the debrief and the Lab.*',
  '*After the blessing, the team does not pack up immediately — stay accessible for ten minutes, same as always. The convening leader finds the rotation leader privately before they leave: one sentence of thanks, one question — “How are you, after that?” — and a listen. Not more coaching. The coaching waits for the debrief.*')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}')
        fail += 1
        continue
    s = s.replace(old, new)

# Differentiation section rewrite
i = s.index('# Differentiation by Cohort')
j = s.index('# Closing Practice in Detail')
new_diff = '''# Differentiation in the Circles

## The other circles

Companion-led, same as Week 3. This week’s remaining tellers tell, with the same card and the same turns.

- Everything in the Week 3 notes applies unchanged — help with prompts, affirm specificity over polish, redirect the story told about someone else, never pressure the silent one.
- Watch for the teller who spent the week rehearsing. A prepared story is still their story; receive it. But if it sounds like a recital, one warm question opens the door: “What’s the part you didn’t put in?” Ask it once, gently, and accept whatever comes.
- The room will have noticed that one of its own is leading tonight. Some will ask about it. The honest answer is the good one: “That’s something any of us can grow into here. Maybe you, next running.” Plant it and move on.

## The leader’s circle

The leader’s circle carries both halves of tonight’s design: its tellers tell, and one of their own facilitates.

- The peer-facilitation dynamic cuts both ways. Some tellers will find it easier to be honest in front of a peer than in front of the “official” Companion; some will find it harder — the facilitator sits beside them on Sunday mornings. The pre-work teller list should flag anyone for whom the peer dynamic is likely to close them down; if the concern is serious, the experienced Companion and the leader can agree in advance that the Companion takes that teller’s turn.
- Watch for the circle testing the leader — the joke at the wrong moment, the sideways look. The leader handles the first instance themselves (“Let’s stay with [teller]”); if it continues, the experienced Companion ends it with one sentence. Order is care, not just process, once it frays.
- Watch for the leader performing. The tell is attention drifting from the teller to the room. This is debrief material, not night-of correction, unless the circle is actually losing safety — in which case the Companion quietly takes the process back and the two of them talk tomorrow.

## The spouse in the room

- If the rotation leader’s husband or wife is in the cohort, they are in one of tonight’s circles with their attention half down the hall. Name it warmly at that circle’s open: “[Name] is leading the other circle tonight. We’ll trust the team with that room so you can be in this one.” Pride and anxiety both distort; naming it releases most of it.
- Second-running tellers watched others go first and have had days to edit themselves. Watch for the over-polished story, and use the Week 3 move: “What did that cost you, specifically?”

'''
s = s[:i] + new_diff + s[j:]

more = [
('Handbook 11.7, run exactly as scripted in Block 7. The order is the safety: affirmation first, one growth item, group only by consent, popcorn only, “for you” language only. This round is also formation for the whole cohort — they are watching what it looks like to receive feedback without inflating or collapsing.',
 'Run exactly as scripted in Block 7. The order is the safety: affirmation first, one growth item, group only by consent, popcorn only, “for you” language only. This round is also formation for the whole cohort — they are watching what it looks like to receive feedback without inflating or collapsing.'),
('Confidentiality restated explicitly, by the senior. The container is not a slogan; it is a discipline, and hearing a peer hold the discipline teaches the teens it belongs to all of them, not just to the adults.',
 'Confidentiality restated explicitly, by the rotation leader. The container is not a slogan; it is a discipline, and hearing a peer hold the discipline teaches the room it belongs to all of them, not only to the convening leader.'),
('Spoken by the Companion-in-Formation tonight. The words are the same words; the voice is younger. Some in the room will receive it differently for that reason — a blessing handed down a generation, already. Notice it. Do not comment on it.',
 'Spoken by the rotation leader tonight. The words are the same words; the voice is a peer’s. Some in the room will receive it differently for that reason — the blessing already passing into the body. Notice it. Do not comment on it.'),
('- The Joint Footprints exercise (20 min, once this week, parent-and-teen pair) — for the families whose teller told THIS week. See Handout H3.5. Families who did it after Week 3 are done; do not assign a repeat.',
 '- The Shared Footprints exercise (20 min, once this week, with a spouse or one close person) — for the members who told THIS week. See Handout H3.3. Those who did it after Week 3 are done; do not assign a repeat.'),
('If a family reports back that they did not get to the Joint Footprints, this is data, not failure — same as last week. Note it for the team debrief and do not shame in Week 5.',
 'If a member reports back that they did not get to the Shared Footprints, this is data, not failure — same as last week. Note it for the team debrief and do not shame in Week 5.'),
('Companion team meets the day after Week 4 for a 45-minute debrief. The Companion-in-Formation is not at this debrief — their feedback already happened in the room, and the team needs to talk freely. What the team decides to coach flows to the senior through the adult Cohort Companion and Lab 3.',
 'Companion team meets the day after Week 4 for a 45-minute debrief. The rotation leader is not at this debrief — their feedback already happened in the room, and the team needs to talk freely. What the team decides to coach flows to them through the experienced Companion who sat across from them.'),
('- The senior led actual blocks — the adults did not quietly re-lead around them.',
 '- The rotation leader led actual blocks — the Companions did not quietly re-lead around them.'),
('- If a handoff happened: it was clean, the adult took it completely, and the circle recovered. A clean handoff is a sign the session worked, full stop.',
 '- If a handoff happened: it was clean, the Companion took it completely, and the circle recovered. A clean handoff is a sign the session worked, full stop.'),
('- The adults hovered. If the Cohort Companion answered questions aimed at the senior or restated their instructions, the room learned the teen was decoration. Own it as an adult failure, not a teen one.',
 '- The Companions hovered. If the experienced Companion answered questions aimed at the leader or restated their instructions, the room learned the rotation was decoration. Own it as a team failure, not the leader’s.'),
('- The senior performed — attention on the room instead of the teller. Coachable, common, and worth naming precisely.',
 '- The leader performed — attention on the room instead of the teller. Coachable, common, and worth naming precisely.'),
('- A circle ran out of time and someone did not tell. Same as Week 3: the most painful failure mode, and the team owns it. Reach out within 24 hours; offer a 1:1 with the Cohort Companion this week.',
 '- A circle ran out of time and someone did not tell. Same as Week 3: the most painful failure mode, and the team owns it. Reach out within 24 hours; offer a 1:1 with the circle Companion this week.'),
('### The Companion-in-Formation — coaching for Week 8',
 '### The rotation leader — coaching for the next running'),
('- How did the senior’s leadership land — with the tellers, with the circle, with the parents down the hall? Not “did they execute the protocol” — did the people in their circle feel held?',
 '- How did the leader’s leadership land — with the tellers, with the circle, with the whole room? Not “did they execute the protocol” — did the people in their circle feel held?'),
('- What does the team coach before their next slot, PROAPT II in Week 8? Pick one thing — the same discipline the Feedback Round imposes on the room applies to the team. Route it through the adult Cohort Companion and Lab 3, not as a pile-on. And name what the senior should keep doing, first, in writing, so the affirmation travels with the growth item.',
 '- What does the team coach before their next slot, or before the next member’s first? Pick one thing — the same discipline the Feedback Round imposes on the room applies to the team. Route it through the experienced Companion, not as a pile-on. And name what the leader should keep doing, first, in writing, so the affirmation travels with the growth item.'),
('- Anyone who disclosed crisis-level material — within 24 hours per Section 6 protocol.',
 '- Anyone who disclosed crisis-level material — within 24 hours per the safeguarding frame.'),
('- Any teller whose story surfaced something a parent or teen may be processing at home. Do not break confidentiality across the cohort line; the team can pray and watch.',
 '- Any teller whose story surfaced something a spouse or close colleague in the cohort may be processing this week. Do not break confidentiality across circle lines; the team can pray and watch.'),
('- Anyone who passed or stayed nearly silent in their circle. Brief, warm, no-pressure check-in: “How did Tuesday land for you?”',
 '- Anyone who passed or stayed nearly silent in their circle. Brief, warm, no-pressure check-in: “How did it land for you?”'),
('- The Companion-in-Formation — a second touch later in the week, from the adult Cohort Companion. Leading for the first time echoes for days; make sure the echo is company, not just adrenaline.',
 '- The rotation leader — a second touch later in the week, from the experienced Companion. Leading for the first time echoes for days; make sure the echo is company, not just adrenaline.'),
('Pray by name for each participant. The team now carries the texture of every story in the cohort — the whole round, both runnings. Carry it forward in prayer for the rest of Getting Started. And pray for the senior by name: that the taste of holding a room for others would form a shepherd, not a performer.',
 'Pray by name for each participant. The team now carries the texture of every story in the cohort — the whole round, both runnings. Carry it forward in prayer for the rest of Getting Started. And pray for the rotation leader by name: that the taste of holding a room for others would form a shepherd, not a performer.'),
('- H4.1 — Companion-in-Formation Facilitation Card (Week 4)',
 '- H4.1 — Rotation Leader’s Facilitation Card (Week 4)'),
('- Reprints as needed for this week’s tellers: H3.1 / H3.2 / H3.3 (storytelling cards), H3.4 (listener’s role card), H3.5 (Joint Footprints — one per family whose teller told this week).',
 '- Reprints as needed for this week’s tellers: H3.1 (storytelling card), H3.2 (listener’s role card), H3.3 (Shared Footprints — one per member who told this week).'),
('**Handout H4.1 — Companion-in-Formation Facilitation Card (Week 4)**',
 '**Handout H4.1 — Rotation Leader’s Facilitation Card (Week 4)**'),
('*Print on cardstock. This card stays in your hand all night. It is not a crutch; it is the form. The room trusts a leader who follows a form more than one who improvises with their friends’ stories.*',
 '*Print on cardstock. This card stays in your hand all night. It is not a crutch; it is the form. The room trusts a leader who follows a form more than one who improvises with the room’s stories.*'),
]
for old, new in more:
    n = s.count(old)
    if n != 1:
        print(f'!! (more) count={n}: {old[:60]}')
        fail += 1
        continue
    s = s.replace(old, new)

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W4: {len(E) + len(more)} pair edits + 1 section rewrite, {fail} failures')
sys.exit(1 if fail else 0)
