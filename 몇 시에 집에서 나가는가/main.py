#-*- coding:utf-8 -*-
import time
import datetime

import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def makeScheduleList(who):
    tmplist = []
    f = open('./' + str(who)+'.txt', 'r', encoding = 'UTF8')
    while True:
        line = f.readline()
        if not line: break
        tmplist.append(line.split(' '))
    f.close
    return tmplist

def makeAnswer(inputList, goORback, addHour, who, nowDate):
    week = nowDate.weekday()
    if week == 5 or week == 6:
        return "신나네요! 해당 요일은, 토요일 또는 일요일입니다."
    t = ['월', '화', '수', '목', '금', '토', '일']

    n1 = 0#시
    n2 = ""#분
    outputString = who + "이 " + t[week] + "요일에 "
    if goORback == 1:
        inputList.reverse()
        outputString += "도착하는 시간은 대략 "
        n1 = 1
    else:
        outputString += "출발하는 시간은 대략 "
        n1 = -1

    for i in inputList:
        if i[week + 1] != '!' and i[week + 1] != '!\n' and i[week + 1][0] != 'o':
            tmp = i[0].split(':')
            n1 = int(tmp[0]) + addHour * n1
            n2 += tmp[1]
            break

        elif i[week + 1][0] == 'o':#여기서 부턴 옵션
            counter = 2
            tmpDate = datetime.datetime(nowDate.year, nowDate.month, nowDate.day)
            while tmpDate != datetime.datetime(2020, 9, 16) and tmpDate != datetime.datetime(2020, 9, 18):
                counter += 1
                tmpDate -= datetime.timedelta(weeks = 1)

            if counter % 2 == 0:
                tmp = i[0].split(':')
                n1 = int(tmp[0]) + addHour * n1
                n2 += tmp[1]
                break

            else:
                continue
    
    if n1 == -1 or n1 == 1:
        return who + "이는 이번 주 " + t[week] + "요일에 학교를 가지 않습니다! 야호!"
    outputString += str(n1) + "시 " + n2 + "분 입니다."
    return outputString
  
class CGUIOn(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton('구본현이 오늘 출발 하는 시간', self)
        self.btn1.setToolTip('<b>구본현<b/>의 <b>오늘<b/> 출발 시간 설명 입니다.')
        self.btn1.clicked.connect(self.bt1_clicked)

        self.btn2 = QPushButton('구본현이 오늘 도착 하는 시간', self)
        self.btn2.move(200, 0)
        self.btn2.setToolTip('<b>구본현<b/>의 <b>오늘<b/> 도착 시간 설명 입니다.')
        self.btn2.clicked.connect(self.bt2_clicked)

        self.btn3 = QPushButton('구본현이 내일 출발 하는 시간', self)
        self.btn3.move(0, 50)
        self.btn3.setToolTip('<b>구본현<b/>의 <b>내일<b/> 출발 시간 설명 입니다.')
        self.btn3.clicked.connect(self.bt3_clicked)

        self.btn4 = QPushButton('구본현이 내일 도착 하는 시간', self)
        self.btn4.move(200, 50)
        self.btn4.setToolTip('<b>구본현<b/>의 <b>내일<b/> 도착 시간 설명 입니다.')
        self.btn4.clicked.connect(self.bt4_clicked)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 140)
        self.textbox.resize(280, 40)
        
        # Create a button in the window
        self.btn5 = QPushButton('해당 날짜로 출발시간 검색하기 /를 이용해 분리\nex)9/25', self)
        self.btn5.move(20, 180)
        self.btn5.clicked.connect(self. bt5_clicked)

        self.btn6 = QPushButton('해당 날짜로 도착시간 검색하기 /를 이용해 분리\nex)9/25', self)
        self.btn6.move(20, 230)
        self.btn6.clicked.connect(self. bt6_clicked)
    
        self.setGeometry(700,300,400,500) #창 위치, 크기
        self.resize(400, 300)
        self.setWindowTitle('구본현 구유정 출발시간 안내 프로그램')
        self.show()

    def bt1_clicked(self):
        QMessageBox.about(self, "구본현 오늘 출발",  makeAnswer(makeScheduleList(0), 0, 2, "본현", datetime.datetime.today()))
    def bt2_clicked(self):
        QMessageBox.about(self, "구본현 오늘 도착", makeAnswer(makeScheduleList(0), 1, 2, "본현", datetime.datetime.today()))
    def bt3_clicked(self):
        QMessageBox.about(self, "구본현 내일 출발",  makeAnswer(makeScheduleList(0), 0, 2, "본현", datetime.datetime.today()+datetime.timedelta(days = 1)))
    def bt4_clicked(self):
        QMessageBox.about(self, "구본현 내일 도착",  makeAnswer(makeScheduleList(0), 1, 2, "본현", datetime.datetime.today()+datetime.timedelta(days = 1)))

    def bt5_clicked(self):
        textboxValue = self.textbox.text()
        tmplist = textboxValue.split('/')
        QMessageBox.about(self, "구본현 해당 날짜 출발",  makeAnswer(makeScheduleList(0), 0, 2, "본현", datetime.datetime(2020, int(tmplist[0]), int(tmplist[1]))))
        #self.textbox.setText("")

    def bt6_clicked(self):
        textboxValue = self.textbox.text()
        tmplist = textboxValue.split('/')
        QMessageBox.about(self, "구본현 해당 날짜 도착",  makeAnswer(makeScheduleList(0), 1, 2, "본현", datetime.datetime(2020, int(tmplist[0]), int(tmplist[1]))))

    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "?", "프로그램을 닫으시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

app = QApplication(sys.argv)
w = CGUIOn()
sys.exit(app.exec_())