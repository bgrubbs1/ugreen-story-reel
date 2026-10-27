# Story Reel

**Upload to the UGREEN Hackathon 2026 on AI NAS - Track: Bring Memories to Life**

Story Reel is a Markdown-only Uliya Skill that turns a chosen period, event, people or place in a
family's own UGREEN AI NAS photo library into a chaptered, narrated memory album. It gathers only
minimal user intent, delegates photo discovery, clustering and caption evidence to the photo expert,
delegates a strictly factual chaptered narrative to the document expert, shows the draft and waits for
approval, then creates the album and saves the story document - each through the registered expert
that owns that capability.

The project page for judges is this README. The two Round 1 uploads are:

| Upload | File | Limit | Status |
| --- | --- | --- | --- |
| Project Proposal (PDF) | [`proposal/round1-proposal.pdf`](proposal/round1-proposal.pdf) | <= 1 MB, ten answers <= 500 words | built and verified |
| Pre-test Skill Package (ZIP) | [`pre-test-skill-package.zip`](pre-test-skill-package.zip) | <= 10 MB, Markdown only, `SKILL.md` at root | built and verified |

## The user story

**Before.** A family has years of photos on the NAS. They can search a single date or person, but
turning a summer, a trip or a childhood year into something they can actually re-live means hours of
scrolling, picking, and writing captions by hand. Cloud memory tools solve the convenience problem by
sending private photos to external models, and they routinely invent captions or merge unrelated trips.

**With Story Reel.** The user says: *"Make a memory story from our summer in 2024, warm tone, and save
both the album and the story."* Story Reel shows a draft of 3-5 chapters built only from real evidence
in that library (real timestamps, places, clusters, extracted captions), the user approves or edits it,
and only then does the album get created and the story document get saved. Nothing is invented, nothing
leaves the NAS, and no state change happens without the user's explicit approval.

## Why it is different

- **Evidence-grounded, not prompt-grounded.** Every chapter must trace to evidence the photo expert
  returned: real photo counts, date spans, locations, captions. Gaps are reported as unknown, never
  filled with plausible-sounding detail.
- **Approval-gated by design.** The story draft is a first-class step: the Skill enters
  `waiting_user` / `waiting_approval`, and the two side-effecting delegations (create album, save text)
  cannot be reached before explicit approval. The platform gateway/workflow approval is also surfaced.
- **NAS-local.** Discovery, clustering, writing and saving all run through the NAS experts and the NAS
  local AI model. No third-party model, service or data flow is required.
- **Orchestration only.** The parent Skill is Markdown. It delegates with
  `delegate --target <agent-id> --instruction '...'`, never calls `cli.invoke`, never touches files,
  and never claims NAS work it did not receive as a real delegation result.
- **Honest failure handling.** `completed`, `failed`, `cancelled`, `waiting_user`, `waiting_approval`,
  empty results and partial results are all defined, and dependent steps stop when their input is
  missing.

## Skill architecture

```text
                    user request (scope, people/place, tone, output)
                                      |
                                      v
+---------------------------- story-reel (this Skill, Markdown only) ----------------------------+
|                                                                                               |
|  Step 1  delegate --target photo-agent      -> photo evidence: real clusters, dates, places,  |
|            ug-photo: search-picture,          captions, photo counts (no invention)           |
|            search-classify, search-hint,                                                      |
|            meta, vision-ocr, vision-vlm                                                       |
|                                      |                                                        |
|                                      v  only the real result is passed downstream              |
|  Step 2  delegate --target document-agent   -> 2-5 chapters: title + highlight + caption,     |
|            ug-document: writing, qa            constrained to the evidence; gaps marked       |
|                                      |                                                        |
|                                      v                                                        |
|  Step 3  present draft -------------------> waiting_user / waiting_approval                    |
|            user approves / edits / cancels                                                    |
|                                      |                                                        |
|              +-----------------------+------------------------+                               |
|              v                                                v                               |
|  Step 4  delegate --target photo-agent          Step 5  delegate --target knowledge-agent     |
|            ug-photo: create-album /                       ug-knowledge: save-text             |
|            create-album-condition                         (state change, workflow approval)     |
|            (state change, workflow approval)                                                  |
|              +-----------------------+------------------------+                               |
|                                      v                                                        |
|                    report real album id + count, verified document path                       |
+-----------------------------------------------------------------------------------------------+
```

Capability -> expert mapping is declared in `SKILL.md` in the section **Generation-time capability
evidence**, in the exact `- <cli> -> <agent>` form the official checker verifies.

## Repository layout

