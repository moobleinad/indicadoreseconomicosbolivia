import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v25_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v25_theme_optimizado.xml")

with open(v25_path, "r", encoding="utf-8") as f:
    c = f.read()

head_start = c.find("<head>")
head_end = c.find("</head>")

print("HEAD METAS AND TAGS:\n")
head_snippet = c[head_start:head_end]
for line in head_snippet.split("\n"):
    if "<meta" in line.lower() or "<title" in line.lower() or "og:" in line.lower() or "twitter:" in line.lower() or "b:include" in line.lower():
        print(line.strip())
