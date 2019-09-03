from socket import *
import threading
import time


def send(sock, sendData):
    while True:
        sendData = input(">>>")
    #sendData = str(sendData)
        sock.send(sendData.encode('utf-8'))

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8081

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('192.168.0.23', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')


x = ([[1,2,3],[2,3,4],[3,4,5]])

send(connectionSock, x)
receiver = threading.Thread(target=receive, args=(connectionSock,))

receiver.start()

while True:
    time.sleep(1)
    pass