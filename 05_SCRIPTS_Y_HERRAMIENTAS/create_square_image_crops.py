import os
from PIL import Image

src_img = r'C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\foto_articulo1_bth_v4_1785592381896.jpg'
out_dir = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz'
square_out_path = os.path.join(out_dir, 'foto_articulo1_bth_cuadrada.jpg')

with Image.open(src_img) as img:
    w, h = img.size
    min_dim = min(w, h)
    
    # Center crop to 1:1 square
    left = (w - min_dim) / 2
    top = (h - min_dim) / 2
    right = (w + min_dim) / 2
    bottom = (h + min_dim) / 2
    
    cropped_img = img.crop((left, top, right, bottom))
    resized_img = cropped_img.resize((1080, 1080), Image.Resampling.LANCZOS)
    resized_img.save(square_out_path, 'JPEG', quality=95)
    
    print(f"SUCCESS: Created 1:1 square image (1080x1080 px): {square_out_path}")
