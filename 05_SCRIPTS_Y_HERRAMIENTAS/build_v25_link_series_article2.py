import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v24_path = os.path.join(theme_dir, "v24_theme_optimizado.xml")
if not os.path.exists(v24_path):
    v24_path = os.path.join(sub_dir, "v24_theme_optimizado.xml")

v25_path_main = os.path.join(theme_dir, "v25_theme_optimizado.xml")
v25_path_sub = os.path.join(sub_dir, "v25_theme_optimizado.xml")

# KEEP V24 UNTOUCHED! READ FROM V24 TO CREATE V25
with open(v24_path, "r", encoding="utf-8") as f:
    v25_content = f.read()

cdn_img_art2 = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtROV7xDFMgxrtLI8R1dDMm9IWEyCWVm5W_LuBcy1A_BHJXD9xharrEpaCaEKTBfw2iAx0YSUgxuZFKeq-OuorQoVEi9Oip2J4pCaIGLxauDCkU_8Us-NmP1djIOlVmV3O02o6_Wl5uAoqt_Hp2NUdDhymGLsJZjRXkBYh5qTOpWvs4aCpDnXeyct9-0nO/s1376/02.04_foto_articulo2_flotacion_oficial_horizontal.webp"
art2_url = "https://www.danielsimons.xyz/2026/08/regimen-cambiario-el-debate-entre-la.html"
art2_title = "R&#201;GIMEN CAMBIARIO: EL DEBATE ENTRE LA TERAPIA DE CHOQUE Y LA FLOTACI&#211;N GRADUAL"

art2_card_html = f"""                <!-- ARTICULO 2 DE LA SERIE -->
                <a href="{art2_url}" class="ds-card-box">
                  <div class="img-wrap">
                    <img src="{cdn_img_art2}" alt="{art2_title}" loading="lazy"/>
                  </div>
                  <div class="card-content">
                    <div class="title">{art2_title}</div>
                    <div class="desc">Serie Politica Monetaria y Sociedad | Parte 2. Analisis de la flotacion libre abrupta frente al modelo de deslizamiento progresivo (crawling peg).</div>
                    <div class="action">Leer Art&#237;culo &#10140;</div>
                  </div>
                </a>
"""

# Insert Article 2 right after <div class="ds-track" id="track-posts">
track_posts_pos = v25_content.find('<div class="ds-track" id="track-posts">')
if track_posts_pos != -1:
    insert_pos = track_posts_pos + len('<div class="ds-track" id="track-posts">')
    v25_content = v25_content[:insert_pos] + "\n" + art2_card_html + v25_content[insert_pos:]
    print("INSERTED ARTICLE 2 OF SERIES AT TOP OF TRACK-POSTS!")

# Save in main theme directory and sub directory
with open(v25_path_main, "w", encoding="utf-8") as f:
    f.write(v25_content)

with open(v25_path_sub, "w", encoding="utf-8") as f:
    f.write(v25_content)

try:
    ET.parse(v25_path_main)
    print("SUCCESS: v25_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v25_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
