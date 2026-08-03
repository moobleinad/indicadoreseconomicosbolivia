import os
import shutil
import hashlib

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
juego_dir = os.path.join(root_dir, "07_JUEGO INFINITO")

# Target structured subfolders
subfolders = {
    "LIBROS": os.path.join(juego_dir, "01_LIBROS"),
    "MEDS": os.path.join(juego_dir, "02_MODELO_MEDS"),
    "MFEIR": os.path.join(juego_dir, "03_MODELO_MFEIR"),
    "INDIVIDUALISMO": os.path.join(juego_dir, "04_INDIVIDUALISMO_RELACIONAL"),
    "RESCATADOS": os.path.join(juego_dir, "05_RESCATADOS_Y_EVOLUTIVOS"),
    "AGENTES": os.path.join(juego_dir, "06_AGENTES_Y_PROMPTS")
}

for sf in subfolders.values():
    os.makedirs(sf, exist_ok=True)

# Scan sources
sources_to_scan = [
    os.path.join(root_dir, "REVISAR Y PASAR JUEGO INFINITO"),
    os.path.join(root_dir, "0 INDIVIDUALISMO RELACIONAL"),
    os.path.join(root_dir, "02_ARTICULOS_Y_PUBLICACIONES", "02.03_0_INDIVIDUALISMO_RELACIONAL")
]

seen_hashes = {}
moved_summary = []

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

for src in sources_to_scan:
    if not os.path.exists(src):
        continue
    for root, dirs, files in os.walk(src):
        for f in files:
            fp = os.path.join(root, f)
            if not os.path.isfile(fp):
                continue
            
            h = get_file_hash(fp)
            if h in seen_hashes:
                print(f"  [DUP DELETED/IGNORED] {f} (matches {seen_hashes[h]})")
                continue
            seen_hashes[h] = f
            
            # Determine destination subfolder
            fname_lower = f.lower()
            rel_path_lower = root.lower()
            
            if "mfeir" in fname_lower or "mfeir" in rel_path_lower:
                target_sub = subfolders["MFEIR"]
            elif "meds" in fname_lower or "estabilidad dinámica" in fname_lower or "estabilidad dinamica" in fname_lower:
                target_sub = subfolders["MEDS"]
            elif "agente" in fname_lower or "esceptico" in fname_lower or "escéptico" in fname_lower or "objeciones" in fname_lower:
                target_sub = subfolders["AGENTES"]
            elif "individualism" in fname_lower or "relacional" in fname_lower:
                target_sub = subfolders["INDIVIDUALISMO"]
            elif "rescatad" in rel_path_lower or "rescatad" in fname_lower:
                target_sub = subfolders["RESCATADOS"]
            elif f.endswith(".docx") or f.endswith(".pdf"):
                target_sub = subfolders["LIBROS"]
            else:
                target_sub = subfolders["RESCATADOS"]
                
            dest_fp = os.path.join(target_sub, f)
            shutil.copy2(fp, dest_fp)
            moved_summary.append((f, target_sub))
            print(f"  OK: {f} -> {os.path.basename(target_sub)}")

print(f"\nORGANIZATION OF ALL MODELS AND SUBFOLDERS COMPLETE! Total Unique Files Organized: {len(moved_summary)}")
