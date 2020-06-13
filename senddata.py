from query import handlingClientQuery
from socket import *


def sendRedirection(request, connectionSocket, flag):
    request = request.decode('utf-8')   #request chuyển hướng của browser
    #browser yêu cầu main page
    if ("GET / HTTP/1.1" in request):
        new_location = """
HTTP/1.1 301 Moved Permanently
Location: /index.html

"""
        connectionSocket.send(bytes(new_location, 'utf-8'))
        return True
    #browser yêu cầu page info
    #Xử lý query của form
    isReliableConnection = handlingClientQuery(request)
    #print(isTruthfulConnection)
    if "POST /index.html" in request and isReliableConnection == False:
        #Gửi 404.html
        new_location = """
HTTP/1.1 301 Moved Permanently
Location: /404.html

"""
        print(new_location)
        connectionSocket.send(bytes(new_location, 'utf-8'))
        flag[0] = -1
        return True
    else:
        if "POST /index" in request and isReliableConnection == True:
            new_location = """
HTTP/1.1 301 Moved Permanently
Location: /info.html

"""
            print(new_location)
            connectionSocket.send(bytes(new_location, 'utf-8'))
            flag[0] = 1
            return True
    return False

def sendImage(imgRequest, connectionSocket):
    imgRequest = imgRequest.decode('utf-8')
    if "GET /Cover-tom2.jpg" not in imgRequest:
        return False
    #Gửi hình ảnh cho browser
    img = open("./Cover-tom2.jpg", "rb").read()
    http_response_img = """HTTP/1.1 200 OK
""" + """Content-Type: image/jpeg
Content-Length: %d""" %len(img) + """

"""
    connectionSocket.send(bytes(http_response_img, 'utf-8'))
    connectionSocket.send(img)
    return True

def sendMainPage(request, connectionSocket):
    request = request.decode('utf-8')
    if "GET /index.html" not in request:
        return False
    #print(request)
    file = open("./index.html", "r")
    outputData = file.read()
    #Header http response của page chính
    http_response = """HTTP/1.1 200 OK
""" + """Content-Type: text/html
Content-Length: %d""" %len(outputData) + """

""" + outputData
    connectionSocket.send(bytes(http_response, 'utf-8'))
    file.close()
    return True

def sendInfoPage(request, connectionSocket):
    request = request.decode('utf-8')
    if "GET /info.html" not in request:
        return False
    #Mở file info.html và gửi response http header cho client
    info = open("./info.html", "r", encoding="utf8").read()
    http_response_info = """HTTP/1.1 200 OK
""" + """Content-Type: text/html
Content-Length: %d""" %len(info) + """

""" + info
    #print(http_response_info)
    connectionSocket.send(bytes(http_response_info, 'utf-8'))
    return True

def sendFavicon(requestFav, connectionSocket):
    requestFav = requestFav.decode('utf-8')
    if "GET /favicon.ico" not in requestFav:
        return False
    fav = open("./favicon.ico", "rb").read()
    http_response_fav = """HTTP/1.1 200 OK
""" + """Content-Type: image/x-icon
Content-Length: %d""" %len(fav) + """

"""
    connectionSocket.send(bytes(http_response_fav, 'utf-8'))
    connectionSocket.send(fav)
    return True

def send404Page(request, connectionSocket):
    request = request.decode('utf-8')
    if "GET /404.html" not in request:
        return False
    file = open("./404.html").read()
    http_response_404 = """HTTP/1.1 200 OK
""" + """Content-Type: text/html
Content-Length: %d""" %len(file) + """

""" + file
    connectionSocket.send(bytes(http_response_404, 'utf-8'))
    return True
