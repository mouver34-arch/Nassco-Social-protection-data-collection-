# Ethical data handling

## Public portfolio boundary

The real-world work described in this repository can involve highly sensitive household and beneficiary information. Public demonstration must therefore use fictional records.

### Never publish

- NIN
- BVN
- phone numbers
- beneficiary names
- exact addresses
- household income or other unnecessary personal details
- identifiable geolocation
- real beneficiary records
- restricted questionnaires/forms
- internal reports or databases
- passwords, API keys, access tokens or private URLs

## Synthetic replacement

Where a real field example would expose protected information, use a fictional record such as `HH001`.

Avoid generating identifier-shaped values that could be mistaken for real government identity numbers.

## Publication checklist

Before pushing a field-data project publicly:

- Search source files for PII.
- Search for secret-like strings and credentials.
- Inspect the Git diff and commit history.
- Confirm that all demonstration records are synthetic.
- Confirm that organizational documents are not restricted.
- Remove unnecessary metadata and identifiable geolocation.
- Keep the public repository focused on methods and transferable skills.
