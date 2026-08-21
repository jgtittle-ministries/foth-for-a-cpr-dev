# Build the what-held rounds into the four re-entry sessions.
# Every replacement must hit exactly once; misses are reported loudly.
import io, sys

FILES = {
 'gs6':  'docs/getting-started/week-06-brave.md',
 'gs11': 'docs/getting-started/week-11-doubts.md',
 'gd7':  'docs/going-deeper/week-07-corporate-listening.md',
 'go9':  'docs/going-out/week-09-body-sent-beyond.md',
}
R = {k: [] for k in FILES}

def rep(k, old, new): R[k].append((old, new))

EM = '—'; EN = '–'; LQ = '“'; RQ = '”'; AP = '’'

# ================= GS WEEK 6 =================
rep('gs6', '**Mode.** Shared opening and teaching; SPLIT into cohort circles for the practice; MERGE for blessings and closing.',
 '**Mode.** Shared opening and teaching; SPLIT into cohort circles for the practice; MERGE for blessings and closing.\n\n**Re-entry.** This session follows the first two-week practice hold; Block 2 is the what-held round.')
# run sheet
rep('gs6', '| 7:00–7:08 | Block 1:', '| 7:00–7:07 | Block 1:')
rep('gs6', '| 7:08–7:12 | Block 2: Wk 5 check-in | Shared | Lead Comp | Brief: how did the friendship practice land? |',
 '| 7:07–7:17 | Block 2: Practice hold re-entry — the what-held round | Shared | Lead Comp | What continued, what lapsed, what surprised. Received without fixing. |')
rep('gs6', '| 7:12–7:25 | Block 3:', '| 7:17–7:28 | Block 3:')
rep('gs6', '| 7:25–7:30 | Block 4:', '| 7:28–7:33 | Block 4:')
rep('gs6', '| 7:30–7:32 | Block 5:', '| 7:33–7:35 | Block 5:')
rep('gs6', '| 7:32–8:05 | Block 6:', '| 7:35–8:08 | Block 6:')
rep('gs6', '| 8:05–8:13 | Block 7:', '| 8:08–8:15 | Block 7:')
rep('gs6', '| 8:13–8:18 | Block 8:', '| 8:15–8:19 | Block 8:')
rep('gs6', '| 8:18–8:25 | Block 9:', '| 8:19–8:25 | Block 9:')
# headings
rep('gs6', '## Block 1 — Welcome and Centering (7:00–7:08, 8 min)', '## Block 1 — Welcome and Centering (7:00–7:07, 7 min)')
rep('gs6', '## Block 2 — Week 5 Check-in (7:08–7:12, 4 min)', '## Block 2 — Practice Hold Re-entry — the What-Held Round (7:07–7:17, 10 min)')
rep('gs6', '## Block 3 — James 5:16 and 1 John 1:9 — Confession as Architecture (7:12–7:25, 13 min)', '## Block 3 — James 5:16 and 1 John 1:9 — Confession as Architecture (7:17–7:28, 11 min)')
rep('gs6', '## Block 4 — Companion Demo (7:25–7:30, 5 min)', '## Block 4 — Companion Demo (7:28–7:33, 5 min)')
rep('gs6', '## Block 5 — Bridge to the Split (7:30–7:32, 2 min)', '## Block 5 — Bridge to the Split (7:33–7:35, 2 min)')
rep('gs6', '## Block 6 — Confession-and-Restoration in Cohort Circles (7:32–8:05, 33 min)', '## Block 6 — Confession-and-Restoration in Cohort Circles (7:35–8:08, 33 min)')
rep('gs6', '## Block 7 — Merge and Shared Blessing (8:05–8:13, 8 min)', '## Block 7 — Merge and Shared Blessing (8:08–8:15, 7 min)')
rep('gs6', '## Block 8 — Between-Session Practice (8:13–8:18, 5 min)', '## Block 8 — Between-Session Practice (8:15–8:19, 4 min)')
rep('gs6', '## Block 9 — Closing Container (8:18–8:25, 7 min)', '## Block 9 — Closing Container (8:19–8:25, 6 min)')
# scripts
rep('gs6', '“Tonight is Week 6. We are halfway through. The first four weeks were preparation. Tonight we use what we have built',
 '“Tonight is Week 6, and the second act begins. Five weeks built the foundation, and the two-week hold just tested it. Tonight we use what we have built')
