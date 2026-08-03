import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
v34_path = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado", "v34_theme_optimizado.xml")

with open(v34_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

head_start = xml_content.find("<head>")
head_end = xml_content.find("</head>")

if head_start != -1 and head_end != -1:
    head_block = xml_content[head_start:head_end+7]
    print("=== HEAD BLOCK IN V34 ===")
    lines = head_block.split("\n")
    for idx, l in enumerate(lines[:60], 1):
        print(f"{idx:02d}: {l}")
