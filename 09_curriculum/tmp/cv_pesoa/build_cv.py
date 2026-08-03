from pathlib import Path
from PIL import Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
    PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(r"C:\Users\Usuario\Desktop\daniel simons\curriculum")
TMP = ROOT / "tmp" / "cv_pesoa"
OUT_DIR = ROOT / "convocatoria pesoa"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "CV Daniel Simons - Pesoa.pdf"

# Crop the portrait from the first page of the original CV.
src_page = Image.open(TMP / "source" / "page-1.png")
portrait = src_page.crop((0, 0, 333, 362))
PORTRAIT = TMP / "foto_daniel_simons.png"
portrait.save(PORTRAIT)

font_dir = Path(r"C:\Windows\Fonts")
font_map = {
    "Arial": font_dir / "arial.ttf",
    "Arial-Bold": font_dir / "arialbd.ttf",
    "Arial-Italic": font_dir / "ariali.ttf",
}
for name, path in font_map.items():
    pdfmetrics.registerFont(TTFont(name, str(path)))

RED = colors.HexColor("#B20D2A")
GRAY = colors.HexColor("#666666")
LIGHT_GRAY = colors.HexColor("#808080")
BLACK = colors.HexColor("#111111")

PAGE_W, PAGE_H = A4
LEFT = 18 * mm
RIGHT = 18 * mm
TOP = 30 * mm
BOTTOM = 18 * mm

styles = {
    "name": ParagraphStyle(
        "Name", fontName="Arial-Bold", fontSize=25, leading=26,
        textColor=BLACK, spaceAfter=2 * mm
    ),
    "contact": ParagraphStyle(
        "Contact", fontName="Arial", fontSize=9.3, leading=11,
        textColor=GRAY, spaceAfter=2.5 * mm
    ),
    "h1": ParagraphStyle(
        "Heading", fontName="Arial-Bold", fontSize=11.2, leading=13,
        textColor=RED, spaceBefore=2.5 * mm, spaceAfter=1.2 * mm,
        keepWithNext=True
    ),
    "body": ParagraphStyle(
        "Body", fontName="Arial", fontSize=9.6, leading=12.3,
        textColor=BLACK, spaceAfter=1.6 * mm
    ),
    "compact": ParagraphStyle(
        "Compact", fontName="Arial", fontSize=9.25, leading=11.6,
        textColor=BLACK, spaceAfter=0.7 * mm
    ),
    "job": ParagraphStyle(
        "Job", fontName="Arial-Bold", fontSize=9.8, leading=12,
        textColor=BLACK, spaceBefore=1.2 * mm, spaceAfter=0.5 * mm
    ),
    "bullet": ParagraphStyle(
        "Bullet", fontName="Arial", fontSize=9.25, leading=11.5,
        leftIndent=5 * mm, firstLineIndent=-3.5 * mm, bulletIndent=1.2 * mm,
        spaceAfter=0.4 * mm
    ),
}


def p(text, style="body"):
    return Paragraph(text, styles[style])


def bullet(text):
    return Paragraph(text, styles["bullet"], bulletText="•")


def section(title):
    return [
        Paragraph(title, styles["h1"]),
        HRFlowable(width="100%", thickness=0.8, color=RED, spaceAfter=1.7 * mm),
    ]


def page_decor(canvas, doc):
    canvas.saveState()
    page = canvas.getPageNumber()
    canvas.setFont("Arial-Bold", 7.3)
    canvas.setFillColor(LIGHT_GRAY)
    canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 10.5 * mm, "DANIEL SIMONS  |  CURRÍCULUM VITAE")
    canvas.setFont("Arial", 7)
    canvas.drawCentredString(PAGE_W / 2, 9 * mm, f"Daniel Simons   ·   +591 65050351   ·   Página {page}")
    if page == 1:
        canvas.drawImage(
            str(PORTRAIT), PAGE_W - RIGHT - 23 * mm, PAGE_H - 39 * mm,
            width=21 * mm, height=23 * mm, preserveAspectRatio=True,
            anchor="c", mask="auto"
        )
    canvas.restoreState()


