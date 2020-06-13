from query import handlingClientQuery
from socket import *
from senddata import *


serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('127.0.0.1', 9000))
serverSocket.listen(10)
flag = [0]
while True:
    print ('Ready to serve...')
    #Lập kết nối
    connectionSocket, addr = serverSocket.accept()
    try:
        #Nhận dữ liệu client gửi (HTTP method)
        request = connectionSocket.recv(1024)
        print (request.decode('utf-8'))
        #print (flag)
        if sendMainPage(request, connectionSocket) == True:
            continue
        if flag[0] == 1:
            if sendInfoPage(request, connectionSocket) == True:
                flag = [0]
                continue
        if flag[0] == -1:
            if send404Page(request, connectionSocket) == True:
                flag = [0]
                continue
        if sendFavicon(request, connectionSocket) == True:
            continue
        if sendImage(request, connectionSocket) == True:
            continue
        if sendRedirection(request, connectionSocket, flag)== True:
            continue

        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        send404Page(connectionSocket)
        #Close client socket
        connectionSocket.close()
serverSocket.close() 
