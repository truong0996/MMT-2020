import json

# Khai báo dict
creds = {
  "1" : {
    "username" : "test1",
    "password" : "1"
  },
  "2" : {
    "username" : "test2",
    "password" : "2"
  },
  "3" : {
    "username" : "test3",
    "password" : "3"
  }
}

# Ghi dữ liệu vào file
with open('credentials.json', 'w') as myfile:
  json.dump(creds, myfile)

print('Ghi file thanh cong !')


