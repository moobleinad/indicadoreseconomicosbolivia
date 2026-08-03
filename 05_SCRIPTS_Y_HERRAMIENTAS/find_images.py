import re
xml_file = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\03_TEMAS_Y_PLANTILLAS_XML\03.02_tema_optimizado\v25_theme_optimizado.xml'

with open(xml_file, 'r', encoding='utf-8') as f:
    content = f.read()

urls = re.findall(r'https://blogger\.googleusercontent\.com/img/b/[^\s"\'\>]+', content)
for u in urls[:10]:
    print(u)
