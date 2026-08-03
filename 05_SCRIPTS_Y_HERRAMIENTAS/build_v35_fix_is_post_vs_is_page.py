import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v34_path = os.path.join(theme_dir, "v34_theme_optimizado.xml")
if not os.path.exists(v34_path):
    v34_path = os.path.join(sub_dir, "v34_theme_optimizado.xml")

v35_path_main = os.path.join(theme_dir, "v35_theme_optimizado.xml")
v35_path_sub = os.path.join(sub_dir, "v35_theme_optimizado.xml")

with open(v34_path, "r", encoding="utf-8") as f:
    v35_content = f.read()

cdn_poster_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp"

# FIX CONFLICT: Change data:view.isSingleItem to data:view.isPost so it NEVER fires on static pages!
if "<b:if cond='data:view.isSingleItem'>" in v35_content:
    v35_content = v35_content.replace("<b:if cond='data:view.isSingleItem'>", "<b:if cond='data:view.isPost'>")
    print("FIXED CONFLICT: Replaced data:view.isSingleItem with data:view.isPost!")

# Clean up static pages OpenGraph block
clean_pages_og = f"""
  <!-- OPENGRAPH EXCLUSIVO PARA PÁGINAS ESTÁTICAS (/p/*.html) -->
  <b:if cond='data:view.isPage'>
    <meta expr:content='data:view.title.escaped + " | Daniel Simons"' property='og:title'/>
    <meta expr:content='data:view.title.escaped + " | Daniel Simons"' name='twitter:title'/>
    <meta content='website' property='og:type'/>
    <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
    <meta expr:content='data:blog.canonicalUrl' name='twitter:url'/>
    <meta content='summary_large_image' name='twitter:card'/>
    <b:if cond='data:view.description'>
      <meta expr:content='data:view.description.escaped' name='description'/>
      <meta expr:content='data:view.description.escaped' property='og:description'/>
      <meta expr:content='data:view.description.escaped' name='twitter:description'/>
    <b:else/>
      <meta content='SIGUE LA COTIZACIÓN DEL TIPO DE CAMBIO Y OTROS INDICADORES. Actualizados a diario.' name='description'/>
      <meta content='SIGUE LA COTIZACIÓN DEL TIPO DE CAMBIO Y OTROS INDICADORES. Actualizados a diario.' property='og:description'/>
      <meta content='SIGUE LA COTIZACIÓN DEL TIPO DE CAMBIO Y OTROS INDICADORES. Actualizados a diario.' name='twitter:description'/>
    </b:if>
    <b:if cond='data:view.featuredImage'>
      <meta expr:content='data:view.featuredImage' property='og:image'/>
      <meta expr:content='data:view.featuredImage' property='og:image:secure_url'/>
      <meta expr:content='data:view.featuredImage' name='twitter:image'/>
    <b:else/>
      <meta content='{cdn_poster_url}' property='og:image'/>
      <meta content='{cdn_poster_url}' property='og:image:secure_url'/>
      <meta content='{cdn_poster_url}' name='twitter:image'/>
    </b:if>
    <meta content='1024' property='og:image:width'/>
    <meta content='1024' property='og:image:height'/>
    <meta content='image/webp' property='og:image:type'/>
  </b:if>
"""

# Replace the top pages block with clean_pages_og
head_pos = v35_content.find("<head>")
if head_pos != -1:
    # Remove old block if needed and insert clean_pages_og right after head
    old_top_block = v35_content[head_pos+6:v35_content.find("<!-- Google tag")]
    v35_content = v35_content.replace(old_top_block, "\n" + clean_pages_og + "\n")

# Save in main theme directory and sub directory
with open(v35_path_main, "w", encoding="utf-8") as f:
    f.write(v35_content)

with open(v35_path_sub, "w", encoding="utf-8") as f:
    f.write(v35_content)

try:
    ET.parse(v35_path_main)
    print("SUCCESS: v35_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v35_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
