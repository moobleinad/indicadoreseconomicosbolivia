import os
import json
import urllib.request
import urllib.parse

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

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
    
    req_blogs = urllib.request.Request("https://www.googleapis.com/blogger/v3/users/self/blogs", headers=headers)
    with urllib.request.urlopen(req_blogs) as b_resp:
        blogs_data = json.loads(b_resp.read().decode("utf-8"))
        blog_id = blogs_data["items"][0]["id"]
        
        # Post 2
        post_id2 = "7665728535146504116"
        url_p2 = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/{post_id2}"
        
        req_p2 = urllib.request.Request(url_p2, headers=headers)
        with urllib.request.urlopen(req_p2) as get_resp:
            p2_data = json.loads(get_resp.read().decode("utf-8"))
            
            p2_data["customMetaData"] = "Serie Política Monetaria y Sociedad | Parte 2. Análisis de la flotación libre abrupta frente al modelo de deslizamiento progresivo (crawling peg)."
            
            req_put = urllib.request.Request(url_p2, data=json.dumps(p2_data).encode("utf-8"), headers=headers, method="PUT")
            with urllib.request.urlopen(req_put) as put_resp:
                print("SET SEARCH DESCRIPTION FOR ARTICLE 2 IN BLOGGER CORE!")
