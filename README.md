# Cross-Layer Performance Capstone

One deep, reproducible performance investigation connecting application behavior to runtime/framework decisions, generated code/kernels, hardware evidence, and production impact.

## Senior reasoning loop
objective → baseline → reproduce → localize → evidence → competing hypotheses → change one variable → validate → stress/soak → quantify trade-offs → rollback/next step.

## Start
1. Copy `templates/BENCHMARK_CONTRACT.md` to your case-study directory.
2. Reuse a workload from an earlier repository.
3. Run `python tools/benchmark.py --help`.
4. Maintain `templates/HYPOTHESIS_LOG.md` as evidence arrives.
5. Finish with an interview-ready case study.

No benchmark result or claimed speedup belongs here unless it was actually measured and reproducible.
