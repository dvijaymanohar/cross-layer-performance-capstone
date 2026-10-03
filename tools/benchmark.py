#!/usr/bin/env python3
import argparse, json, statistics, subprocess, time

p=argparse.ArgumentParser(description="Repeat a command and report robust wall-clock statistics.")
p.add_argument("--warmup",type=int,default=3)
p.add_argument("--reps",type=int,default=15)
p.add_argument("--json",action="store_true")
p.add_argument("command",nargs=argparse.REMAINDER)
a=p.parse_args()
if not a.command: p.error("provide a command after --")
for _ in range(a.warmup): subprocess.run(a.command,check=True,stdout=subprocess.DEVNULL)
samples=[]
for _ in range(a.reps):
    t=time.perf_counter(); subprocess.run(a.command,check=True,stdout=subprocess.DEVNULL)
    samples.append((time.perf_counter()-t)*1000)
out={"boundary":"process wall clock","reps":a.reps,"median_ms":statistics.median(samples),
     "min_ms":min(samples),"max_ms":max(samples),"spread_ms":max(samples)-min(samples)}
print(json.dumps(out,indent=2) if a.json else out)
