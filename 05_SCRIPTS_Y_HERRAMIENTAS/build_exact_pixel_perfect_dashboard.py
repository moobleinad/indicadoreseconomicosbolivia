import os
import json
import urllib.request
import urllib.parse

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
json_path = os.path.join(ind_dir, "08.02_Datos_Indicadores_Bolivia.json")
html_path = os.path.join(ind_dir, "08.03_Dashboard_Indicadores_Economicos.html")
copy_paste_path = os.path.join(ind_dir, "08.05_INDICADORES_PARA_COPIAR_Y_PEGAR_EN_BLOGGER.html")
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

cdn_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp"
wa_link = "https://whatsapp.com/channel/0029VbDAeCQ1t90gu0qjtC07"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

indicadores = data.get("indicadores", [])

def get_sem_style(sem):
    sem = sem.lower()
    if sem == "verde":
        return "border: 1px solid #2ecc71; color: #2ecc71; background: rgba(40,167,69,0.12);"
    elif sem == "amarillo":
        return "border: 1px solid #f1c40f; color: #f1c40f; background: rgba(255,193,7,0.12);"
    else:
        return "border: 1px solid #e74c3c; color: #e74c3c; background: rgba(220,53,69,0.12);"

def get_dot(sem):
    sem = sem.lower()
    if sem == "verde": return "🟢"
    elif sem == "amarillo": return "🟡"
    else: return "🔴"

