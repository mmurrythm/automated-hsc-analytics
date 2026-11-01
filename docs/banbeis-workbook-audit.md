# BANBEIS college workbook inspection

## Adopted project rule

**The 2022 BANBEIS workbook is the project's primary institution-directory baseline. Only rows whose `INSTITUTE LEVEL` is exactly `HIGHER SECONDARY` are eligible for the working HSC college directory.** The project owner has explicitly chosen to retain this historical snapshot as the main frame. The working directory therefore contains 1,400 institutions across the nine general boards.

The project accepts the practical assumption that colleges newly established after the 2022 snapshot are generally too small to materially alter the ranking results. This is a scope assumption, not a verified fact about every new institution. Document it as a limitation in publications; do not silently imply that the directory is a complete 2026 census.

## Inspection result

The user-provided workbook contains one worksheet, `clg`, with 3,321 institution records and 14 columns. It has 3,321 unique EIINs across all 64 districts. The workbook's internal document properties show creation and modification timestamps of 26 June 2022.

The working directory applies the explicit eligibility filter:
```python
df[df["INSTITUTE LEVEL"].astype(str).str.strip().str.upper() == "HIGHER SECONDARY"]
```

Filtered result: **1,400 rows, 1,400 unique EIINs, no duplicate EIINs**, spanning all nine boards and all 64 districts. The other 1,921 records (Degree Pass, Degree Honours, Masters, or other non-matching levels) are excluded from the working directory.

## Board-wise working-directory counts

| Board | Higher-secondary institutions |
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

The board mapping is derived from district-to-board jurisdiction groupings. All 64 source district labels were mapped; independently verify jurisdiction mapping before publication.

## Data quality checks

- 3,321 original rows loaded from the `clg` worksheet.
- 3,321 unique EIINs in the source workbook.
- 1,400 rows retained after the Higher Secondary-only filter.
- 1,400 unique EIINs in the filtered directory.
- No duplicate EIINs in either source or filtered directory.
- 64 distinct district labels; all 64 mapped.
- Repeated institution-name strings exist; retain separate records where EIIN differs.
- Some address/post/geography fields are missing; do not fill missing values with zero or invented text.
- Mobile contact numbers are omitted from the cleaned project directory because they are unnecessary for aggregate institution analytics.

## Scope limitation

The 2022 snapshot remains the main frame by project decision. Newly established colleges after the snapshot may be absent. The project assumes their omission is unlikely to materially change top-20 rankings, but this has not been empirically tested. If a newly established college is found in official HSC 2026 result records and appears competitive, flag it separately as a documented exception rather than silently changing the baseline.

The Higher Secondary label is treated as the operational eligibility criterion for this project, per the project owner's instruction. Actual HSC 2026 participation should still be confirmed when institution result data are collected.

## Provenance

Source: BANBEIS official College List attachment listed at https://banbeis.gov.bd/pages/files/6919975c933eb65569ddc4e2

The exact workbook was supplied by the project owner. Internal workbook metadata: created 2022-06-26, modified 2022-06-26. The attachment page is listed as updated 21 April 2024: https://banbeis.gov.bd/site/page/3d999522-bccb-4a63-9caa-a33fdf922416/কলেজের-তালিকা
