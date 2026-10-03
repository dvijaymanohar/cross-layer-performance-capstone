# Compiler, runtime, and generated code

Inspect this layer **only when higher-level evidence points here**.

## Concepts
compiler vs runtime; code generation; intermediate representation (IR); PTX; SASS; JIT vs AOT; optimization passes; vectorization; inlining; graph/operator fusion.

## Investigation chain
application/framework → graph/runtime/provider → generated/fused operator or library tactic → PTX/SASS/kernel → hardware counters.

## Evidence examples
- provider/operator placement
- graph fusion decisions
- runtime/compiler logs
- library/tactic selection
- generated kernel/IR
- PTX/SASS
- instruction mix
- register use/spills
- memory operations
- launch count
- JIT/AOT startup effects

Do not inspect assembly by default. Start from a performance symptom, localize the layer, then descend only as far as needed to distinguish hypotheses.
