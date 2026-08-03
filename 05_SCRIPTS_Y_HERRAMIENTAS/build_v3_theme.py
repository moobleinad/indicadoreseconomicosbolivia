import os
import xml.etree.ElementTree as ET

source_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\copia de seguridad del tema web\theme-433667097766389126.xml"
output_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado"
output_path = os.path.join(output_dir, "v3_theme_optimizado.xml")

os.makedirs(output_dir, exist_ok=True)

with open(source_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# Live Page URLs created on Blogger:
URL_DESTILADO = "https://www.danielsimons.xyz/p/destilado-de-ideas-de-negocio_0599447061.html"
URL_FORJA = "https://www.danielsimons.xyz/p/forja-disciplina-habitos-y-lucidez.html"
URL_MARKETING = "https://www.danielsimons.xyz/p/marketing-360.html"
URL_MYPE = "https://www.danielsimons.xyz/p/impulso-mype-360.html"
URL_JUEGO = "https://www.danielsimons.xyz/p/el-juego-del-emprendedor-libro-para.html"

# 1. SEO & Open Graph Meta Tags
seo_block = """
  <!-- OPTIMIZACION SEO Y META TAGS OPEN GRAPH (VERSION v3) -->
  <b:if cond='data:view.isSingleItem'>
    <meta expr:content='data:view.title.escaped + " | Daniel Simons"' property='og:title'/>
    <meta expr:content='data:view.title.escaped + " | Daniel Simons"' name='twitter:title'/>
    <b:if cond='data:view.description'>
      <meta expr:content='data:view.description' name='description'/>
      <meta expr:content='data:view.description' property='og:description'/>
      <meta expr:content='data:view.description' name='twitter:description'/>
    <b:else/>
      <meta expr:content='data:view.title.escaped + " - Servicios de emprendimiento, trabajo intelectual, proyectos productivos y recursos docentes por Daniel Simons."' name='description'/>
      <meta expr:content='data:view.title.escaped + " - Servicios de emprendimiento, trabajo intelectual, proyectos productivos y recursos docentes por Daniel Simons."' property='og:description'/>
      <meta expr:content='data:view.title.escaped + " - Servicios de emprendimiento, trabajo intelectual, proyectos productivos y recursos docentes por Daniel Simons."' name='twitter:description'/>
    </b:if>
    <meta content='article' property='og:type'/>
  <b:else/>
    <meta content='Daniel Simons | Consultoría en Emprendimientos &amp; Trabajo Intelectual' property='og:title'/>
    <meta content='Daniel Simons | Consultoría en Emprendimientos &amp; Trabajo Intelectual' name='twitter:title'/>
    <meta content='Portal oficial de Daniel Simons. Servicios de consultoría para emprendimientos (Destilado de Ideas, Forja, Marketing 360, Impulso MYPE), trabajo intelectual, análisis y contenidos académicos.' name='description'/>
    <meta content='Portal oficial de Daniel Simons. Servicios de consultoría para emprendimientos (Destilado de Ideas, Forja, Marketing 360, Impulso MYPE), trabajo intelectual, análisis y contenidos académicos.' property='og:description'/>
    <meta content='Portal oficial de Daniel Simons. Servicios de consultoría para emprendimientos (Destilado de Ideas, Forja, Marketing 360, Impulso MYPE), trabajo intelectual, análisis y contenidos académicos.' name='twitter:description'/>
    <meta content='website' property='og:type'/>
  </b:if>
  
  <meta content='Daniel Simons' name='author'/>
  <meta content='Daniel Simons' property='og:site_name'/>
  <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
  <meta content='summary_large_image' name='twitter:card'/>
  <meta content='index, follow, max-image-preview:large' name='robots'/>
  <meta content='daniel simons, emprendimientos, destilado de ideas, forja de proyectos, marketing 360, impulso mype, historia bolivia, geografia economica, santa cruz' name='keywords'/>
"""

# 2. Enhanced CSS Block for v3
css_block = """
  <style type='text/css'>
  /*<![CDATA[*/
    body {
      color: #e6e6e6 !important;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
      background-color: #0c0d10 !important;
    }

    body.homepage-view .sidebar-container {
      display: none !important;
    }

    body.homepage-view .page,
    body.homepage-view #main,
    body.homepage-view .centered-bottom {
      width: 100% !important;
      max-width: 1200px !important;
      float: none !important;
      margin: 0 auto !important;
    }

    /* BARRA DE SENDAS Y SERVICIOS EN PORTADA */
    .ds-sendas-bar {
      background: #131720;
      border: 1px solid rgba(188, 167, 114, 0.3);
      border-radius: 12px;
      padding: 16px 20px;
      margin: 20px 0 30px 0;
      display: flex;
      justify-content: space-around;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.5);
    }

    .ds-senda-item {
      display: flex;
      align-items: center;
      gap: 8px;
      color: #ffffff !important;
      font-family: 'Montserrat', sans-serif;
      font-weight: 700;
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      text-decoration: none !important;
      padding: 8px 16px;
      border-radius: 20px;
      background: rgba(255,255,255,0.04);
      border: 1px solid transparent;
      transition: all 0.25s ease;
    }

    .ds-senda-item:hover {
      background: rgba(188, 167, 114, 0.15);
      border-color: #bca772;
      color: #bca772 !important;
      transform: translateY(-2px);
    }

    .ds-section-divider {
      text-align: center;
      margin: 30px 0 25px 0;
      position: relative;
    }

    .ds-section-divider h2 {
      font-family: 'Montserrat', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .ds-section-divider span {
      color: #bca772;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 2px;
      display: block;
      margin-bottom: 4px;
    }

    .post-body, .post-body p {
      font-size: 19px !important;
      line-height: 1.75 !important;
      color: #e0e0e0 !important;
    }

    .post-title, .post-title a {
      color: #ffffff !important;
      font-family: 'Montserrat', sans-serif !important;
      font-weight: 700 !important;
      transition: color 0.3s ease;
    }

    .post-title a:hover {
      color: #bca772 !important;
    }

    a {
      color: #bca772 !important;
      transition: all 0.25s ease;
    }

    a:hover {
      color: #dfc88f !important;
    }

    ::-webkit-scrollbar {
      width: 8px;
    }
    ::-webkit-scrollbar-track {
      background: #111;
    }
    ::-webkit-scrollbar-thumb {
      background: #bca772;
      border-radius: 4px;
    }
  /*]]>*/
  </style>
"""

# 3. HTML Block for Navigation Bar linked to new static pages
sendas_html_block = f"""
            <b:if cond='data:view.isHomepage'>
              <!-- BARRA DE SERVICIOS Y SENDAS DANIEL SIMONS (VERSION v3) -->
              <nav class="ds-sendas-bar">
                <a href="{URL_DESTILADO}" class="ds-senda-item">
                  <span>🧪</span> Destilado de Ideas
                </a>
                <a href="{URL_FORJA}" class="ds-senda-item">
                  <span>🔨</span> Forja de Proyectos
                </a>
                <a href="{URL_MARKETING}" class="ds-senda-item">
                  <span>📈</span> Marketing 360
                </a>
                <a href="{URL_MYPE}" class="ds-senda-item">
                  <span>🚀</span> Impulso MYPE
                </a>
              </nav>

              <div class="ds-section-divider">
                <span>PORTAFOLIO DE ANÁLISIS &amp; TRABAJO INTELECTUAL</span>
                <h2>Últimas Publicaciones &amp; Investigaciones</h2>
              </div>
            </b:if>
"""

# 4. AI Chatbot Widget HTML & JS Block (Linked to Static Pages)
widget_block = f"""
  <style type='text/css'>
  /*<![CDATA[*/
    #ds-ai-widget-container {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 999999;
      font-family: 'Montserrat', sans-serif;
    }}

    #ds-ai-trigger {{
      background: linear-gradient(135deg, #1b365d 0%, #bca772 100%);
      color: #ffffff;
      border: 2px solid #bca772;
      padding: 12px 20px;
      border-radius: 50px;
      cursor: pointer;
      box-shadow: 0 8px 25px rgba(0,0,0,0.6);
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 700;
      font-size: 14px;
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}

    #ds-ai-trigger:hover {{
      transform: scale(1.05);
      box-shadow: 0 12px 30px rgba(188, 167, 114, 0.4);
    }}

    #ds-ai-modal {{
      display: none;
      position: fixed;
      bottom: 90px;
      right: 24px;
      width: 360px;
      max-width: calc(100vw - 48px);
      height: 480px;
      background: rgba(18, 18, 18, 0.95);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(188, 167, 114, 0.4);
      border-radius: 16px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.8);
      flex-direction: column;
      overflow: hidden;
      z-index: 999999;
    }}

    .ds-ai-header {{
      background: #111111;
      padding: 16px;
      border-bottom: 1px solid rgba(188, 167, 114, 0.2);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .ds-ai-header-title {{
      font-size: 15px;
      font-weight: 700;
      color: #bca772;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .ds-ai-close {{
      background: transparent;
      border: none;
      color: #888888;
      font-size: 20px;
      cursor: pointer;
    }}

    .ds-ai-close:hover {{ color: #ffffff; }}

    .ds-ai-body {{
      flex: 1;
      padding: 16px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
      font-size: 13px;
    }}

    .ds-ai-msg {{
      padding: 10px 14px;
      border-radius: 12px;
      line-height: 1.5;
      max-width: 85%;
    }}

    .ds-ai-msg-bot {{
      background: rgba(188, 167, 114, 0.15);
      border: 1px solid rgba(188, 167, 114, 0.3);
      color: #f0f0f0;
      align-self: flex-start;
      border-bottom-left-radius: 2px;
    }}

    .ds-ai-msg-user {{
      background: #1b365d;
      color: #ffffff;
      align-self: flex-end;
      border-bottom-right-radius: 2px;
    }}

    .ds-ai-quick-options {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }}

    .ds-ai-opt-btn {{
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(188, 167, 114, 0.3);
      color: #bca772;
      padding: 6px 10px;
      border-radius: 15px;
      font-size: 11px;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .ds-ai-opt-btn:hover {{
      background: #bca772;
      color: #000000;
    }}

    .ds-ai-footer {{
      padding: 12px;
      border-top: 1px solid rgba(188, 167, 114, 0.2);
      display: flex;
      gap: 8px;
      background: #0a0a0a;
    }}

    .ds-ai-input {{
      flex: 1;
      background: #181818;
      border: 1px solid #333333;
      border-radius: 20px;
      padding: 8px 14px;
      color: #ffffff;
      font-size: 12px;
      outline: none;
    }}

    .ds-ai-input:focus {{ border-color: #bca772; }}

    .ds-ai-send {{
      background: #bca772;
      color: #000000;
      border: none;
      border-radius: 50%;
      width: 34px;
      height: 34px;
      font-weight: bold;
      cursor: pointer;
    }}
  /*]]>*/
  </style>

  <div id="ds-ai-widget-container">
    <button id="ds-ai-trigger" onclick="toggleDsAiModal()">
      <span>💬</span> Asistente IA | Daniel Simons
    </button>

    <div id="ds-ai-modal">
      <div class="ds-ai-header">
        <div class="ds-ai-header-title">
          <span>🤖</span> Consultas &amp; Proyectos 24/7
        </div>
        <button class="ds-ai-close" onclick="toggleDsAiModal()">✕</button>
      </div>

      <div class="ds-ai-body" id="dsAiBody">
        <div class="ds-ai-msg ds-ai-msg-bot">
          ¡Hola! 👋 Soy el asistente de <strong>Daniel Simons</strong>. ¿Qué servicio o proyecto deseas explorar hoy?
        </div>
        
        <div class="ds-ai-quick-options">
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Destilado de Ideas')">🧪 Destilado de Ideas</button>
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Forja de Proyectos')">🔨 Forja de Proyectos</button>
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Marketing 360')">📈 Marketing 360 / MYPE</button>
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Trabajo Intelectual')">🧠 Análisis &amp; Propuestas</button>
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Contacto WhatsApp')">📲 WhatsApp Directo</button>
        </div>
      </div>

      <div class="ds-ai-footer">
        <input type="text" id="dsAiInput" class="ds-ai-input" placeholder="Escribe tu mensaje..." onkeypress="if(event.key==='Enter') sendDsAiUserMsg()"/>
        <button class="ds-ai-send" onclick="sendDsAiUserMsg()">➔</button>
      </div>
    </div>
  </div>

  <script type='text/javascript'>
  //<![CDATA[
    function toggleDsAiModal() {{
      var modal = document.getElementById('ds-ai-modal');
      if (modal.style.display === 'flex') {{
        modal.style.display = 'none';
      }} else {{
        modal.style.display = 'flex';
      }}
    }}

    function addDsAiMessage(text, isUser) {{
      var body = document.getElementById('dsAiBody');
      var msgDiv = document.createElement('div');
      msgDiv.className = 'ds-ai-msg ' + (isUser ? 'ds-ai-msg-user' : 'ds-ai-msg-bot');
      msgDiv.innerHTML = text;
      body.appendChild(msgDiv);
      body.scrollTop = body.scrollHeight;
    }}

    function sendDsAiUserMsg() {{
      var input = document.getElementById('dsAiInput');
      var val = input.value.trim();
      if (!val) return;
      addDsAiMessage(val, true);
      input.value = '';
      processDsAiBotResponse(val);
    }}

    function sendDsAiPreset(topic) {{
      addDsAiMessage(topic, true);
      processDsAiBotResponse(topic);
    }}

    function processDsAiBotResponse(query) {{
      var q = query.toLowerCase();
      var reply = "";

      if (q.indexOf("destilado") !== -1 || q.indexOf("idea") !== -1) {{
        reply = "🧪 <strong>Destilado de Ideas de Negocio:</strong><br/>Proceso de purificación y validación estratégica para proyectos y emprendimientos.<br/><br/><a href='{URL_DESTILADO}' target='_blank' style='color:#bca772; font-weight:bold;'>👉 Ver Página Oficial del Servicio</a>";
      }} else if (q.indexOf("forja") !== -1 || q.indexOf("proyecto") !== -1) {{
        reply = "🔨 <strong>Forja de Emprendimientos:</strong><br/>Estructuración, moldeado y construcción sólida de proyectos productivos.<br/><br/><a href='{URL_FORJA}' target='_blank' style='color:#bca772; font-weight:bold;'>👉 Ver Página Oficial de Forja</a>";
      }} else if (q.indexOf("marketing") !== -1 || q.indexOf("mype") !== -1) {{
        reply = "📈 <strong>Marketing 360° &amp; Impulso MYPE:</strong><br/>Estrategias integrales de crecimiento y aceleración comercial para empresas y PYMEs.<br/><br/><a href='{URL_MARKETING}' target='_blank' style='color:#bca772; font-weight:bold;'>👉 Ver Servicios 360</a>";
      }} else if (q.indexOf("intelectual") !== -1 || q.indexOf("analisis") !== -1 || q.indexOf("politica") !== -1) {{
        reply = "🧠 <strong>Trabajo Intelectual &amp; Análisis:</strong><br/>Ensayos, análisis electoral, propuestas de transparencia y coyuntura económica de Bolivia.<br/><br/><a href='https://www.danielsimons.xyz/2025/06/propuesta-estrategia-integral-para-la.html' target='_blank' style='color:#bca772; font-weight:bold;'>👉 Leer Últimos Análisis</a>";
      }} else {{
        reply = "✨ Gracias por tu interés. Puedes escribirle a Daniel Simons de forma directa a su WhatsApp personal:<br/><br/><a href='https://api.whatsapp.com/send?phone=59178000000&amp;text=Hola%20Daniel,%20quisiera%20consultarte%20sobre%20un%20proyecto' target='_blank' style='background:#bca772; color:#000!important; padding:8px 16px; border-radius:20px; text-decoration:none; font-weight:bold; font-size:12px; display:inline-block; margin-top:6px;'>📲 WhatsApp Directo</a>";
      }}

      setTimeout(function() {{
        addDsAiMessage(reply, false);
      }}, 500);
    }}
  //]]>
  </script>
"""

# Inject into XML
head_pos = xml_content.find("</head>")
if head_pos != -1:
    xml_content = xml_content[:head_pos] + seo_block + css_block + xml_content[head_pos:]

main_target = "<main class='centered-bottom' id='main' role='main' tabindex='-1'>"
main_pos = xml_content.find(main_target)
if main_pos != -1:
    insert_at = main_pos + len(main_target)
    xml_content = xml_content[:insert_at] + "\n" + sendas_html_block + xml_content[insert_at:]

body_pos = xml_content.find("</body>")
if body_pos != -1:
    xml_content = xml_content[:body_pos] + widget_block + xml_content[body_pos:]

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

# Validate XML parsing
try:
    ET.parse(output_path)
    print("SUCCESS: v3_theme_optimizado.xml passed strict XML parsing test!")
except Exception as e:
    print("XML ERROR:", e)
