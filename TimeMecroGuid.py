
import time
import datetime
import pyautogui
pyautogui.FAILSAFE = False #메크로 안전장치 해제
#왜 안전장치가 내 컴퓨터에서만 문제되는지 모르겠음, 모니터를 두개 쓰기 때문인가.

def keyinput(c):#키를 입력시킴
    if c == 1 :
        print("Take_ Left  OTHER")
        pyautogui.keyDown('shift')  
        pyautogui.press('f2')  
        pyautogui.keyUp('shift')
    elif c == 2 :
        print("Take_ Right KA")
        pyautogui.keyDown('shift')  
        pyautogui.press('f4')  
        pyautogui.keyUp('shift')

print("---------------------------------------------------------------------------------------------------------")
print("Made by 9\n")
print("---------------------------------------------------------------------------------------------------------")
print("This program will !first start! at 0.00 seconds to match the minutes that were raised after the input.\n")
print("If input ended at 08:22:31--This programe will !first start! at 08:23:00")
print("---------------------------------------------------------------------------------------------------------")
print("And !Next start!")
print("The next run is performed when the entered delay is added by adding one minute and making 0.00 seconds.\n")
print("If !first start! at 08:23:00.003 and your input delay 1 min--This programe will next esxcute at 08:25:00")
print("---------------------------------------------------------------------------------------------------------")
waitmin = int(input("Input the wait minute : "))
keyinputType = int(input("who? 1)left, 2)right : "))
print("---------------------------------------------------------------------------------------------------------")
nowTime = datetime.datetime.now()#현재 시간
print ("Input END at", nowTime.strftime('%y / %m / %d -- %H:%M:%S'))
print("---------------------------------------------------------------------------------------------------------")

endTime = nowTime + datetime.timedelta(minutes = 1)#1분뒤 시간
endTime = endTime.replace(second = 0, microsecond = 0)#초와 마이크로초를 0으로 처리함
while True:#첫 대기
    time.sleep(0.01)
    nowTime = datetime.datetime.now()
    nowTime = nowTime.replace(microsecond = 0)#nowTime은 0.01초 딜레이 때문에 마이크로초를 비교하면 안됨
    if nowTime == endTime:
        break

counter = 1
keyinput(keyinputType)
nowTime = datetime.datetime.now()#현재 시간
print (nowTime.strftime('%y / %m / %d -- %H:%M:%S'), " !!! ", counter, " Cycle", "\n")
endTime = nowTime + datetime.timedelta(minutes = waitmin + 1)#waitmin + 1분뒤 시간
endTime = endTime.replace(second = 0, microsecond = 0)#초와 마이크로초를 0으로 처리함

while True:
    time.sleep(0.01)
    nowTime = datetime.datetime.now()
    nowTime = nowTime.replace(microsecond = 0)#nowTime은 0.01초 딜레이 때문에 마이크로초를 비교하면 안됨
    
    if nowTime == endTime:
            counter += 1
            keyinput(keyinputType)
            nowTime = datetime.datetime.now()#현재 시간
            print (nowTime.strftime('%y / %m / %d -- %H:%M:%S'), " !!! ", counter, " Cycle", "\n")
            endTime = nowTime + datetime.timedelta(minutes = waitmin + 1)#waitmin + 1분뒤 시간
            endTime = endTime.replace(second = 0, microsecond = 0)#초와 마이크로초를 0으로 처리함

# pyinstaller --clean --onefile .\MecroGuid.py