import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/blogger']
CLIENT_SECRET_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\client_secret.json'

flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRET_FILE, 
    SCOPES, 
    redirect_uri='urn:ietf:wg:oauth:2.0:oob'
)

auth_url, _ = flow.authorization_url(prompt='consent')

print("="*80)
print("COPIA Y ABRE ESTA URL EN TU NAVEGADOR:")
print(auth_url)
print("="*80)

with open(r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\auth_url.txt', 'w') as f:
    f.write(auth_url)
