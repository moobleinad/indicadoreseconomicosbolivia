import os
import json

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
json_path = os.path.join(ind_dir, "08.02_Datos_Indicadores_Bolivia.json")
html_path = os.path.join(ind_dir, "08.03_Dashboard_Indicadores_Economicos.html")
copy_paste_path = os.path.join(ind_dir, "08.05_INDICADORES_PARA_COPIAR_Y_PEGAR_EN_BLOGGER.html")
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

cdn_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

indicadores = data.get("indicadores", [])

def get_badge_class(sem):
    sem = sem.lower()
    if sem == "verde":
        return "background: rgba(40, 167, 69, 0.15); border: 1px solid #2ecc71; color: #2ecc71;"
    elif sem == "amarillo":
        return "background: rgba(255, 193, 7, 0.15); border: 1px solid #f1c40f; color: #f1c40f;"
    else:
        return "background: rgba(220, 53, 69, 0.15); border: 1px solid #e74c3c; color: #e74c3c;"

html_out = '''<style>
  .ds-dash-wrap {
    max-width: 820px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    color: #ffffff;
    background: #000000;
    padding: 10px;
  }
  .ds-header {
    background: #0d0d0d;
    border: 1px solid rgba(188, 167, 114, 0.35);
    border-radius: 14px;
    padding: 24px 20px;
    text-align: center;
    margin-bottom: 24px;
  }
  .ds-card-box {
    background: #0d0d0d;
    border: 1px solid rgba(188, 167, 114, 0.3);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 24px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.7);
  }
  .ds-card-title {
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 4px;
  }
  .ds-card-period {
    font-size: 13px;
    color: #8892B0;
    margin-bottom: 12px;
  }
  .ds-hero-val {
    font-size: 46px;
    font-weight: 900;
    color: #BCA772;
    text-align: center;
    margin: 10px 0 4px 0;
    text-shadow: 0 0 20px rgba(188, 167, 114, 0.2);
  }
  .ds-sub-val {
    font-size: 13px;
    color: #B7BEC9;
    text-align: center;
    margin-bottom: 14px;
  }
  .ds-source-pill {
    text-align: center;
    font-size: 12px;
    color: #8892B0;
    margin-bottom: 16px;
  }
  .ds-source-pill strong { color: #BCA772; }

  /* ACCORDION SUMMARY BUTTONS */
  .ds-details-group {
    margin-top: 16px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 16px;
  }
  summary.ds-btn-trigger {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    margin: 4px 6px 8px 0;
    user-select: none;
    transition: all 0.2s ease;
    list-style: none;
  }
  summary.ds-btn-trigger::-webkit-details-marker { display: none; }

  .ds-btn-sem { border-radius: 20px; text-transform: uppercase; font-size: 11px; }
  .ds-btn-tab { background: #1a1c20; border: 1px solid rgba(188, 167, 114, 0.3); color: #CBD5E1; }
  .ds-btn-tab:hover { border-color: #BCA772; color: #ffffff; }

  .ds-tab-content {
    background: #141619;
    border: 1px solid rgba(188, 167, 114, 0.25);
    border-radius: 12px;
    padding: 18px;
    margin-top: 10px;
    font-size: 13.5px;
    color: #CBD5E1;
    line-height: 1.6;
  }
  .ds-tab-heading {
    color: #BCA772;
    font-size: 14px;
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
  }
  .ds-exec-question {
    background: rgba(188, 167, 114, 0.05);
    border-left: 4px solid #BCA772;
    padding: 14px 18px;
    border-radius: 0 10px 10px 0;
    margin: 20px 0;
    font-size: 13.5px;
    color: #CBD5E1;
    line-height: 1.5;
  }
  .ds-exec-question strong { color: #ffffff; }
  .ds-rates-flex {
    display: flex;
    justify-content: center;
    gap: 16px;
    margin: 14px 0;
  }
  .ds-rate-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(188,167,114,0.35);
    padding: 8px 18px;
    border-radius: 8px;
    text-align: center;
  }
</style>

<div class="ds-dash-wrap">

  <div class="ds-header">
    <h1 style="color: #BCA772; font-size: 24px; font-weight: 800; text-transform: uppercase; margin-bottom: 8px;">🇧🇴 INDICADORES ECONÓMICOS DE BOLIVIA</h1>
    <p style="color: #B7BEC9; font-size: 13.5px; margin-bottom: 16px;">Monitoreo ejecutivo de datos clave actualizados al 02 de Agosto de 2026. Fuentes oficiales e independientes.</p>
    <a href="https://whatsapp.com/channel/0029VbDAeCQ1t90gu0qjtC07" target="_blank" style="display: inline-block; background: rgba(37, 211, 102, 0.15); border: 1px solid #25D366; color: #25D366 !important; padding: 10px 20px; border-radius: 25px; font-size: 12.5px; font-weight: 700; text-decoration: none !important;">
      📲 ACTUALIZACIONES DIARIAS: UNIRSE AL CANAL DE WHATSAPP &#10140;
    </a>
  </div>
'''

