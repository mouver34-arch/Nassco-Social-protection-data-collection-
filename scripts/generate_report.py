from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

RAW = ROOT / "data" / "synthetic_household_data.csv"
CLEAN = ROOT / "outputs" / "cleaned_demo_dataset.csv"
VALIDATION = ROOT / "outputs" / "validation_results.json"
REPORT = ROOT / "outputs" / "data_quality_report.md"

raw = pd.read_csv(RAW)
clean = pd.read_csv(CLEAN)

results = json.loads(
    VALIDATION.read_text(encoding="utf-8")
)

missing = raw.isna().sum()

missing_lines = "\n".join(
    f"| `{field}` | {int(count)} |"
    for field, count in missing.items()
)

report = f"""# Synthetic Data Quality Report

> **Portfolio demonstration only. This is not an official NASSCO/SOCU report and contains no real beneficiary records.**

## Summary

| Metric | Result |
|---|---:|
| Input records | {len(raw)} |
| Output records | {len(clean)} |
| Exact duplicate rows removed | {len(raw) - len(clean)} |
| Duplicate household-ID records flagged | {results["duplicate_household_id_count"]} |
| Invalid household-size rows | {len(results["invalid_household_size_rows"])} |
| Invalid registration-status rows | {len(results["invalid_registration_rows"])} |
| Registration formatting issues | {len(results["registration_formatting_issues"])} |
| Invalid validation-status rows | {len(results["invalid_validation_rows"])} |
| Validation formatting issues | {len(results["validation_formatting_issues"])} |

## Missing values

| Field | Missing values |
|---|---:|
{missing_lines}

## Interpretation

The synthetic dataset contains intentionally introduced quality issues:

- duplicate household records;
- one missing household size;
- one non-positive household size;
- one registration-status capitalization inconsistency; and
- one missing community.

The cleaning step standardizes safe text categories and removes the exact duplicate row. Missing or invalid substantive information is not guessed.

## Recommended review actions

1. Confirm duplicate records against the original field source before deciding whether a record should be retained.
2. Review the missing household size with the responsible field/enumerator workflow.
3. Review the non-positive household size as a likely data-entry or collection issue.
4. Confirm the missing community from source documentation rather than inferring it.
5. Keep a traceable record of changes made during production data cleaning.

## Portfolio boundary

All records and findings above are synthetic test cases created to demonstrate a reproducible QA workflow.
"""

REPORT.write_text(
    report,
    encoding="utf-8"
)

print(report)
