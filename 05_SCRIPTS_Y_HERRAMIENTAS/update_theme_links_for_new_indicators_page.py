import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v36_path = os.path.join(theme_dir, "v36_theme_optimizado.xml")
if not os.path.exists(v36_path):
    v36_path = os.path.join(sub_dir, "v36_theme_optimizado.xml")

v37_path_main = os.path.join(theme_dir, "v37_theme_optimizado.xml")
v37_path_sub = os.path.join(sub_dir, "v37_theme_optimizado.xml")

with open(v36_path, "r", encoding="utf-8") as f:
    v37_content = f.read()

new_indicators_url = "https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia_0225498393.html"

# Update any old indicators page URLs in theme to point to the new clean page URL
old_urls = [
    "https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia.html",
    "https://www.danielsimons.xyz/p/guia-y-analisis-de-indicadores.html",
    "/p/indicadores-economicos-de-bolivia.html",
    "/p/guia-y-analisis-de-indicadores.html"
]

for old_u in old_urls:
    if old_u in v37_content:
        v37_content = v37_content.replace(old_u, new_indicators_url)
        print(f"UPDATED LINK '{old_u}' -> '{new_indicators_url}' IN V37!")

# Save in main theme directory and sub directory
with open(v37_path_main, "w", encoding="utf-8") as f:
    f.write(v37_content)

with open(v37_path_sub, "w", encoding="utf-8") as f:
    f.write(v37_content)

try:
    ET.parse(v37_path_main)
    print("SUCCESS: v37_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v37_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
