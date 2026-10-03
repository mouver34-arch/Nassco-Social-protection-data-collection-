# Social Protection Field Data Collection & Validation

A synthetic portfolio project demonstrating practical skills in **household enumeration, beneficiary registration and verification workflows, data validation, data-quality assurance, cleaning, and reporting**.

This repository is designed for a **Field Data Enumerator / Research & Data Analyst portfolio**. It reflects the type of field-to-data workflow used in social-protection data activities while using **synthetic data only**.

---

## 1. Real-world context

The portfolio is informed by my field experience with **NASSCO/SOCU in Jigawa State**, where my work has included:

- household enumeration;
- beneficiary enrollment and registration activities;
- verification and validation;
- data-quality checking;
- discrepancy clarification;
- community engagement;
- digital data collection; and
- field-level review of records.

My experience includes work connected with social-protection activities such as **PVHH, RRR, NIMC-linked integration of household NIN information into social-register processes, and current N-CARES-related expansion**.

This repository is a **portfolio extension** of that experience. The code, dataset, findings, and outputs here are intentionally constructed for demonstration.

---

## 2. What this project demonstrates

The project follows a simplified field-data lifecycle:

**FIELD → DATA COLLECTION → DATA VALIDATION → DATA QUALITY ASSURANCE → CLEANING → ANALYSIS → REPORTING → DECISION SUPPORT**

The emphasis is not on creating a large software system. It is on demonstrating that field data can be checked systematically before it is used for reporting or decisions.

---

## 3. Problem

Field-collected household data can contain issues such as:

- duplicate household records;
- missing values;
- invalid numeric values;
- inconsistent category formatting;
- records requiring manual review;
- incomplete community information; and
- discrepancies that should not be silently corrected.

A good field-data workflow should identify these issues, document them, and separate **verified records** from records requiring review.

---

## 4. Objectives

1. Define a small, auditable household dataset structure.
2. Demonstrate field-level validation checks.
3. Detect duplicates, missing values, and invalid household-size values.
4. Standardize safe categorical formatting without inventing missing information.
5. Produce a simple data-quality report.
6. Export a cleaned demonstration dataset.
7. Keep all portfolio data free from real beneficiary identifiers.

---

## 5. Synthetic-data disclaimer

**All records in `data/synthetic_household_data.csv` are fictional and created solely for portfolio demonstration.**

They are not extracted from:

- NASSCO/SOCU databases;
- the National Social Register;
- NIMC records;
- beneficiary registers;
- household enumeration forms;
- KoboToolbox/ODK production projects; or
- any confidential organizational system.

The communities and programme context mentioned in this README reflect the professional context of the portfolio owner. The individual household records, IDs, values, and quality issues are synthetic.

---

## 6. Dataset schema

| Field | Type | Description |
|---|---|---|
| `household_id` | string | Synthetic household identifier created for this portfolio. |
| `lga` | string | Local Government Area represented in the demonstration data. |
| `community` | string | Synthetic community label used to demonstrate geographic grouping without identifying a real household. |
| `household_size` | integer | Number of household members recorded in the synthetic dataset. |
| `registration_status` | category | Demonstrates registration workflow status: `registered` or `pending`. |
| `validation_status` | category | Demonstrates QA status: `verified` or `needs_review`. |

### Intentional quality issues

The dataset contains deliberately introduced issues so the validation workflow has something meaningful to detect:

- a missing household size;
- a zero household size;
- inconsistent capitalization in a category;
- an exact duplicate household record; and
- a missing community.

These are **test cases**, not real field findings.

---

## 7. Validation and quality-control workflow

### Step 1 — Structural checks

Confirm that required fields exist and that the input file can be read.

### Step 2 — Identifier checks

Check for duplicate `household_id` values.

### Step 3 — Missing-value checks

Count missing values by field.

### Step 4 — Field-level validity

Check that household size is a positive whole number.

### Step 5 — Category consistency

Check registration and validation categories after normalizing case/whitespace, while also recording formatting inconsistencies in the raw values.

### Step 6 — Cleaning

Standardize safe categorical values and remove exact duplicate rows.

Missing or invalid information is **flagged rather than guessed**.

### Step 7 — Reporting

Generate a concise Markdown quality report showing:

- record counts;
- duplicate counts;
- missing values;
- invalid household-size records;
- category issues;
- cleaning actions; and
- review recommendations.

---

## 8. Python implementation

Requirements:

```bash
pip install -r requirements.txt
