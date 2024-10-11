# [1] 파일 열기 # 쓰기 모드
# [2] 현재 파이썬에 내장된 모듈 호출
# import csv # 현재파일에 csv 모듈 호출
import csv

file = open('test1.csv','w',newline="")
# [2] csv 쓰기 객체 호출
csvfile=csv.writer(file,delimiter=',')
#[3] csv 파일에 내용 쓰기
csvfile.writerow(['이름' , '전화번호'])
csvfile.writerow(['유재석','010-1111-2222'])

#[4] 파일 닫기
file.close()

# csv 파일 읽기
# [5] 파일 열기 # 읽기 모드 파일객체 반환
file = open( 'test1.csv', 'r')
# [6] csv 읽기 객체 호출 #
content = csv.reader(file)
print(content)
print( list(content)) # list() 리스트 타입 으로 변환 함수
