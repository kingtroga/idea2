import requests

access_token = "c310020b3769b40be179be8b60396b161b5c7512"
logout_url = "http://127.0.0.1:8000/api/account/logout/"

headers = {
    "Authorization": f"Bearer {access_token}"
}

response = requests.post(logout_url, headers=headers)

if response.status_code == 200:
    print(response.json())
    print("Logged out successfully")
else:
    print("Logout failed with status code:", response.status_code)
