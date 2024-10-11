# 주제 : 인천시 부평구의 아파트 실거래가 현황 분석
# [1] 데이터 수집
# 국토교통부
#  아파트 매매 계약일 1년
# 시도 인천 시군 부평
# csv 다운
# 다운 파일 현재 폴더로 이동
import csv

# [2] csv 파일을 읽어오기
file=open('아파트(매매)_실거래가_20240919211232.csv','r')# 1. 파일 읽기 모드로 파일 객체 생성
csv.reader(file)# 2. csv 객체로 내용 읽어오기 # import csv
content = csv.reader(file)
# [3] 리스트 타입 으로 변환
newcontent = list(content)
# print(newcontent)
# [4] 필요 없는 데이터 제거 # 슬라이싱
newcontent = newcontent [16 : ] # 16인덱스 부터 마지막 인덱스 까지 슬라이싱
# print(newcontent)
# [6] 반복문 이용한 한줄식 읽어오가
고가금액 = 0 # 가장 큰 거래 금액
고가단지 = '' # 가장 큰 단지명
for row in newcontent :
    print(row)
    # (1) 부평구의 거래량 출력
print(f' 부평구 아파트의 거래수 : {len(newcontent)}')
    # (2) 1년간의 부평구 아파트 의 가장 큰 거래 금액 과 단지명 출력
print( f'단지명: {row[5]}, 거래금액: {row[9]}')
# 1. 거래 금액을 콤마 제거
천단위 = row[9].split(',')[0]
백단위 = row[9].split(',')[1]
금액 = int(천단위+백단위)
print(금액)
if 고가금액< 금액:
    고가금액 = 금액
    고가단지 = row[5]

print(f'최고가 단지명 : {고가단지} , 거래금액 : {고가금액}')