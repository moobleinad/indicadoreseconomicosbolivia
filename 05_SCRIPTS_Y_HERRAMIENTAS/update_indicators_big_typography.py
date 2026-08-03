import os
import json
import urllib.request
import urllib.parse

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
html_path = os.path.join(ind_dir, "08.03_Dashboard_Indicadores_Economicos.html")
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

# BUILD ULTRA-LEGIBLE BIG TYPOGRAPHY DASHBOARD HTML
big_dashboard_html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Indicadores Económicos de Bolivia | Daniel Simons</title>
  <style>
    :root {
      --bg-color: #000000;
      --card-bg: #0d0d0d;
      --card-border: rgba(188, 167, 114, 0.35);
      --gold-accent: #BCA772;
      --gold-hover: #d4a017;
      --text-main: #FFFFFF;
      --text-muted: #E0E0E0;
      --text-subtle: #A0AAB8;
      
      --badge-human-bg: rgba(76, 175, 80, 0.15);
      --badge-human-border: rgba(76, 175, 80, 0.4);
      --badge-human-text: #81C784;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background-color: var(--bg-color);
      color: var(--text-main);
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      line-height: 1.5;
      padding: 24px 12px;
    }

    .econ-dashboard {
      max-width: 900px;
      margin: 0 auto;
    }

    /* Encabezado Principal */
    .dashboard-header {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 28px 24px;
      text-align: center;
      margin-bottom: 28px;
      box-shadow: 0 6px 25px rgba(0, 0, 0, 0.9);
    }

    .dashboard-title {
      font-size: 26px;
      font-weight: 800;
      color: var(--gold-accent);
      letter-spacing: 0.5px;
      margin-bottom: 8px;
      text-transform: uppercase;
    }

    .dashboard-subtitle {
      font-size: 14px;
      color: var(--text-muted);
      max-width: 700px;
      margin: 0 auto;
    }

    /* Grid de Tarjetas Principales */
    .indicator-grid {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }

    /* Tarjeta Individual Estilo Mockup */
    .indicator-card {
      background: var(--card-bg);
      border: 1.5px solid var(--card-border);
      border-radius: 14px;
      overflow: hidden;
      transition: border-color 0.25s ease, transform 0.25s ease;
      box-shadow: 0 4px 18px rgba(0, 0, 0, 0.6);
    }

    .indicator-card:hover {
      border-color: var(--gold-accent);
    }

    /* Header de la Tarjeta */
    .indicator-main {
      padding: 24px 26px;
      display: flex;
      flex-direction: column;
      gap: 16px;
      cursor: pointer;
      user-select: none;
    }

    .indicator-header-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 12px;
    }

    .indicator-name {
      font-size: 22px;
      font-weight: 800;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 10px;
      line-height: 1.2;
    }

    .toggle-icon {
      font-size: 13px;
      color: var(--gold-accent);
      transition: transform 0.25s ease;
    }

    .indicator-card.open .toggle-icon {
      transform: rotate(180deg);
    }

    .indicator-date-badge {
      font-size: 13.5px;
      color: #ffffff;
      font-weight: 600;
      margin-top: 4px;
    }

    .indicator-date-badge strong {
      color: var(--gold-accent);
    }

    /* DATO NUMÉRICO GIGANTE SOBRESALIENTE */
    .indicator-big-value-container {
      text-align: center;
      padding: 16px 0;
      margin: 8px 0;
    }

    .indicator-big-value {
      font-size: 52px;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: -1px;
      line-height: 1;
      text-shadow: 0 0 20px rgba(255, 255, 255, 0.15);
    }

    /* DESGLOSE GIGANTE PARA COMPRA Y VENTA */
    .rate-box-gigante {
      display: flex;
      justify-content: space-around;
      align-items: center;
      background: rgba(188, 167, 114, 0.1);
      border: 1.5px solid rgba(188, 167, 114, 0.4);
      padding: 16px 20px;
      border-radius: 12px;
      margin: 8px 0;
    }

    .rate-item-g {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .rate-label-g {
      font-size: 12px;
      font-weight: 800;
      color: var(--gold-accent);
      letter-spacing: 1px;
      margin-bottom: 2px;
    }

    .rate-val-g {
      font-size: 34px;
      font-weight: 900;
      color: #ffffff;
      line-height: 1;
    }

    .rate-divider-g {
      font-size: 28px;
      color: rgba(188, 167, 114, 0.4);
      font-weight: 300;
    }

    .indicator-footer-meta {
      display: flex;
      flex-direction: column;
      gap: 6px;
      text-align: center;
      font-size: 13.5px;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .indicator-footer-meta strong {
      color: var(--gold-accent);
      font-weight: 700;
    }

    /* Badges */
    .verification-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 14px;
      background: var(--badge-human-bg);
      border: 1px solid var(--badge-human-border);
      color: var(--badge-human-text);
    }

    /* Desplegable de Detalles */
    .indicator-details {
      display: none;
      padding: 0 26px 26px 26px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(0, 0, 0, 0.4);
    }

    .details-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 14px;
      margin-top: 20px;
    }

    .detail-item {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 8px;
      padding: 12px 14px;
    }

    .detail-label {
      font-size: 11px;
      color: var(--text-subtle);
      text-transform: uppercase;
      font-weight: 700;
    }

    .detail-val {
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
      margin-top: 3px;
    }

    .history-title {
      font-size: 14px;
      font-weight: 800;
      color: var(--gold-accent);
      margin: 20px 0 10px 0;
      text-transform: uppercase;
    }

    .history-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }

    .history-table th,
    .history-table td {
      padding: 10px 12px;
      text-align: left;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }

    .history-table th {
      color: var(--text-subtle);
      font-weight: 700;
    }

    .history-table td strong {
      color: var(--gold-accent);
    }

    .methodology-box {
      margin-top: 18px;
      padding: 14px 16px;
      background: rgba(188, 167, 114, 0.08);
      border-left: 4px solid var(--gold-accent);
      font-size: 13px;
      color: #ffffff;
      border-radius: 0 8px 8px 0;
      line-height: 1.5;
    }

    @media (max-width: 600px) {
      .indicator-name {
        font-size: 19px;
      }
      .indicator-big-value {
        font-size: 42px;
      }
      .rate-val-g {
        font-size: 26px;
      }
      .rate-label-g {
        font-size: 10.5px;
      }
    }
  </style>
