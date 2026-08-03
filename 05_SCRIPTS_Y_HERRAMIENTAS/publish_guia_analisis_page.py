import os
import json
import sys
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

sys.stdout.reconfigure(encoding='utf-8')

BLOG_ID = '433667097766389126'
GUIA_PAGE_ID = '872050355747455845'
TOKEN_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\04_API_BLOGGER_Y_AUTENTICACION\04.03_token.json'
SCOPES = ['https://www.googleapis.com/auth/blogger']
HTML_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\08_INDICADORES_ECONOMICOS\08.05_Guia_y_Analisis_Indicadores.html'

def get_service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    return build('blogger', 'v3', credentials=creds)

def publish_page():
    service = get_service()
    
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()

    target_title = "Guía y Análisis de Indicadores Económicos de Bolivia"
    
    body = {
        "title": target_title,
        "content": html_content
    }
    updated_page = service.pages().patch(blogId=BLOG_ID, pageId=GUIA_PAGE_ID, body=body).execute()
    print(f"Pagina 2 (Guía y Análisis) actualizada con exito!")
    print(f"URL: {updated_page.get('url')}")

    # Borrar la página duplicada si existe
    dup_id = '7148645510223278715'
    try:
        service.pages().delete(blogId=BLOG_ID, pageId=dup_id).execute()
        print(f"Pagina duplicada {dup_id} eliminada con exito.")
    except Exception as e:
        pass

if __name__ == "__main__":
    publish_page()
