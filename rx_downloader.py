from selenium import webdriver
import urllib.request
import time
import os
import random as rand
from urllib.parse import unquote

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('headless')
driver = webdriver.Chrome('./chromedriver.exe', options=options)#v91
#https://sites.google.com/a/chromium.org/chromedriver/downloads

def webWait(st, et):
    global driver
    t = rand.uniform(st, et)
    driver.implicitly_wait(t)

def staticWait(st, et):
    t = rand.uniform(st, et)
    time.sleep(t)

def createForder(forderName):
    try:
        if not os.path.exists(forderName):
            os.makedirs(forderName)
    except OSError:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!폴더만들기 오류")

def fileNameMake(fileName):
    xList = [',', '\\', '/', ':', '*', '?','"', '<', '>', '|']
    for x in xList:
        fileName = fileName.replace(x, '_')
    return fileName

def getLastIndex():
    global driver
    try:
        lastBtn = driver.find_element_by_xpath('//*[@id="paginator"]/div/a[3]')
        lastLink = lastBtn.get_attribute('href')
    except:
        return 1
    lastIndex = lastLink.split('/')[6]
    #href="/post/list/a/26"
    return int(lastIndex)

def pageDownload(url):
    global driver, forderName, rev
    driver.get(url)
    webWait(1, 2)
    btns = driver.find_elements_by_xpath('//a[@class = "shm-thumb-link"]')
    pages = []
    loading = ""

    for btn in btns:
        pages.append(btn.get_attribute('href'))

    i = 1
    re = 0
    if rev == 1:
        pages.reverse()
    for page in pages:
        driver.get(page)
        webWait(1, 2)
        try:
            s = driver.find_element_by_xpath('//*[@id="main_image"]/source')
            staticWait(2, 3)
        except:
            s = driver.find_element_by_xpath('//*[@id="main_image"]')
        s = s.get_attribute('src')
        fileName = unquote(s.split('/')[5])
        fileName = fileNameMake(fileName)
        try:
            urllib.request.urlretrieve(s, './' + forderName + '/' + fileName)
            #wget.download(s, out='./'+forderName+'/')
            staticWait(1, 2)
            if os.path.getsize('./' + forderName + '/' + fileName) == 0:
                re += 1
                urllib.request.urlretrieve(s, './' + forderName + '/' + fileName)
        except:
            print("!!!!!!!!!!!!!!!")
            input("???")

        loading += "/"
        print('\r', "complite:" ,str(i), " error:", str(re), " # ", loading, end='')
        i += 1
        driver.back()
        driver.implicitly_wait(2)

def start(startLink):
    global driver, rev
    driver.get(startLink + str(1))
    webWait(2, 3)
    driver.find_element_by_xpath('//a[contains(@onclick,"tnc_agree();")]').click()
    webWait(1, 1.5)
    driver.get(startLink + str(1))
    webWait(1, 1.5)

    startIndex = 1
    lastIndex = getLastIndex()
    
    a = int(input("범위를 직접 선택하시겠나요? || 1)처음부터 끝까지 || 2)커스텀 || : "))
    if a == 2 :
        startIndex = int(input("작은 인덱스를 입력해주세요 : "))
        lastIndex = int(input("큰 인덱스를 입력해주세요 : "))

    if rev == 1:
        for i in range(lastIndex, startIndex-1, -1):
            print("------------------------------------------------------\n", str(i), "번 페이지 시작")
            pageDownload(startLink + str(i))
            print("\n", str(i), "번 페이지 종료")
            staticWait(1, 2)
    elif rev == 2:
        for i in range(startIndex, int(lastIndex)+1):
            print("------------------------------------------------------\n", str(i), "번 페이지 시작")
            pageDownload(startLink + str(i))
            print("\n", str(i), "번 페이지 종료")
            staticWait(1, 2)

if __name__ == "__main__":
    startLink = input("제작:Enin    인덱스만 지운 링크를 입력해주세요 : ")
    rev = int(input("제작:Enin    받는 순서를 둘중에 골라주세요 || 1)오래됨->최신 || 2)최신->오래됨 || : "))
    forderName = startLink.split("/")[5].replace("%20", " ")
    print("준비중...")
    createForder(forderName)
    start(startLink)
    driver.close()
    print("모든 작업이 종료되었습니다. 엔터시 창닫힘")
    input()