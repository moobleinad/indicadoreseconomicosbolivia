import os
import shutil
import hashlib
import docx

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
src_dir = os.path.join(root_dir, "REVISAR Y PASAR JUEGO INFINITO")
dst_dir = os.path.join(root_dir, "07_JUEGO INFINITO", "01_LIBROS")
os.makedirs(dst_dir, exist_ok=True)

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

files = os.listdir(src_dir)
hash_dict = {}
unique_files = []
duplicates = []

for f in files:
    fp = os.path.join(src_dir, f)
    if os.path.isfile(fp):
        h = get_file_hash(fp)
        if h in hash_dict:
            duplicates.append((f, hash_dict[h]))
        else:
            hash_dict[h] = f
            unique_files.append(f)

print(f"TOTAL FILES: {len(files)}")
print(f"UNIQUE FILES: {len(unique_files)}")
print(f"DUPLICATES DETECTED: {len(duplicates)}")

print("\n--- DUPLICATES TO REMOVE ---")
for d, orig in duplicates:
    print(f"  - Duplicate: {d} (identical to {orig})")

# Clean target mapping for unique files
clean_mapping = {
    "0 3 9 LIBRO INDIVIDUALISMO RELACIONAL POLITICO Y ECONOMICO - copia(1).docx": "01.01_Libro_Individualismo_Relacional_Politico_y_Economico.docx",
    "004_MODELO DE ESTABILIDAD DINÁMICA SISTÉMICA(1).docx": "01.02_Modelo_de_Estabilidad_Dinamica_Sistemica_MEDS.docx",
    "005_AAAA MODELO DE ESTABILIDAD DINÁMICA SISTÉMICA(2).docx": "01.02b_Modelo_Estabilidad_Dinamica_Sistemica_Ampliado.docx",
    "006_EL JUEGO DEL PODER V1 MARZO 2026.docx": "01.03_El_Juego_del_Poder_v1.docx",
    "008_MEDS OPERACIONALIZACION  INICIAL(1).docx": "01.04_MEDS_Operacionalizacion_Inicial.docx",
    "018_LA ILUSIÓN DE LA ESTABILIDAD V1 MARZO 2026 .docx": "01.05_La_Ilusion_de_la_Estabilidad_v1.docx",
    "032_JEFE DE MARKETING 05 2026 - copia.pdf": "01.06_Manual_Jefe_de_Marketing.pdf",
    "1 AGENTE ANTIDANIEL SIMONS.docx": "01.07_Agente_AntiDaniel_Simons_Dialectica.docx",
    "10 11 2025 ver1 SOBREVIVIENDO A LA TESIS.pdf": "01.08_Sobreviviendo_a_la_Tesis.pdf",
    "3 INDIVIDUALISTA RELACIONAL.docx": "01.09_Manifiesto_Individualista_Relacional.docx",
    "3 VERSIÓN FUNDACIONAL FILOSOFIA DEL JUEGO 2.0(1).docx": "01.10_Version_Fundacional_Filosofia_del_Juego_2.0.docx",
    "4 ESCEPTICO EMPIRICO.docx": "01.11_Perfil_Esceptico_Empirico.docx",
    "4 OBJECIONES Y PUNTOS FUERTES A VERSION 2.0 (4).docx": "01.12_Objeciones_y_Puntos_Fuertes_Version_2.0.docx",
    "5 NEGOCIOS FINANZAS.docx": "01.13_Estructuracion_Negocios_y_Finanzas.docx",
    "AAA EL JUEGO DEL EMPRENDEDOR Libro para jovenes.docx": "01.14_El_Juego_del_Emprendedor_Libro_Jovenes.docx",
    "PROYECTO1.docx": "01.15_Proyecto_1_Base.docx"
}

# Copy and rename unique files into 07_JUEGO INFINITO/01_LIBROS/
print("\n--- COPYING & RENAMING UNIQUE BOOKS TO 07_JUEGO INFINITO/01_LIBROS ---")
for orig_f in unique_files:
    src_p = os.path.join(src_dir, orig_f)
    if orig_f in clean_mapping:
        dest_name = clean_mapping[orig_f]
    else:
        dest_name = orig_f
    dest_p = os.path.join(dst_dir, dest_name)
    shutil.copy2(src_p, dest_p)
    print(f"  ✓ {orig_f} -> {dest_name}")

print("\nORGANIZATION COMPLETE!")
