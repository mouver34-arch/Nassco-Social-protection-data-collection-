"""Generate a Markdown data-quality report from the synthetic household dataset."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "synthetic_household_data.csv"
CLEAN = ROOT / "outputs" / "cleaned_demo_dataset.csv"
REPORT = ROOT / "outputs" / "data_quality_report.md"


def main() -> None:
    raw = pd.read_csv(RAW)
    clean = pd.read_csv(CLEAN)

    missing = raw.isna().sum()
    duplicate_ids = int(raw["household_id"].duplicated(keep=False).sum())
    invalid_sizes = int(((raw["household_size"].notna()) & (raw["household_size"] <= 0)).sum())

    quality_counts = clean["quality_flag"].value_counts()

    lines = [
        "# Data-quality report",
        "",
        "> **SYNTHETIC DATA — FOR DEMONSTRATION ONLY**",
        "",
        "This report describes fictional records created for a portfolio demonstration.",
        "",
        "## Overview",
        "",
        f"- Raw rows inspected: **{len(raw)}**",
        f"- Rows in cleaned output: **{len(clean)}**",
        f"- Duplicate household-ID rows detected: **{duplicate_ids}**",
        f"- Invalid non-positive household-size rows: **{invalid_sizes}**",
        "",
        "## Missing values",
        "",
        missing.to_frame("missing_count").to_markdown(),
        "",
        "## Quality flags after cleaning",
        "",
        quality_counts.to_frame("records").to_markdown(),
        "",
        "## Cleaning decisions",
        "",
        "- Known categorical values were standardized to lowercase.",
        "- Exact duplicate rows were removed.",
        "- Missing values were not guessed or fabricated.",
        "- Invalid household sizes were flagged for review rather than silently corrected.",
        "",
        "## Interpretation",
        "",
        "The purpose of this report is to demonstrate a transparent QA workflow. It is not a measure of NASSCO/SOCU data quality and contains no NASSCO/SOCU records.",
    ]

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT}")


if __name__ == "__main__":
    main()