frame = Frame(
    LEFT, BOTTOM, PAGE_W - LEFT - RIGHT, PAGE_H - TOP - BOTTOM,
    leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0
)
doc = BaseDocTemplate(
    str(OUT), pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT,
    topMargin=TOP, bottomMargin=BOTTOM,
    title="Currículum Vitae - Daniel Simons",
    author="Daniel Simons"
)
doc.addPageTemplates(PageTemplate(id="cv", frames=[frame], onPage=page_decor))

story = []

# PAGE 1
story += [
    Paragraph("DANIEL SIMONS", styles["name"]),
    Paragraph(
        "danielbsimons@gmail.com&nbsp;&nbsp; · &nbsp;&nbsp;+591 65050351<br/>"
        "B. Est. Argentina / C. José V. Solíz No 3070&nbsp;&nbsp; · &nbsp;&nbsp;48 AÑOS",
        styles["contact"]
    ),
]
story += section("EXPERIENCIA")
story += [
    p("<b>Sinergia Solutions - Tecnología en Refrigeración (2023-2025)</b><br/>"
      "Administrativo comercial<br/>Santa Cruz - Bolivia", "compact"),
    Spacer(1, 1.5 * mm),
    p("<b>Administrador comercial (2021-2023)</b><br/>"
      "Administrador de personal de ventas y marketing.<br/>"
      "Ofertangas - Santa Cruz - Bolivia", "compact"),
    Spacer(1, 1.5 * mm),
    p("<b>Analista de planificación y proyectos (2018-2020)</b><br/>"
      "Grupo SION Inmobiliaria Kintas s.r.l.<br/>Santa Cruz, Bolivia", "compact"),
    Spacer(1, 1.5 * mm),
    p("<b>Coordinación Administrativa (2015-2018)</b><br/>"
      "Departamento de planificación<br/>"
      "Secretaría Municipal de Seguridad Ciudadana - Gobierno Autónomo Municipal de Santa Cruz<br/>"
      "Santa Cruz, Bolivia", "compact"),
    Spacer(1, 1.5 * mm),
    p("<b>Anteriormente:</b>", "compact"),
    bullet("Administrativo y auxiliar administrativo en Constructora Quebracho. (Manejo de personal)"),
    bullet("Asesor de micro negocios en la empresa Servidor S.A."),
    bullet("Asistente técnico para la Escuela de Proyectos de la CIDOB."),
    bullet("Diseño y administración de campañas publicitarias en redes sociales y Google."),
    Spacer(1, 1 * mm),
    p("Docente de Taller de ideas de negocio Instituto ILACE. Docente de Proyectos de emprendimientos "
      "productivos Instituto ILACE. Docente de Taller de modalidad de grado Instituto ILACE.", "compact"),
]
story += section("SKILLS")
story += [
    bullet("Autogestión y trabajo por metas."),
    bullet("Dinámico y versátil."),
    bullet("Metódico, planificado y organizado."),
]
story += section("REFERENCIAS")
story += [
    p("<b>Ing. Héctor Cáceres</b><br/>GERENTE GENERAL - SINERGIA SOLUTIONS<br/>72606967", "compact"),
    p("<b>Ing. Gabriel Simons</b><br/>Jefe de producción - ALICORP<br/>72131765", "compact"),
    PageBreak(),
]

