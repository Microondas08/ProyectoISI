import requests

url = "https://google-search3.p.rapidapi.com/api/v1/images/q=tesla"

payload = "{\r\n    \"query\": \"q=google+search+api&num=100\",\r\n    \"website\": \"https://rapidapi.com\"\r\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "a86c5d4cf5msh01e7347aa790ac7p12391ajsn88ddaf12958a",
    'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }

response = requests.request("GET", url, data=payload, headers=headers)


print(response.json()["image_results"][1]["image"]["src"])

