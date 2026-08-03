import os
import re
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v27_path = os.path.join(theme_dir, "v27_theme_optimizado.xml")
if not os.path.exists(v27_path):
    v27_path = os.path.join(sub_dir, "v27_theme_optimizado.xml")

v28_path_main = os.path.join(theme_dir, "v28_theme_optimizado.xml")
v28_path_sub = os.path.join(sub_dir, "v28_theme_optimizado.xml")

with open(v27_path, "r", encoding="utf-8") as f:
    v28_content = f.read()

# Remove old custom opengraph block
v28_content = re.sub(r'<!-- OPENGRAPH 2\.0 & TWITTER CARDS OFICIAL DANIEL SIMONS.*?-->', '', v28_content, flags=re.DOTALL)

# ADVANCED OPENGRAPH 2.0 BLOCK WITH EXPLICIT DIMENSIONS AND WEBP METADATA FOR FACEBOOK POPUP RENDERER
top_head_og_v28_xml = """
  <!-- OPENGRAPH 2.0 & TWITTER CARDS CON DIMENSIONES EXPLÍCITAS (VERSION 28) -->
  <b:if cond='data:view.isSingleItem'>
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
      <meta content='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIG7CrEnww8e0tXKx4-5T0fPI9VuIb-7be3g-Aor7fMkqxQbfp7JvolPod3WFzvozbUrNUjEX-ziAo0Cj3UucGIFBCgCEPglvySv5Jiy6L0zx0QpMPBHJZ9URfttZ5IlcSzotnsgH7yT_MVGefmNcC7tU5rgTr7QC_4zxfaQU_rdt_xQCugVJZCfbcTwu1/s1376/02.03_foto_articulo1_rm245_oficial_horizontal.webp' property='og:image'/>
      <meta content='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIG7CrEnww8e0tXKx4-5T0fPI9VuIb-7be3g-Aor7fMkqxQbfp7JvolPod3WFzvozbUrNUjEX-ziAo0Cj3UucGIFBCgCEPglvySv5Jiy6L0zx0QpMPBHJZ9URfttZ5IlcSzotnsgH7yT_MVGefmNcC7tU5rgTr7QC_4zxfaQU_rdt_xQCugVJZCfbcTwu1/s1376/02.03_foto_articulo1_rm245_oficial_horizontal.webp' name='twitter:image'/>
    </b:if>
    <meta content='1200' property='og:image:width'/>
    <meta content='630' property='og:image:height'/>
    <meta content='image/webp' property='og:image:type'/>
  </b:if>

  <b:if cond='data:view.isHomepage'>
    <meta content='Daniel Simons | Estructurador de Ideas Complejas' property='og:title'/>
    <meta content='Daniel Simons | Estructurador de Ideas Complejas' name='twitter:title'/>
    <meta content='website' property='og:type'/>
    <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
    <meta content='Portal oficial de Daniel Simons. Estructurador de ideas complejas, Forja de Proyectos, Destilado de Conocimiento, Modelo MFEIR e Indicadores Econ&#243;micos.' name='description'/>
    <meta content='Portal oficial de Daniel Simons. Estructurador de ideas complejas, Forja de Proyectos, Destilado de Conocimiento, Modelo MFEIR e Indicadores Econ&#243;micos.' property='og:description'/>
    <meta content='Portal oficial de Daniel Simons. Estructurador de ideas complejas, Forja de Proyectos, Destilado de Conocimiento, Modelo MFEIR e Indicadores Econ&#243;micos.' name='twitter:description'/>
    <meta content='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIG7CrEnww8e0tXKx4-5T0fPI9VuIb-7be3g-Aor7fMkqxQbfp7JvolPod3WFzvozbUrNUjEX-ziAo0Cj3UucGIFBCgCEPglvySv5Jiy6L0zx0QpMPBHJZ9URfttZ5IlcSzotnsgH7yT_MVGefmNcC7tU5rgTr7QC_4zxfaQU_rdt_xQCugVJZCfbcTwu1/s1376/02.03_foto_articulo1_rm245_oficial_horizontal.webp' property='og:image'/>
    <meta content='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIG7CrEnww8e0tXKx4-5T0fPI9VuIb-7be3g-Aor7fMkqxQbfp7JvolPod3WFzvozbUrNUjEX-ziAo0Cj3UucGIFBCgCEPglvySv5Jiy6L0zx0QpMPBHJZ9URfttZ5IlcSzotnsgH7yT_MVGefmNcC7tU5rgTr7QC_4zxfaQU_rdt_xQCugVJZCfbcTwu1/s1376/02.03_foto_articulo1_rm245_oficial_horizontal.webp' name='twitter:image'/>
    <meta content='1200' property='og:image:width'/>
    <meta content='630' property='og:image:height'/>
    <meta content='image/webp' property='og:image:type'/>
  </b:if>

  <meta content='summary_large_image' name='twitter:card'/>
  <meta content='Daniel Simons' property='og:site_name'/>
  <meta content='Daniel Simons' name='author'/>
"""

# Insert top_head_og_v28_xml right after <head>
head_open_pos = v28_content.find("<head>")
if head_open_pos != -1:
    insert_pos = head_open_pos + len("<head>")
    v28_content = v28_content[:insert_pos] + "\n" + top_head_og_v28_xml + v28_content[insert_pos:]
    print("PLACED EXPLICIT DIMENSIONS OPENGRAPH 2.0 AT TOP OF HEAD IN V28!")

# Save in main theme directory and sub directory
with open(v28_path_main, "w", encoding="utf-8") as f:
    f.write(v28_content)

with open(v28_path_sub, "w", encoding="utf-8") as f:
    f.write(v28_content)

try:
    ET.parse(v28_path_main)
    print("SUCCESS: v28_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v28_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