# Build EXACT 1:1 Pixel Perfect Dashboard Matching User Screenshots
html_content = '''<style>
  .ds-main-container {
    max-width: 820px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #ffffff;
    background-color: #000000;
    padding: 10px;
  }
  
  /* HEADER BANNER */
  .ds-top-banner {
    background: #0a0b0c;
    border: 1px solid rgba(188, 167, 114, 0.3);
    border-radius: 16px;
    padding: 24px 20px;
    text-align: center;
    margin-bottom: 24px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.8);
  }
  .ds-top-title {
    color: #BCA772;
    font-size: 24px;
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
  }
  .ds-top-sub {
    color: #B7BEC9;
    font-size: 13.5px;
    margin-bottom: 18px;
  }
  .ds-top-wa-btn {
    display: inline-block;
    background: rgba(37, 211, 102, 0.12);
    border: 1px solid #25D366;
    color: #25D366 !important;
    padding: 10px 22px;
    border-radius: 25px;
    font-size: 12.5px;
    font-weight: 700;
    text-decoration: none !important;
    text-transform: uppercase;
    letter-spacing: 0.4px;
  }

  /* CARD STRUCTURE EXACT LIKE SCREENSHOT 1 */
  .ds-card {
    background: #0b0c0d;
    border: 1px solid rgba(188, 167, 114, 0.25);
    border-radius: 16px;
    padding: 24px 24px 0 24px;
    margin-bottom: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.6);
    overflow: hidden;
  }
  .ds-card-header-title {
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 4px;
  }
  .ds-card-header-title .ds-arrow {
    color: #BCA772;
    font-size: 16px;
    margin-left: 4px;
  }
  .ds-card-period {
    font-size: 13px;
    color: #8892B0;
    margin-bottom: 16px;
  }
  .ds-card-period strong {
    color: #BCA772;
  }
  .ds-hero-number {
    font-size: 48px;
    font-weight: 900;
    color: #ffffff;
    text-align: center;
    margin: 12px 0 4px 0;
    line-height: 1.1;
    letter-spacing: -0.5px;
  }
  .ds-hero-subtext {
    font-size: 13.5px;
    color: #8892B0;
    text-align: center;
    margin-bottom: 10px;
  }
  .ds-source-text {
    font-size: 13px;
    color: #8892B0;
    text-align: center;
    margin-bottom: 14px;
  }
  .ds-source-text strong {
    color: #BCA772;
  }
  .ds-updated-pill-wrap {
    text-align: center;
    margin-bottom: 20px;
  }
  .ds-updated-pill {
    display: inline-block;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    padding: 6px 16px;
    border-radius: 6px;
    font-size: 12px;
    color: #8892B0;
  }
  .ds-updated-pill strong {
    color: #ffffff;
  }

  /* RATES BOX FOR DOLLAR CARDS */
  .ds-compra-venta-flex {
    display: flex;
    justify-content: center;
    gap: 16px;
    margin: 12px 0;
  }
  .ds-cv-box {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(188, 167, 114, 0.3);
    padding: 8px 20px;
    border-radius: 8px;
    text-align: center;
    min-width: 110px;
  }
  .ds-cv-label {
    font-size: 11px;
    color: #8892B0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .ds-cv-val {
    font-size: 17px;
    font-weight: 800;
    color: #BCA772;
    margin-top: 2px;
  }

  /* BOTTOM BUTTON STRIP EXACT LIKE SCREENSHOT 1 */
  .ds-bottom-strip {
    background: #111215;
    margin: 20px -24px 0 -24px;
    padding: 14px 20px;
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
  }
  
  /* SUMMARY ACCORDION TRIGGER BUTTONS */
  summary.ds-strip-btn {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    user-select: none;
    list-style: none;
    transition: all 0.2s ease;
  }
  summary.ds-strip-btn::-webkit-details-marker { display: none; }
  
  .ds-btn-grey {
    background: #1e2025;
    border: 1px solid rgba(255, 255, 255, 0.12);
    color: #ffffff !important;
  }
  .ds-btn-grey:hover {
    border-color: #BCA772;
    background: #252830;
  }

  /* INNER TABS ROW INSIDE ACCORDION (SCREENSHOT 2 & 3) */
  .ds-panel-body {
    background: #121417;
    border: 1px solid rgba(188, 167, 114, 0.25);
    border-radius: 12px;
    padding: 20px;
    margin: 14px 0 20px 0;
  }
  .ds-inner-tabs-row {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 18px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    padding-bottom: 14px;
  }
  .ds-tab-pill {
    background: #1a1c22;
    border: 1px solid rgba(188, 167, 114, 0.3);
    color: #CBD5E1;
    padding: 7px 15px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    user-select: none;
    list-style: none;
  }
  .ds-tab-pill::-webkit-details-marker { display: none; }
  .ds-tab-pill:hover {
    border-color: #BCA772;
    color: #ffffff;
  }
  .ds-tab-heading {
    color: #BCA772;
    font-size: 13.5px;
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
  }

  /* EVALUATION BOXES (SCREENSHOT 2) */
  .ds-eval-box {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(188, 167, 114, 0.3);
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 14px;
    font-size: 13px;
    color: #CBD5E1;
    line-height: 1.6;
  }
  .ds-params-box {
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 14px 18px;
    font-size: 12.5px;
    color: #CBD5E1;
  }
  .ds-params-title {
    color: #BCA772;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
  }

  /* INTER-CARD REFLECTION BANNER (EXACT SCREENSHOT MATCH) */
  .ds-reflection-banner {
    background: #090a0b;
    border: 1px solid rgba(188, 167, 114, 0.25);
    border-radius: 10px;
    padding: 14px 20px;
    margin: 16px 0 24px 0;
    text-align: center;
    font-size: 13px;
    color: #CBD5E1;
    line-height: 1.5;
  }
  .ds-reflection-title {
    color: #BCA772;
    font-weight: 800;
  }
  .ds-reflection-link {
    color: #BCA772 !important;
    font-weight: 800;
    text-decoration: none !important;
    margin-left: 4px;
  }
  .ds-reflection-link:hover {
    text-decoration: underline !important;
  }
</style>

<div class="ds-main-container">

  <!-- BANNER ENCABEZADO -->
  <div class="ds-top-banner">
    <h1 class="ds-top-title">🇧🇴 INDICADORES ECONÓMICOS DE BOLIVIA</h1>
    <p class="ds-top-sub">Monitoreo ejecutivo de datos clave actualizados al 02 de Agosto de 2026. Fuentes oficiales e independientes.</p>
    <a href="''' + wa_link + '''" target="_blank" class="ds-top-wa-btn">
      📲 ACTUALIZACIONES DIARIAS: UNIRSE AL CANAL DE WHATSAPP &#10140;
    </a>
  </div>
'''

