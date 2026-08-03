import os
import json

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")

json_path = os.path.join(ind_dir, "08.02_Datos_Indicadores_Bolivia.json")
html_path = os.path.join(ind_dir, "08.03_Dashboard_Indicadores_Economicos.html")

# 1. UPDATE JSON DATA WITH COMPRA AND VENTA
with open(json_path, "r", encoding="utf-8") as f:
    datos = json.load(f)

for item in datos["indicadores"]:
    if item["id"] == "tc_oficial":
        item["compra"] = "11.95 Bs"
        item["venta"] = "12.13 Bs"
        item["valor"] = "Compra: 11.95 Bs | Venta: 12.13 Bs"
        item["periodo"] = "02 de Agosto de 2026"
        item["fecha_actualizacion"] = "02/08/2026"
    elif item["id"] == "tc_paralelo":
        item["compra"] = "11.60 Bs"
        item["venta"] = "11.90 Bs"
        item["valor"] = "Compra: 11.60 Bs | Venta: 11.90 Bs"
        item["periodo"] = "02 de Agosto de 2026"
        item["fecha_actualizacion"] = "02/08/2026"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)
print("UPDATED JSON WITH COMPRA & VENTA DATA!")

# 2. UPDATE HTML FILE TO DYNAMICALLY RENDER COMPRA AND VENTA BOXES
new_html_content = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Indicadores Económicos de Bolivia | Daniel Simons</title>
  <style>
    :root {
      --bg-color: #000000;
      --card-bg: #0d0d0d;
      --card-border: rgba(188, 167, 114, 0.25);
      --gold-accent: #BCA772;
      --gold-hover: #d4a017;
      --text-main: #FFFFFF;
      --text-muted: #B7BEC9;
      --text-subtle: #8892B0;
      
      --status-stable: #28a745;
      --status-caution: #ffc107;
      --status-alert: #dc3545;

      --badge-ai-bg: rgba(77, 163, 255, 0.12);
      --badge-ai-border: rgba(77, 163, 255, 0.3);
      --badge-ai-text: #64B5F6;

      --badge-human-bg: rgba(76, 175, 80, 0.12);
      --badge-human-border: rgba(76, 175, 80, 0.3);
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
      padding: 20px 10px;
    }

    .econ-dashboard {
      max-width: 900px;
      margin: 0 auto;
    }

    /* Encabezado Principal */
    .dashboard-header {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 24px 20px;
      text-align: center;
      margin-bottom: 24px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
    }

    .dashboard-title {
      font-size: 22px;
      font-weight: 700;
      color: var(--gold-accent);
      letter-spacing: 0.5px;
      margin-bottom: 6px;
      text-transform: uppercase;
    }

    .dashboard-subtitle {
      font-size: 13px;
      color: var(--text-muted);
      max-width: 650px;
      margin: 0 auto;
    }

    /* Grid de Tarjetas Principales */
    .indicator-grid {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    /* Tarjeta Individual */
    .indicator-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      overflow: hidden;
      transition: border-color 0.2s ease, transform 0.2s ease;
    }

    .indicator-card:hover {
      border-color: rgba(188, 167, 114, 0.5);
    }

    /* Header de la Tarjeta */
    .indicator-main {
      padding: 18px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      cursor: pointer;
      user-select: none;
      gap: 16px;
    }

    .indicator-info {
      flex: 1;
    }

    .indicator-name {
      font-size: 17px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .toggle-icon {
      font-size: 11px;
      color: var(--gold-accent);
      transition: transform 0.2s ease;
    }

    .indicator-card.open .toggle-icon {
      transform: rotate(180deg);
    }

    .indicator-meta-brief {
      font-size: 11px;
      color: var(--text-subtle);
      margin-top: 4px;
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }

    .indicator-meta-brief strong {
      color: var(--gold-accent);
    }

    .indicator-value-container {
      text-align: right;
      display: flex;
      flex-direction: column;
      align-items: flex-end;
    }

    .indicator-value {
      font-size: 24px;
      font-weight: 800;
      color: var(--gold-accent);
      letter-spacing: -0.5px;
      line-height: 1.1;
    }

    .indicator-unit {
      font-size: 10.5px;
      color: var(--text-subtle);
      margin-top: 2px;
    }

    /* ESTILOS DE DESGLOSE COMPRA Y VENTA */
    .rate-box-container {
      display: flex;
      gap: 12px;
      align-items: center;
      background: rgba(188, 167, 114, 0.08);
      border: 1px solid rgba(188, 167, 114, 0.3);
      padding: 8px 16px;
      border-radius: 8px;
    }

    .rate-item {
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .rate-label {
      font-size: 9.5px;
      font-weight: 800;
      color: var(--text-subtle);
      letter-spacing: 0.5px;
    }

    .rate-val {
      font-size: 18px;
      font-weight: 800;
      color: var(--gold-accent);
    }

    .rate-divider {
      font-size: 16px;
      color: rgba(188, 167, 114, 0.4);
    }

    /* Badges de Verificacion */
    .verification-badge {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-size: 10.5px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 12px;
      margin-top: 6px;
    }

    .badge-ia {
      background: var(--badge-ai-bg);
      border: 1px solid var(--badge-ai-border);
      color: var(--badge-ai-text);
    }

    .badge-humano {
      background: var(--badge-human-bg);
      border: 1px solid var(--badge-human-border);
      color: var(--badge-human-text);
    }

    /* Desplegable de Detalles */
    .indicator-details {
      display: none;
      padding: 0 20px 20px 20px;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      background: rgba(0, 0, 0, 0.3);
    }

    .details-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 12px;
      margin-top: 16px;

    }

    .detail-item {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 6px;
      padding: 10px;
    }

    .detail-label {
      font-size: 10px;
      color: var(--text-subtle);
      text-transform: uppercase;
    }

    .detail-val {
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-main);
      margin-top: 2px;
    }

    .history-title {
      font-size: 12px;
      font-weight: 700;
      color: var(--gold-accent);
      margin: 16px 0 8px 0;
      text-transform: uppercase;
    }

    .history-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 11.5px;
    }

    .history-table th,
    .history-table td {
      padding: 8px 10px;
      text-align: left;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    }

    .history-table th {
      color: var(--text-subtle);
      font-weight: 600;
    }

    .history-table td strong {
      color: var(--gold-accent);
    }

    .methodology-box {
      margin-top: 14px;
      padding: 10px 12px;
      background: rgba(188, 167, 114, 0.05);
      border-left: 3px solid var(--gold-accent);
      font-size: 11px;
      color: var(--text-muted);
      border-radius: 0 6px 6px 0;
    }

    @media (max-width: 600px) {
      .indicator-main {
        flex-direction: column;
        align-items: flex-start;

      }
      .indicator-value-container {
        align-items: flex-start;
        width: 100%;
        margin-top: 8px;

      }
      .rate-box-container {
        width: 100%;
        justify-content: space-around;

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
      "valor": "Compra: 11.95 Bs | Venta: 12.13 Bs",
      "unidad": "Bs / USD",
      "fuente": "Banco Central de Bolivia (BCB)",
      "periodo": "02 de Agosto de 2026",
      "fecha_actualizacion": "02/08/2026",
      "verificacion": "humano",
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
      "valor": "Compra: 11.60 Bs | Venta: 11.90 Bs",
      "unidad": "Bs / USD (Promedio Diario)",
      "fuente": "Mercado P2P Binance / AirTM / Casas de Cambio",
      "periodo": "02 de Agosto de 2026",
      "fecha_actualizacion": "02/08/2026",
      "verificacion": "humano",
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
      "verificacion": "humano",
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
      "verificacion": "humano",
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
      "verificacion": "humano",
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
      const isIA = item.verificacion === "ia";
      const badgeClass = isIA ? "badge-ia" : "badge-humano";

      const historyRows = item.detalles_historicos.map(h => `
        <tr>
          <td>${h.periodo}</td>
          <td><strong>${h.valor}</strong></td>
          <td>${h.fuente}</td>
        </tr>
      `).join('');

      let valueHTML = `
        <div class="indicator-value">${item.valor}</div>
        <div class="indicator-unit">${item.unidad}</div>
      `;

      if (item.compra && item.venta) {
        valueHTML = `
          <div class="rate-box-container">
            <div class="rate-item">
              <span class="rate-label">COMPRA</span>
              <span class="rate-val">${item.compra}</span>
            </div>
            <div class="rate-divider">|</div>
            <div class="rate-item">
              <span class="rate-label">VENTA</span>
              <span class="rate-val">${item.venta}</span>
            </div>
          </div>
          <div class="indicator-unit" style="margin-top: 4px;">${item.unidad}</div>
        `;
      }

      const cardHTML = `
        <div class="indicator-card" id="card-${item.id}">
          <div class="indicator-main" onclick="toggleDetails('${item.id}')">
            <div class="indicator-info">
              <div class="indicator-name">
                ${item.nombre}
                <span class="toggle-icon">▼</span>
              </div>
              <div class="indicator-meta-brief">
                <span>Fuente: <strong>${item.fuente}</strong></span>
                <span>• Fecha: <strong>${item.periodo}</strong></span>
              </div>
              <div>
                <span class="verification-badge ${badgeClass}">${item.verificacion_texto}</span>
              </div>
            </div>
            <div class="indicator-value-container">
              ${valueHTML}
            </div>
          </div>

          <div class="indicator-details" id="details-${item.id}">
            <div class="details-grid">
              <div class="detail-item">
                <div class="detail-label">Fuente Oficial / Mercado</div>
                <div class="detail-val">${item.fuente}</div>
              </div>
              <div class="detail-item">
                <div class="detail-label">Fecha / Período Exacto</div>
                <div class="detail-val">${item.periodo}</div>
              </div>
              <div class="detail-item">
                <div class="detail-label">Última Actualización</div>
                <div class="detail-val">${item.fecha_actualizacion}</div>
              </div>
            </div>

            <div class="history-title">📊 Histórico y Registro Comparativo</div>
            <table class="history-table">
              <thead>
                <tr>
                  <th>Período / Fecha</th>
                  <th>Valor</th>
                  <th>Fuente Registrada</th>
                </tr>
              </thead>
              <tbody>
                ${historyRows}
              </tbody>
            </table>

            <div class="methodology-box">
              💡 <strong>Detalle de la fuente:</strong> ${item.nota}
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
    f.write(new_html_content)

print("UPDATED HTML DASHBOARD WITH COMPRA / VENTA COLUMNS!")
