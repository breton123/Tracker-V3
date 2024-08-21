
import os
import random
from database.createSet import createSet
from database.getSets import getSets
from scripts.parse_chr_file import parse_chr_file
from scripts.getProfiles import getDataPath
from scripts.terminalController import closeTerminal
from scripts.update_ini_file import update_ini_file
from scripts.write_chr_file import write_chr_file

def loadSets(account_id, profileName, terminalPath, setFiles, apiKey, expertName, symbolSuffix, user):
    terminalIndex = 0
    directory = os.getcwd()

    powName = expertName
    defaultChartPath = f"{directory}\\scripts\\chart01.chr"
    chartNumber = 1

    dataPath = getDataPath(terminalPath)
    chartsPath = os.path.join(dataPath, 'MQL5', 'Profiles', 'Charts', profileName)

    if os.path.isdir(chartsPath):
        chartNumber = len([f for f in os.listdir(chartsPath) if os.path.isfile(os.path.join(chartsPath, f))])
    else:
        os.makedirs(chartsPath)
        chartNumber = 1

    currentMagics = []
    sets = getSets(user, int(account_id))

    for nSet in sets:
        currentMagics.append(int(nSet["magic"]))

    for setFile in setFiles:
        chartsPath = os.path.join(dataPath, 'MQL5', 'Profiles', 'Charts', profileName)

        if os.path.isdir(chartsPath):
            chartNumber = len([f for f in os.listdir(chartsPath) if os.path.isfile(os.path.join(chartsPath, f))])
        else:
            os.makedirs(chartsPath)
            chartNumber = 1

        defaultConfig = parse_chr_file(defaultChartPath)
        magicNumber = setFile["name"].split("_")[-1].replace(".set","")
        symbol = setFile["name"].split(" ")[0] + symbolSuffix

        if int(magicNumber) not in currentMagics:
            newObject = {
            "magic": int(magicNumber),
            "account": int(account_id),
            "user": str(user),
            "name": setFile["name"].replace(".set",""),
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

        setConfig = parseSetFile(setFile["data"])
        defaultConfig["chart"]["description"] = setFile["name"].replace(".set","")
        defaultConfig["chart"]["expert"]["inputs"] = setConfig
        defaultConfig["chart"]["id"] = random.randint(100000000000000000, 999999999999999999)
        defaultConfig["chart"]["symbol"] = symbol
        defaultConfig["chart"]["expert"]["inputs"]["apiKey"] = apiKey
        defaultConfig["chart"]["expert"]["inputs"]["MAGIC_NUMBER"] = str(magicNumber)
        defaultConfig["chart"]["expert"]["inputs"]["StrategyDescription"] = setFile["name"].replace(".set","")
        defaultConfig["chart"]["expert"]["inputs"]["TradeComment"] = setFile["name"].replace(".set","")
        defaultConfig["chart"]["expert"]["name"] = expertName.replace(".ex5","")
        defaultConfig["chart"]["expert"]["path"] = f"Experts\\{powName}"
        defaultConfig["chart"]["expert"]["expertmode"] = 1

        output_chr_file_path = f'{dataPath}\\MQL5\\Profiles\\Charts\\{profileName}\\chart0{chartNumber}.chr'
        write_chr_file(output_chr_file_path, defaultConfig)
        chartNumber += 1

    terminalConfigPath = os.path.join(getDataPath(terminalPath), "config", "common.ini")
    closeTerminal(terminalPath)
    update_ini_file(terminalConfigPath, profileName)

def parseSetFile(data):
     data = data.split("\n")
     config = {}
     for line in data:
          if ";" not in line:
               try:
                    key, value = line.split("=")
                    value = value.split("|")[0]
                    config[key] = value
               except:
                    pass
     return config