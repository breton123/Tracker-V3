import MetaTrader5 as mt5
from datetime import datetime

## Tested and working
#from openMt5 import openMt5

tickets = []

def getProfit(magic):
     orders = mt5.history_deals_get(0, datetime.now())
     totalProfit = 0
     for order in orders:
          order = order._asdict()
          orderMagic = order["magic"]
          if order["type"] == 1:
               if orderMagic == magic:
                    profit = round(order["profit"], 2)
                    totalProfit += profit
     return totalProfit

#openMt5(r"C:\Program Files\Vantage 2\terminal64.exe", "7451935", "uLo%9kmp", "VantageInternational-Demo")
#print(getProfit(3342))
