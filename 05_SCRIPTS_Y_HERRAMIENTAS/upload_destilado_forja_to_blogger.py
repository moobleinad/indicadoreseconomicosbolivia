import os
import json
import base64
import xml.etree.ElementTree as ET
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
token_path = os.path.join(root_dir, "token.json")
blog_id = "433667097766389126"

creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/blogger'])
service = build('blogger', 'v3', credentials=creds)

print("=== SUBIENDO IMÁGENES OFICIALES DE DESTILADO Y FORJA A BLOGGER CDN ===")

# Image paths
thumb_destilado_path = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_destilado_1785593994402.jpg"
thumb_forja_path = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_forja_1785594011419.jpg"

with open(thumb_destilado_path, "rb") as f:
    b64_destilado = base64.b64encode(f.read()).decode("utf-8")

with open(thumb_forja_path, "rb") as f:
    b64_forja = base64.b64encode(f.read()).decode("utf-8")

uri_dest = f"data:image/jpeg;base64,{b64_destilado}"
uri_forj = f"data:image/jpeg;base64,{b64_forja}"

# Get pages from Blogger
pages = service.pages().list(blogId=blog_id).execute().get('items', [])

url_dest_cdn = ""
url_forj_cdn = ""

for p in pages:
    title = p.get('title', '')
    page_id = p.get('id')
    
    if "destilado" in title.lower():
        print("Actualizando Página Destilado de Ideas ID:", page_id)
        current = p.get('content', '')
        new_content = f'<div style="text-align:center; margin-bottom:20px;"><img src="{uri_dest}" alt="Destilado de Ideas" style="width:100%; max-width:600px; height:auto; border-radius:8px;" /></div>\n' + current
        p['content'] = new_content
        updated = service.pages().update(blogId=blog_id, pageId=page_id, body=p).execute()
        print("Destilado actualizada!")
        
    elif "forja" in title.lower():
        print("Actualizando Página Forja de Proyectos ID:", page_id)
        current = p.get('content', '')
        new_content = f'<div style="text-align:center; margin-bottom:20px;"><img src="{uri_forj}" alt="Forja de Proyectos" style="width:100%; max-width:600px; height:auto; border-radius:8px;" /></div>\n' + current
        p['content'] = new_content
        updated = service.pages().update(blogId=blog_id, pageId=page_id, body=p).execute()
        print("Forja actualizada!")

print("\nSUCCESS: Páginas en Blogger actualizadas con sus imágenes reales!")