rep('gs6', '*“Last week we did the friendship audit and committed to one condition, one friendship, one week. Take ninety seconds: any one of you, one sentence about how that practice landed.”*',
 '*“Before the hold, we committed to one condition in one friendship — and then the meetings stopped for two weeks, on purpose. So the round tonight is the what-held round, and it has three questions: what continued, what lapsed, and what surprised you. One sentence each, any of the three. ‘It lapsed by the first Thursday, and I noticed I missed it’ is a real answer — in this room it may be the most valuable answer.”*')
rep('gs6', '*(Take 2–3 voluntary contributions. Don’t ask for more. Move on.)*',
 '*(Around the circle, voluntary, pass anytime. Receive every report without fixing it — the honest lapse most warmly of all. Do not summarize the round into a lesson; the round is the lesson.)*\n\n*(Leader note: worth a quiet written line afterward — how long did the room take to settle tonight, after two unheld weeks? That number is data the year will want.)*')

# ================= GS WEEK 11 =================
rep('gs11', '**Mode.** Shared teaching of the practice; SPLIT into pairs within cohort circles for the Any Doubts? exercise; MERGE for closing.',
 '**Mode.** Shared teaching of the practice; SPLIT into pairs within cohort circles for the Any Doubts? exercise; MERGE for closing.\n\n**Re-entry.** This session follows the second two-week practice hold; Block 2 is the what-held round on the garden rhythm.')
rep('gs11', '| 7:00–7:08 | Block 1:', '| 7:00–7:07 | Block 1:')
rep('gs11', '| 7:08–7:13 | Block 2: Week 9 check-in | Shared circle | Lead Comp | Brief check on garden returns. One-sentence shares. |',
 '| 7:07–7:17 | Block 2: Practice hold re-entry — the what-held round | Shared circle | Lead Comp | Visits kept and missed; the quiet weeks; anything heard, not yet told. |')
rep('gs11', '| 7:13–7:25 | Block 3:', '| 7:17–7:28 | Block 3:')
rep('gs11', '| 7:25–7:35 | Block 4:', '| 7:28–7:37 | Block 4:')
rep('gs11', '| 7:35–7:38 | Block 5:', '| 7:37–7:40 | Block 5:')
rep('gs11', '| 7:38–8:13 | Block 6:', '| 7:40–8:15 | Block 6:')
rep('gs11', '| 8:13–8:22 | Block 7:', '| 8:15–8:23 | Block 7:')
rep('gs11', '| 8:22–8:27 | Block 8:', '| 8:23–8:27 | Block 8:')
rep('gs11', 'Reaffirm. Aaronic blessing. Mention next Tuesday closes Getting Started.', 'Reaffirm. Aaronic blessing. Frame Week 12.')
rep('gs11', '## **Block 1 — Welcome and Centering (7:00–7:08, 8 min)**', '## **Block 1 — Welcome and Centering (7:00–7:07, 7 min)**')
rep('gs11', '## **Block 2 — Week 9 Check-in (7:08–7:13, 5 min)**', '## **Block 2 — Practice Hold Re-entry — the What-Held Round (7:07–7:17, 10 min)**')
rep('gs11', '## **Block 3 — Mark 9:14–29 — The Scripture Ground (7:13–7:25, 12 min)**', '## **Block 3 — Mark 9:14–29 — The Scripture Ground (7:17–7:28, 11 min)**')
rep('gs11', '## **Block 4 — The Any Doubts? Practice — Teaching (7:25–7:35, 10 min)**', '## **Block 4 — The Any Doubts? Practice — Teaching (7:28–7:37, 9 min)**')
rep('gs11', '## **Block 5 — Bridge to the Split (7:35–7:38, 3 min)**', '## **Block 5 — Bridge to the Split (7:37–7:40, 3 min)**')
rep('gs11', '## **Block 6 — Any Doubts? in Pairs (7:38–8:13, 35 min)**', '## **Block 6 — Any Doubts? in Pairs (7:40–8:15, 35 min)**')
rep('gs11', '## **Block 7 — Merge and Surface (8:13–8:22, 9 min)**', '## **Block 7 — Merge and Surface (8:15–8:23, 8 min)**')
rep('gs11', '## **Block 8 — Between-Session Practice (8:22–8:27, 5 min)**', '## **Block 8 — Between-Session Practice (8:23–8:27, 4 min)**')
rep('gs11', '“Tonight is Week 11. We have two weeks left in Getting Started. Tonight we are going to do something',
 '“Tonight is Week 11 — the final act of Getting Started begins, and we are back from the second hold. Tonight we are going to do something')
