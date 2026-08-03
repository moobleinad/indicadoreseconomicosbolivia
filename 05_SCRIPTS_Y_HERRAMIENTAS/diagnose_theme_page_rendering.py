import os
import re

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v37_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v37_theme_optimizado.xml")
html_path = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS", "08.03_Dashboard_Indicadores_Economicos.html")

print("=== EMPIRICAL DIAGNOSTIC OF INDICATORS CODE & THEME ===")

# 1. Check local source file
if os.path.exists(html_path):
    size_kb = os.path.getsize(html_path) / 1024
    print(f"1. LOCAL SOURCE FILE '08.03_Dashboard_Indicadores_Economicos.html': INTACT! Size = {size_kb:.2f} KB")
else:
    print("1. LOCAL SOURCE FILE MISSING!")

# 2. Check XML Theme for page body CSS rules
with open(v37_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

print("2. CHECKING XML THEME FOR PAGE CSS AND CONTAINER STRUCTURE:")

# Look for .item-view, .static_page, .post-body CSS
page_css_matches = re.findall(r'(\.(?:item-view|static_page|post-body)[^{]*\{[^}]*\})', xml_content)
print(f"   Found {len(page_css_matches)} page CSS rules.")
for m in page_css_matches[:10]:
    print("   -", m.strip())

# Check where <b:include name='post'/> or <b:include name='main'/> is in the theme
has_post_include = "<b:include data='post' name='post'/>" in xml_content or "<b:include name='post'/>" in xml_content
print("3. B:INCLUDE POST IN XML:", "PRESENT" if has_post_include else "NOT FOUND")

# Check if there is any display:none or visibility:hidden applying to static pages
hidden_rules = [l for l in xml_content.split("\n") if "display: none" in l and ("page" in l.lower() or "post" in l.lower())]
print(f"4. HIDDEN RULES FOUND: {len(hidden_rules)}")
for hr in hidden_rules:
    print("   -", hr.strip())
