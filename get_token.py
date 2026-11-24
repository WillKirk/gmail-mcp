from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# 1. Create the login flow from the credentials files
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)

# 2. Run the login: opens browser, returns credentials
creds = flow.run_local_server(port=0)

# 3. Make the tokens folder and save the credentials into it
tokens_dir = Path("tokens")
tokens_dir.mkdir(exist_ok=True)
(tokens_dir / "personal.json").write_text(creds.to_json())