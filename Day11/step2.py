# [1] 예외 다중 처리
from csv import excel
from multiprocessing.managers import Value
from typing import final

array=[1,2,3]
try:
    array[5]
    print(5/0)
    int('a')
except IndexError as e :
    print(e)
except ZeroDivisionError as e :
    print(e)
except ValueError as e :
    print(e)

# [2] 모든 예외 처리 하는 클래스 # 예외 상위 클래스 Exception 클래스
try:
    array[5]
    print(4/0)
    int('a')
except Exception as e:
    print(e)
except ValueError as e:
    print(e)

# [3] finally 키워드 # 예외 발생 여부와 상관없이 무조건 실행되는 코드
try :
    array[2]
except IndexError as e :
    print(e)
finally:
    print('예외 여부와 상관없이 싱행된다')

# [4] pass # 예외 발생시 아무것도 하지 않을때 사용
try :
    print(4/0)
except:
    pass

# [5] raise 키워드 # 강제로 예외를 발생 시킬때 사용
try :
    raise ValueError
except ValueError as  e :
    print(e)

# 실습 1
# 1.이름(문자) 2.나이(정수)를 입력받는 코드작성 # 입력받을때 1가지 이상의 예외를 예측해서  예외처리
# 2. member 딕셔너리 내 'phone' 이라는 key의 value 를 호출 하기 # 호출시 예외발생 처리 하기
# [1]
name=input('name : ')
age=int(input('age : '))
# [2]
dic={'name':name,'age':age}
print(dic['phone'])

except ValueError as e :
    print('나이를 숫자로 입력해 주세요')
except KeyError as e :
    print('존재하지 않는 key 입니다')
except Exception as e :
    print('예외발생 [관리자에게문의]')
finally :
    print('프로그램이 안전하게 종료 됩니다.')

