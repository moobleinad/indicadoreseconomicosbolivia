import os
import base64
from PIL import Image, ImageDraw, ImageFont

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
img_destilado = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_destilado_1785593994402.jpg"
img_forja = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_forja_1785594011419.jpg"

def create_styled_square_thumb(filename, text_title, bg_color=(13, 13, 13), accent_color=(188, 167, 114)):
    out_path = os.path.join(root_dir, filename)
    img = Image.new('RGB', (600, 600), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw border and gold accents
    draw.rectangle([10, 10, 590, 590], outline=accent_color, width=3)
    draw.rectangle([20, 20, 580, 580], outline=(40, 40, 40), width=1)
    
    # Draw title text centered
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
        
    bbox = draw.textbbox((0, 0), text_title, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((600 - tw)/2, (600 - th)/2), text_title, fill=accent_color, font=font)
    
    img.save(out_path, 'JPEG', quality=95)
    print(f"Created styled thumb: {out_path}")
    return out_path

create_styled_square_thumb("thumb_mkt360.jpg", "MARKETING 360°")
create_styled_square_thumb("thumb_mype.jpg", "IMPULSO MYPE")
create_styled_square_thumb("thumb_juego.jpg", "JUEGO EMPRENDEDOR")
create_styled_square_thumb("thumb_mfeir.jpg", "MODELO MFEIR")

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

uri_destilado = get_b64(img_destilado)
uri_forja = get_b64(img_forja)
uri_mkt360 = get_b64(os.path.join(root_dir, "thumb_mkt360.jpg"))
uri_mype = get_b64(os.path.join(root_dir, "thumb_mype.jpg"))
uri_juego = get_b64(os.path.join(root_dir, "thumb_juego.jpg"))
uri_mfeir = get_b64(os.path.join(root_dir, "thumb_mfeir.jpg"))
uri_art1 = get_b64(os.path.join(root_dir, "foto_articulo1_bth_cuadrada.jpg"))

print("All 6 Data URIs ready for v11 theme!")
