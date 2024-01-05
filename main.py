import os
import subprocess
import shutil
if os.path.exists("type_cookie.txt"):
    os.remove("type_cookie.txt")
if os.path.exists("run.txt"):
    os.remove("run.txt")
if os.path.exists("results") and os.path.isdir("results"):
    subdirectories = [f.path for f in os.scandir("results") if f.is_dir()]
    for subdir in subdirectories:
        shutil.rmtree(subdir)
if os.path.exists("download") and os.path.isdir("download"):
    # Use shutil.rmtree to remove the entire folder and its contents
    shutil.rmtree("download")
subprocess.run("""streamlit run app.py""",timeout=1200)