import os
import xml.etree.ElementTree as ET

base_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\v1_theme_optimizado.xml"
output_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\v2_theme_optimizado.xml"

with open(base_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# CSS fix for 100% Pure Black #000000 everywhere and complete removal of left sidebar
quirurgico_css = """
  <style type='text/css'>
  /*<![CDATA[*/
    /* 1. FONDO NEGRO PURO #000000 EN TODOS LOS ELEMENTOS PARA FUSIONAR CON LAS IMÁGENES */
    html, body, .page_body, .centered-top-container, .centered-top-placeholder, 
    #main, .centered-bottom, .post, .post-outer, .post-outer-container, 
    .post-body, .hero-image, .bg-photo, .page, .feed-widget, .blog-posts,
    .post-bottom, .widget, .main-container, body.homepage-view .page_body {
      background-color: #000000 !important;
      background: #000000 !important;
      color: #e6e6e6 !important;
    }

    /* 2. ELIMINAR COMPLETAMENTE LA BARRA LATERAL IZQUIERDA Y MENU HAMBURGUESA */
    .sidebar-container, 
    .sidebar-back, 
    #sidebar-left, 
    .hamburger-menu-container, 
    .hamburger-menu, 
    .navigation,
    .sidebar-container-container {
      display: none !important;
      visibility: hidden !important;
      width: 0 !important;
      height: 0 !important;
      margin: 0 !important;
      padding: 0 !important;
    }

    /* 3. CENTRAR Y AMPLIAR EL CONTENIDO PRINCIPAL A ANCHO COMPLETO */
    #main, 
    .page, 
    .centered-bottom, 
    .post-outer-container,
    .centered-top-container,
    .centered-top-placeholder {
      width: 100% !important;
      max-width: 1200px !important;
      margin: 0 auto !important;
      float: none !important;
      left: 0 !important;
      box-sizing: border-box !important;
    }
  /*]]>*/
  </style>
"""

# Inject before </head>
head_pos = xml_content.find("</head>")
if head_pos != -1:
    xml_content = xml_content[:head_pos] + quirurgico_css + xml_content[head_pos:]

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(output_path)
    print("SUCCESS: v2_theme_optimizado.xml created and passed XML test!")
except Exception as e:
    print("XML ERROR:", e)
