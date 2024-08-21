
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