import MetaTrader5 as mt5

from database.getMaxDrawdown import getMaxDrawdown


## Tested and working
#from openMt5 import openMt5

def getDrawdown(magic, account, user):
    positions = mt5.positions_get()


    equity = 0
    for position in positions:
        position = position._asdict()
        setMagic = position["magic"]
        profit = position["profit"]

        if setMagic == magic:
            equity += profit

    equity = round(equity,2)
    drawdown = 0

    if equity < 0:
        drawdown = equity

    ## Get max drawdown from db
    try:
        maxDrawdown = getMaxDrawdown(magic, account, user)["maxDrawdown"]
    except:
        maxDrawdown = 0

    if drawdown < maxDrawdown:
        maxDrawdown = drawdown

    return equity, drawdown, maxDrawdown



#openMt5(r"C:\Program Files\Vantage 2\terminal64.exe", "7451935", "uLo%9kmp", "VantageInternational-Demo")
#print(getDrawdown(2209))

