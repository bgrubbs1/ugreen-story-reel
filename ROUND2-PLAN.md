# Round 2 plan (finalists only)

Round 2 runs **2026-11-22 00:00 PT through 2026-11-30 23:45 PT** (submit by **2026-12-01 02:45 ET**).
Up to 30 finalists get **one assigned testing day of free remote access to a UGREEN AI NAS iDX6011 Pro
(64 GB)** between **2026-11-22 and 2026-11-28**, from **00:00 to 23:59 PT** on that day only.
Finalist invitations and credentials are emailed on **2026-11-21**.

Round 1 scores do **not** carry over. Round 2 is judged on the working Skill in the assigned NAS
environment, the demo video, and the documentation - including whether the Round 1 ideas were delivered.

## A. Before the assigned testing day (Nov 21-22)

Hard rules and constraints:

- Credentials arrive by email on 2026-11-21 to the Representative only. Do not share them, do not commit
  them, do not put them in the Skill package or the video.
- Access expires at the end of the assigned day. There is no second day.
- The assigned NAS is reset after the testing window; data deleted during reset cannot be recovered.

Prep checklist (30-45 minutes, before the day):

- [ ] Confirm the assigned day and the connection instructions in the email; note the activation and
      expiration times in the entrant's own calendar (not in this repo).
- [ ] Freeze the Skill: run `./scripts/package.sh` from a clean checkout and confirm exit 0 and
      `static-pass`. Copy `pre-test-skill-package.zip` next to the final package as the fallback.
- [ ] Run `python3 scripts/make_proposal_pdf.py --check` (>500-word guard) so the video narration and
      the final documentation stay consistent with the proposal.
- [ ] Prepare a 3-minute recording plan (section E) and a screenshot checklist (section D).
- [ ] Prepare the exact trigger sentence to speak: *"Make a memory story from our summer in 2024, warm
      tone, and save both the album and the story."* Have a second trigger sentence ready for the Kyoto
      trip case.
- [ ] Rehearse the approval flow so the gateway/workflow approval prompt is expected, not a surprise.
- [ ] Have a way to get files off the NAS before the day ends: download screenshots/recordings to the
      entrant's own machine via the browser session / client, not by leaving them on the NAS.
- [ ] Check network, screen recorder, microphone, and a quiet room for the video take.

## B. Install / validation steps on the assigned iDX6011 Pro

Exact UI labels for loading a third-party Skill on the assigned NAS are **UNVERIFIED** for this
round - the public rules, starter kit, and kit README do not publish the finalist device click path.
The finalist instructions in the credentials email are authoritative; follow them first. The
following sequence is the plan to adapt:

1. **Connect** to the assigned NAS exactly as the credentials email says (remote access URL/client).
2. **Verify the environment** (record the firmware/UGOS version and the Skills page entry point shown).
3. **Load the Skill package** into the Skills area using the mechanism named in the finalist
   instructions (for example an upload page or the Skills Hub publish/import flow shown in the
   environment). Use the final ZIP from this repo. Do not rename `SKILL.md`.
4. **Validate the Skill on device**:
   - [ ] The Skill appears with name `story-reel` and the expected description (accurate, not
         exaggerated, not presented as an official UGREEN skill).
   - [ ] A natural-language trigger in the assistant selects the Skill (no exact-command invocation
         needed).
   - [ ] The Skill's dependency on the three experts is viable: a read-only request reaches
         `photo-agent`, and the assistant does not attempt direct CLI execution.
   - [ ] Approval behavior: no state change is attempted before the user approves the draft.
5. **Smoke test** with a tiny scope (for example one month with a handful of photos) before the two core
   cases. Confirm photo evidence returns real counts/dates, not invented content.
6. **If installation fails**: capture the exact error text and screenshot, try the fallback ZIP, and
   note the failure honestly in the Round 2 documentation (the judging values reliable execution
   appropriate to the stage; a documented honest gap beats a false claim).
7. **Record evidence** as you go: screenshots of each state (`completed`, `waiting_user` /
   `waiting_approval`, `failed` / empty result), album created, story document saved, real album
   identifier and photo count.

## C. Test cases to run on the assigned NAS

### Core test case 1 - period + both outputs (the main demo)

- Trigger sentence: *"Make a memory story from our summer in 2024, warm tone, and save both the album
  and the story."*
- Setup on the assigned NAS: use the photos in the assigned environment. If the library has no 2024
  data, adjust only the period to a period that has real photos, and say so in the video. Do not
  fabricate a period.
