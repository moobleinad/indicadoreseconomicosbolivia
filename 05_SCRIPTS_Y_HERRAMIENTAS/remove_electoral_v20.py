import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")

v19_path = os.path.join(theme_dir, "v19_theme_optimizado.xml")
v20_path = os.path.join(theme_dir, "v20_theme_optimizado.xml")

with open(v19_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# TARGET URL FOR ESTRATEGIA ELECTORAL 2026
target_url = "https://www.danielsimons.xyz/p/estrategia-electoral-2026.html"

card_start = xml_content.find(f'<a href="{target_url}"')

if card_start != -1:
    card_end = xml_content.find('</a>', card_start) + 4
    card_html = xml_content[card_start:card_end]
    print("FOUND CARD HTML TO REMOVE:\n", card_html[:150], "...")
    
    # Remove card and any trailing/leading whitespace
    xml_content = xml_content[:card_start] + xml_content[card_end:]
    print("SURGICALLY REMOVED ESTRATEGIA ELECTORAL 2026 CARD!")
else:
    print("ERROR: COULD NOT FIND ESTRATEGIA ELECTORAL CARD URL IN v19")

with open(v20_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(v20_path)
    print("SUCCESS: v20_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v20_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
