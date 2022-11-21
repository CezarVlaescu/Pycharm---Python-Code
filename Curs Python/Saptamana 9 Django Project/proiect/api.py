import requests

url = "https://v6.exchangerate-api.com/v6/d01788f6764c212c4285d31a/latest/USD"

payload = ""
headers = {
  'Authorization': 'Token a3fd725209d75d4c3b4da69afc22b2a4c7ce0f50'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
