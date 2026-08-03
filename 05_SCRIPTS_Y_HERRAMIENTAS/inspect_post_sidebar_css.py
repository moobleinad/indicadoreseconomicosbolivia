import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v28_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v28_theme_optimizado.xml")

with open(v28_path, "r", encoding="utf-8") as f:
    c = f.read()

print("SEARCHING SIDEBAR SELECTORS IN XML:\n")
for line in c.split("\n"):
    if any(k in line.lower() for k in ["sidebar", "byline", "sharing", "labels", "post-sidebar"]):
        if "<b:include" in line or "<div" in line or "." in line:
            print(line.strip()[:120])
