import os
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

BLOG_ID = '433667097766389126'
TOKEN_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\token.json'
SCOPES = ['https://www.googleapis.com/auth/blogger']

# Target service post IDs to convert to Static Pages
TARGET_SERVICE_POST_IDS = [
    '6510575811332764929', # DESTILADO DE IDEAS DE NEGOCIO
    '6210313043372536832', # FORJA
    '5500517356527264167', # MARKETING 360
    '1481924812236707286', # Impulso MYPE 360
    '2868870457539510865'  # EL JUEGO DEL EMPRENDEDOR
]

def get_service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    return build('blogger', 'v3', credentials=creds)

def convert_posts_to_pages():
    service = get_service()
    
    # Check existing pages to avoid duplicating
    existing_pages = service.pages().list(blogId=BLOG_ID).execute().get('items', [])
    existing_titles = [pg['title'].strip().lower() for pg in existing_pages]
    
    created_pages = []

    for post_id in TARGET_SERVICE_POST_IDS:
        try:
            post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
            title = post.get('title', '').strip()
            content = post.get('content', '')

            # Add WhatsApp CTA box at the end of each service page
            cta_box = """
            <div style="background: rgba(188, 167, 114, 0.1); border: 1px solid #bca772; border-radius: 12px; padding: 20px; margin-top: 30px; text-align: center; font-family: sans-serif;">
                <h3 style="color: #bca772; margin-top: 0; font-size: 20px;">¿Te interesa implementar este servicio en tu proyecto?</h3>
                <p style="color: #e0e0e0; font-size: 15px;">Ponte en contacto directo con Daniel Simons para coordinar una consultoría estratégica personalizada.</p>
                <a href="https://api.whatsapp.com/send?phone=59178000000&text=Hola%20Daniel,%20quisiera%20mas%20informacion%20sobre%20" + title + "' target='_blank' style='display: inline-block; background: linear-gradient(135deg, #bca772 0%, #997a15 100%); color: #000; font-weight: bold; padding: 12px 24px; border-radius: 25px; text-decoration: none; margin-top: 10px;'>📲 Contactar por WhatsApp</a>
            </div>
            """
            
            full_page_content = content + cta_box

            # Check if page with similar title exists
            if title.lower() in existing_titles:
                print(f"PAGE ALREADY EXISTS: {title}")
                continue

            page_body = {
                "kind": "blogger#page",
                "title": title,
                "content": full_page_content
            }
            
            created_page = service.pages().insert(blogId=BLOG_ID, body=page_body).execute()
            created_pages.append(created_page)
            print(f"CREATED PAGE: [{created_page['id']}] {created_page['title']} -> {created_page['url']}")

        except Exception as e:
            print(f"Error processing post {post_id}: {e}")

    return created_pages

if __name__ == "__main__":
    convert_posts_to_pages()