rep('gs11', '*“Last week was the Garden of Your Heart. The practice for this week was three returns to the garden. Anyone want to say one sentence about how that went — the garden visits, or what surfaced, or that you didn’t get to it?”*',
 '*“Before the hold, Week 10 set the garden rhythm at two visits a week, journaled — and said out loud that the goal was a rhythm that survives. Then the meetings stopped for two weeks, which was the test. So: the what-held round. Visits kept, visits missed, what the quiet weeks were like — and anything God said in the garden that you have not yet told anyone. One sentence, any of those. ‘I stopped after the first week’ is a real answer. So is ‘I went, and nothing came’ — the garden has quiet weeks, and showing up is the practice.”*')
rep('gs11', '*(Take 3–4 voluntary contributions. Receive without commentary. Move on with: “Good. The garden is still there. You can return any time. We continue.”)*',
 '*(Around the circle, voluntary. Receive without commentary — and listen for the difference between a practice that lapsed and a practice that went quiet while continuing; they sound alike in the first sentence and are opposites underneath. Close with: “Good. The garden is still there. We continue.”)*\n\n*(Leader note: time-to-settled after this second hold, quietly written down beside the first hold’s number.)*')

# ================= GD WEEK 7 =================
rep('gd7', '**Mode.** Whole-room. No cohort split. The whole cohort sits as one circle with the Bringer’s chair in the centre. ONE Bringer pre-briefed Saturday. ONE real question. The cohort listens together; speaks back; the Bringer weighs.',
 '**Mode.** Whole-room. No cohort split. The whole cohort sits as one circle with the Bringer’s chair in the centre. ONE Bringer pre-briefed Saturday. ONE real question. The cohort listens together; speaks back; the Bringer weighs.\n\n**Re-entry.** This session follows the series’ two-week practice hold; Block 2 is the what-held round on extended PROAPT and the Tells.')
rep('gd7', '| 7:00–7:08 | Block 1:', '| 7:00–7:07 | Block 1:')
rep('gd7', '| 7:08–7:13 | Block 2: Wk 6 landing | Shared circle | Lead Comp | One word about extended PROAPT and the daily Tells. |',
 '| 7:07–7:16 | Block 2: Practice hold re-entry — the what-held round | Shared circle | Lead Comp | The hearing that continued and lapsed; the Tell that surprised; the silence. |')
