from __future__ import annotations
import argparse, json
from pathlib import Path
import pandas as pd
from .parse import parse_html_file
from .validate import normalize_and_validate
from .analysis import make_rankings, make_board_summary

ROOT = Path(__file__).resolve().parents[2]

def main():
    p = argparse.ArgumentParser(description="Bangladesh HSC 2026 analytics")
    sub = p.add_subparsers(dest="command", required=True)
    sub.add_parser("validate-config")
    h = sub.add_parser("parse-html")
    h.add_argument("--input-dir", default="data/raw/html")
    h.add_argument("--output", default="data/processed/institution_results.csv")
    a = sub.add_parser("analyze")
    a.add_argument("--input", default="data/processed/institution_results.csv")
    a.add_argument("--output-dir", default="reports")
    args = p.parse_args()
    if args.command == "validate-config":
        cfg = json.loads((ROOT / "config/boards.json").read_text(encoding="utf-8"))
        boards = cfg["boards"]
        assert len(boards) == 9, "Expected exactly nine general boards"
        assert len({b["code"] for b in boards}) == 9, "Board codes must be unique"
        print("Config OK: nine general education boards; unverified portals remain explicitly blank.")
    elif args.command == "parse-html":
        rows = [parse_html_file(f) for f in Path(args.input_dir).glob("*.html")]
        out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
        df = normalize_and_validate(pd.DataFrame(rows))
        df.to_csv(out, index=False)
        print(f"Wrote {len(df)} institution rows to {out}")
    elif args.command == "analyze":
        df = pd.read_csv(args.input)
        out = Path(args.output_dir); out.mkdir(parents=True, exist_ok=True)
        cfg = json.loads((ROOT / "config/ranking.json").read_text(encoding="utf-8"))
        rankings = make_rankings(df, cfg)
        for metric, table in rankings.items():
            table.to_csv(out / f"top_{cfg['top_n_per_board']}_{metric}.csv", index=False)
        make_board_summary(df).to_csv(out / "board_summary.csv", index=False)
        print(f"Analysis written to {out}")

if __name__ == "__main__":
    main()
