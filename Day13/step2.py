# [1] 무한 루프
import csv

# 전화번호 목록 리스트
phonebooks=[]
while True :
##----------------csv 파일 읽어오기-----------------##
    file = open('phonebooks.csv', 'r')  # 1. 파일 읽기 모드로 파일 객체 변환
    contents = csv.reader(file)  # 2. 읽어온 객체를 list 타입으로 변환 # list() : list 타입으로 변환해주는 함수
    phonebooks = list(contents)
    file.close()  # 4. 파일객체 닫기
##------------------------------------------------##
    # 들여쓰기 주의
    # [2] 기능 입력받기
    # [3] 입력 조건문
    choose = input('1. 등록 2. 목록 3. 종료')

    if choose == '1' :
        print( '>>> 전화번호 등록 >>>' )
        #[4] 입력받기
        name = input( '>name :')
        phone = input( '>phone :')
        phonebooks.append([name,phone]) #.append( 새로운 요소 )# 리스트내 요소 추가

    if choose == '2' :
        print( '>>> 전화번호 목록 >>> ')
        # 2차원 리스트 출력하기
        for row in phonebooks : # 2차원 리스트 출력 하기 # 2차원 리스트를 반복문 이용한 자료 반환
            print(row)
    if choose == '3' :
        break # 가장 가까운 반목문을 종료한다, 탈출
##-----------------csv 파일 쓰기-----------------##
    file = open('phoneBooks.csv', 'w', newline="")  # 1. 파일 쓰기 모드
    csvfile = csv.writer(file, delimiter=',')  # 2. csv 쓰기 파일 객체 호츨 # 파일 상단에 import csv
   # csvfile.writerow([name, phone])
    csvfile.writerows(phonebooks) # csv 내용 쓰기
    file.close()  # 4. 파일객체 닫기