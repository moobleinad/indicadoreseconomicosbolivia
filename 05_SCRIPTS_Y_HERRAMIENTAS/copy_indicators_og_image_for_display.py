import os
import shutil

src = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\foto_og_indicadores_economicos_horizontal_1785694970637.jpg"
dst_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\08_INDICADORES_ECONOMICOS"
dst = os.path.join(dst_dir, "foto_og_indicadores_economicos_horizontal.jpg")

shutil.copy(src, dst)
print("COPIED JPG FOR DISPLAY:", dst)
