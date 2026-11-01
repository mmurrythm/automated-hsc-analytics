# Bangladesh HSC 2026 Analytics

Research pipeline for collecting, validating, ranking, and comparing institution-level HSC 2026 statistics from Bangladesh's **nine general education boards**.

> **Status: scaffold / verification in progress.** This repository does not yet contain a verified 180-college dataset. Board portals differ, and some require CAPTCHA or interactive downloads. The pipeline is deliberately conservative: it does not bypass CAPTCHA, authentication, or other access controls.

## Scope

Dhaka, Rajshahi, Cumilla, Jashore, Chattogram, Barishal, Sylhet, Dinajpur, and Mymensingh. Madrasah and Technical boards are excluded.

## What it does

- Keeps board portal metadata in `config/boards.json`.
- Discovers EIINs from a supplied institution directory CSV (the directory source must be documented).
- Parses institution result tables from saved HTML files or accessible public pages.
- Validates candidate/pass/fail/GPA-5 arithmetic and derives rates.
- Produces reproducible CSV rankings and summary statistics.
- Preserves source URLs and retrieval timestamps.

## Ranking: don't confuse volume with performance

Three separate rankings are produced:
1. GPA-5 count (scale / volume).
2. GPA-5 rate among appeared candidates (outcome rate).
3. Pass rate among appeared candidates.

A minimum appeared-candidate threshold is configurable. The default is 0 (no hidden exclusion); always disclose the threshold in reports. Small colleges can otherwise dominate rate-based tables. Ties are retained using a stable secondary ordering.

## Quick start

