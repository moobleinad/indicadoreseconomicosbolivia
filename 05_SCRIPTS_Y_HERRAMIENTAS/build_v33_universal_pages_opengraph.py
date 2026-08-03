import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v32_path = os.path.join(theme_dir, "v32_theme_optimizado.xml")
if not os.path.exists(v32_path):
    v32_path = os.path.join(sub_dir, "v32_theme_optimizado.xml")

v33_path_main = os.path.join(theme_dir, "v33_theme_optimizado.xml")
v33_path_sub = os.path.join(sub_dir, "v33_theme_optimizado.xml")

# KEEP V32 UNTOUCHED! READ FROM V32 TO CREATE V33
with open(v32_path, "r", encoding="utf-8") as f:
    v33_content = f.read()

cdn_poster_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp"

# UNIVERSAL OPENGRAPH ENGINE FOR ALL STATIC PAGES (/p/*.html)
universal_pages_og_xml = f"""
  <!-- MOTOR UNIVERSAL OPENGRAPH PARA TODAS LAS PÁGINAS ESTÁTICAS (/p/*.html) -->
  <b:if cond='data:view.isPage'>
    <meta content="website" property="og:type"/>
    <meta content="summary_large_image" name="twitter:card"/>
    <b:if cond='data:view.featuredImage'>
      <meta expr:content='data:view.featuredImage' property='og:image'/>
      <meta expr:content='data:view.featuredImage' property='og:image:secure_url'/>
      <meta expr:content='data:view.featuredImage' name='twitter:image'/>
    <b:else/>
      <meta content="{cdn_poster_url}" property="og:image"/>
      <meta content="{cdn_poster_url}" property="og:image:secure_url"/>
      <meta content="{cdn_poster_url}" name="twitter:image"/>
    </b:if>
    <meta content="1024" property="og:image:width"/>
    <meta content="1024" property="og:image:height"/>
    <meta content="image/webp" property="og:image:type"/>
  </b:if>
"""

# Insert right after <head>
head_open_pos = v33_content.find("<head>")
if head_open_pos != -1:
    insert_pos = head_open_pos + len("<head>")
    v33_content = v33_content[:insert_pos] + "\n" + universal_pages_og_xml + v33_content[insert_pos:]
    print("SUCCESSFULLY INSTALLED UNIVERSAL OPENGRAPH ENGINE FOR ALL STATIC PAGES IN V33!")

# Save in main theme directory and sub directory
with open(v33_path_main, "w", encoding="utf-8") as f:
    f.write(v33_content)

with open(v33_path_sub, "w", encoding="utf-8") as f:
    f.write(v33_content)

try:
    ET.parse(v33_path_main)
    print("SUCCESS: v33_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v33_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
