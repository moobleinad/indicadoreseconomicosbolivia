import urllib.request
import urllib.parse
import json
import os
import time

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

user_exact_html = '''<div style="font-family: system-ui, -apple-system, sans-serif; background-color: #0d0d0d; color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid rgba(188, 167, 114, 0.3); max-width: 800px; margin: 0 auto;">

  <!-- ENCABEZADO PRINCIPAL -->
  <div style="text-align: center; margin-bottom: 25px; padding-bottom: 15px; border-bottom: 1px solid rgba(188, 167, 114, 0.2);">
    <h1 style="color: #BCA772; font-size: 24px; font-weight: 800; text-transform: uppercase; margin-bottom: 8px;">🇧🇴 INDICADORES ECONÓMICOS DE BOLIVIA</h1>
    <p style="color: #B7BEC9; font-size: 13.5px; margin-bottom: 16px;">Monitoreo ejecutivo de datos clave actualizados al 02 de Agosto de 2026. Fuentes oficiales e independientes.</p>
    <a href="https://whatsapp.com/channel/0029VbDAeCQ1t90gu0qjtC07" target="_blank" style="display: inline-block; background: rgba(37, 211, 102, 0.15); border: 1px solid #25D366; color: #25D366 !important; padding: 10px 20px; border-radius: 25px; font-size: 12.5px; font-weight: 700; text-decoration: none !important;">
      📲 ACTUALIZACIONES DIARIAS: UNIRSE AL CANAL DE WHATSAPP &#10140;
    </a>
  </div>

  <!-- TARJETA 1: DÓLAR PARALELO -->
  <div style="background: #141619; border: 1px solid rgba(188, 167, 114, 0.3); border-radius: 12px; padding: 20px; margin-bottom: 16px; text-align: center;">
    <h3 style="color: #ffffff; font-size: 20px; font-weight: 800; margin-bottom: 4px;">Dólar Paralelo / Mercado Libre</h3>
    <p style="color: #8892B0; font-size: 12.5px; margin-bottom: 12px;">Actualizado al <strong>02 de Agosto de 2026</strong></p>
    
    <div style="display: flex; justify-content: center; gap: 15px; margin: 12px 0;">
      <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(188,167,114,0.3); padding: 8px 16px; border-radius: 8px;">
        <div style="font-size: 11px; color: #8892B0; text-transform: uppercase;">Compra</div>
        <div style="font-size: 16px; font-weight: 700; color: #BCA772;">11.65 Bs</div>
      </div>
      <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(188,167,114,0.3); padding: 8px 16px; border-radius: 8px;">
        <div style="font-size: 11px; color: #8892B0; text-transform: uppercase;">Venta</div>
        <div style="font-size: 16px; font-weight: 700; color: #BCA772;">11.85 Bs</div>
      </div>
    </div>

    <div style="font-size: 42px; font-weight: 900; color: #BCA772; margin: 6px 0;">11.75 Bs</div>
    <div style="font-size: 12.5px; color: #B7BEC9; margin-bottom: 10px;">Promedio P2P / Mercado Libre</div>
    <span style="display: inline-block; background: rgba(40, 167, 69, 0.15); border: 1px solid #2ecc71; color: #2ecc71; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 800; text-transform: uppercase;">● ESTABILIZADO EN MERCADO P2P</span>
    <p style="color: #CBD5E1; font-size: 13px; text-align: left; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.08); line-height: 1.5;">
      El dólar en el mercado libre refleja la cotización real de la divisa estadounidense en plataformas P2P y casas de cambio. Muestra convergencia con el tipo de cambio oficial flexible, estabilizando el costo de reposición no regulado.
    </p>
  </div>

  <!-- TARJETA 2: DÓLAR OFICIAL -->
  <div style="background: #141619; border: 1px solid rgba(188, 167, 114, 0.3); border-radius: 12px; padding: 20px; margin-bottom: 16px; text-align: center;">
    <h3 style="color: #ffffff; font-size: 20px; font-weight: 800; margin-bottom: 4px;">Dólar Oficial (BCB)</h3>
    <p style="color: #8892B0; font-size: 12.5px; margin-bottom: 12px;">Actualizado al <strong>02 de Agosto de 2026</strong></p>
    
    <div style="display: flex; justify-content: center; gap: 15px; margin: 12px 0;">
      <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(188,167,114,0.3); padding: 8px 16px; border-radius: 8px;">
        <div style="font-size: 11px; color: #8892B0; text-transform: uppercase;">Compra</div>
        <div style="font-size: 16px; font-weight: 700; color: #BCA772;">12.07 Bs</div>
      </div>
      <div style="background: rgba(255,255,255,0.04); border: 1px solid rgba(188,167,114,0.3); padding: 8px 16px; border-radius: 8px;">
        <div style="font-size: 11px; color: #8892B0; text-transform: uppercase;">Venta</div>
        <div style="font-size: 16px; font-weight: 700; color: #BCA772;">12.19 Bs</div>
      </div>
    </div>

    <div style="font-size: 42px; font-weight: 900; color: #BCA772; margin: 6px 0;">12.13 Bs</div>
    <div style="font-size: 12.5px; color: #B7BEC9; margin-bottom: 10px;">Tipo de Cambio Oficial Flexible (BCB)</div>
    <span style="display: inline-block; background: rgba(220, 53, 69, 0.15); border: 1px solid #e74c3c; color: #e74c3c; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 800; text-transform: uppercase;">● CRÍTICO / AJUSTE</span>
    <p style="color: #CBD5E1; font-size: 13px; text-align: left; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.08); line-height: 1.5;">
      Cotización oficial del Banco Central de Bolivia bajo el régimen flexible. La transición del régimen fijo (6.96 Bs) a un esquema flexible busca sincerar la paridad monetaria y reordenar la liquidación de divisas en la banca.
    </p>
  </div>

  <!-- TARJETA 3: INFLACIÓN -->
  <div style="background: #141619; border: 1px solid rgba(188, 167, 114, 0.3); border-radius: 12px; padding: 20px; margin-bottom: 16px; text-align: center;">
    <h3 style="color: #ffffff; font-size: 20px; font-weight: 800; margin-bottom: 4px;">Inflación (IPC Acumulado)</h3>
    <p style="color: #8892B0; font-size: 12.5px; margin-bottom: 12px;">A Junio de 2026 (1er Semestre)</p>
    <div style="font-size: 42px; font-weight: 900; color: #BCA772; margin: 6px 0;">4.82%</div>
    <div style="font-size: 12.5px; color: #B7BEC9; margin-bottom: 10px;">Variación Interanual a 12 meses: 9.23% (INE)</div>
    <span style="display: inline-block; background: rgba(220, 53, 69, 0.15); border: 1px solid #e74c3c; color: #e74c3c; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 800; text-transform: uppercase;">● ALTA PRESIÓN DE PRECIOS</span>
    <p style="color: #CBD5E1; font-size: 13px; text-align: left; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.08); line-height: 1.5;">
      El Índice de Precios al Consumidor acumula 4,82% en el primer semestre. El ritmo interanual del 9,23% refleja el encarecimiento de bienes importados e insumos agrícolas por el período de ajuste cambiario.
    </p>
  </div>

  <!-- TARJETA 4: RESERVAS RIN -->
  <div style="background: #141619; border: 1px solid rgba(188, 167, 114, 0.3); border-radius: 12px; padding: 20px; margin-bottom: 16px; text-align: center;">
    <h3 style="color: #ffffff; font-size: 20px; font-weight: 800; margin-bottom: 4px;">Reservas Internacionales (RIN)</h3>
    <p style="color: #8892B0; font-size: 12.5px; margin-bottom: 12px;">Al 30 de Junio de 2026</p>
    <div style="font-size: 42px; font-weight: 900; color: #BCA772; margin: 6px 0;">$3.617,3 MM</div>
    <div style="font-size: 12.5px; color: #B7BEC9; margin-bottom: 10px;">Oro Físico: $2.882,9M | Divisas Líquidas: $666,1M</div>
    <span style="display: inline-block; background: rgba(255, 193, 7, 0.15); border: 1px solid #f1c40f; color: #f1c40f; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 800; text-transform: uppercase;">● PRECAUCIÓN / MONITOREO</span>
    <p style="color: #CBD5E1; font-size: 13px; text-align: left; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.08); line-height: 1.5;">
      El saldo de reservas se sostiene prioritariamente en el valor del oro físico ($2.882,9M en 22.3 toneladas). La liquidez operativa en divisas ($666,1M) permanece bajo monitoreo constante.
    </p>
  </div>

  <!-- TARJETA 5: BALANZA COMERCIAL -->
  <div style="background: #141619; border: 1px solid rgba(188, 167, 114, 0.3); border-radius: 12px; padding: 20px; margin-bottom: 16px; text-align: center;">
    <h3 style="color: #ffffff; font-size: 20px; font-weight: 800; margin-bottom: 4px;">Balanza Comercial</h3>
    <p style="color: #8892B0; font-size: 12.5px; margin-bottom: 12px;">1er Semestre de 2026</p>
    <div style="font-size: 42px; font-weight: 900; color: #BCA772; margin: 6px 0;">+$1.669 MM</div>
    <div style="font-size: 12.5px; color: #B7BEC9; margin-bottom: 10px;">Superávit Comercial Acumulado</div>
    <span style="display: inline-block; background: rgba(40, 167, 69, 0.15); border: 1px solid #2ecc71; color: #2ecc71; padding: 4px 14px; border-radius: 20px; font-size: 11px; font-weight: 800; text-transform: uppercase;">● SUPERÁVIT RELEVANTE</span>
    <p style="color: #CBD5E1; font-size: 13px; text-align: left; margin-top: 14px; padding-top: 12px; border-top: 1px solid rgba(255,255,255,0.08); line-height: 1.5;">
      Superávit impulsado por el repunte de exportaciones no tradicionales (soya, minería, carne) y la moderación de importaciones de combustibles bajo los nuevos incentivos de producción.
    </p>
  </div>

  <!-- AFICHE OFICIAL DE COMPARTIR -->
  <div style="text-align: center; margin-top: 30px; padding: 20px; background: #141619; border: 1px solid rgba(188,167,114,0.3); border-radius: 12px;">
    <p style="color: #BCA772; font-weight: 700; font-size: 13px; margin-bottom: 12px;">PUBLICACIÓN OFICIAL PARA REDES SOCIALES</p>
    <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp" alt="Indicadores Económicos de Bolivia" width="600" style="max-width:100%; border-radius:8px;" />
  </div>

</div>'''

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
                        "content": user_exact_html
                    }
                    req_up = urllib.request.Request(update_page_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="PUT")
                    with urllib.request.urlopen(req_up) as up_resp:
                        up_data = json.loads(up_resp.read().decode("utf-8"))
                        print(f"SUCCESS: PUSHED EXACT USER HTML TO PAGE ID {page_id}! URL: {up_data.get('url')}")
