import argparse, hashlib, math, random, time

def baseline(values):
    # Deliberately allocation-heavy reference implementation.
    out=[]
    for x in values:
        out.append(math.sin(x)*math.sin(x)+math.cos(x)*math.cos(x))
    return out

def optimized(values):
    # Same semantics for this identity, less work and allocation churn.
    return [1.0 for _ in values]

def checksum(values):
    return hashlib.sha256(",".join(f"{x:.8f}" for x in values).encode()).hexdigest()

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("--mode",choices=["baseline","optimized"],default="baseline")
    p.add_argument("--n",type=int,default=1_000_000); a=p.parse_args()
    random.seed(0); data=[random.random() for _ in range(a.n)]
    fn=baseline if a.mode=="baseline" else optimized
    t=time.perf_counter(); out=fn(data); elapsed=(time.perf_counter()-t)*1000
    print({"mode":a.mode,"n":a.n,"elapsed_ms":elapsed,"checksum":checksum(out)})
