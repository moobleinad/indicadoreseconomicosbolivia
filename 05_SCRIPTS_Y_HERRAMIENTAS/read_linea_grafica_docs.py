import os
import docx

base_dir = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\linea grafica'

docx_files = ['GUIA.docx', 'PROMPT1.docx', 'estilo de imagen.docx']

for df in docx_files:
    fpath = os.path.join(base_dir, df)
    print(f"\n==========================================")
    print(f"DOCUMENTO: {df}")
    print(f"==========================================")
    if os.path.exists(fpath):
        try:
            doc = docx.Document(fpath)
            fullText = [p.text for p in doc.paragraphs if p.text.strip()]
            print("\n".join(fullText))
        except Exception as e:
            print("Error reading docx:", e)
