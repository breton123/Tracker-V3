-- Table: users
CREATE TABLE users (
    username TEXT PRIMARY KEY UNIQUE,
    email    TEXT UNIQUE,
    password TEXT,
    type     TEXT DEFAULT 'full'::text
);

-- Table: accounts
CREATE TABLE accounts (
    login            INTEGER PRIMARY KEY UNIQUE,
    password         TEXT,
    name             TEXT,
    server           TEXT,
    deposit          INTEGER,
    enabled          BOOLEAN DEFAULT FALSE,
    user             TEXT PRIMARY KEY REFERENCES users(username) ON DELETE CASCADE,
    terminalFilePath TEXT
);

-- Table: sets
CREATE TABLE sets (
    id                INTEGER PRIMARY KEY UNIQUE DEFAULT nextval('sets_id_seq'::regclass),
    magic             INTEGER,
    account           INTEGER,
    user              TEXT,
    name              TEXT,
    strategy          TEXT,
    profit            DOUBLE PRECISION,
    maxDrawdown       DOUBLE PRECISION,
    profitFactor      DOUBLE PRECISION,
    returnOnDrawdown  DOUBLE PRECISION,
    openEquity        DOUBLE PRECISION,
    openDrawdown      DOUBLE PRECISION,
    minLotSize        DOUBLE PRECISION,
    maxLotSize        DOUBLE PRECISION,
    avgLotSize        DOUBLE PRECISION,
    wins              INTEGER,
    losses            INTEGER,
    winRate           INTEGER,
    minTradeTime      TEXT,
    maxTradeTime      TEXT,
    avgTradeTime      TEXT,
    trades            INTEGER,
    created_at        TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at        TIMESTAMP WITH TIME ZONE DEFAULT now(),
    PRIMARY KEY (user, account, magic),
    FOREIGN KEY (user, account) REFERENCES accounts(user, login) ON DELETE CASCADE,
    FOREIGN KEY (user) REFERENCES users(username) ON DELETE CASCADE
);

-- Table: snapshots
CREATE TABLE snapshots (
    time        TIMESTAMP WITH TIME ZONE DEFAULT now(),
    set         INTEGER,
    account     INTEGER,
    user        TEXT,
    totalProfit DOUBLE PRECISION,
    openProfit  DOUBLE PRECISION,
    drawdown    DOUBLE PRECISION,
    PRIMARY KEY (time, set, account, user),
    FOREIGN KEY (user, account) REFERENCES accounts(user, login) ON DELETE CASCADE,
    FOREIGN KEY (user) REFERENCES users(username) ON DELETE CASCADE
);

-- Table: trades
CREATE TABLE trades (
    id          INTEGER PRIMARY KEY UNIQUE,
    account     INTEGER,
    user        TEXT,
    set         INTEGER,
    profit      DOUBLE PRECISION,
    volume      DOUBLE PRECISION,
    symbol      TEXT,
    direction   TEXT,
    entryTime   TEXT,
    exitTime    TEXT,
    holdTime    TEXT,
    entryPrice  DOUBLE PRECISION,
    exitPrice   DOUBLE PRECISION,
    PRIMARY KEY (id, account, user, set),
    FOREIGN KEY (account, user) REFERENCES accounts(login, user) ON DELETE CASCADE,
    FOREIGN KEY (user) REFERENCES users(username) ON DELETE CASCADE
);
