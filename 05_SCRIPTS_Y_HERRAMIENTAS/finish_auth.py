import os
import json
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/blogger']
CLIENT_SECRET_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\client_secret.json'
TOKEN_FILE = r'c:\Users\Usuario\Desktop\antigravity\blogger_danielsimons.xyz\token.json'
BLOG_ID = '433667097766389126'

def complete_auth(auth_code):
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, 
        SCOPES, 
        redirect_uri='urn:ietf:wg:oauth:2.0:oob'
    )
    
    flow.fetch_token(code=auth_code)
    creds = flow.credentials
    
    with open(TOKEN_FILE, 'w') as token:
        token.write(creds.to_json())

    print("SUCCESS: Token saved to token.json!")
    
    # Test connection
    service = build('blogger', 'v3', credentials=creds)
    blog = service.blogs().get(blogId=BLOG_ID).execute()
    print(f"CONNECTED TO BLOGGER: {blog.get('name')} ({blog.get('url')})")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        code = sys.argv[1].strip()
        complete_auth(code)
    else:
        print("Usage: python finish_auth.py <AUTH_CODE>")
