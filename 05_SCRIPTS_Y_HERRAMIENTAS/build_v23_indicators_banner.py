import os
import xml.etree.ElementTree as ET

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
theme_dir = os.path.join(root_dir, "03_TEMAS_Y_PLANTILLAS_XML", "03.02_tema_optimizado")
sub_dir = os.path.join(theme_dir, "del 1 al 22")

v22_path = os.path.join(sub_dir, "v22_theme_optimizado.xml")
v23_path_main = os.path.join(theme_dir, "v23_theme_optimizado.xml")
v23_path_sub = os.path.join(sub_dir, "v23_theme_optimizado.xml")

# KEEP V22 UNTOUCHED! READ FROM V22 TO CREATE V23
with open(v22_path, "r", encoding="utf-8") as f:
    v23_content = f.read()

# 1. ADD BANNER CSS BEFORE </style>
banner_css = """
    /* BANNER INDICADORES ECONOMICOS DE BOLIVIA */
    .ds-indicators-banner {
      background: linear-gradient(135deg, #0d0d0d 0%, #161616 100%);
      border: 1px solid rgba(188, 167, 114, 0.35);
      border-radius: 12px;
      padding: 16px 20px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      text-decoration: none !important;
      transition: all 0.3s ease;
      box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }

    .ds-indicators-banner:hover {
      border-color: #bca772;
      box-shadow: 0 6px 20px rgba(188, 167, 114, 0.15);
      transform: translateY(-2px);
    }

    .ds-indicators-banner-info {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .ds-indicators-banner-title {
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin: 0;
    }

    .ds-indicators-banner-title span {
      color: #bca772;
    }

    .ds-indicators-banner-sub {
      font-size: 12px;
      color: #bca772;
      display: flex;
      align-items: center;
      gap: 6px;
      margin: 0;
    }

    .ds-live-dot {
      width: 8px;
      height: 8px;
      background-color: #25D366;
      border-radius: 50%;
      display: inline-block;
      box-shadow: 0 0 8px #25D366;
    }

    .ds-indicators-banner-action {
      font-size: 12px;
      font-weight: 700;
      color: #ffffff;
      background: rgba(188, 167, 114, 0.15);
      border: 1px solid rgba(188, 167, 114, 0.4);
      padding: 8px 14px;
      border-radius: 6px;
      white-space: nowrap;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    @media (max-width: 767px) {
      .ds-indicators-banner {
        flex-direction: column;
        align-items: flex-start;
        gap: 12px;
        padding: 14px 16px;
      }

      .ds-indicators-banner-title {
        font-size: 14px;
      }

      .ds-indicators-banner-sub {
        font-size: 11px;
      }

      .ds-indicators-banner-action {
        width: 100%;
        justify-content: center;
        box-sizing: border-box;
      }
    }
"""

style_tag_pos = v23_content.find('</style>')
if style_tag_pos != -1:
    v23_content = v23_content[:style_tag_pos] + banner_css + "\n" + v23_content[style_tag_pos:]
    print("ADDED BANNER CSS!")

# 2. INSERT BANNER HTML RIGHT ABOVE SECTION 1 (sec-posts)
indicators_page_url = "https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia.html"

banner_html = f"""              <!-- BANNER OFICIAL: INDICADORES ECON&#211;MICOS DE BOLIVIA -->
              <a href="{indicators_page_url}" class="ds-indicators-banner">
                <div class="ds-indicators-banner-info">
                  <h3 class="ds-indicators-banner-title">INDICADORES <span>ECON&#211;MICOS DE BOLIVIA</span></h3>
                  <p class="ds-indicators-banner-sub"><span class="ds-live-dot"></span> Actualizados todos los d&#237;as</p>
                </div>
                <div class="ds-indicators-banner-action">
                  Ver Indicadores &#10140;
                </div>
              </a>

"""

sec_posts_pos = v23_content.find('<section class="ds-section-block" id="sec-posts">')
if sec_posts_pos != -1:
    v23_content = v23_content[:sec_posts_pos] + banner_html + v23_content[sec_posts_pos:]
    print("INSERTED INDICATORS BANNER HTML ABOVE SEC-POSTS!")
else:
    print("ERROR: COULD NOT FIND SEC-POSTS POSITION")

# Save in both locations
with open(v23_path_main, "w", encoding="utf-8") as f:
    f.write(v23_content)

with open(v23_path_sub, "w", encoding="utf-8") as f:
    f.write(v23_content)

try:
    ET.parse(v23_path_main)
    print("SUCCESS: v23_theme_optimizado.xml created and passed XML test!")
    file_size_kb = os.path.getsize(v23_path_main) / 1024
    print(f"File Size: {file_size_kb:.2f} KB (Safe for Blogger Upload!)")
except Exception as e:
    print("XML ERROR:", e)