for idx, ind in enumerate(indicadores, 1):
    sem = ind.get("semaforo", "rojo")
    sem_style = get_sem_style(sem)
    dot = get_dot(sem)
    
    compra_venta = ""
    if "detalles_historicos" in ind and isinstance(ind["detalles_historicos"], dict) and "compra" in ind["detalles_historicos"]:
        compra_venta = f'''
        <div class="ds-compra-venta-flex">
          <div class="ds-cv-box">
            <div class="ds-cv-label">Compra</div>
            <div class="ds-cv-val">{ind["detalles_historicos"]["compra"]} Bs</div>
          </div>
          <div class="ds-cv-box">
            <div class="ds-cv-label">Venta</div>
            <div class="ds-cv-val">{ind["detalles_historicos"]["venta"]} Bs</div>
          </div>
        </div>
        '''

    params_html = ""
    if "criterio_evaluacion" in ind:
        crit = ind["criterio_evaluacion"]
        params_html = f'''
        <div class="ds-params-box">
          <div class="ds-params-title">📐 PARÁMETROS TÉCNICOS DE EVALUACIÓN MACROECONÓMICA</div>
          <div>🟢 <strong>Verde:</strong> {crit.get("verde", "")}</div>
          <div style="margin: 4px 0;">🟡 <strong>Amarillo:</strong> {crit.get("amarillo", "")}</div>
          <div>🔴 <strong>Rojo:</strong> {crit.get("rojo", "")}</div>
        </div>
        '''

    html_content += f'''
  <!-- TARJETA {idx}: {ind.get("nombre")} -->
  <div class="ds-card">
    <div class="ds-card-header-title">{ind.get("nombre")} <span class="ds-arrow">▾</span></div>
    <div class="ds-card-period">• Período: <strong>{ind.get("periodo")}</strong></div>

    {compra_venta}

    <div class="ds-hero-number">{ind.get("valor")}</div>
    <div class="ds-hero-subtext">{ind.get("unidad")}</div>
    <div class="ds-source-text">Fuente: <strong>{ind.get("fuente")}</strong></div>
    <div class="ds-updated-pill-wrap">
      <span class="ds-updated-pill">Actualizado al día: <strong>{ind.get("fecha_actualizacion")}</strong></span>
    </div>

    <!-- BOTONERA INFERIOR (FRANJA OSCURA - IGUAL A SCREENSHOT 1) -->
    <div class="ds-bottom-strip">
      
      <!-- BOTÓN 1: SEMÁFORO ESTADO -->
      <details>
        <summary class="ds-strip-btn" style="{sem_style}">
          {dot} {ind.get("semaforo_label")}
        </summary>
        <div class="ds-panel-body">
          <div class="ds-tab-heading">EVALUACIÓN TÉCNICA DEL ESTADO ACTUAL</div>
          <div class="ds-eval-box">
            {ind.get("evaluacion_corta")}
          </div>
          {params_html}
        </div>
      </details>

      <!-- BOTÓN 2: ¿QUÉ ES? -->
      <details>
        <summary class="ds-strip-btn ds-btn-grey">
          ¿Qué es? &#10140;
        </summary>
        <div class="ds-panel-body">
          <div class="ds-tab-heading">📖 ¿QUÉ ES ESTE INDICADOR?</div>
          <div style="font-size: 13.5px; color: #CBD5E1; line-height: 1.6;">
            {ind.get("que_es")}
          </div>
        </div>
      </details>

      <!-- BOTÓN 3: ANÁLISIS -->
      <details>
        <summary class="ds-strip-btn ds-btn-grey">
          Análisis &#10140;
        </summary>
        <div class="ds-panel-body">
          <div class="ds-tab-heading">💡 ANÁLISIS COYUNTURAL DE CAUSA-EFECTO</div>
          <div style="font-size: 13.5px; color: #CBD5E1; line-height: 1.6;">
            {ind.get("analisis")}
          </div>
        </div>
      </details>

    </div>
  </div>

  <!-- BANNER DE REFLEXIÓN INTER-TARJETA (EXACTO A TUS CAPTURAS) -->
  <div class="ds-reflection-banner">
    💡 <span class="ds-reflection-title">Reflexión para tu empresa:</span> "{ind.get("pregunta_estrategica")}"
    <a href="{wa_link}" target="_blank" class="ds-reflection-link">Consultar a Daniel Simons &#10140;</a>
  </div>
'''

html_content += f'''
  <!-- AFICHE OFICIAL DE PREVISUALIZACIÓN Y COMPARTIR -->
  <div style="text-align: center; margin-top: 35px; padding: 24px; background: #0b0c0d; border: 1px solid rgba(188, 167, 114, 0.35); border-radius: 16px;">
    <div style="color: #BCA772; font-weight: 800; font-size: 13.5px; margin-bottom: 16px; text-transform: uppercase;">PUBLICACIÓN OFICIAL PARA REDES SOCIALES</div>
    <a href="{cdn_url}" target="_blank">
      <img src="{cdn_url}" alt="Indicadores Económicos de Bolivia" width="600" style="max-width:100%; height:auto; border-radius:10px; border:1px solid #1E222A;" />
    </a>
  </div>

</div>
'''

# Overwrite local files
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(copy_paste_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("SUCCESSFULLY GENERATED 1:1 PIXEL-PERFECT HTML MATCHING USER SCREENSHOTS!")

# Push live via Blogger API
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
                        "content": html_content
                    }
                    req_up = urllib.request.Request(update_page_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="PUT")
                    with urllib.request.urlopen(req_up) as up_resp:
                        up_data = json.loads(up_resp.read().decode("utf-8"))
                        print(f"SUCCESSFULLY PUSHED 1:1 PIXEL-PERFECT DASHBOARD TO BLOGGER API! URL: {up_data.get('url')}")
