from query import handlingClientQuery
from socket import *

def sendImage(imgRequest, connectionSocket):
    imgRequest = imgRequest.decode('utf-8')
    if "GET /info/Cover-tom2.jpg HTTP/1.1" not in imgRequest:
        return False
    print(imgRequest)
    #Gửi hình ảnh cho client
    img = open("./info/Cover-tom2.jpg", "rb").read()
    http_response_img = """HTTP/1.1 200 OK
""" + """Content-Type: image/jpeg
Content-Length: %d""" %len(img) + """

"""
    connectionSocket.send(bytes(http_response_img, 'utf-8'))
    connectionSocket.send(img)
    return True

def sendMainPage(request, connectionSocket):
    request = request.decode('utf-8')
    if ("GET / HTTP/1.1" not in request) and ("GET /index.html HTTP/1.1" not in request):
        return False
    print(request)
    file = open("./index.html", "r")
    outputData = file.read()
    #Header http response của page chính
    http_response = """HTTP/1.1 200 OK
""" + """Content-Type: text/html
Content-Length: %d""" %len(outputData) + """

""" + outputData
    connectionSocket.send(bytes(http_response, 'utf-8'))
    return True

def sendInfoPage(postRequest, connectionSocket):
    print(postRequest.decode('utf-8'))
    #Xử lý query của form
    isTruthfulConnection = handlingClientQuery(postRequest.decode('utf-8'))
    #print(isTruthfulConnection)
    if isTruthfulConnection == True:
        #Mở file info.html và gửi response http header cho client
        info = open("./info/info.html", "r", encoding="utf8").read()
        http_response_info = """HTTP/1.1 200 OK
""" + """Content-Type: text/html
Content-Length: %d""" %len(info) + """

""" + info
        #print(http_response_info)
        connectionSocket.send(bytes(http_response_info, 'utf-8'))
        return True
    return False

        
