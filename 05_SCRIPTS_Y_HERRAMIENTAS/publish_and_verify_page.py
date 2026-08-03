import urllib.request
import urllib.parse
import json
import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
html_path = os.path.join(ind_dir, "08.03_Dashboard_Indicadores_Economicos.html")
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

cdn_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp"

clean_content = f'''
<div style="font-family: sans-serif; background: #0d0d0d; color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #BCA772;">
  <h2 style="color: #BCA772; text-align: center;">INDICADORES ECONÓMICOS DE BOLIVIA</h2>
  <p style="text-align: center; color: #B7BEC9;">Monitoreo ejecutivo de datos clave actualizados al 02 de Agosto de 2026.</p>
  
  <div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #2ecc71;">
    <h3 style="margin: 0; color: #ffffff;">💵 Dólar Paralelo / Mercado Libre</h3>
    <p style="font-size: 24px; font-weight: bold; color: #BCA772; margin: 5px 0;">11.75 Bs (Compra: 11.65 | Venta: 11.85)</p>
    <p style="font-size: 13px; color: #2ecc71; margin: 0;">● ESTABILIZADO EN MERCADO P2P</p>
  </div>

  <div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #e74c3c;">
    <h3 style="margin: 0; color: #ffffff;">🏦 Dólar Oficial Flexible (BCB)</h3>
    <p style="font-size: 24px; font-weight: bold; color: #BCA772; margin: 5px 0;">12.13 Bs (Compra: 12.07 | Venta: 12.19)</p>
    <p style="font-size: 13px; color: #e74c3c; margin: 0;">● AJUSTE REGIMEN FLEXIBLE</p>
  </div>

  <div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #e74c3c;">
    <h3 style="margin: 0; color: #ffffff;">📊 Inflación Acumulada (IPC 1S)</h3>
    <p style="font-size: 24px; font-weight: bold; color: #BCA772; margin: 5px 0;">4.82% (Interanual: 9.23%)</p>
    <p style="font-size: 13px; color: #e74c3c; margin: 0;">● PRESIÓN DE PRECIOS</p>
  </div>

  <div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #f1c40f;">
    <h3 style="margin: 0; color: #ffffff;">🏛️ Reservas Internacionales (RIN)</h3>
    <p style="font-size: 24px; font-weight: bold; color: #BCA772; margin: 5px 0;">$3.617,3 MM USD</p>
    <p style="font-size: 13px; color: #f1c40f; margin: 0;">● ORO: $2.882,9M | DIVISAS: $666,1M</p>
  </div>

  <div style="background: #1a1a1a; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #2ecc71;">
    <h3 style="margin: 0; color: #ffffff;">📈 Balanza Comercial</h3>
    <p style="font-size: 24px; font-weight: bold; color: #BCA772; margin: 5px 0;">+$1.669 MM USD</p>
    <p style="font-size: 13px; color: #2ecc71; margin: 0;">● SUPERÁVIT ACUMULADO</p>
  </div>

  <div style="text-align: center; margin-top: 25px;">
    <img src="{cdn_url}" alt="Indicadores Económicos de Bolivia" width="600" style="max-width:100%; border-radius:8px;" />
  </div>
</div>
'''

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
                        "title": "INDICADORES ECONÓMICOS DE BOLIVIA",
                        "content": clean_content
                    }
                    req_up = urllib.request.Request(update_page_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="PUT")
                    with urllib.request.urlopen(req_up) as up_resp:
                        up_data = json.loads(up_resp.read().decode("utf-8"))
                        print(f"SUCCESSFULLY PUBLISHED LIVE PAGE ID {page_id}! URL: {up_data.get('url')}")
