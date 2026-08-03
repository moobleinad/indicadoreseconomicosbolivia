import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v37_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v37_theme_optimizado.xml")
v38_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v38_theme_optimizado.xml")

with open(v37_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("=== SEARCHING FOR POST.BODY IN THEME XML ===")
for idx, line in enumerate(lines, 1):
    if "post.body" in line or "post-body" in line:
        print(f"Line {idx}: {line.strip()}")
        # Print surrounding lines
        start = max(0, idx - 5)
        end = min(len(lines), idx + 5)
        for s in range(start, end):
            print(f"  [{s+1}] {lines[s].strip()}")
        print("-" * 50)
