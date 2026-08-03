import os
import json
import urllib.request
import urllib.parse

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")
html_path = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS", "08.03_Dashboard_Indicadores_Economicos.html")

with open(token_path, "r", encoding="utf-8") as f:
    token_data = json.load(f)

with open(secret_path, "r", encoding="utf-8") as f:
    secret_data = json.load(f)

client_info = secret_data.get("installed") or secret_data.get("web") or {}
client_id = client_info.get("client_id")
client_secret = client_info.get("client_secret")
refresh_token = token_data.get("refresh_token")

# Refresh token
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
    
    # Get blog ID
    req_blogs = urllib.request.Request("https://www.googleapis.com/blogger/v3/users/self/blogs", headers=headers)
    with urllib.request.urlopen(req_blogs) as b_resp:
        blogs_data = json.loads(b_resp.read().decode("utf-8"))
        blog_id = blogs_data["items"][0]["id"]
        
        # Read updated HTML content
        with open(html_path, "r", encoding="utf-8") as hf:
            dashboard_html = hf.read()
            
        # Get list of pages
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
                    "content": dashboard_html
                }
                req_up = urllib.request.Request(update_page_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="PUT")
                with urllib.request.urlopen(req_up) as up_resp:
                    up_data = json.loads(up_resp.read().decode("utf-8"))
                    print("PAGE UPDATED LIVE SUCCESSFULLY VIA BLOGGER API!")
                    print("PAGE URL:", up_data.get("url"))
            else:
                print("TARGET PAGE NOT FOUND, CREATING NEW PAGE...")
                page_payload = {
                    "kind": "blogger#page",
                    "title": "INDICADORES ECONÓMICOS DE BOLIVIA",
                    "content": dashboard_html
                }
                req_new = urllib.request.Request(pages_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="POST")
                with urllib.request.urlopen(req_new) as new_resp:
                    new_data = json.loads(new_resp.read().decode("utf-8"))
                    print("NEW PAGE CREATED SUCCESSFULLY VIA BLOGGER API!")
                    print("PAGE URL:", new_data.get("url"))
