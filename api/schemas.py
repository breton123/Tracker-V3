# schemas.py
from datetime import datetime
from typing import List
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
     username: str
     email: EmailStr
     password: str
     type: str = "full"

class CheckLogin(BaseModel):
     username: str
     email: str
     password: str

class UserRemove(BaseModel):
     username: str

# Define the response schema
class UserResponse(BaseModel):
     username: str
     email: EmailStr
     type: str

     class Config:
          orm_mode = True

class SetsGet(BaseModel):
     user: str
     account: int

class SetResponse(BaseModel):
    magic: str
    name: str
    strategy: str
    profit: float
    maxDrawdown: float
    profitFactor: float
    returnOnDrawdown: float
    minLotSize: float
    maxLotSize: float
    avgLotSize: float
    wins: int
    losses: int
    winRate: int
    minTradeTime: str
    maxTradeTime: str
    avgTradeTime: str
    trades: int
    openEquity: float
    openDrawdown: float


class SetsResponse(BaseModel):
    sets: list[SetResponse]


class CreateSetResponse(BaseModel):
    magic: int
    name: str
    strategy: str
    profit: float
    trades: int
    maxDrawdown: float
    profitFactor: float
    returnOnDrawdown: float
    created_at: datetime
    updated_at: datetime

class SetGet(BaseModel):
     user: str
     account: int
     magic: int

class SetRemove(BaseModel):
     magic: int
     account: int
     user: str

# Request Model for creating a set
class SetCreate(BaseModel):
    magic: int
    name: Optional[str] = 'Unnamed Set'
    strategy: Optional[str] = '-'
    profit: Optional[float] = 0
    trades: Optional[int] = 0
    maxDrawdown: Optional[float] = 0
    profitFactor: Optional[float] = 0
    returnOnDrawdown: Optional[float] = 0
    account: int
    user: str
    openEquity: Optional[float] = 0
    openDrawdown: Optional[float] = 0
    minLotSize: Optional[float] = 0
    maxLotSize: Optional[float] = 0
    avgLotSize: Optional[float] = 0
    wins: Optional[int] = 0
    losses: Optional[int] = 0
    winRate: Optional[int] = 0
    minTradeTime: Optional[str] = '0'
    maxTradeTime: Optional[str] = '0'
    avgTradeTime: Optional[str] = '0'

class SetExistenceCheck(BaseModel):
    magic: int
    account: int
    user: str

class TradeExistenceCheck(BaseModel):
    magic: int
    account: int
    user: str
    id: int


class SetUpdate(BaseModel):
    magic: int
    account: int
    user: str
    name: Optional[str] = "Unnamed Set"
    strategy: Optional[str] = "-"
    profit: Optional[float] = 0.0
    trades: Optional[int] = 0
    maxDrawdown: Optional[float] = 0.0
    profitFactor: Optional[float] = 0.0
    returnOnDrawdown: Optional[float] = 0.0
    openEquity: Optional[float] = 0.0
    openDrawdown: Optional[float] = 0.0
    minLotSize: Optional[float] = 0.0
    maxLotSize: Optional[float] = 0.0
    avgLotSize: Optional[float] = 0.0
    wins: Optional[int] = 0
    losses: Optional[int] = 0
    winRate: Optional[int] = 0
    minTradeTime: Optional[str] = "00:00:00"
    maxTradeTime: Optional[str] = "00:00:00"
    avgTradeTime: Optional[str] = "00:00:00"

class AccountsGet(BaseModel):
     user: str

class AccountGet(BaseModel):
     user: str
     login: int

class AccountRemove(BaseModel):
     login: int
     username: str

class AccountRemoveResponse(BaseModel):
     login: int

class AccountResponse(BaseModel):
     enabled: bool
     login: int
     name: str
     server: str
     terminalFilePath: str
     user: str
     password: str
     deposit: int

class AccountUpdate(BaseModel):
     login: int
     user: str
     password: Optional[str] = None
     name: Optional[str] = None
     server: Optional[str] = None
     deposit: Optional[int] = None
     enabled: Optional[bool] = None

class AccountCreate(BaseModel):
     type: bool = False
     login: int
     password: str
     deposit: int
     user: str
     name: str
     server: str
     terminalFilePath: str


class AccountsResponse(BaseModel):
     accounts: List[AccountResponse]

class Trade(BaseModel):
    id: int
    entryTime: str
    exitTime: str
    entryPrice: float
    exitPrice: float
    volume: float
    profit: float
    symbol: str
    set: int
    direction: str
    holdTime: str
    user: str
    account: int
    direction: str

class SnapshotResponse(BaseModel):
     set: int
     totalProfit: float
     openProfit: float
     drawdown: float


class Snapshot(BaseModel):
     magic: int
     account: int
     time: str
     user: str
     totalProfit: float
     openProfit: float
     drawdown: float

class SnapshotResponseBase(BaseModel):
     set: int
     account: int
     time: str
     user: str
     totalProfit: float
     openProfit: float
     drawdown: float

class GetSnapShot(BaseModel):
     account: int
     user: str

class GetSnapShotMagic(BaseModel):
     magic: int
     account: int
     user: str

class SnapshotsResponse(BaseModel):
     snapshots: list[SnapshotResponseBase]

class SnapshotsGraphDataPoint(BaseModel):
    time: str
    value: float

# Define models for the response structure
class SnapshotsGraphResponse(BaseModel):
    drawdownData: List[SnapshotsGraphDataPoint]
    equityData: List[SnapshotsGraphDataPoint]

class DrawdownResponse(BaseModel):
     maxDrawdown: float

class InsertSetInput(BaseModel):
     username: str