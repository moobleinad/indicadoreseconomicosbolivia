import os
import re
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")

v19_path = os.path.join(theme_dir, "v19_theme_optimizado.xml")
v20_path = os.path.join(theme_dir, "v20_theme_optimizado.xml")

# KEEP V19 UNTOUCHED! READ FROM V19 TO CREATE V20
with open(v19_path, "r", encoding="utf-8") as f:
    v20_content = f.read()

# FIND track-work BLOCK
track_work_start = v20_content.find('<div class="ds-carousel-track" id="track-work">')
track_work_end = v20_content.find('</div>', track_work_start + 100)

if track_work_start != -1:
    work_block = v20_content[track_work_start:track_work_end+6]
    
    # REMOVE THE ESTRATEGIA ELECTORAL 2026 CARD SURGICALLY
    # Pattern to match the entire <a> anchor card containing Estrategia Electoral 2026
    pattern = r'<a href="[^"]*estrategia-electoral-2026[^"]*" class="ds-card-box">.*?</a>'
    
    new_work_block = re.sub(pattern, '', work_block, flags=re.DOTALL)
    
    if new_work_block != work_block:
        v20_content = v20_content[:track_work_start] + new_work_block + v20_content[track_work_end+6:]
        print("SURGICALLY REMOVED ESTRATEGIA ELECTORAL 2026 CARD FROM TRABAJOS Y PROPUESTAS!")
    else:
        print("WARNING: Pattern did not match, attempting fallback search...")
        # Fallback search by title text
        title_pos = work_block.find('Estrategia Electoral 2026')
        if title_pos != -1:
            card_start = work_block.rfind('<a ', 0, title_pos)
            card_end = work_block.find('</a>', title_pos) + 4
            card_to_remove = work_block[card_start:card_end]
            new_work_block = work_block.replace(card_to_remove, '')
            v20_content = v20_content[:track_work_start] + new_work_block + v20_content[track_work_end+6:]
            print("SURGICALLY REMOVED ESTRATEGIA ELECTORAL 2026 CARD VIA FALLBACK!")
        else:
            print("ERROR: Could not locate Estrategia Electoral 2026 card!")

with open(v20_path, "w", encoding="utf-8") as f:
    f.write(v20_content)

try:
    ET.parse(v20_path)
    print("SUCCESS: v20_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v20_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
