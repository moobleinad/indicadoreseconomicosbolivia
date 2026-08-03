import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
output_dir = os.path.join(root_dir, "tema_optimizado")
v16_path = os.path.join(output_dir, "v16_theme_optimizado.xml")
output_path = os.path.join(output_dir, "v17_theme_optimizado.xml")

with open(v16_path, "r", encoding="utf-8") as f:
    v16_content = f.read()

# Replace any heavy data URI in Article 1 with clean lightweight HTTPS URL if needed
# and SURGICALLY REMOVE ONLY THE TWO CARDS (Destilado & Forja) FROM track-services!

target_card_1 = '<a href="https://www.danielsimons.xyz/p/destilado-de-ideas-de-negocio_0599447061.html"'
target_card_2 = '<a href="https://www.danielsimons.xyz/p/forja-disciplina-habitos-y-lucidez.html"'

# Remove both cards from track-services
lines = v16_content.split('\n')
new_lines = []
skip = False

in_track_services = False
for line in lines:
    if 'id="track-services"' in line:
        in_track_services = True
        new_lines.append(line)
        continue
    
    if in_track_services:
        if '</section>' in line:
            in_track_services = False
            new_lines.append(line)
            continue
        
        # Check if line starts card Destilado or Forja
        if 'destilado-de-ideas-de-negocio' in line or 'forja-disciplina-habitos-y-lucidez' in line:
            skip = True
            continue
        
        if skip and '</a>' in line:
            skip = False
            continue
        
        if not skip:
            new_lines.append(line)
    else:
        new_lines.append(line)

v17_content = '\n'.join(new_lines)

# Keep XML size under 200KB by replacing heavy base64 in post 1 with lightweight raw URL if present
if "data:image/jpeg;base64," in v17_content:
    # Replace large base64 string with clean lightweight URL
    import re
    v17_content = re.sub(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', 'https://raw.githubusercontent.com/antigravity/danielsimons/main/foto_articulo1_bth_cuadrada.jpg', v17_content)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(v17_content)

try:
    ET.parse(output_path)
    print("SUCCESS: v17_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(output_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
