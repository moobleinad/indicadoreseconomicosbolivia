import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v20_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v20_theme_optimizado.xml")

with open(v20_path, "r", encoding="utf-8") as f:
    content = f.read()

s = content.find('ÚLTIMAS ENTRADAS')
if s != -1:
    e = content.find('</section>', s)
    print(content[s-200:e])
else:
    s2 = content.find('ENTRADAS')
    print("Found ENTRADAS at:", s2)
    print(content[s2-100:s2+500])
