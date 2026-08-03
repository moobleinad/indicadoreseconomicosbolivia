import os
import json
import time
import urllib.request
import urllib.parse

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
html_path = os.path.join(ind_dir, "08.03_Dashboard_Indicadores_Economicos.html")
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

# Read current HTML code
with open(html_path, "r", encoding="utf-8") as f:
    dashboard_html = f.read()

# Authenticate Blogger API v3
with open(token_path, "r", encoding="utf-8") as f:
    token_data = json.load(f)
with open(secret_path, "r", encoding="utf-8") as f:
    secret_data = json.load(f)

client_info = secret_data.get("installed") or secret_data.get("web") or {}
client_id = client_info.get("client_id")
client_secret = client_info.get("client_secret")
refresh_token = token_data.get("refresh_token")

refresh_url = "https://oauth2.googleapis.com/token"
refresh_payload = urllib.parse.urlencode({
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token,
    "grant_type": "refresh_token"
}).encode("utf-8")

req_token = urllib.request.Request(refresh_url, data=refresh_payload, headers={"Content-Type": "application/x-www-form-urlencoded"})

with urllib.request.urlopen(req_token) as resp:
    new_token_resp = json.loads(resp.read().decode("utf-8"))
    access_token = new_token_resp["access_token"]
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    req_blogs = urllib.request.Request("https://www.googleapis.com/blogger/v3/users/self/blogs", headers=headers)
    with urllib.request.urlopen(req_blogs) as b_resp:
        blogs_data = json.loads(b_resp.read().decode("utf-8"))
        blog_id = blogs_data["items"][0]["id"]
        
        # 1. Fetch current pages
        pages_url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/pages"
        req_pages = urllib.request.Request(pages_url, headers=headers)
        with urllib.request.urlopen(req_pages) as p_resp:
            pages_data = json.loads(p_resp.read().decode("utf-8"))
            existing_pages = pages_data.get("items", [])
            
        print(f"FOUND {len(existing_pages)} EXISTING PAGES IN BLOGGER.")
        
        # Identify old pages to delete
        old_pages_to_delete = []
        for p in existing_pages:
            title_l = p.get("title", "").lower()
            url_l = p.get("url", "").lower()
            if "indicadores" in title_l or "indicadores" in url_l:
                old_pages_to_delete.append(p)
                print(f"IDENTIFIED OLD PAGE TO DELETE: ID={p['id']}, Title='{p.get('title')}', URL='{p.get('url')}'")
                
        # 2. CREATE BRAND NEW STATIC PAGE
        new_page_payload = {
            "kind": "blogger#page",
            "title": "INDICADORES ECONÓMICOS DE BOLIVIA",
            "content": dashboard_html
        }
        
        req_create = urllib.request.Request(pages_url, data=json.dumps(new_page_payload).encode("utf-8"), headers=headers, method="POST")
        with urllib.request.urlopen(req_create) as create_resp:
            new_page_data = json.loads(create_resp.read().decode("utf-8"))
            new_page_id = new_page_data["id"]
            new_page_url = new_page_data["url"]
            print("\nSUCCESS: BRAND NEW INDICATORS PAGE CREATED!")
            print(f"NEW PAGE ID: {new_page_id}")
            print(f"NEW PAGE URL: {new_page_url}")
            
        # 3. DELETE OLD PAGES THAT WERE NOT THE NEW ONE
        for old_p in old_pages_to_delete:
            if old_p["id"] != new_page_id:
                del_url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/pages/{old_p['id']}"
                req_del = urllib.request.Request(del_url, headers=headers, method="DELETE")
                try:
                    with urllib.request.urlopen(req_del) as del_resp:
                        print(f"DELETED OLD PAGE ID: {old_p['id']} ('{old_p.get('title')}')")
                except Exception as ex:
                    print(f"Error deleting page {old_p['id']}: {ex}")
