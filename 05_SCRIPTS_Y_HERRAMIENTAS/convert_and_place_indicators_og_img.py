import os
from PIL import Image

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
src_jpg = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\foto_og_indicadores_economicos_horizontal_1785694970637.jpg"

target_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
out_webp = os.path.join(target_dir, "08.04_foto_og_indicadores_economicos_horizontal.webp")

im = Image.open(src_jpg).convert("RGB")
im.save(out_webp, "WEBP", quality=85)

print(f"Official Horizontal 16:9 Indicators OG Image Saved: {out_webp} ({os.path.getsize(out_webp)/1024:.2f} KB)")
