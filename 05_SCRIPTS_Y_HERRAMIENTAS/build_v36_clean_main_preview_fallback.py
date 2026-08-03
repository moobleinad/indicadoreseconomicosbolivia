import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v35_path = os.path.join(theme_dir, "v35_theme_optimizado.xml")
if not os.path.exists(v35_path):
    v35_path = os.path.join(sub_dir, "v35_theme_optimizado.xml")

v36_path_main = os.path.join(theme_dir, "v36_theme_optimizado.xml")
v36_path_sub = os.path.join(sub_dir, "v36_theme_optimizado.xml")

with open(v35_path, "r", encoding="utf-8") as f:
    v36_content = f.read()

# Main Site Official Preview Image URL (1200x630 HD Widescreen)
main_site_img_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIG7CrEnww8e0tXKx4-5T0fPI9VuIb-7be3g-Aor7fMkqxQbfp7JvolPod3WFzvozbUrNUjEX-ziAo0Cj3UucGIFBCgCEPglvySv5Jiy6L0zx0QpMPBHJZ9URfttZ5IlcSzotnsgH7yT_MVGefmNcC7tU5rgTr7QC_4zxfaQU_rdt_xQCugVJZCfbcTwu1/s1376/02.03_foto_articulo1_rm245_oficial_horizontal.webp"

# CLEAN & ELEGANT OPENGRAPH SYSTEM FOR V36:
# 1. For POSTS (Artículos): Use post title, description and post featured image.
# 2. For EVERYTHING ELSE (Homepage & Static Pages): Use Main Site Official Title, Description and Main Preview Image!

clean_head_opengraph = f"""
  <!-- Google tag (gtag.js) GA4 DANIEL SIMONS -->
  <script async='async' src='https://www.googletagmanager.com/gtag/js?id=G-LL1KM8J1TP'></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', 'G-LL1KM8J1TP');
  </script>

  <!-- SISTEMA DE PREVISUALIZACIÓN OPENGRAPH LIMPIO Y UNIFICADO (VERSION 36) -->
  <b:if cond='data:view.isPost'>
    <!-- ARTÍCULOS DE BLOG: MUESTRAN SU FOTO Y TÍTULO ESPECÍFICO -->
    <meta expr:content='data:view.title.escaped + " | Daniel Simons"' property='og:title'/>
    <meta expr:content='data:view.title.escaped + " | Daniel Simons"' name='twitter:title'/>
    <meta content='article' property='og:type'/>
    <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
    <meta expr:content='data:blog.canonicalUrl' name='twitter:url'/>
    <b:if cond='data:view.description'>
      <meta expr:content='data:view.description.escaped' name='description'/>
      <meta expr:content='data:view.description.escaped' property='og:description'/>
      <meta expr:content='data:view.description.escaped' name='twitter:description'/>
    <b:else/>
      <meta expr:content='data:view.title.escaped + " - An&#225;lisis de estructura por Daniel Simons."' name='description'/>
      <meta expr:content='data:view.title.escaped + " - An&#225;lisis de estructura por Daniel Simons."' property='og:description'/>
      <meta expr:content='data:view.title.escaped + " - An&#225;lisis de estructura por Daniel Simons."' name='twitter:description'/>
    </b:if>
    <b:if cond='data:view.featuredImage'>
      <meta expr:content='data:view.featuredImage' property='og:image'/>
      <meta expr:content='data:view.featuredImage' property='og:image:secure_url'/>
      <meta expr:content='data:view.featuredImage' name='twitter:image'/>
    <b:else/>
      <meta content='{main_site_img_url}' property='og:image'/>
      <meta content='{main_site_img_url}' property='og:image:secure_url'/>
      <meta content='{main_site_img_url}' name='twitter:image'/>
    </b:if>
    <meta content='1200' property='og:image:width'/>
    <meta content='630' property='og:image:height'/>
    <meta content='image/webp' property='og:image:type'/>
    <meta content='summary_large_image' name='twitter:card'/>
  <b:else/>
    <!-- PORTADA Y PÁGINAS ESTÁTICAS: MUESTRAN LA PREVISUALIZACIÓN DE LA PÁGINA PRINCIPAL -->
    <meta expr:content='data:blog.title + " | Estructurador de Ideas Complejas"' property='og:title'/>
    <meta expr:content='data:blog.title + " | Estructurador de Ideas Complejas"' name='twitter:title'/>
    <meta content='website' property='og:type'/>
    <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
    <meta expr:content='data:blog.canonicalUrl' name='twitter:url'/>
    <meta content='Sitio Oficial de Daniel Simons: Art&#237;culos sobre econom&#237;a, modelos sist&#233;micos, finanzas e inteligencia relacional.' name='description'/>
    <meta content='Sitio Oficial de Daniel Simons: Art&#237;culos sobre econom&#237;a, modelos sist&#233;micos, finanzas e inteligencia relacional.' property='og:description'/>
    <meta content='Sitio Oficial de Daniel Simons: Art&#237;culos sobre econom&#237;a, modelos sist&#233;micos, finanzas e inteligencia relacional.' name='twitter:description'/>
    <meta content='{main_site_img_url}' property='og:image'/>
    <meta content='{main_site_img_url}' property='og:image:secure_url'/>
    <meta content='{main_site_img_url}' name='twitter:image'/>
    <meta content='1200' property='og:image:width'/>
    <meta content='630' property='og:image:height'/>
    <meta content='image/webp' property='og:image:type'/>
    <meta content='summary_large_image' name='twitter:card'/>
  </b:if>
"""

# Find head and replace metadata section cleanly
head_open_pos = v36_content.find("<head>")
title_tag_pos = v36_content.find("<title>")

if head_open_pos != -1 and title_tag_pos != -1:
    v36_content = v36_content[:head_open_pos + len("<head>")] + "\n" + clean_head_opengraph + "\n  " + v36_content[title_tag_pos:]
    print("SUCCESSFULLY RESTRUCTURED OPENGRAPH HEAD FOR V36!")

# Save in main theme directory and sub directory
with open(v36_path_main, "w", encoding="utf-8") as f:
    f.write(v36_content)

with open(v36_path_sub, "w", encoding="utf-8") as f:
    f.write(v36_content)

try:
    ET.parse(v36_path_main)
    print("SUCCESS: v36_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v36_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