</head>
<body>

<div class="econ-dashboard">

  <!-- Encabezado Principal -->
  <div class="dashboard-header">
    <h1 class="dashboard-title">INDICADORES ECONÓMICOS DE BOLIVIA</h1>
    <p class="dashboard-subtitle">
      Monitoreo ejecutivo de datos clave. Información al día desde fuentes oficiales y de mercado sin modificaciones.
    </p>
  </div>

  <!-- Lista de Indicadores -->
  <div class="indicator-grid" id="indicatorContainer">
    <!-- Se genera dinámicamente -->
  </div>

</div>

<script>
  const datosIndicadores = [
    {
      "id": "tc_oficial",
      "nombre": "Dólar Oficial (BCB)",
      "compra": "11.95 Bs",
      "venta": "12.13 Bs",
      "valor": "12.13 Bs",
      "unidad": "Bs / USD",
      "fuente": "Banco Central de Bolivia (BCB)",
      "periodo": "02 de Agosto de 2026",
      "fecha_actualizacion": "02/08/2026",
      "verificacion_texto": "✓ Confirmado por ser humano",
      "detalles_historicos": [
        {"periodo": "02/08/2026", "valor": "Compra: 11.95 Bs | Venta: 12.13 Bs", "fuente": "BCB (Dólar Flexible)"},
        {"periodo": "01/08/2026", "valor": "Compra: 11.95 Bs | Venta: 12.13 Bs", "fuente": "BCB"},
        {"periodo": "31/07/2026", "valor": "Compra: 11.98 Bs | Venta: 12.15 Bs", "fuente": "BCB"},
        {"periodo": "Régimen Fijo 2025", "valor": "6.86 Bs / 6.96 Bs", "fuente": "BCB (Régimen anterior)"}
      ],
      "nota": "Cotización oficial diaria publicada por el Banco Central de Bolivia bajo la política de tipo de cambio flexible."
    },
    {
      "id": "tc_paralelo",
      "nombre": "Dólar Paralelo / Mercado Libre",
      "compra": "11.60 Bs",
      "venta": "11.90 Bs",
      "valor": "11.90 Bs",
      "unidad": "Bs / USD (Promedio Diario)",
      "fuente": "Mercado P2P Binance / AirTM / Casas de Cambio",
      "periodo": "02 de Agosto de 2026",
      "fecha_actualizacion": "02/08/2026",
      "verificacion_texto": "✓ Confirmado por ser humano",
      "detalles_historicos": [
        {"periodo": "02/08/2026", "valor": "Compra: 11.60 Bs | Venta: 11.90 Bs", "fuente": "Mercado P2P"},
        {"periodo": "01/08/2026", "valor": "Compra: 11.65 Bs | Venta: 11.85 Bs", "fuente": "Mercado P2P"},
        {"periodo": "Julio 2026", "valor": "Compra: 11.90 Bs | Venta: 12.10 Bs", "fuente": "Mercado P2P"}
      ],
      "nota": "Promedio ponderado de precios efectivos de compra y venta en plataformas digitales P2P y mercado libre no regulado."
    },
    {
      "id": "inflacion",
      "nombre": "Inflación (IPC)",
      "valor": "4.82%",
      "unidad": "Acumulada 1er Semestre (Interanual: 9.23%)",
      "fuente": "Instituto Nacional de Estadística (INE)",
      "periodo": "A Junio 2026 (1er Semestre)",
      "fecha_actualizacion": "05/07/2026",
      "verificacion_texto": "✓ Confirmado por ser humano",
      "detalles_historicos": [
        {"periodo": "Acumulada 1S 2026", "valor": "4.82%", "fuente": "INE"},
        {"periodo": "Junio 2026 (Mensual)", "valor": "2.15%", "fuente": "INE"},
        {"periodo": "Interanual (12 Meses)", "valor": "9.23%", "fuente": "INE"},
        {"periodo": "Gestión 2025 Total", "valor": "7.40%", "fuente": "INE"}
      ],
      "nota": "Variación porcentual oficial del Índice de Precios al Consumidor publicado mensualmente por el INE."
    },
    {
      "id": "reservas",
      "nombre": "Reservas Internacionales (RIN)",
      "valor": "$3.617,3 MM",
      "unidad": "Millones de USD",
      "fuente": "Banco Central de Bolivia (BCB)",
      "periodo": "Al 30 de Junio de 2026",
      "fecha_actualizacion": "15/07/2026",
      "verificacion_texto": "✓ Confirmado por ser humano",
      "detalles_historicos": [
        {"periodo": "Junio 2026", "valor": "$3.617,3 MM", "fuente": "BCB (Oro: $2.882.9M | Divisas: $666.1M)"},
        {"periodo": "Diciembre 2025", "valor": "$3.713,2 MM", "fuente": "BCB"},
        {"periodo": "Diciembre 2024", "valor": "$1.708,0 MM", "fuente": "BCB"}
      ],
      "nota": "Monto total de RIN reportado por el BCB ($2.882,9M en oro físico de 22.3 toneladas, $666,1M en divisas y DEG)."
    },
    {
      "id": "pib",
      "nombre": "Crecimiento del PIB",
      "valor": "2.10%",
      "unidad": "Variación Porcentual Anual",
      "fuente": "Instituto Nacional de Estadística (INE)",
      "periodo": "Gestión 2025 / 2026",
      "fecha_actualizacion": "25/06/2026",
      "verificacion_texto": "✓ Confirmado por ser humano",
      "detalles_historicos": [
        {"periodo": "Proyección 2026", "valor": "2.10%", "fuente": "INE / Banco Mundial"},
        {"periodo": "Gestión 2025", "valor": "2.30%", "fuente": "INE"},
        {"periodo": "Gestión 2024", "valor": "3.10%", "fuente": "INE"}
      ],
      "nota": "Variación interanual del Producto Interno Bruto a precios constantes."
    }
  ];

  function renderDashboard() {
    const container = document.getElementById("indicatorContainer");
    container.innerHTML = "";

    datosIndicadores.forEach(item => {
      const historyRows = item.detalles_historicos.map(h => `
        <tr>
          <td>${h.periodo}</td>
          <td><strong>${h.valor}</strong></td>
          <td>${h.fuente}</td>
        </tr>
      `).join('');

      let mainDisplayHTML = `
        <div class="indicator-big-value-container">
          <div class="indicator-big-value">${item.valor}</div>
        </div>
      `;

      if (item.compra && item.venta) {
        mainDisplayHTML = `
          <div class="rate-box-gigante">
            <div class="rate-item-g">
              <span class="rate-label-g">COMPRA</span>
              <span class="rate-val-g">${item.compra}</span>
            </div>
            <div class="rate-divider-g">|</div>
            <div class="rate-item-g">
              <span class="rate-label-g">VENTA</span>
              <span class="rate-val-g">${item.venta}</span>
            </div>
          </div>
        `;
      }

      const cardHTML = `
        <div class="indicator-card" id="card-${item.id}">
          <div class="indicator-main" onclick="toggleDetails('${item.id}')">
            
            <div class="indicator-header-top">
              <div>
                <div class="indicator-name">
                  ${item.nombre}
                  <span class="toggle-icon">▼</span>
                </div>
                <div class="indicator-date-badge">
                  Fecha de última actualización: <strong>${item.periodo}</strong>
                </div>
              </div>
              <div>
                <span class="verification-badge">${item.verificacion_texto}</span>
              </div>
            </div>

            ${mainDisplayHTML}

            <div class="indicator-footer-meta">
              <div>${item.unidad}</div>
              <div>Fuente: <strong>${item.fuente}</strong></div>
            </div>

          </div>

          <div class="indicator-details" id="details-${item.id}">
            <div class="details-grid">
              <div class="detail-item">
                <div class="detail-label">Fuente Oficial / Mercado</div>
                <div class="detail-val">${item.fuente}</div>
              </div>
              <div class="detail-item">
                <div class="detail-label">Fecha de última actualización</div>
                <div class="detail-val">${item.periodo}</div>
              </div>
              <div class="detail-item">
                <div class="detail-label">Última Revisión</div>
                <div class="detail-val">${item.fecha_actualizacion}</div>
              </div>
            </div>

            <div class="history-title">📊 Histórico y Registro Comparativo</div>
            <table class="history-table">
              <thead>
                <tr>
                  <th>Período / Fecha</th>
                  <th>Valor Registrado</th>
                  <th>Fuente Registrada</th>
                </tr>
              </thead>
              <tbody>
                ${historyRows}
              </tbody>
            </table>

            <div class="methodology-box">
              💡 <strong>Detalle y metodología:</strong> ${item.nota}
            </div>
          </div>
        </div>
      `;

      container.insertAdjacentHTML('beforeend', cardHTML);
    });
  }

  function toggleDetails(id) {
    const details = document.getElementById(`details-${id}`);
    const card = document.getElementById(`card-${id}`);

    if (details.style.display === "block") {
      details.style.display = "none";
      card.classList.remove("open");
    } else {
      details.style.display = "block";
      card.classList.add("open");
    }
  }

  document.addEventListener("DOMContentLoaded", renderDashboard);
</script>

</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(big_dashboard_html)
print("SAVED ULTRA-LEGIBLE BIG TYPOGRAPHY DASHBOARD HTML!")

# REFRESH TOKEN AND UPDATE LIVE ON BLOGGER
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
                    "content": big_dashboard_html
                }
                req_up = urllib.request.Request(update_page_url, data=json.dumps(page_payload).encode("utf-8"), headers=headers, method="PUT")
                with urllib.request.urlopen(req_up) as up_resp:
                    up_data = json.loads(up_resp.read().decode("utf-8"))
                    print("PAGE UPDATED LIVE SUCCESSFULLY WITH BIG TYPOGRAPHY!")
                    print("PAGE URL:", up_data.get("url"))
