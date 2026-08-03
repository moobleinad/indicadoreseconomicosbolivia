import urllib.request

url = "https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia_0225498393.html"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        print("=== VERIFYING LIVE RENDERED DASHBOARD ===")
        print("HTML Size:", len(html))
        print("Contains econ-dashboard:", "econ-dashboard" in html)
        print("Contains indicatorContainer:", "indicatorContainer" in html)
        print("Contains Dólar Paralelo:", "Dólar Paralelo" in html or "tc_paralelo" in html)
        print("Contains 11.75 Bs:", "11.75" in html)
except Exception as e:
    print("Error fetching live page:", e)
