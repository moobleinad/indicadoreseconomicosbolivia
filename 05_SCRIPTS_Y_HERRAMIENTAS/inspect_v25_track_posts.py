import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v25_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v25_theme_optimizado.xml")

with open(v25_path, "r", encoding="utf-8") as f:
    c = f.read()

pos = c.find('id="track-posts"')
if pos != -1:
    print("TRACK POSTS CONTENT:\n", c[pos:pos+2000])
else:
    print("NOT FOUND id=track-posts")
