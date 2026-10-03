# Synthetic Data Quality Report

> **Portfolio demonstration only. This is not an official NASSCO/SOCU report and contains no real beneficiary records.**

## Summary

| Metric | Result |
|---|---:|
| Input records | 21 |
| Output records | 20 |
| Exact duplicate rows removed | 1 |
| Duplicate household-ID records flagged | 2 |
| Invalid household-size rows | 2 |
| Invalid registration-status rows | 0 |
| Registration formatting issues | 1 |
| Invalid validation-status rows | 0 |
| Validation formatting issues | 0 |

## Missing values

| Field | Missing values |
|---|---:|
| `household_id` | 0 |
| `lga` | 0 |
| `community` | 1 |
| `household_size` | 1 |
| `registration_status` | 0 |
| `validation_status` | 0 |

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
