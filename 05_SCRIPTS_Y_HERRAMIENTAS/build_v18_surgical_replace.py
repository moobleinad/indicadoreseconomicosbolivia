import os
import base64
import xml.etree.ElementTree as ET
from PIL import Image

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
output_dir = os.path.join(root_dir, "tema_optimizado")

# KEEP V17 UNTOUCHED! Read from v17 to create brand new v18_theme_optimizado.xml
v17_path = os.path.join(output_dir, "v17_theme_optimizado.xml")
v18_path = os.path.join(output_dir, "v18_theme_optimizado.xml")

with open(v17_path, "r", encoding="utf-8") as f:
    v18_content = f.read()

# Compress Destilado & Forja official 1:1 thumbnails to 240x240 lightweight JPGs (~10 KB each)
thumb_dest_path = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_destilado_1785593994402.jpg"
thumb_forj_path = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_forja_1785594011419.jpg"

dest_comp_path = os.path.join(root_dir, "destilado_official_min.jpg")
forj_comp_path = os.path.join(root_dir, "forja_official_min.jpg")

im_dest = Image.open(thumb_dest_path).convert("RGB")
im_dest.thumbnail((240, 240))
im_dest.save(dest_comp_path, "JPEG", quality=50)

im_forj = Image.open(thumb_forj_path).convert("RGB")
im_forj.thumbnail((240, 240))
im_forj.save(forj_comp_path, "JPEG", quality=50)

with open(dest_comp_path, "rb") as f:
    b64_dest = base64.b64encode(f.read()).decode("utf-8")

with open(forj_comp_path, "rb") as f:
    b64_forj = base64.b64encode(f.read()).decode("utf-8")

data_uri_destilado = f"data:image/jpeg;base64,{b64_dest}"
data_uri_forja = f"data:image/jpeg;base64,{b64_forj}"

print(f"Compressed Destilado b64 len: {len(b64_dest)}")
print(f"Compressed Forja b64 len: {len(b64_forj)}")

# SURGICALLY REPLACE ONLY THE 2 THUMBNAIL URLS IN track-services IN v18
REAL_IMG_JUEGO = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0_W9ImaOofGpPg4nKkSdwKXB4VeWya_6_rN-v8rJ5yVPayXWXE1AkRAaZRJCrxkk-DJ2PGNsgvP2Nq9PD5YKT2KUJ1i1JG0doww5YQtNmhHkPIOg-nx30S6bTdYdAI3f7ovcebKFeunio-dbH5IPgqkavhxpxFHJA6DUut5mPRBZBAMLQWcJgi1W5uYHv/s400/1eljuegodelemprendedordanielsimons.webp"
REAL_IMG_TESIS = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3R3HKNWS-yFvyk6bJ5lRP1bNaN6e5LHb4O1lb636MgMot-ty4_ouYM7-tYtjJ0rtDWhiKHHflwOUxYKKw3KWHVibRPTqEK6kJVg9i3VKPEGw_HJCceM1VG_ZjsbNHF3UY55yN9BsQjvqlkNXU5H88QkrEMkYOHtEKqFrWpk26YT0jrFJ1_4OApFAysCiL/s400/1guiasobreviviendoalatesisdanielsimons.webp"

# Target the track-services block specifically
track_services_start = v18_content.find('<div class="ds-carousel-track" id="track-services">')
track_services_end = v18_content.find('</div>', track_services_start + 100)

if track_services_start != -1:
    services_block = v18_content[track_services_start:track_services_end+6]
    
    # Replace book cover images in services block with official 1:1 thumbnails
    new_services_block = services_block.replace(REAL_IMG_JUEGO, data_uri_destilado)
    new_services_block = new_services_block.replace(REAL_IMG_TESIS, data_uri_forja)
    
    v18_content = v18_content[:track_services_start] + new_services_block + v18_content[track_services_end+6:]
    print("Surgically replaced book covers with official Destilado & Forja thumbnails in track-services!")
else:
    print("ERROR FINDING track-services BLOCK")

with open(v18_path, "w", encoding="utf-8") as f:
    f.write(v18_content)

try:
    ET.parse(v18_path)
    print("SUCCESS: v18_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v18_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
