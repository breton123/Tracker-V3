import base64
import json
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from GET.getCardData import getCardData
from GET.getAccount import getAccount
from GET.getMaxDrawdown import getMaxDrawdown
from GET.getSnapshots import getSnapshots, getSnapshotsGraph, getSnapshotsWithMagic
from GET.getTrades import getTrades
from GET.getUsers import getUsers
from GET.getSet import getSet
from POST.checkLogin import checkLogin
from POST.createAccount import createAccount
from POST.createSnapshot import createSnapshot
from POST.doesSetExist import doesSetExist
from POST.doesTradeExist import doesTradeExist
from POST.insertTrade import insertTrade
from POST.removeUser import removeUser
from POST.removeAccount import removeAccount
from POST.updateAccount import updateAccount
from POST.updateSet import updateSet
from POST.removeSet import removeSet
from POST.createSet import createSet
from schemas import AccountCreate, AccountGet, AccountRemove, AccountRemoveResponse, AccountResponse, AccountUpdate, AccountsResponse, CheckLogin, CreateSetResponse, DrawdownResponse, GetSnapShot, GetSnapShotMagic, InsertSetInput, SetCreate, SetExistenceCheck, SetRemove, SetResponse, SetUpdate, SetsResponse, Snapshot, SnapshotResponse, SnapshotsGraphResponse, SnapshotsResponse, Trade, TradeExistenceCheck, UserCreate, UserRemove, UserResponse, SetsGet, SetGet, AccountsGet
from POST.createUser import createUser
from GET.getSets import getSets
from GET.getAccounts import getAccounts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # URL for the website
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/createUser/", response_model=UserResponse)
def create_user(user: UserCreate):
     try:
          user_data = createUser(user.username, user.email, user.password, user.type)
          return UserResponse(**user_data)
     except Exception as e:
          raise HTTPException(status_code=500, detail=e)

@app.post("/checkLogin/", response_model=UserResponse)
def check_login(user: CheckLogin):
     try:
          user_data = checkLogin(user.email, user.username, user.password)
          if user_data == None:
               raise HTTPException(status_code=401, detail=e)
          return UserResponse(**user_data)
     except Exception as e:
          raise HTTPException(status_code=500, detail=e)

@app.delete("/removeUser/", response_model=UserRemove)
def remove_user(user: UserRemove):
     try:
          username = removeUser(user.username)
          return UserRemove(**username)
     except Exception as e:
          raise HTTPException(status_code=500, detail=e)

## Update User

@app.get("/getUsers")
def get_users():
     try:
          users = getUsers()
          return users
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/getSets", response_model=SetsResponse)
def get_sets(payload: SetsGet):
     try:
          sets = getSets(payload.user, payload.account)
          return SetsResponse(**sets)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/getTrades")
def get_trades(payload: SetGet):
     try:
          trades = getTrades(payload.user, payload.account, payload.magic)
          return JSONResponse(trades)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/getCardData")
def get_sets(payload: SetsGet):
     try:
          data = getCardData(payload.user, payload.account)
          return JSONResponse(data)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/getSet", response_model=SetResponse)
def get_sets(payload: SetGet):
     try:
          set = getSet(payload.user, payload.account, payload.magic)
          return SetResponse(**set)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/getMaxDrawdown")
