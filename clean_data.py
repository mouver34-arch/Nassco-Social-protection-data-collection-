"""Clean the synthetic household dataset using transparent rules."""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_household_data.csv"
OUTPUT = ROOT / "outputs" / "cleaned_demo_dataset.csv"


def main() -> None:
    df = pd.read_csv(DATA)

    # Standardize known categorical values.
    df["registration_status"] = df["registration_status"].astype("string").str.strip().str.lower()
    df["validation_status"] = df["validation_status"].astype("string").str.strip().str.lower()

    # Remove exact duplicate household rows, retaining the first occurrence.
    before = len(df)
    df = df.drop_duplicates()
    removed_exact_duplicates = before - len(df)

    # Do not invent missing values. Invalid records are retained but flagged.
    df["quality_flag"] = "clean"
    df.loc[df["community"].isna(), "quality_flag"] = "review_missing_community"
    df.loc[df["household_size"].isna(), "quality_flag"] = "review_missing_household_size"
    df.loc[df["household_size"].notna() & (df["household_size"] <= 0), "quality_flag"] = "review_invalid_household_size"

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)

    print(f"Rows after exact-duplicate removal: {len(df)}")
    print(f"Exact duplicate rows removed: {removed_exact_duplicates}")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
