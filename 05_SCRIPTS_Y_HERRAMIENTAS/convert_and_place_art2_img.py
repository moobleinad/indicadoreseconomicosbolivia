import os
from PIL import Image

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
src_jpg = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\foto_oficial_horizontal_16_9_serie2_1785672174797.jpg"

target_dir = os.path.join(root_dir, "02_ARTICULOS_Y_PUBLICACIONES", "02.04_Articulo_Serie_2_Flotacion_Libre_vs_Flotacion_Sucia")
out_webp = os.path.join(target_dir, "02.04_foto_articulo2_flotacion_oficial_horizontal.webp")

im = Image.open(src_jpg).convert("RGB")
im.save(out_webp, "WEBP", quality=82)

print(f"Official Horizontal 16:9 Series Article 2 Image Saved: {out_webp} ({os.path.getsize(out_webp)/1024:.2f} KB)")
