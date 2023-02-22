host = '127.0.0.5'
port = 1235
import socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((host, port))

print("UDP3 server up and listening")

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(1024)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    m=message.decode()
    clientMsg = "Message from Client "+m[len(m)-1]+": "+m[0:len(m)-1]
    clientIP  = "Client IP Address: {}".format(address)
    print('(UDP1)Connected to: ' + clientIP + ':' + str(address[1]))
    print(clientMsg)
    