'파일 열기'
file = open('file.txt', '옵션',encoding='문자 인코딩')
'파일 일기'
content = file.read()
'파일 닫기'
file.close()
with open('file.txt', 'r') as file:
    content = file.read()
'파일 쓰기'
file.write( 데이터 )

# [1] 파일 쓰기
writeFile = open( 'day03FILE.txt' , 'w' , encoding='UTF-8' )
# 같은 패키지 의 메모장 파일 생성 되었다.
# [2] 파일 내 데이터 대입하기
writeFile.write("파이썬에서 작성한 자료\n")
# [3] 입력받은 값을 파일에 저장하기
str = input( 'txt파일에 저장할 내용 : ' )
writeFile.write( str )
# [4] 파일 닫기 / 파일 쓰기 종료
writeFile.close()

# [5] 파일 읽기
readFile = open( 'day03FILE.txt' , 'r' , encoding='UTF-8' )
# [6] 파일내 데이터/자료 가져오기
while True :
    inStr = readFile.read( ) # 파일 자료의 한줄씩 읽어오기
    print( inStr )
    if not inStr : # 만약에 읽어온 자료가 없으면
        break   # 반복문 종료
readFile.close() # 파일 읽기 종료


# ============================
noteFile = open( 'day03Note.txt' , 'w' , encoding='utf-8' )
while True :
    str = input('[종료는 x ,엔터는 줄바꿈] txt 파일에 작성할 내용 : ')
    if str == 'x' :
        break # 가장 가까운 반복문 종료
    str += '\n' # 입력한 자료를 메모장에 쓰기 하기 전에 뒤에 줄바꿈 문자를 추가
    noteFile.write( str )
noteFile.close() # 파일 쓰기 종료
# ============================
fileName = input( '가져올 파일명.확장자 : ')
try :
    noteReadFile = open( fileName , 'r' , encoding='utf-8')
        # 만약에 존재하지 않는 파일명 을 읽어올때 예외 발생한다. FileNotFoundError
    while True :
        str = noteReadFile.read()
        if not str :
            break
        print( str )
except FileNotFoundError as e :
    print( '[파일읽기 실패] 존재하지 않는 파일명 입니다.')

#[1]. import csv
csv.reader: # CSV 파일을 읽어 각 라인을 리스트로 변환합니다.
csv.writer: # CSV 형식으로 데이터를 파일에 씁니다.
csv.writerows: # CSV 형식으로 리스트 데이터 를 파일에 씁니다.

# [2] CSV 파일 읽기
csvfile = open( 'file1.csv' , 'r' )
rows = csv.reader( csvfile )
print( rows )   # 읽어온 데이터들을 가지고 있는 객체
print( type(rows) ) # 객체 타입

for row in rows :
    print( type( row ) )    # 하나의 줄/행 을 리스트 타입 으로 반환
    print( row )
    for col in row :        # 하나의 열 을 문자로 타입 으로 반환
        print( type(col) )
        print( col )
csvfile.close()