def get_sets(payload: SetGet):
     try:
          maxDrawdown = getMaxDrawdown(payload.user, payload.account, payload.magic)
          return JSONResponse(maxDrawdown["sets"][0])
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/createSet", response_model=CreateSetResponse)
def create_set(payload: SetCreate):
    try:
        result = createSet(
            magic=payload.magic,
            name=payload.name,
            strategy=payload.strategy,
            profit=payload.profit,
            trades=payload.trades,
            maxDrawdown=payload.maxDrawdown,
            profitFactor=payload.profitFactor,
            returnOnDrawdown=payload.returnOnDrawdown,
            account=payload.account,
            user=payload.user,
            openEquity=payload.openEquity,
            openDrawdown=payload.openDrawdown,
            minLotSize=payload.minLotSize,
            maxLotSize=payload.maxLotSize,
            avgLotSize=payload.avgLotSize,
            wins=payload.wins,
            losses=payload.losses,
            winRate=payload.winRate,
            minTradeTime=payload.minTradeTime,
            maxTradeTime=payload.maxTradeTime,
            avgTradeTime=payload.avgTradeTime
        )
        return CreateSetResponse(**result['set'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/removeSet/")
def remove_set(payload: SetRemove):
     try:
          deleted_set = removeSet(
               magic=payload.magic,
               account=payload.account,
               user=payload.user
          )
          if not deleted_set:
               raise HTTPException(status_code=404, detail="Set not found")
          return {"message": "Set deleted successfully", "deleted_set": deleted_set}
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/doesSetExist", response_model=bool)
def check_set_existence(payload: SetExistenceCheck):
    try:
        exists = doesSetExist(
            magic=payload.magic,
            account=payload.account,
            user=payload.user
        )
        return exists
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/doesTradeExist", response_model=bool)
def check_trade_existence(payload: TradeExistenceCheck):
    try:
        exists = doesTradeExist(
            magic=payload.magic,
            account=payload.account,
            user=payload.user,
            id=payload.id
        )
        return exists
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/updateSet")
def update_set(request: SetUpdate):
    try:
        result = updateSet(
            magic=request.magic,
            account=request.account,
            user=request.user,
            name=request.name,
            strategy=request.strategy,
            profit=request.profit,
            trades=request.trades,
            maxDrawdown=request.maxDrawdown,
            profitFactor=request.profitFactor,
            returnOnDrawdown=request.returnOnDrawdown,
            openEquity=request.openEquity,
            openDrawdown=request.openDrawdown,
            minLotSize=request.minLotSize,
            maxLotSize=request.maxLotSize,
            avgLotSize=request.avgLotSize,
            wins=request.wins,
            losses=request.losses,
            winRate=request.winRate,
            minTradeTime=request.minTradeTime,
            maxTradeTime=request.maxTradeTime,
            avgTradeTime=request.avgTradeTime
        )
        return result
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/getAccounts", response_model=AccountsResponse)
def get_sets(payload: AccountsGet):
     try:
          accounts = getAccounts(payload.user)
          return AccountsResponse(**accounts)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/getAccount")
def get_sets(payload: AccountGet):
     try:
          account = getAccount(payload.user, payload.login)
          return JSONResponse(account)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

# API endpoint to update an account
@app.put("/updateAccount/")
def update_account(payload: AccountUpdate):
     try:
          currentDetails = getAccount(payload.user, payload.login)
          if payload.password is None:
               payload.password = currentDetails["password"]
          if payload.server is None:
               payload.server = currentDetails["server"]
          if payload.deposit is None:
               payload.deposit = currentDetails["deposit"]
          if payload.enabled is None:
               payload.enabled = currentDetails["enabled"]
          account = updateAccount(
               login=payload.login,
               user=payload.user,
               password=payload.password,
               name=payload.name,
               server=payload.server,
               deposit=payload.deposit,
               enabled=payload.enabled
          )
          if not account:
               raise HTTPException(status_code=404, detail="Account not found")
          return account
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/createAccount/")
def create_account(payload: AccountCreate):
     try:
          account = createAccount(payload.login, payload.password, payload.server, payload.deposit, payload.user, payload.name, payload.terminalFilePath)
          return AccountCreate(**account)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/removeAccount/", response_model=AccountRemoveResponse)
def delete_account(payload: AccountRemove):
     try:
          response = removeAccount(payload.login, payload.username)
          return AccountRemoveResponse(**response)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/insertTrade")
def insert_trade(trade: Trade):
     try:
          trade_data = trade.dict()
          response = insertTrade(trade_data)
          return Trade(**response)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))


