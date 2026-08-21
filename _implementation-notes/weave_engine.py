# The session weave (backlog 15b): One True Sentence + Leader Feedback Round
# + teach-back + self-read beats, woven into the run sheets with clocks paid.
# Per-session decisions are explicit; the engine repacks clocks preserving gaps,
# keeps every substitution counted, and fails loudly.
import io, re, sys

EN = '–'

OTS_TXT = '''
*“And before we move on: one true sentence. One true thing about your own week with God, however small. ‘Nothing came’ is a true sentence. We receive; we do not fix.”*

*(Around the circle, brief, pass anytime. This beat runs every week of the year — the smallest rung of costly telling, its occasion scheduled so the muscle always has one.)*
'''

RND_TXT = '''
*“Before we close the container: the round. I led tonight, so I go first — what I think went well, and what I would do differently. [Leader answers, specific and brief.] Now the room, same two questions about the evening. Went well; do differently. About the evening and how we ran it — never about what any person brought, said, or heard.”*

*(Receive without defending. Then the teach-back, leader only: “If I were to teach tonight’s process to someone, here is what I would tell them.” One or two sentences. Then close the container as written below.)*
'''

TB_TXT = '''
*(Then the teach-back, leader only: “If I were to teach tonight’s process to someone, here is what I would tell them.” One or two sentences, and done.)*
'''

SETUP_TXT = '''
*“One more thing, carried into the hold on no paper: think about us. What should we keep doing? What could we do differently? And what would you tell somebody else about what this group is like? Don’t answer tonight. Carry it. We answer together when we return.”*
'''

ANSWER_TXT = '''
*“And now the question you carried into the hold: keep, change, tell. What should we keep doing? What could we do differently? What would you tell somebody about this group? I answer first, with evidence, same as always.”*

*(The signs are never handed to the room; map what you hear to the observing pages afterward, on your side of the paper. A gap between the room’s read and yours is data, never a correction.)*
'''

