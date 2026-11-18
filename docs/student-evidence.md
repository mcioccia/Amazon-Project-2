I used OpenAI Codex to organize this evidence form. My personal observations and AI-off responses will be entered by me.

This is an educational course project. It is not financial or investment advice.

# Personal evidence

## Source check

**Status: source screenshots received; Matt's own monthly-return calculation and interpretation pending.**

On November 18, 2026, Matt supplied two screenshots of Yahoo Finance's QQQ daily historical prices. The images are preserved unchanged below. Codex transcribed the visible values and compared them with the archived input file; this transcription is not Matt's independent arithmetic.

[Yahoo page shown in both screenshots](https://finance.yahoo.com/quote/QQQ/history/?period1=1785542400&period2=1790812800&frequency=1d) · [Archived prices](../data/prices.csv) · [Original source ledger](../data/source-ledger.json)

| Observation date | Screenshot Adj Close (USD/share) | Archived QQQ adjusted close (USD/share) | Comparison |
|---|---:|---:|---|
| August 31, 2026 | 716.01 | 716.013916015625 | Matches when rounded to cents |
| September 30, 2026 | 739.77 | 739.77001953125 | Matches when rounded to cents |

The September image identifies QQQ, USD, Daily frequency, column headings and the September 30 row. The August image shows the August 31 row at the same page URL; column positions are interpreted using the first image. August's unadjusted Close is 716.76, whereas its Adj Close is 716.01. The adjusted-close field is the one the model uses.

| Field | Evidence / remaining personal entry |
|---|---|
| Date received | November 18, 2026; exact capture/access date is not visible and remains unconfirmed |
| Source and input | Yahoo Finance QQQ daily historical data; adjusted close, USD per share |
| Values visible in Matt's screenshots | August 31: 716.01; September 30: 739.77 |
| Comparison performed by Codex | Both observations match the October 22 archive to the source's displayed cent precision |
| Matt's independent calculation | Pending: use (September Adj Close / August Adj Close - 1) x 100 and retain calculator or handwritten evidence |
| Matt's explanation of any match or difference | Pending personal response; no difference visible at cent precision |
| Effect on Matt's decision | Pending personal response |

This sample supports two month-end observations. It does not verify every fund or date, the entire annual estimate, or future performance. QQQ's estimated return affects the target constraint, so this check concerns a portfolio input. The separate [automated CPI comparison](../outputs/source-check.json) supplies additional evidence; the CPI reserve floor is slack at base.

### Screenshots supplied by Matt

Original screenshots are retained without editing. The AI disclosure and educational-use notice at the top of this record apply to the organization and explanation of these attachments.

**September 30 observation, including column headings**

![QQQ September 30 daily historical prices showing Adj Close of 739.77](evidence/qqq-source-2026-09-30.png)

**August 31 observation on the same historical-data page**

![QQQ August 31 daily historical row showing Adj Close of 716.01](evidence/qqq-source-2026-08-31.png)

File fingerprints identify the exact attachments preserved here; they do not establish when the screenshots were captured.

| File | SHA-256 |
|---|---|
| qqq-source-2026-09-30.png | edbfc331736c756de5c98c8a60fdbe5ffecbc6cb0843574b59515be82f90e8fc |
| qqq-source-2026-08-31.png | 4272cb7b5f55ab2674311f9f2cc073d4efe01abade3d7a8fbe7dd24ceea0e669 |

## Highest-risk claim and three possible failures

Complete this section yourself with AI closed, following the instructor’s feedback. Name the claim in your own words and explain how it could fail. The saved code tests are separate evidence.

| Field | Matt’s response |
|---|---|
| Highest-risk claim I am making | Pending |
| Evidence supporting it | Pending |
| Failure possibility 1 and how I would detect it | Pending |
| Failure possibility 2 and how I would detect it | Pending |
| Failure possibility 3 and how I would detect it | Pending |
| My conclusion and the condition that changes it | Pending |

Complete the [Locked Changed-Input Record](validation-and-ai-use.md) with a genuinely new scenario, commit it before running, and preserve the outcome afterward.

## Recording evidence

Keep your face visible in every video. Record from the final app and use the two disclosures at the start. Correct the transcript after listening to the actual recording.

| Item | Status |
|---|---|
| Video 1, at most 3 minutes | Link and corrected transcript pending |
| Video 2, at most 5 minutes | Link and corrected transcript pending |
| Video 3, at most 5 minutes, opens on the live app | Link and corrected transcript pending |
| Instructor access to repository and videos | Unconfirmed |
