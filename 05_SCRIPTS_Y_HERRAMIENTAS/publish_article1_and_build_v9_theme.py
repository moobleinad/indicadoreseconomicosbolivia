import os
import time
import json
import base64
import xml.etree.ElementTree as ET
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
token_path = os.path.join(root_dir, "token.json")
blog_id = "433667097766389126"

# 1. PUBLISH ARTICLE 1 TO BLOGGER VIA API V3
print("=== 1. PUBLICANDO ARTÍCULO 1 EN BLOGGER VIA API V3 ===")
creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/blogger'])
service = build('blogger', 'v3', credentials=creds)

md_art1_path = os.path.join(root_dir, "0_Articulo_1_El_Drama_del_BTH_DanielSimons.md")
with open(md_art1_path, "r", encoding="utf-8") as f:
    art1_text = f.read()

# Base64 data URIs for images
img_pano = r"C:\Users\Usuario\.gemini\antigravity\brain\953edcf7-5053-4ba6-94e5-82edfed7e1d2\foto_articulo1_bth_v4_1785592381896.jpg"
img_sq = os.path.join(root_dir, "foto_articulo1_bth_cuadrada.jpg")

with open(img_pano, "rb") as f:
    b64_pano = base64.b64encode(f.read()).decode("utf-8")
with open(img_sq, "rb") as f:
    b64_sq = base64.b64encode(f.read()).decode("utf-8")

data_uri_pano = f"data:image/jpeg;base64,{b64_pano}"
data_uri_sq = f"data:image/jpeg;base64,{b64_sq}"

# Convert markdown content to clean HTML for Blogger
html_body = f"""
<div style="text-align: center; margin-bottom: 25px;">
  <img src="{data_uri_pano}" alt="De la idea escolar al proyecto ordenado" style="width:100%; max-width:900px; height:auto; border-radius:8px; border:1px solid rgba(188,167,114,0.3);" />
</div>

<p><strong>Por Daniel Simons</strong><br/>
<em>Estructurador de Ideas Complejas | Autor de «El Juego del Emprendedor»</em></p>

<hr style="border-color: rgba(188,167,114,0.3); margin: 20px 0;" />

<h3>📌 El verdadero reto de los proyectos de emprendimiento escolar</h3>
<p>Cada año, miles de estudiantes de secundaria y jóvenes emprendedores se enfrentan al desafío de presentar un proyecto productivo o iniciativa de negocio. Tanto para los alumnos como para sus familias y docentes, la primera gran barrera no es la falta de creatividad o entusiasmo, sino una pregunta fundamental: <strong>¿por dónde se empieza y cómo se pasa de una idea en la cabeza a una propuesta clara y ordenada?</strong></p>

<p>En la mayoría de las ferias y materias prácticas, es común ver un esfuerzo enorme enfocado únicamente en la presentación visual del producto. Sin embargo, cuando se le pregunta al estudiante sobre la utilidad real de su idea, sus costos o su público objetivo, surge la confusión.</p>

<hr style="border-color: rgba(188,167,114,0.3); margin: 20px 0;" />

<h3>💡 El valor del orden: Transformar el desorden en estructura lógica</h3>
<p>Emprender en la etapa escolar o universitaria no requiere presentar de inmediato una empresa gigante ni buscar financiamiento bancario a gran escala. Ser realistas y honestos es el primer paso: <strong>un proyecto juvenil no necesita ser perfecto ni financiable de inmediato para ser valioso</strong>.</p>

<p>Lo que verdaderamente transforma la experiencia de un estudiante es adquirir <strong>orden, criterio técnico y estructura</strong>.</p>

<p>Pasar del caos a la claridad implica responder cuatro preguntas clave de forma sencilla:</p>
<ol>
  <li><strong>El Problema Real:</strong> ¿Qué necesidad o deseo concreto busca resolver este proyecto?</li>
  <li><strong>El Público Objetivo:</strong> ¿A quién le interesa realmente este producto o servicio y por qué?</li>
  <li><strong>Los Costos Reales:</strong> ¿Cuánto cuesta producirlo y a qué precio se debe ofrecer sin trabajar a pérdida?</li>
  <li><strong>La Propuesta Clara:</strong> ¿Cómo se presenta la idea de forma lógica, comprensible y honesta?</li>
</ol>

<hr style="border-color: rgba(188,167,114,0.3); margin: 20px 0;" />

<h3>🎯 Una expectativa honesta: Claridad antes que ilusión</h3>
<p>El objetivo de trabajar con métodos estructurados de emprendimiento no es prometer resultados irreales o bancables de la noche a la mañana.</p>

<p>La verdadera ganancia para el joven, el padre de familia y el docente radica en dar <strong>un paso sólido hacia adelante</strong>:</p>
<ul>
  <li><strong>Del desorden a la estructura:</strong> El estudiante deja de improvisar y aprende a pensar con lógica de negocio.</li>
  <li><strong>De la duda a la seguridad:</strong> Comprende los números y los fundamentos de su trabajo, lo que le permite defender su idea con confianza ante cualquier evaluación.</li>
  <li><strong>De la teoría a la práctica útil:</strong> Desarrolla un producto mínimo ordenado y entendible que sienta las bases para su futuro profesional.</li>
</ul>

<p>Aunque el proyecto aún esté lejos de un financiamiento comercial, haber logrado orden, claridad y criterio es el mayor activo que un estudiante puede llevarse para la vida real.</p>

<hr style="border-color: rgba(188,167,114,0.3); margin: 20px 0;" />

<h3>🚀 Construyendo claridad paso a paso</h3>
<p>Si eres docente, director o padre de familia y deseas que tus jóvenes aprendan a transformar sus ideas en proyectos ordenados y con sentido práctico:</p>

<ul>
  <li>📘 <strong>«El Juego del Emprendedor»:</strong> La guía metodológica simplificada diseñada para acompañar a estudiantes y jóvenes en el diseño paso a paso de sus proyectos.</li>
  <li>🎓 <strong>Talleres &amp; Estructuración Guiada:</strong> Capacitaciones prácticas para colegios, institutos y universidades.</li>
</ul>

<p style="margin-top:25px;">📲 <strong>Contacto directo con Daniel Simons:</strong> <a href="https://wa.me/59170000000" style="color:#bca772; font-weight:bold;">WhatsApp de Consultoría y Estructuración</a><br/>
🌐 <strong>Portal Oficial:</strong> <a href="https://www.danielsimons.xyz" style="color:#bca772; font-weight:bold;">www.danielsimons.xyz</a></p>
"""

