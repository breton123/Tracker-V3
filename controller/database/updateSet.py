import requests
import json

def updateSet(set):
     url = "http://127.0.0.1:8000/updateSet"
     headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json',
     }

     response = requests.post(url, headers=headers, json=set, timeout=10)
     return response.json()