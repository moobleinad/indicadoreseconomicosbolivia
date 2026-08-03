import os
from PIL import Image

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
src_jpg = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\foto_oficial_alt2_alt5_rm245_1785641707070.jpg"

target_dir = os.path.join(root_dir, "02_ARTICULOS_Y_PUBLICACIONES", "02.03_Articulo_Serie_1_Resolucion_Ministerial_245")
out_webp = os.path.join(target_dir, "02.03_foto_articulo1_rm245_oficial.webp")

im = Image.open(src_jpg).convert("RGB")
im.save(out_webp, "WEBP", quality=82)

print(f"Official Combined Image Alt2+Alt5 Saved: {out_webp} ({os.path.getsize(out_webp)/1024:.2f} KB)")
