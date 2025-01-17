# day03 > step1.py
# 주석 : 실행 되지 않는 구역( 코드 설명,학습용,협업 )
10 # 자료(리터럴) , 정수 타입

# type( 자료 )
type( 10.5 ) # 자료의 타입 반환/알려주는 함수
# int( 문자열 ) , float( 문자열 ) , bool( 문자열 ) # 문자열 자료를 각 타입으로 반환 함수들
    # 정수타입 10 vs 문자열타입 '10' 다르다.
int( '10' )
# int( 'a' ) , 이러한 경우는 불가능
float( '10.5')
bool( 'True')

# 변수의 선언 하고 초기화[처음에 값을 넣어 주는 행위] , 변수명 = 초기값
var = 10
# 변수의 자료/값 호출
var
# 변수의 자료/값 수정 , 변수명 = 새로운값
var = 5

# 콘솔 창에 출력함수 , print( 자료 또는 변수명 )
print( var )
print( f'var : { var }')    # 문자열과 변수의 값 을 같이 출력할수 있다. f포메팅
print( f'var : \t { var } \n') # \n 줄바꿈 \t 들여쓰기 , 이스케이프 문자

# [1] 콘솔에서 입력받기 , input()
    # 콘솔에서 입력후 *엔터* 기준 으로 입력값 을 *문자열타입* 반환/돌려주는 함수.
    # 콘솔창에 초록색 부분이 입력된 값 , 검정색 부분이 출력된 값
input()
    # - 하나의 데이터를 입력받아서 출력하시오.
print( input() )    # <class 'str'>
    # - 하나의 (2)정수 데이터를 (1)입력받아서 (3)출력하시오.
print( int( input() ) )
    # - 하나의 정수 데이터를 입력받아서 변수에 저장하고 해당 변수를 출력하시오.
    # 1.  input()
    # 2.  int( input() )
    # 3. 변수에 저장
var = int( input( ) )
    # 4. 변수값 호출해서 출력한다
print( var )