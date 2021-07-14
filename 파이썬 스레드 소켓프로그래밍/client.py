import socket

cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock.connect(('192.168.10.2', 9999))
print("-실행됨-")
while(True):
    msg = cliSock.recv(1024)#최대 1024바이트의 스트림을 받아온다. (받을때까지 대기), 0바이트를 해당 함수가 반환한다면 연결이 끊겼다는 것을 의미한다
    print("메세지 도착 :" + msg.decode())