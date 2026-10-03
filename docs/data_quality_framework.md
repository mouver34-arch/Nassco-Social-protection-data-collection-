# Data Quality Framework

The repository uses a simple exception-first workflow:

1. **Read and structure** — confirm the file and required fields.
2. **Identify duplicates** — flag repeated household IDs.
3. **Check completeness** — count missing values by field.
4. **Check validity** — test household size and controlled categories.
5. **Normalize safely** — standardize case/whitespace where this does not alter meaning.
6. **Flag exceptions** — send incomplete or invalid records for review.
7. **Clean defensibly** — remove exact duplicate rows only; do not invent missing values.
8. **Report** — produce an auditable summary of what was found and changed.

## Principle

**Do not turn uncertainty into false certainty.**

For example, if a community value is missing, the workflow reports it as missing rather than guessing the community from another field.
