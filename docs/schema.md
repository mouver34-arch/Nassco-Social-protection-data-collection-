# Synthetic Dataset Schema

## Purpose

This schema supports a small demonstration of household enumeration and social-protection data-quality workflows.

## Fields

| Field | Data type | Required? | Validation | Portfolio meaning |
|---|---|---:|---|---|
| `household_id` | string | Yes | Must be present; duplicates are flagged | Synthetic record identifier |
| `lga` | string | Yes | Must be present | Demonstration LGA |
| `community` | string | Yes | Missing values are flagged | Synthetic community grouping |
| `household_size` | integer | Yes | Must be a positive whole number | Demonstration household count |
| `registration_status` | category | Yes | `registered` / `pending` after normalization | Registration workflow status |
| `validation_status` | category | Yes | `verified` / `needs_review` after normalization | QA disposition |

## Important boundary

The schema is intentionally simplified. It does **not** represent an official NASSCO/SOCU production schema and should not be presented as one.
