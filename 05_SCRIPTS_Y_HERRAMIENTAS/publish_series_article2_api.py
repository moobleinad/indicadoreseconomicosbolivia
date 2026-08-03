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

client_info = secret_data.get("installed") or secret_data.get("web") or {}
client_id = client_info.get("client_id")
client_secret = client_info.get("client_secret")
refresh_token = token_data.get("refresh_token")

# Refresh token
refresh_url = "https://oauth2.googleapis.com/token"
refresh_payload = urllib.parse.urlencode({
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token,
    "grant_type": "refresh_token"
}).encode("utf-8")

req_token = urllib.request.Request(refresh_url, data=refresh_payload, headers={"Content-Type": "application/x-www-form-urlencoded"})

with urllib.request.urlopen(req_token) as resp:
    new_token_resp = json.loads(resp.read().decode("utf-8"))
    access_token = new_token_resp["access_token"]
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    req_blogs = urllib.request.Request("https://www.googleapis.com/blogger/v3/users/self/blogs", headers=headers)
    with urllib.request.urlopen(req_blogs) as b_resp:
        blogs_data = json.loads(b_resp.read().decode("utf-8"))
        blog_id = blogs_data["items"][0]["id"]
        
        post_title = "RÉGIMEN CAMBIARIO: EL DEBATE ENTRE LA TERAPIA DE CHOQUE Y LA FLOTACIÓN GRADUAL"
        
        post_body_html = """<p><strong>Serie Política Monetaria y Sociedad | Parte 2</strong><br/>
<em>Por Daniel Simons</em></p>

<p>El paso repentino hacia un tipo de cambio totalmente flexible ha generado una sacudida inmediata en la economía boliviana. Pasar sin anestesia de una cotización congelada durante más de una década a una flotación libre transfiere toda la volatilidad cambiaria directamente al bolsillo del ciudadano y a la estructura de costos de las pequeñas y medianas empresas.</p>

<p>Al igual que ocurrió con el incremento brusco en el precio de los combustibles, este salto repentino obliga a la economía privada y a las familias a pagar de golpe los grandes desajustes acumulados por el Estado.</p>

<h3>1. La cadena de transmisión del choque libre</h3>

<p>En una economía endeble con baja disponibilidad de divisas en ventanilla bancaria, la flotación libre desencadena un mecanismo de transmisión inmediato.</p>

<p>La incertidumbre sobre el valor diario del dólar eleva los precios de reposición de insumos e importaciones. Este incremento se traslada en tiempo real a los bienes de consumo final, acelerando la presión inflacionaria.</p>

<p>El resultado es la erosión del poder adquisitivo y el agotamiento del capital de trabajo de las MYPEs, que ven cómo su liquidez se evapora al intentar reponer inventario.</p>

<h3>2. La alternativa técnica: El modelo de flotación sucia administrada</h3>

<p>Frente a una terapia de choque, la teoría monetaria y la experiencia de la región demuestran que existía un camino de ajuste predecible: el modelo de flotación sucia o deslizamiento progresivo con bandas cambiarias.</p>

<p>Bajo este esquema, el Banco Central establece una pauta de ajuste gradual conocido de antemano por el mercado.</p>

<p>Este mecanismo permite que importadores, productores y familias proyecten sus costos de reposición y flujo de caja con margen de planificación, evitando picos especulativos salvajes y situaciones de pánico.</p>

<h3>3. Adaptación estructural: Cómo proteger tu patrimonio y tu empresa</h3>

<p>Con el régimen flexible en marcha, la solución para las empresas y familias no es esperar medidas gubernamentales milagrosas, sino adaptar la estructura interna.</p>

<p>Resguardar excedentes líquidos en divisas duras o en activos reales tangibles preserva el valor del capital frente al deterioro de la moneda nacional.</p>

<p>Para las empresas, revisar el margen bruto real, ajustar los ciclos de cobro y adaptar la propuesta de valor a la nueva realidad de costos es la única garantía de continuidad.</p>

<p>Si necesitas evaluar la estructura financiera de tu empresa, proteger tu liquidez o rediseñar tu modelo operativo frente al nuevo escenario cambiario, conoce nuestro programa de acompañamiento técnico:</p>

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
            print("ARTICLE 2 PUBLISHED SUCCESSFULLY VIA BLOGGER API!")
            print("LIVE ARTICLE URL:", pub_data.get("url"))
            print("LIVE ARTICLE ID:", pub_data.get("id"))
            
            with open(os.path.join(root_dir, "05_SCRIPTS_Y_HERRAMIENTAS", "last_published_article2.json"), "w", encoding="utf-8") as pf:
                json.dump(pub_data, pf, indent=2)
