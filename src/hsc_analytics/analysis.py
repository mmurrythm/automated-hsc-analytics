from __future__ import annotations
import pandas as pd

def make_rankings(df: pd.DataFrame, config: dict) -> dict[str, pd.DataFrame]:
    results = {}
    minimum = int(config.get("minimum_appeared", 0))
    n = int(config.get("top_n_per_board", 20))
    eligible = df.copy()
    if "appeared" in eligible:
        eligible = eligible[eligible["appeared"].fillna(-1) >= minimum]
    sorters = {
        "gpa5_count": ["gpa5_count", "pass_rate", "appeared", "college_name"],
        "gpa5_rate": ["gpa5_rate", "appeared", "college_name"],
        "pass_rate": ["pass_rate", "appeared", "college_name"],
    }
    for metric, cols in sorters.items():
        valid = eligible.dropna(subset=[metric]).copy() if metric in eligible else eligible.iloc[0:0].copy()
        cols = [c for c in cols if c in valid.columns]
        if not cols: results[metric] = valid; continue
        ascending = [False] * len(cols)
        if "college_name" in cols: ascending[cols.index("college_name")] = True
        valid = valid.sort_values(cols, ascending=ascending, kind="mergesort")
        valid["rank_within_board"] = valid.groupby("board_code").cumcount() + 1
        results[metric] = valid[valid["rank_within_board"] <= n]
    return results

def make_board_summary(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty: return pd.DataFrame()
    sums = df.groupby("board_code", dropna=False).agg(
        colleges=("eiin","count"),
        appeared=("appeared","sum"),
        passed=("passed","sum"),
        failed=("failed","sum"),
        gpa5_count=("gpa5_count","sum")
    ).reset_index()
    sums["pass_rate"] = sums["passed"] / sums["appeared"] * 100
    sums["gpa5_rate"] = sums["gpa5_count"] / sums["appeared"] * 100
    return sums
