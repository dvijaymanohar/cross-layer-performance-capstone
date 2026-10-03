import json, platform, shutil, subprocess, sys

def cmd(args):
    if not shutil.which(args[0]): return None
    try:return subprocess.check_output(args,text=True,stderr=subprocess.STDOUT,timeout=5).strip()
    except Exception as e:return f"error: {e}"

out={
 "platform":platform.platform(),
 "python":sys.version,
 "cpu":platform.processor(),
 "nvidia_smi":cmd(["nvidia-smi","--query-gpu=name,driver_version,memory.total","--format=csv"]),
 "nvcc":cmd(["nvcc","--version"]),
}
print(json.dumps(out,indent=2))
