import requests
import json
import auth

# Get an access token from Microsoft Identity platform
tenant_id = auth.tenant_id
client_id = auth.client_id
client_secret = auth.client_secret
authority_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"

body = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "https://graph.microsoft.com/.default",
}

token_response = requests.post(authority_url, data=body)
token = token_response.json().get('access_token')

# Use the token to make an API request
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# API call to get all users
url = "https://graph.microsoft.com/v1.0/users"
response = requests.get(url, headers=headers)

# Print the result
users = response.json()
print(json.dumps(users, indent=4))