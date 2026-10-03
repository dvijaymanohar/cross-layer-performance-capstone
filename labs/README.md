# Senior diagnosis practice

Start with the deliberately simple regression exercise:

```bash
python scripts/capture_environment.py
python examples/regression_workload.py --mode baseline
python examples/regression_workload.py --mode optimized
python examples/compare_regression.py
```

Then repeat the method on a real workload from another repository.

## Required reasoning
1. Define the user-visible symptom and measurement boundary.
2. Capture a trusted baseline.
3. State at least two competing bottleneck hypotheses.
4. Collect evidence that can distinguish them.
5. Change one major factor.
6. Re-measure and re-profile.
7. Re-run correctness or quality validation.
8. Check boundary/stress behavior.
9. Document trade-offs and rollback criteria.
10. Explain what you would investigate next.

The example optimization is intentionally obvious; the goal is to practice the evidence structure before applying it to CUDA/inference/serving work.
