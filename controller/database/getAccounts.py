import requests
import json

def getAccounts(user):
     url = "http://127.0.0.1:8000/getAccounts"
     headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json',
     }
     payload = {
          "user": user
     }
     response = requests.post(url, headers=headers, json=payload, timeout=10)
     return response.json()
