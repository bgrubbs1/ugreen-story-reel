# Photo evidence and anti-invention rules

Use this reference before delegating photo discovery and again before accepting the evidence returned by `photo-agent`.

## Evidence the photo expert must return

For each candidate cluster, the real result must contain:

- real photo count and the identifier range the expert returned;
- the date span taken from real timestamps;
- the locations the expert resolved from real photo metadata;
- captions or text only where the expert extracted them from real metadata or OCR;
- a one-line summary that adds no facts beyond the fields above.

Reject any cluster that has no photo count, no date span, or only a summary with no underlying photos.

## Which Action to request

- Date range or place: `search-picture` with the real start and end values.
- People, pets or event/theme context: `search-classify` and `search-hint`, then `search-picture` with the resolved identifiers returned by the expert.
- Timestamps, locations and camera data: `meta`.
- Visible text in photos: `vision-ocr` only when text evidence is needed.
- Visible content description: `vision-vlm` only when a caption is needed and the user authorized content reading.

The parent Skill does not choose private parameters. State the user-facing scope and let the expert select the Action and its parameters.

## Anti-invention rules

- Every chapter title, highlight and caption must be supportable from the returned evidence list.
- A gap in evidence is reported as unknown or unavailable, never filled with a plausible detail.
- Do not rename a person, place or event that the user named; keep the user's real entities.
- Do not merge two different periods or places into one chapter to make a story smoother.
- Do not describe feelings or motives of people in the photos; describe only what the evidence shows.
- If the photo expert returns an empty result, report that no photos matched and stop. Do not retry with a wider scope and do not substitute another album or data source.

## Chapter constraints

- Between two and five chapters per story.
- Chapters are ordered by the real date span, earliest first.
- Each chapter covers a contiguous real date range and at least one real photo.
- The final story includes the overall date span, total real photo count and the memory scope the user gave.
