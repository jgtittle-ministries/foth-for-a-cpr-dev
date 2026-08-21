import io, sys
f = 'docs/getting-started/index.md'
s = io.open(f, encoding='utf-8').read()
E = [
("- **Weeks 14\u201315** close in two movements \u2014 the whole cohort sent through a family commissioning, then the Companions-in-Formation commissioned as FC1 in a witnessed rite of their own.",
 "- **Weeks 14\u201315** close in two movements \u2014 the Household Blessing Night, where each member blesses their own people before witnesses, then the commissioning rite where the covering takes public authority and the church sends the cohort as its Formation Companion team."),
("- **Detailed Run Sheet** \u2014 minute-by-minute flow for the 90 minutes (120 for Week 10).",
 "- **Detailed Run Sheet** \u2014 minute-by-minute flow for the 90 minutes (120 for Week 14)."),
("- **Length.** Weeks 1\u20139 are 90 minutes. Week 10 is 120 minutes (family commissioning night).",
 "- **Length.** Sessions run 90 minutes. Week 14 runs to 120 minutes (the Household Blessing Night)."),
("- **Companion team.** A convening leader plus Co-Companions. Weeks 2\u20139 use a split-and-merge structure \u2014 shared opening and teaching, then SPLIT into circles of four to eight for the experiential center, MERGE for closing. Week 1 and Week 10 stay in the shared circle the entire session.",
 "- **Companion team.** A convening leader plus Co-Companions. Most mid-series weeks use a split-and-merge structure \u2014 shared opening and teaching, then SPLIT into circles of four to eight for the experiential center, MERGE for closing. Week 1 and the two closing weeks stay in the shared circle the entire session."),
]
fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}'); fail += 1; continue
    s = s.replace(old, new)
if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'gs-index-stale: {len(E)} edits, {fail} failures')
sys.exit(1 if fail else 0)
