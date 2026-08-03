import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")

for r, d, files in os.walk(ind_dir):
    for f in files:
        fp = os.path.join(r, f)
        print("FILE:", fp)
        try:
            with open(fp, "r", encoding="utf-8", errors="ignore") as file:
                c = file.read()
                print("CONTENT SNIPPET:\n", c[:500])
                print("="*50)
        except Exception as e:
            print("ERROR READING:", e)