rep('gd7', '| 7:13–7:30 | Block 3:', '| 7:16–7:31 | Block 3:')
rep('gd7', '| 7:30–7:35 | Block 4:', '| 7:31–7:36 | Block 4:')
rep('gd7', '| 7:35–7:55 | Block 5:', '| 7:36–7:56 | Block 5:')
rep('gd7', '| 7:55–8:15 | Block 6:', '| 7:56–8:16 | Block 6:')
rep('gd7', '| 8:15–8:23 | Block 7:', '| 8:16–8:24 | Block 7:')
rep('gd7', '| 8:23–8:27 | Block 8:', '| 8:24–8:27 | Block 8:')
rep('gd7', '**Block 1 — Open and 60-Second Settling (7:00–7:08, 8 min)**', '**Block 1 — Open and 60-Second Settling (7:00–7:07, 7 min)**')
rep('gd7', '**Block 2 — Wk 6 Landing (7:08–7:13, 5 min)**', '**Block 2 — Practice Hold Re-entry — the What-Held Round (7:07–7:16, 9 min)**')
rep('gd7', '**Block 3 — 1 Corinthians 14 and Corporate Listening (7:13–7:30, 17 min)**', '**Block 3 — 1 Corinthians 14 and Corporate Listening (7:16–7:31, 15 min)**')
rep('gd7', '**Block 4 — Bringer Presents the Question (7:30–7:35, 5 min)**', '**Block 4 — Bringer Presents the Question (7:31–7:36, 5 min)**')
rep('gd7', '**Block 5 — Silent Corporate Listening (7:35–7:55, 20 min)**', '**Block 5 — Silent Corporate Listening (7:36–7:56, 20 min)**')
rep('gd7', '**Block 6 — Speaking-Back Round (7:55–8:15, 20 min)**', '**Block 6 — Speaking-Back Round (7:56–8:16, 20 min)**')
rep('gd7', '**Block 7 — Bringer Weighs and Names (8:15–8:23, 8 min)**', '**Block 7 — Bringer Weighs and Names (8:16–8:24, 8 min)**')
rep('gd7', '**Block 8 — Between-Session Practice (8:23–8:27, 4 min)**', '**Block 8 — Between-Session Practice (8:24–8:27, 3 min)**')
rep('gd7', '“Tonight is Wk 7. Three things to name before we begin.”', '“Tonight is Wk 7 — the first session back from the hold. Three things to name before we begin.”')
rep('gd7', '*“Last Tuesday was extended PROAPT and the Tell step in the room. Across the week each of you was meant to do daily extended PROAPT and one Tell each weekday — five Tells, five different people. One word, around the circle, about how that landed for you. ‘Faithful.’ ‘Spotty.’ ‘Surprising.’ ‘Tested.’ ‘Quiet.’ Pass anytime.”*',
 '*“Three weeks ago, Week 6 sent you out with the extended hearing practice — daily PROAPT on a long passage, and Tells to people outside this cohort — and then the hold took the meetings away for two weeks, which was the point. So: the what-held round. The hearing that continued; the hearing that lapsed; the Tell that surprised you; the silence that had something in it. One sentence, any of those, around the circle. ‘I stopped by the fourth day and I know why’ is costly telling, and it counts here.”*')
rep('gd7', '*(Around the circle. 5 seconds per person. Receive each word with eye contact.)*',
 '*(Around the circle. Receive every report without correction — the honest lapse most warmly. The standing pairs carried the check-ins through the hold; if a pair learned something the room should hear, they may say so, but nothing is required.)*\n\n*(Leader note: time-to-settled tonight, quietly written down — the room has been unheld for two weeks.)*')
rep('gd7', '*“Good. Tonight the daily PROAPT becomes corporate. Each of you has been hearing individually all week; that practice is the foundation for what we do now.”*',
 '*“Good. Here is why tonight follows the hold: each of you has been hearing alone for three weeks. Tonight the cohort becomes a corporate hearing instrument — and everything you just reported, the faithfulness and the lapses and the silence alike, is the foundation we bring to it.”*')

# ================= GO WEEK 9 =================
rep('go9', '**Mode.** Whole-room. The cohort sits as one body for the laying-on-of-hands. The cohort split, if it happens at all tonight, is brief and only if Landing 2 (individual sending) requires cohort-specific preparation.',
 '**Mode.** Whole-room. The cohort sits as one body for the laying-on-of-hands. The cohort split, if it happens at all tonight, is brief and only if Landing 2 (individual sending) requires cohort-specific preparation.\n\n**Re-entry.** This session follows the series’ two-week practice hold; Block 1 carries the what-held round at two levels — each person’s practice, and the cohort’s own yes.')
rep('go9', '| 7:00–7:08 | Block 1: Open + Wk 8 landing review | Shared circle | Lead Companion | Aaronic. Re-read Wk 8’s landing; orient tonight’s adaptation. |',
 '| 7:00–7:12 | Block 1: Open + practice hold re-entry — the what-held round | Shared circle | Lead Companion | Aaronic. Re-read Wk 8’s landing; what held for you, and what held for us. |')
