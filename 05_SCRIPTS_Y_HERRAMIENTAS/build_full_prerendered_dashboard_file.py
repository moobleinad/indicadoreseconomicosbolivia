import os

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
ind_dir = os.path.join(root_dir, "08_INDICADORES_ECONOMICOS")
html_path = os.path.join(ind_dir, "08.03_Dashboard_Indicadores_Economicos.html")

cdn_url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYeCIA7MRmr_6TVpf3cry8x0OfN-Iz3C_miEhJg0iJMBHlMyW8NmKbo8sT2Ej76oy8H_ovtseFk0CxuM3M93JWIGLi4x9QkWu0KJLz8QQ8Qandg5PKkavDv5-jn5lJ1J-iTSkWrzOiMUmrA2aEv6P9gpGxOlCrBZtlPOEz7CqSXvKlJHg4LxjCZZS7fpl8/s1024/09.02_afiche_indicadores_economicos_cuadrado.webp"

full_static_dashboard_html = f'''<style>
  .ds-dashboard-wrap {{
    max-width: 820px;
    margin: 0 auto;
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
    color: #ffffff;
    background-color: #000000;
    padding: 10px;
  }}
  .ds-header-box {{
    background: #0d0d0d;
    border: 1px solid rgba(188, 167, 114, 0.35);
    border-radius: 14px;
    padding: 26px 20px;
    text-align: center;
    margin-bottom: 20px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.8);
  }}
  .ds-header-title {{
    font-size: 24px;
    font-weight: 800;
    color: #BCA772;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .ds-header-sub {{
    font-size: 13.5px;
    color: #B7BEC9;
    margin-bottom: 16px;
    line-height: 1.4;
  }}
  .ds-wa-btn {{
    display: inline-block;
    background: rgba(37, 211, 102, 0.15);
    border: 1px solid #25D366;
    color: #25D366 !important;
    padding: 10px 22px;
    border-radius: 25px;
    font-size: 12.5px;
    font-weight: 700;
    text-decoration: none !important;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    transition: all 0.2s ease;
  }}
  .ds-wa-btn:hover {{
    background: #25D366;
    color: #000000 !important;
  }}
  .ds-card {{
    background: #0d0d0d;
    border: 1px solid rgba(188, 167, 114, 0.3);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 18px;
    text-align: center;
    box-shadow: 0 6px 24px rgba(0,0,0,0.7);
  }}
  .ds-card-title {{
    font-size: 21px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 4px;
  }}
  .ds-card-date {{
    font-size: 13px;
    color: #8892B0;
    margin-bottom: 14px;
  }}
  .ds-card-date strong {{
    color: #BCA772;
  }}
  .ds-hero-val {{
    font-size: 46px;
    font-weight: 900;
    color: #BCA772;
    margin: 8px 0 4px 0;
    line-height: 1.1;
    text-shadow: 0 0 20px rgba(188, 167, 114, 0.2);
  }}
  .ds-hero-unit {{
    font-size: 13px;
    color: #B7BEC9;
    margin-bottom: 14px;
  }}
  .ds-rates-box {{
    display: flex;
    justify-content: center;
    gap: 16px;
    margin: 14px 0;
  }}
  .ds-rate-pill {{
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(188, 167, 114, 0.35);
    padding: 10px 20px;
    border-radius: 10px;
    min-width: 120px;
  }}
  .ds-rate-lbl {{
    font-size: 11px;
    color: #8892B0;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.5px;
  }}
  .ds-rate-num {{
    font-size: 18px;
    font-weight: 800;
    color: #BCA772;
    margin-top: 2px;
  }}
  .ds-badge {{
    display: inline-block;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 11.5px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.4px;
    margin-bottom: 14px;
  }}
  .ds-badge-verde {{
    background: rgba(40, 167, 69, 0.15);
    border: 1px solid #2ecc71;
    color: #2ecc71;
  }}
  .ds-badge-rojo {{
    background: rgba(220, 53, 69, 0.15);
    border: 1px solid #e74c3c;
    color: #e74c3c;
  }}
  .ds-badge-amarillo {{
    background: rgba(255, 193, 7, 0.15);
    border: 1px solid #f1c40f;
    color: #f1c40f;
  }}
  .ds-card-desc {{
    font-size: 13.5px;
    color: #CBD5E1;
    text-align: left;
    margin-top: 16px;
    padding-top: 16px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    line-height: 1.6;
  }}
  .ds-question-box {{
    background: rgba(188, 167, 114, 0.04);
    border-left: 3px solid #BCA772;
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin-top: 14px;
    font-size: 13px;
    color: #B7BEC9;
    text-align: left;
  }}
  .ds-question-box strong {{
    color: #ffffff;
  }}
  .ds-poster-box {{
    text-align: center;
    margin-top: 35px;
    padding: 24px;
    background: #0d0d0d;
    border: 1px solid rgba(188, 167, 114, 0.35);
    border-radius: 16px;
  }}
  .ds-poster-title {{
    color: #BCA772;
    font-weight: 800;
    font-size: 13.5px;
    margin-bottom: 16px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
</style>

<div class="ds-dashboard-wrap">

  <!-- ENCABEZADO PRINCIPAL -->
  <div class="ds-header-box">
    <h1 class="ds-header-title">🇧🇴 INDICADORES ECONÓMICOS DE BOLIVIA</h1>
    <p class="ds-header-sub">Monitoreo ejecutivo de datos macroeconómicos clave. Análisis de estructura transparente y actualizado.</p>
    <a href="https://whatsapp.com/channel/0029VbDAeCQ1t90gu0qjtC07" target="_blank" class="ds-wa-btn">
      📲 ACTUALIZACIONES DIARIAS: UNIRSE AL CANAL DE WHATSAPP &#10140;
    </a>
  </div>

  <!-- TARJETA 1: DÓLAR PARALELO -->
  <div class="ds-card">
    <div class="ds-card-title">Dólar Paralelo / Mercado Libre</div>
    <div class="ds-card-date">Actualizado al <strong>02 de Agosto de 2026</strong></div>
    
    <div class="ds-rates-box">
      <div class="ds-rate-pill">
        <div class="ds-rate-lbl">Compra</div>
        <div class="ds-rate-num">11.65 Bs</div>
      </div>
      <div class="ds-rate-pill">
        <div class="ds-rate-lbl">Venta</div>
        <div class="ds-rate-num">11.85 Bs</div>
      </div>
    </div>

    <div class="ds-hero-val">11.75 Bs</div>
    <div class="ds-hero-unit">Promedio Mercado P2P (Binance, AirTM, Casas de Cambio)</div>
    <span class="ds-badge ds-badge-verde">● ESTABILIZADO EN MERCADO LIBRE</span>
    
    <div class="ds-card-desc">
      El dólar en el mercado libre refleja la cotización real de la divisa estadounidense en operaciones P2P y casas de cambio no reguladas. A diferencia del tipo fijo por decreto, este valor se determina por oferta y demanda directa de agentes económicos. Muestra convergencia con el tipo de cambio oficial flexible, reduciendo el riesgo de descalce mayorista.
    </div>

    <div class="ds-question-box">
      💡 <strong>Criterio Ejecutivo:</strong> Con la convergencia del dólar libre a 11.75 Bs, ¿tu empresa ya recalculó el costo real de reposición de inventarios?
    </div>
  </div>

  <!-- TARJETA 2: DÓLAR OFICIAL -->
  <div class="ds-card">
    <div class="ds-card-title">Dólar Oficial (BCB)</div>
    <div class="ds-card-date">Actualizado al <strong>02 de Agosto de 2026</strong></div>
    
    <div class="ds-rates-box">
      <div class="ds-rate-pill">
        <div class="ds-rate-lbl">Compra</div>
        <div class="ds-rate-num">12.07 Bs</div>
      </div>
      <div class="ds-rate-pill">
        <div class="ds-rate-lbl">Venta</div>
        <div class="ds-rate-num">12.19 Bs</div>
      </div>
    </div>

    <div class="ds-hero-val">12.13 Bs</div>
    <div class="ds-hero-unit">Tipo de Cambio Oficial Flexible (Banco Central de Bolivia)</div>
    <span class="ds-badge ds-badge-rojo">● CRÍTICO / AJUSTE REGULADO</span>
    
    <div class="ds-card-desc">
      Cotización oficial del Banco Central de Bolivia bajo el régimen flexible. La transición del régimen fijo (6.96 Bs) a un esquema flexible busca sincerar la paridad monetaria con la realidad del mercado y reordenar la liquidación de divisas en la banca formal.
    </div>

    <div class="ds-question-box">
      💡 <strong>Criterio Ejecutivo:</strong> Frente al ajuste del régimen flexible a 12.13 Bs, ¿tus contratos y pasivos bancarios cuentan con protección cambiaria?
    </div>
  </div>

  <!-- TARJETA 3: INFLACIÓN -->
  <div class="ds-card">
    <div class="ds-card-title">Inflación (IPC Acumulado)</div>
    <div class="ds-card-date">A Junio de 2026 (1er Semestre)</div>
    
    <div class="ds-hero-val">4.82%</div>
    <div class="ds-hero-unit">Variación Interanual a 12 meses: 9.23% (INE)</div>
    <span class="ds-badge ds-badge-rojo">● ALTA PRESIÓN DE PRECIOS</span>
    
    <div class="ds-card-desc">
      El Índice de Precios al Consumidor acumula 4,82% en el primer semestre del año. El ritmo interanual a doce meses del 9,23% refleja el traslado de costos por insumos importados y productos agrícolas afectados por la fase de ajuste monetario.
    </div>

    <div class="ds-question-box">
      💡 <strong>Criterio Ejecutivo:</strong> Con la inflación interanual del 9.23%, ¿cuántos puntos de margen operativo ha absorbido el costo de insumos en tu sector?
    </div>
  </div>

  <!-- TARJETA 4: RESERVAS RIN -->
  <div class="ds-card">
    <div class="ds-card-title">Reservas Internacionales (RIN)</div>
    <div class="ds-card-date">Al 30 de Junio de 2026</div>
    
    <div class="ds-hero-val">$3.617,3 MM</div>
    <div class="ds-hero-unit">Oro Físico: $2.882,9M (22.3 t) | Divisas Líquidas: $666,1M</div>
    <span class="ds-badge ds-badge-amarillo">● PRECAUCIÓN / MONITOREO</span>
    
    <div class="ds-card-desc">
      Las Reservas Internacionales Netas se sostienen prioritariamente en el valor de las reservas de oro físico ($2.882,9M), mientras que la liquidez de divisas de libre disponibilidad ($666,1M) permanece bajo seguimiento continuo del BCB.
    </div>

    <div class="ds-question-box">
      💡 <strong>Criterio Ejecutivo:</strong> Considerando la liquidez actual de divisas, ¿tienes garantizado el flujo de pagos de importaciones al exterior a 90 días?
    </div>
  </div>

  <!-- TARJETA 5: BALANZA COMERCIAL -->
  <div class="ds-card">
    <div class="ds-card-title">Balanza Comercial</div>
    <div class="ds-card-date">1er Semestre de 2026</div>
    
    <div class="ds-hero-val">+$1.669 MM</div>
    <div class="ds-hero-unit">Superávit Comercial Acumulado (INE)</div>
    <span class="ds-badge ds-badge-verde">● SUPERÁVIT RELEVANTE</span>
    
    <div class="ds-card-desc">
      El saldo comercial positivo de $1.669 millones de dólares está impulsado por el repunte de exportaciones no tradicionales (soya, minería, carne) y la moderación de importaciones de combustibles bajo los nuevos esquemas de producción.
    </div>
  </div>

  <!-- AFICHE OFICIAL DE PREVISUALIZACIÓN Y COMPARTIR -->
  <div class="ds-poster-box">
    <div class="ds-poster-title">PUBLICACIÓN OFICIAL PARA REDES SOCIALES</div>
    <a href="{cdn_url}" target="_blank">
      <img src="{cdn_url}" alt="Indicadores Económicos de Bolivia" width="600" style="max-width:100%; height:auto; border-radius:10px; border:1px solid #1E222A;" />
    </a>
  </div>

</div>
'''

with open(html_path, "w", encoding="utf-8") as f:
    f.write(full_static_dashboard_html)

print("SUCCESS: REBUILT 08.03_Dashboard_Indicadores_Economicos.html AS 100% PURE PRE-RENDERED STATIC HTML & CSS!")
