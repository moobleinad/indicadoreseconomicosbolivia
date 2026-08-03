import os
import base64
from PIL import Image

dir_path = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\linea grafica'

img_mobile_path = os.path.join(dir_path, 'ChatGPT Image 31 jul 2026, 11_40_15 p.m.png')
img_pc_path = os.path.join(dir_path, 'LOGO 2.png')

def convert_to_svg(img_path, svg_out_path):
    with Image.open(img_path) as img:
        w, h = img.size
        with open(img_path, 'rb') as f:
            b64_data = base64.b64encode(f.read()).decode('utf-8')
            
        mime = 'image/png' if img_path.lower().endswith('.png') else 'image/jpeg'
        svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#000000"/>
  <image width="{w}" height="{h}" xlink:href="data:{mime};base64,{b64_data}"/>
</svg>'''
        with open(svg_out_path, 'w', encoding='utf-8') as f_svg:
            f_svg.write(svg_content)
        print(f"SUCCESS: Converted {os.path.basename(img_path)} ({w}x{h}) to SVG: {svg_out_path}")

if __name__ == "__main__":
    convert_to_svg(img_mobile_path, os.path.join(dir_path, 'cabecera_mobile.svg'))
    convert_to_svg(img_pc_path, os.path.join(dir_path, 'cabecera_pc.svg'))
