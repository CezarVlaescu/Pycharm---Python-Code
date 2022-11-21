import requests

url = "https://v6.exchangerate-api.com/v6/767a073272000147a74b981e/latest/USD"

payload = ""
headers = {
  'Authorization': 'Token 767a073272000147a74b981e'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)