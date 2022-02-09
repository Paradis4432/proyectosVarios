import requests
import json

url = 'https://csgoskins.gg/api/v1/basic-item-details'
payload = {
    "page": 249847660,
    "limit": 63
}
headers = {
  'Authorization': 'Bearer 45|F1GZVVhm42sqEWEnqdw1ddAINkBOMjfsH5mPR4DY',
  'Content-Type': 'application/json'
}

response = requests.request('GET', url, headers=headers, json=payload)
response.json()
print(response)