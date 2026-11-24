from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# 1. Load the saved credentials from token file
creds = Credentials.from_authorized_user_file("tokens/personal.json", SCOPES)

# 2. Build Gmail API client using above credentials
service = build("gmail", "v1", credentials=creds)

messages = service.users().messages().list(userId="me", maxResults=5, q="from:amazon").execute()
print(messages)