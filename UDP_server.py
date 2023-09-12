from socket import *
from datetime import datetime
import sys
import time

#Reads in and Stores sommand line arguments and sets up varibles
serverPort = int(sys.argv[2])
serverIP = sys.argv[1]
connectionId = []
connectionIdTime = []

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
timeSinceRequest= time.time()

print("The UDP server is ready to receive")

#loop used to keep server listening
while True:
    try:
        #sends and recives messages
        serverSocket.settimeout(120)
        message, clientAddress = serverSocket.recvfrom(2048) # if the buf size value is smaller than the datagram size, it will drop the rest.
        modifiedMessage = message.decode().split()

        count=0

        #handles deleting connectionID after 30 seconds
        for id in connectionId:
            if time.time() - connectionIdTime[count] > 30:
                del connectionId[count]
                del connectionIdTime[count]
            count+=1

        #handles return message
        if modifiedMessage[1] in connectionId:
            returnMessage = 'Reset Connection'
            serverSocket.sendto(returnMessage.encode(), clientAddress)
        else:
            timeSinceRequest= time.time()
            connectionId.append(modifiedMessage[1])
            connectionIdTime.append(time.time())
            returnMessage= "OK " + modifiedMessage[1]
            serverSocket.sendto(returnMessage.encode(), clientAddress)
    except:
        print('Server Closed')
        serverSocket.close()
        break