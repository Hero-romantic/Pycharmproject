#编写TCP服务器
from socket import *
tcpSock =socket(AF_INET,SOCK_STREAM)
tcpSock.bind(("",7788))
tcpSock.listen(5)
newSock,clientAddr=tcpSock.accept()

date =newSock.recv(1024)
newSock.send(b"xiexie")

newSock.close()
tcpSock.close()





























