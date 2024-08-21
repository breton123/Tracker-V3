import MetaTrader5 as mt5
from datetime import datetime

## Tested and working
#from openMt5 import openMt5

def getAllMagics():
    magics = []

    orders = mt5.history_deals_get(0, datetime.now())
    for order in orders:
        order = order._asdict()
        if order["magic"] not in magics:
            if str(order["magic"]) != "0":
                    magics.append(order["magic"])


    positions = mt5.positions_get()
    for position in positions:
        position = position._asdict()
        if position["magic"] not in magics:
            if str( position["magic"]) != "0":
                magics.append(position["magic"])


    return magics

#openMt5(r"C:\Program Files\Vantage 2\terminal64.exe", "7451935", "uLo%9kmp", "VantageInternational-Demo")
#print(getAllMagics())