#!/usr/bin/env python3
"""Build the project's 2022 BANBEIS complete nine-board college EIIN directory.

Input: BANBEIS college-list XLSX workbook, worksheet 'clg', header row 2.
Output: all-college CSV and board summary CSV. All institute levels are retained.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

DISTRICT_TO_BOARD = {
    **{d: "dhaka" for d in ["Dhaka", "Faridpur", "Gazipur", "Gopalganj", "Kishoreganj", "Madaripur", "Manikganj", "Munshiganj", "Narayanganj", "Narsingdi", "Rajbari", "Shariatpur", "Tangail"]},
    **{d: "rajshahi" for d in ["Bogura", "Joypurhat", "Naogaon", "Natore", "Nawabganj", "Pabna", "Rajshahi", "Sirajganj"]},
    **{d: "cumilla" for d in ["Brahamanbaria", "Chandpur", "Cumilla", "Feni", "Lakshmipur", "Noakhali"]},
    **{d: "jashore" for d in ["Bagerhat", "Chuadanga", "Jashore", "Jhenaidah", "Khulna", "Kushtia", "Magura", "Meherpur", "Norail", "Satkhira"]},
    **{d: "chattogram" for d in ["Bandarban", "Chattogram", "Coxs Bazar", "Khagrachhari", "Rangamati"]},
    **{d: "barishal" for d in ["Barguna", "Barisal", "Bhola", "Jhalokati", "Patuakhali", "Pirojpur"]},
    **{d: "sylhet" for d in ["Habiganj", "Maulvibazar", "Sunamganj", "Sylhet"]},
    **{d: "dinajpur" for d in ["Dinajpur", "Gaibandha", "Kurigram", "Lalmonirhat", "Nilphamari", "Panchagarh", "Rangpur", "Thakurgaon"]},
    **{d: "mymensingh" for d in ["Jamalpur", "Mymensingh", "Netrakona", "Sherpur"]},
}
BOARD_NAMES = {
    "dhaka": "Dhaka", "rajshahi": "Rajshahi", "cumilla": "Cumilla",
    "jashore": "Jashore", "chattogram": "Chattogram", "barishal": "Barishal",
    "sylhet": "Sylhet", "dinajpur": "Dinajpur", "mymensingh": "Mymensingh",
}


def build(input_xlsx: Path, output_csv: Path, summary_csv: Path) -> None:
    source = pd.read_excel(input_xlsx, sheet_name="clg", header=1)
    required = {"DISTRICT", "EIIN", "INSTITUTE NAME", "INSTITUTE LEVEL"}
    missing = required - set(source.columns)
    if missing:
        raise ValueError(f"Missing required workbook columns: {sorted(missing)}")

    source["board_code"] = source["DISTRICT"].map(DISTRICT_TO_BOARD)
    unmapped = sorted(source.loc[source["board_code"].isna(), "DISTRICT"].dropna().unique())
    if unmapped:
        raise ValueError(f"Unmapped district labels: {unmapped}")

    # Retain every college row; institute level is descriptive metadata.
    selected = source.copy()
    selected["board_name"] = selected["board_code"].map(BOARD_NAMES)
    selected["higher_secondary_level_flag"] = source["INSTITUTE LEVEL"].astype(str).str.strip().str.upper().eq("HIGHER SECONDARY")

    result = selected.rename(columns={
        "DISTRICT": "district_source", "UPAZILA/THANA": "upazila_thana",
        "EIIN": "eiin", "INSTITUTE NAME": "institution_name",
        "INSTITUTE TYPE": "institution_type", "INSTITUTE LEVEL": "institution_level",
        "ADDRESS": "address", "POST": "post", "MANAGEMENT": "management",
        "MPO": "mpo", "STUDY TYPE": "study_type", "AREA": "area",
        "GEOGRPY": "geography",
    })
    result["source_workbook_metadata_created"] = "2022-06-26"
    result["source_workbook_metadata_modified"] = "2022-06-26"
    columns = [
        "board_code", "board_name", "district_source", "upazila_thana", "eiin",
        "institution_name", "institution_type", "institution_level",
        "higher_secondary_level_flag", "management", "mpo", "study_type",
        "area", "geography", "address", "post",
        "source_workbook_metadata_created", "source_workbook_metadata_modified",
    ]
    result = result[columns].sort_values(["board_code", "district_source", "eiin"])
    if result["eiin"].duplicated().any():
        raise ValueError("Duplicate EIINs found in the nine-board college frame")

    output_csv.parent.mkdir(parents=True, exist_ok=True)
    summary_csv.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output_csv, index=False, encoding="utf-8-sig")
    summary = result.groupby(["board_code", "board_name"]).agg(
        college_records=("eiin", "nunique"),
        explicitly_higher_secondary_labelled=("higher_secondary_level_flag", "sum"),
        districts=("district_source", "nunique"),
    ).reset_index()
    summary.to_csv(summary_csv, index=False, encoding="utf-8-sig")
    print(f"Wrote {len(result)} colleges to {output_csv}")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("workbook", type=Path, help="Path to the BANBEIS 2022 XLSX workbook")
    parser.add_argument("--output", type=Path, default=Path("data/input/banbeis_college_eiin_directory_2022.csv"))
    parser.add_argument("--summary", type=Path, default=Path("data/processed/banbeis_college_board_summary_2022.csv"))
    args = parser.parse_args()
    build(args.workbook, args.output, args.summary)
