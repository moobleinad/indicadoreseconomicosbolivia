import os
import xml.etree.ElementTree as ET

base_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\v3_theme_optimizado.xml"
output_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\v4_theme_optimizado.xml"

with open(base_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# Fix image scaling & proportional container width (max-width: 980px)
image_size_fix_css = """
  <style type='text/css'>
  /*<![CDATA[*/
    /* RESTREÑIR EL ANCHO MÁXIMO DEL CONTENEDOR PARA EVITAR IMÁGENES GIGANTES (TAMAÑO ORIGINAL ELEGANTE) */
    #main, 
    .page, 
    .centered-bottom, 
    .post-outer-container,
    .centered-top-container,
    .centered-top-placeholder,
    .hero-image {
      width: 100% !important;
      max-width: 980px !important;
      margin: 0 auto !important;
      float: none !important;
      left: 0 !important;
      box-sizing: border-box !important;
    }

    /* CONTROL DE ALTURA Y ESCALADO DEL BANNER PRINCIPAL */
    .hero-image, .bg-photo, header img, .centered-top-container img {
      max-height: 280px !important;
      width: 100% !important;
      object-fit: contain !important;
      margin: 0 auto !important;
      display: block !important;
    }

    /* CONTROL DE ALTURA Y PROPORCIÓN DE LAS IMÁGENES DE LAS ENTRADAS (DESTILADO, FORJA, ETC) */
    .snippet-thumbnail, .post-thumbnail {
      max-height: 260px !important;
      overflow: hidden !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      background-color: #000000 !important;
    }

    .snippet-thumbnail img, .post-thumbnail img, .post-body img {
      max-height: 250px !important;
      width: auto !important;
      max-width: 100% !important;
      object-fit: contain !important;
      margin: 0 auto !important;
      background-color: #000000 !important;
    }

    /* GRID DE 2 COLUMNAS COMPACTAS EN PC Y 1 EN CELULAR */
    @media (min-width: 768px) {
      .blog-posts {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 25px !important;
      }
      .post-outer-container, .post-outer, .post {
        width: 100% !important;
        max-width: 100% !important;
        margin: 0 !important;
      }
    }
  /*]]>*/
  </style>
"""

# Inject before </head>
head_pos = xml_content.find("</head>")
if head_pos != -1:
    xml_content = xml_content[:head_pos] + image_size_fix_css + xml_content[head_pos:]

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(output_path)
    print("SUCCESS: v4_theme_optimizado.xml created and passed XML test!")
except Exception as e:
    print("XML ERROR:", e)
