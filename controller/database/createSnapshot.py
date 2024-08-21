import requests
import json

def createSnapshot(snapshot):
     url = "http://127.0.0.1:8000/createSnapshot"
     headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json',
     }

     response = requests.post(url, headers=headers, json=snapshot, timeout=10)
     return response.json()
