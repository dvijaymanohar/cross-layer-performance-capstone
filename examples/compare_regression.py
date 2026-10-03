import json, statistics, subprocess, sys, time

def run(mode,reps=7):
    times=[]; checksum=None
    for _ in range(reps):
        p=subprocess.run([sys.executable,"examples/regression_workload.py","--mode",mode,"--n","300000"],
                         check=True,capture_output=True,text=True)
        # Use process-level measurement to practice defining a boundary.
        # The workload also prints its internal timer for comparison.
        d=eval(p.stdout.strip(),{"__builtins__":{}})
        times.append(d["elapsed_ms"]); checksum=d["checksum"]
    return {"median_ms":statistics.median(times),"min_ms":min(times),"max_ms":max(times),"checksum":checksum}

base=run("baseline"); opt=run("optimized")
assert base["checksum"]==opt["checksum"],"correctness regression"
print(json.dumps({"baseline":base,"optimized":opt,"speedup":base["median_ms"]/opt["median_ms"]},indent=2))
print("This is a teaching workload; do not generalize its speedup to real systems.")
