# BANBEIS college workbook inspection

## Inspection result

The user-provided workbook contains one worksheet, `clg`, with 3,321 institution records and 14 columns. It has 3,321 unique EIINs across all 64 districts. There are 24 repeated institution-name strings, but no duplicate EIINs; repeated names are not treated as duplicate institutions.

The workbook's internal document properties show creation and modification timestamps of 26 June 2022. The BANBEIS web page where the attachment is listed was last updated 21 April 2024, but that does not make the workbook itself a 2024 snapshot. Treat this file as a historical candidate directory, not a current verified 2026 universe.

## Board mapping

All 64 district labels in the workbook were mapped to the nine general education boards using the board jurisdiction/district grouping. No district was left unmapped. This mapping is a derived classification and should be independently checked against current board jurisdiction documentation before publication.

## Counts by assigned board

See `data/processed/banbeis_directory_board_summary.csv`.

The full cleaned directory contains 3,321 rows and is available as a downloadable CSV generated from the uploaded workbook. It retains original EIIN, institution name, district, upazila/thana, institute level, management and other fields, with added `board_code`, `board_name`, and `higher_secondary_level_flag`.

| Board | All college records | Explicitly labelled Higher Secondary |
|---|---:|---:|
| Barishal | 264 | 95 |
| Chattogram | 187 | 77 |
| Cumilla | 305 | 126 |
| Dhaka | 678 | 338 |
| Dinajpur | 451 | 194 |
| Jashore | 466 | 163 |
| Mymensingh | 225 | 116 |
| Rajshahi | 579 | 211 |
| Sylhet | 166 | 80 |
| **Total** | **3,321** | **1,400** |

## Critical eligibility caveat

The workbook's `INSTITUTE LEVEL` field has four values: Higher Secondary (1,400), Degree (Pass) (1,081), Degree (Honors) (644), and Masters (196). The 1,400 Higher Secondary rows are only the records explicitly labelled Higher Secondary. Degree and honours colleges may also conduct HSC; therefore, filtering to that label alone would likely omit HSC-participating institutions. Conversely, including every college record does not prove that it participated in HSC 2026.

Use this file as a candidate EIIN directory. Determine actual HSC 2026 participation from official board result records, and reconcile the candidate universe against a current BANBEIS/DSHE source before claiming complete coverage.

## Data quality checks

- 3,321 rows loaded from the single `clg` worksheet.
- 3,321 unique EIINs; no duplicate EIINs.
- 64 distinct district labels; all 64 mapped.
- 24 duplicate institution-name strings; retain separate EIIN records.
- Some address/post/geography fields are missing; do not fill missing values with zero or invented text.
- The workbook includes mobile contact numbers. They are intentionally omitted from the cleaned project directory because they are unnecessary for aggregate HSC institution analytics.

## Provenance

Source: BANBEIS official College List attachment listed at https://banbeis.gov.bd/pages/files/6919975c933eb65569ddc4e2
The exact workbook was supplied by the project owner in this conversation. Internal workbook metadata: created 2022-06-26, modified 2022-06-26. The attachment page is listed as updated 21 April 2024: https://banbeis.gov.bd/site/page/3d999522-bccb-4a63-9caa-a33fdf922416/কলেজের-তালিকা
