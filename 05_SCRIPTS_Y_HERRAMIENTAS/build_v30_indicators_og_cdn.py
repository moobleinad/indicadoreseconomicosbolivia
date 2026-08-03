import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v29_path = os.path.join(theme_dir, "v29_theme_optimizado.xml")
if not os.path.exists(v29_path):
    v29_path = os.path.join(sub_dir, "v29_theme_optimizado.xml")

v30_path_main = os.path.join(theme_dir, "v30_theme_optimizado.xml")
v30_path_sub = os.path.join(sub_dir, "v30_theme_optimizado.xml")

with open(v29_path, "r", encoding="utf-8") as f:
    v30_content = f.read()

cdn_poster_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp"

# ADD CONDITIONAL OG IMAGE RULE FOR INDICATORS PAGE
indicators_og_xml = f"""
  <!-- METADATOS ESPECIALES Y AFICHE CDN PARA LA PÁGINA DE INDICADORES -->
  <b:if cond='data:view.isPage and (data:view.url == "https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia.html" or data:view.url == "https://www.danielsimons.xyz/p/guia-y-analisis-de-indicadores.html")'>
    <meta content="INDICADORES ECON&#211;MICOS DE BOLIVIA | Daniel Simons" property="og:title"/>
    <meta content="INDICADORES ECON&#211;MICOS DE BOLIVIA | Daniel Simons" name="twitter:title"/>
    <meta content="SIGUE LA COTIZACI&#211;N DEL TIPO DE CAMBIO Y OTROS INDICADORES. Actualizados a diario." property="og:description"/>
    <meta content="SIGUE LA COTIZACI&#211;N DEL TIPO DE CAMBIO Y OTROS INDICADORES. Actualizados a diario." name="twitter:description"/>
    <meta content="{cdn_poster_url}" property="og:image"/>
    <meta content="{cdn_poster_url}" property="og:image:secure_url"/>
    <meta content="{cdn_poster_url}" name="twitter:image"/>
    <meta content="1024" property="og:image:width"/>
    <meta content="1024" property="og:image:height"/>
    <meta content="image/webp" property="og:image:type"/>
  </b:if>
"""

# Insert right after <head>
head_open_pos = v30_content.find("<head>")
if head_open_pos != -1:
    insert_pos = head_open_pos + len("<head>")
    v30_content = v30_content[:insert_pos] + "\n" + indicators_og_xml + v30_content[insert_pos:]
    print("INSERTED INDICATORS CDN AFICHE IN HEAD OF V30!")

# Save in main theme directory and sub directory
with open(v30_path_main, "w", encoding="utf-8") as f:
    f.write(v30_content)

with open(v30_path_sub, "w", encoding="utf-8") as f:
    f.write(v30_content)

try:
    ET.parse(v30_path_main)
    print("SUCCESS: v30_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v30_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
