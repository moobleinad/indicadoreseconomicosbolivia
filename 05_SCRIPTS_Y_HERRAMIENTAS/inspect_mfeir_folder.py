import os
import docx

base_dir = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\0 INDIVIDUALISMO RELACIONAL'

print("=== ESTRUCTURA DE LA CARPETA 0 INDIVIDUALISMO RELACIONAL ===")

for root, dirs, files in os.walk(base_dir):
    rel_root = os.path.relpath(root, base_dir)
    print(f"\n[DIRECTORIO: {rel_root}]")
    for f in files:
        fpath = os.path.join(root, f)
        size_kb = os.path.getsize(fpath) / 1024
        print(f"  - {f} ({size_kb:.1f} KB)")

print("\n=== LEYENDO RESUMENES DE ARCHIVOS LLAVE ===")

# Read .txt files
txt_files = [
    r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\0 INDIVIDUALISMO RELACIONAL\MFEIR\MFEIRv1\2.1 MFEIRv1 FUNDAMENTACIÓN TEÓRICA CONCEPTUAL  .txt',
    r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\0 INDIVIDUALISMO RELACIONAL\rescatados\MODELO RELACIONAL.txt'
]

for tf in txt_files:
    if os.path.exists(tf):
        print(f"\n--- CONTENIDO DE: {os.path.basename(tf)} ---")
        try:
            with open(tf, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                print(content[:1500])
        except Exception as e:
            print("Error reading txt:", e)

# Read summaries from key DOCX files
docx_files = [
    r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\0 INDIVIDUALISMO RELACIONAL\MFEIR\300 PROPUESTA FORMALIZACIÓN MFEIR.docx',
    r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\0 INDIVIDUALISMO RELACIONAL\MFEIR\0 INFORME MFEIR01v1  DECISIÓN METODOLÓGICA MFEIRv2.docx',
    r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\0 INDIVIDUALISMO RELACIONAL\MFEIR\1 IMPLEMENTACIÓN MFEIRv2.docx'
]

for df in docx_files:
    if os.path.exists(df):
        print(f"\n--- RESUMEN DE: {os.path.basename(df)} ---")
        try:
            doc = docx.Document(df)
            fullText = [p.text for p in doc.paragraphs if p.text.strip()]
            print("\n".join(fullText[:15]))
        except Exception as e:
            print("Error reading docx:", e)
