import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
html_path = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS", "08.03_Dashboard_Indicadores_Economicos.html")

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

print("HTML LENGTH:", len(content))
print("HTML SNIPPET:\n", content[:2500])
