import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v21_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v21_theme_optimizado.xml")

with open(v21_path, "r", encoding="utf-8") as f:
    content = f.read()

s = content.find('.ds-section-header')
print("DS SECTION HEADER CSS:")
print(content[s:s+1500])

s_link = content.find('.ds-section-link')
print("\nDS SECTION LINK CSS:")
print(content[s_link:s_link+800])
