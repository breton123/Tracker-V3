import MetaTrader5 as mt5
from datetime import datetime

## Tested and working
#from openMt5 import openMt5

def getSetName(magic):
    setName = f"Unnamed set {magic}"
    orders = mt5.history_deals_get(0, datetime.now())

    for order in orders:
        order = order._asdict()
        orderMagic = order["magic"]
        comment = order["comment"]
        if orderMagic == magic:
            if comment != "" and "[sl" not in comment and "[tp" not in comment:
                setName = comment


    return setName

#openMt5(r"C:\Program Files\Vantage 2\terminal64.exe", "7451935", "uLo%9kmp", "VantageInternational-Demo")
#print(getSetName(4587))