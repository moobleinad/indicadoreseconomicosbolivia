import os
import json
import urllib.request
import urllib.parse

root_dir = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz"
token_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.03_token.json")
secret_path = os.path.join(root_dir, "04_API_BLOGGER_Y_AUTENTICACION", "04.02_client_secret.json")

with open(token_path, "r", encoding="utf-8") as f:
    token_data = json.load(f)

with open(secret_path, "r", encoding="utf-8") as f:
    secret_data = json.load(f)

# Extract client_id and client_secret
client_info = secret_data.get("installed") or secret_data.get("web") or {}
client_id = client_info.get("client_id")
client_secret = client_info.get("client_secret")
refresh_token = token_data.get("refresh_token")

print("Client ID:", client_id)
print("Has refresh token:", bool(refresh_token))

# Refresh access token
refresh_url = "https://oauth2.googleapis.com/token"
refresh_payload = urllib.parse.urlencode({
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token,
    "grant_type": "refresh_token"
}).encode("utf-8")

req_token = urllib.request.Request(refresh_url, data=refresh_payload, headers={"Content-Type": "application/x-www-form-urlencoded"})

try:
    with urllib.request.urlopen(req_token) as resp:
        new_token_resp = json.loads(resp.read().decode("utf-8"))
        access_token = new_token_resp["access_token"]
        print("SUCCESSFULLY REFRESHED ACCESS TOKEN!")
        
        # Save updated token
        token_data["token"] = access_token
        with open(token_path, "w", encoding="utf-8") as f:
            json.dump(token_data, f, indent=2)
            
        # Headers for Blogger API
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        # Fetch user's blogs
        req_blogs = urllib.request.Request("https://www.googleapis.com/blogger/v3/users/self/blogs", headers=headers)
        with urllib.request.urlopen(req_blogs) as b_resp:
            blogs_data = json.loads(b_resp.read().decode("utf-8"))
            blog_id = blogs_data["items"][0]["id"]
            print("TARGET BLOG ID:", blog_id)
            
            # Post content in HTML format
            post_title = "RÉGIMEN CAMBIARIO: CÓMO FUNCIONA AHORA EL TIPO DE CAMBIO DEL DÓLAR EN BOLIVIA"
            
            post_body_html = """<p><strong>Serie Política Monetaria y Sociedad | Parte 1</strong><br/>
<em>Por Daniel Simons</em></p>

<p>La <strong>Resolución Ministerial N° 245</strong> ha oficializado la transición hacia un <strong>Régimen Cambiario Flexible</strong> en Bolivia. El Estado ha dejado de fijar un precio congelado para el dólar, abriendo paso a un sistema donde la cotización se determina por la interacción diaria entre la oferta y la demanda de divisas en el sistema financiero.</p>

<p>Comprender cómo funciona este mecanismo y qué esperar a corto y mediano plazo es fundamental para resguardar el patrimonio personal y empresarial.</p>

<h3>1. El mecanismo de oferta y demanda en el mercado monetario</h3>

<p>El dinero funciona bajo la misma lógica que cualquier bien en el mercado:</p>

<ul>
  <li><strong>Oferta de divisas:</strong> Proviene de las exportaciones, el ingreso de remesas, los créditos internacionales y la venta de oro por parte del Banco Central de Bolivia (BCB).</li>
  <li><strong>Demanda de divisas:</strong> Nace de los importadores de mercadería, repuestos y materia prima, así como de los ciudadanos que buscan proteger sus ahorros.</li>
</ul>

<p>Bajo la R.M. 245, el BCB determina la cotización oficial registrando diariamente el punto de cruce entre esta oferta y demanda en el sistema bancario. Si la demanda de dólares supera a la oferta disponible, el valor de la divisa sube; si ingresan dólares al sistema, la cotización tiende a estabilizarse.</p>

<h3>2. Proyección y presión inflacionaria: ¿Qué esperar para los próximos meses?</h3>

<p>A corto plazo, la transición abrupta a un régimen flexible genera dos efectos inmediatos:</p>

<ol>
  <li><strong>Volatilidad continuada:</strong> El tipo de cambio fluctuará mientras la economía busca su punto de equilibrio real.</li>
  <li><strong>Presión inflacionaria (Inflación por costos):</strong> El encarecimiento del dólar eleva el costo de los productos e insumos importados, trasladando esa presión de precios de forma directa a la canasta familiar y a la estructura operativa de los negocios.</li>
</ol>

<h3>3. Cómo resguardar tu dinero y el estímulo a la producción nacional</h3>

<p>Frente a este escenario, existen tres estrategias fundamentales de resguardo y adaptación:</p>

<ul>
  <li><strong>Resguardo en Dólares (Divisa Dura):</strong> Pese a cualquier narrativa o discurso oficial, mantener reservas o activos indexados en moneda fuerte sigue siendo la vía principal de protección del capital frente a la devaluación del boliviano.</li>
  <li><strong>Refugio en Activos Físicos y Reales:</strong> Convertir excedentes líquidos en activos tangibles —inventario no perecedero (arroz, alimentos, insumos básicos), inmuebles o terrenos— preserva el valor real del patrimonio frente al deterioro del poder adquisitivo.</li>
  <li><strong>Oportunidad para la Producción Nacional:</strong> El encarecimiento de los productos importados genera un efecto de sustitución: los bienes producidos en Bolivia se vuelven más competitivos en precio frente a lo importado, lo que puede estimular la industria y la producción local, siempre que los productores adapten sus costos de insumos.</li>
</ul>

<h3>4. Conexión a la Parte 2: El impacto en el ciudadano</h3>

<p>Este no es el mejor camino. Al igual que ocurrió con el ajuste repentino de los precios de los carburantes, este salto brusco coloca en aprietos directos al ciudadano común y le hace pagar a él los grandes ajustes acumulados de la economía.</p>

<p>¿Era la flotación libre inmediata la única opción, o un ajuste gradual (flotación sucia) hubiera protegido mejor al ciudadano y a la MYPE?</p>

<p><a href="https://www.danielsimons.xyz/p/impulso-mype-360.html"><strong>[EVALUAR ESTRUCTURA DE MI NEGOCIO CON DANIEL SIMONS]</strong></a></p>
"""
            
            post_payload = {
                "kind": "blogger#post",
                "title": post_title,
                "content": post_body_html
            }
            
            publish_url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/"
            req_pub = urllib.request.Request(publish_url, data=json.dumps(post_payload).encode("utf-8"), headers=headers, method="POST")
            
            with urllib.request.urlopen(req_pub) as pub_resp:
                pub_data = json.loads(pub_resp.read().decode("utf-8"))
                print("PUBLISHED SUCCESSFULLY VIA BLOGGER API!")
                print("LIVE POST URL:", pub_data.get("url"))
                print("LIVE POST ID:", pub_data.get("id"))
                
                with open(os.path.join(root_dir, "05_SCRIPTS_Y_HERRAMIENTAS", "last_published_post.json"), "w", encoding="utf-8") as pf:
                    json.dump(pub_data, pf, indent=2)

except Exception as e:
    print("REFRESH AND PUBLISH ERROR:", e)
