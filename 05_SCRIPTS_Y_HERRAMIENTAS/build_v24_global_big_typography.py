import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v23_path = os.path.join(theme_dir, "v23_theme_optimizado.xml")
if not os.path.exists(v23_path):
    v23_path = os.path.join(sub_dir, "v23_theme_optimizado.xml")

v24_path_main = os.path.join(theme_dir, "v24_theme_optimizado.xml")
v24_path_sub = os.path.join(sub_dir, "v24_theme_optimizado.xml")

# KEEP V23 UNTOUCHED! READ FROM V23 TO CREATE V24
with open(v23_path, "r", encoding="utf-8") as f:
    v24_content = f.read()

# 1. ENHANCE GLOBAL TYPOGRAPHY CSS IN THEME
global_big_typography_css = """
    /* ESTILO GENERAL DE ALTA LEGIBILIDAD Y TIPOGRAFÍA GIGANTE */
    .ds-card-box .title {
      font-size: 18px !important;
      font-weight: 800 !important;
      color: #ffffff !important;
      line-height: 1.35 !important;
      margin: 12px 0 6px 0 !important;
    }

    .ds-card-box .desc {
      font-size: 13.5px !important;
      color: #e0e0e0 !important;
      line-height: 1.45 !important;
      font-weight: 400 !important;
    }

    .ds-card-box .action {
      font-size: 13px !important;
      font-weight: 800 !important;
      color: #bca772 !important;
      margin-top: 12px !important;
      letter-spacing: 0.3px !important;
    }

    .ds-section-header h2 {
      font-size: 22px !important;
      font-weight: 900 !important;
      color: #ffffff !important;
      text-transform: uppercase !important;
      letter-spacing: 0.5px !important;
    }

    .ds-section-header h2 span {
      color: #bca772 !important;
    }

    .ds-indicators-banner-title {
      font-size: 19px !important;
      font-weight: 900 !important;
    }

    .ds-indicators-banner-sub {
      font-size: 13.5px !important;
      color: #ffffff !important;
      font-weight: 600 !important;
    }

    .ds-indicators-banner-action {
      font-size: 13px !important;
      font-weight: 800 !important;
    }

    @media (max-width: 767px) {
      .ds-card-box .title {
        font-size: 16.5px !important;
        line-height: 1.3 !important;
        font-weight: 800 !important;
      }
      .ds-card-box .desc {
        font-size: 13px !important;
        line-height: 1.4 !important;
        color: #e0e0e0 !important;
      }
      .ds-section-header h2 {
        font-size: 19px !important;
      }
    }
"""

style_tag_pos = v24_content.find('</style>')
if style_tag_pos != -1:
    v24_content = v24_content[:style_tag_pos] + global_big_typography_css + "\n" + v24_content[style_tag_pos:]
    print("ADDED GLOBAL BIG TYPOGRAPHY CSS!")

# Save in main theme directory and sub directory
with open(v24_path_main, "w", encoding="utf-8") as f:
    f.write(v24_content)

with open(v24_path_sub, "w", encoding="utf-8") as f:
    f.write(v24_content)

try:
    ET.parse(v24_path_main)
    print("SUCCESS: v24_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v24_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
