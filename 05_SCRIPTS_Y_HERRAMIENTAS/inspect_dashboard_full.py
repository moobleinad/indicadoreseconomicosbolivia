import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
html_path = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS", "08.03_Dashboard_Indicadores_Economicos.html")
json_path = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS", "08.02_Datos_Indicadores_Bolivia.json")

with open(json_path, "r", encoding="utf-8") as f:
    print("JSON DATA:\n", f.read().encode("ascii", errors="replace").decode("ascii"))

with open(html_path, "r", encoding="utf-8") as f:
    c = f.read()
    s = c.find('<script>')
    print("\nSCRIPT IN HTML:\n", c[s:].encode("ascii", errors="replace").decode("ascii"))
