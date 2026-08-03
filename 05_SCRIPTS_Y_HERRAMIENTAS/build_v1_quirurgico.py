import os
import xml.etree.ElementTree as ET

base_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\0 theme_optimizado_danielsimons.xml"
output_path = r"c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\tema_optimizado\v1_theme_optimizado.xml"

with open(base_path, "r", encoding="utf-8") as f:
    xml_content = f.read()

# Replace the chatbot trigger button styles with a LARGER, HIGHER VISIBILITY GOLD BUTTON
old_trigger_style = """    #ds-ai-trigger {
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
    }"""

new_trigger_style = """    #ds-ai-trigger {
      background: linear-gradient(135deg, #ffd700 0%, #cca010 100%);
      color: #000000 !important;
      border: 2px solid #ffffff;
      padding: 16px 28px;
      border-radius: 50px;
      cursor: pointer;
      box-shadow: 0 10px 35px rgba(255, 215, 0, 0.6), 0 0 15px rgba(255, 255, 255, 0.4);
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 800;
      font-size: 16px;
      letter-spacing: 0.5px;
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    #ds-ai-trigger span {
      font-size: 22px;
    }"""

if old_trigger_style in xml_content:
    xml_content = xml_content.replace(old_trigger_style, new_trigger_style)
else:
    # Target replacement via sub-string if formatting differs slightly
    target_substr = "background: linear-gradient(135deg, #1b365d 0%, #bca772 100%);"
    new_bg = "background: linear-gradient(135deg, #ffd700 0%, #cca010 100%); color: #000000 !important; padding: 16px 28px; font-size: 16px; font-weight: 800; border: 2px solid #ffffff; box-shadow: 0 10px 35px rgba(255, 215, 0, 0.6);"
    xml_content = xml_content.replace(target_substr, new_bg)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_content)

try:
    ET.parse(output_path)
    print("SUCCESS: v1_theme_optimizado.xml generated and passed XML test!")
except Exception as e:
    print("XML ERROR:", e)