# PAGE 2
story += section("EDUCACIÓN")
education = [
    ("Cursos de POSTGRADO en Formulación y Gestión de Proyectos (2013-2015)",
     "Escuela de Negocios UAGRMBS<br/>Santa Cruz, Bolivia"),
    ("Economía (Licenciatura)",
     "Universidad Autónoma Gabriel René Moreno<br/>Santa Cruz, Bolivia"),
    ("Curso de Gestión de Alcance, Tiempo y Costo (PMI - PMBOK) (2013)",
     "Escuela de Negocios UAGRMBS<br/>Santa Cruz, Bolivia"),
    ("Curso de Gestión de calidad, Recursos humanos y comunicaciones (PMI - PMBOK) (2014)",
     "Escuela de Negocios UAGRMBS<br/>Santa Cruz, Bolivia"),
    ("Curso de Gestión de riesgos, adquisiciones, interesados (PMI - PMBOK) (2014)",
     "Escuela de Negocios UAGRMBS<br/>Santa Cruz, Bolivia"),
    ("Curso de Fundamentos de la escritura en español (2016)",
     "Tecnológico de Monterrey - Coursera (On line)<br/>Santa Cruz, Bolivia"),
    ("Curso especializado de MARKETING GERENCIAL (Curso) 2021",
     "Universidad de Chile - Coursera (On line)<br/>Santa Cruz, Bolivia"),
]
for title, detail in education:
    story.append(KeepTogether([
        p(f"<b>{title}</b><br/>{detail}", "compact"),
        Spacer(1, 1.25 * mm),
    ]))
story += [
    p("<b>Certificación GOOGLE, de Marketing DIGITAL al 100 % completado (Demostrable).</b>", "compact"),
    p("<b>Certificación ADS Expert by Aleph Consulting al 60 % de avance (Demostrable).</b>", "compact"),
]
story += section("SKILLS")
story += [
    bullet("Autogestión y trabajo por metas."),
    bullet("Dinámico y versátil."),
    bullet("Metódico, planificado y organizado."),
]
story += section("REFERENCIAS")
story += [
    p("<b>Ing. Héctor Cáceres</b><br/>GERENTE GENERAL - SINERGIA SOLUTIONS<br/>72606967", "compact"),
    p("<b>Ing. Gabriel Simons</b><br/>Jefe de producción - ALICORP<br/>72131765", "compact"),
    PageBreak(),
]

# PAGE 3
story += section("OTROS")
story += [
    p("<b>HABILIDADES:</b>", "job"),
    p("Gestión y planificación certificada.<br/>"
      "Buen manejo financiero y de proyectos.<br/>"
      "Buen manejo de herramientas publicitarias “ADS”.<br/>"
      "Operador de Microsoft Office.<br/>"
      "Excelente redacción.<br/>"
      "Análisis numérico y analítica.<br/>"
      "Buen manejo y rápido aprendizaje de softwares.<br/>"
      "Diseño gráfico y de video.", "compact"),
    p("<b>IDIOMAS:</b>", "job"),
    p("<b>Inglés</b>&nbsp;&nbsp;&nbsp; Nivel Oral: Básico&nbsp;&nbsp;&nbsp; Nivel Escrito: Básico&nbsp;&nbsp;&nbsp; "
      "Nivel Lectura: Medio alto", "compact"),
]
story += section("REFERENCIAS")
references = [
    ("Ing. Carlos Simons Rocha", "Ex gerente de Constructora Quebracho", "Celular: 76020132"),
    ("Ing. Pablo Sesgua", "Ex Jefe de Planificación Inmobiliaria Kintas Grupo SION", "Celular: 72690937"),
    ("Lic. José Negrete", "Ex Secretario de Seguridad Ciudadana Gobierno Autónomo Municipal SCZ", "Celular: 77395905"),
    ("Lic. Jaime Vargas", "Ex Director de Cultura de la Casa del Cultura Santa Cruz", "Celular: 79878767"),
    ("Ing. Gabriel Simons Rocha", "Jefe de Producción ALICORP", "Celular: 72131765"),
    ("Ing. Héctor Cáceres", "GERENTE GENERAL SINERGIA SOLUTIONS", "Celular: 72606967"),
]
for name, role, phone in references:
    story.append(p(f"<b>{name}</b><br/>{role}<br/>{phone}", "compact"))

doc.build(story)
print(OUT)