@app.post("/createSnapshot", response_model=SnapshotResponse)
def create_snapshot(payload: Snapshot):
     try:
          result = createSnapshot(
               magic=payload.magic,
               account=payload.account,
               user=payload.user,
               current_time=payload.time,
               totalProfit=payload.totalProfit,
               openProfit=payload.openProfit,
               drawdown=payload.drawdown

          )
          return SnapshotResponse(**result['snapshot'])
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/getSnapshotsWithMagic", response_model=SnapshotsResponse)
def create_snapshot(payload: GetSnapShotMagic):
     try:
          result = getSnapshotsWithMagic(
               magic=payload.magic,
               account=payload.account,
               user=payload.user

          )
          return SnapshotsResponse(**result)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/getSnapshots", response_model=SnapshotsResponse)
def create_snapshot(payload: GetSnapShot):
     try:
          result = getSnapshots(
               account=payload.account,
               user=payload.user

          )
          return SnapshotsResponse(**result)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

@app.post("/getSnapshotsGraph")
def create_snapshot(payload: GetSnapShot):
     try:
          drawdownData, equityData, magics = getSnapshotsGraph(
               account=payload.account,
               user=payload.user

          )
          response = {
               "drawdownData": drawdownData,
               "equityData": equityData,
               "magics": magics
          }
          return JSONResponse(response)
     except Exception as e:
          raise HTTPException(status_code=500, detail=str(e))

apps = {}
controllers = {}
accounts = {}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
     await websocket.accept()
     username = None
     try:
          while True:
               data = await websocket.receive_text()
               message = json.loads(data)
               if message.get("type") == "connect":
                    username = message["username"]
                    source = message["source"]

                    if source == "app":
                         account = message["account"]
                         if username not in apps:
                              apps[username] = websocket
                              accounts[username] = account
                         if username in controllers:
                              await controllers[username].send_json({
                                   "message": f"Set Data",
                                   "newData": True,
                                   "account" : account
                              })
                              await websocket.send_json({
                                   "message": f"Connected {username} from {source}",
                                   "controller": True
                              })
                         else:
                              await websocket.send_json({
                                   "message": f"Connected {username} from {source}",
                                   "controller": False
                              })

                    elif source == "controller":
                         if username not in controllers:
                              controllers[username] = websocket
                         if username in apps:
                              account = accounts[username]
                              await apps[username].send_json({
                                   "message": f"Connected {username} from {source}",
                                   "controller": True
                              })

                              await websocket.send_json({
                                        "message": f"Set Data",
                                        "newData": True,
                                        "account" : account
                                   })
                         else:
                              await websocket.send_json({
                                   "message": f"Connected {username} from {source}"
                              })

                    print(f"{username} connected from {source}")
               elif message.get("type") == "upload":
                    if username in controllers:
                         await controllers[username].send_json(message)
               else:
                    print(f"Received from {username}: {message}")
                    if message["source"] == "controller":
                         if message["message"] == "Set Data":
                              if username in apps:
                                   await apps[username].send_json({
                                        "message": "Set Data",
                                        "previousProfile": message["previousProfile"],
                                        "profiles": message["profiles"],
                                        "profileSets": message["profileSets"],
                                        "controller": True
                                   })
                    if message["source"] == "app":
                         if message["message"] == "Set Data":
                              account = message["account"]
                              if username in controllers:
                                   await controllers[username].send_json({
                                        "message": f"Set Data",
                                        "newData": False,
                                        "account": account,
                                        "profile": message["profile"]
                              })

                    await websocket.send_json({
                         "message": f"Recieved {username}"
                    })

     except WebSocketDisconnect:
          if username:
               try:
                    if apps[username] == websocket:
                         del apps[username]
                         del accounts[username]
                         print(f"{username} disconnected from App")
                    elif controllers[username] == websocket:
                         del controllers[username]
                         if username in apps:
                              await apps[username].send_json({
                                   "message": f"Connected {username} from {source}",
                                   "controller": False
                              })
                         print(f"{username} disconnected from Controller")
                    else:
                         print(f"{username} disconnected from Unknown")
               except:
                    print(f"Failed to disconnect for {username}")
                    print(f"Apps: {apps}")
                    print(f"Controllers {controllers}")



@app.get("/")
def read_root():
     return {"message": "Welcome to the FastAPI app"}
