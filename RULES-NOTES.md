# Rules notes: verbatim quotes and compliance analysis

Sources (fetched 2026-10-27 with `curl -s -L -A 'Mozilla/5.0'`; raw HTML and extracted text are kept
under `research/` for audit):

- Official rules: https://ugreenhackathon.devpost.com/rules
- Hackathon overview / submission page: https://ugreenhackathon.devpost.com/
- Official starter kit: https://ai.ugreen.com/pages/hackathon-starter-kit

Quotes are verbatim from the rendered pages, including their original punctuation and typography
(including the full-width closing parenthesis in the rules for Round 2 functionality). Each quote is
followed by "What we do". Where the public pages are silent or ambiguous, the item is marked
**UNVERIFIED**.

## 1. Dates and deadlines

> Round 1 Submission Period:
> October 22, 2026 (9:00 am Pacific Time) – November 15, 2026 (11:45 pm Pacific Time) ("Round 1
> Submission Period").

> Round 1 Judging Period:
> November 16, 2026 (12:00 am Pacific Time) – November 19, 2026 (5:00 pm Pacific Time) ("Round 1
> Judging Period").

> Finalist Invitations:
> November 21, 2026 (12:00 a.m. Pacific Time).

> Round 2 Submission Period:
> November 22, 2026 (12:00 am Pacific Time)  - November 30, 2026 (11:45 pm Pacific Time) ("Round 2
> Submission Period").

> Round 2 Judging Period:
> December 1, 2026 (10:00 am Pacific Time) - December 5, 2026 (5:00 pm Pacific Time) ("Round 2 Judging
> Period").

> Winners Announced:
> On or around December 6, 2026 (2:00 pm Pacific Time).

The Devpost page header also shows: `Deadline: Nov 15, 2026 @ 11:45pm PST`.

**What we do.** Round 1 is targeted for 2026-11-15 11:45 pm PT. November 15 is after US daylight saving
ends (2026-11-01), so 11:45 pm PT = 2026-11-16 02:45 ET. Plan to submit at least 24 hours early.
Round 2 is 2026-11-30 11:45 pm PT = 2026-12-01 02:45 ET. Note Devpost says "PST" on the page header and
"Pacific Time" in the rules; treat both as America/Los_Angeles local time.

> Before the end of each Submission Period, you may save draft versions of your Submission. Once a
> Submission Period ends, you may not change the Submission for that round, but you may continue to
> update the Project in your Devpost portfolio. Do not delete your Round 1 Submission materials.

**What we do.** Round 1 materials are kept in this repository and not deleted after submitting.

> At 12:00 a.m. PT on November 21, 2026 , UGREEN will email each Finalist its temporary login
> credentials, assigned device, testing day, connection instructions, and private submission URL. Each
> Finalist Project receives one set of credentials and one testing day. For Teams and Organizations,
> UGREEN sends the credentials only to the Representative.

**What we do.** No credentials are requested, stored, or committed in this repo. If the entrant
advances, credentials stay in the entrant's own password manager and never enter this repository.

## 2. Eligibility

> The Hackathon IS open to:
>
> Individuals who are at least the age of majority where they reside as of the time of entry ("Eligible
> Individuals");
>
> Teams of up to three Eligible Individuals ("Teams"); and
>
> (the above are collectively, "Entrants")

> Each Eligible Individual may enter either individually or as a member of one Team, but not both. An
> Eligible Individual may not join more than one Team. If a Team or Organization is entering the
> Hackathon, they must appoint and authorize one individual (the "Representative") to represent, act,
> and enter a Submission, on their behalf.

> The Hackathon IS NOT open to:
>
> Individuals who are residents of, or Organizations domiciled in, a country, state, province or
> territory where the laws of the United States or local law prohibits participating or receiving a
> prize in the Hackathon (including, but not limited to, the province of Quebec, ... China, ...)

The excluded-country list is long; the full verbatim list is preserved in `research/rules.txt`
(lines 123-124), including `province of Quebec` and `China`, plus sanctioned regions and any country
comprehensively sanctioned by OFAC.

> Organizations (including corporations, not-for-profit corporations and other nonprofit
> organizations, limited liability companies, partnerships, and other legal entities) that exist and
> have been organized or incorporated at the time of entry.

**What we do / what the entrant must confirm.** This submission is written as an **individual** entry
by an adult resident of an eligible country (the United States is on the eligible list:
`United States, Canada (excluding Quebec), ...`). The entrant must confirm, before submitting:
18+/age of majority, residence outside the excluded list, not employed by / affiliated with the
Promotion Entities, not a Judge or a Judge's employer, and no conflict of interest. Teams are capped at
three and each person may enter only one Project - this package assumes a single individual entry.
Because the rules exclude organizations from the open categories, the entrant does not submit on
behalf of a company.

## 3. What to build and technical requirements

> All submitted Skills must comply with the supported capabilities and technical requirements specified
> in the official documentation. Skills must follow the official Uliya Skill Development Standard and
> use supported UGOS CLI capabilities through registered expert agents. Custom executable scripts,
> general-purpose programming runtimes, and unauthorized direct access to NAS resources are not
> supported.

> Entrants are encouraged to use the AI NAS local AI model, but its use is not required. Properly
> authorized third-party models may also be used, subject to applicable rights, service terms, and the
> data restrictions outlined under Third Party Integrations.

**What we do.** The package is Markdown only, orchestrates only catalog-listed Actions through the
three registered experts (`photo-agent`, `document-agent`, `knowledge-agent`), uses no scripts at
runtime, no direct NAS access, no external model, and no external data flow. AI is the NAS local model
via the platform's own writing/vision Actions.

> An Entrant may build on an idea conceived before the Hackathon, but the submitted Skill and its core
> workflow must be newly developed during the Hackathon. Previously developed Skills or submission
> materials may not be reused. Properly authorized third-party development tools and resources may be
> used, subject to the technical requirements and applicable licenses. Round 2 Submissions must build
> on the same Project submitted in Round 1.

**What we do.** `story-reel` and all Round 1 materials were authored during the Round 1 Submission
Period (2026-10-22 through 2026-11-15). No prior skill or submission material is reused.

## 4. Round 1 submission requirements (PDF)

> Include a PDF answering the following questions. The ten substantive responses must not exceed 500
> English words in total. Team consent declarations, member names, electronic signatures, and
> third-party license information are excluded from this word limit.
>
> 1. One sentence: What does the Skill do?
> 2. Who is the target user and problem?
> 3. What is your proposed solution?
> 4. What is the Core User Flow?
> 5. What substantive difference does your idea offer compared with existing tools or conventional AI
>    solutions?
> 6. Which UGREEN AI NAS capabilities will be used, and at which step in the workflow?
> 7. What was your technical approach? Describe the planned Skill workflow, supported NAS CLI
>    capabilities, expert agent orchestration, required inputs, permissions, AI model choices, and data
>    handling, as applicable;
> 8. What is the current development status? Identify what was implemented already, not yet
>    implemented, or is pending NAS validation if selected to be a Finalist.
> 9. What is your final validation plan? Name two core test cases and one edge case to validate if
>    selected as a Finalist.
> 10. Are there any known limitations of your Project? Describe current known limitations, technical
>     risks, and any external dependencies.

From the hackathon submission page:

> Submit the Project Proposal as a separate PDF file no larger than 1 MB.

> Any third-party components must be identified, including their sources and applicable licenses.

**What we do.** `proposal/round1-proposal.pdf` answers all ten items in the same order and states the
word count on the page. The ten answers total **487 words** (machine-counted by
`scripts/make_proposal_pdf.py`, limit 500) and are the only material between the word-count markers.
The PDF is 14,526 bytes, well under 1 MB. The third-party/licensing/team/AI-drafting section is clearly
labeled as excluded, exactly as the rules allow, and it identifies the official Uliya Skill Kit (with
source), the UGOS capabilities used, that no other third-party components or data are used, and the AI
tools used and their principal uses.

## 5. Round 1 submission requirements (ZIP)

> Include a ZIP Initial Skill Package with the following items:
>
> Submit the initial version of your Skill as a ZIP file. The ZIP file must not exceed 10 MB for
> contest submission.
>
> The package must follow the official Uliya Skill Development Standard and include:
>
> SKILL.md (Required):
> The required entry point containing the Skill name, description, user goal, required inputs,
> supported CLI capabilities, expert orchestration workflow, and completion and failure handling.
> The file must include the following fortmat:
> - name: A lowercase, hyphenated name containing 2–64 characters.
> - description: A description of no more than 1,024 characters.
>
> Supporting References
> (Optional):
> Additional Markdown files under the references/ directory, each directly linked from SKILL.md.
>
> Additional Requirements
> The Initial Skill Package does not need to be fully installable or operational on UGREEN AI NAS at
> this stage.
> Local test results are optional. Executable scripts must not be included in the Skill package.
> Entrants are not required to submit demo videos, runtime screenshots, test reports, public
> repositories, Git histories, AI conversation logs, model weights, or training datasets during
> Round 1.
>
> The package must not contain real credentials, personal data, unauthorized third-party materials,
> malicious code, or functionality that enables undisclosed high-risk external access. Password
> protection that prevents review is prohibited.
>
> Round 1 does not require a separate code repository link, or a demo link/video.

From the hackathon submission page (stricter combined limits):

> The ZIP file and uncompressed package must each be no larger than 10 MB, with a maximum of 1 MB per
> file and 100 files. Separate manifests, scripts, executables, binaries, and other unsupported files
> are prohibited. Use placeholders for configuration examples; do not include real credentials, personal
> data, or API keys.

> In SKILL.md or its linked references, disclose third-party components and open source libraries,
> their sources and licenses, the principal functionality developed for this Hackathon, and AI tools
> used and their principal uses.

**What we do.** `pre-test-skill-package.zip` has `SKILL.md` at the ZIP root and three linked Markdown
references, no manifests/scripts/binaries. Measured: ZIP 7,284 bytes, uncompressed 16,332 bytes, 4 files,
largest file 9,422 bytes. Third-party and AI-tool disclosures are in
`skill/references/disclosures.md`, linked from `SKILL.md`. No credentials, no PII, no third-party kit
files (the kit is gitignored and not zipped). `scripts/check.sh` and `scripts/package.sh` run the
official checker and enforce every size/file limit; the ZIP is also unpacked and re-checked.

## 6. Judging criteria (Round 1 and Round 2)

> Judging Criteria (Rounds 1 and 2): Entries will be judged on the following equally weighted criteria
> (the "Judging Criteria"), according to the sole and absolute discretion of the Judges:

> User Value:
> Whether the Skill addresses a clear user problem and gives users a clear workflow, useful feedback,
> and a meaningful result.

> Innovation & Differentiation:
> Whether the Skill offers a substantive new function, interaction, or workflow that differs from
> conventional AI tools and existing solutions.

> Technical Quality:
> Whether the Skill demonstrates a sound orchestration approach, appropriate use of supported CLI
> capabilities and expert agents, proper handling of permissions and errors, and reliable execution
> appropriate to its development stage.

> AI NAS Fit & Validation:
> Whether the Skill makes meaningful use of UGREEN AI NAS capabilities, including relevant local data,
> storage, computing, privacy, or other supported capabilities, rather than merely running on NAS.

> Because Entrants do not have NAS access during the Round 1 Submission Period, Judges will evaluate
> each criterion based on the Round 1 Submission materials, including the PDF and ZIP Pre-test Skill
> Package, and the Project's proposed functionality, planned use of UGREEN AI NAS capabilities, and
> validation plan. A lack of NAS runtime evidence will not, by itself, make a Submission ineligible or
> lower its Round 1 score.

> Judges will review the Round 1 PDF and ZIP Pre-test Skill Package. No website, demo link, or test
> build is required.

**What we do.** The four criteria are addressed directly: User Value in answers 1-4 and the user story;
Innovation & Differentiation in answer 5 (evidence-grounded + approval-gated + NAS-local versus gallery
search and cloud tools); Technical Quality in answers 6-8 and the validated static package; AI NAS Fit &
Validation in answers 6, 8, 9 and the Round 2 plan (local library, local AI, two core cases + one edge
case). Round 1 needs no runtime evidence; the proposal marks pending items honestly instead of claiming
NAS validation.

## 7. Round 2 requirements (finalists only)

> The Final Skill Package must install and run consistently in the assigned UGREEN AI NAS environment.
> It must function as shown in the video and described in the documentation. (The Skill package must
> follow the official Uliya Skill Development Standard and use SKILL.md as its required entry point. It
> may include supporting Markdown files under references/, each directly linked from SKILL.md. Separate
> manifests, scripts, executables, binaries, and other unsupported files must not be included.）

> Finalists are responsible for backing up any data they wish to retain, including Skill runtime logs
> and test data, before their assigned testing period ends. Data deleted during the reset process
> cannot be recovered.

> Each Finalist will receive one assigned testing day of free, exclusive remote access to an assigned
> UGREEN AI NAS iDX6011 Pro (64GB version), from 12:00 a.m. to 11:59 p.m. PT, to conduct full testing of
> their Skill. UGREEN will provide the assigned testing date, account activation and expiration times,
> and connection instructions. Credentials are valid only for the assigned testing day.

> Provide a link to a public YouTube video of no more than 3 minutes, using English narration or
> complete English subtitles. Record the Skill operating on your assigned UGREEN AI NAS during your
> assigned testing day, and show its core workflow, key capabilities, and actual results.

From the rules on the video:

> should be less than three (3) minutes. Judges are not required to watch beyond three minutes
>
> must include footage that shows the Project running in the UGREEN AI NAS test environment and
> narration explaining the Skill's core workflow, key capabilities, and actual results.
>
> must be uploaded to and made publicly visible on YouTube and a link to the video must be provided on
> the submission form on the Hackathon Website; and
>
> must not include third party trademarks, or copyrighted music or other material unless the Entrant
> has permission to use such material. Entrants may show the Sponsor's trademarks and materials that the
> Sponsor provides for the Hackathon.

**What we do.** `ROUND2-PLAN.md` covers the assigned-day schedule, install/validation steps, two core
test cases + one edge case, evidence backup before reset, video recording with an English script, and
the Nov 30 checklist. Round 2's final package is the same Project as Round 1 and the same Skill
structure.

## 8. Ownership, third-party, and originality

> Submission ownership
> Be the original work of the Entrant, be solely owned by the Entrant, and not violate the Intellectual
> Property rights of any other person or entity.

> Your Submission must: (a) be your (or your Team, or Organization's) original work product; (b) be
> solely owned by you, your Team, your Organization with no other person or entity having any right or
> interest in it; and (c) not violate the intellectual property rights or other rights including but not
> limited to copyright, trademark, patent, contract, and/or privacy rights, of any other person or
> entity.

> Properly licensed third-party components and general technical assistance through the UGREEN
> Community are permitted; **a person outside the team may not develop the Project or create its
> submission materials for the Entrant.** An Entrant may submit a Submission that includes the use of
> open source software or hardware, provided the Entrant complies with applicable open source licenses
> and, as part of the Submission, creates software that enhances and builds upon the features and
> functionality included in the underlying open source product.

> An Entrant may use third-party SDKs, APIs, components, and data only when it has the right to do so
> and complies with the applicable terms and licenses. The Proposal must identify third-party
> components, their sources and applicable licenses, and any external services and data flows. The
> Entrant bears responsibility for infringement arising from its Project or use of third-party
> material.

> A Project must not have been developed, or derived from a Project developed, with financial or
> preferential support from the Sponsor or Administrator. Such Projects include, but are not limited
> to, those that received funding or investment for their development, were developed under contract,
> or received a commercial license, from the Sponsor or Administrator any time prior to the end of
> either Submission Period.

> All Submissions remain the intellectual property of the individuals or organizations that developed
> them. By submitting an entry, entrants agree that the Sponsor will have a non-exclusive license to use
> such entry for judging the entry. Entrants agree that the sponsor and Devpost shall have the right to
> promote the Submission and use the name, likeness, voice and image of all individuals contributing to
> a Submission, in any materials promoting or publicizing the Hackathon and its results, during the
> Hackathon Period and for three years thereafter.

**What we do.** The original work is the orchestration design and its written specification. The
official Uliya Skill Kit is used only as an authoring/validation tool, is not redistributed, and is not
part of the submitted package. No third-party data, model, SDK, or service is used. No sponsor funding
or preferential support was received. The entrant owns the submission and grants only the non-exclusive
judging/promotion license that the rules require by entering.

### How the entrant remains the author/director while using AI as a drafting tool

The rules' restriction is on a **person outside the team** developing the Project or creating its
submission materials. The official starter kit, published by the Sponsor to guide the Hackathon,
explicitly instructs entrants to:

> Use the official UGOS Skill Creation Tool with your preferred AI assistant to create skills that can
> be used on UGREEN NAS / Uliya.

> The tool currently supports WorkBuddy, Claude, and Codex.

So the Sponsor's own workflow expects an AI assistant to be part of authoring. Our compliance posture:

1. **The entrant sets every product decision**: the skill's purpose, target user, scope rules, approval
   gate, chapter constraints, failure behavior, and the two core test cases and edge case.
2. **The entrant reviews and owns every statement**: the Skill, proposal, README and submission text
   are read and edited by the entrant before upload; unreviewed AI output is never submitted.
3. **No human outside the team contributes**: no hired writer, no third-party developer, no copied
   skill, and no reused prior submission material.
4. **AI use is disclosed** in the proposal's excluded third-party section and in
   `skill/references/disclosures.md` (AI tools used and their principal uses), as required by the
   hackathon submission page.
5. **The AI is a tool, not an author**: it drafts and checks text at the entrant's direction. The
   entrant is the author and director of the Project for the purposes of the rules.

The one **UNVERIFIED** point: the rules and pages do not define a formal threshold for "AI-assisted"
versus "AI-generated" development, and no separate AI-use declaration field is documented on the public
submission page. We disclose it in both required places rather than assume it is unnecessary.

## 9. Language

> Registration, submitted materials, and entrant communications must be in English. Demo videos must use
> English narration or complete English subtitles.

**What we do.** Every artifact in this package is English. The Round 2 demo video script is English and
the plan requires English narration plus full English subtitles.

## 10. Other compliance notes

- **No accounts, registrations, submissions, or organizer contact were performed by the authoring
  agent.** The repo contains no Devpost credentials and no personal data of any third party. Devpost
  account work is a user-only step; see `DEVPOST-SETUP.md`.
- **Downloaded official tooling** lives under `tooling/uliya-skill-kit/` and is gitignored and excluded
  from the ZIP; it is not redistributed.
- **Privacy:** the Skill is designed to process only the user's authorized local library and to send
  nothing external. The package contains no real data, no sample photos, no personal names.
- **Password protection:** none; the ZIP is reviewable by judges.
- **Round 1 materials** are kept after submission (`Do not delete your Round 1 Submission materials.`).
