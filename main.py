# make.fun image entry: copy the image beside this file to /output/entry.png.
# Runs with no network; the copy is byte-identical on every run.
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(os.path.join(here, "entry.png"), os.path.join(out, "entry.png"))
