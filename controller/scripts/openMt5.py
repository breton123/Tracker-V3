import MetaTrader5 as mt5
import datetime as datetime

def openMt5(terminalFilePath, login, password, server):
     if not mt5.initialize(terminalFilePath, login=int(login), password=password, server=server):
          print("initialize() failed, error code =",mt5.last_error())
          quit()