I used OpenAI Codex to correct transcription errors and compare the caption text with the saved code and results. The analysis and decision remain Matt's.

Educational purposes only; not financial or investment advice.

# Video 2 caption review — November 19, 2026

**Review draft, not yet the final submission transcript.** Matt supplied the recorded video's SRT. The [original](evidence/video-2-original.srt) is preserved unchanged. [Proposed corrected captions](captions-video-2-review.srt) and [proposed readable transcript](transcript-video-2-review.txt) retain all 102 original cue numbers and timestamps. The last cue ends at 00:04:30,863; this does not establish the full video runtime.

Finance terms corrected include annualizes, covariance, archived vintages, one-way turnover, search, inverse volatility and constrained mix. The recorded opening and transitions, two-decimal turnover of 48.33%, the brief restart before the verdict, and final funding wording are retained. Grammar and punctuation were lightly cleaned, without replacing the entire recording with the rehearsal script.

## Three passages requiring playback confirmation

| Time / cue | Supplied SRT | Correct value in the script and saved model | Status |
|---|---|---|---|
| 00:27 / 12 | October 13th | October 30th, 2026 | Proposed correction; confirm what was spoken |
| 02:36 / 61 | 10 basis points becomes 0.001% | 10 basis points = 0.001 as a decimal = 0.1% | Proposed correction; confirm what was spoken |
| 03:19 / 77 | 65 passing candidates | 655 passing candidates out of 53,130 | Proposed correction; confirm what was spoken |

The review drafts use the script/model values in this table. They are **not ready for upload** until Matt confirms whether these are caption recognition errors or spoken mistakes. If a value was spoken incorrectly, keep an honest record of the spoken error and record/edit an audible correction rather than silently making the transcript claim different speech. Any video edit may require new caption timings.

## Numerical evidence

- Base information cutoff: 2026-10-30 in analysis.py and the saved committee run.
- Base annual risk: 7.240552784%, displayed as 7.241%.
- Base one-way turnover: 48.333333333%, consistent with 48.33% in the captions.
- Switching cost: 10 / 10,000 = 0.001, or 0.1%; cost on $100,000 at base turnover = $48.33.
- Base eligible mixes: 655. Full grid size: 53,130.
- Changed-case risk: 7.244615791%, displayed as 7.245%.
- CPI year-over-year change: 3.717250844%, displayed as 3.72%.

Sources: [base output](../outputs/committee-run.json), [15 bp output](../outputs/cost15-changed.json), [calculation code](../analysis.py), [word-for-word rehearsal script](video-2-word-for-word-script.md).

No audio or video was supplied for this review. Playback, webcam visibility, synchronization, complete runtime, YouTube access and published captions remain unverified. Final filenames after resolution: captions-video-2-corrected.srt and transcript-video-2.txt.
