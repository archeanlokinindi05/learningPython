from socket import *
HOST='localhost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data=input('Enter any')
    if not data:
                   break
    data
    tcpCliSock.send(data)
    x=tcpCliSock.recv(BUFSIZ)
    if not data:
            break
    print(data)
tcpCliSock.close()
