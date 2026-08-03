import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/blogger']
CLIENT_SECRET_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\client_secret.json'
TOKEN_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\token.json'
BLOG_ID = '433667097766389126'

def get_blogger_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())

    return build('blogger', 'v3', credentials=creds)

def list_posts_and_pages():
    service = get_blogger_service()
    
    print("--- BLOG INFO ---")
    blog = service.blogs().get(blogId=BLOG_ID).execute()
    print(f"Blog Title: {blog.get('name')}")
    print(f"Blog URL: {blog.get('url')}")
    
    print("\n--- ENTRADAS (POSTS) ---")
    posts_result = service.posts().list(blogId=BLOG_ID, maxResults=50).execute()
    posts = posts_result.get('items', [])
    for p in posts:
        print(f"ID: {p['id']} | Title: {p['title']} | URL: {p['url']}")

    print("\n--- PÁGINAS ESTÁTICAS (PAGES) ---")
    pages_result = service.pages().list(blogId=BLOG_ID).execute()
    pages = pages_result.get('items', [])
    if pages:
        for pg in pages:
            print(f"ID: {pg['id']} | Title: {pg['title']} | URL: {pg['url']}")
    else:
        print("No static pages created yet.")

if __name__ == "__main__":
    list_posts_and_pages()
