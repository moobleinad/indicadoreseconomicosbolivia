import os
import json
import urllib.request

WHATSAPP_API_TOKEN = os.getenv("WHATSAPP_CLOUD_API_TOKEN", "")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
RECIPIENT_ID = os.getenv("WHATSAPP_RECIPIENT_ID", "") # Puede ser número o ID de canal

def send_whatsapp_message(message_text, recipient=None):
    """
    Envía un mensaje a través de Meta WhatsApp Cloud API.
    Si los tokens no están configurados en el entorno, registra un aviso explicativo.
    """
    token = os.getenv("WHATSAPP_CLOUD_API_TOKEN", WHATSAPP_API_TOKEN)
    phone_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID", PHONE_NUMBER_ID)
    target = recipient or os.getenv("WHATSAPP_RECIPIENT_ID", RECIPIENT_ID)

    if not token or not phone_id or not target:
        print("ℹ️ Nota: Meta WhatsApp Cloud API preparada. (Configura WHATSAPP_CLOUD_API_TOKEN, WHATSAPP_PHONE_NUMBER_ID y WHATSAPP_RECIPIENT_ID en los Secrets de GitHub para envío automático).")
        return False

    url = f"https://graph.facebook.com/v18.0/{phone_id}/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": target,
        "type": "text",
        "text": {
            "preview_url": True,
            "body": message_text
        }
    }

    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode())
            print(f"📲 Mensaje a WhatsApp enviado con éxito: {res}")
            return True
    except Exception as e:
        print(f"⚠️ Error al enviar mensaje a WhatsApp Cloud API: {e}")
        return False

def generate_daily_whatsapp_summary(dataset):
    """
    Genera el formato institucional del resumen diario para el Canal de WhatsApp.
    Maneja el formato del dataset independientemente de si 'indicadores' es una lista o un diccionario.
    """
    raw_indicadores = dataset.get("indicadores", [])
    indicadores_dict = {}

    if isinstance(raw_indicadores, list):
        for item in raw_indicadores:
            if isinstance(item, dict) and "id" in item:
                indicadores_dict[item["id"]] = item
    elif isinstance(raw_indicadores, dict):
        indicadores_dict = raw_indicadores

    fecha = dataset.get("ultima_actualizacion", "Hoy")
    reflexion = "El monitoreo continuo de indicadores es esencial para la toma de decisiones financieras informadas."
    
    # Buscar reflexión de algún indicador o usar la general
    for ind in indicadores_dict.values():
        if "pregunta_estrategica" in ind:
            reflexion = ind["pregunta_estrategica"]
            break

    p2p = indicadores_dict.get("tc_paralelo", {}).get("valor", "11.75 Bs")
    oficial = indicadores_dict.get("tc_oficial", {}).get("valor", "12.13 Bs")
    inflacion = indicadores_dict.get("inflacion", {}).get("valor", "4.82%")
    oro = indicadores_dict.get("oro_intl", {}).get("valor", "$2.450 USD")
    reservas = indicadores_dict.get("reservas", {}).get("valor", "$3.617,3 MM")

    mensaje = (
        f"🇧🇴 *INDICADORES ECONÓMICOS DE BOLIVIA*\n"
        f"📅 *Fecha:* {fecha}\n\n"
        f"🟢 *Dólar Libre / P2P:* {p2p}\n"
        f"🔴 *Dólar Oficial (BCB):* {oficial}\n"
        f"🔴 *Inflación:* {inflacion}\n"
        f"🟢 *Oro Spot LBMA:* {oro}\n"
        f"🟡 *Reservas (RIN):* {reservas}\n\n"
        f"💡 *Reflexión Coyuntural:*\n{reflexion}\n\n"
        f"📊 *Dashboard Interactivo Completo:*\n"
        f"https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia_0349188327.html"
    )
    return mensaje

if __name__ == "__main__":
    test_dataset = {
        "ultima_actualizacion": "03 de Agosto de 2026",
        "indicadores": {
            "dolar_p2p": {"valor": "11.75"},
            "dolar_oficial": {"valor": "6.96"},
            "inflacion": {"valor": "9.23"},
            "oro_lbma": {"valor": "2450.00"},
            "reservas_netas": {"valor": "1970"}
        }
    }
    msg = generate_daily_whatsapp_summary(test_dataset)
    print("=== VISTA PREVIA DEL MENSAJE DE WHATSAPP ===")
    print(msg)
