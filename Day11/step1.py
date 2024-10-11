'''
Python1 문법
-출력함수 : print()
    - 이스케이프 문자, f포메링
-입력함수 : input()
-타입변환 함수 : int(), float(), bool()
-변수 : 하나의 자료 저장하는 메모리 공간
-연산자
    1. 산술연산자 : + - * / // %
    2. 연결연산자 : + ,
    3. 비겨연산자 : > < >= <= == !=
    4. 논리연산자 : and or not
    5. 대입연산자 " = += *= /= -= //= %=
    6. 상항연산자 : true if 조건문 else false

- 조건문, if
    if 조건문:
        true
    elso:
        false

-반복문 , for
    for 반복변수 in range():
-리스트 :()
-튜플 : {}
-딕셔너리 []
-함수 :
    1. 정의 : def 함수명(배개변수1,배개변수2)
    2. 호출/사용 : 함수명(값1,값2)
-클래스/객체
    1. 클래스 : class 클래스명 :
    2. 객체 : 클래스명()
'''

'''
    예외 처리
        - 에러[error]
            시스템이 조료 되어야 할 수준의 상황 같이 개발자가 수습할수 없는 심각한문제
            개발자가 미리 예측/방지 할 수 없다. 주로 하드웨어 관련된 오류가 발생한다.
            
        - 예외[exception]
            개발자가 구현한 로직에서 발생한 실수 나 사용자의 영향에 의해 발생 하는 문제
            오류 와 달리 개발자가 미리 예측/방지 할 수 있기에 상황에 맞게 예외 처리를 해야한다.
            개발자 예측 -> 개발자가 경험이 풍부 -> 개발자의 경함의 의존성이 큼
    -목적 : 문제/오류 발생하면 프로그램은 자동으로 강제 종료된다.
        즉) 예외가 발생 하더라도 프로그램은 24시간 종료되지 않고 서비스를 제공해야 한다.
    - 에외처리 문법
        try :
            예외가 발생 하거나 발생 할 것 같은 코드
        except :
            만약에 try 에서 예외가 발생 했을때 실행 되는 코드
'''
# [1] 고의적으로 예외 발생1 # 인덱스
array = [1,2,3]
# array[5]
try :
    array[5]
except :
    print('IndexError 예외 발생') # IndexError 예외 발생 # 프로그램 유지

# [2] 예외 발생
# print(3/0) # ZeroDivisionError
try :
    print(3/0)
except ZeroDivisionError as e : # except 예외 클래스명  as 변수명 : # 변수명에 예외 사유를 대입
    print(e)

# [3] 예외 발생
# int('a') # ValueError: invalid literal for int() with base 10: 'a'
try:
    int('a')
except ValueError as e:
    print(e)