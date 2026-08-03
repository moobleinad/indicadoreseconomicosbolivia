import os
import shutil

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
juego_dir = os.path.join(root_dir, "07_JUEGO INFINITO")

orig_dir = os.path.join(juego_dir, "ORIGINALES")
v2026_dir = os.path.join(juego_dir, "2026")

os.makedirs(orig_dir, exist_ok=True)
os.makedirs(v2026_dir, exist_ok=True)

# Subfolders currently in 07_JUEGO INFINITO to move into ORIGINALES
subfolders_to_move = [
    "01_LIBROS",
    "02_MODELO_MEDS",
    "03_MODELO_MFEIR",
    "04_INDIVIDUALISMO_RELACIONAL",
    "05_RESCATADOS_Y_EVOLUTIVOS",
    "06_AGENTES_Y_PROMPTS"
]

for sf in subfolders_to_move:
    src_sf = os.path.join(juego_dir, sf)
    dst_sf = os.path.join(orig_dir, sf)
    if os.path.exists(src_sf) and not os.path.exists(dst_sf):
        shutil.move(src_sf, dst_sf)
        print(f"MOVED TO ORIGINALES: {sf}")

# Create parallel 2026 structure for advanced editions
subfolders_2026 = [
    "01_LIBROS_2026",
    "02_MODELO_MEDS_2026",
    "03_MODELO_MFEIR_2026",
    "04_INDIVIDUALISMO_RELACIONAL_2026",
    "05_PRODUCTOS_Y_SERVICIOS_2026",
    "06_AGENTES_Y_PROMPTS_2026"
]

for sf in subfolders_2026:
    p = os.path.join(v2026_dir, sf)
    os.makedirs(p, exist_ok=True)
    print(f"CREATED 2026 SUBFOLDER: 2026/{sf}")

print("\nSUCCESS: ORIGINALES and 2026 folders configured cleanly!")
