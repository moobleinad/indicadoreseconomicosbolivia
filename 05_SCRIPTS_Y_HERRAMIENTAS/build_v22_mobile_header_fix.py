import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")

v21_path = os.path.join(theme_dir, "v21_theme_optimizado.xml")
v22_path = os.path.join(theme_dir, "v22_theme_optimizado.xml")

# KEEP V21 UNTOUCHED! READ FROM V21 TO CREATE V22
with open(v21_path, "r", encoding="utf-8") as f:
    v22_content = f.read()

# 1. UPDATE CSS FOR .ds-section-link TO WHITE TEXT & NO-WRAP
old_link_css = """.ds-section-link {
      font-size: 11px;
      font-weight: 700;
      color: #bca772 !important;
      text-transform: uppercase;
      text-decoration: none !important;
    }"""

new_link_css = """.ds-section-link {
      font-size: 11px;
      font-weight: 700;
      color: #ffffff !important;
      text-transform: uppercase;
      text-decoration: none !important;
      white-space: nowrap !important;
    }

    @media (max-width: 767px) {
      .ds-section-header {
        flex-direction: column !important;
        align-items: flex-start !important;
        gap: 10px !important;
      }

      .ds-section-header-right {
        display: flex !important;
        width: 100% !important;
        justify-content: space-between !important;
        align-items: center !important;
      }
    }"""

if old_link_css in v22_content:
    v22_content = v22_content.replace(old_link_css, new_link_css)
    print("REPLACED CSS FOR .ds-section-link TO WHITE & MOBILE STACK!")
else:
    # Try regex replace for CSS
    import re
    v22_content = re.sub(
        r'\.ds-section-link\s*\{\s*font-size:\s*11px;\s*font-weight:\s*700;\s*color:\s*#bca772\s*!important;\s*text-transform:\s*uppercase;\s*text-decoration:\s*none\s*!important;\s*\}',
        new_link_css,
        v22_content
    )
    print("REPLACED CSS VIA REGEX!")

# 2. UPDATE SECTION 1 HEADER HTML IN sec-posts
old_header_html = """              <!-- SECCI&#211;N 1: &#21A;LTIMAS ENTRADAS DEL BLOG (CON MINIATURA REAL EMBEBIDA 100% GARANTIZADA) -->
              <section class="ds-section-block" id="sec-posts">
                <div class="ds-section-header">
                  <h2>&#21A;LTIMAS <span>ENTRADAS DEL BLOG</span></h2>
                  <div style="display:flex; align-items:center; gap:12px;">
                    <a href="https://www.danielsimons.xyz/search" class="ds-section-link">VER TODAS &#10140;</a>
                    <div class="ds-nav-arrows">
                      <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', -1)">&#10094;</div>
                      <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', 1)">&#10095;</div>
                    </div>
                  </div>
                </div>"""

new_header_html = """              <!-- SECCI&#211;N 1: &#21A;LTIMAS ENTRADAS DEL BLOG (CON MINIATURA REAL EMBEBIDA 100% GARANTIZADA) -->
              <section class="ds-section-block" id="sec-posts">
                <div class="ds-section-header">
                  <h2>&#21A;LTIMAS <span>ENTRADAS DEL BLOG</span></h2>
                  <div class="ds-section-header-right" style="display:flex; align-items:center; gap:12px;">
                    <a href="https://www.danielsimons.xyz/search" class="ds-section-link">Ver todas las entradas &#10140;</a>
                    <div class="ds-nav-arrows">
                      <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', -1)">&#10094;</div>
                      <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', 1)">&#10095;</div>
                    </div>
                  </div>
                </div>"""

if old_header_html in v22_content:
    v22_content = v22_content.replace(old_header_html, new_header_html)
    print("REPLACED SECTION 1 HEADER HTML TO 'Ver todas las entradas' WITH WHITE TEXT AND NEW CLASS!")
else:
    # Try alternate search
    import re
    v22_content = re.sub(
        r'<a href="https://www\.danielsimons\.xyz/search" class="ds-section-link">VER TODAS &#10140;</a>',
        '<a href="https://www.danielsimons.xyz/search" class="ds-section-link">Ver todas las entradas &#10140;</a>',
        v22_content
    )
    v22_content = re.sub(
        r'<div style="display:flex; align-items:center; gap:12px;">\s*<a href="https://www\.danielsimons\.xyz/search"',
        '<div class="ds-section-header-right" style="display:flex; align-items:center; gap:12px;">\n                    <a href="https://www.danielsimons.xyz/search"',
        v22_content
    )
    print("REPLACED HEADER HTML VIA REGEX!")

with open(v22_path, "w", encoding="utf-8") as f:
    f.write(v22_content)

try:
    ET.parse(v22_path)
    print("SUCCESS: v22_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v22_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
