from socket import *
from time import time
HOST = "localhost"
PORT = 9000

#Main
def runServer():
    print "Starting server on port", PORT
    #Load socket & bind
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)

    #Wait for requests
    while(1):
        (client, address) = server.accept()
        print client.recv(32)
        client.send("Seconds since epoch " +  str(time())) #Response text
        client.close()

runServer()

# source
# https://ruslanspivak.com/lsbaws-part1/
