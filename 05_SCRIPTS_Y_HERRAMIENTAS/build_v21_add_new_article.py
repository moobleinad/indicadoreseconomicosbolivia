import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")

v20_path = os.path.join(theme_dir, "v20_theme_optimizado.xml")
v21_path = os.path.join(theme_dir, "v21_theme_optimizado.xml")

# KEEP V20 UNTOUCHED! READ FROM V20 TO CREATE V21
with open(v20_path, "r", encoding="utf-8") as f:
    v21_content = f.read()

# LIVE CDN IMAGE URL DELIVERED BY DANIEL (OPTIMIZED TO /s600/)
live_cdn_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIG7CrEnww8e0tXKx4-5T0fPI9VuIb-7be3g-Aor7fMkqxQbfp7JvolPod3WFzvozbUrNUjEX-ziAo0Cj3UucGIFBCgCEPglvySv5Jiy6L0zx0QpMPBHJZ9URfttZ5IlcSzotnsgH7yT_MVGefmNcC7tU5rgTr7QC_4zxfaQU_rdt_xQCugVJZCfbcTwu1/s600/02.03_foto_articulo1_rm245_oficial_horizontal.webp"
article_url = "https://www.danielsimons.xyz/2026/08/regimen-cambiario-como-funciona-ahora.html"

new_card_html = f'''                  <a href="{article_url}" class="ds-card-box">
                    <div>
                      <img src="{live_cdn_url}" alt="R&#233;gimen Cambiario: C&#243;mo funciona ahora el tipo de cambio del d&#243;lar en Bolivia" class="ds-card-thumb" />
                      <div class="title">R&#233;gimen Cambiario: C&#243;mo funciona ahora el tipo de cambio del d&#243;lar en Bolivia</div>
                      <div class="desc">Serie Politica Monetaria y Sociedad | Parte 1</div>
                    </div>
                    <div class="action">Leer Art&#237;culo &#10140;</div>
                  </a>

'''

# INSERT AT THE VERY TOP OF track-posts
target_track = '<div class="ds-carousel-track" id="track-posts">'
if target_track in v21_content:
    v21_content = v21_content.replace(target_track, target_track + "\n" + new_card_html)
    print("SUCCESSFULLY INSERTED NEW ARTICLE CARD INTO TRACK-POSTS!")
else:
    print("ERROR: COULD NOT FIND TRACK-POSTS CONTAINER IN v20")

with open(v21_path, "w", encoding="utf-8") as f:
    f.write(v21_content)

try:
    ET.parse(v21_path)
    print("SUCCESS: v21_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v21_path) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
