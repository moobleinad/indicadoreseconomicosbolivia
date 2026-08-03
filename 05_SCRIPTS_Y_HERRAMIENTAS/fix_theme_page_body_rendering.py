import os
import re

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v37_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v37_theme_optimizado.xml")
v38_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v38_theme_optimizado.xml")

with open(v37_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

print("=== FIXING THEME XML PAGE BODY RENDERING ===")

# Search where post.body is rendered in the XML
matches = list(re.finditer(r'(<b:if[^>]*>\s*<div[^>]*post-body[^>]*>.*?data:post\.body.*?</b:if>)', xml_content, re.DOTALL))
print(f"Found {len(matches)} post.body conditional blocks.")

# Let's inspect the conditionals around data:post.body
body_blocks = re.findall(r'<b:if cond=[\'"]([^\'"]+)[\'"][^>]*>\s*<div[^>]*class=[\'"][^\'"]*post-body[^\'"]*[\'"]', xml_content)
print("Conditionals wrapping post-body:", body_blocks)

# We need <data:post.body/> to render on both isPost AND isPage (or isSingleItem)!
# Replace any condition wrapping post-body that checks ONLY isPost with isSingleItem or (isPost || isPage)
new_xml = xml_content

# Look for <b:if cond='data:view.isPost'> that wraps post-body
def replace_post_body_cond(match):
    full_block = match.group(0)
    # Change isPost to (data:view.isPost or data:view.isPage) or isSingleItem
    fixed_block = re.sub(r'cond=[\'"]data:view\.isPost[\'"]', "cond='data:view.isSingleItem'", full_block)
    return fixed_block

new_xml = re.sub(r'(<b:if cond=[\'"]data:view\.isPost[\'"][^>]*>\s*<div[^>]*class=[\'"][^\'"]*post-body.*?data:post\.body.*?</div\s*>\s*</b:if>)', replace_post_body_cond, new_xml, flags=re.DOTALL)

with open(v38_path, "w", encoding="utf-8") as f:
    f.write(new_xml)

print(f"SUCCESS: SAVED FIXED THEME XML TO 'v38_theme_optimizado.xml' ({os.path.getsize(v38_path)/1024:.2f} KB)!")
