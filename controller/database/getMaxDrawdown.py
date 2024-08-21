import requests
import json

def getMaxDrawdown(magic, login, user):
     url = "http://127.0.0.1:8000/getMaxDrawdown"
     headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json',
     }

     payload = {
          "magic": magic,
          "account": login,
          "user": user
     }
     response = requests.post(url, headers=headers, json=payload, timeout=10)
     return response.json()