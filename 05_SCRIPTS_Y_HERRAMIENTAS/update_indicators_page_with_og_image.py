import os
import json
import urllib.request
import urllib.parse

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
html_path = os.path.join(ind_dir, "08.03_Dashboard_Indicadores_Economicos.html")
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

# 1. READ HTML
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Add hidden image tag at the top of the body for Blogger featuredImage detector
# We can use a reliable Blogger CDN URL or our high-quality horizontal image CDN URL
og_img_cdn_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIG7CrEnww8e0tXKx4-5T0fPI9VuIb-7be3g-Aor7fMkqxQbfp7JvolPod3WFzvozbUrNUjEX-ziAo0Cj3UucGIFBCgCEPglvySv5Jiy6L0zx0QpMPBHJZ9URfttZ5IlcSzotnsgH7yT_MVGefmNcC7tU5rgTr7QC_4zxfaQU_rdt_xQCugVJZCfbcTwu1/s1376/02.03_foto_articulo1_rm245_oficial_horizontal.webp"

hidden_img_html = f"""<!-- IMAGEN DE PREVISUALIZACIÓN DE REDES SOCIALES (WHATSAPP, FACEBOOK, LINKEDIN) -->
<div style="display:none !important; visibility:hidden !important; height:0 !important; width:0 !important; overflow:hidden !important;">
  <img src="{og_img_cdn_url}" alt="Indicadores Económicos de Bolivia | Daniel Simons" width="1200" height="630" />
</div>

"""

if "<!-- IMAGEN DE PREVISUALIZACIÓN DE REDES SOCIALES" not in html_content:
    body_pos = html_content.find("<body>")
    if body_pos != -1:
        insert_p = body_pos + len("<body>")
        html_content = html_content[:insert_p] + "\n" + hidden_img_html + html_content[insert_p:]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("ADDED HIDDEN FEATURED IMAGE TO INDICATORS PAGE HTML!")

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
                    print("INDICATORS PAGE UPDATED LIVE VIA API WITH FEATURED OG IMAGE!")
                    print("URL:", up_data.get("url"))
