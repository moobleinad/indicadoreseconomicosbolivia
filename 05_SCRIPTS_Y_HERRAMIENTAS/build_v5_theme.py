import os
import xml.etree.ElementTree as ET

source_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\copia de seguridad del tema web\theme-433667097766389126.xml"
output_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado"
output_path = os.path.join(output_dir, "v5_theme_optimizado.xml")

os.makedirs(output_dir, exist_ok=True)

with open(source_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# Live Page URLs created on Blogger:
URL_DESTILADO = "https://www.danielsimons.xyz/p/destilado-de-ideas-de-negocio_0599447061.html"
URL_FORJA = "https://www.danielsimons.xyz/p/forja-disciplina-habitos-y-lucidez.html"
URL_MARKETING = "https://www.danielsimons.xyz/p/marketing-360.html"
URL_MYPE = "https://www.danielsimons.xyz/p/impulso-mype-360.html"
URL_MFEIR = "https://www.danielsimons.xyz/p/liberalismo-vs-socialismo.html"
URL_TODAS_PUBLICACIONES = "https://www.danielsimons.xyz/search"

# 1. SEO & Open Graph Meta Tags
seo_block = """
  <!-- OPTIMIZACION SEO Y META TAGS OPEN GRAPH (VERSION v5) -->
  <b:if cond='data:view.isSingleItem'>
    <meta expr:content='data:view.title.escaped + " | Daniel Simons"' property='og:title'/>
    <meta expr:content='data:view.title.escaped + " | Daniel Simons"' name='twitter:title'/>
    <b:if cond='data:view.description'>
      <meta expr:content='data:view.description' name='description'/>
      <meta expr:content='data:view.description' property='og:description'/>
      <meta expr:content='data:view.description' name='twitter:description'/>
    <b:else/>
      <meta expr:content='data:view.title.escaped + " - De ideas complejas a resultados concretos por Daniel Simons."' name='description'/>
      <meta expr:content='data:view.title.escaped + " - De ideas complejas a resultados concretos por Daniel Simons."' property='og:description'/>
      <meta expr:content='data:view.title.escaped + " - De ideas complejas a resultados concretos por Daniel Simons."' name='twitter:description'/>
    </b:if>
    <meta content='article' property='og:type'/>
  <b:else/>
    <meta content='Daniel Simons | De ideas complejas a resultados concretos' property='og:title'/>
    <meta content='Daniel Simons | De ideas complejas a resultados concretos' name='twitter:title'/>
    <meta content='Portal oficial de Daniel Simons. Estructurador de ideas complejas, Forja de Proyectos, Destilado de Conocimiento, Modelo MFEIR y Observatorio Económico.' name='description'/>
    <meta content='Portal oficial de Daniel Simons. Estructurador de ideas complejas, Forja de Proyectos, Destilado de Conocimiento, Modelo MFEIR y Observatorio Económico.' property='og:description'/>
    <meta content='Portal oficial de Daniel Simons. Estructurador de ideas complejas, Forja de Proyectos, Destilado de Conocimiento, Modelo MFEIR y Observatorio Económico.' name='twitter:description'/>
    <meta content='website' property='og:type'/>
  </b:if>
  
  <meta content='Daniel Simons' name='author'/>
  <meta content='Daniel Simons' property='og:site_name'/>
  <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
  <meta content='summary_large_image' name='twitter:card'/>
  <meta content='index, follow, max-image-preview:large' name='robots'/>
"""

# 2. Enhanced CSS Block for v5
css_block = f"""
  <style type='text/css'>
  /*<![CDATA[*/
    html, body, .page_body, .centered-top-container, .centered-top-placeholder, 
    #main, .centered-bottom, .post, .post-outer, .post-outer-container, 
    .post-body, .hero-image, .bg-photo, .page {{
      background-color: #000000 !important;
      background: #000000 !important;
      color: #e0e0e0 !important;
      font-family: 'Montserrat', sans-serif !important;
    }}

    .sidebar-container, .sidebar-back, #sidebar-left, .hamburger-menu-container {{
      display: none !important;
    }}

    #main, .page, .centered-bottom, .post-outer-container {{
      width: 100% !important;
      max-width: 1200px !important;
      margin: 0 auto !important;
      float: none !important;
      left: 0 !important;
      box-sizing: border-box !important;
    }}

    .ds-hero-section {{
      margin: 30px 0 40px 0;
    }}

    .ds-main-title {{
      text-align: center;
      margin-bottom: 25px;
    }}

    .ds-main-title h2 {{
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 1px;
    }}

    .ds-main-title span {{
      color: #bca772;
    }}

    .ds-two-cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
    }}

    .ds-hero-card {{
      background: #0c0c0c;
      border: 1px solid rgba(188, 167, 114, 0.35);
      border-radius: 12px;
      padding: 30px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.3s ease;
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }}

    .ds-hero-card:hover {{
      border-color: #bca772;
      transform: translateY(-4px);
    }}

    .ds-card-title {{
      font-size: 28px;
      font-weight: 800;
      color: #bca772;
      margin-bottom: 8px;
    }}

    .ds-card-subtitle {{
      font-size: 13px;
      color: #aaaaaa;
      margin-bottom: 18px;
    }}

    .ds-card-bullet-list {{
      list-style: none;
      margin-bottom: 25px;
    }}

    .ds-card-bullet-list li {{
      font-size: 13px;
      color: #dddddd;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .ds-btn-gold {{
      display: inline-block;
      background: linear-gradient(135deg, #bca772 0%, #997a15 100%);
      color: #000000 !important;
      font-weight: 800;
      font-size: 12px;
      padding: 12px 24px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 1px;
      text-decoration: none !important;
      align-self: flex-start;
    }}

    .ds-btn-blue {{
      display: inline-block;
      background: linear-gradient(135deg, #1b365d 0%, #102442 100%);
      border: 1px solid #4a7bb0;
      color: #ffffff !important;
      font-weight: 800;
      font-size: 12px;
      padding: 12px 24px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 1px;
      text-decoration: none !important;
      align-self: flex-start;
    }}

    .ds-carousel-wrapper {{
      display: flex;
      gap: 16px;
      overflow-x: auto;
      padding: 10px 0 20px 0;
      margin-bottom: 40px;
      scrollbar-width: thin;
      scrollbar-color: #bca772 #111;
    }}

    .ds-pill-card {{
      min-width: 210px;
      background: #0a0a0a;
      border: 1px solid #222222;
      border-radius: 10px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 8px;
      transition: all 0.3s;
    }}

    .ds-pill-card:hover {{
      border-color: #bca772;
      background: #111111;
    }}

    .ds-pill-num {{
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #bca772;
      color: #000;
      font-weight: 800;
      font-size: 11px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .ds-pill-title {{
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
    }}

    .ds-pill-desc {{
      font-size: 11px;
      color: #888888;
    }}

    .ds-posts-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba(188, 167, 114, 0.2);
    }}

    .ds-posts-header h2 {{
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      text-transform: uppercase;
    }}

    .ds-posts-header h2 span {{
      color: #bca772;
    }}

    .ds-ver-todas-btn {{
      font-size: 12px;
      font-weight: 700;
      color: #bca772 !important;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      text-decoration: none !important;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: color 0.3s;
    }}

    .ds-ver-todas-btn:hover {{
      color: #ffffff !important;
    }}
  /*]]>*/
  </style>
"""

# 3. HTML Block for Front Page (Literal utf-8 arrow)
frontpage_html_block = f"""
            <b:if cond='data:view.isHomepage'>
              <!-- SECCIÓN: ¿CÓMO PUEDO AYUDARTE? -->
              <section class="ds-hero-section">
                <div class="ds-main-title">
                  <h2>¿CÓMO PUEDO <span>AYUDARTE?</span></h2>
                </div>

                <div class="ds-two-cards-grid">
                  <!-- TARJETA FORJA -->
                  <div class="ds-hero-card">
                    <div>
                      <div class="ds-card-title">FORJA</div>
                      <div class="ds-card-subtitle">Convertimos <strong>ideas</strong> en proyectos, negocios y estrategias.</div>
                      <ul class="ds-card-bullet-list">
                        <li>🚀 Emprendimiento &amp; Modelos de negocio</li>
                        <li>💡 Innovación &amp; Diseño de proyectos</li>
                        <li>🛡️ Validación y estrategia</li>
                        <li>👥 Acompañamiento integral</li>
                      </ul>
                    </div>
                    <a href="{URL_FORJA}" class="ds-btn-gold">TRABAJEMOS JUNTOS &#10140;</a>
                  </div>

                  <!-- TARJETA DESTILADO -->
                  <div class="ds-hero-card">
                    <div>
                      <div class="ds-card-title">DESTILADO</div>
                      <div class="ds-card-subtitle">Convertimos <strong>complejidad</strong> en claridad absoluta.</div>
                      <ul class="ds-card-bullet-list">
                        <li>🔍 Investigación y análisis</li>
                        <li>✍️ Redacción y síntesis estratégica</li>
                        <li>📚 Libros, guías e informes técnicos</li>
                        <li>⭐ Contenido de alto valor</li>
                      </ul>
                    </div>
                    <a href="{URL_DESTILADO}" class="ds-btn-blue">SOLICITAR PROYECTO &#10140;</a>
                  </div>
                </div>
              </section>

              <!-- SECCIÓN: IDEAS QUE EXPLORO Y CONSTRUYO (CARRUSEL) -->
              <section>
                <div class="ds-main-title">
                  <h2>IDEAS QUE <span>EXPLORO Y CONSTRUYO</span></h2>
                </div>

                <div class="ds-carousel-wrapper">
                  <div class="ds-pill-card">
                    <div class="ds-pill-num">1</div>
                    <div class="ds-pill-title">FORJA</div>
                    <div class="ds-pill-desc">De la idea a la ejecución.</div>
                  </div>
                  <div class="ds-pill-card">
                    <div class="ds-pill-num">2</div>
                    <div class="ds-pill-title">DESTILADO</div>
                    <div class="ds-pill-desc">Del conocimiento a la claridad.</div>
                  </div>
                  <div class="ds-pill-card">
                    <div class="ds-pill-num">3</div>
                    <div class="ds-pill-title">MFEIR / MEDS</div>
                    <div class="ds-pill-desc">Individualidades Relacionales.</div>
                  </div>
                  <div class="ds-pill-card">
                    <div class="ds-pill-num">4</div>
                    <div class="ds-pill-title">FILOSOFÍA DEL JUEGO</div>
                    <div class="ds-pill-desc">Investigación aplicada.</div>
                  </div>
                  <div class="ds-pill-card">
                    <div class="ds-pill-num">5</div>
                    <div class="ds-pill-title">LABORATORIO</div>
                    <div class="ds-pill-desc">Colabora y construye.</div>
                  </div>
                </div>
              </section>

              <!-- SECCIÓN: PUBLICACIONES DESTACADAS CON BOTÓN VER TODAS -->
              <section>
                <div class="ds-posts-header">
                  <h2>PUBLICACIONES <span>DESTACADAS</span></h2>
                  <a href="{URL_TODAS_PUBLICACIONES}" class="ds-ver-todas-btn">
                    VER TODAS LAS PUBLICACIONES &#10140;
                  </a>
                </div>
              </section>
            </b:if>
"""

# Inject into XML
head_pos = xml_content.find("</head>")
if head_pos != -1:
    xml_content = xml_content[:head_pos] + seo_block + css_block + xml_content[head_pos:]

main_target = "<main class='centered-bottom' id='main' role='main' tabindex='-1'>"
main_pos = xml_content.find(main_target)
if main_pos != -1:
    insert_at = main_pos + len(main_target)
    xml_content = xml_content[:insert_at] + "\n" + frontpage_html_block + xml_content[insert_at:]

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(output_path)
    print("SUCCESS: v5_theme_optimizado.xml created and passed XML test!")
except Exception as e:
    print("XML ERROR:", e)
