import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v25_path = os.path.join(theme_dir, "v25_theme_optimizado.xml")
if not os.path.exists(v25_path):
    v25_path = os.path.join(sub_dir, "v25_theme_optimizado.xml")

v26_path_main = os.path.join(theme_dir, "v26_theme_optimizado.xml")
v26_path_sub = os.path.join(sub_dir, "v26_theme_optimizado.xml")

# KEEP V25 UNTOUCHED! READ FROM V25 TO CREATE V26
with open(v25_path, "r", encoding="utf-8") as f:
    v26_content = f.read()

# REMOVE OLD CONFLICTING META TAGS FROM HEAD
import re

# Clean old static or duplicate og/twitter metas
clean_patterns = [
    r"<meta expr:content='data:view\.title\.escaped \+ \" \| Daniel Simons\"' property='og:title'/>",
    r"<meta expr:content='data:view\.title\.escaped \+ \" \| Daniel Simons\"' name='twitter:title'/>",
    r"<meta expr:content='data:view\.description' name='description'/>",
    r"<meta expr:content='data:view\.description' property='og:description'/>",
    r"<meta expr:content='data:view\.description' name='twitter:description'/>",
    r"<meta expr:content='data:view\.title\.escaped \+ \" - De ideas complejas a resultados concretos por Daniel Simons\.\"' name='description'/>",
    r"<meta expr:content='data:view\.title\.escaped \+ \" - De ideas complejas a resultados concretos por Daniel Simons\.\"' property='og:description'/>",
    r"<meta expr:content='data:view\.title\.escaped \+ \" - De ideas complejas a resultados concretos por Daniel Simons\.\"' name='twitter:description'/>",
    r"<meta content='article' property='og:type'/>",
    r"<meta content='Daniel Simons \| De ideas complejas a resultados concretos' property='og:title'/>",
    r"<meta content='Daniel Simons \| De ideas complejas a resultados concretos' name='twitter:title'/>",
    r"<meta content='Portal oficial de Daniel Simons\. Estructurador de ideas complejas, Forja de Proyectos, Destilado de Conocimiento, Modelo MFEIR y Observatorio Econ[^\']*' name='description'/>",
    r"<meta content='Portal oficial de Daniel Simons\. Estructurador de ideas complejas, Forja de Proyectos, Destilado de Conocimiento, Modelo MFEIR y Observatorio Econ[^\']*' property='og:description'/>",
    r"<meta content='Portal oficial de Daniel Simons\. Estructurador de ideas complejas, Forja de Proyectos, Destilado de Conocimiento, Modelo MFEIR y Observatorio Econ[^\']*' name='twitter:description'/>",
    r"<meta content='website' property='og:type'/>",
    r"<meta content='Daniel Simons' name='author'/>",
    r"<meta content='Daniel Simons' property='og:site_name'/>",
    r"<meta expr:content='data:blog\.canonicalUrl' property='og:url'/>",
    r"<meta content='summary_large_image' name='twitter:card'/>"
]

for pat in clean_patterns:
    v26_content = re.sub(pat, '', v26_content)

# ROBUST OPENGRAPH 2.0 CONDITIONAL SYSTEM FOR BLOGGER
opengraph_system_xml = """
    <!-- METADATOS Y OPENGRAPH 2.0 MULTI-REDES (FACEBOOK, WHATSAPP, LINKEDIN, TWITTER/X, TELEGRAM) -->
    <b:if cond='data:view.isSingleItem'>
      <meta expr:content='data:view.title.escaped + " | Daniel Simons"' property='og:title'/>
      <meta expr:content='data:view.title.escaped + " | Daniel Simons"' name='twitter:title'/>
      <meta content='article' property='og:type'/>
      <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
      
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
        <meta expr:content='data:view.featuredImage' name='twitter:image'/>
        <meta expr:content='data:view.featuredImage' property='og:image:secure_url'/>
      <b:else/>
        <meta content='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIG7CrEnww8e0tXKx4-5T0fPI9VuIb-7be3g-Aor7fMkqxQbfp7JvolPod3WFzvozbUrNUjEX-ziAo0Cj3UucGIFBCgCEPglvySv5Jiy6L0zx0QpMPBHJZ9URfttZ5IlcSzotnsgH7yT_MVGefmNcC7tU5rgTr7QC_4zxfaQU_rdt_xQCugVJZCfbcTwu1/s1376/02.03_foto_articulo1_rm245_oficial_horizontal.webp' property='og:image'/>
        <meta content='https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIG7CrEnww8e0tXKx4-5T0fPI9VuIb-7be3g-Aor7fMkqxQbfp7JvolPod3WFzvozbUrNUjEX-ziAo0Cj3UucGIFBCgCEPglvySv5Jiy6L0zx0QpMPBHJZ9URfttZ5IlcSzotnsgH7yT_MVGefmNcC7tU5rgTr7QC_4zxfaQU_rdt_xQCugVJZCfbcTwu1/s1376/02.03_foto_articulo1_rm245_oficial_horizontal.webp' name='twitter:image'/>
      </b:if>
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
    </b:if>

    <meta content='summary_large_image' name='twitter:card'/>
    <meta content='Daniel Simons' property='og:site_name'/>
    <meta content='Daniel Simons' name='author'/>
"""

# Insert OpenGraph System right before </head>
head_close_pos = v26_content.find("</head>")
if head_close_pos != -1:
    v26_content = v26_content[:head_close_pos] + opengraph_system_xml + "\n" + v26_content[head_close_pos:]
    print("INSERTED OPENGRAPH 2.0 MULTI-PLATFORM SYSTEM IN HEAD!")

# Save in main theme directory and sub directory
with open(v26_path_main, "w", encoding="utf-8") as f:
    f.write(v26_content)

with open(v26_path_sub, "w", encoding="utf-8") as f:
    f.write(v26_content)

try:
    ET.parse(v26_path_main)
    print("SUCCESS: v26_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v26_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
