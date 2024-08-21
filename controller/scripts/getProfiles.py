import os
import chardet

user_profile = os.environ['USERPROFILE']
terminalsFolder = os.path.join(user_profile, 'AppData', 'Roaming', 'MetaQuotes', 'Terminal')

def getDataPath(terminalFolder):
    terminalFolder = terminalFolder.replace(r"\terminal64.exe", "")
    for folder in os.listdir(terminalsFolder):
        terminalFolderFilePath = os.path.join(terminalsFolder, folder, "origin.txt")
        try:
            with open(terminalFolderFilePath, "r", encoding=detect_encoding(terminalFolderFilePath)) as file:
                if file.read() == r"C:\Program Files\Vantage 2":
                    return os.path.join(terminalsFolder, folder)
        except:
            pass
    return ""

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def getProfiles(terminalFilePath):
    profiles = []
    dataPath = getDataPath(terminalFilePath)
    profilesPath = os.path.join(dataPath, "MQL5", "Profiles", "Charts")
    for d in os.listdir(profilesPath):
        if os.path.isdir(os.path.join(profilesPath, d)):
            profiles.append(d)
    return profiles

