import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
target_dir = os.path.join(root_dir, "REVISAR Y PASAR JUEGO INFINITO")

files = os.listdir(target_dir)
print(f"TOTAL FILES IN 'REVISAR Y PASAR JUEGO INFINITO': {len(files)}\n")

for idx, f in enumerate(files, 1):
    fp = os.path.join(target_dir, f)
    sz = os.path.getsize(fp) / 1024
    print(f"{idx:02d}. {f} ({sz:.1f} KB)")
