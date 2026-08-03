import os
from PIL import Image

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
static_img_dir = os.path.join(root_dir, "09_IMAGENES_PAGINAS_ESTATICAS")
os.makedirs(static_img_dir, exist_ok=True)

src_jpg = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\afiche_indicadores_letras_blancas_cuadrado_1785712069047.jpg"
out_webp = os.path.join(static_img_dir, "09.02_afiche_indicadores_economicos_cuadrado.webp")

im = Image.open(src_jpg).convert("RGB")
im.save(out_webp, "WEBP", quality=88)

print(f"SUCCESS: Saved updated square poster WebP: {out_webp} ({os.path.getsize(out_webp)/1024:.2f} KB)")
