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

cdn_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp"

# Read local HTML
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Remove any hidden image div if present
import re
html_content = re.sub(r'<div[^>]*ds-og-hidden-image[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)

# Add a BEAUTIFUL VISIBLE AFICHE BANNER at the bottom of the dashboard HTML
visible_banner_html = f'''
<!-- AFICHE OFICIAL DE PREVISUALIZACIÓN Y COMPARTIR -->
<div style="max-width: 860px; margin: 40px auto 20px auto; text-align: center; background: #0D0F12; padding: 25px; border-radius: 12px; border: 1px solid #1E222A; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
  <p style="color: #BCA772; font-size: 14px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; margin-bottom: 15px;">PUBLICACIÓN OFICIAL PARA REDES SOCIALES</p>
  <div class="separator" style="clear: both; text-align: center;">
    <a href="{cdn_url}" target="_blank" style="display: block; margin: 0 auto;">
      <img border="0" data-original-height="1024" data-original-width="1024" src="{cdn_url}" width="600" style="max-width: 100%; height: auto; border-radius: 8px; border: 1px solid #2A2E39;" alt="Indicadores Económicos de Bolivia" />
    </a>
  </div>
  <p style="color: #94A3B8; font-size: 13.5px; margin-top: 15px; font-style: italic;">Sigue la cotización del tipo de cambio y otros indicadores económicos actualizados a diario.</p>
</div>
'''

if "09.02_afiche_indicadores_economicos_cuadrado.webp" not in html_content:
    html_content += visible_banner_html

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML UPDATED WITH BEAUTIFUL VISIBLE BANNER!")

# Now push live via Blogger API
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
            
            for p in pages_data.get("items", []):
                if "indicadores" in p.get("title", "").lower() or "indicadores" in p.get("url", "").lower():
                    page_id = p["id"]
                    update_page_url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/pages/{page_id}"
                    page_payload = {
                        "kind": "blogger#page",
                        "id": page_id,
                        "title": p.get("title"),
                        "content": html_content
                    }
                    
                    for attempt in range(3):
                        try:
                            req_up = urllib.request.Request(update_page_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="PUT")
                            with urllib.request.urlopen(req_up) as up_resp:
                                up_data = json.loads(up_resp.read().decode("utf-8"))
                                print(f"SUCCESS: VISIBLE BANNER IS NOW LIVE ON '{p.get('title')}'! URL: {up_data.get('url')}")
                                break
                        except Exception as ex:
                            time.sleep(2)
