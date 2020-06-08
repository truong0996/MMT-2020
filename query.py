import json
#import regular expression library
import re

def handlingClientQuery(httpRequest):
    request = httpRequest.split(" ", 2)[1]
    #print('QUERYYYYYYY'+request)
    #get username, password
    credentials = re.split("^\/\?username=|&password=", request)
    if len(credentials) != 3:
        return False
    uname = credentials[1]
    pwd = credentials[2]
    
    #load data
    with open('credentials.json', 'r') as f:
        data = json.load(f)

    for _id in data:
        if uname == data[_id]["username"] and pwd == data[_id]["password"]:
            return True
    return False
    
