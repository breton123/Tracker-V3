
import asyncio
import threading, time
from database.getAccounts import getAccounts
from trackingThread import track
from scripts.tasksSocket import listen_to_server


runningAccounts = []
user = "breton123"

class Account():
     def __init__(self, filePath, login, password, server, user):
          self.terminalFilePath = filePath
          self.login = login
          self.password = password
          self.server = server
          self.user = user

def run_async_code():
     # Create a new event loop for this thread
     loop = asyncio.new_event_loop()
     asyncio.set_event_loop(loop)

     # Run the async function
     loop.run_until_complete(listen_to_server())

thread = threading.Thread(target=run_async_code)
thread.start()

while True:
     accounts = getAccounts(user)
     for account in accounts["accounts"]:
          if account["enabled"]:
               if account["login"] not in runningAccounts:
                    AccountData = Account(account["terminalFilePath"], account["login"], account["password"], account["server"], account["user"])
                    trackerThread = threading.Thread(target=track, args=(AccountData,)).start()
                    runningAccounts.append(account["login"])
     time.sleep(30)
