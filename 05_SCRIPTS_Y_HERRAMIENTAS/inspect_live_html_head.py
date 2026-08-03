import urllib.request

url = "https://www.danielsimons.xyz/2026/08/regimen-cambiario-el-debate-entre-la.html"

headers = {
    "User-Agent": "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
}

req = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(req) as resp:
    html = resp.read().decode("utf-8")
    
head_end = html.find("</head>")
head_html = html[:head_end]

print("RAW LIVE HEAD TAGS (FIRST 3000 CHARS):\n")
for line in head_html.split("\n"):
    line_s = line.strip()
    if line_s.startswith("<meta") or line_s.startswith("<title") or "og:" in line_s or "twitter:" in line_s:
        print(line_s)
