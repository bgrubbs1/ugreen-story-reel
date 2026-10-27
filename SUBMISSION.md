# Round 1 submission content (paste-ready)

This file holds the exact Devpost Round 1 fields and the Round 2 follow-up material. Nothing here is
submitted automatically; the entrant reviews and submits.

- Hackathon: UGREEN Hackathon 2026 on AI NAS (Devpost id `31552`)
- Manage submissions page: https://devpost.com/submit-to/31552-ugreen-hackathon-2026-on-ai-nas/manage/submissions
- Track/theme to select: **Bring Memories to Life**
- Round 1 deadline: **Sunday 2026-11-15, 11:45 pm PT** = Monday **2026-11-16, 02:45 ET**
- Round 2 (finalists only) deadline: **2026-11-30, 11:45 pm PT** = **2026-12-01, 02:45 ET**

## Field 1: Project name

```text
Story Reel
```

## Field 2: Tagline / elevator pitch (short, one line)

```text
A NAS-local AI skill that turns your family photo library into a fact-checked, chaptered memory album you approve before anything is created.
```

Alternative shorter line if the field has a tight limit:

```text
Chaptered, narrated memory albums from your own NAS photos, with approval before anything changes.
```

## Field 3: Description / "About the project"

Paste-ready Markdown. Keep the word limit note: the description field is not the ten-question PDF, so
it does not count toward the 500-word cap, but keep it readable.

```markdown
## Inspiration
Every family has a NAS full of photos and no way to turn them into memories. Searching works; telling
the story of a summer, a trip, or a childhood year still takes hours of scrolling, selecting, and
caption writing. Cloud "memory" tools solve it by shipping private photos to external models, then
invent captions and merge unrelated events. On a UGREEN AI NAS, that trade-off is unnecessary.

## What it does
Story Reel turns a chosen period, event, people, or place in a family's photo library into a chaptered,
narrated memory album. It asks for a small scope and an output choice, then:
1. delegates photo discovery and clustering to the photo expert (real timestamps, places, captions,
   photo counts - evidence only, no invention);
2. delegates a strictly factual 2-5 chapter narrative with titles, highlights, and captions to the
   document expert, constrained to that evidence;
3. shows the draft and waits for approval;
4. after approval, creates the album with the photo expert and saves the story document with the
   knowledge expert, then reports the real album id, photo count, and verified document path.
It works with `ug-photo`, `ug-document`, and `ug-knowledge` through their registered experts, and it
never creates anything before approval.

## How it is built
The Skill is Markdown-only orchestration following the official Uliya Skill Development Standard. The
parent Skill delegates with standard `delegate --target <agent> --instruction '...'` commands and never
calls `cli.invoke` or touches files. Every used CLI is declared in the required capability-evidence
section. Empty results, partial results, and all five delegation states are handled explicitly, and
dependent steps stop when their input is missing.

## Why it is different
- Evidence-grounded chapters, not AI imagination: gaps are marked unknown.
- Approval-gated: the draft is a real step, not a courtesy message.
- NAS-local AI: no external model, service, or data flow.
- Both a reusable album and a durable story document come out of one run.

## What is next
Round 1 is a fully specified, statically validated package (official checker: 0 errors, 0 warnings).
If selected as a finalist, one testing day on the assigned UGREEN AI NAS iDX6011 Pro will validate the
expert round trips, approval prompts, and real-library behavior against two core cases and one edge
case (see the proposal PDF, answer 9).
```

## Field 4: Track / theme

Select exactly:

```text
Bring Memories to Life
```

## Field 5: Uploads (exactly two files)

| Upload slot | File to upload | Constraints |
| --- | --- | --- |
| Project Proposal (PDF) | `proposal/round1-proposal.pdf` | PDF, <= 1 MB, ten answers <= 500 words total |
| Pre-test Skill Package (ZIP) | `pre-test-skill-package.zip` | ZIP <= 10 MB, Markdown only, `SKILL.md` at ZIP root |

Optional Devpost fields (video / repo / website) are **not required for Round 1** - do not invent them.
If a field cannot be left empty, leave it blank rather than adding a private repo or placeholder link.

