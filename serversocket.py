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
        sendMainPage(request, connectionSocket)
        #Nhận credentials từ client gửi form
        sendInfoPage(request, connectionSocket)
        sendImage(request, connectionSocket)
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send(b'404 Not Found')
        #Close client socket
        connectionSocket.close()
serverSocket.close() 
