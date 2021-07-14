import threading
import socket

import os
import time

#원래 메신저 같은 애들은 소캣을 24시간 유지시킬까?

cliSocks = []#클라이언트 소켓들
cliAddrs = []#클라이언트 주소들

#연결된 모든 클라이언트들에게 메세지 전달
def th_send_msg(s):
    global cliSocks
    cliCount = len(cliSocks)#덱같은 경우가 아니더라도 멀티스레딩때문에 중간에 사이즈가 바뀔수 있어서 고정해놔야할듯?
    i = 0
    #구조는 덱과같다
    while i < cliCount:
        try:
            cliSocks[i].sendall(s.encode())#문자열을 바이트스트림으로 변화시키고 전송한다.
            i += 1
        #보내려고 했으나 해당 소켓의 연결이 끊긴 경우
        except ConnectionResetError:
            #이 좆같은 현상을 파훼하는 방법이 내가 알기론 두가지, 하나는 클라이언트 측에서 살아있다는 신호를 주기적으로 보내는것, 하나는 서버에서 무시하는것
            #전자는 클라이언트에도 조치가 필요함
            del cliSocks[i]
            cliCount -= 1
    print("총 "+ str(i) + "개의 클라이언트에게 전송 완료했습니다.")

#계속해서 클라이언트의 연결을 기다림
def th_anytime_add_cli(servSock):
    while True:
        cliSock, cliAddr = servSock.accept()#연결을 받을때까지 대기한다. 받으면 반환한다.
        cliSocks.append(cliSock)
        cliAddrs.append(cliAddr)
        print("클라이언트가 추가되었습니다! 주소 : " + str(cliAddr))

#콘솔 명령어 처리
def cmd(s):
    if s == "": return
    s = s.split()
    if s[0] == 'cls':
        os.system('cls')
    elif s[0] == 'send':
        thr2_send_cli = threading.Thread(target=th_send_msg, args=(s[1],))
        thr2_send_cli.daemon = True
        thr2_send_cli.start()
    elif s[0] == '아짱나보고싶다':
        print("진짜루")
    elif s[0] == 'exit' or s[0] == 'quit':
        print("-명령에 의한 프로그램 종료-")
        time.sleep(1000)
        exit()
    else:
        print("잘못된 명령어입니다. --cls, send, quit, exit-- 중에 하나를 입력해주세요")

def server_start(host, port):
    #소켓의 정의 : 패밀리(주소체계)와 소켓타입이 매게변수로 들어간다.
    servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #소켓의 설정 : 
    servSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servSock.bind((host, port))
    servSock.listen(5)#최대 5개의 동시접속을 허용한다.

    thr1_add_cli = threading.Thread(target=th_anytime_add_cli, args=(servSock,))#지정함 튜플임에 주의
    thr1_add_cli.daemon = True#프로세스가 종료되면 스레드도 강제종료된다.
    thr1_add_cli.start()

    print("-실행됨-")
    while(True):
        try:
            s = input()
            cmd(s)
        except KeyboardInterrupt:
            servSock.close()
            print("-인터럽트로 인한 프로그램 강제종료-\n")
            time.sleep(1000)
            return

if __name__ == '__main__':
    #host = input("받을 주소 입력(공백시 모두) : ")
    #port = int(input("서버 포트 입력 : "))
    #server_start(host, port)
    server_start('', 9999)