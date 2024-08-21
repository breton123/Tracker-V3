import requests
import json

def insertTrade(trade):
     url = "http://127.0.0.1:8000/insertTrade"
     headers = {
          'accept': 'application/json',
          'Content-Type': 'application/json',
     }

     response = requests.post(url, headers=headers, json=trade, timeout=10)
     return response.json()