# ots: block gaining +3 and the OTS script ('so:'=script-only, no clock)
# rnd: closing block gaining +4, retitle, round script ('tb:'=teach-back only)
# setup: closing block gaining +2 more + setup script (pre-holds)
# ans: block gaining the answer fold, script only (re-entries)
# cuts: {block: minus-minutes}
S = {
 'docs/getting-started/week-01-welcome.md': dict(table=False, rnd='so:8', retitle={'8': 'Feedback Round and Closing Container'}),
 'docs/getting-started/week-02-soil.md': dict(table=False, ots='2', rnd='7', retitle={'7': 'Feedback Round, Closing Container and Aaronic Blessing'}, cuts={'1': 2, '3': 3, '5': 2}),
 'docs/getting-started/week-03-story.md': dict(ots='2', rnd='9', cuts={'1': 2, '3': 1, '4': 1, '6': 1, '7': 1, '8': 1}),
 'docs/getting-started/week-04-story-2.md': dict(ots='2', rnd='tb:7', cuts={'1': 2, '3': 1}),
 'docs/getting-started/week-05-known.md': dict(ots='2', rnd='8', setup='8', cuts={'1': 2, '3': 2, '5': 1, '6': 2, '7': 2}),
 'docs/getting-started/week-06-brave.md': dict(rnd='9', ans='2', cuts={'3': 1, '4': 1, '6': 1, '7': 1}),
 'docs/getting-started/week-07-proapt.md': dict(ots='2', rnd='9', cuts={'1': 1, '3': 1, '4': 1, '6': 2, '7': 1, '8': 1}),
 'docs/getting-started/week-08-proapt-2.md': dict(ots='2', rnd='tb:8', cuts={'1': 1, '4': 2}),
 'docs/getting-started/week-09-garden.md': dict(ots='2', rnd='8', cuts={'1': 2, '3': 3, '6': 2}),
 'docs/getting-started/week-10-garden-2.md': dict(ots='2', rnd='tb:9', setup='9', cuts={'1': 1, '3': 2, '6': 1, '7': 1}),
 'docs/getting-started/week-11-doubts.md': dict(rnd='9', ans='2', cuts={'3': 1, '4': 1, '7': 1, '8': 1}),
 'docs/getting-started/week-12-mission.md': dict(ots='2', rnd='8', cuts={'1': 1, '3': 2, '5': 2, '6': 2}),
 'docs/getting-started/week-13-rhythm.md': dict(ots='2', rnd='tb:8', cuts={'3': 2, '6': 1}),
 'docs/going-deeper/week-01-welcome-back.md': dict(ots='so:2', rnd='8', cuts={'2': 2, '4': 1, '5': 1}),
 'docs/going-deeper/week-02-soils.md': dict(ots='2', rnd='8', cuts={'1': 1, '3': 3, '5': 2, '6': 1}),
 'docs/going-deeper/week-03-knots.md': dict(ots='2', rnd='9', cuts={'1': 1, '3': 3, '4': 1, '6': 1, '7': 1}),
 'docs/going-deeper/week-04-co-processing.md': dict(ots='2', rnd='9', cuts={'1': 1, '3': 2, '5': 2, '7': 2}),
 'docs/going-deeper/week-05-confession.md': dict(ots='2', rnd='8', cuts={'1': 1, '3': 3, '5': 2, '6': 1}),
 'docs/going-deeper/week-06-proapt.md': dict(ots='2', rnd='8', setup='8', cuts={'1': 1, '3': 3, '4': 1, '5': 2, '6': 1, '7': 1}),
 'docs/going-deeper/week-07-corporate-listening.md': dict(rnd='9', ans='2', cuts={'3': 2, '4': 1, '6': 1}),
 'docs/going-deeper/week-08-group-hears-itself.md': dict(ots='2', rnd='8', cuts={'1': 1, '3': 3, '5': 2, '6': 1}),
 'docs/going-deeper/week-09-shadow-mission.md': dict(ots='2', rnd='8', cuts={'3': 4, '5': 2, '6': 1}),
 'docs/going-deeper/week-10-calling-discernment.md': dict(ots='2', rnd='9', cuts={'1': 1, '3': 3, '6': 2, '7': 1}),
 'docs/going-deeper/week-11-where-is-our-cohort.md': dict(ots='2', rnd='8', cuts={'1': 1, '3': 2, '5': 2, '6': 2}),
 'docs/going-deeper/week-12-sending-and-bridge.md': dict(ots='2', cuts={'1': 1, '3': 2}),
 'docs/going-out/week-01-welcome-back.md': dict(ots='so:4', rnd='7', cuts={'2': 1, '3': 1, '4': 1, '5': 1}),
 'docs/going-out/week-02-body-sent.md': dict(ots='2', rnd='8', cuts={'1': 1, '3': 3, '4': 1, '5': 2}),
 'docs/going-out/week-03-where-sent.md': dict(ots='1', rnd='7', cuts={'2': 1, '4': 2, '5': 2, '6': 2}),
 'docs/going-out/week-04-daily-tells.md': dict(ots='1', rnd='7', cuts={'2': 3, '4': 2, '5': 2}),
 'docs/going-out/week-05-household.md': dict(ots='1', rnd='6', cuts={'2': 1, '3': 2, '4': 2, '5': 2}),
 'docs/going-out/week-06-vocational.md': dict(ots='1', rnd='7', cuts={'2': 2, '4': 2, '5': 1, '6': 2}),
 'docs/going-out/week-07-third-place.md': dict(ots='1', rnd='7', cuts={'2': 3, '4': 2, '5': 1, '6': 1}),
 'docs/going-out/week-08-discernment.md': dict(rnd='7', setup='7', cuts={'2': 1, '3': 1, '4': 2, '6': 2}),
 'docs/going-out/week-09-body-sent-beyond.md': dict(rnd='6', ans='1', cuts={'2': 1, '4': 2, '5': 1}),
 'docs/going-out/week-10-what-going-out-produced.md': dict(ots='1', rnd='7', cuts={'2': 1, '3': 1, '4': 2, '5': 2, '6': 1}),
 'docs/going-out/week-11-cohort-lands.md': dict(ots='1', rnd='6', retitle={'6': 'Feedback Round, Bridge to Wk 12 and Closing'}, cuts={'2': 1, '3': 2, '4': 2, '5': 2}),
}
EXCLUDED = ['docs/getting-started/week-14-sending.md', 'docs/getting-started/week-15-commissioning.md', 'docs/going-out/week-12-long-obedience.md']

