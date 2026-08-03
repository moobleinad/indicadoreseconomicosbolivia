import os
import json
import re
import urllib.request
import urllib.parse

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
html_path = os.path.join(ind_dir, "08.03_Dashboard_Indicadores_Economicos.html")
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

# 1. READ HTML AND REMOVE HIDDEN IMAGE TAG
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Remove hidden image tag block
html_content = re.sub(r'<!-- IMAGEN DE PREVISUALIZACIÓN DE REDES SOCIALES.*?</div>', '', html_content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("REMOVED HIDDEN IMAGE TAG FROM INDICATORS DASHBOARD HTML!")

# 2. REFRESH TOKEN AND UPDATE LIVE ON BLOGGER API
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
        
        pages_url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/pages"
        req_pages = urllib.request.Request(pages_url, headers=headers)
        with urllib.request.urlopen(req_pages) as p_resp:
            pages_data = json.loads(p_resp.read().decode("utf-8"))
            
            target_page = None
            for p in pages_data.get("items", []):
                if "indicadores" in p.get("title", "").lower() or "indicadores" in p.get("url", "").lower():
                    target_page = p
                    break
                    
            if target_page:
                page_id = target_page["id"]
                update_page_url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/pages/{page_id}"
                page_payload = {
                    "kind": "blogger#page",
                    "id": page_id,
                    "title": "INDICADORES ECONÓMICOS DE BOLIVIA",
                    "content": html_content
                }
                req_up = urllib.request.Request(update_page_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="PUT")
                with urllib.request.urlopen(req_up) as up_resp:
                    up_data = json.loads(up_resp.read().decode("utf-8"))
                    print("REMOVED HIDDEN IMAGE FROM LIVE BLOGGER PAGE SUCCESSFULLY!")
                    print("URL:", up_data.get("url"))
