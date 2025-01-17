# [7] 함수 안에서 선언된 변수의 사용 범위 # 지역 변수
var1 = 1                    # 함수 밖에서 선언된 변수 ( 전역 변수 )
def test1( var1 ) :         # 함수 인자값 저장하는 변수 ( 매개 변수 , 지역 변수 )
    var1 = var1 + 1         # 함수 안에서 선언된 변수  ( 지역 변수 )
test1( var1 )
print( var1 ) # 확인 # 1

# 1. return 반환          # 전역변수와 지역변수가 이름이 동일하면 함수내에서는 지역변수가 우선이다.
# 왜? 지역변수를 사용하는 이유 > 즉 함수를 사용하는 이유 : 함수내 코드들은 실행시 에만 메모리 할당/부여 , 종료 되면 다 사라짐
# 메모리(물리적인 저장장치)/자원 = 자원을 아껴쓰자 -> 함수는 실행할때만 함수내 코드의 메모리 할당 하고 함수를 종료하거나 안쓰면 메모리할당 안함
# 즉] 사용시 에만 메모리(자원) 사용 개념
def test2( var1 ) :
    var1 = var1 + 1         # var1  = 지역변수
    return var1             # 지역 변수의 자료를 반환/리턴 # 함수 종료되면 함수내 메모리/변수/자료 는 다 사라진다. # 필요한 자료는 복귀/반환
print( test2( var1 ) )      # 확인 # 2

# 2. 전역변수를 함수 안으로 불러내기 , global 키워드
def test3(  ) :
    global var1             #global 전역변수명 # 함수 밖에 있는 전역변수를 함수 안으로 가져왔다.
    var1 = var1 + 2
test3()
print( var1 )               # 확인 # 3

# [실습1] : 키보드로 부터 입력받은 2개 의 정수를 인자값으로 전달하여 두 정수를 제곱 계산 하여 결과를 반환 하는 함수 만들기
정수1 = int( input('(1)정수:') ) # input( ) # 키보드로부터 입력받는 기능를 처리 함수 # 매개변수:출력할자료 # 반환값 : 키보드로 부터 입력받은(엔터기준) 문자열
# int( ) # 자료를 정수 타입으로 변환 처리 함수 # 매개변수 : 변환할자료 # 반환값: 정수로 변환된 자료
정수2 = int( input('(2)정수:') ) # input() 반환한 문자열을 int() 가 변환해서 반환된 정수를 '정수2'라는 변수에 대입

# 함수 정의/만들기
def square( x , y ) : # 2개의 인자값을 받아 2개의 매개변수에 저장하는 함수 정의/만들기
    result = x ** y # 계산 또는 실행문 , 함수 실행
    return result # 계산된 결과 #   리턴을 안하면 함수내 모든 자료를 사라진다.왜? 지역변수의 특징
# 함수 호출/사용
# print() : 파이썬 회사에 미리 만든 함수
a = square( 정수1 , 정수2 ) # 인자값으로 입력받은 값 정수 2개 ,(쉼표) 구분해서 전달 # 내가 만든 함수 # 매개변수에 무엇을 전달해야되는지 알고 있는상태
# 함수가 종료되면서 반환된 제곱 결과를 반환받아서 a변수에 대입
print( a )

# [실습2] : [ 1, 2, 3, 4 ] 자료 4개를 가지는 리스트 자료1개를 인자값으로 전달하여 매개변수(리스트)의 총합계를 계산하여 반환 하는 함수 만들기
