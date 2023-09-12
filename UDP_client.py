import sys
from socket import *
from datetime import datetime
import time

#Reads in and Stores sommand line arguments and sets up varibles
message= sys.argv[1]
serverName = sys.argv[2]
serverPort = int(sys.argv[3])
clientSocket = socket(AF_INET, SOCK_DGRAM)
timePassed= time.time()
count=0

#loop for repeated connection attempts and for id resets
while True:
    try:
        #clientSocket.timeout(15)

        #code that connect to the server and get its message
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        recived, serverAddress = clientSocket.recvfrom(2048)
        messsageList = recived.decode().split()

        #Handles resets and message receival
        if(count==3):
            print('Connection Failure on ' + datetime.now())
        if(messsageList[0]=="OK"):
            print("Connection established " + str(messsageList[1]) + " " + str(serverName) + " " +  str(serverPort))
            break
        if(messsageList[0]=="Reset"):
            num = input("ConnectionID already in use. Select new ID: ")
            message = "HELLO " + num 
            count+=1

    #handles connection failures        
    except:
        print('Connection Failure on ' + str(datetime.now()))
        break
clientSocket.close()