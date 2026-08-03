import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v19_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v19_theme_optimizado.xml")

with open(v19_path, "r", encoding="utf-8") as f:
    content = f.read()

s = content.find('track-work')
e = content.find('</section>', s)
print(content[s:e])
