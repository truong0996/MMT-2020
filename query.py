import json
#import regular expression library
import re

def handlingClientQuery(httpRequest):
    #get username, password
    credentials = re.split("username=|&password=", httpRequest)
    uname = credentials[len(credentials) - 2]
    pwd = credentials[len(credentials) - 1]
    #print(uname + "\n" + pwd)
    
    #load data
    with open('credentials.json', 'r') as f:
        data = json.load(f)

    for _id in data:
        if uname == data[_id]["username"] and pwd == data[_id]["password"]:
            return True
    return False
    
