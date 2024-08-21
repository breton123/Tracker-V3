import MetaTrader5 as mt5
from datetime import datetime

## Tested and working
#from openMt5 import openMt5

def getTradeAmount(magic):
    amount = 0
    orders = mt5.history_deals_get(0, datetime.now())
    for order in orders:
        order = order._asdict()
        if order["magic"] == magic:
            if order["type"] == 1:
                amount += 1
    return amount

#openMt5(r"C:\Program Files\Vantage 2\terminal64.exe", "7451935", "uLo%9kmp", "VantageInternational-Demo")
#print(getTradeAmount(3342))