# Data-quality report

> **SYNTHETIC DATA — FOR DEMONSTRATION ONLY**

This report describes fictional records created for a portfolio demonstration.

## Overview

- Raw rows inspected: **21**
- Rows in cleaned output: **20**
- Duplicate household-ID rows detected: **2**
- Invalid non-positive household-size rows: **1**

## Missing values

|                     |   missing_count |
|:--------------------|----------------:|
| household_id        |               0 |
| lga                 |               0 |
| community           |               1 |
| household_size      |               1 |
| registration_status |               0 |
| validation_status   |               0 |

## Quality flags after cleaning

| quality_flag                  |   records |
|:------------------------------|----------:|
| clean                         |        17 |
| review_missing_household_size |         1 |
| review_invalid_household_size |         1 |
| review_missing_community      |         1 |

## Cleaning decisions

- Known categorical values were standardized to lowercase.
- Exact duplicate rows were removed.
- Missing values were not guessed or fabricated.
- Invalid household sizes were flagged for review rather than silently corrected.

## Interpretation

The purpose of this report is to demonstrate a transparent QA workflow. It is not a measure of NASSCO/SOCU data quality and contains no NASSCO/SOCU records.