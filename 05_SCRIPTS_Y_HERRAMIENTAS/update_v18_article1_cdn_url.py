import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v18_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v18_theme_optimizado.xml")

with open(v18_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# DANIEL'S LIVE BLOGGER CDN IMAGE URL FOR ARTICLE 1
EXACT_ART1_CDN_URL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTRsBXTzWUk5H0_cbWuoZEUxMO2k6wcwRBfEa9odQuS3cjaygEFoZAKHs1DWbd8U1ywJWCewvlR4-nG7V1wWKZ6vftDx2LgZEqLQDrNm2pa-unaRmxUQ02Zq_BaCFFWkAHesJACiwSjSt4r1OdRX9ItME-wl3QdRbMU7bEcTOQZ2tLOJ1QK5JzhPa2f0Fo/s600/foto_articulo1_bth_oficial.webp"

# Find track-posts block in v18 XML
track_posts_start = xml_content.find('<div class="ds-carousel-track" id="track-posts">')
track_posts_end = xml_content.find('</div>', track_posts_start + 100)

if track_posts_start != -1:
    posts_block = xml_content[track_posts_start:track_posts_end+6]
    
    # Replace data URI or raw URL with Daniel's exact Blogger CDN URL
    import re
    new_posts_block = re.sub(r'src="[^"]+"', f'src="{EXACT_ART1_CDN_URL}"', posts_block, count=1)
    
    xml_content = xml_content[:track_posts_start] + new_posts_block + xml_content[track_posts_end+6:]
    print("Surgically updated Article 1 thumbnail with Daniel's Blogger CDN URL!")
else:
    print("ERROR: Could not find track-posts block!")

with open(v18_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(v18_path)
    print("SUCCESS: v18_theme_optimizado.xml updated and passed XML test!")
    file_size_kb = os.path.getsize(v18_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
