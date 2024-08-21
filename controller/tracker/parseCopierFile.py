
import chardet

def parseCopierFile(file_path):
    with open(file_path, 'r', encoding=detect_encoding(file_path)) as file:
        lines = file.readlines()

    config = {
        'chart': {
            'expert': {
                'inputs': {}
            },
            'window': {
                'indicator': {},
                'object': {}
            }
        }
    }

    current_sections = []
    currentSection = ""

    for line in lines:
        line = line.strip()
        ## Setting current sections
        if '<' in line and '>' in line and "/" not in line:
            currentSection = line.split("<")[1].split(">")[0]
            current_sections.append(currentSection)
        elif line.startswith('</'):
            del current_sections[-1]
        
        ## Setting new value
        elif '=' in line:
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            newEval = "config"
            for section in current_sections:
                newEval += f"['{section}']"
            newEval += f"['{key}']='{value}'"
            exec(newEval) 

    return config

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']