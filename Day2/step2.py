# day02 폴더 step2.py
'''
    변수란?
        - (수학) 변수: 정해져 있지 않는 임의의 값 , 상수:항상 일정한 수
        - (컴퓨터) 변수 : 하나의 데이터를 저장할수 있는 메모리 공간 , 상수 : 수정 불가능
    변수 사용 하는 이유
        - (생활) 냉장고( 먹고 남은 음식을 냉장고 보관) , 핸드폰( 복잡한/외우기 힘든 전화번호를 이름 저장 )
        - (컴퓨터) 1.저장 2.재사용 3.복잡한 계산식/연산식 을 저장해서 간단한 이름 으로 저장 등등
    변수 만드는 방법 / 준비물
        1. 변수명  , 값을 저장 하고 있는 메모리 공간의 이름 , 띄어 쓰기 대신 _(언더바) , 숫자 시작 못함 , 카멜 표기법(권장)
        2. =      , 오른쪽 값을 왼쪽 변수의 메모리 공간에 대입/넣어주기 , = 같다가 아니고 대입 연산자
        3.저장할값 , 변수에 저장할 값(리터럴값)


'''
# (1)
도토리필드 = 6    # 메모리 공간은 2개(변수메모리,리터럴메모리) , 리터럴값 1개
    # 1. '도토리필드' 변수명
    # 2. = 대입(오른쪽 값을 왼쪽에 대입/넣어주기 )
    # 3. 6 ( 리터럴값 )
# 메모리( 컴퓨터에 데이터를 저장 메모리/공간 ) 공간 몇개? 2개
선물상자 = '손목시계' # 상자,시계 실체 2개 , 상자안 내용물 1개 , 선물상자 라는 공간에 손목시계 를 넣었다.
# (2) 변수에 데이터 대입
과일상자 = "바나나"    # "바나나" 라는 문자열타입 으로 리터럴 값을 '과일상자' 라는 변수에 대입
''' ------과일상자--------
    |      "바나나"      |
    --------------------- '''
# (3) 변수에 데이터를 호출 , 변수명
# "바나나" 꺼내기 위해서는 바나나 가 들어있는 상자이름/식별/상징적인이름 을 알아야 한다.
과일상자 # 실행 했더니 콘솔창에 출력이 안된다. 변수에 데이터를 꺼낸거지 출력한다고 안함.
print( 과일상자 )
    #1. 출력[print()]하고 변수에 데이터 호출( 과일상자 ). 틀린 말
    #2. 변수에 데이터 호출( 과일상자 ) 하고 출력[print()]한다 . 맞는 말
    # 컴퓨터도 여러개 명령어들을 순서대로 처리하는 우선순위가 정해져 있다.
        # = 대입 기준으로 오른쪽 명령어/코드 처리
        # 안쪽 () 먼저 명령어/코드 처리
# (4) 변수에 데이터를 변경 , 변수명 = 새로운값
과일상자 = "수박"
print( 과일상자 )