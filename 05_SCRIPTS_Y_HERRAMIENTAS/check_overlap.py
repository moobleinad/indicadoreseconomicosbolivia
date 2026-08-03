from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

BLOG_ID = '433667097766389126'
TOKEN_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\token.json'
SCOPES = ['https://www.googleapis.com/auth/blogger']

creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
service = build('blogger', 'v3', credentials=creds)

posts = service.posts().list(blogId=BLOG_ID, maxResults=50).execute().get('items', [])
pages = service.pages().list(blogId=BLOG_ID).execute().get('items', [])

print("=== PAGINAS ESTATICAS EXISTENTES EN BLOGGER ===")
page_map = {}
for pg in pages:
    t = pg['title'].strip()
    page_map[t.lower()] = pg
    print(f"PAGINA: {t} -> {pg.get('url')}")

print("\n=== COINCIDENCIAS (ENTRADAS QUE YA TIENEN PAGINA ESTATICA) ===")
coincidences = set()
for p in posts:
    pt = p['title'].strip()
    matched = None
    for pgt, pg_obj in page_map.items():
        if pgt in pt.lower() or pt.lower() in pgt:
            matched = pg_obj
            break
    
    if matched:
        print(f"COINCIDENCIA ENCONTRADA:")
        print(f"  - Entrada (Post): '{pt}'")
        print(f"  - Pagina Estatica (Page): '{matched['title']}' ({matched.get('url')})")
        coincidences.add(pt)

print("\n=== ENTRADAS QUE SOLO EXISTEN COMO ARTICULOS ===")
for p in posts:
    pt = p['title'].strip()
    if pt not in coincidences:
        print(f"ENTRADA: '{pt}'")
