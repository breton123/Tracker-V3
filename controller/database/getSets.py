import requests
import json

def getSets(user, account):
     url = "http://127.0.0.1:8000/getSets"
     headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json',
     }
     payload = {
          "user": user,
          "account": account,
     }
     response = requests.post(url, headers=headers, json=payload, timeout=10)
     return response.json()["sets"]
