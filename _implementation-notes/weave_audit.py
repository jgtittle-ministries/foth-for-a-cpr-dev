import io, re, glob
HEAD_RE = re.compile(r'^(#{0,2}\s*\*{0,2})Block (\d+[a-c]?) — (.*?) \((\d+:\d+)[–-](\d+:\d+), (\d+) min(, [^)]+)?\)(\*{0,2})\s*$', re.M)
ROW_RE = re.compile(r'^\| (\d+:\d+)[–-](\d+:\d+) \| ([^|]+?) \|', re.M)
def mins(t):
    h, m = map(int, t.split(':')); return (h % 12) * 60 + m
src = io.open('_implementation-notes/weave_engine.py', encoding='utf-8').read()
Sblock = src.split('S = {')[1].split('\n}')[0]
probs = 0
files = sorted(glob.glob('docs/*/week-*.md'))
files = [f.replace(chr(92), '/') for f in files if 'practice-hold' not in f]
for f in files:
    s = io.open(f, encoding='utf-8').read()
    name = f.split('/')[-2] + '/' + f.split('/')[-1]
    excluded = any(x in f for x in ('week-14-sending', 'week-15-commissioning', 'going-out/week-12'))
    heads = {}
    for m in HEAD_RE.finditer(s):
        heads[m.group(2)] = (mins(m.group(4)), mins(m.group(5)), int(m.group(6)))
        if not m.group(2).endswith(('b', 'c')) and mins(m.group(5)) - mins(m.group(4)) != int(m.group(6)):
            print(f'!! {name} heading B{m.group(2)}: span != dur'); probs += 1
    rows = [(m.group(1), m.group(2), m.group(3).strip()) for m in ROW_RE.finditer(s)]
    if rows:
        prev = None
        for a, b, nm in rows:
            if prev is not None and mins(a) != prev:
                print(f'!! {name} gap/overlap before "{nm[:40]}" at {a}'); probs += 1
            prev = mins(b)
        if rows[-1][1] not in ('8:30', '8:25'):
            print(f'!! {name} ends {rows[-1][1]}'); probs += 1
        for a, b, nm in rows:
            bm = re.match(r'Block (\d+[a-c]?):', nm)
            if bm and bm.group(1) in heads:
                ha, hb, hd = heads[bm.group(1)]
                if (mins(a), mins(b)) != (ha, hb):
                    print(f'!! {name} B{bm.group(1)} table {a}-{b} disagrees with heading'); probs += 1
    line = [l for l in Sblock.split('\n') if f in l]
    if excluded:
        for probe in ('one true sentence. One true thing', 'Before we close the container: the round'):
            if probe in s:
                print(f'!! {name}: EXCLUDED file contains weave text'); probs += 1
        continue
    if not line:
        print(f'?? {name} not in decision map'); continue
    l = line[0]
    if "ots='" in l and 'ne true sentence' not in s:
        print(f'!! {name}: OTS expected, missing'); probs += 1
    if "rnd='tb:" in l:
        if 'teach-back, leader only' not in s:
            print(f'!! {name}: teach-back missing'); probs += 1
    elif "rnd='so:" in l or ("rnd='" in l):
        if 'Before we close the container: the round' not in s:
            print(f'!! {name}: round missing'); probs += 1
    if "setup='" in l and 'carried into the hold on no paper' not in s:
        print(f'!! {name}: setup missing'); probs += 1
    if "ans='" in l and 'the question you carried into the hold' not in s:
        print(f'!! {name}: answer fold missing'); probs += 1
print('files checked:', len(files), '| problems:', probs)
