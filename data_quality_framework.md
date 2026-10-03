# Data quality framework

The demonstration checks five practical dimensions.

| Dimension | Example check |
|---|---|
| Completeness | Required fields are not blank |
| Uniqueness | Household IDs are not duplicated |
| Validity | Household size is a positive integer |
| Consistency | Categorical values follow an agreed format |
| Traceability | Validation and cleaning outputs document what changed |

## Cleaning principle

The script uses conservative transformations. It standardizes known categorical values and removes duplicate rows only when the duplicate is an exact duplicate of the household record.

Records with missing or invalid information are flagged rather than silently guessed.
