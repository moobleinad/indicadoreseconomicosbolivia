import os
from PIL import Image

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
src_jpg = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\foto_articulo2_dolar_mype_1785634415860.jpg"

out_dir = os.path.join(root_dir, "01_LINEA_GRAFICA_Y_ASSETS")
out_webp = os.path.join(out_dir, "01.06_foto_articulo2_dolar_mype_oficial.webp")

im = Image.open(src_jpg).convert("RGB")
im.save(out_webp, "WEBP", quality=82)

print(f"Generated Article 2 WebP: {out_webp} (Size: {os.path.getsize(out_webp)/1024:.2f} KB)")
