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

with open(v24_path, "r", encoding="utf-8") as f:
    v25_content = f.read()

cdn_img_art2 = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhtROV7xDFMgxrtLI8R1dDMm9IWEyCWVm5W_LuBcy1A_BHJXD9xharrEpaCaEKTBfw2iAx0YSUgxuZFKeq-OuorQoVEi9Oip2J4pCaIGLxauDCkU_8Us-NmP1djIOlVmV3O02o6_Wl5uAoqt_Hp2NUdDhymGLsJZjRXkBYh5qTOpWvs4aCpDnXeyct9-0nO/s600/02.04_foto_articulo2_flotacion_oficial_horizontal.webp"
art2_url = "https://www.danielsimons.xyz/2026/08/regimen-cambiario-el-debate-entre-la.html"
art2_title = "R&#233;gimen Cambiario: El debate entre la terapia de choque y la flotaci&#243;n gradual"

art2_card_html = f"""                  <!-- ARTICULO 2 DE LA SERIE -->
                  <a href="{art2_url}" class="ds-card-box">
                    <div>
                      <img src="{cdn_img_art2}" alt="{art2_title}" class="ds-card-thumb" loading="lazy" />
                      <div class="title">{art2_title}</div>
                      <div class="desc">Serie Politica Monetaria y Sociedad | Parte 2</div>
                    </div>
                    <div class="action">Leer Art&#237;culo &#10140;</div>
                  </a>

"""

# Find Article 1 card tag position and insert Article 2 directly before Article 1
art1_href = "https://www.danielsimons.xyz/2026/08/regimen-cambiario-como-funciona-ahora.html"
pos_art1 = v25_content.find(art1_href)

if pos_art1 != -1:
    # Go back to the opening <a href= of Article 1
    pos_a_start = v25_content.rfind("<a ", 0, pos_art1)
    if pos_a_start != -1:
        v25_content = v25_content[:pos_a_start] + art2_card_html + v25_content[pos_a_start:]
        print("SUCCESSFULLY INSERTED ARTICLE 2 DIRECTLY BEFORE ARTICLE 1 IN V25!")
    else:
        print("ERROR: COULD NOT FIND OPENING <a TAG FOR ARTICLE 1")
else:
    print("ERROR: COULD NOT FIND ARTICLE 1 HREF")

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
