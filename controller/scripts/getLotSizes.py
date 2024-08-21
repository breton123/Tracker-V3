import MetaTrader5 as mt5
from datetime import datetime

## Tested and working
#from openMt5 import openMt5

def getLotSizes(magic):
    lotSizes = []
    orders = mt5.history_deals_get(0, datetime.now())
    for order in orders:
        order = order._asdict()
        if order["magic"] == magic:
            lotSizes.append(order["volume"])

    positions = mt5.positions_get()
    for position in positions:
        position = position._asdict()
        if position["magic"] == magic:
            lotSizes.append(position["volume"])

    minLotSize = min(lotSizes)
    maxLotSize = max(lotSizes)
    avgLotSize = round(sum(lotSizes) / len(lotSizes),2)

    return minLotSize, maxLotSize, avgLotSize


#openMt5(r"C:\Program Files\Vantage 2\terminal64.exe", "7451935", "uLo%9kmp", "VantageInternational-Demo")
#print(getLotSizes(1457))
