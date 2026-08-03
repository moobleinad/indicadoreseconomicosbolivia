import os
import base64
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
source_path = os.path.join(root_dir, r"copia de seguridad del tema web\theme-433667097766389126.xml")
output_dir = os.path.join(root_dir, "tema_optimizado")
output_path = os.path.join(output_dir, "v11_theme_optimizado.xml")

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

uri_art1 = get_b64(os.path.join(root_dir, "foto_articulo1_bth_cuadrada.jpg"))
uri_destilado = get_b64(r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_destilado_1785593994402.jpg")
uri_forja = get_b64(r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\thumb_forja_1785594011419.jpg")
uri_mkt360 = get_b64(os.path.join(root_dir, "thumb_mkt360.jpg"))
uri_mype = get_b64(os.path.join(root_dir, "thumb_mype.jpg"))
uri_juego = get_b64(os.path.join(root_dir, "thumb_juego.jpg"))
uri_mfeir = get_b64(os.path.join(root_dir, "thumb_mfeir.jpg"))

with open(source_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# Live Page URLs:
URL_POST_1 = "https://www.danielsimons.xyz/2026/08/de-la-idea-escolar-al-proyecto-ordenado.html"
URL_DESTILADO = "https://www.danielsimons.xyz/p/destilado-de-ideas-de-negocio_0599447061.html"
URL_FORJA = "https://www.danielsimons.xyz/p/forja-disciplina-habitos-y-lucidez.html"
URL_MARKETING = "https://www.danielsimons.xyz/p/marketing-360.html"
URL_MYPE = "https://www.danielsimons.xyz/p/impulso-mype-360.html"
URL_JUEGO = "https://www.danielsimons.xyz/p/el-juego-del-emprendedor-libro-para.html"
URL_MFEIR = "https://www.danielsimons.xyz/p/liberalismo-vs-socialismo.html"
URL_URBANIZACIONES = "https://www.danielsimons.xyz/p/propuesta-urbanizaciones.html"
URL_TRANSPARENCIA = "https://www.danielsimons.xyz/p/transparencia-inteligente.html"
URL_ELECTORAL = "https://www.danielsimons.xyz/p/estrategia-electoral-2026.html"
URL_TESIS = "https://www.danielsimons.xyz/p/guia-tesis.html"
URL_MARCA = "https://www.danielsimons.xyz/p/evaluar-desarrollo-de-marca.html"
URL_TODAS = "https://www.danielsimons.xyz/search"

# SEO Block
seo_block = """
  <!-- OPTIMIZACION SEO V11 DANIEL SIMONS -->
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

# CSS for V11: Square Thumbnails 100% Full Width, Mobile Title 15px, Pure Black #000000
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

    #main, .page, .centered-bottom, .post-outer-container, .centered-top-container {
      width: 100% !important;
      max-width: 1040px !important;
      margin: 0 auto !important;
      padding: 0 40px !important;
      float: none !important;
      left: 0 !important;
      box-sizing: border-box !important;
    }

    @media (max-width: 767px) {
      #main, .page, .centered-bottom, .post-outer-container, .centered-top-container {
        padding: 0 15px !important;
      }
    }

    .Header, #Header1, .header-widget {
      background: #000000 !important;
      text-align: center !important;
      margin: 15px 0 25px 0 !important;
      padding: 0 !important;
    }

    .Header img, #Header1 img {
      width: 100% !important;
      max-width: 900px !important;
      height: auto !important;
      max-height: 260px !important;
      object-fit: contain !important;
      margin: 0 auto !important;
      display: block !important;
    }

    .ds-section-block {
      margin: 35px 0;
    }

    .ds-section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      padding-bottom: 8px;
      border-bottom: 1px solid rgba(188, 167, 114, 0.25);
    }

    .ds-section-header h2 {
      font-size: 18px;
      font-weight: 800;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin: 0;
    }

    .ds-section-header h2 span {
      color: #bca772;
    }

    .ds-section-link {
      font-size: 11px;
      font-weight: 700;
      color: #bca772 !important;
      text-transform: uppercase;
      text-decoration: none !important;
    }

    .ds-nav-arrows {
      display: flex;
      gap: 10px;
      align-items: center;
    }

    .ds-arrow-btn {
      background: #0d0d0d;
      border: 1px solid rgba(188, 167, 114, 0.4);
      color: #bca772;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 14px;
      transition: all 0.25s ease;
      user-select: none;
    }

    .ds-arrow-btn:hover {
      background: #bca772;
      color: #000000;
      border-color: #bca772;
    }

    /* CARRUSEL HORIZONTAL */
    .ds-carousel-track {
      display: flex !important;
      gap: 16px !important;
      overflow-x: auto !important;
      scroll-behavior: smooth !important;
      scroll-snap-type: x mandatory !important;
      padding-bottom: 12px !important;
      -ms-overflow-style: none;
      scrollbar-width: none;
    }

    .ds-carousel-track::-webkit-scrollbar {
      display: none;
    }

    .ds-card-box {
      flex: 0 0 calc(33.333% - 11px) !important;
      min-width: 260px !important;
      scroll-snap-align: start !important;
      background: #0d0d0d;
      border: 1px solid rgba(188, 167, 114, 0.25);
      border-radius: 8px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.25s ease;
      box-sizing: border-box !important;
      text-decoration: none !important;
    }

    @media (max-width: 767px) {
      .ds-card-box {
        flex: 0 0 calc(50% - 8px) !important;
        min-width: 210px !important;
        padding: 12px !important;
      }
    }

    .ds-card-box:hover {
      border-color: #bca772;
      transform: translateY(-3px);
      background: #111111;
    }

    /* MINIATURA CUADRADA REALISTA QUE LLENA EL 100% DEL ÁREA */
    .ds-card-thumb {
      width: 100% !important;
      height: auto !important;
      aspect-ratio: 1 / 1 !important;
      border-radius: 6px !important;
      object-fit: cover !important;
      margin-bottom: 12px !important;
      border: 1px solid rgba(188, 167, 114, 0.3) !important;
      display: block !important;
    }

    .ds-card-box .title {
      font-size: 14px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1.35;
      margin-bottom: 6px;
    }

    /* TIPOGRAFÍA MÁS GRANDE EN CELULAR */
    @media (max-width: 767px) {
      .ds-card-box .title {
        font-size: 15px !important;
        line-height: 1.3 !important;
        font-weight: 700 !important;
      }
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

    /* BLOQUE QUIÉN SOY */
    .ds-bio-card {
      background: #0d0d0d;
      border: 1px solid rgba(188, 167, 114, 0.3);
      border-radius: 10px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .ds-bio-card h3 {
      font-size: 20px;
      color: #bca772;
      margin: 0 0 6px 0;
      font-weight: 800;
    }

    .ds-bio-card p {
      font-size: 13px;
      line-height: 1.6;
      color: #cccccc;
      margin: 0;
    }
  /*]]>*/
  </style>

  <script type='text/javascript'>
  //<![CDATA[
    function scrollCarousel(id, direction) {
      var container = document.getElementById(id);
      if (container) {
        var scrollAmount = container.clientWidth * 0.75;
        container.scrollBy({
          left: direction * scrollAmount,
          behavior: 'smooth'
        });
      }
    }
  //]]>
  </script>
"""

# HTML Frontpage Block for V11 with 100% Square Image Thumbnails on All Cards
frontpage_html_block = f"""
            <b:if cond='data:view.isHomepage'>

              <!-- SECCIÓN 1: ÚLTIMAS ENTRADAS DEL BLOG -->
              <section class="ds-section-block">
                <div class="ds-section-header">
                  <h2>ÚLTIMAS <span>ENTRADAS DEL BLOG</span></h2>
                  <div style="display:flex; align-items:center; gap:12px;">
                    <a href="{URL_TODAS}" class="ds-section-link">VER TODAS &#10140;</a>
                    <div class="ds-nav-arrows">
                      <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', -1)">&#10094;</div>
                      <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', 1)">&#10095;</div>
                    </div>
                  </div>
                </div>

                <div class="ds-carousel-track" id="track-posts">
                  <a href="{URL_POST_1}" class="ds-card-box">
                    <div>
                      <img src="{uri_art1}" alt="De la idea escolar al proyecto ordenado" class="ds-card-thumb" />
                      <div class="title">De la idea escolar al proyecto ordenado</div>
                      <div class="desc">Cómo estructurar emprendimientos juveniles BTH con claridad e impacto.</div>
                    </div>
                    <div class="action">Leer Artículo &#10140;</div>
                  </a>
                </div>
              </section>

              <!-- SECCIÓN 2: SERVICIOS DE ESTRUCTURACIÓN CON VISTAS PREVIAS FOTOGRÁFICAS CUADRADAS -->
              <section class="ds-section-block">
                <div class="ds-section-header">
                  <h2>SERVICIOS <span>DE ESTRUCTURACIÓN</span></h2>
                  <div class="ds-nav-arrows">
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-services', -1)">&#10094;</div>
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-services', 1)">&#10095;</div>
                  </div>
                </div>

                <div class="ds-carousel-track" id="track-services">
                  <a href="{URL_DESTILADO}" class="ds-card-box">
                    <div>
                      <img src="{uri_destilado}" alt="Destilado de Ideas" class="ds-card-thumb" />
                      <div class="title">Destilado de Ideas</div>
                      <div class="desc">Del conocimiento disperso a la claridad ejecutiva.</div>
                    </div>
                    <div class="action">Ver Servicio &#10140;</div>
                  </a>

                  <a href="{URL_FORJA}" class="ds-card-box">
                    <div>
                      <img src="{uri_forja}" alt="Forja de Proyectos" class="ds-card-thumb" />
                      <div class="title">Forja de Proyectos</div>
                      <div class="desc">De la idea a la ejecución sólida y estructurada.</div>
                    </div>
                    <div class="action">Ver Servicio &#10140;</div>
                  </a>

                  <a href="{URL_MARKETING}" class="ds-card-box">
                    <div>
                      <img src="{uri_mkt360}" alt="Marketing 360°" class="ds-card-thumb" />
                      <div class="title">Marketing 360°</div>
                      <div class="desc">Estrategias integrales y posicionamiento de marca.</div>
                    </div>
                    <div class="action">Ver Servicio &#10140;</div>
                  </a>

                  <a href="{URL_MYPE}" class="ds-card-box">
                    <div>
                      <img src="{uri_mype}" alt="Impulso MYPE" class="ds-card-thumb" />
                      <div class="title">Impulso MYPE</div>
                      <div class="desc">Acompañamiento técnico a pequeños negocios.</div>
                    </div>
                    <div class="action">Ver Servicio &#10140;</div>
                  </a>
                </div>
              </section>

              <!-- SECCIÓN 3: PROYECTOS PROPIOS & INVESTIGACIÓN -->
              <section class="ds-section-block">
                <div class="ds-section-header">
                  <h2>PROYECTOS <span>PROPIOS &amp; INVESTIGACIÓN</span></h2>
                  <div class="ds-nav-arrows">
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-projects', -1)">&#10094;</div>
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-projects', 1)">&#10095;</div>
                  </div>
                </div>

                <div class="ds-carousel-track" id="track-projects">
                  <a href="{URL_MFEIR}" class="ds-card-box">
                    <div>
                      <img src="{uri_mfeir}" alt="Modelo MFEIR" class="ds-card-thumb" />
                      <div class="title">Modelo MFEIR</div>
                      <div class="desc">Individualidades Relacionales y Análisis Político-Social.</div>
                    </div>
                    <div class="action">Conocer Modelo &#10140;</div>
                  </a>

                  <a href="{URL_JUEGO}" class="ds-card-box">
                    <div>
                      <img src="{uri_juego}" alt="El Juego del Emprendedor" class="ds-card-thumb" />
                      <div class="title">El Juego del Emprendedor</div>
                      <div class="desc">Libro y guía metodológica para jóvenes y colegios.</div>
                    </div>
                    <div class="action">Ver Libro &#10140;</div>
                  </a>
                </div>
              </section>

              <!-- SECCIÓN 4: QUIÉN SOY (DANIEL SIMONS) -->
              <section class="ds-section-block">
                <div class="ds-bio-card">
                  <h3>DANIEL SIMONS</h3>
                  <p><strong>Estructurador de Ideas Complejas | IDEAS • ESTRUCTURA • IMPACTO</strong></p>
                  <p>Convierto ideas dispersas o complejas en soluciones claras, estructuradas y aplicables mediante investigación, análisis, diseño estratégico y desarrollo de proyectos. No vendo únicamente consultoría. Construyo claridad.</p>
                </div>
              </section>

              <!-- SECCIÓN 5: TRABAJOS Y PROPUESTAS -->
              <section class="ds-section-block">
                <div class="ds-section-header">
                  <h2>TRABAJOS <span>Y PROPUESTAS</span></h2>
                  <div class="ds-nav-arrows">
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-work', -1)">&#10094;</div>
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-work', 1)">&#10095;</div>
                  </div>
                </div>

                <div class="ds-carousel-track" id="track-work">
                  <a href="{URL_URBANIZACIONES}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#bca772; font-weight:800; font-size:16px; border:1px solid rgba(188,167,114,0.3);">
                        <div style="font-size:30px; margin-bottom:4px;">🏙️</div>
                        URBANIZACIONES
                      </div>
                      <div class="title">Propuesta Urbanizaciones</div>
                      <div class="desc">Estrategias de desarrollo urbano en Santa Cruz.</div>
                    </div>
                    <div class="action">Ver Propuesta &#10140;</div>
                  </a>

                  <a href="{URL_TRANSPARENCIA}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#bca772; font-weight:800; font-size:16px; border:1px solid rgba(188,167,114,0.3);">
                        <div style="font-size:30px; margin-bottom:4px;">👁️</div>
                        TRANSPARENCIA
                      </div>
                      <div class="title">Transparencia Inteligente</div>
                      <div class="desc">Modelos de gestión institucional y datos.</div>
                    </div>
                    <div class="action">Ver Propuesta &#10140;</div>
                  </a>

                  <a href="{URL_ELECTORAL}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#bca772; font-weight:800; font-size:16px; border:1px solid rgba(188,167,114,0.3);">
                        <div style="font-size:30px; margin-bottom:4px;">🗳️</div>
                        ELECTORAL 2026
                      </div>
                      <div class="title">Estrategia Electoral 2026</div>
                      <div class="desc">Análisis político y estratégico para Bolivia.</div>
                    </div>
                    <div class="action">Ver Estrategia &#10140;</div>
                  </a>

                  <a href="{URL_TESIS}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#bca772; font-weight:800; font-size:16px; border:1px solid rgba(188,167,114,0.3);">
                        <div style="font-size:30px; margin-bottom:4px;">🎓</div>
                        GUÍA TESIS
                      </div>
                      <div class="title">Guía Sobreviviendo a la Tesis</div>
                      <div class="desc">Metodología práctica para proyectos universitarios.</div>
                    </div>
                    <div class="action">Ver Guía &#10140;</div>
                  </a>

                  <a href="{URL_MARCA}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; flex-direction:column; align-items:center; justify-content:center; color:#bca772; font-weight:800; font-size:16px; border:1px solid rgba(188,167,114,0.3);">
                        <div style="font-size:30px; margin-bottom:4px;">🔍</div>
                        DESARROLLO MARCA
                      </div>
                      <div class="title">Evaluar Desarrollo de Marca</div>
                      <div class="desc">Auditoría estratégica de marca y mercado.</div>
                    </div>
                    <div class="action">Ver Evaluación &#10140;</div>
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
    print("SUCCESS: v11_theme_optimizado.xml created and passed XML test!")
except Exception as e:
    print("XML ERROR:", e)
