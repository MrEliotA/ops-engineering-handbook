#!/usr/bin/env python3
import argparse, datetime as dt, json, socket, subprocess
from pathlib import Path

def run(name, argv, outdir):
    p=subprocess.run(argv, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=30, check=False)
    target=outdir/f"{name}.txt"; target.write_text(p.stdout, encoding="utf-8", errors="replace")
    return {"name":name,"command":argv,"exit_code":p.returncode,"output_file":target.name}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--out", default=None); args=ap.parse_args()
    stamp=dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out=Path(args.out or f"evidence/{socket.gethostname()}-{stamp}"); out.mkdir(parents=True, exist_ok=True)
    checks=[]
    for name,argv in [("uptime",["uptime"]),("vmstat",["vmstat","-w","1","5"]),("ss",["ss","-s"]),("df",["df","-hT"])]:
        try: checks.append(run(name,argv,out))
        except (FileNotFoundError, subprocess.TimeoutExpired): pass
    manifest={"captured_at":dt.datetime.now(dt.timezone.utc).isoformat(),"host":socket.gethostname(),"checks":checks}
    (out/"manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(out)
if __name__=="__main__": main()
