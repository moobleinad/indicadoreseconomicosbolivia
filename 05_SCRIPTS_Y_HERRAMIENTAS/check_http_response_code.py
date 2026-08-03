import urllib.request

url = "https://www.danielsimons.xyz/2026/08/regimen-cambiario-el-debate-entre-la.html"

# Test standard browser user-agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req) as resp:
        print("STANDARD BROWSER STATUS:", resp.status)
        print("FINAL URL:", resp.geturl())
except Exception as e:
    print("BROWSER ERROR:", e)

# Test Facebook Bot user-agent
fb_headers = {
    "User-Agent": "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
}
req_fb = urllib.request.Request(url, headers=fb_headers)
try:
    with urllib.request.urlopen(req_fb) as resp_fb:
        print("FACEBOOK BOT STATUS:", resp_fb.status)
        print("FACEBOOK FINAL URL:", resp_fb.geturl())
except Exception as e:
    print("FACEBOOK ERROR:", e)
