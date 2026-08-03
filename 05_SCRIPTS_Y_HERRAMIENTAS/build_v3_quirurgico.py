import os
import xml.etree.ElementTree as ET

base_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\v2_theme_optimizado.xml"
output_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\v3_theme_optimizado.xml"

with open(base_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# Responsive Grid CSS: 2 columns on PC (desktop) and 1 column on Mobile
grid_css = """
    /* 4. DISPOSICIÓN DE ENTRADAS: 2 COLUMNAS EN PC Y 1 EN MÓVIL */
    @media (min-width: 768px) {
      .blog-posts {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 30px !important;
      }
      .post-outer-container, .post-outer, .post {
        width: 100% !important;
        max-width: 100% !important;
        margin: 0 !important;
        box-sizing: border-box !important;
      }
    }

    @media (max-width: 767px) {
      .blog-posts {
        display: flex !important;
        flex-direction: column !important;
        gap: 20px !important;
      }
      .post-outer-container, .post-outer, .post {
        width: 100% !important;
      }
    }
"""

# Inject before </style> or inside our CDATA block
target_str = "/*]]>*/"
pos = xml_content.find(target_str)
if pos != -1:
    xml_content = xml_content[:pos] + grid_css + "\n" + xml_content[pos:]

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(output_path)
    print("SUCCESS: v3_theme_optimizado.xml created and passed XML test!")
except Exception as e:
    print("XML ERROR:", e)
