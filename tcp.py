from socket import *
from time import ctime

HOST=''
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)
tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('Connection Awaiting')
    tcpCliSock,addr=tcpSerSock.accept()
    print('Connected from',addr)

while True:
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    tcpCliSock.send('[%s] %s'%(ctime(),data))

tcpClisock.close()
tcpSerSock.close()
