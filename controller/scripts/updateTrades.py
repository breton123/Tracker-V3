import MetaTrader5 as mt5
import datetime as datetime
from datetime import datetime

from database.doesTradeExist import doesTradeExist
tickets = []

def updateTrades(account, user):
    global tickets
    orders = mt5.history_deals_get(0, datetime.now())
    openTrades = {}
    closedTrades = []
    for order in orders:
        order = order._asdict()
        orderMagic = order["magic"]
        order_id = order["ticket"]
        position = order["position_id"]
        entry = order["entry"]
        if entry == 0:
            if order_id not in tickets:
                orderType = order["type"]
                if orderType == 0:
                    orderType = "LONG"
                elif orderType == 1:
                    orderType = "SHORT"
                orderTime = order["time"]
                orderTime = datetime.fromtimestamp(orderTime)
                volume = order["volume"]
                price = round(order["price"],2)
                profit = round(order["profit"], 2)
                symbol = order["symbol"]
                newTrade = {
                    "id": int(order_id),
                    "account": int(account),
                    "user": str(user),
                    "entryTime": orderTime,
                    "exitTime": 0,
                    "volume": volume,
                    "entryPrice": price,
                    "exitPrice": 0,
                    "profit": profit,
                    "symbol": symbol,
                    "set": orderMagic,
                    "direction": orderType
                }
                openTrades[position] = newTrade
                tickets.append(order_id)
        else:
            try:
                orderTime = order["time"]
                orderTime = datetime.fromtimestamp(orderTime)
                holdTime = str(orderTime - openTrades[position]["entryTime"])
                orderTime = str(orderTime)

                price = round(order["price"],2)
                profit = round(order["profit"], 2)

                if openTrades[position]["direction"] == "SHORT":
                    openTrades[position]["entryTime"] = str(orderTime)
                    openTrades[position]["exitTime"] = str(openTrades[position]["entryTime"])
                else:
                    openTrades[position]["entryTime"] = str(openTrades[position]["entryTime"])
                    openTrades[position]["exitTime"] = str(orderTime)
                openTrades[position]["holdTime"] = str(holdTime)
                openTrades[position]["exitPrice"] = price
                openTrades[position]["profit"] = profit

                closedTrades.append(openTrades[position])
            except:
                pass

    return closedTrades
