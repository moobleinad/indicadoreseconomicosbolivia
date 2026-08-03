import os
import xml.etree.ElementTree as ET

base_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\0 theme_optimizado_danielsimons.xml"
output_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\v1_theme_optimizado.xml"

with open(base_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# STRICTLY ONLY TWO CHANGES:
# 1. Background color pure black #000000
# 2. Hide left sidebar
clean_css = """
  <style type='text/css'>
  /*<![CDATA[*/
    /* 1. FONDO NEGRO PURO #000000 */
    html, body, .page_body, .centered-top-container, .centered-top-placeholder, 
    #main, .centered-bottom, .post, .post-outer, .post-outer-container, 
    .post-body, .hero-image, .bg-photo, .page, .feed-widget, .blog-posts,
    .post-bottom, .widget, .main-container {
      background-color: #000000 !important;
      background: #000000 !important;
      color: #e6e6e6 !important;
    }

    /* 2. ELIMINAR BARRA LATERAL IZQUIERDA */
    .sidebar-container, 
    .sidebar-back, 
    #sidebar-left, 
    .hamburger-menu-container, 
    .hamburger-menu, 
    .navigation {
      display: none !important;
      visibility: hidden !important;
      width: 0 !important;
    }
  /*]]>*/
  </style>
"""

# Inject before </head>
head_pos = xml_content.find("</head>")
if head_pos != -1:
    xml_content = xml_content[:head_pos] + clean_css + xml_content[head_pos:]

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(output_path)
    print("SUCCESS: v1_theme_optimizado.xml generated strictly with 2 changes!")
except Exception as e:
    print("XML ERROR:", e)
