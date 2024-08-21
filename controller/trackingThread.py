
from datetime import datetime
import threading
import time
from database.createSet import createSet
from database.createSnapshot import createSnapshot
from database.doesSetExist import doesSetExist
from database.doesTradeExist import doesTradeExist
from database.insertTrade import insertTrade
from database.updateSet import updateSet
from scripts.getAllMagics import getAllMagics
from scripts.getDrawdown import getDrawdown
from scripts.getLotSizes import getLotSizes
from scripts.getProfit import getProfit
from scripts.getSetName import getSetName
from scripts.getTradeAmount import getTradeAmount
from scripts.getTradeTimes import getTradeTimes
from scripts.getWinRate import getWinRate
from scripts.openMt5 import openMt5
from scripts.terminalController import isTerminalOpen
from scripts.updateTrades import updateTrades

updateDelay = 1
snapshotDelay = 60000
enableOutput = False

def track(accountData):
     try:
          openMt5(accountData.terminalFilePath, accountData.login, accountData.password, accountData.server)
          lastSnapshot = 0

          ## Confirm to api that server is running

          while True:
               ## Checks to see if account is still enabled if not break
               enabled = True
               if not enabled:
                    break

               ## Check tasks

               newTrades = updateTrades(accountData.login, accountData.user)
               for trade in newTrades:
                    isTrade = doesTradeExist({
                         "id": trade["id"],
                         "user": trade["user"],
                         "account": trade["account"],
                         "magic": trade["set"]
                    })
                    isSet = doesSetExist({
                              "magic": trade["set"],
                              "account": accountData.login,
                              "user": accountData.user
                         })
                    if not isTrade:
                         if isSet:
                              insertTrade(trade)
                         else:
                              newObject = {
                              "magic": int(trade["set"]),
                              "account": int(accountData.login),
                              "user": str(accountData.user),
                              "profit": float(0),
                              "trades": int(0),
                              "maxDrawdown": float(0),
                              "profitFactor": float(0),
                              "returnOnDrawdown": float(0),
                              "openEquity": float(0),
                              "openDrawdown": float(0),
                              "minLotSize": float(0),
                              "maxLotSize": float(0),
                              "avgLotSize": float(0),
                              "wins": int(0),
                              "losses": int(0),
                              "winRate": int(0),
                              "minTradeTime": str(0),
                              "maxTradeTime": str(0),
                              "avgTradeTime": str(0),
                         }
                              createSet(newObject)
                              insertTrade(trade)
               snapshotTime = time.time()
               currentTime = str(datetime.now().isoformat())
               for magic in getAllMagics():
                    equity, drawdown, maxDrawdown = getDrawdown(magic, accountData.login, accountData.user)
                    profit = getProfit(magic)
                    trades = getTradeAmount(magic)
                    minLotSize, maxLotSize, avgLotSize = getLotSizes(magic)
                    wins, losses, winRate, profitFactor = getWinRate(magic, trades)
                    minTradeTime, maxTradeTime, avgTradeTime = getTradeTimes(magic)
                    try:
                         returnOnDrawdown = round(profit / maxDrawdown, 2)
                    except:
                         returnOnDrawdown = 0

                    #Update Set
                    if enableOutput:
                         print(f"\nSet Update for {magic}")
                         print(f"Equity: {equity}, Drawdown: {drawdown}, Max Drawdown: {maxDrawdown}")
                         print(f"Profit: {profit}")
                         print(f"Trades: {trades}")
                         print(f"MinLotSize: {minLotSize}, MaxLotSize: {maxLotSize}, AverageLotSize: {avgLotSize}")
                         print(f"Wins: {wins}, Losses: {losses}, WinRate: {winRate}")
                         print(f"MinTradeTime: {minTradeTime}, MaxTradeTime: {maxTradeTime}, AverageTradeTime: {avgTradeTime}")
                         print(f"Profit Factor: {profitFactor}, Return on Drawdown: {returnOnDrawdown}")

                    updateObject = {
                         "magic": int(magic),
                         "account": int(accountData.login),
                         "user": str(accountData.user),
                         "profit": float(profit),
                         "trades": int(trades),
                         "maxDrawdown": float(maxDrawdown),
                         "profitFactor": float(profitFactor),
                         "returnOnDrawdown": float(returnOnDrawdown),
                         "openEquity": float(equity),
                         "openDrawdown": float(drawdown),
                         "minLotSize": float(minLotSize),
                         "maxLotSize": float(maxLotSize),
                         "avgLotSize": float(avgLotSize),
                         "wins": int(wins),
                         "losses": int(losses),
                         "winRate": int(winRate),
                         "minTradeTime": str(minTradeTime),
                         "maxTradeTime": str(maxTradeTime),
                         "avgTradeTime": str(avgTradeTime),
                    }
                    if doesSetExist({
                         "magic": magic,
                         "account": accountData.login,
                         "user": accountData.user
                    }):
                         updateObject["name"] = str(getSetName(magic))
                         updateSet(updateObject)
                    else:
                         updateObject["name"] = str(getSetName(magic))
                         updateObject["strategy"] =  "-"
                         #print(updateObject)
                         createSet(updateObject)


                    if snapshotTime - lastSnapshot >= snapshotDelay:
                         snapshotObject = {
                         "magic": int(magic),
                         "account": int(accountData.login),
                         "user": str(accountData.user),
                         "totalProfit": float(profit),
                         "openProfit": float(equity),
                         "drawdown": float(drawdown),
                         "time": currentTime
                         }
                         createSnapshot(snapshotObject)
               if snapshotTime - lastSnapshot >= snapshotDelay:
                    lastSnapshot = snapshotTime

               if not isTerminalOpen(accountData.terminalFilePath):
                    openMt5(accountData.terminalFilePath, accountData.login, accountData.password, accountData.server)

               time.sleep(updateDelay)
     except:
          openMt5(accountData.terminalFilePath, accountData.login, accountData.password, accountData.server)
