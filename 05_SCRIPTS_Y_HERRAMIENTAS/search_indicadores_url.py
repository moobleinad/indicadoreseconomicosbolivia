import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"

for r, d, files in os.walk(root_dir):
    for f in files:
        if f.endswith(".xml") or f.endswith(".md") or f.endswith(".txt") or f.endswith(".json"):
            fp = os.path.join(r, f)
            try:
                with open(fp, "r", encoding="utf-8", errors="ignore") as file:
                    c = file.read()
                    if "indicadores" in c.lower():
                        print("FOUND IN:", fp)
                        for line in c.split("\n"):
                            if "indicadores" in line.lower() and ("http" in line.lower() or "html" in line.lower()):
                                print("  LINE:", line.strip())
            except Exception as e:
                pass
