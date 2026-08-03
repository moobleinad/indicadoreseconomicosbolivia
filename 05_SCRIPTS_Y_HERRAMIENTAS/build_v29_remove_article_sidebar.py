import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v28_path = os.path.join(theme_dir, "v28_theme_optimizado.xml")
if not os.path.exists(v28_path):
    v28_path = os.path.join(sub_dir, "v28_theme_optimizado.xml")

v29_path_main = os.path.join(theme_dir, "v29_theme_optimizado.xml")
v29_path_sub = os.path.join(sub_dir, "v29_theme_optimizado.xml")

with open(v28_path, "r", encoding="utf-8") as f:
    v29_content = f.read()

# CSS TO HIDE LEFT SIDEBAR (COMPARTIR & ETIQUETAS) AND CENTER THE ARTICLE CONTENT
remove_sidebar_css = """
    /* REMOVER COLUMNA IZQUIERDA (COMPARTIR Y ETIQUETAS) EN ARTÍCULOS */
    .post-sidebar,
    .post-sidebar-item,
    .post-sidebar-labels,
    .post-share-buttons,
    .byline.post-labels,
    .byline.reactions,
    .item-post-labels,
    .item-post-share {
      display: none !important;
      visibility: hidden !important;
      width: 0 !important;
      height: 0 !important;
      margin: 0 !important;
      padding: 0 !important;
      overflow: hidden !important;
    }

    /* CENTRAR CONTENIDO DE LECTURA LIMPIO EN ARTÍCULOS */
    .item-view .post-body-container,
    .item-view .main-container,
    .item-view .centered-top-container,
    .item-view .blog-post,
    .item-view .post-outer {
      margin-left: auto !important;
      margin-right: auto !important;
      padding-left: 0 !important;
      max-width: 860px !important;
      width: 100% !important;
    }

    .item-view .post-header {
      margin-left: 0 !important;
      padding-left: 0 !important;
      width: 100% !important;
    }

    .item-view .post-body {
      margin-left: 0 !important;
      padding-left: 0 !important;
    }

    @media screen and (min-width: 768px) {
      .item-view .post-sidebar {
        display: none !important;
      }
      .item-view .centered-top-container {
        padding-left: 0 !important;
      }
    }
"""

style_tag_pos = v29_content.find('</style>')
if style_tag_pos != -1:
    v29_content = v29_content[:style_tag_pos] + remove_sidebar_css + "\n" + v29_content[style_tag_pos:]
    print("ADDED CSS TO REMOVE COMPARTIR & ETIQUETAS SIDEBAR!")

# Save in main theme directory and sub directory
with open(v29_path_main, "w", encoding="utf-8") as f:
    f.write(v29_content)

with open(v29_path_sub, "w", encoding="utf-8") as f:
    f.write(v29_content)

try:
    ET.parse(v29_path_main)
    print("SUCCESS: v29_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v29_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
