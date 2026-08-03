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

pages = service.pages().list(blogId=blog_id).execute().get('items', [])

print("=== IMÁGENES REALES EN DESTILADO Y FORJA ===")
for p in pages:
    title = p.get('title', '')
    url = p.get('url', '')
    content = p.get('content', '')
    
    if "destilado" in title.lower() or "forja" in title.lower():
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
        print(f"PÁGINA: {title} ({url})")
        print(f"  IMÁGENES ENCONTRADAS: {imgs}\n")
