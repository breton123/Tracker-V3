import requests
import json

def doesSetExist(payload):
     url = "http://127.0.0.1:8000/doesSetExist"
     headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json',
     }

     response = requests.post(url, headers=headers, json=payload, timeout=10)
     return response.json()