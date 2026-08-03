import os
import re
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v33_path = os.path.join(theme_dir, "v33_theme_optimizado.xml")
if not os.path.exists(v33_path):
    v33_path = os.path.join(sub_dir, "v33_theme_optimizado.xml")

v34_path_main = os.path.join(theme_dir, "v34_theme_optimizado.xml")
v34_path_sub = os.path.join(sub_dir, "v34_theme_optimizado.xml")

with open(v33_path, "r", encoding="utf-8") as f:
    v34_content = f.read()

cdn_poster_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp"

# REPLACE ALL OCCURRENCES OF AVvXsEix_default_preview.jpg WITH THE REAL CDN POSTER URL
old_default = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEix_default_preview.jpg"

if old_default in v34_content:
    v34_content = v34_content.replace(old_default, cdn_poster_url)
    print("REPLACED OLD DEFAULT PREVIEW URL WITH HIGH-RES CDN POSTER URL!")

# Save in main theme directory and sub directory
with open(v34_path_main, "w", encoding="utf-8") as f:
    f.write(v34_content)

with open(v34_path_sub, "w", encoding="utf-8") as f:
    f.write(v34_content)

try:
    ET.parse(v34_path_main)
    print("SUCCESS: v34_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v34_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
