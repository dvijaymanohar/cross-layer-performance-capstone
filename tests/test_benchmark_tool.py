import subprocess, sys

def test_benchmark_tool_runs():
    r=subprocess.run([sys.executable,"tools/benchmark.py","--warmup","1","--reps","2",sys.executable,"-c","pass"],capture_output=True,text=True)
    assert r.returncode==0
    assert "median_ms" in r.stdout
