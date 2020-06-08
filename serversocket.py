from query import handlingClientQuery
from socket import *
import io

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('127.0.0.1', 9000))
serverSocket.listen(5)
while True:
    print ('Ready to serve...')
    #Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        #Nhận dữ liệu client gửi (HTTP method)
        request = connectionSocket.recv(1024)
        print(request.decode('utf-8'))
        file = open("./index.html")
        outputData = file.read()
        #Header http response file index.html
        http_response = """HTTP/1.1 200 OK
""" + """Content-Type: text/html
Content-Length: %d""" %len(outputData) + """

""" + outputData
        connectionSocket.send(bytes(http_response, 'utf-8'))

        #Nhận credentials từ client gửi form
        queryRequest = connectionSocket.recv(1024)
        print(queryRequest.decode('utf-8'))
        #Xử lý query của form
        isTruthfulConnection = handlingClientQuery(queryRequest.decode('utf-8'))
        #print(isTruthfulConnection)
        if isTruthfulConnection == True:
            #Mở file info.html và gửi response http header cho client
            info = io.open("./info/info.html", mode="r", encoding="utf-8").read()
            http_response_info = """HTTP/1.1 200 OK /info/info.html
""" + """Content-Type: text/html
Content-Length: %d""" %len(info) + """

""" + info
            print(http_response_info)
            connectionSocket.send(bytes(http_response_info, 'utf-8'))
            #Chưa gửi được ảnh
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send(b'404 Not Found')
        #Close client socket
        connectionSocket.close()
serverSocket.close() 
