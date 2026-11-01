from __future__ import annotations
import pandas as pd

NUMERIC = ["registered", "appeared", "passed", "failed", "gpa5_count", "eiin"]

def normalize_and_validate(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty: return df
    for col in NUMERIC:
        if col not in df: df[col] = pd.NA
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
    for col in ["board_code","college_name","source_url","source_file","parse_status"]:
        if col not in df: df[col] = pd.NA
    df["validation_flags"] = ""
    def flags(r):
        out = []
        vals = {k: r.get(k) for k in NUMERIC}
        for k, v in vals.items():
            if pd.notna(v) and v < 0: out.append(f"negative_{k}")
        if pd.notna(r.get("passed")) and pd.notna(r.get("appeared")) and r["passed"] > r["appeared"]:
            out.append("passed_exceeds_appeared")
        if pd.notna(r.get("failed")) and pd.notna(r.get("appeared")) and r["failed"] > r["appeared"]:
            out.append("failed_exceeds_appeared")
        if pd.notna(r.get("passed")) and pd.notna(r.get("failed")) and pd.notna(r.get("appeared")):
            if r["passed"] + r["failed"] != r["appeared"]: out.append("pass_fail_does_not_equal_appeared")
        if pd.notna(r.get("gpa5_count")) and pd.notna(r.get("passed")) and r["gpa5_count"] > r["passed"]:
            out.append("gpa5_exceeds_passed")
        return ";".join(out)
    df["validation_flags"] = df.apply(flags, axis=1)
    df["pass_rate"] = (df["passed"] / df["appeared"] * 100).where(df["appeared"] > 0)
    df["gpa5_rate"] = (df["gpa5_count"] / df["appeared"] * 100).where(df["appeared"] > 0)
    return df
