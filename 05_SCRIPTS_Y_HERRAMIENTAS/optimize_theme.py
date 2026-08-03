import os
import xml.etree.ElementTree as ET

source_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\copia de seguridad del tema web\theme-433667097766389126.xml"
output_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado"
output_path = os.path.join(output_dir, "theme_optimizado_danielsimons.xml")

os.makedirs(output_dir, exist_ok=True)

with open(source_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# 1. SEO & Open Graph Meta Tags
seo_block = """
  <!-- OPTIMIZACION SEO Y META TAGS OPEN GRAPH DE BLOGGER -->
  <b:if cond='data:view.isSingleItem'>
    <meta expr:content='data:view.title.escaped' property='og:title'/>
    <meta expr:content='data:view.title.escaped' name='twitter:title'/>
    <b:if cond='data:view.description'>
      <meta expr:content='data:view.description' name='description'/>
      <meta expr:content='data:view.description' property='og:description'/>
      <meta expr:content='data:view.description' name='twitter:description'/>
    <b:else/>
      <meta expr:content='data:view.title.escaped' name='description'/>
      <meta expr:content='data:view.title.escaped' property='og:description'/>
      <meta expr:content='data:view.title.escaped' name='twitter:description'/>
    </b:if>
    <meta content='article' property='og:type'/>
  <b:else/>
    <meta content='Daniel Simons | Consultoría Estratégica, Campaña Electoral 2026, Branding e IA' property='og:title'/>
    <meta content='Daniel Simons | Consultoría Estratégica, Campaña Electoral 2026, Branding e IA' name='twitter:title'/>
    <meta content='Portal oficial de Daniel Simons. Servicios de consultoría estratégica en Santa Cruz Bolivia, estrategia para campaña electoral 2026, evaluación de marca, guía de tesis con GPT Tutor y transparencia inteligente.' name='description'/>
    <meta content='Portal oficial de Daniel Simons. Servicios de consultoría estratégica en Santa Cruz Bolivia, estrategia para campaña electoral 2026, evaluación de marca, guía de tesis con GPT Tutor y transparencia inteligente.' property='og:description'/>
    <meta content='Portal oficial de Daniel Simons. Servicios de consultoría estratégica en Santa Cruz Bolivia, estrategia para campaña electoral 2026, evaluación de marca, guía de tesis con GPT Tutor y transparencia inteligente.' name='twitter:description'/>
    <meta content='website' property='og:type'/>
  </b:if>
  
  <meta content='Daniel Simons' name='author'/>
  <meta content='Daniel Simons' property='og:site_name'/>
  <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
  <meta content='summary_large_image' name='twitter:card'/>
  <meta content='index, follow, max-image-preview:large' name='robots'/>
  <meta content='consultoria estrategica, santa cruz bolivia, campaña electoral 2026, desarrollo de marca, inteligencia artificial, gpt tutor tesis, daniel simons' name='keywords'/>
"""

# 2. Enhanced CSS Block (Includes Hero & Service Cards Layout)
css_block = """
  <style type='text/css'>
  /*<![CDATA[*/
    body {
      color: #e6e6e6 !important;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
      background-color: #0d0d0d !important;
    }
    
    .post-body, .post-body p {
      font-size: 19px !important;
      line-height: 1.75 !important;
      color: #e0e0e0 !important;
      letter-spacing: 0.2px;
    }

    .post-title, .post-title a {
      color: #ffffff !important;
      font-family: 'Montserrat', sans-serif !important;
      font-weight: 700 !important;
      letter-spacing: 0.5px;
      transition: color 0.3s ease;
    }

    .post-title a:hover {
      color: #bca772 !important;
    }

    a {
      color: #bca772 !important;
      transition: all 0.25s ease-in-out;
    }

    a:hover {
      color: #dfc88f !important;
      text-shadow: 0 0 8px rgba(188, 167, 114, 0.4);
    }

    .btn-ds-cta {
      display: inline-block;
      background: linear-gradient(135deg, #bca772 0%, #997a15 100%);
      color: #000000 !important;
      font-family: 'Montserrat', sans-serif;
      font-weight: 700;
      font-size: 14px;
      padding: 12px 24px;
      border-radius: 30px;
      text-transform: uppercase;
      letter-spacing: 1px;
      box-shadow: 0 4px 15px rgba(188, 167, 114, 0.3);
      text-decoration: none !important;
      margin: 10px 5px 10px 0;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .btn-ds-cta:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(188, 167, 114, 0.5);
      color: #000000 !important;
    }

    /* ESTILOS DE LA MAQUETA DE INICIO (HERO + SERVICIOS) */
    .ds-hero {
      background: linear-gradient(180deg, #12161f 0%, #0d0d0d 100%);
      border-bottom: 1px solid rgba(188, 167, 114, 0.2);
      padding: 50px 20px;
      text-align: center;
      position: relative;
      overflow: hidden;
      margin-bottom: 40px;
      border-radius: 12px;
    }

    .ds-hero-badge {
      display: inline-block;
      background: rgba(188, 167, 114, 0.15);
      border: 1px solid rgba(188, 167, 114, 0.4);
      color: #bca772;
      font-family: 'Montserrat', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 2px;
      padding: 6px 16px;
      border-radius: 20px;
      margin-bottom: 16px;
      text-transform: uppercase;
    }

    .ds-hero-title {
      font-family: 'Montserrat', sans-serif;
      font-size: 38px;
      font-weight: 800;
      color: #ffffff;
      margin-bottom: 12px;
      line-height: 1.2;
    }

    .ds-hero-title span {
      background: linear-gradient(135deg, #bca772 0%, #e6d3a3 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .ds-hero-subtitle {
      font-size: 16px;
      color: #aaaaaa;
      max-width: 700px;
      margin: 0 auto 26px auto;
      letter-spacing: 1px;
      text-transform: uppercase;
      font-weight: 300;
    }

    .ds-hero-buttons {
      display: flex;
      justify-content: center;
      gap: 16px;
      flex-wrap: wrap;
    }

    .ds-btn-gold {
      background: linear-gradient(135deg, #bca772 0%, #997a15 100%);
      color: #000000 !important;
      font-family: 'Montserrat', sans-serif;
      font-weight: 700;
      font-size: 13px;
      padding: 12px 24px;
      border-radius: 30px;
      text-transform: uppercase;
      letter-spacing: 1px;
      text-decoration: none;
      box-shadow: 0 6px 20px rgba(188, 167, 114, 0.35);
      transition: all 0.3s ease;
    }

    .ds-btn-gold:hover {
      transform: translateY(-2px);
      box-shadow: 0 10px 25px rgba(188, 167, 114, 0.5);
    }

    .ds-btn-outline {
      background: transparent;
      color: #ffffff !important;
      border: 1px solid rgba(255, 255, 255, 0.3);
      font-family: 'Montserrat', sans-serif;
      font-weight: 600;
      font-size: 13px;
      padding: 12px 24px;
      border-radius: 30px;
      text-transform: uppercase;
      letter-spacing: 1px;
      text-decoration: none;
      transition: all 0.3s ease;
    }

    .ds-btn-outline:hover {
      border-color: #bca772;
      color: #bca772 !important;
      background: rgba(188, 167, 114, 0.05);
    }

    .ds-services {
      padding: 20px 0 50px 0;
    }

    .ds-section-header {
      text-align: center;
      margin-bottom: 40px;
    }

    .ds-tag {
      color: #bca772;
      font-family: 'Montserrat', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
    }

    .ds-section-header h2 {
      font-family: 'Montserrat', sans-serif;
      font-size: 28px;
      font-weight: 700;
      color: #ffffff;
      margin: 6px 0 10px 0;
    }

    .ds-section-header p {
      color: #999999;
      font-size: 15px;
      max-width: 600px;
      margin: 0 auto;
    }

    .ds-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 20px;
    }

    .ds-card {
      background: #14161d;
      border: 1px solid rgba(188, 167, 114, 0.2);
      border-radius: 14px;
      padding: 24px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.3s ease;
    }

    .ds-card:hover {
      transform: translateY(-5px);
      border-color: #bca772;
      box-shadow: 0 10px 25px rgba(0,0,0,0.7), 0 0 12px rgba(188, 167, 114, 0.2);
    }

    .ds-card-icon {
      width: 48px;
      height: 48px;
      background: rgba(188, 167, 114, 0.1);
      border: 1px solid rgba(188, 167, 114, 0.3);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
      margin-bottom: 16px;
    }

    .ds-card h3 {
      font-family: 'Montserrat', sans-serif;
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 10px;
    }

    .ds-card p {
      color: #bbbbbb;
      font-size: 13.5px;
      line-height: 1.5;
      margin-bottom: 20px;
    }

    .ds-card-link {
      color: #bca772 !important;
      font-family: 'Montserrat', sans-serif;
      font-weight: 700;
      font-size: 12px;
      text-decoration: none;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      display: inline-block;
    }

    .ds-card-link:hover {
      color: #dfc88f !important;
    }

    .ds-articles-title-box {
      border-top: 1px dashed rgba(188, 167, 114, 0.3);
      padding-top: 40px;
      margin-top: 40px;
      text-align: center;
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

# 3. HTML Block for Homepage Hero & Services
homepage_html_block = """
            <b:if cond='data:view.isHomepage'>
              <!-- HERO BANNER & SERVICIOS IMPACTANTES (by Antigravity AI) -->
              <section class="ds-hero">
                <span class="ds-hero-badge">CONSULTORÍA ESTRATÉGICA &amp; ANÁLISIS DE DATOS</span>
                <h1 class="ds-hero-title">De ideas complejas a <span>estructuras claras</span></h1>
                <p class="ds-hero-subtitle">Estructura • Integración • Conceptualización</p>
                <div class="ds-hero-buttons">
                  <a href="#servicios-ds" class="ds-btn-gold">Explorar Servicios</a>
                  <a href="https://api.whatsapp.com/send?phone=59178000000&amp;text=Hola%20Daniel,%20quisiera%20una%20consultoria" target="_blank" class="ds-btn-outline">Contacto Directo</a>
                </div>
              </section>

              <section id="servicios-ds" class="ds-services">
                <div class="ds-section-header">
                  <span class="ds-tag">PROPUESTAS &amp; SERVICIOS</span>
                  <h2>Áreas de Especialización</h2>
                  <p>Soluciones personalizadas en estrategia política, evaluación corporativa e Inteligencia Artificial.</p>
                </div>

                <div class="ds-grid">
                  <div class="ds-card">
                    <div>
                      <div class="ds-card-icon">🏛️</div>
                      <h3>Campaña Electoral Santa Cruz 2026</h3>
                      <p>Estrategia integral, análisis de datos electorales y posicionamiento territorial de candidatos.</p>
                    </div>
                    <a href="/2025/06/propuesta-estrategia-integral-para-la.html" class="ds-card-link">Ver Propuesta Electoral ➔</a>
                  </div>

                  <div class="ds-card">
                    <div>
                      <div class="ds-card-icon">📊</div>
                      <h3>Evaluación &amp; Desarrollo de Marca</h3>
                      <p>Diagnóstico de madurez de marca empresarial, estrategia 360° e identidad corporativa.</p>
                    </div>
                    <a href="/2025/11/evaluar-mi-marca-online.html" class="ds-card-link">Solicitar Evaluación ➔</a>
                  </div>

                  <div class="ds-card">
                    <div>
                      <div class="ds-card-icon">🎓</div>
                      <h3>Guía de Tesis &amp; GPT Tutor IA</h3>
                      <p>Metodología estructurada y asistente interactivo con IA para la redacción y defensa de tesis.</p>
                    </div>
                    <a href="/2025/11/guia-de-supervivencia-la-tesis-doma-y.html" class="ds-card-link">Acceder al Tutor GPT ➔</a>
                  </div>

                  <div class="ds-card">
                    <div>
                      <div class="ds-card-icon">🏢</div>
                      <h3>Transparencia &amp; Urbanizaciones</h3>
                      <p>Estrategias de transparencia inteligente y valor agregado para proyectos inmobiliarios.</p>
                    </div>
                    <a href="/2025/11/propuesta-transparencia-inteligente.html" class="ds-card-link">Ver Brochure / Oferta ➔</a>
                  </div>
                </div>

                <div class="ds-articles-title-box">
                  <span class="ds-tag">IDEAS &amp; TENDENCIAS</span>
                  <h2 style="font-family:'Montserrat', sans-serif; color:#ffffff; margin-top:8px;">Últimos Análisis &amp; Publicaciones</h2>
                </div>
              </section>
            </b:if>
"""

# 4. AI Chatbot Widget HTML & JS Block (XML safe with CDATA)
widget_block = """
  <style type='text/css'>
  /*<![CDATA[*/
    #ds-ai-widget-container {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 999999;
      font-family: 'Montserrat', sans-serif;
    }

    #ds-ai-trigger {
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
    }

    #ds-ai-trigger:hover {
      transform: scale(1.05);
      box-shadow: 0 12px 30px rgba(188, 167, 114, 0.4);
    }

    #ds-ai-modal {
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
    }

    .ds-ai-header {
      background: #111111;
      padding: 16px;
      border-bottom: 1px solid rgba(188, 167, 114, 0.2);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .ds-ai-header-title {
      font-size: 15px;
      font-weight: 700;
      color: #bca772;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .ds-ai-close {
      background: transparent;
      border: none;
      color: #888888;
      font-size: 20px;
      cursor: pointer;
    }

    .ds-ai-close:hover { color: #ffffff; }

    .ds-ai-body {
      flex: 1;
      padding: 16px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
      font-size: 13px;
    }

    .ds-ai-msg {
      padding: 10px 14px;
      border-radius: 12px;
      line-height: 1.5;
      max-width: 85%;
    }

    .ds-ai-msg-bot {
      background: rgba(188, 167, 114, 0.15);
      border: 1px solid rgba(188, 167, 114, 0.3);
      color: #f0f0f0;
      align-self: flex-start;
      border-bottom-left-radius: 2px;
    }

    .ds-ai-msg-user {
      background: #1b365d;
      color: #ffffff;
      align-self: flex-end;
      border-bottom-right-radius: 2px;
    }

    .ds-ai-quick-options {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }

    .ds-ai-opt-btn {
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(188, 167, 114, 0.3);
      color: #bca772;
      padding: 6px 10px;
      border-radius: 15px;
      font-size: 11px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .ds-ai-opt-btn:hover {
      background: #bca772;
      color: #000000;
    }

    .ds-ai-footer {
      padding: 12px;
      border-top: 1px solid rgba(188, 167, 114, 0.2);
      display: flex;
      gap: 8px;
      background: #0a0a0a;
    }

    .ds-ai-input {
      flex: 1;
      background: #181818;
      border: 1px solid #333333;
      border-radius: 20px;
      padding: 8px 14px;
      color: #ffffff;
      font-size: 12px;
      outline: none;
    }

    .ds-ai-input:focus { border-color: #bca772; }

    .ds-ai-send {
      background: #bca772;
      color: #000000;
      border: none;
      border-radius: 50%;
      width: 34px;
      height: 34px;
      font-weight: bold;
      cursor: pointer;
    }
  /*]]>*/
  </style>

  <div id="ds-ai-widget-container">
    <button id="ds-ai-trigger" onclick="toggleDsAiModal()">
      <span>💬</span> Asistente IA | Daniel Simons
    </button>

    <div id="ds-ai-modal">
      <div class="ds-ai-header">
        <div class="ds-ai-header-title">
          <span>🤖</span> Consultas &amp; Propuestas 24/7
        </div>
        <button class="ds-ai-close" onclick="toggleDsAiModal()">✕</button>
      </div>

      <div class="ds-ai-body" id="dsAiBody">
        <div class="ds-ai-msg ds-ai-msg-bot">
          ¡Hola! 👋 Soy el asistente virtual de <strong>Daniel Simons</strong>. ¿En qué propuesta o servicio estás interesado hoy?
        </div>
        
        <div class="ds-ai-quick-options">
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Campaña Electoral 2026')">🏛️ Campaña Santa Cruz 2026</button>
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Desarrollo de Marca')">📊 Evaluar mi Marca</button>
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Guia de Tesis GPT')">🎓 Guía de Tesis / GPT Tutor</button>
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Transparencia e Inmobiliaria')">🏢 Propuesta Inmobiliaria</button>
          <button class="ds-ai-opt-btn" onclick="sendDsAiPreset('Contacto WhatsApp')">📲 WhatsApp Directo</button>
        </div>
      </div>

      <div class="ds-ai-footer">
        <input type="text" id="dsAiInput" class="ds-ai-input" placeholder="Escribe tu consulta..." onkeypress="if(event.key==='Enter') sendDsAiUserMsg()"/>
        <button class="ds-ai-send" onclick="sendDsAiUserMsg()">➔</button>
      </div>
    </div>
  </div>

  <script type='text/javascript'>
  //<![CDATA[
    function toggleDsAiModal() {
      var modal = document.getElementById('ds-ai-modal');
      if (modal.style.display === 'flex') {
        modal.style.display = 'none';
      } else {
        modal.style.display = 'flex';
      }
    }

    function addDsAiMessage(text, isUser) {
      var body = document.getElementById('dsAiBody');
      var msgDiv = document.createElement('div');
      msgDiv.className = 'ds-ai-msg ' + (isUser ? 'ds-ai-msg-user' : 'ds-ai-msg-bot');
      msgDiv.innerHTML = text;
      body.appendChild(msgDiv);
      body.scrollTop = body.scrollHeight;
    }

    function sendDsAiUserMsg() {
      var input = document.getElementById('dsAiInput');
      var val = input.value.trim();
      if (!val) return;
      addDsAiMessage(val, true);
      input.value = '';
      processDsAiBotResponse(val);
    }

    function sendDsAiPreset(topic) {
      addDsAiMessage(topic, true);
      processDsAiBotResponse(topic);
    }

    function processDsAiBotResponse(query) {
      var q = query.toLowerCase();
      var reply = "";

      if (q.indexOf("campaña") !== -1 || q.indexOf("electoral") !== -1 || q.indexOf("santa cruz") !== -1 || q.indexOf("2026") !== -1) {
        reply = "🏛️ <strong>Estrategia Electoral 2026 (Santa Cruz):</strong><br/>Ofrecemos una solución integral de análisis de datos electorales, posicionamiento de candidatos y estrategia digital.<br/><br/><a href='https://www.danielsimons.xyz/2025/06/propuesta-estrategia-integral-para-la.html' target='_blank' style='color:#bca772; font-weight:bold;'>👉 Ver Propuesta Electoral Completa</a>";
      } else if (q.indexOf("marca") !== -1 || q.indexOf("empresa") !== -1 || q.indexOf("branding") !== -1) {
        reply = "📊 <strong>Desarrollo y Evaluación de Marca:</strong><br/>Auditamos la madurez de tu marca corporativa y diseñamos estrategias de posicionamiento 360°.<br/><br/><a href='https://www.danielsimons.xyz/2025/11/evaluar-mi-marca-online.html' target='_blank' style='color:#bca772; font-weight:bold;'>👉 Solicitar Evaluación de Marca</a>";
      } else if (q.indexOf("tesis") !== -1 || q.indexOf("gpt") !== -1 || q.indexOf("tutor") !== -1) {
        reply = "🎓 <strong>Guía Sobreviviendo a la Tesis &amp; GPT Tutor:</strong><br/>Aprende a domar monstruos metodológicos con nuestra guía y asistencia interactiva de IA.<br/><br/><a href='https://www.danielsimons.xyz/2025/11/guia-de-supervivencia-la-tesis-doma-y.html' target='_blank' style='color:#bca772; font-weight:bold;'>👉 Acceder al GPT Tutor &amp; Libro</a>";
      } else if (q.indexOf("inmobiliaria") !== -1 || q.indexOf("urbanizacion") !== -1 || q.indexOf("transparencia") !== -1) {
        reply = "🏢 <strong>Transparencia e Inmobiliaria:</strong><br/>Propuestas de valor para urbanizaciones y transparencia de gestión inteligente.<br/><br/><a href='https://www.danielsimons.xyz/2025/11/propuesta-transparencia-inteligente.html' target='_blank' style='color:#bca772; font-weight:bold;'>👉 Descargar Brochure / Ver Oferta</a>";
      } else {
        reply = "✨ Gracias por tu mensaje. Para una atención inmediata y personalizada con Daniel Simons, puedes escribirnos directamente a WhatsApp:<br/><br/><a href='https://api.whatsapp.com/send?phone=59178000000&amp;text=Hola%20Daniel,%20quisiera%20mas%20informacion' target='_blank' class='btn-ds-cta' style='color:#000!important; padding:8px 16px; font-size:12px;'>📲 Contactar por WhatsApp</a>";
      }

      setTimeout(function() {
        addDsAiMessage(reply, false);
      }, 500);
    }
  //]]>
  </script>
"""

# Inject into XML
# 1. Inject SEO & CSS inside <head> before </head>
head_pos = xml_content.find("</head>")
if head_pos != -1:
    xml_content = xml_content[:head_pos] + seo_block + css_block + xml_content[head_pos:]

# 2. Inject Homepage Hero & Services inside <main ...> right after <main class='centered-bottom' ...>
main_target = "<main class='centered-bottom' id='main' role='main' tabindex='-1'>"
main_pos = xml_content.find(main_target)
if main_pos != -1:
    insert_at = main_pos + len(main_target)
    xml_content = xml_content[:insert_at] + "\n" + homepage_html_block + xml_content[insert_at:]

# 3. Inject Widget right before </body>
body_pos = xml_content.find("</body>")
if body_pos != -1:
    xml_content = xml_content[:body_pos] + widget_block + xml_content[body_pos:]

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

# Validate XML parsing
try:
    ET.parse(output_path)
    print("SUCCESS: Optimized XML passed strict XML parsing test!")
except Exception as e:
    print("XML ERROR:", e)
