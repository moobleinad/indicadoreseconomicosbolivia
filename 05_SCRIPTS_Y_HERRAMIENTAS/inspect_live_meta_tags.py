import urllib.request
import re

url = "https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia.html"
req = urllib.request.Request(url, headers={"User-Agent": "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        print("=== OPENGRAPH & TWITTER META TAGS IN LIVE HEAD ===")
        
        meta_tags = re.findall(r'<meta[^>]+>', html, re.IGNORECASE)
        og_tags = [m for m in meta_tags if "og:" in m.lower() or "twitter:" in m.lower()]
        
        for m in og_tags:
            print("  -", m)
            
        if not og_tags:
            print("WARNING: NO OPENGRAPH TAGS FOUND IN HEAD!")
except Exception as e:
    print("Error fetching live meta tags:", e)
