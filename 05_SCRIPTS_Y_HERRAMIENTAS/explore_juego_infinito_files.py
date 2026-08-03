import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"

print("SCANNING WORKSPACE DIRECTORIES FOR BOOKS & JUEGO INFINITO:\n")

for item in os.listdir(root_dir):
    full_p = os.path.join(root_dir, item)
    if os.path.isdir(full_p):
        print(f"[DIR] {item}")
        try:
            sub_items = os.listdir(full_p)
            for s in sub_items[:10]:
                print(f"      - {s}")
            if len(sub_items) > 10:
                print(f"      ... and {len(sub_items)-10} more items.")
        except Exception as e:
            print("  Error listing:", e)
