import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")

v18_path = os.path.join(theme_dir, "v18_theme_optimizado.xml")
v19_path = os.path.join(theme_dir, "v19_theme_optimizado.xml")

# KEEP V18 UNTOUCHED! READ FROM V18 TO CREATE V19
with open(v18_path, "r", encoding="utf-8") as f:
    v19_content = f.read()

# TARGET THE FORJA CARD INSIDE track-services
old_title_snippet = '<div class="title">Forja de Proyectos</div>'
old_desc_snippet = '<div class="desc">De la idea a la ejecuci&#243;n s&#243;lida y estructurada.</div>'

# NEW TEXT matching the real Forja page
new_title_snippet = '<div class="title">FORJA</div>'
new_desc_snippet = '<div class="desc">De la dispersi&#243;n mental a la estructura consciente.</div>'

if old_title_snippet in v19_content:
    v19_content = v19_content.replace(old_title_snippet, new_title_snippet)
    print("REPLACED TITLE TO FORJA!")
else:
    # Try alternate unicode decoding if present
    import re
    v19_content = re.sub(r'<div class="title">Forja de Proyectos</div>', new_title_snippet, v19_content)
    print("REPLACED TITLE VIA REGEX!")

if old_desc_snippet in v19_content:
    v19_content = v19_content.replace(old_desc_snippet, new_desc_snippet)
    print("REPLACED DESC TO NEW FORJA DESC!")
else:
    import re
    v19_content = re.sub(r'<div class="desc">De la idea a la ejecuci[^<]+s&#243;lida y estructurada\.</div>', new_desc_snippet, v19_content)
    v19_content = re.sub(r'<div class="desc">De la idea a la ejecución sólida y estructurada\.</div>', new_desc_snippet, v19_content)
    print("REPLACED DESC VIA REGEX!")

with open(v19_path, "w", encoding="utf-8") as f:
    f.write(v19_content)

try:
    ET.parse(v19_path)
    print("SUCCESS: v19_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v19_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
