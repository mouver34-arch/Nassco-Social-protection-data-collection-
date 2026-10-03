"""Validate the synthetic household dataset and report data-quality issues."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_household_data.csv"

REQUIRED = {
    "household_id", "lga", "community", "household_size",
    "registration_status", "validation_status"
}
ALLOWED_REGISTRATION = {"registered", "pending"}
ALLOWED_VALIDATION = {"verified", "needs_review"}


def main() -> None:
    df = pd.read_csv(DATA)
    missing_columns = REQUIRED.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Missing columns: {sorted(missing_columns)}")

    issues = []

    for col in ["household_id", "lga", "community", "registration_status", "validation_status"]:
        rows = df.index[df[col].isna()].tolist()
        for row in rows:
            issues.append({"row": row + 2, "field": col, "issue": "missing_value"})

    duplicate_mask = df["household_id"].duplicated(keep=False)
    for row in df.index[duplicate_mask]:
        issues.append({"row": row + 2, "field": "household_id", "issue": "duplicate_id"})

    invalid_size = df["household_size"].notna() & (
        (df["household_size"] <= 0) | (df["household_size"] % 1 != 0)
    )
    for row in df.index[invalid_size]:
        issues.append({"row": row + 2, "field": "household_size", "issue": "invalid_positive_integer"})

    # Case/format consistency is assessed before cleaning.
    for row in df.index[~df["registration_status"].isna()]:
        value = str(df.at[row, "registration_status"])
        if value.strip().lower() not in ALLOWED_REGISTRATION:
            issues.append({"row": row + 2, "field": "registration_status", "issue": "invalid_category"})

    print(f"Rows inspected: {len(df)}")
    print(f"Quality issues detected: {len(issues)}")
    for issue in issues:
        print(issue)


if __name__ == "__main__":
    main()
