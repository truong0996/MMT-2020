#import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('127.0.0.1', 9000))
serverSocket.listen(5)
while True:
    print ('Ready to serve...')
    #Establish the connection
    connectionSocket, addr = serverSocket.accept()
    try:
        request = connectionSocket.recv(1024)
        file = open("./index.html")
        outputData = file.read()
        print(request.decode('utf-8'))
        
        http_response = """HTTP/1.1 200 OK
""" + """Content-Type: text/html
Content-Length: %d""" % len(outputData) + """

"""
        print(http_response)
        connectionSocket.send(bytes(http_response, 'utf-8'))
        for i in range(0, len(outputData)):
            connectionSocket.send(bytes(outputData[i], 'utf-8'))
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send(b'404 Not Found')
        #Close client socket
        connectionSocket.close()
serverSocket.close() 