- Pass criteria:
  - [ ] Photo evidence returns real clusters, photo counts, date spans, and locations.
  - [ ] Document expert returns 2-5 chapters with titles, highlights, captions.
  - [ ] No invented names, places, events, or dates; gaps are marked unknown.
  - [ ] The draft is shown and the run pauses for approval (`waiting_user`/`waiting_approval`).
  - [ ] After approval, the album is created and the story document is saved, both with real
        identifiers/verified output returned by the experts.
  - [ ] The final report matches what actually exists in the NAS.

### Core test case 2 - event / place + tone (repeat-use case)

- Trigger sentence: *"Make a memory story from our Kyoto trip, playful tone, just the album for now."*
  (or another place/event present in the assigned library; keep the user's real wording)
- Pass criteria:
  - [ ] Place/event filters are handled by the photo expert, with real evidence.
  - [ ] The tone changes wording only, never facts.
  - [ ] Output choice "album only" is honored: no story document is created.
  - [ ] Approval gate still runs before album creation.

### Edge case - empty or partial evidence

- Trigger sentence: *"Make a memory story from our trip to Iceland in 2019."* where the library has no
  matching photos (or no usable timestamps).
- Pass criteria:
  - [ ] The Skill reports "no photos matched" (or the partial result) plainly and stops.
  - [ ] It does not substitute another album, does not widen the scope, and does not invent a story.
  - [ ] No album is created and no document is saved.
  - [ ] If partial (some photos but no timestamps/locations), it asks before continuing and labels the
        chapters as partial.

## D. Data and backup notes

- The assigned NAS is reset; **data deleted during reset cannot be recovered**. Copy everything the
  entrant wants to keep (screenshots, logs, exported album/story evidence, the finished video) off the
  NAS before the assigned day ends.
- Do not rely on the real library staying available after the day; if the video needs the real album
  visible, record it during the session.
- Do not upload personal or sensitive photos into the recorded material. Use the assigned environment's
  content as provided and keep the demo family-appropriate.
- No credentials or personal data are stored in this repository; keep it that way on the testing day
  too (no pasting credentials into docs, scripts, or the video).

## E. Demo video recording (English, < 3 minutes)

Requirements: under 3:00; footage of the Skill running in the assigned NAS environment; narration
explaining the core workflow, key capabilities, and actual results; public on YouTube; English
narration or complete English subtitles; no third-party trademarks or copyrighted music unless
permission is held (showing UGREEN/hackathon material is allowed).

Recording plan:

1. Script: the timed narration table in [`SUBMISSION.md`](SUBMISSION.md#round-2-demo-video-script-finalists-only--3-minutes-english-narration)
   (0:00-2:50). Read it once without recording, then record in 2-3 takes and cut.
2. Capture: 1080p or better; show the real screen. Do not fake a result; if a take fails, cut it.
3. Voice: English narration; also add full English subtitles (safest, and required if narration is not
   English - but keep narration English).
4. Music: no music, or rights-cleared music only. Voice-only is safest.
5. Trim to under 3:00 exactly. Judges are not required to watch beyond three minutes, so put the
   result (album + story + real photos) on screen before 2:10.
6. Upload to YouTube as **Public**, copy the URL, and check it in a private/incognito window before
   submitting.
7. Keep the original recording and the YouTube URL in the submission notes; do not delete it before
   the judging period ends (Dec 5).

## F. Final submission checklist (by 2026-11-30 23:45 PT = 2026-12-01 02:45 ET)

- [ ] Final Skill Package ZIP: same Project as Round 1, `SKILL.md` at root, Markdown only, official
      checker exits 0 on the staged and unpacked package, ZIP and uncompressed size <= 10 MB, each file
      <= 1 MB, <= 100 files.
- [ ] Disclosures still accurate after Round 2 changes (third-party components, sources/licenses,
      principal functionality, AI tools used and principal uses) - update
      `skill/references/disclosures.md` and the excluded proposal section if anything changed.
- [ ] Round 2 documentation: what was tested on the assigned NAS, what passed, what did not, actual
      results, screenshots as text descriptions (do not embed private photos).
- [ ] Demo video: public YouTube URL, under 3:00, English narration/subtitles, shows the Skill running
      on the assigned NAS with real results.
- [ ] Round 1 materials not deleted.
- [ ] Submit through the private Round 2 submission URL from the finalist email.
- [ ] Re-open the submission after submitting and confirm both ZIP and video URL are attached.
- [ ] Keep the Project available free of charge for testing/evaluation until the Round 2 Judging
      Period ends (December 5, 2026).
- [ ] Submit at least 24 hours early; do not rely on the final hour.
