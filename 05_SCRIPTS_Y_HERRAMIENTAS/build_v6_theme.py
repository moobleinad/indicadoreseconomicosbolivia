import os
import xml.etree.ElementTree as ET

source_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\copia de seguridad del tema web\theme-433667097766389126.xml"
output_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado"
output_path = os.path.join(output_dir, "v6_theme_optimizado.xml")

os.makedirs(output_dir, exist_ok=True)

with open(source_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# Live Page URLs created on Blogger:
URL_DESTILADO = "https://www.danielsimons.xyz/p/destilado-de-ideas-de-negocio_0599447061.html"
URL_FORJA = "https://www.danielsimons.xyz/p/forja-disciplina-habitos-y-lucidez.html"
URL_MARKETING = "https://www.danielsimons.xyz/p/marketing-360.html"
URL_MYPE = "https://www.danielsimons.xyz/p/impulso-mype-360.html"
URL_JUEGO = "https://www.danielsimons.xyz/p/el-juego-del-emprendedor-libro-para.html"
URL_MFEIR = "https://www.danielsimons.xyz/p/liberalismo-vs-socialismo.html"
URL_TODAS_PUBLICACIONES = "https://www.danielsimons.xyz/search"

# 1. SEO & Open Graph Meta Tags
seo_block = """
  <!-- OPTIMIZACION SEO Y META TAGS OPEN GRAPH (VERSION v6) -->
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

# 2. Enhanced CSS Block for v6 (6 per row on PC, 2 per row on Mobile)
css_block = """
  <style type='text/css'>
  /*<![CDATA[*/
    html, body, .page_body, .centered-top-container, .centered-top-placeholder, 
    #main, .centered-bottom, .post, .post-outer, .post-outer-container, 
    .post-body, .hero-image, .bg-photo, .page {
      background-color: #000000 !important;
      background: #000000 !important;
      color: #e0e0e0 !important;
      font-family: 'Montserrat', sans-serif !important;
    }

    .sidebar-container, .sidebar-back, #sidebar-left, .hamburger-menu-container {
      display: none !important;
    }

    #main, .page, .centered-bottom, .post-outer-container {
      width: 100% !important;
      max-width: 1240px !important;
      margin: 0 auto !important;
      float: none !important;
      left: 0 !important;
      box-sizing: border-box !important;
    }

    .ds-section-block {
      margin: 35px 0;
    }

    .ds-section-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba(188, 167, 114, 0.25);
    }

    .ds-section-header h2 {
      font-size: 20px;
      font-weight: 800;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .ds-section-header h2 span {
      color: #bca772;
    }

    .ds-section-link {
      font-size: 12px;
      font-weight: 700;
      color: #bca772 !important;
      text-transform: uppercase;
      text-decoration: none !important;
      transition: color 0.3s;
    }

    .ds-section-link:hover {
      color: #ffffff !important;
    }

    /* GRID RESPONSIVO: 6 COLUMNAS EN PC, 2 COLUMNAS EN CELULAR */
    @media (min-width: 992px) {
      .ds-grid-6 {
        display: grid !important;
        grid-template-columns: repeat(6, 1fr) !important;
        gap: 16px !important;
      }
      .blog-posts {
        display: grid !important;
        grid-template-columns: repeat(6, 1fr) !important;
        gap: 16px !important;
      }
    }

    @media (max-width: 991px) and (min-width: 600px) {
      .ds-grid-6, .blog-posts {
        display: grid !important;
        grid-template-columns: repeat(3, 1fr) !important;
        gap: 14px !important;
      }
    }

    @media (max-width: 599px) {
      .ds-grid-6, .blog-posts {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 10px !important;
      }
    }

    .ds-card-box {
      background: #0d0d0d;
      border: 1px solid rgba(188, 167, 114, 0.25);
      border-radius: 8px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
      min-height: 180px;
    }

    .ds-card-box:hover {
      border-color: #bca772;
      transform: translateY(-3px);
      background: #111111;
    }

    .ds-card-box .icon {
      font-size: 22px;
      margin-bottom: 8px;
    }

    .ds-card-box .title {
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
      margin-bottom: 6px;
    }

    .ds-card-box .desc {
      font-size: 11px;
      color: #888888;
      line-height: 1.3;
    }

    .ds-card-box .action {
      font-size: 11px;
      font-weight: 700;
      color: #bca772;
      margin-top: 10px;
    }
  /*]]>*/
  </style>
"""

# 3. HTML Block for Front Page (6 columns on PC, 2 on Mobile)
frontpage_html_block = f"""
            <b:if cond='data:view.isHomepage'>
              <!-- FILA SUPERIOR: ÚLTIMAS ENTRADAS DEL BLOG (6 EN PC / 2 EN CELULAR) -->
              <section class="ds-section-block">
                <div class="ds-section-header">
                  <h2>ÚLTIMAS <span>ENTRADAS DEL BLOG</span></h2>
                  <a href="{URL_TODAS_PUBLICACIONES}" class="ds-section-link">VER TODAS &#10140;</a>
                </div>
              </section>

              <!-- FILA INFERIOR: PÁGINAS ESTÁTICAS SELECCIONADAS (6 EN PC / 2 EN CELULAR) -->
              <section class="ds-section-block">
                <div class="ds-section-header">
                  <h2>PÁGINAS <span>OFICIALES &amp; SERVICIOS</span></h2>
                </div>

                <div class="ds-grid-6">
                  <a href="{URL_DESTILADO}" class="ds-card-box">
                    <div>
                      <div class="icon">🧪</div>
                      <div class="title">Destilado de Ideas</div>
                      <div class="desc">Purificación estratégica de conceptos.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_FORJA}" class="ds-card-box">
                    <div>
                      <div class="icon">🔨</div>
                      <div class="title">Forja de Proyectos</div>
                      <div class="desc">De la idea a la ejecución sólida.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_MARKETING}" class="ds-card-box">
                    <div>
                      <div class="icon">📈</div>
                      <div class="title">Marketing 360°</div>
                      <div class="desc">Estrategias integrales de marca.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_MYPE}" class="ds-card-box">
                    <div>
                      <div class="icon">🚀</div>
                      <div class="title">Impulso MYPE</div>
                      <div class="desc">Acompañamiento a pequeños negocios.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_JUEGO}" class="ds-card-box">
                    <div>
                      <div class="icon">📘</div>
                      <div class="title">El Juego del Emprendedor</div>
                      <div class="desc">Libro y guía para jóvenes.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_MFEIR}" class="ds-card-box">
                    <div>
                      <div class="icon">⚖️</div>
                      <div class="title">Modelo MFEIR</div>
                      <div class="desc">Individualidades Relacionales.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
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
    print("SUCCESS: v6_theme_optimizado.xml created and passed XML test!")
except Exception as e:
    print("XML ERROR:", e)
