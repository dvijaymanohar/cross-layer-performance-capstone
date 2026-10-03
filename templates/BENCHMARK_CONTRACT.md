# Benchmark contract

## User-visible problem
What is slow, costly, or unstable?

## Primary metric
Latency, throughput, cost/request, energy, or another explicit metric.

## Boundary
Exactly what starts and stops the timer?

## Workload
Input shape/distribution, batch/concurrency, precision, warm/cold state.

## Environment
OS, CPU, GPU, topology, driver, CUDA/runtime/framework/compiler versions and build flags.

## Correctness/quality constraint
Reference output, numerical tolerance, task metric, and failure criteria.

## Method
Warm-up, repetitions, synchronization, median/spread, cold-start handling.

## Safety/reliability constraints
Memory ceiling, error-rate/SLO boundary, queue limits, timeout policy, rollback condition.
