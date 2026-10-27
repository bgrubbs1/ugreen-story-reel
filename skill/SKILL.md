---
name: story-reel
description: A chaptered, narrated memory album built only from a user's own NAS photos in a chosen period, event, people or place, with the proposed chapters shown for approval before any album or story document is created. Use when a user asks to turn family photos into a memory story, a narrated recap or a memory album.
---

# Goal

Give the user a finished memory story from their own photo library: 2-5 factual chapters with short titles, highlights and captions, presented first as a draft, then, after the user approves, one photo album plus one saved story document. The whole story stays inside the user's NAS photo library; nothing is uploaded and no memory is described unless real photo evidence supports it.

# Required input

Collect only what the workflow needs, in one short conversational pass:

- Required: the memory scope, either a date range (start and end) or an event or theme phrase.
- Optional: people, place, tone, and the output choice (album only, story document only, or both). If the output choice is missing, propose both and let the user confirm.
- Ask at most one clarifying question when both the scope and the output choice are missing. Do not ask for CLI parameters, paths or internal identifiers; the delegated experts resolve those.

Fixed scope rules:

- Only the user's authorized photo library. Never widen the date range, people, place or theme beyond what the user asked for.
- Never invent photo content, names, places, dates, events or captions. Every chapter, highlight and caption must trace to evidence returned by the photo expert.
- At most one album and one story document per run.
- Tone only changes wording, never facts.

# Generation-time capability evidence

- `ug-photo` → `photo-agent`
- `ug-document` → `document-agent`
- `ug-knowledge` → `knowledge-agent`

Actions used, per the catalog: `ug-photo` `search-picture`, `search-classify`, `search-hint`, `meta`, `vision-ocr`, `vision-vlm`, `create-album`, `create-album-condition`; `ug-document` `writing`, `qa`; `ug-knowledge` `save-text`. Read-only actions are discovery and drafting. State-change actions are `create-album`, `create-album-condition` and `save-text`; `writing` carries gateway approval. This Skill delegates through the registered experts only and never calls `cli.invoke` directly.

# Orchestration

Run the steps in order. Each delegation is a single standard command; pass only the real result of the previous delegation into the next one.

## Step 1: discover and cluster photo evidence (photo expert)

`delegate --target photo-agent --instruction 'Discover and cluster photo evidence for a family memory story in the user authorized NAS photo library. Memory scope: the date range or event or theme the user gave. Optional filters: the people and place the user named, or none; tone is not a photo filter. Use search-picture for date, place and album filters, search-classify and search-hint for people, event and theme context, meta for timestamps, locations and camera data, and vision-ocr or vision-vlm only when caption or visible content evidence is needed. Return 3 to 8 candidate clusters, each with real photo count, date span, locations, captions and a one-line factual summary. Use only real NAS content. If no photos match, return an empty result and state it plainly. Do not create or modify any album.'`

Accept the step only when the result state is `completed` and it lists real photos or clusters. If it returns an empty result, report that no photos matched the scope and stop; never substitute other photos or widen the scope.

## Step 2: draft the chaptered narrative (document expert)

`delegate --target document-agent --instruction 'Write a factual chaptered memory narrative from the photo evidence list supplied in this instruction. Use only that evidence: its real dates, locations, people, captions and photo counts. Produce 2 to 5 chapters. For each chapter return a short title, a one-sentence highlight and a two to three sentence caption in the tone the user chose, defaulting to warm and plain. Never invent names, places, events, dates or photo content, and never add facts that are not in the evidence. Mark any gap as unknown instead of filling it. When useful, use the document question-answering action to check that each chapter claim is supported by the evidence, and drop any unsupported claim. Return plain text chapters only and do not save or write any file.'`

Pass in the verified evidence from step 1. If this delegation is not `completed`, report the failure and stop; do not present invented chapters.

## Step 3: present the draft and wait for approval

Show the user the proposed story: chapter titles, one-line highlights, photo counts, the album or document names, and the fact that two state changes will follow. Ask the user to approve, edit or cancel. This turn is `waiting_user` or `waiting_approval`; it is not a success. No state-change action may run before explicit approval. If the user edits a chapter, return to step 2 with the new constraint. If the user cancels, stop and leave the library unchanged.

## Step 4: create the approved album (photo expert)

Only after approval:

`delegate --target photo-agent --instruction 'Create one photo album for the approved memory story from the real photo evidence returned by the discovery step in this run. Use the approved story title and date span as the album name. Use create-album with the approved query, or create-album-condition with the approved date range, people and place when those values are exact. Add only photos from the approved evidence list and never add unrelated photos. This action changes the library and requires the platform workflow approval; request that approval and report the returned state without assuming success. Return the real album identifier and the final photo count.'`

## Step 5: save the approved story document (knowledge expert)

Only after approval. Steps 4 and 5 may run in either order:

`delegate --target knowledge-agent --instruction 'Save the approved memory story as a Markdown text document in the user knowledge space. Content: the approved chapter titles, highlights and captions, plus the memory scope, date span and photo count from the real evidence. Suggest a filename built from the story title and date span. Use save-text only. This action changes storage and requires the platform workflow approval; request that approval and report the verified output file without assuming success. Do not invent content and do not overwrite a different existing document.'`

# Completion and failure

- `completed`: report the real chapter list, the real album identifier and photo count, and the verified story document path. Report only what the expert returned.
- `failed`: report which step failed and why, keep any earlier verified results, and stop any step that depends on the missing result. Do not retry a state change automatically.
- `cancelled`: report that the run was cancelled, name the steps already completed, and confirm that no further album or document changes were made.
- `waiting_user`: report that the draft and the approval question are waiting for the user. Do not begin any state-change step.
- `waiting_approval`: report that the approval step is pending with the gateway or child workflow. Do not claim the album or document exists until the state becomes `completed`.

Empty result: if discovery returns no photos, or every photo lacks usable evidence, report the empty result and stop. Partial result: present only the chapters backed by evidence, mark the rest as unavailable, and state exactly which photos or clusters were missing. Dependent steps stop when their required input is unavailable. Never invent NAS content to fill a gap.

# Approval and data handling

The three state-change actions (`create-album`, `create-album-condition`, `save-text`) carry workflow approval, and `writing` carries gateway approval. The child expert workflow and the platform gateway request and enforce that approval; this Skill only asks the user to approve the proposed story and then reports the real state. Credentials are never requested, stored or embedded.

All processing uses the user's authorized library, the NAS local AI model, and the registered experts. Photo files stay on the NAS. No photo, caption or story text is sent to an external service, and no third-party model or dataset is used beyond the NAS itself. The story document is saved only where the user approved.

# References

Read these supporting Markdown files when the matching situation applies:

- [Photo evidence and anti-invention rules](references/photo-evidence-rules.md): read before step 1 and before accepting any photo evidence.
- [Delegation states and recovery](references/states-and-recovery.md): read when any delegation returns a state other than `completed`, or when results are empty or partial.
- [Disclosures and principal functionality](references/disclosures.md): read when reviewing the package, its third-party components or the AI tools used to draft it.

# Boundary

This Skill orchestrates registered experts. It does not execute NAS commands itself, does not access files directly, does not run scripts, and does not claim NAS execution from local generation or static checks. It stays inside the capabilities listed in the catalog and reports unsupported requests as unsupported.
