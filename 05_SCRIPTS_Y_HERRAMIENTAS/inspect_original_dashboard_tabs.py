import os
import re

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")

files = os.listdir(ind_dir)
print("Files in 08_INDICADORES_ECONOMICOS:", files)

for f in files:
    if f.endswith(".html") or f.endswith(".js") or f.endswith(".json"):
        fp = os.path.join(ind_dir, f)
        print(f"\n--- FILE: {f} ({os.path.getsize(fp)} bytes) ---")
