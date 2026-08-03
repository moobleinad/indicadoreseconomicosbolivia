import os
import base64
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
token_path = os.path.join(root_dir, "token.json")
blog_id = "433667097766389126"

creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/blogger'])
service = build('blogger', 'v3', credentials=creds)

thumb_destilado_path = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_destilado_1785593994402.jpg"
thumb_forja_path = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_forja_1785594011419.jpg"

with open(thumb_destilado_path, "rb") as f:
    b64_dest = base64.b64encode(f.read()).decode("utf-8")

with open(thumb_forja_path, "rb") as f:
    b64_forj = base64.b64encode(f.read()).decode("utf-8")

content = f"""
<div>
  <img id="img-destilado" src="data:image/jpeg;base64,{b64_dest}" alt="Thumb Destilado" />
  <img id="img-forja" src="data:image/jpeg;base64,{b64_forj}" alt="Thumb Forja" />
</div>
"""

post_body = {
    'title': 'Imágenes Oficiales Servicios Destilado y Forja',
    'content': content,
    'labels': ['system-assets']
}

created_post = service.posts().insert(blogId=blog_id, body=post_body).execute()
print("Created Assets Post ID:", created_post.get('id'))
print("Fetched Post Images:", created_post.get('images', []))
