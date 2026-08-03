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

# Clean, Pure Static HTML Dashboard (Zero JS dependency, instant 100% rendering on all devices)
prerendered_html = f'''
<style>
  .econ-dashboard {{
    max-width: 800px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    color: #ffffff;
  }}
  .dashboard-header {{
    background: #0d0d0d;
    border: 1px solid rgba(188, 167, 114, 0.3);
    border-radius: 12px;
    padding: 24px 20px;
    text-align: center;
    margin-bottom: 20px;
  }}
  .dashboard-title {{
    font-size: 24px;
    font-weight: 800;
    color: #BCA772;
    margin-bottom: 8px;
    text-transform: uppercase;
  }}
  .dashboard-subtitle {{
    font-size: 13.5px;
    color: #B7BEC9;
    margin-bottom: 16px;
  }}
  .wa-btn {{
    display: inline-block;
    background: rgba(37, 211, 102, 0.15);
    border: 1px solid #25D366;
    color: #25D366 !important;
    padding: 10px 20px;
    border-radius: 25px;
    font-size: 13px;
    font-weight: 700;
    text-decoration: none !important;
  }}
  .indicator-card {{
    background: #0d0d0d;
    border: 1px solid rgba(188, 167, 114, 0.25);
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 16px;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.6);
  }}
  .indicator-title {{
    font-size: 20px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 4px;
  }}
  .indicator-date {{
    font-size: 12.5px;
    color: #8892B0;
    margin-bottom: 12px;
  }}
  .indicator-hero {{
    font-size: 44px;
    font-weight: 900;
    color: #BCA772;
    margin: 8px 0;
    line-height: 1.1;
  }}
  .indicator-unit {{
    font-size: 13px;
    color: #B7BEC9;
    margin-bottom: 12px;
  }}
  .badge-verde {{
    display: inline-block;
    background: rgba(40, 167, 69, 0.15);
    border: 1px solid #2ecc71;
    color: #2ecc71;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
  }}
  .badge-rojo {{
    display: inline-block;
    background: rgba(220, 53, 69, 0.15);
    border: 1px solid #e74c3c;
    color: #e74c3c;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
  }}
  .badge-amarillo {{
    display: inline-block;
    background: rgba(255, 193, 7, 0.15);
    border: 1px solid #f1c40f;
    color: #f1c40f;
    padding: 5px 14px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
  }}
  .indicator-desc {{
    font-size: 13.5px;
    color: #CBD5E1;
    text-align: left;
    margin-top: 14px;
    padding-top: 14px;
    border-top: 1px solid rgba(255,255,255,0.08);
    line-height: 1.6;
  }}
  .rates-box {{
    display: flex;
    justify-content: center;
    gap: 15px;
    margin: 12px 0;
  }}
  .rate-pill {{
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(188,167,114,0.3);
    padding: 8px 16px;
    border-radius: 8px;
  }}
  .rate-label {{ font-size: 11px; color: #8892B0; text-transform: uppercase; }}
  .rate-val {{ font-size: 16px; font-weight: 700; color: #BCA772; }}
</style>

<div class="econ-dashboard">

  <div class="dashboard-header">
    <h1 class="dashboard-title">🇧🇴 INDICADORES ECONÓMICOS DE BOLIVIA</h1>
    <p class="dashboard-subtitle">Monitoreo macroeconómico transparente y actualizado. Datos oficiales e independientes.</p>
    <a href="https://whatsapp.com/channel/0029VbDAeCQ1t90gu0qjtC07" target="_blank" class="wa-btn">
      📲 UNIRSE AL CANAL DE WHATSAPP &#10140;
    </a>
  </div>

  <!-- TARJETA 1: DÓLAR PARALELO -->
  <div class="indicator-card">
    <div class="indicator-title">Dólar Paralelo / Mercado Libre</div>
    <div class="indicator-date">Actualizado al <strong>02 de Agosto de 2026</strong></div>
    
    <div class="rates-box">
      <div class="rate-pill">
        <div class="rate-label">Compra</div>
        <div class="rate-val">11.65 Bs</div>
      </div>
      <div class="rate-pill">
        <div class="rate-label">Venta</div>
        <div class="rate-val">11.85 Bs</div>
      </div>
    </div>

    <div class="indicator-hero">11.75 Bs</div>
    <div class="indicator-unit">Promedio P2P / Mercado Libre</div>
    <span class="badge-verde">● ESTABILIZADO</span>
    <div class="indicator-desc">
      El dólar en el mercado libre refleja la cotización real de la divisa estadounidense en plataformas P2P y casas de cambio. Muestra convergencia con el tipo de cambio oficial flexible, estabilizando el costo de reposición no regulado.
    </div>
  </div>

  <!-- TARJETA 2: DÓLAR OFICIAL -->
  <div class="indicator-card">
    <div class="indicator-title">Dólar Oficial (BCB)</div>
    <div class="indicator-date">Actualizado al <strong>02 de Agosto de 2026</strong></div>
    
    <div class="rates-box">
      <div class="rate-pill">
        <div class="rate-label">Compra</div>
        <div class="rate-val">12.07 Bs</div>
      </div>
      <div class="rate-pill">
        <div class="rate-label">Venta</div>
        <div class="rate-val">12.19 Bs</div>
      </div>
    </div>

    <div class="indicator-hero">12.13 Bs</div>
    <div class="indicator-unit">Tipo de Cambio Oficial Flexible (BCB)</div>
    <span class="badge-rojo">● CRÍTICO / AJUSTE</span>
    <div class="indicator-desc">
      Cotización oficial del Banco Central de Bolivia bajo el régimen flexible. La transición del régimen fijo (6.96 Bs) a un esquema flexible busca sincerar la paridad monetaria y reordenar la liquidación de divisas en la banca.
    </div>
  </div>

  <!-- TARJETA 3: INFLACIÓN -->
  <div class="indicator-card">
    <div class="indicator-title">Inflación (IPC Acumulado)</div>
    <div class="indicator-date">A Junio de 2026 (1er Semestre)</div>
    <div class="indicator-hero">4.82%</div>
    <div class="indicator-unit">Variación Interanual: 9.23% (INE)</div>
    <span class="badge-rojo">● ALTA PRESIÓN</span>
    <div class="indicator-desc">
      El Índice de Precios al Consumidor acumula 4,82% en el primer semestre. El ritmo interanual del 9,23% refleja el encarecimiento de bienes importados e insumos agrícolas por el período de ajuste cambiario.
    </div>
  </div>

  <!-- TARJETA 4: RESERVAS RIN -->
  <div class="indicator-card">
    <div class="indicator-title">Reservas Internacionales (RIN)</div>
    <div class="indicator-date">Al 30 de Junio de 2026</div>
    <div class="indicator-hero">$3.617,3 MM</div>
    <div class="indicator-unit">Oro: $2.882,9M | Divisas Líquidas: $666,1M</div>
    <span class="badge-amarillo">● PRECAUCIÓN / MONITOREO</span>
    <div class="indicator-desc">
      El saldo de reservas se sostiene prioritariamente en el valor del oro físico ($2.882,9M en 22.3 toneladas). La liquidez operativa en divisas ($666,1M) permanece bajo monitoreo constante.
    </div>
  </div>

  <!-- TARJETA 5: BALANZA COMERCIAL -->
  <div class="indicator-card">
    <div class="indicator-title">Balanza Comercial</div>
    <div class="indicator-date">1er Semestre de 2026</div>
    <div class="indicator-hero">+$1.669 MM</div>
    <div class="indicator-unit">Superávit Comercial Acumulado</div>
    <span class="badge-verde">● SUPERÁVIT RELEVANTE</span>
    <div class="indicator-desc">
      Superávit impulsado por el repunte de exportaciones no tradicionales (soya, minería, carne) y la moderación de importaciones de combustibles bajo los nuevos incentivos de producción.
    </div>
  </div>

  <!-- AFICHE OFICIAL DE PREVISUALIZACIÓN -->
  <div style="text-align: center; margin-top: 30px; padding: 20px; background: #0d0d0d; border: 1px solid rgba(188,167,114,0.3); border-radius: 12px;">
    <p style="color: #BCA772; font-weight: 700; font-size: 13px; margin-bottom: 12px;">PUBLICACIÓN OFICIAL PARA REDES SOCIALES</p>
    <img src="{cdn_url}" alt="Indicadores Económicos de Bolivia" width="600" style="max-width:100%; height:auto; border-radius:8px;" />
  </div>

</div>
'''

# Update live page via Blogger API
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
                        "content": prerendered_html
                    }
                    
                    for attempt in range(3):
                        try:
                            req_up = urllib.request.Request(update_page_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="PUT")
                            with urllib.request.urlopen(req_up) as up_resp:
                                up_data = json.loads(up_resp.read().decode("utf-8"))
                                print(f"SUCCESS: PUSHED PURE STATIC HTML DASHBOARD TO '{p.get('title')}'! URL: {up_data.get('url')}")
                                break
                        except Exception as ex:
                            time.sleep(2)
