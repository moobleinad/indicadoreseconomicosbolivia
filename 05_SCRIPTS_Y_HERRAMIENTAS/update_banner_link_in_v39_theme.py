import os
import re

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v38_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v38_theme_optimizado.xml")
v39_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v39_theme_optimizado.xml")

with open(v38_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

target_url = "https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia_0349188327.html"

print("=== UPDATING BANNER LINKS IN THEME XML ===")

# Search for any href linking to /p/indicadores-economicos... or /p/guia-y-analisis...
matches = re.findall(r'<a[^>]*href=[\'"][^\'"]*indicadores[^\'"]*[\'"][^>]*>', xml_content, re.IGNORECASE)
print(f"Found {len(matches)} banner link tags in XML:")
for m in matches:
    print(" -", m)

# Replace all occurrences of old indicators page URLs in href attributes with target_url
new_xml = xml_content

# Match any href pointing to an indicators page
new_xml = re.sub(
    r'href=[\'"]https://www\.danielsimons\.xyz/p/[^\'"]*indicadores[^\'"]*[\'"]',
    f'href="{target_url}"',
    new_xml,
    flags=re.IGNORECASE
)

new_xml = re.sub(
    r'href=[\'"]/p/[^\'"]*indicadores[^\'"]*[\'"]',
    f'href="{target_url}"',
    new_xml,
    flags=re.IGNORECASE
)

with open(v39_path, "w", encoding="utf-8") as f:
    f.write(new_xml)

print(f"SUCCESS: CREATED 'v39_theme_optimizado.xml' WITH UPDATED BANNER LINK ({os.path.getsize(v39_path)/1024:.2f} KB)!")
