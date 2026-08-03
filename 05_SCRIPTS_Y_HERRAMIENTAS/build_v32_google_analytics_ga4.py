import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v31_path = os.path.join(theme_dir, "v31_theme_optimizado.xml")
if not os.path.exists(v31_path):
    v31_path = os.path.join(sub_dir, "v31_theme_optimizado.xml")

v32_path_main = os.path.join(theme_dir, "v32_theme_optimizado.xml")
v32_path_sub = os.path.join(sub_dir, "v32_theme_optimizado.xml")

# KEEP V31 UNTOUCHED! READ FROM V31 TO CREATE V32
with open(v31_path, "r", encoding="utf-8") as f:
    v32_content = f.read()

# GA4 TRACKING CODE FOR DANIEL SIMONS (G-LL1KM8J1TP)
ga4_code = """
  <!-- Google tag (gtag.js) GA4 DANIEL SIMONS -->
  <script async='async' src='https://www.googletagmanager.com/gtag/js?id=G-LL1KM8J1TP'></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', 'G-LL1KM8J1TP');
  </script>
"""

# Insert GA4 code right after <head>
head_open_pos = v32_content.find("<head>")
if head_open_pos != -1:
    insert_pos = head_open_pos + len("<head>")
    v32_content = v32_content[:insert_pos] + "\n" + ga4_code + v32_content[insert_pos:]
    print("SUCCESSFULLY INSERTED GA4 TRACKING CODE IN HEAD OF V32!")

# Save in main theme directory and sub directory
with open(v32_path_main, "w", encoding="utf-8") as f:
    f.write(v32_content)

with open(v32_path_sub, "w", encoding="utf-8") as f:
    f.write(v32_content)

try:
    ET.parse(v32_path_main)
    print("SUCCESS: v32_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v32_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
