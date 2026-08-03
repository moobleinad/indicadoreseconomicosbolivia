import urllib.request

url = "https://www.danielsimons.xyz/2026/08/regimen-cambiario-el-debate-entre-la.html"

# Simulate Facebookexternalhit user-agent (Facebook Scraper)
headers = {
    "User-Agent": "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
        print("FACEBOOK SCRAPER FETCH STATUS: SUCCESS (200 OK)")
        
        print("\nOPENGRAPH TAGS RETURNED TO FACEBOOK:\n")
        for line in html.split("\n"):
            if "og:" in line or "twitter:" in line or "<title" in line:
                print(line.strip())
except Exception as e:
    print("ERROR FETCHING:", e)