rep('go9', '| 7:08–7:18 | Block 2:', '| 7:12–7:21 | Block 2:')
rep('go9', '| 7:18–7:38 | Block 3:', '| 7:21–7:41 | Block 3:')
rep('go9', '| 7:38–8:13 | Block 4:', '| 7:41–8:16 | Block 4:')
rep('go9', '| 8:13–8:23 | Block 5:', '| 8:16–8:24 | Block 5:')
rep('go9', '| 8:23–8:30 | Block 6:', '| 8:24–8:30 | Block 6:')
rep('go9', '**Block 1 — Open + Wk 8 Landing Review (7:00–7:08, 8 min)**', '**Block 1 — Open + Practice Hold Re-entry — the What-Held Round (7:00–7:12, 12 min)**')
rep('go9', '**Block 2 — Acts 13 Sending Architecture (7:08–7:18, 10 min)**', '**Block 2 — Acts 13 Sending Architecture (7:12–7:21, 9 min)**')
rep('go9', '**Block 3 — Walking the Cost (7:18–7:38, 20 min)**', '**Block 3 — Walking the Cost (7:21–7:41, 20 min)**')
rep('go9', '**Block 4 — Laying-On-of-Hands Sending (7:38–8:13, 35 min)**', '**Block 4 — Laying-On-of-Hands Sending (7:41–8:16, 35 min)**')
rep('go9', '**Block 5 — Bridge to Wks 10–12 (8:13–8:23, 10 min)**', '**Block 5 — Bridge to Wks 10–12 (8:16–8:24, 8 min)**')
rep('go9', '**Block 6 — Closing Container (8:23–8:30, 7 min)**', '**Block 6 — Closing Container (8:24–8:30, 6 min)**')
rep('go9', '‘Holy Spirit, you spoke to us last Tuesday. We have carried what you said across the week.',
 '‘Holy Spirit, you spoke to us at the discernment night. We have carried what you said across the hold.')
rep('go9', '“Tonight is Wk 9. Mission far closes. Last Tuesday the body discerned',
 '“Tonight is Wk 9 — the first session back from the hold. Mission far closes. Three weeks ago the body discerned')
rep('go9', '*(Lead Companion reads Wk 8’s landed sentence from the flip chart, briefly.)*',
 '*(Lead Companion reads Wk 8’s landed sentence from the flip chart, briefly.)*\n\n*“Before we walk the cost, the what-held round — and tonight it has two levels. First, for you: the daily noticing question, the pair check-ins — what held, what lapsed, what surprised you? Second, for us: two unheld weeks have passed since the body said what it said. Where does the room actually stand on it tonight? Say it straight. A yes that settled deeper over the hold is worth knowing. A yes that turned out to be the evening’s enthusiasm is worth knowing more — and better now than three months in. Neither is failure; both are the discernment finishing its work.”*\n\n*(Brief round, voluntary, pass anytime. Receive the room’s answer the way you receive a person’s — without correcting it. What surfaces here feeds directly into the cost-walking in Block 3; do not resolve anything now.)*')
rep('go9', 'the laying-on-of-hands moment, which adapts to what we landed last week.', 'the laying-on-of-hands moment, which adapts to what we landed at the discernment night.')
rep('go9', 'Reversal of Wk 8’s landing. Across the week, members’ honest yes/no/maybe has shifted what was landed.',
 'Reversal of Wk 8’s landing. Across the hold, members’ honest yes/no/maybe has shifted what was landed.')
rep('go9', '‘What we discerned last week we are now refining’', '‘What we discerned before the hold we are now refining’')

# ---- apply ----
fail = 0
for k, path in FILES.items():
    s = io.open(path, encoding='utf-8').read()
    for old, new in R[k]:
        n = s.count(old)
        if n != 1:
            print(f'!! {k}: count={n} for: {old[:70]}')
            fail += 1
            continue
        s = s.replace(old, new)
    io.open(path, 'w', encoding='utf-8').write(s)
    print(f'{k}: {len(R[k])} replacements attempted')
print('FAILURES:', fail)
sys.exit(1 if fail else 0)
