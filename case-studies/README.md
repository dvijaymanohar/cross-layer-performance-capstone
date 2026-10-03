# Case studies

Create one directory per investigation:

```text
case-studies/<name>/
├── README.md
├── benchmark-contract.md
├── hypothesis-log.md
├── raw-results/
├── profiler-notes/
├── correctness/
└── decision-record.md
```

Start by copying the templates from `templates/`.

A completed case study must make it possible for another engineer to reproduce the baseline, see which hypotheses were considered, inspect the evidence, reproduce the optimization, validate correctness/quality, and understand rollback conditions.
