import os

v18_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\v18_theme_optimizado.xml"
with open(v18_path, "r", encoding="utf-8") as f:
    content = f.read()

s = content.find('track-services')
e = content.find('</section>', s)
print(content[s:e])
