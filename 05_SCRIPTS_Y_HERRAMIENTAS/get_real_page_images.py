import os
import json
import re
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
token_path = os.path.join(root_dir, "token.json")
blog_id = "433667097766389126"

creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/blogger'])
service = build('blogger', 'v3', credentials=creds)

print("=== BUSCANDO IMÁGENES REALES EN PÁGINAS Y ENTRADAS DE BLOGGER ===")
pages = service.pages().list(blogId=blog_id).execute().get('items', [])
posts = service.posts().list(blogId=blog_id).execute().get('items', [])

image_map = {}

def extract_first_img(html_content):
    match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', html_content, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

for p in pages:
    title = p.get('title')
    url = p.get('url')
    content = p.get('content', '')
    img = extract_first_img(content)
    print(f"PÁGINA: {title}")
    print(f"  URL: {url}")
    print(f"  IMAGEN REAL: {img}")
    if img:
        image_map[url] = img

for p in posts:
    title = p.get('title')
    url = p.get('url')
    content = p.get('content', '')
    img = extract_first_img(content)
    print(f"POST: {title}")
    print(f"  URL: {url}")
    print(f"  IMAGEN REAL: {img}")
    if img:
        image_map[url] = img

with open(os.path.join(root_dir, "image_map.json"), "w", encoding="utf-8") as f:
    json.dump(image_map, f, indent=2)

print("\nSUCCESS: Saved real image map to image_map.json!")
