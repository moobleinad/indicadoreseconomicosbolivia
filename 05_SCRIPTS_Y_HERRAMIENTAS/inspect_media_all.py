import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v21_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v21_theme_optimizado.xml")

with open(v21_path, "r", encoding="utf-8") as f:
    content = f.read()

s = content.find('@media')
while s != -1:
    print("--- MEDIA QUERY AT", s, "---")
    print(content[s:s+400])
    s = content.find('@media', s+1)
