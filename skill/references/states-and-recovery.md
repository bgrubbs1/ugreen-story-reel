# Delegation states and recovery

Use this reference whenever a delegated expert returns a state other than `completed`, or when a result is empty or partial.

## State handling

| State | Meaning | What the Skill does |
| --- | --- | --- |
| `completed` | The expert finished and returned a real result. | Accept the real result and continue with the next step that depends on it. |
| `failed` | The expert could not finish. | Report the failing step and the returned reason. Keep earlier verified results. Stop dependent steps. Do not run a state change again automatically. |
| `cancelled` | The run or the approval was cancelled. | Report cancellation, list steps already completed, confirm the library and notes were not changed further, and stop. |
| `waiting_user` | The user still has to answer a question or approve the draft. | Present the question or the draft and stop. Never treat this state as success. |
| `waiting_approval` | The gateway or child workflow is waiting for approval. | Report that approval is pending. Never claim the album or document exists until the state becomes `completed`. |

## Partial results

- Keep every verified partial result and label it as partial.
- Present only chapters that are backed by evidence; mark the rest as unavailable.
- Name the missing photos, clusters or fields so the user knows what is missing.
- Do not continue a dependent step when its required input is missing.

## Empty results

- Discovery with no matching photos: report that no photos matched the scope and stop.
- Evidence with no usable timestamps or locations: ask the user whether to continue with a smaller visual-only story, and stop if the user declines.
- Narrative with no usable evidence: do not present invented chapters; report that the story cannot be grounded.

## Recovery rules

- A user edit to a chapter returns the run to the narrative step, not to discovery, unless the user changed the memory scope.
- A change to the memory scope returns the run to discovery.
- Retrying a read-only step once is allowed when the failure is transient and the reason is reported. Retrying a state-change step requires a fresh user approval.
- Approval is per run. A new run needs a new approval.
