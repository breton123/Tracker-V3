import MetaTrader5 as mt5
import datetime as datetime
from datetime import datetime

## Tested and working
#from openMt5 import openMt5

def getWinRate(magic, trades):
    wins = 0
    losses = 0
    winProfit = 0
    lossProfit = 0
    orders = mt5.history_deals_get(0, datetime.now())
    for order in orders:
        order = order._asdict()
        if order["magic"] == magic:
            if order["reason"] == 4:
                if order["profit"] >= 0:
                    wins += 1
                    winProfit += order["profit"]
                elif order["profit"] < 0:
                    losses += 1
                    lossProfit += order["profit"]
    try:
        profitFactor = round(winProfit / abs(lossProfit), 2)
    except:
        profitFactor = 0
    try:
        return wins, losses, int(str(round((wins / trades)*100, 0)).replace(".0", "")), profitFactor
    except ZeroDivisionError as e:
        return wins, losses, 0, profitFactor


#openMt5(r"C:\Program Files\Vantage 2\terminal64.exe", "7451935", "uLo%9kmp", "VantageInternational-Demo")
#print(getWinRate(3342, 6))