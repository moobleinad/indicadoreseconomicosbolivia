import os
import json
import sys
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

sys.stdout.reconfigure(encoding='utf-8')

BLOG_ID = '433667097766389126'
DASHBOARD_PAGE_ID = '7694550740270244064'
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TOKEN_FILE = os.getenv("BLOGGER_TOKEN_FILE", os.path.join(BASE_DIR, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json"))
SCOPES = ['https://www.googleapis.com/auth/blogger']
HTML_FILE = os.path.join(BASE_DIR, "08_INDICADORES_ECONOMICOS", "08.03_Dashboard_Indicadores_Economicos.html")

def get_service():
    token_json_env = os.getenv("BLOGGER_TOKEN_JSON")
    if token_json_env:
        token_data = json.loads(token_json_env)
        creds = Credentials.from_authorized_user_info(token_data, SCOPES)
    else:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    return build('blogger', 'v3', credentials=creds)

def publish_page():
    service = get_service()
    
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()

    target_title = "Indicadores Económicos de Bolivia"
    
    body = {
        "title": target_title,
        "content": html_content
    }
    updated_page = service.pages().patch(blogId=BLOG_ID, pageId=DASHBOARD_PAGE_ID, body=body).execute()
    print(f"Pagina 1 (Dashboard) actualizada con exito!")
    print(f"URL: {updated_page.get('url')}")

if __name__ == "__main__":
    publish_page()