Python 3.10+ recommended.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
source .venv/bin/activate
pip install -r requirements.txt
python -m hsc_analytics.cli validate-config
```

### Prepare an institution directory

The working institution frame is based on the BANBEIS 2022 college workbook. The project retains **all 3,321 college records** in the 2022 workbook across the nine general boards. `INSTITUTE LEVEL` is descriptive metadata, not an eligibility filter: Degree, Honours, and Masters-level institutions are retained because the institution's highest recorded level does not establish that it lacks HSC activity. The 2022 snapshot is a historical sampling frame, not a complete 2026 census. The assumption that newer colleges are unlikely to materially alter rankings is a documented, untested limitation in `docs/banbeis-workbook-audit.md`. Recreate the full directory with:

```bash
python scripts/build_banbeis_directory.py /path/to/banbeis_college_list_2022.xlsx
```

This writes `data/input/banbeis_college_eiin_directory_2022.csv` (all colleges) and `data/processed/banbeis_college_board_summary_2022.csv`. The output includes `higher_secondary_level_flag` for descriptive analysis. Verify HSC 2026 participation from official result records before treating any listed institution as a confirmed participant.

Create or adapt `data/input/colleges.csv` with columns:

```csv
board_code,college_name,eiin,source_url
dhaka,Example College,123456,https://official-source.example/...
```

Only include EIINs supported by a documented source. Do not invent missing identifiers.

### Parse saved institution report pages

Save publicly accessible report pages as UTF-8 HTML in `data/raw/html/`. Name each file `<board_code>_<eiin>.html`, then run:

```bash
python -m hsc_analytics.cli parse-html --input-dir data/raw/html --output data/processed/institution_results.csv
python -m hsc_analytics.cli analyze --input data/processed/institution_results.csv --output-dir reports
```

The parser extracts labelled values when it can identify them. Review `parse_status` and manually verify every board-specific layout before treating outputs as authoritative.

## Data fields

Where published: registered, appeared, passed, failed, GPA-5, board, college, EIIN, source URL, retrieval time, and parser status. Rates are calculated only when denominators are positive. Missing is not treated as zero.

## Official portal discovery

Board-specific result and statistics endpoints identified during initial research are recorded in `config/boards.json`. Key links include:
- Dhaka: https://result.dhakaeducationboard.gov.bd/v2/home
- Chattogram: https://hscresult.bise-ctg.gov.bd/h22_31_x1_26/individual/index.php
- Sylhet: https://result.sylhetboard.gov.bd/v2/home

Some boards publish consolidated statistics PDFs while others expose EIIN-based interactive result services. A discovered link is not evidence that its contents have been downloaded or parsed. Do not guess subdomains or endpoints; keep unconfirmed links null.

The central results portal is https://www.educationboardresults.gov.bd/v2/home. The BSS announcement on 27 October 2026 stated that HSC 2026 results would be published on 31 October 2026 and that institutions could obtain complete result sheets through the common or respective board websites using EIIN. Verify availability and the exact report format at runtime.

## Responsible collection

- Respect each portal's terms, robots guidance, and published rate limits.
- Use low request rates; the default HTTP client waits between requests.
- Do not solve, outsource, or bypass CAPTCHA automatically. If a portal presents CAPTCHA, complete the official workflow manually and save the resulting report.
- Do not submit student roll/registration numbers or collect individual student-level personal data.
- Cache public responses and retain source URL, timestamp, and retrieval method.
- Check copyright / reuse terms before redistributing raw report files.

## National comparison

The overall HSC-and-equivalent headline figures reported in news may include Madrasah and Technical boards. They are **not** a valid benchmark for this project's nine-general-board subset. Use official nine-board aggregates with matching definitions (appeared vs registered, same exam year and scope). If no matching official aggregate is available, mark it unavailable rather than estimating it.

## Project structure

```
config/                 board portal and ranking settings
data/input/             user-supplied college directory (not committed)
data/raw/html/          saved public report pages (not committed)
data/processed/         normalized CSV output (not committed)
reports/                generated tables and summaries (not committed)
src/hsc_analytics/      CLI, parsing, validation, analysis
tests/                  unit tests
```

## Credits

- Project owner and research lead: **mmurrythm**
- AI-assisted research, software architecture, data-collection workflow, statistical analysis, and documentation: **ChatGPT (OpenAI)**

## Disclaimer

This is an independent research project, not an official publication of the Bangladesh Education Boards. Rankings depend on the completeness and comparability of published data. Every result should be traceable to its source and checked before publication.



## Board websites and common result portals

The nine official board homepages supplied for this project are recorded in `config/boards.json`. A board homepage is a discovery starting point, not necessarily the result endpoint.

The common result interfaces currently verified are:
- Government-hosted: https://www.educationboardresults.gov.bd/v2/home
- Web-based result system: https://www.eboardresults.com/v2/home

Both forms expose board, examination, year, result type, EIIN, and CAPTCHA fields. The government-hosted form identifies the Inter-Education Board Coordination Committee and says result information is maintained by the respective board. Institution-result retrieval therefore remains a human-assisted step where CAPTCHA is required.

Board-specific sources identified so far:
- Dhaka result portal: https://result.dhakaeducationboard.gov.bd/v2/home
- Rajshahi HSC statistics page: https://rajshahieducationboard.gov.bd/pages/static-pages/691997b2933eb65569dde245
- Jashore HSC Corner / statistics notice: https://www.jessoreboard.gov.bd/index.php/site/notice/6/index.php
- Cumilla institution-wise result information: https://web.comillaboard.gov.bd/bisecb/eseba_details/10
- Chattogram EIIN-wise result: https://hscresult.bise-ctg.gov.bd/h22_31_x1_26/individual/index.php
- Sylhet result portal: https://result.sylhetboard.gov.bd/v2/home
- Dinajpur result portal: https://results.dinajpurboard.gov.bd/
- Mymensingh board homepage / result analytics discovery: https://www.mymensingheducationboard.gov.bd/

Barishal's consolidated 2026 institution statistics endpoint still requires confirmation. Rajshahi and Jashore pages list 2026 statistics material, but institution-level records have not yet been extracted. The 27 October 2026 BSS announcement confirms that institutions can download complete result sheets from common education-board sites and respective board websites using EIIN: https://www.bssnews.net/news/439086.
