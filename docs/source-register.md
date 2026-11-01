# HSC 2026 source register

Research scope: Bangladesh's nine general education boards only. Madrasah and Technical are excluded from the institution-level study and from nine-board comparisons.

## Verified public result sources

| Source | URL | What it supports | Status / caveat |
|---|---|---|---|
| Inter-Education Board Coordination Committee result system | https://www.educationboardresults.gov.bd/v2/home | Board, exam, year, result type, EIIN, district and centre fields; CAPTCHA is present | Official government-hosted result form. EIIN/institution workflow is visible; CAPTCHA must not be bypassed. |
| eboardresults.com | https://www.eboardresults.com/v2/home | Common result form with EIIN input | Operational public portal; independently verify provenance and terms before automated use. |
| Dhaka Board result portal | https://result.dhakaeducationboard.gov.bd/v2/home | Dhaka-specific result form with EIIN field | Board-specific official subdomain; CAPTCHA present. |
| Chattogram Board institution result | https://hscresult.bise-ctg.gov.bd/h22_31_x1_26/individual/index.php | Institution-wise / EIIN-wise HSC 2026 results | Board-specific portal; inspect its current form and terms before collection. |
| Cumilla Board institution result | https://hscresult.comillaboard.gov.bd/EIIN/index.php | Institute-wise HSC-2026 result page | Board-specific result page discovered; validate current accessibility and output. |
| BANBEIS college files | https://banbeis.gov.bd/pages/files/6919975c933eb65569ddc4e2 | Official college list and school-and-college list downloads | Candidate authoritative source for institution universe/EIIN mapping. Download and inspect file before using; page does not itself establish the current file's completeness. |
| BANBEIS downloads | https://banbeis.gov.bd/pages/downloads | Lists college-related downloads | Official catalogue; locate exact downloadable file and record its publication date/version. |

## HSC 2026 nine-board aggregate (provisional)

A BSS report published 31 October 2026 states that the nine general education boards had:
- Appeared: 1,048,530
- Passed: 541,249
- Pass rate: 51.62%
- GPA-5: 35,948

Source: https://www.bssnews.net/news-flash/440327

This is recorded in `data/processed/hsc_2026_nine_general_boards_baseline.csv` as a provisional secondary-source baseline, not an official raw dataset. A second contemporary news report gave a conflicting appeared-candidate figure (1,069,714) while reporting the same nine-board pass rate and GPA-5 count. Resolve this discrepancy against the Ministry/Inter-Education Board Coordination Committee's consolidated statistics or the nine individual board result statistics before final publication.

## Collection constraints

- Institution-level data should be aggregate only; do not collect student-level records.
- Preserve the source URL, retrieval timestamp, extraction method, and a copy/hash of each source artifact where permitted.
- Missing values are unknown, not zero.
- Do not bypass CAPTCHA, rate limits, authentication, or other access controls. Use a human-assisted retrieval workflow where required.
- Do not infer a complete institution universe from search-engine results. Establish it from an official BANBEIS/board directory and document coverage.
- Publish separate GPA-5 count, GPA-5 rate, and pass-rate rankings. Disclose the appeared-candidate threshold.
