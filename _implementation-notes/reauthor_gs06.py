# GS Week 6 adult re-authoring (confession night).
import io, sys
f = 'docs/getting-started/week-06-brave.md'
s = io.open(f, encoding='utf-8').read()
E = []
def R(old, new): E.append((old, new))

R('Pilot edition — Covenant Christian Academy of Warrenton',
  'Adult edition — the leadership-first year (FotH for a CPR)')
R('- Catholic-style confession associations. For some teens, this will feel foreign or theologically charged. Frame it as Protestant practice grounded in James 5:16, not as sacramental.',
  '- Catholic-style confession associations. For some members, this will feel foreign or theologically charged. Frame it as Protestant practice grounded in James 5:16, not as sacramental.')
R('- The teen who has nothing to confess. Honor it. Reframe: “Where do you want to walk in greater honesty?” Almost everyone has a place.',
  '- The member who has nothing to confess. Honor it. Reframe: “Where do you want to walk in greater honesty?” Almost everyone has a place — and a leader who has rehearsed blamelessness for years may need the reframe most.')
R('- Parents disclosing sins their teen does not know about. Plan for this. The parent cohort is the right place; do not bring it back to the room.',
  '- Members disclosing what a spouse — perhaps sitting in the next circle — does not know. Plan for this. Circle assignments are the protection; do not bring it back to the room.')
R('**If a teen confesses to self-harm or suicidal ideation.** Section 6 applies in full. Two-adult rule, immediate after-session check-in, parent notification, pastoral/clinical backup.',
  '**If a member confesses to self-harm or suicidal ideation.** The safeguarding frame applies in full. Two adults, immediate after-session check-in, pastoral/clinical backup, and the door out named again before they leave.')
R('**If a teen confesses to substance abuse, eating disorder behavior, or pornography use, that warrants intervention.** Honor in the room with brief acknowledgment and blessing. Follow up offline within 48 hours with parent and qualified care. Do NOT process in the room.',
  '**If a member confesses to substance abuse, disordered eating, or pornography use that warrants intervention.** Honor in the room with brief acknowledgment and blessing. Follow up offline within 48 hours with qualified care. Do NOT process in the room.')
R('**If a parent confesses something that significantly affects family dynamics (affair, addiction, financial concealment).** Do not interrogate. Pastoral 1:1 within 48 hours. The room is not a confessional in the legal sense, but the Lead Companion may have mandatory-reporting obligations depending on what is disclosed — review in advance.',
  '**If a member confesses something that significantly affects their family (an affair, addiction, financial concealment).** Do not interrogate. Pastoral 1:1 within 48 hours. The room is not a confessional in the legal sense, and a disclosure that touches a minor’s safety may carry reporting duties — review the host church’s policy in advance.')
R('**If a teen names abuse they have experienced.** Section 6 mandatory reporting protocol applies regardless of the framing of the disclosure.',
  '**If a member names abuse — their own history, or harm involving a minor.** The safeguarding frame applies regardless of the framing of the disclosure, and a disclosure involving a minor may carry mandatory-reporting duties for some in the room.')
R('The frame is critical. We are not asking teens or parents to disclose specific sins.',
  'The frame is critical. We are not asking anyone to disclose specific sins.')
R('We are not introducing Catholic confession, sacramental absolution, or anything contested at CCA.',
  'We are not introducing Catholic confession, sacramental absolution, or anything contested in the host church’s tradition.')
R('| T-15 min | Door opens. | Co-Comp (Teen) |', '| T-15 min | Door opens. | Co-Comp |')
R('| 6:45–7:00 | Arrival window | Forming | Co-Comp (Teen) | Same arrival rhythm. |',
  '| 6:45–7:00 | Arrival window | Forming | Co-Comp | Same arrival rhythm. |')
R('| 8:11–8:15 | Block 8: Between-session practice | Shared | Co-Comp (Parent) | Introduce Five-Minute Examen. |',
  '| 8:11–8:15 | Block 8: Between-session practice | Shared | Co-Comp | Introduce Five-Minute Examen. |')
R('- A pre-arranged Co-Companion (the Parent or Teen Co-Comp) speaks a brief blessing back.',
  '- A pre-arranged Co-Companion speaks a brief blessing back.')
R('- Parents auditing each other’s spouses or kids rather than naming their own place.',
  '- Members auditing spouses or colleagues rather than naming their own place.')
R('- Anyone whose silence in the circle was unusual — a teen who passed, a parent who deflected. Brief, warm, no pressure.',
  '- Anyone whose silence in the circle was unusual — someone who passed, someone who deflected. Brief, warm, no pressure.')

fail = 0
for old, new in E:
    n = s.count(old)
    if n != 1:
        print(f'!! count={n}: {old[:70]}'); fail += 1; continue
    s = s.replace(old, new)

i = s.index('## Junior teens (12–14)')
j = s.index('# Closing Practice')
new_diff = '''## Those doing this work for the first time

The practice is fully accessible with the right framing. “Where do you want to walk in greater honesty?” works for anyone. The Companion must model something concrete.

- Demo is critical. The Companion names something concrete and accessible. “The way I get sharp with my kid when I’m tired” models the form.
- Watch for the member who treats it lightly. Gentle redirect: “Take a breath. Pick something real. Even a small real thing.”
- Watch for the member who confesses to fit in or to seem deep. Same redirect. The real thing is better than the impressive thing.

## The veterans

Veterans can hold this practice at full depth. The challenge is that they may carry specific patterns — substance use, pornography, disordered eating, performance and its costs — that warrant pastoral follow-up rather than circle-level processing.

- Honor the disclosure; do not process it in the circle. The Companion works with the convening leader on follow-up based on the safety threshold.
- Watch for the confession aimed at impressing the circle. Same redirect: real over impressive.
- Watch for the practiced testimony wearing confession’s clothes — named once before, polished since. “Is there a place you haven’t said out loud before?”

## The ordained and the staff

The ordained have the most to lose tonight, and the most to gain. Adults have practiced hiding for longer, and the ordained have practiced it professionally. The circle Companion must go first and go honestly to set the depth.

- Frame at the start, if needed: “The room this cohort will lead is shaped by the honesty of this circle tonight. Nobody here is filing a report.”
- Watch for the member who confesses something significant about their family system (an affair, addiction, financial concealment). Receive in the room with brief acknowledgment. Follow up with pastoral 1:1 within 48 hours. Do not bring it back to the room without their consent and explicit framing.
- Watch for the member who ‘confesses’ someone else’s behavior — a spouse’s, a colleague’s, the congregation’s. Redirect: “Tonight is for our own places.”
- If someone breaks down — normal and welcome. Hold space. Bless gently. Do not rush.

'''
s = s[:i] + new_diff + s[j:]

if fail == 0:
    io.open(f, 'w', encoding='utf-8').write(s)
print(f'W6: {len(E)} pair edits + diff rewrite, {fail} failures')
sys.exit(1 if fail else 0)
