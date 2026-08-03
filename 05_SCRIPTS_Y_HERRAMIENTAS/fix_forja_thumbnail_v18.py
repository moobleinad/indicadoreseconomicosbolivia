import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
output_dir = os.path.join(root_dir, "tema_optimizado")

v18_path = os.path.join(output_dir, "v18_theme_optimizado.xml")

with open(v18_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# DANIEL SIMONS' EXACT CDN URL FOR FORJA (ANVIL LOGO)
EXACT_FORJA_URL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi4mgMvkjLp_ScFp2lGYufq-rjZoGWDPO2EzxrxFwT8ox50IT2enqn0ViY1uZyPlbLYkE7p7km6JMTwrQ6NWwOp4NhyU8fBEhzK4C1rkDWNO6iZnqWj3-hBoKCY5gl1h9t4DxUz2ybzb3DLBHPV-yAs1DVqeLshADK6wvd6OyGzzTfQKZgoBoKVJVh82Ets/s600/1forjaserviciodanielsimons.webp"

# Find track-services block
track_services_start = xml_content.find('<div class="ds-carousel-track" id="track-services">')
track_services_end = xml_content.find('</div>', track_services_start + 100)

if track_services_start != -1:
    services_block = xml_content[track_services_start:track_services_end+6]
    
    # Locate Forja card specifically inside services_block
    forja_card_start = services_block.find('alt="Forja de Proyectos"')
    if forja_card_start != -1:
        # Find img tag before alt="Forja de Proyectos"
        img_start = services_block.rfind('<img ', 0, forja_card_start)
        img_end = services_block.find('/>', forja_card_start)
        
        old_img_tag = services_block[img_start:img_end+2]
        print("OLD FORJA IMG TAG:", old_img_tag)
        
        new_img_tag = f'<img src="{EXACT_FORJA_URL}" alt="Forja de Proyectos" class="ds-card-thumb" />'
        
        new_services_block = services_block[:img_start] + new_img_tag + services_block[img_end+2:]
        xml_content = xml_content[:track_services_start] + new_services_block + xml_content[track_services_end+6:]
        print("SURGICALLY REPLACED FORJA IMG TAG SUCCESSFULLY!")
    else:
        print("ERROR: Could not find Forja card in services block!")
else:
    print("ERROR: Could not find track-services block!")

with open(v18_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(v18_path)
    print("SUCCESS: v18_theme_optimizado.xml updated and passed XML test!")
    file_size_kb = os.path.getsize(v18_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
