import os
import re

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v37_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v37_theme_optimizado.xml")
v38_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v38_theme_optimizado.xml")

with open(v37_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

print("=== FIXING THEME XML WITH FLEXIBLE REGEX ===")

pattern = r"(<b:if cond=['\"]data:view\.isPost['\"]>\s*<b:include name=['\"]headerByline['\"]/>\s*<b:include data=['\"]post['\"] name=['\"]postTitle['\"]/>\s*<div class=['\"]post-body-container['\"]>)"
replacement = r"<b:if cond='data:view.isSingleItem'>\n<b:include name='headerByline'/>\n<b:include data='post' name='postTitle'/>\n<div class='post-body-container'>"

matches = re.findall(pattern, xml_content)
print(f"Found {len(matches)} matches via regex!")

fixed_xml = re.sub(pattern, replacement, xml_content)

with open(v38_path, "w", encoding="utf-8") as f:
    f.write(fixed_xml)

print(f"SUCCESS: GENERATED 'v38_theme_optimizado.xml' ({os.path.getsize(v38_path)/1024:.2f} KB)!")
