import os
import base64
from PIL import Image

dir_path = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\linea grafica'
img_path = os.path.join(dir_path, 'Cabecera_Daniel_Simons.png')
svg_out_path = os.path.join(dir_path, 'Cabecera_Daniel_Simons.svg')

with Image.open(img_path) as img:
    w, h = img.size
    with open(img_path, 'rb') as f:
        b64_data = base64.b64encode(f.read()).decode('utf-8')
        
    mime = 'image/png'
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#000000"/>
  <image width="{w}" height="{h}" xlink:href="data:{mime};base64,{b64_data}"/>
</svg>'''

    with open(svg_out_path, 'w', encoding='utf-8') as f_svg:
        f_svg.write(svg_content)
        
    print(f"SUCCESS: Converted {os.path.basename(img_path)} ({w}x{h}) to SVG: {svg_out_path}")
