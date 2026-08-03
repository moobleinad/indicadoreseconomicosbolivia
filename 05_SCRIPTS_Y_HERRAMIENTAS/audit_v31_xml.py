import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v31_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v31_theme_optimizado.xml")

print("AUDITING v31_theme_optimizado.xml...")
print("Path:", v31_path)

file_size_bytes = os.path.getsize(v31_path)
file_size_kb = file_size_bytes / 1024
print(f"File Size: {file_size_kb:.2f} KB ({file_size_bytes} bytes)")

if file_size_kb < 200:
    print("STATUS: SAFE SIZE (< 200 KB) for Blogger Upload!")
else:
    print("WARNING: SIZE EXCEEDS 200 KB!")

# XML Syntax validation
try:
    tree = ET.parse(v31_path)
    root = tree.getroot()
    print("XML PARSE STATUS: VALID (No XML syntax errors detected!)")
except Exception as e:
    print("XML PARSE ERROR:", e)

# Read file content to inspect key components
with open(v31_path, "r", encoding="utf-8", errors="ignore") as f:
    c = f.read()

# Check key sections
has_head = "<head>" in c and "</head>" in c
has_og_afiche = "09.02_afiche_indicadores_economicos_cuadrado.webp" in c
has_art2 = "regimen-cambiario-el-debate-entre-la.html" in c
has_no_sidebar = ".post-sidebar" in c and "display: none !important" in c
has_indicators_banner = "ds-indicators-banner" in c

print("\nCOMPONENT INTEGRITY CHECK:")
print("- <head> tags structure:", "OK" if has_head else "MISSING")
print("- Indicadores OG CDN Afiche (09.02):", "VERIFIED IN XML" if has_og_afiche else "NOT FOUND")
print("- Artículo 2 de la Serie linked:", "VERIFIED IN XML" if has_art2 else "NOT FOUND")
print("- Sidebar Compartir/Etiquetas hidden:", "VERIFIED IN XML" if has_no_sidebar else "NOT FOUND")
print("- Indicadores Económicos Banner in Header:", "VERIFIED IN XML" if has_indicators_banner else "NOT FOUND")
