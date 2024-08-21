import configparser
import chardet

def read_ini_file(file_path):
    try:
        encoding = detect_encoding(file_path)
        config = configparser.ConfigParser()
        config.read(file_path, encoding=encoding)
        return config
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']
    return encoding

def getPreviousProfile(file_path):
    terminal_config = read_ini_file(file_path)
    if terminal_config is None:
        return "MT5-Tracker-Profile"
    if "Charts" in terminal_config:
        return terminal_config["Charts"]["ProfileLast"]
    else:
        return "MT5-Tracker-Profile"
