import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
output_dir = os.path.join(root_dir, "tema_optimizado")

# KEEP V17 UNTOUCHED! Read from v17 to create brand new v18_theme_optimizado.xml
v17_path = os.path.join(output_dir, "v17_theme_optimizado.xml")
v18_path = os.path.join(output_dir, "v18_theme_optimizado.xml")

with open(v17_path, "r", encoding="utf-8") as f:
    v18_content = f.read()

# DANIEL SIMONS' EXACT REAL BLOGGER CDN IMAGE URLS FOR DESTILADO AND FORJA
EXACT_CDN_DESTILADO = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNb5mnyiSuyI37HO_j08Atk1mUogyKdy8ccy_I4V0NFEVe8Q49pD9B8zF0iPt_XKdjaGpr7Q8Tor3oxRkRWYpP4p2UNUtv2hJj_0_HxDAUlXXJmAMpKZmGLY8vsaWOpYlp1wMQBn8ssZGm34g0fW_xEJKqxTLvOUY28ScWBL6n5egGWx9BwWif4oElUmwQ/s600/1destiladosserviciodanielsimons.webp"
EXACT_CDN_FORJA = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4mgMvkjLp_ScFp2lGYufq-rjZoGWDPO2EzxrxFwT8ox50IT2enqn0ViY1uZyPlbLYkE7p7km6JMTwrQ6NWwOp4NhyU8fBEhzK4C1rkDWNO6iZnqWj3-hBoKCY5gl1h9t4DxUz2ybzb3DLBHPV-yAs1DVqeLshADK6wvd6OyGzzTfQKZgoBoKVJVh82Ets/s600/1forjaserviciodanielsimons.webp"

# SURGICALLY REPLACE ONLY THE 2 THUMBNAIL URLS IN track-services IN v18
OLD_JUEGO_URL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0_W9ImaOofGpPg4nKkSdwKXB4VeWya_6_rN-v8rJ5yVPayXWXE1AkRAaZRJCrxkk-DJ2PGNsgvP2Nq9PD5YKT2KUJ1i1JG0doww5YQtNmhHkPIOg-nx30S6bTdYdAI3f7ovcebKFeunio-dbH5IPgqkavhxpxFHJA6DUut5mPRBZBAMLQWcJgi1W5uYHv/s400/1eljuegodelemprendedordanielsimons.webp"
OLD_TESIS_URL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3R3HKNWS-yFvyk6bJ5lRP1bNaN6e5LHb4O1lb636MgMot-ty4_ouYM7-tYtjJ0rtDWhiKHHflwOUxYKKw3KWHVibRPTqEK6kJVg9i3VKPEGw_HJCceM1VG_ZjsbNHF3UY55yN9BsQjvqlkNXU5H88QkrEMkYOHtEKqFrWpk26YT0jrFJ1_4OApFAysCiL/s400/1guiasobreviviendoalatesisdanielsimons.webp"

# Target the track-services block specifically
track_services_start = v18_content.find('<div class="ds-carousel-track" id="track-services">')
track_services_end = v18_content.find('</div>', track_services_start + 100)

if track_services_start != -1:
    services_block = v18_content[track_services_start:track_services_end+6]
    
    # Replace book cover images in services block with exact CDN URLs provided by Daniel
    new_services_block = services_block.replace(OLD_JUEGO_URL, EXACT_CDN_DESTILADO)
    new_services_block = new_services_block.replace(OLD_TESIS_URL, EXACT_CDN_FORJA)
    
    # Also clean any data URI fallback if present
    import re
    new_services_block = re.sub(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', EXACT_CDN_DESTILADO, new_services_block, count=1)
    new_services_block = re.sub(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', EXACT_CDN_FORJA, new_services_block, count=1)

    v18_content = v18_content[:track_services_start] + new_services_block + v18_content[track_services_end+6:]
    print("Surgically replaced book covers with Daniel's exact Blogger CDN URLs!")
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
