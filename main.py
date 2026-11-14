# make.fun image entry: copy the image beside this file to /output/entry.png.
# Runs with no network; the copy is byte-identical on every run.
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
src = os.path.join(here, "entry.png")
dst = os.path.join(out, "entry.png")
shutil.copyfile(src, dst)
# Fail loudly if the copy is short: the judge must see exactly these bytes.
if os.path.getsize(dst) != os.path.getsize(src):
    raise SystemExit("entry.png copy is incomplete")
