import requests
import json

# Define the URL of the API endpoint
url = "http://127.0.0.1:8000/api/users/"

# Define your authentication token
token = "aef8b8ce3fb45cddc7f6ae8825776da3767d1d7d"

# Define headers with the token
headers = {
    "Authorization": f"Token {token}"
}

try:
    # Send a GET request to the endpoint with the token in headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

        # Print the data or process it as needed
        print(data)
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