post_title = "De la idea escolar al proyecto ordenado: Cómo estructurar emprendimientos juveniles con claridad e impacto real"
post_data = {
    'title': post_title,
    'content': html_body,
    'labels': ['BTH', 'Emprendimiento', 'Jóvenes', 'Daniel Simons'],
}

try:
    published_post = service.posts().insert(blogId=blog_id, body=post_data, isDraft=False).execute()
    print("SUCCESS: Post publicado exitosamente en Blogger!")
    print("URL del Post:", published_post.get('url'))
    url_post_1 = published_post.get('url')
except Exception as e:
    print("Error publicando post:", e)
    url_post_1 = "https://www.danielsimons.xyz/search"

# 2. BUILD V9 THEME XML WITH SQUARE THUMBNAILS & SMOOTH SLIDER CAROUSEL WITH GOLD ARROWS
print("\n=== 2. CONSTRUYENDO V9 THEME XML CON MINIATURAS CUADRADAS Y CARRUSEL DESLIZANTE ===")
source_path = os.path.join(root_dir, r"copia de seguridad del tema web\theme-433667097766389126.xml")
output_dir = os.path.join(root_dir, "tema_optimizado")
output_path = os.path.join(output_dir, "v9_theme_optimizado.xml")

with open(source_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# Live Page URLs on Blogger:
URL_DESTILADO = "https://www.danielsimons.xyz/p/destilado-de-ideas-de-negocio_0599447061.html"
URL_FORJA = "https://www.danielsimons.xyz/p/forja-disciplina-habitos-y-lucidez.html"
URL_MARKETING = "https://www.danielsimons.xyz/p/marketing-360.html"
URL_MYPE = "https://www.danielsimons.xyz/p/impulso-mype-360.html"
URL_JUEGO = "https://www.danielsimons.xyz/p/el-juego-del-emprendedor-libro-para.html"
URL_MFEIR = "https://www.danielsimons.xyz/p/liberalismo-vs-socialismo.html"

# SEO & Open Graph Meta Tags
seo_block = """
  <!-- OPTIMIZACION SEO V9 DANIEL SIMONS -->
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

# CSS for Pure Black #000000, Square Thumbnails, and Horizontal Carousel Slider with Gold Arrows
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

    /* CARRUSEL HORIZONTAL EN UNA SOLA FILA */
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
        min-width: 200px !important;
      }
    }

    .ds-card-box:hover {
      border-color: #bca772;
      transform: translateY(-3px);
      background: #111111;
    }

    .ds-card-thumb {
      width: 100%;
      aspect-ratio: 1 / 1;
      border-radius: 6px;
      object-fit: cover;
      margin-bottom: 12px;
      border: 1px solid rgba(188, 167, 114, 0.2);
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

# Frontpage HTML Block with Smooth Horizontal Slider & Square Thumbnails
frontpage_html_block = f"""
            <b:if cond='data:view.isHomepage'>
              <!-- FILA 1: ÚLTIMAS ENTRADAS DEL BLOG (CARRUSEL SLIDER HORIZONTAL) -->
              <section class="ds-section-block">
                <div class="ds-section-header">
                  <h2>ÚLTIMAS <span>ENTRADAS DEL BLOG</span></h2>
                  <div class="ds-nav-arrows">
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', -1)">&#10094;</div>
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-posts', 1)">&#10095;</div>
                  </div>
                </div>

                <div class="ds-carousel-track" id="track-posts">
                  <a href="{url_post_1}" class="ds-card-box">
                    <div>
                      <img src="{data_uri_sq}" alt="De la idea escolar al proyecto ordenado" class="ds-card-thumb" />
                      <div class="title">De la idea escolar al proyecto ordenado</div>
                      <div class="desc">Cómo estructurar emprendimientos juveniles BTH con claridad e impacto.</div>
                    </div>
                    <div class="action">Leer Artículo &#10140;</div>
                  </a>
                </div>
              </section>

              <!-- FILA 2: PÁGINAS OFICIALES Y SERVICIOS (CARRUSEL SLIDER HORIZONTAL) -->
              <section class="ds-section-block">
                <div class="ds-section-header">
                  <h2>PÁGINAS <span>OFICIALES &amp; SERVICIOS</span></h2>
                  <div class="ds-nav-arrows">
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-pages', -1)">&#10094;</div>
                    <div class="ds-arrow-btn" onclick="scrollCarousel('track-pages', 1)">&#10095;</div>
                  </div>
                </div>

                <div class="ds-carousel-track" id="track-pages">
                  <a href="{URL_DESTILADO}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; align-items:center; justify-center; font-size:42px;">🧪</div>
                      <div class="title">Destilado de Ideas</div>
                      <div class="desc">Del conocimiento disperso a la claridad ejecutiva.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_FORJA}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; align-items:center; justify-center; font-size:42px;">🔨</div>
                      <div class="title">Forja de Proyectos</div>
                      <div class="desc">De la idea a la ejecución sólida y estructurada.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_MARKETING}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; align-items:center; justify-center; font-size:42px;">📈</div>
                      <div class="title">Marketing 360°</div>
                      <div class="desc">Estrategias integrales y posicionamiento de marca.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_MYPE}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; align-items:center; justify-center; font-size:42px;">🚀</div>
                      <div class="title">Impulso MYPE</div>
                      <div class="desc">Acompañamiento técnico a pequeños negocios.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_JUEGO}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; align-items:center; justify-center; font-size:42px;">📘</div>
                      <div class="title">El Juego del Emprendedor</div>
                      <div class="desc">Libro y guía metodológica para jóvenes.</div>
                    </div>
                    <div class="action">Ver Página &#10140;</div>
                  </a>

                  <a href="{URL_MFEIR}" class="ds-card-box">
                    <div>
                      <div class="ds-card-thumb" style="background:#141414; display:flex; align-items:center; justify-center; font-size:42px;">⚖️</div>
                      <div class="title">Modelo MFEIR</div>
                      <div class="desc">Individualidades Relacionales y Análisis.</div>
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
    print("SUCCESS: v9_theme_optimizado.xml created and passed XML test!")
except Exception as e:
    print("XML ERROR:", e)
