from query import handlingClientQuery
from socket import *
from senddata import *


serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('127.0.0.1', 9000))
serverSocket.listen(10)
while True:
    print ('Ready to serve...')
    #Lập kết nối
    connectionSocket, addr = serverSocket.accept()
    try:
        #Nhận dữ liệu client gửi (HTTP method)
        request = connectionSocket.recv(1024)
        print (request.decode('utf-8'))
        if sendMainPage(request, connectionSocket) == True:
            continue
        if sendFavicon(request, connectionSocket) == True:
            continue
        #Nhận credentials từ client gửi form
        if sendImage(request, connectionSocket) == True:
            continue
        if sendInfoPage(request, connectionSocket) == True:
            continue
        else: send404Page(connectionSocket)

        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        send404Page(connectionSocket)
        #Close client socket
        connectionSocket.close()
serverSocket.close() 