def mins(t):
    h, m = map(int, t.split(':')); return (h % 12) * 60 + m
def clock(m):
    h = m // 60; mm = m % 60
    if h == 0: h = 12
    return f'{h}:{mm:02d}'

HEAD_RE = re.compile(r'^(#{0,2}\s*\*{0,2})Block (\d+[a-c]?) — (.*?) \((\d+:\d+)[–-](\d+:\d+), (\d+) min(, [^)]+)?\)(\*{0,2})\s*$', re.M)
ROW_RE = re.compile(r'^\| (\d+:\d+)[–-](\d+:\d+) \| ([^|]+?) \|', re.M)

report = []
problems = 0
ONLY = set(sys.argv[1:])
for f, d in S.items():
    if ONLY and f not in ONLY: continue
    s = io.open(f, encoding='utf-8').read()
    delta = {}
    for b, c in d.get('cuts', {}).items(): delta[b] = delta.get(b, 0) - c
    ots = d.get('ots'); rnd = d.get('rnd'); setup = d.get('setup'); ans = d.get('ans')
    if ots and not ots.startswith('so:'): delta[ots] = delta.get(ots, 0) + 3
    if rnd and not rnd.startswith(('so:', 'tb:')): delta[rnd] = delta.get(rnd, 0) + 4
    if setup: delta[setup] = delta.get(setup, 0) + 2
    if sum(delta.values()) != 0:
        print(f'!! {f}: deltas do not sum to zero ({sum(delta.values())})'); problems += 1; continue

    # --- parse headings, compute new clock preserving gaps ---
    heads = list(HEAD_RE.finditer(s))
    if not heads:
        print(f'!! {f}: no block headings'); problems += 1; continue
    sched = []  # (blockid, start, end, dur)
    for m in heads:
        sched.append([m.group(2), mins(m.group(4)), mins(m.group(5)), int(m.group(6))])
    newt = {}
    cur = sched[0][1]
    prev_end = None
    for bid, a, b, dur in sched:
        if bid.endswith(('b', 'c')):  # parallel split blocks share the base block's window
            base = bid[:-1]
            newt[bid] = newt[base]; continue
        if prev_end is not None:
            cur += a - prev_end  # preserve original gap
        nd = dur + delta.get(bid, 0)
        if nd < 2: print(f'!! {f}: block {bid} would be {nd} min'); problems += 1
        newt[bid] = (cur, cur + nd, nd)
        cur, prev_end = cur + nd, b
    end_orig = sched[-1][2]
    end_new = newt[sched[-1][0]][1]
    if end_new != end_orig:
        print(f'!! {f}: end drift {clock(end_new)} vs {clock(end_orig)}'); problems += 1; continue

    # --- rewrite headings (times + retitles) ---
    retitle = d.get('retitle', {})
    if rnd and not rnd.startswith(('so:', 'tb:')) and rnd not in retitle:
        m = next(m for m in heads if m.group(2) == rnd)
        old_t = m.group(3).rstrip('* ').strip()
        low = old_t[0].lower() + old_t[1:] if old_t else old_t
        retitle[rnd] = 'Feedback Round and ' + old_t
    def hsub(m):
        bid = m.group(2)
        a, b, nd = newt[bid]
        title = retitle.get(bid, m.group(3))
        suf = m.group(7) or ''
        return f'{m.group(1)}Block {bid} — {title} ({clock(a)}{EN}{clock(b)}, {nd} min{suf}){m.group(8)}'
    s = HEAD_RE.sub(hsub, s)

    # --- rewrite table rows ---
    if d.get('table', True):
        rows = list(ROW_RE.finditer(s))
        seq = []
        for m in rows:
            nm = m.group(3).strip()
            bm = re.match(r'Block (\d+[a-c]?):\s*(.*)', nm)
            seq.append((m, bm.group(1) if bm else None, mins(m.group(1)), mins(m.group(2)), bm.group(2) if bm else nm))
        pieces, last = [], 0
        cur = seq[0][2]; prev_end = None
        for m, bid, a, b, nm in seq:
            if prev_end is not None: cur += a - prev_end
            nd = (b - a) + (delta.get(bid, 0) if bid else 0)
            na, nb = cur, cur + nd
            cur, prev_end = nb, b
            if bid and bid in retitle:
                nt = retitle[bid]
                nm2 = f'Block {bid}: {nt[0] + nt[1:].lower() if nt.isupper() else nt[0] + nt[1:]}'
                nm2 = f'Block {bid}: {retitle[bid][0]}{retitle[bid][1:].lower()}' if False else f'Block {bid}: {retitle[bid][0] + retitle[bid][1:].lower()}'
                # sentence-case the retitle for table style
                tt = retitle[bid]
                nm2 = f'Block {bid}: {tt[0] + tt[1:].lower()}'
            elif bid:
                nm2 = f'Block {bid}: {nm}'
            else:
                nm2 = nm
            pieces.append(s[last:m.start()])
            pieces.append(f'| {clock(na)}{EN}{clock(nb)} | {nm2} |')
            last = m.end()
        pieces.append(s[last:])
        s = ''.join(pieces)
        if cur - seq[0][2] != seq[-1][3] - seq[0][2]:
            print(f'!! {f}: table end drift'); problems += 1

    # --- script inserts: place text right after the block's heading line ---
    def insert_after_block_heading(text, bid, label):
        nonlocal_s = insert_after_block_heading  # noop
        m2 = re.search(r'^(#{0,2}\s*\*{0,2})Block ' + re.escape(bid) + r' — [^\n]*$', SREF[0], re.M)
        if not m2:
            print(f'!! {f}: no heading for block {bid} ({label})'); return False
        pos = m2.end()
        # skip an immediately-following '## Script' line
        after = SREF[0][pos:pos+30]
        mm = re.match(r'\s*\n+(#+\s*\*{0,2}Script\*{0,2})\s*\n', SREF[0][pos:])
        if mm: pos += mm.end()
        SREF[0] = SREF[0][:pos] + '\n' + text.strip() + '\n' + SREF[0][pos:]
        return True

    SREF = [s]
    def insert_end_of_block(text, bid, label):
        m2 = re.search(r'^(#{0,2}\s*\*{0,2})Block ' + re.escape(bid) + r' — [^\n]*$', SREF[0], re.M)
        if not m2:
            print(f'!! {f}: no heading for block {bid} ({label})'); return False
        nxt = re.search(r'^(#{0,2}\s*\*{0,2})Block \d+[a-c]? — ', SREF[0][m2.end():], re.M)
        pos = m2.end() + (nxt.start() if nxt else len(SREF[0]) - m2.end())
        SREF[0] = SREF[0][:pos].rstrip() + '\n\n' + text.strip() + '\n\n' + SREF[0][pos:].lstrip('\n')
        return True

    ok = True
    if ots:
        bid = ots.split(':')[-1]
        ok &= insert_end_of_block(OTS_TXT, bid, 'OTS')
    if ans:
        ok &= insert_end_of_block(ANSWER_TXT, ans, 'answer-fold')
    if rnd:
        bid = rnd.split(':')[-1]
        if rnd.startswith('tb:'):
            ok &= insert_end_of_block(TB_TXT, bid, 'teach-back')
        else:
            ok &= insert_after_block_heading(RND_TXT, bid, 'round')
    if setup:
        # setup beat goes after the round text, still inside the closing block
        ok &= insert_after_block_heading(RND_TXT.strip() + '\n\n' + SETUP_TXT.strip(), setup, 'round+setup') if not rnd else True
        if rnd and not rnd.startswith(('so:', 'tb:')):
            # round already inserted after heading; append setup right after it
            i = SREF[0].find(RND_TXT.strip())
            if i < 0: print(f'!! {f}: setup anchor missing'); ok = False
            else:
                j = i + len(RND_TXT.strip())
                SREF[0] = SREF[0][:j] + '\n\n' + SETUP_TXT.strip() + SREF[0][j:]
        elif rnd and rnd.startswith('tb:'):
            ok &= insert_end_of_block(SETUP_TXT, setup, 'setup')
    s = SREF[0]
    if not ok: problems += 1

    io.open(f, 'w', encoding='utf-8').write(s)
    report.append(f'{f.split("/")[-1]}: ok')

print(f'{len(report)} sessions woven, {problems} problems')
sys.exit(1 if problems else 0)