for idx, ind in enumerate(indicadores, 1):
    sem_style = get_badge_class(ind.get("semaforo", "rojo"))
    compra_venta_html = ""
    if "detalles_historicos" in ind and isinstance(ind["detalles_historicos"], dict) and "compra" in ind["detalles_historicos"]:
        compra_venta_html = f'''
        <div class="ds-rates-flex">
          <div class="ds-rate-box">
            <div style="font-size:11px; color:#8892B0; text-transform:uppercase;">Compra</div>
            <div style="font-size:16px; font-weight:700; color:#BCA772;">{ind["detalles_historicos"]["compra"]} Bs</div>
          </div>
          <div class="ds-rate-box">
            <div style="font-size:11px; color:#8892B0; text-transform:uppercase;">Venta</div>
            <div style="font-size:16px; font-weight:700; color:#BCA772;">{ind["detalles_historicos"]["venta"]} Bs</div>
          </div>
        </div>
        '''

    criterio_eval = ""
    if "criterio_evaluacion" in ind:
        crit = ind["criterio_evaluacion"]
        criterio_eval = f'''
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(188,167,114,0.2); padding: 12px 16px; border-radius: 8px; margin-top: 12px; font-size: 12.5px;">
          <div style="color: #BCA772; font-weight: 700; font-size: 11px; text-transform: uppercase; margin-bottom: 6px;">📐 PARÁMETROS TÉCNICOS DE EVALUACIÓN MACROECONÓMICA</div>
          <div>🟢 <strong>Verde:</strong> {crit.get("verde", "")}</div>
          <div style="margin: 4px 0;">🟡 <strong>Amarillo:</strong> {crit.get("amarillo", "")}</div>
          <div>🔴 <strong>Rojo:</strong> {crit.get("rojo", "")}</div>
        </div>
        '''

    html_out += f'''
  <!-- TARJETA {idx}: {ind.get("nombre")} -->
  <div class="ds-card-box">
    <div class="ds-card-title">{ind.get("nombre")}</div>
    <div class="ds-card-period">• Período: <strong>{ind.get("periodo")}</strong></div>

    {compra_venta_html}

    <div class="ds-hero-val">{ind.get("valor")}</div>
    <div class="ds-sub-val">{ind.get("unidad")}</div>
    <div class="ds-source-pill">Fuente: <strong>{ind.get("fuente")}</strong> | Actualizado al día: <strong>{ind.get("fecha_actualizacion")}</strong></div>

    <!-- PESTAÑAS INTERACTIVAS NATIVAS HTML5 -->
    <div class="ds-details-group">
      
      <!-- DESPLEGABLE 1: PARÁMETROS SEMÁFORO -->
      <details style="margin-bottom: 8px;">
        <summary class="ds-btn-trigger ds-btn-sem" style="{sem_style}">
          ● {ind.get("semaforo_label")} &#9660;
        </summary>
        <div class="ds-tab-content">
          <div class="ds-tab-heading">EVALUACIÓN TÉCNICA DEL ESTADO ACTUAL</div>
          <p>{ind.get("evaluacion_corta")}</p>
          {criterio_eval}
        </div>
      </details>

      <!-- DESPLEGABLE 2: ¿QUÉ ES ESTE INDICADOR? -->
      <details style="margin-bottom: 8px;">
        <summary class="ds-btn-trigger ds-btn-tab">
          📖 ¿Qué es este indicador? &#9660;
        </summary>
        <div class="ds-tab-content">
          <div class="ds-tab-heading">¿QUÉ ES ESTE INDICADOR?</div>
          <p>{ind.get("que_es")}</p>
        </div>
      </details>

      <!-- DESPLEGABLE 3: ANÁLISIS COYUNTURAL -->
      <details style="margin-bottom: 8px;">
        <summary class="ds-btn-trigger ds-btn-tab">
          💡 Análisis Coyuntural &#9660;
        </summary>
        <div class="ds-tab-content">
          <div class="ds-tab-heading">ANÁLISIS COYUNTURAL DE CAUSA-EFECTO</div>
          <p>{ind.get("analisis")}</p>
        </div>
      </details>

    </div>
  </div>

  <!-- RECUADRO DE CRITERIO EJECUTIVO ENTRE INDICADORES -->
  <div class="ds-exec-question">
    💡 <strong>Criterio Ejecutivo:</strong> {ind.get("pregunta_estrategica")}
  </div>
'''

html_out += f'''
  <!-- AFICHE OFICIAL DE PREVISUALIZACIÓN Y COMPARTIR -->
  <div style="text-align: center; margin-top: 35px; padding: 24px; background: #0d0d0d; border: 1px solid rgba(188, 167, 114, 0.35); border-radius: 16px;">
    <div style="color: #BCA772; font-weight: 800; font-size: 13.5px; margin-bottom: 16px; text-transform: uppercase;">PUBLICACIÓN OFICIAL PARA REDES SOCIALES</div>
    <a href="{cdn_url}" target="_blank">
      <img src="{cdn_url}" alt="Indicadores Económicos de Bolivia" width="600" style="max-width:100%; height:auto; border-radius:10px; border:1px solid #1E222A;" />
    </a>
  </div>

</div>
'''

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_out)

with open(copy_paste_path, "w", encoding="utf-8") as f:
    f.write(html_out)

print("SUCCESSFULLY BUILT NATIVE HTML5 INTERACTIVE DASHBOARD WITH ALL TABS, SEMAPHORES & EXECUTIVE QUESTIONS!")

# Push live via Blogger API
import urllib.request
import urllib.parse
import time

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
                        "content": html_out
                    }
                    req_up = urllib.request.Request(update_page_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="PUT")
                    with urllib.request.urlopen(req_up) as up_resp:
                        up_data = json.loads(up_resp.read().decode("utf-8"))
                        print(f"SUCCESSFULLY PUSHED NATIVE HTML5 INTERACTIVE TABS TO BLOGGER API! URL: {up_data.get('url')}")
