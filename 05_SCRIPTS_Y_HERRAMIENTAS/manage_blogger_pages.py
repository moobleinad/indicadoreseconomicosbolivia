import os
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

BLOG_ID = '433667097766389126'
TOKEN_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\token.json'
SCOPES = ['https://www.googleapis.com/auth/blogger']

def get_service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    return build('blogger', 'v3', credentials=creds)

def fetch_all_posts(service):
    posts_result = service.posts().list(blogId=BLOG_ID, maxResults=50).execute()
    return posts_result.get('items', [])

def fetch_all_pages(service):
    pages_result = service.pages().list(blogId=BLOG_ID).execute()
    return pages_result.get('items', [])

def create_static_page(service, title, content):
    body = {
        "kind": "blogger#page",
        "title": title,
        "content": content
    }
    page = service.pages().insert(blogId=BLOG_ID, body=body).execute()
    return page

def main():
    service = get_service()
    print("--- CONEXIÓN EXITOSA A BLOGGER ---")
    
    posts = fetch_all_posts(service)
    print(f"Total de entradas encontradas: {len(posts)}")
    for p in posts:
        print(f" - [{p['id']}] {p['title']}")
        
    pages = fetch_all_pages(service)
    print(f"\nPáginas estáticas actuales: {len(pages)}")
    for pg in pages:
        print(f" - [{pg['id']}] {pg['title']} -> {pg['url']}")

if __name__ == "__main__":
    main()
