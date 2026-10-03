from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "synthetic_household_data.csv"
OUTPUT = ROOT / "outputs" / "cleaned_demo_dataset.csv"

df = pd.read_csv(INPUT)

original_rows = len(df)

# Safe normalization of controlled text categories.
for column in [
    "lga",
    "community",
    "registration_status",
    "validation_status",
]:
    df[column] = df[column].apply(
        lambda value: (
            value.strip().lower()
            if isinstance(value, str)
            else value
        )
    )

# Restore title case for location labels used in this demo.
for column in ["lga", "community"]:
    df[column] = df[column].apply(
        lambda value: (
            value.title()
            if isinstance(value, str)
            else value
        )
    )

# Remove only exact duplicate rows.
# Missing values are not guessed or filled.
df = df.drop_duplicates().reset_index(drop=True)

OUTPUT.parent.mkdir(exist_ok=True)

df.to_csv(OUTPUT, index=False)

print(f"Original rows: {original_rows}")
print(
    f"Rows after exact-duplicate removal: {len(df)}"
)
print(
    f"Rows removed: {original_rows - len(df)}"
)
print(f"Output: {OUTPUT}")
