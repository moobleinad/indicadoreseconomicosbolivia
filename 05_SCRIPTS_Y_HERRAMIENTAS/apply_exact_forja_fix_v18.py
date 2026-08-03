import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
output_dir = os.path.join(root_dir, "tema_optimizado")

v18_path = os.path.join(output_dir, "v18_theme_optimizado.xml")

with open(v18_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

OLD_TESIS_CDN = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3R3HKNWS-yFvyk6bJ5lRP1bNaN6e5LHb4O1lb636MgMot-ty4_ouYM7-tYtjJ0rtDWhiKHHflwOUxYKKw3KWHVibRPTqEK6kJVg9i3VKPEGw_HJCceM1VG_ZjsbNHF3UY55yN9BsQjvqlkNXU5H88QkrEMkYOHtEKqFrWpk26YT0jrFJ1_4OApFAysCiL/s400/1guiasobreviviendoalatesisdanielsimons.webp"
EXACT_FORJA_ANVIL_CDN = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4mgMvkjLp_ScFp2lGYufq-rjZoGWDPO2EzxrxFwT8ox50IT2enqn0ViY1uZyPlbLYkE7p7km6JMTwrQ6NWwOp4NhyU8fBEhzK4C1rkDWNO6iZnqWj3-hBoKCY5gl1h9t4DxUz2ybzb3DLBHPV-yAs1DVqeLshADK6wvd6OyGzzTfQKZgoBoKVJVh82Ets/s600/1forjaserviciodanielsimons.webp"

if OLD_TESIS_CDN in xml_content:
    xml_content = xml_content.replace(OLD_TESIS_CDN, EXACT_FORJA_ANVIL_CDN)
    print("SUCCESSFULLY REPLACED OLD TESIS CDN WITH EXACT FORJA ANVIL CDN!")
else:
    print("ERROR: OLD TESIS CDN NOT FOUND IN v18_theme_optimizado.xml")

with open(v18_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(v18_path)
    print("SUCCESS: v18_theme_optimizado.xml updated and passed XML test!")
    file_size_kb = os.path.getsize(v18_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
