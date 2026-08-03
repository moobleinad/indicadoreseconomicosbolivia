import os
import json

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
json_path = os.path.join(ind_dir, "08.02_Datos_Indicadores_Bolivia.json")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== JSON INDICATORS STRUCTURE ===")
print("Keys in JSON:", list(data.keys()))
if "indicadores" in data:
    for ind in data["indicadores"]:
        print(f"\n- ID: {ind.get('id')}, Nombre: {ind.get('nombre')}")
        print("  Semaforo:", ind.get("semaforo"))
        print("  Pestañas disponibles:", list(ind.keys()))