## Field 6: "Built with" / technologies (if the form asks)

```text
UGREEN AI NAS, UGOS, Uliya Skill Development Standard, ug-photo, ug-document, ug-knowledge
```

## Round 1 final checks before submitting

1. PDF opens, page count is 3, ten answers total 487 words (verified by `scripts/make_proposal_pdf.py`).
2. ZIP opens, root contains `SKILL.md` + `references/*.md` only, official checker exits 0.
3. Track is "Bring Memories to Life".
4. Deadline: submit at least 24 hours early. After the Round 1 window closes the submission cannot be
   changed for that round, and Round 1 materials must not be deleted.

## Round 2 demo video script (finalists only, < 3 minutes, English narration)

Rules requirements: under three minutes; shows the Skill running in the assigned UGREEN AI NAS test
environment; narrates the core workflow, key capabilities, and actual results; public on YouTube;
English narration or complete English subtitles; no third-party trademarks or copyrighted music unless
permission is held (showing UGREEN/hackathon materials is allowed).

Recorded during the assigned testing day (2026-11-22 to 2026-11-28) on the assigned iDX6011 Pro.

| Time | Shot | Narration (English) |
| --- | --- | --- |
| 0:00-0:15 | Title card over the NAS desktop / Skills page | "This is Story Reel, a skill for the UGREEN AI NAS that turns a family photo library into a chaptered memory album. Everything you will see runs on the NAS itself." |
| 0:15-0:40 | Trigger the skill with a real sentence: *"Make a memory story from our summer in 2024, warm tone, and save both the album and the story."* | "The user gives one sentence: a period, a tone, and the two outputs. Story Reel asks only for what is missing, then delegates photo discovery to the photo expert - real dates, real places, real clusters, no invented content." |
| 0:40-1:05 | Show the photo evidence coming back (photo counts, date spans, locations) | "The photo expert searches the local library, clusters the best candidates, and returns evidence. Story Reel passes only that verified evidence to the document expert, which writes two to five chapters with titles, highlights, and captions." |
| 1:05-1:35 | Show the proposed story draft on screen | "Before anything changes, the skill presents the draft: chapters, photo counts, and the album and story document names. This is the approval gate. Nothing has been written to the library yet." |
| 1:35-2:10 | Approve in the conversation, then show the approval prompt and the real album being created | "After explicit approval, the photo expert creates the album and the knowledge expert saves the story document. Both are state-changing actions, so the platform approval is part of the flow. The user sees the real album and document, not a promise." |
| 2:10-2:35 | Open the created album and the saved story document; scroll the real chapters | "Here is the result: an album of the real photos, and a durable written story with the same chapters. Every caption traces back to evidence from this library." |
| 2:35-2:50 | Show the failure path briefly: a scope with no matching photos | "If the scope has no matching photos, it says so and stops. It does not substitute another album or invent a memory. That is Story Reel: evidence-grounded, approval-gated, and entirely NAS-local." |

Production notes:

- Keep the recording under 3:00; trim exactly. Put full English subtitles on the video even if narrating.
- Show real screen activity (no mockups). If a take fails, cut it - do not fake a result.
- Upload to YouTube as public, copy the link into the Round 2 Devpost form.
- No background music unless it is rights-cleared; voice-only is safest.

## Finalist testing-day plan (summary; details in ROUND2-PLAN.md)

1. Before the assigned day: read the credentials email (arrives 2026-11-21 from UGREEN, sent to the
   Representative only), confirm the assigned day and connection instructions, prepare the final ZIP
   and a recording script.
2. On the assigned day (12:00 a.m. - 11:59 p.m. PT access only): connect, install/load the Skill,
   validate it on device, run core case 1, core case 2, and the edge case, capture screenshots and
   logs, record the demo video.
3. Before the day ends: copy all evidence and the recording off the NAS, because the environment is
   reset and deleted data cannot be recovered.
4. By 2026-11-30 11:45 pm PT: submit the final Skill ZIP and the public YouTube link through the private
   Round 2 submission URL.
