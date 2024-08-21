import os
import chardet
from scripts.parse_chr_file import parse_chr_file


user_profile = os.environ['USERPROFILE']
terminalsFolder = os.path.join(user_profile, 'AppData', 'Roaming', 'MetaQuotes', 'Terminal')

def getDataPath(terminalFolder):
    terminalFolder = terminalFolder.replace(r"\terminal64.exe", "")
    for folder in os.listdir(terminalsFolder):
        try:
            terminalFolderFilePath = os.path.join(terminalsFolder, folder, "origin.txt")
            with open(terminalFolderFilePath, "r", encoding=detect_encoding(terminalFolderFilePath)) as file:
                if terminalFolder == file.read() or terminalFolder+r"\terminal64.exe" == file.read():
                    dataPath = os.path.join(terminalsFolder, folder)
                    return dataPath
        except:
            pass
    return ""

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def getProfileSets(terminalFilePath, profile):
    dataPath = getDataPath(terminalFilePath)
    profilePath = os.path.join(dataPath, "MQL5", "Profiles", "Charts", profile)
    profileSets = []
    try:
        for chartFile in os.listdir(profilePath):
            chartPath = os.path.join(dataPath, "MQL5", "Profiles", "Charts", profile, chartFile)
            try:
                chartConfig = parse_chr_file(chartPath)
                chartData = {
                    "setName": chartConfig["chart"]["expert"]["inputs"]["StrategyDescription"],
                    "symbol": chartConfig["chart"]["symbol"],
                    "magic": chartConfig["chart"]["expert"]["inputs"]["MAGIC_NUMBER"]
                }
                profileSets.append(chartData)
            except:
                pass
    except Exception as e:
        print(f"Failed to get profile sets {e}")

    return profileSets