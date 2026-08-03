import os

art_base_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\02_ARTICULOS_Y_PUBLICACIONES"

loose_files = [
    "02.03_Articulo_Serie_1_Resolucion_Ministerial_245.docx",
    "02.03_Articulo_Serie_1_Resolucion_Ministerial_245.md",
    "~$.03_Articulo_Serie_1_Resolucion_Ministerial_245.docx"
]

for f in loose_files:
    p = os.path.join(art_base_dir, f)
    if os.path.exists(p):
        try:
            os.remove(p)
            print(f"Removed loose file: {f}")
        except Exception as e:
            print(f"Could not remove {f}: {e}")

print("Cleaned up loose files in 02_ARTICULOS_Y_PUBLICACIONES!")
