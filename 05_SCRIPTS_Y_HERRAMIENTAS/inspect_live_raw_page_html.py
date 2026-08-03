import urllib.request
import re

url = "https://www.danielsimons.xyz/p/indicadores-economicos-de-bolivia_0349188327.html"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
        matches = [m.start() for m in re.finditer("INDICADORES", html)]
        
        for idx in range(4, len(matches)):
            m_pos = matches[idx]
            print(f"\n--- OCCURRENCE {idx+1} AT POS {m_pos} ---")
            snippet = html[max(0, m_pos-100):min(len(html), m_pos+800)]
            print(snippet.encode("ascii", errors="replace").decode("ascii"))
            
except Exception as e:
    print("Error:", e)
