# step1.py

# day01 문법 포인트
# 1. 주석 : 인터프리터(파이썬 코드를 기계어로)번역 하는 프로그램 이 무시되는 구역
    #  '#'특수문자 이용한 한줄 주석 , 사용처 : 1. 학습메모 2.협업 3. 라이브러리 설명서
# 2. 리터럴 : 파이썬에서 미리 정의 해둔 데이터
    # 데이터/자료 : 3.14 , 3 , "안녕" , 'a' , True , False
    # 예] 쓰레기 : 내가먹은콜라페트병1개 , 서류종이1장 , 쿠팡비닐포장지1개
    # 타입/분류 : (기본타입) 정수타입'int'  , 실수타입'float' , 문자열타입'str' , 불리언타입'bool'
    # 예] 쓰레기분리수거 : 페트병류 , 종이류 , 비닐류
    # --- 빠른 데이터 처리 와 효율적인 데이터 처리 를 위해서 파이썬 언어를 만든 회사에서 미리 정의했다.

#
# 1. 데이터들 의 타입 확인 , type( 리터럴값 )
print( 123 )            # 자동완성 : pr + 엔터 # 정수
print( "123" )          # 정수??? , 문자열 타입
print( type(123) )      # <class 'int'> , 'int' 이라는 단어가 정수타입 이라는 뜻
print( type("123") )    # <class 'str'> , 'str' 이라는 단어가 문자열타입 이라는 뜻
print( type( 3.14 ) )   # <class 'float'> , 'float' 이라는 단어가 실수타입 이라는 뜻
print( type(True) )     # <class 'bool'> , 'bool' 이라는 단어가 불리언 타입 이라는 뜻
# 2. 기본타입 종류 와 데이터들 형태
# 2-1 정수타입 , 일반적인 정수의 데이터
print( 3 )
print( 12121212 )
print( 3 + 3 ) # 3+3의 결과 '6' 도 정수 리터럴
# 2-2 실수타입 , 일반적인 소수점 형식의 데이터
print( 3.14 )
print( 12.121212 )
print( 12.0 + 8.1 ) # 12.0 + 8.1의 결과 '20.1' 도 실수 리터럴
# 2-3 불리언타입 , 일반적인 참 과 거짓 형식의 데이터 , 주의할점 첫글자 대문자 True , False
print( True )
print( False )
print( 10 > 3 )     # True # 10 이 3보다 크다 의 결과도 참'True' 도 불리언 리터럴
# 2-4 문자열타입 , 일반적인 텍스트 형식의 데이터 , 주의할점 정수,실수,불리언도 문자열로 감싸면 문자열이다.
    # " " , ' ' , """ """ , ''' ''' 로 감싼 데이터 들을 문자열 타입
print( "안녕" )
print( '안녕' )
print( """안녕""" )
print( '''안녕''' )
print( "True" ) # 불리언 타입이 아니고 " " 큰따옴표로 감싼 형식 이므로 문자열 타입이다.
print( "3.14" ) # 실수 타입이 아니고 " " 큰따옴표로 감싼 형식 이므로 문자열 타입이다.

# 3. 문자열 타입을 (정수,실수,불리언) 으로 변경 하는 방법. ,
    # "123"(str문자열) --> 123(int정수)
    # 1. int( ) : 문자열 타입을 정수 타입 으로 변경 해서 반환/돌려주는 함수
    # 2. float( ) : 문자열 타입을 실수 타입 으로 변경 해서 반환/돌려주는 함수
    # 3. bool( ) : 문자열 타입을 불리언 타입 으로 변경 해서 반환/돌려주는 함수
print( type( int( "123" ) ) ) # <class 'int'>  # 주의할점 : '(' 열고 ')' 닫기 개수를 맞추어 작성하기.
print( type( float( "3.14") ) ) # <class 'float'> # "3.14" 문자열타입 -> 실수타입 으로 변경
print( type( bool("True") ) ) # <class 'bool'> # "Ttue" 문자열타입 -> 불리언타입 으로 변경