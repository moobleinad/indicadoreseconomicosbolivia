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

# Mapping of unique files to clean executive names
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
    "PLAN_CIERRE_NUCLEO_FILOSOFICO.md": "01.15_Plan_Cierre_Nucleo_Filosofico.md",
    "PROYECTO1.docx": "01.16_Proyecto1_Base_Estructura.docx",
    "PROYECTO_DE_MIGRACION.md": "01.17_Proyecto_de_Migracion.md"
}

# Copy unique files
print("--- COPYING & RENAMING UNIQUE FILES TO 07_JUEGO INFINITO/01_LIBROS ---")
for orig_f in unique_files:
    src_p = os.path.join(src_dir, orig_f)
    if orig_f in clean_mapping:
        dest_name = clean_mapping[orig_f]
    else:
        dest_name = orig_f
    dest_p = os.path.join(dst_dir, dest_name)
    shutil.copy2(src_p, dest_p)
    print(f"  OK: {orig_f} -> {dest_name}")

print("\n--- ANALYZING EACH UNIQUE FILE CONTENT ONE BY ONE ---")
summary_list = []

for orig_f in sorted(unique_files):
    dest_name = clean_mapping.get(orig_f, orig_f)
    dest_p = os.path.join(dst_dir, dest_name)
    
    text_snippet = ""
    word_count = 0
    
    if dest_name.endswith(".docx"):
        try:
            doc = docx.Document(dest_p)
            full_text = [p.text for p in doc.paragraphs if p.text.strip()]
            word_count = sum(len(p.split()) for p in full_text)
            text_snippet = "\n".join(full_text[:6])
        except Exception as e:
            text_snippet = f"Error reading docx: {e}"
    elif dest_name.endswith(".md"):
        try:
            with open(dest_p, "r", encoding="utf-8", errors="ignore") as f:
                c = f.read()
                word_count = len(c.split())
                text_snippet = c[:400]
        except Exception as e:
            text_snippet = f"Error reading md: {e}"
    elif dest_name.endswith(".pdf"):
        text_snippet = "[PDF File Document]"
        word_count = 0
    else:
        text_snippet = "[Other File Type]"
        
    summary_list.append({
        "orig": orig_f,
        "clean": dest_name,
        "words": word_count,
        "snippet": text_snippet
    })

# Write a comprehensive analysis report JSON and MD
analysis_md_path = os.path.join(root_dir, "07_JUEGO INFINITO", "ANALISIS_ESTRATEGICO_LIBROS_JUEGO_INFINITO.md")

with open(analysis_md_path, "w", encoding="utf-8") as f:
    f.write("# 📚 ANÁLISIS ESTRATÉGICO UNO A UNO: LIBROS Y DOCUMENTOS DE DANIEL SIMONS\n")
    f.write("### Sistema de Pensamiento: Del Individualismo Relacional al Juego Infinito\n\n")
    f.write(f"Total de Archivos Auditados en 'REVISAR Y PASAR JUEGO INFINITO': **{len(files)}**\n")
    f.write(f"Archivos Duplicados Eliminados: **{len(duplicates)}**\n")
    f.write(f"Obras Máster Únicas Clasificadas: **{len(unique_files)}**\n\n")
    f.write("="*60 + "\n\n")
    
    for idx, item in enumerate(summary_list, 1):
        f.write(f"## {idx}. {item['clean']}\n")
        f.write(f"- **Nombre Original:** `{item['orig']}`\n")
        f.write(f"- **Volumen de Texto:** ~{item['words']} palabras\n")
        f.write("- **Extracto del Contenido:**\n")
        f.write("```text\n")
        f.write(item['snippet'][:500] + "\n")
        f.write("```\n\n")

print("ANALYSIS COMPLETED & SAVED TO 07_JUEGO INFINITO/ANALISIS_ESTRATEGICO_LIBROS_JUEGO_INFINITO.md!")
