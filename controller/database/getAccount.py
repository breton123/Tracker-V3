import requests
import json

def getAccount(user, account):
     url = "http://127.0.0.1:8000/getAccount"
     headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json',
     }
     payload = {
          "user": user,
          "login": account
     }
     response = requests.post(url, headers=headers, json=payload, timeout=10)
     return response.json()
