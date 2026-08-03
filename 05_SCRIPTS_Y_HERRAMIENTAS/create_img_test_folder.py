import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
test_dir = os.path.join(root_dir, "01_LINEA_GRAFICA_Y_ASSETS", "01.08_PRUEBAS_IMAGENES_NEURO_REALISTAS")
os.makedirs(test_dir, exist_ok=True)

print("Created folder:", test_dir)
