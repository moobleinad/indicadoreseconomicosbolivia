import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")

v24_path = os.path.join(theme_dir, "v24_theme_optimizado.xml")
v25_path = os.path.join(theme_dir, "v25_theme_optimizado.xml")

with open(v24_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. CSS addition for .ds-section-link-below
css_addition = """
    .ds-section-title-wrap {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
    }
    .ds-section-link-below {
      display: inline-block !important;
      margin-top: 4px !important;
      font-size: 11.5px !important;
      font-weight: 700 !important;
      color: #ffffff !important;
      text-transform: uppercase !important;
      text-decoration: none !important;
      letter-spacing: 0.5px !important;
      opacity: 0.95;
      transition: opacity 0.2s ease;
    }
    .ds-section-link-below:hover {
      opacity: 1;
      color: #ffffff !important;
      text-decoration: underline !important;
    }
"""

# Inject CSS before </style>
style_end = content.find("</style>")
if style_end != -1:
    content = content[:style_end] + css_addition + content[style_end:]

# 2. Update the ds-section-header structure for sec-posts
old_posts_header = """<section class="ds-section-block" id="sec-posts">
                <div class="ds-section-header">
                  <h2>ÚLTIMAS <span>ENTRADAS DEL BLOG</span></h2>
                  <div class="ds-section-header-right" style="display:flex; align-items:center; gap:12px;">
                    <a href="https://www.danielsimons.xyz/search" class="ds-section-link">Ver todas las entradas &#10140;</a>
                    <div class="ds-nav-arrows">
                      <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', -1)">&#10094;</div>
                      <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', 1)">&#10095;</div>
                    </div>
                  </div>
                </div>"""

new_posts_header = """<section class="ds-section-block" id="sec-posts">
                <div class="ds-section-header">
                  <div class="ds-section-title-wrap">
                    <h2>ÚLTIMAS <span>ENTRADAS DEL BLOG</span></h2>
                    <a href="https://www.danielsimons.xyz/search" class="ds-section-link-below">VER TODAS LAS ENTRADAS &#10140;</a>
                  </div>
                  <div class="ds-nav-arrows">
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', -1)">&#10094;</div>
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', 1)">&#10095;</div>
                  </div>
                </div>"""

if old_posts_header in content:
    content = content.replace(old_posts_header, new_posts_header)
    print("SUCCESS: Updated ÚLTIMAS ENTRADAS DEL BLOG header!")
else:
    # Try HTML entity variant if exact string wasn't matched
    print("Exact string match failed, trying regex replacement for sec-posts header...")
    import re
    pattern = r'<section class="ds-section-block" id="sec-posts">\s*<div class="ds-section-header">.*?<div class="ds-nav-arrows">'
    replacement = """<section class="ds-section-block" id="sec-posts">
                <div class="ds-section-header">
                  <div class="ds-section-title-wrap">
                    <h2>ÚLTIMAS <span>ENTRADAS DEL BLOG</span></h2>
                    <a href="https://www.danielsimons.xyz/search" class="ds-section-link-below">VER TODAS LAS ENTRADAS &#10140;</a>
                  </div>
                  <div class="ds-nav-arrows">"""
    content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    print(f"Replaced {count} instances.")

# 3. Ensure banner text is uppercase "ACTUALIZADOS TODOS LOS DÍAS"
old_sub = 'Actualizados todos los d&#237;as'
new_sub = 'ACTUALIZADOS TODOS LOS D&#205;AS'
if old_sub in content:
    content = content.replace(old_sub, new_sub)

with open(v25_path, "w", encoding="utf-8") as f:
    f.write(content)

try:
    ET.parse(v25_path)
    print(f"XML Validation: SUCCESS! Created v25_theme_optimizado.xml ({os.path.getsize(v25_path)/1024:.2f} KB)")
except Exception as e:
    print("XML Validation ERROR:", e)
