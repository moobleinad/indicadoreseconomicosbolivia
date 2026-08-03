import urllib.request

url = "https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia.html"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        print("=== LIVE HTML FETCHED FROM BLOGGER ===")
        print("Length:", len(html))
        print("Contains img tag:", "<img" in html.lower())
        print("Contains 09.02_afiche:", "09.02_afiche" in html)
        print("Contains cdn webp:", "googleusercontent.com" in html)
        
        # Find where <img> tags are
        import re
        imgs = re.findall(r'<img[^>]+>', html, re.IGNORECASE)
        print("\nFound img tags in live HTML:")
        for img in imgs:
            print("  -", img)
except Exception as e:
    print("Error fetching live HTML:", e)