```text
contest-entries/ugreen/
├── skill/                          # canonical Skill source (what gets zipped)
│   ├── SKILL.md                    # required entry point
│   └── references/
│       ├── photo-evidence-rules.md # evidence + anti-invention rules
│       ├── states-and-recovery.md  # delegation states, empty/partial results, recovery
│       └── disclosures.md          # required third-party + AI tools disclosure
├── pre-test-skill-package.zip      # Round 1 upload 2 (SKILL.md at ZIP root)
├── proposal/
│   ├── round1-proposal.md          # proposal source, word-count markers
│   └── round1-proposal.pdf         # Round 1 upload 1
├── scripts/
│   ├── check.sh                    # stage + run the official static checker
│   ├── package.sh                  # reproducible ZIP build + full verification
│   └── make_proposal_pdf.py        # pure-Python PDF writer + 500-word check
├── research/                       # fetched rules/starter-kit pages + extracted text (evidence)
├── README.md                       # this page
├── SUBMISSION.md                   # paste-ready Devpost fields + Round 2 video script
├── RULES-NOTES.md                  # verbatim rule quotes + compliance analysis
├── ROUND2-PLAN.md                  # finalist testing-day + Nov 30 final plan
├── DEVPOST-SETUP.md                # exact Round 1 upload click-path + user checklist
├── LICENSE                         # MIT for the original skill text
├── .gitignore
└── tooling/uliya-skill-kit/        # official kit (gitignored, NOT redistributed)
```

## Quickstart

Requirements: Node.js 18+ for the official checker, Python 3.9+ for the PDF script, `zip`/`unzip`.

```bash
cd contest-entries/ugreen

# 1. Static-check the Skill with the official checker (stages skill/ to build/story-reel/)
./scripts/check.sh                       # JSON output, exit 0 = uploadable

# 2. Build and verify the Round 1 ZIP (checker on staged + unpacked package, size limits)
./scripts/package.sh

# 3. Rebuild the proposal PDF and enforce the 500-word cap
python3 scripts/make_proposal_pdf.py --check   # word count only
python3 scripts/make_proposal_pdf.py           # writes proposal/round1-proposal.pdf
```

The official checker derives the expected Skill name from the directory basename. Because the canonical
source folder is named `skill/`, `scripts/check.sh` and `scripts/package.sh` copy it to
`build/story-reel/` first; that staged directory is byte-identical to `skill/`. The checker is also run
on the unpacked ZIP at `build/unpacked/story-reel/`.

## Verification results (2026-10-27)

| Check | Command | Result |
| --- | --- | --- |
| Official static checker, staged Skill | `node tooling/uliya-skill-kit/scripts/check-skill.mjs build/story-reel` | **exit 0**, `status: static-pass`, 0 errors, 0 warnings, 0 info |
| Official static checker, unpacked ZIP | `node .../check-skill.mjs build/unpacked/story-reel` | **exit 0**, `status: static-pass`, 0 errors, 0 warnings |
| ZIP size | `wc -c pre-test-skill-package.zip` | 7,284 bytes (limit 10,485,760) |
| Uncompressed package size | `find build/story-reel -type f -exec wc -c {} +` | 16,332 bytes (limit 10,485,760) |
| File count / largest file | `find`, `wc -c` | 4 files (limit 100); largest 9,422 bytes (limit 1,048,576) |
| ZIP layout | `unzip -l pre-test-skill-package.zip` | `SKILL.md`, `references/{disclosures,photo-evidence-rules,states-and-recovery}.md`; Markdown only |
| ZIP reproducibility | two consecutive `./scripts/package.sh` runs | byte-identical builds, sha256 `47978bdc240d327ea0014b3e9f9b36449ec9e925f64157cbcb3432bbb3296e7d` |
| Proposal PDF validity | `file proposal/round1-proposal.pdf` | `PDF document, version 1.4, 3 pages` |
| PDF size | `wc -c proposal/round1-proposal.pdf` | 14,526 bytes (limit 1,048,576) |
| Ten-answer word count | `python3 scripts/make_proposal_pdf.py --check` | **487 words** (limit 500) |
| PDF text extraction | `pdftotext -layout proposal/round1-proposal.pdf -` | all ten answers and the excluded disclosure section extract cleanly |
| Secrets / PII scan | `grep` patterns, manual review | no credentials, no API keys, no personal data, no third-party tooling files in the ZIP |

## Round 2

If selected as a finalist: one assigned testing day between 2026-11-22 and 2026-11-28 on a remote
UGREEN AI NAS iDX6011 Pro (64 GB), then a final Skill Package plus an English-narrated demo video under
3 minutes by **2026-11-30 11:45 pm PT**. See [`ROUND2-PLAN.md`](ROUND2-PLAN.md) for the testing-day
plan and video script, and [`SUBMISSION.md`](SUBMISSION.md) for the paste-ready video narration.

## License

Original Skill text and documentation in this folder are released under the MIT License - see
[`LICENSE`](LICENSE). UGREEN, UGOS, Uliya and the Action/CLI names are UGREEN platform names used only
to describe supported platform capabilities. The official Uliya Skill Kit is not redistributed here.
