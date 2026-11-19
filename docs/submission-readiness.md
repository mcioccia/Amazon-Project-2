I used OpenAI Codex to audit the repository, rerun existing checks, compare the requirements and organize the remaining work. Matt owns the analysis and decision; this audit does not certify personal authorship or promise a grade.

Educational purposes only. Not financial or investment advice.

# Project 2 submission readiness — November 19, 2026

**The core app and numerical evidence pass the existing checks. The submission is not yet fully ready: YouTube transcripts are not enabled, and material spoken/caption discrepancies still need resolution.** The repository is now public and readable while signed out. No hosting deployment or another investment model is needed to meet the listed base requirements.

Requirements checked against the current [Project 2 page](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/project-2-investment-management-application.md) and [student checklist](https://github.com/CinderZhang/FIN43900-Fall2026/blob/main/projects/major-project-student-checklist.md). Brightspace determines the due date and points; its submission page was not inspected.

## What passed

| Requirement | Evidence and status |
|---|---|
| Runnable app and stranger's setup route | README and pinned requirements present. Existing AppTest runs passed for base, changed window, infeasible reserve, missing vintage and reset. An earlier clean environment install and partner fresh-download success are recorded; this audit reused the installed environment. |
| Mandate | Six funds, 7.49% first-year net target, 10% estimated volatility ceiling, equal-weight benchmark, reserve and CPI rules, costs, horizon and review triggers documented. |
| Two baselines plus constrained portfolio | All three displayed with distinct mandate verdicts; independent enumeration reproduces the base winner and 655 feasible mixes from 53,130 candidates. |
| Point-in-time signal | CPIAUCSL archived vintages, same-vintage inflation calculation, dates, units, source URLs and limitations recorded. The signal floor is slack at base; no timing advantage is claimed. |
| Stress and stop rules | Estimate, window, cost, reserve and lag stresses reproduce saved output. The 90% BIL minimum pauses allocation; missing eligible CPI also pauses. |
| Locked record | Original 15 bp prediction commit ed8b8f9 at 00:41:21 precedes the 00:43:53 run; result committed separately. Original prediction text is unchanged. This checks chronology, not how the student authored it. |
| Recommendation | Paper pilot with 65–85% BIL across tested complete mixes, corresponding 35–15% equities, monitoring, stop/reconsideration conditions and committee ask. |
| Disclosures | README and memo open with AI role/ownership and education/no-advice statements. Transcript text contains opening disclosures; full spoken delivery still needs review. |
| Source check and arithmetic | Two QQQ source screenshots, calculator evidence and Matt's unchanged response recorded. His reported source-access date is recorded separately from what the screenshots establish. |
| Training and software validation | All 43 published comparisons passed through verify.py; independent covariance/grid, failure, output-reproduction and app-interaction checks passed again. |
| Files and access | All required files present; 198 existing local Markdown file links resolved before documentation cleanup. No common credential-pattern matches or sensitive filenames in the 74 tracked files scanned. Public GitHub access verified; this limited scan is not a security certification. |

Base reproduced: **7.498% first-year net estimate, 7.241% estimated annual volatility, 65% BIL, PASS**. Equal weight fails at 12.138% volatility; inverse volatility fails the return target at 3.775% net. The 15 bp saved result is 7.503% net, 7.245% volatility, 65% BIL. [Saved output](../outputs/committee-run.json) · [Cost comparison](cost15-prediction-comparison.md) · [Audit evidence](../outputs/submission-audit.json).

## Required work before submission

### 1. Resolve material video wording and align the transcripts

Replay these passages. The following are the correct project facts; the edited text alone does not prove the recording says them.

| Recording | Approximate time from supplied SRT | Fact to check |
|---|---|---|
| Video 2 | 00:27 | Information cutoff is **October 30**, not October 13. |
| Video 2 | 02:36 | **10 bp = 0.001 as a decimal = 0.1%**, not 0.001%. |
| Video 2 | 03:19 | **655** passing mixes, not 65. |
| Video 3 | 00:16 | Information cutoff is **October 30**, not October 13. |
| Video 3 | 01:49 | BIL stays at **65%**, not 15%. |
| Video 3 | Opening | Matt confirms the full opening statement is in the recording, but the supplied SRT begins mid-sentence. Align the caption start with the actual video. |

Matt confirmed at least one Video 2 spoken error. If the audio is correct and only recognition was wrong, correct the captions. For a spoken numerical error, repair that short passage or add a clear correction to the video, then make the transcript and captions accurately represent the resulting recording. Keep the original caption evidence and correction notes. Do not present a script substitution as verbatim audio. The exact repair approach is a recommendation to eliminate a material conflict; the course requires accurate substantive terms/numbers and consistent submission materials.

### 2. Enable YouTube transcripts on all three videos

All three players still reported **Subtitles/closed captions unavailable** during this audit. Repository .txt files alone do not meet the explicit requirement for YouTube links with transcripts enabled.

In **YouTube Studio → Subtitles → select video → English → Add**, upload the reviewed SRT with timing, or use an accurate spoken transcript and auto-sync. Review the track and save/publish it. If using transcript text, exclude the unspoken editorial note at the end of Videos 2 and 3. Check CC and Show transcript on the signed-out watch page. [Official YouTube caption instructions](https://support.google.com/youtube/answer/2734796?hl=en).

| Video | Current local caption file | Status |
|---|---|---|
| 1 | [captions-video-1-corrected.srt](captions-video-1-corrected.srt) | Prepared; review against playback, then publish. |
| 2 | [captions-video-2-review.srt](captions-video-2-review.srt) | Review draft; resolve the three numerical passages before finalizing. |
| 3 | [captions-video-3-review.srt](captions-video-3-review.srt) | Review draft; resolve numbers and align the full opening. |

### 3. Do one full playback review

Watch all **11 minutes 19 seconds** once. Confirm your face remains visible, audio is understandable, both disclosures are spoken at the opening of each video, and captions match. Video 3 must show the live app at the start; its opening does. Opening webcam visibility was observed for all three, but continuous visibility and the complete narration have not been independently verified.

| Video | Runtime | Maximum | Current access |
|---|---|---|---|
| [Video 1](https://youtu.be/e79Ix9xr71k) | 2:36 | 3:00 | Unlisted; signed-out playback checked |
| [Video 2](https://youtu.be/YfrNEF4OK6g) | 4:32 | 5:00 | Unlisted; signed-out playback checked |
| [Video 3](https://youtu.be/9RYrqkSZCaw) | 4:11 | 5:00 | Unlisted; signed-out playback checked |

If a video is replaced, update its link, runtime and transcript in the manifest. Recheck limits after any spoken correction.

### 4. Submit the final package in Brightspace

After video corrections are finalized and pushed, use the actual assignment header for the deadline. Submit:

- Repository: [Amazon-Project-2](https://github.com/mcioccia/Amazon-Project-2).
- Attach the same [decision-memo.md](decision-memo.md) and [validation-and-ai-use.md](validation-and-ai-use.md) that appear in the repository.
- Supply [manifest.md](manifest.md), with its GitHub file links, video URLs, titles, durations, timestamp indices and access status. Attach the Markdown manifest as well so the locations remain easy to follow.
- Supply all three YouTube links above. Transcript links already appear in the repository and manifest; the course permits linking them there instead of separate transcript attachments.
- Submit and save the Brightspace confirmation receipt.

For Project 2, Edition A, Edition B and Research-Evolution are not submitted. The submission uses Markdown documents rather than the Project 1 PDFs. A hosted deployment is optional; the runnable app and setup instructions are already included.

## Ways to strengthen the evidence further

These do not require another full rebuild or rewriting the locked prediction.

- Ask Aj to complete the existing cold-run report with the actual app-launch command, where he read the result, whether he used only the README, and one control's old/new values and resulting verdict. The successful fresh download, 15 minutes, no errors and matching base values are already documented. Do not invent a commit ID or changed-control observation.
- In your own dated follow-up below the highest-risk reflection, acknowledge that the observed 15 bp risk was **7.245%**, rather than the **7.6%** mentioned in that later reflection, and that BIL stayed **65%**. The technical notes already explain this; a personal acknowledgment makes the reasoning clearer. Preserve the original **7.7% pre-run forecast**, its commit and the original **50%** trigger; the later **55%** review trigger is separately documented.

## Audit scope and fixes

This audit corrected stale source-check, video and repository-access statuses, preserved Matt's supplied paragraph exactly, replaced rehearsal instructions in the README with the completed video table, and made local manifest locations explicit GitHub links. It did not alter the model, input data, archived results, original prediction or personal reflection. All required output numbers remain unchanged. Tests used the existing local environment, not a new partner run. The audit does not certify AI-off authorship, full audio accuracy, future investment performance or a grade.
