import urllib.request

url = "https://www.danielsimons.xyz/2026/08/de-la-idea-escolar-al-proyecto-ordenado.html"

headers = {
    "User-Agent": "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
        print("STATUS:", resp.status)
        print("FINAL URL:", resp.geturl())
        
        print("\nOPENGRAPH TAGS IN BTH POST:\n")
        for line in html.split("\n"):
            line_s = line.strip()
            if "og:" in line_s or "twitter:" in line_s or "<title" in line_s:
                print(line_s)
except Exception as e:
    print("ERROR:", e)
