# BANBEIS college workbook inspection

## Adopted project rule

**Retain all 3,321 college records in the 2022 BANBEIS workbook as the primary candidate institution directory for the nine general education boards.** Do not filter by `INSTITUTE LEVEL`.

The user's rationale is that Degree, Honours, and Masters labels describe the institution's highest recorded level; these labels do not establish that the institution does not conduct HSC. The `INSTITUTE LEVEL` field is therefore retained as descriptive metadata, and an explicit `higher_secondary_level_flag` is provided for audit and stratified analysis only.

The 2022 snapshot is a historical sampling frame, not a complete 2026 census. The project owner accepts the working assumption that colleges established after the snapshot are generally unlikely to materially change the rankings. This is an untested scope assumption, not a verified fact. If a newer institution appears in official HSC 2026 result records, include it as a documented exception or supplementary record rather than silently altering the historical baseline.

**Presence in this directory does not confirm HSC 2026 participation.** Confirm participation using official board result records before ranking.

## Inspection result

The user-provided workbook contains one worksheet, `clg`, with 3,321 institution records and 14 columns. It has 3,321 unique EIINs across all 64 districts. The workbook's internal document properties show creation and modification timestamps of 26 June 2022.

All rows are retained:
- **3,321 college records**
- **3,321 unique EIINs**
- **64 districts**
- **Nine general education boards**
- No duplicate EIINs found

The earlier Higher Secondary-only subset contained 1,400 records. That filter is superseded and must not be used as the primary institution universe.

## Board-wise full-directory counts

| Board | College records |
|---|---:|
| Dhaka | 678 |
| Rajshahi | 579 |
| Jashore | 466 |
| Dinajpur | 451 |
| Cumilla | 305 |
| Barishal | 264 |
| Mymensingh | 225 |
| Chattogram | 187 |
| Sylhet | 166 |
| **Total** | **3,321** |

The district-to-board mapping is derived from board jurisdiction groupings. All 64 source district labels were mapped. Independently verify jurisdiction mapping before publication.

## Higher Secondary label counts (metadata only)

| Board | Explicitly labelled Higher Secondary |
|---|---:|
| Dhaka | 338 |
| Rajshahi | 211 |
| Dinajpur | 194 |
| Jashore | 163 |
| Cumilla | 126 |
| Mymensingh | 116 |
| Barishal | 95 |
| Sylhet | 80 |
| Chattogram | 77 |
| **Total** | **1,400** |

These counts describe the workbook's exact `INSTITUTE LEVEL = HIGHER SECONDARY` label only. They are not the eligible universe and must not be used to exclude the remaining institutions.

## Data quality checks

- 3,321 original rows loaded from the `clg` worksheet.
- 3,321 unique EIINs in the source workbook.
- 3,321 rows retained in the full directory.
- No duplicate EIINs in the full directory.
- 64 distinct district labels; all 64 mapped.
- Repeated institution-name strings exist; retain separate records where EIIN differs.
- Some address/post/geography fields are missing; do not fill missing values with zero or invented text.
- Mobile contact numbers are omitted from the cleaned project directory because they are unnecessary for aggregate institution analytics.

## Scope limitations

1. **Historical frame:** institutions established after the 2022 snapshot may be absent.
2. **Unverified participation:** the directory is a candidate frame; HSC 2026 participation must be confirmed from board results.
3. **Untested new-college assumption:** the belief that newer colleges are unlikely to change top rankings materially has not been empirically tested.
4. **Board mapping:** district-to-board mapping should be independently checked before publication.

## Provenance

Source: BANBEIS official College List attachment listed at https://banbeis.gov.bd/pages/files/6919975c933eb65569ddc4e2

The exact workbook was supplied by the project owner. Internal workbook metadata: created 2022-06-26, modified 2022-06-26. The attachment page is listed as updated 21 April 2024: https://banbeis.gov.bd/site/page/3d999522-bccb-4a63-9caa-a33fdf922416/কলেজের-তালিকা
