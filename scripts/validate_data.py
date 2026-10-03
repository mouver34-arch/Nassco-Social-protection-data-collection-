from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "synthetic_household_data.csv"
OUTPUT = ROOT / "outputs" / "validation_results.json"

REQUIRED_COLUMNS = [
    "household_id",
    "lga",
    "community",
    "household_size",
    "registration_status",
    "validation_status",
]

ALLOWED_REGISTRATION = {"registered", "pending"}
ALLOWED_VALIDATION = {"verified", "needs_review"}

df = pd.read_csv(INPUT)

missing_columns = [
    column for column in REQUIRED_COLUMNS
    if column not in df.columns
]

results = {
    "input_file": str(INPUT.relative_to(ROOT)),
    "record_count": int(len(df)),
    "missing_required_columns": missing_columns,
    "duplicate_household_id_count": (
        int(df["household_id"].duplicated(keep=False).sum())
        if "household_id" in df
        else None
    ),
    "missing_values_by_field": {
        key: int(value)
        for key, value in df.isna().sum().items()
    },
    "invalid_household_size_rows": [],
    "invalid_registration_rows": [],
    "invalid_validation_rows": [],
    "registration_formatting_issues": [],
    "validation_formatting_issues": [],
}

if not missing_columns:

    # Validate household size.
    size = pd.to_numeric(
        df["household_size"],
        errors="coerce"
    )

    invalid_size = (
        size.isna()
        | (size <= 0)
        | (size % 1 != 0)
    )

    results["invalid_household_size_rows"] = [
        int(index)
        for index in df.index[invalid_size]
    ]

    # Validate registration status.
    raw_registration = (
        df["registration_status"]
        .fillna("")
        .astype(str)
    )

    registration = (
        raw_registration
        .str.strip()
        .str.lower()
    )

    invalid_registration = (
        ~registration.isin(ALLOWED_REGISTRATION)
    )

    results["invalid_registration_rows"] = [
        int(index)
        for index in df.index[invalid_registration]
    ]

    formatting_registration = (
        raw_registration.ne(
            raw_registration.str.strip()
        )
        | raw_registration.ne(
            raw_registration.str.lower()
        )
    ) & raw_registration.ne("")

    results["registration_formatting_issues"] = [
        int(index)
        for index in df.index[formatting_registration]
    ]

    # Validate validation status.
    raw_validation = (
        df["validation_status"]
        .fillna("")
        .astype(str)
    )

    validation = (
        raw_validation
        .str.strip()
        .str.lower()
    )

    invalid_validation = (
        ~validation.isin(ALLOWED_VALIDATION)
    )

    results["invalid_validation_rows"] = [
        int(index)
        for index in df.index[invalid_validation]
    ]

    formatting_validation = (
        raw_validation.ne(
            raw_validation.str.strip()
        )
        | raw_validation.ne(
            raw_validation.str.lower()
        )
    ) & raw_validation.ne("")

    results["validation_formatting_issues"] = [
        int(index)
        for index in df.index[formatting_validation]
    ]

OUTPUT.parent.mkdir(exist_ok=True)

OUTPUT.write_text(
    json.dumps(results, indent=2),
    encoding="utf-8"
)

print(json.dumps(results, indent=2))
