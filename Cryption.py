#대칭형 암호화 교본으로 쓰려고 만든 소스입니다.

normalword = ['\t', '\n', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '~', '-', '_', '=', '+', '|', ';', ':', '.', '/', '<', '>', '?', '[', '{', ']', '}']

def OpenCryptFile():
	print("열고싶은, 암호화 된 파일의 경로를 입력해 주세요")
	filelocal = input("대상 경로 : ")
	print("사용할 키 파일 경로를 입력해주세요")
	keylocal = input("키 경로 : ")
	i = open(filelocal, 'r')
	inputwords = i.readlines()
	i.close()
	k = open(keylocal, 'r')
	keywords = k.read()
	k.close()

	outwords = ""
	for line in inputwords:
		for word in line:
			count = 0
			while word != keywords[count]:
				count += 1
			outwords += normalword[count]
	
	print(outwords)

def MakeOpenFile():
	print("주의하십시요, 컴퓨터의 삭제된 파일들은 복구 될 수 있습니다.")
	print("복호화후 저장하고 싶은, 암호화 된 파일의 경로를 입력해 주세요")
	filelocal = input("대상 경로 : ")
	print("사용할 키 파일 경로를 입력해주세요")
	keylocal = input("키 경로 : ")
	print("복호화된 파일이 저장될 경로를 입력해 주세요")
	savelocal = input("저장 경로 : ")
	savelocal += ".txt"
	i = open(filelocal, 'r')
	inputwords = i.readlines()
	i.close()
	k = open(keylocal, 'r')
	keywords = k.read()
	k.close()

	outwords = ""
	for line in inputwords:
		for word in line:
			count = 0
			while word != keywords[count]:
				count += 1
			outwords += normalword[count]
	
	o = open(savelocal, 'w')
	o.writelines(outwords)
	o.close()	

def MakeCryptFile():
	print("이용하고 싶은 메모 파일의 경로를 입력해 주세요")
	filelocal = input("대상 경로 : ")
	print("	사용할 키 파일의 경로를 입력해 주세요")
	keylocal = input("키 경로 : ")
	print("암호화된 파일이 저장될 경로를 입력해 주세요")
	savelocal = input("저장 경로 : ")
	savelocal += ".encry9t"

	i = open(filelocal, 'r')
	inputwords = i.readlines()
	i.close()
	k = open(keylocal, 'r')
	keywords = k.read()
	k.close()

	outwords = ""
	for line in inputwords:
		for word in line:
			count = 0
			while word != normalword[count]:
				count += 1
			outwords += keywords[count]
	
	o = open(savelocal, 'w')
	o.writelines(outwords)
	o.close()	

def MakeKey():
	print("키파일을 생성 할 경로를 입력해 주세요")
	filelocal = input("대상 경로 : ")
	filelocal += ".k9y"
	f = open(filelocal, 'w')
	import random
	random.random()
	randWords = normalword
	random.shuffle(randWords)
	for i in randWords:
		f.write(i)
	f.close()

print("================================================")
print("##############-Enin Circle Crypt-###############")
print("================================================")
print("-----------------------------------by 9B0//-----")
print("------------------2020.06.19--------------------")
print("------------------------------------------------")
print("원하시는 작업을 선택해 주세요-------------------")
print("1. 키 파일로 암호화된 파일 열어보기-------------")
print("2. 키 파일로 암호화된 파일 복호화후 저장하기(!)-")
print("3. 키 파일로 암호화후 저장하기------------------")
print("4. 키 파일 생성하기-----------------------------")
print("------------------------------------------------")
c = input("선택 : ")
if c == '1':
	OpenCryptFile()
elif c == '2':
	MakeOpenFile()	
elif c == '3':
	MakeCryptFile()
elif c == '4':
	MakeKey()
else:
	print("잘못된 입력입니다.")

print("\n\n!!프로그램을 종료합니다.!!")