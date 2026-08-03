import os
from PIL import Image

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
test_dir = os.path.join(root_dir, "01_LINEA_GRAFICA_Y_ASSETS", "01.08_PRUEBAS_IMAGENES_NEURO_REALISTAS")

images = [
    ("alt1_ejecutivo_smartphone", r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\alt1_ejecutivo_smartphone_1785639816355.jpg"),
    ("alt2_manos_divisas", r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\alt2_manos_divisas_1785639842810.jpg"),
    ("alt3_reunion_socios", r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\alt3_reunion_socios_1785639870572.jpg"),
    ("alt4_escritorio_financiero", r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\alt4_escritorio_financiero_1785639898250.jpg"),
    ("alt5_equipetrol_urbano", r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\alt5_equipetrol_urbano_1785639928146.jpg")
]

for name, src in images:
    out_webp = os.path.join(test_dir, f"{name}.webp")
    if os.path.exists(src):
        im = Image.open(src).convert("RGB")
        im.save(out_webp, "WEBP", quality=82)
        print(f"Saved: {out_webp} ({os.path.getsize(out_webp)/1024:.2f} KB)")
