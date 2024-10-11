# 사용 공통점 : 여러 자료/값 들을 하나의 자료로 묶음
# 리스트변수 = [ value1 , value2 ]
# 튜플변수 = ( value1 , value2 )
# 딕셔너리변수 = { key1 : value1 , key2 : value2 }

# 실습1 : 카페의 제품명과 가격 들을 컴퓨터에 저장 하는 설계
# 그림과 같이 제품과 가격이 여러개 존재할때 타입 생각!
# 생각1 : 리스트타입 일때
# 생각2 : 튜플타입 일때
# 생각3 : 딕셔너리 일때
# 생각4 : 위 3가지(리스트/튜플/딕셔너리/객체) 를 사용 하지 못할때
# 샘플 : 아메리카노(5800) , 카페라떼(6300) , 자몽차(5500)
    # - 데이터/자료 : 1.아메리카노 2.5800 3.카페라떼 4.6300 5. 자몽차 6.5500
    # 샘플 기준으로 자료는 6개
# 변수란 ? 하나의 자료를 저장하는 메모리 공간
# (1) 각 자료들 마다 변수를 선언해서 하나씩 대입해준다. 근데!! 만약에 제품100이면 제품수*2 => 200개 변수 # 변수 많아서 힘들어
제품명1 = '아메리카노'      # 제품명1 = '아메리카노' 5800   하나의 변수에 2개 자료 저장 불가능
제품가격1 = 5800
제품명2 = '카페라떼'
제품가격2 = 6300
제품명3 = '자몽차'
제품가격3 = 5500

# (2) 여러개 자료들을 하나의 자료로 묶어서 하나의 변수에 넣기
# 리스트 = [ ]
# (2-1) 하나의 리스트 에 다 넣기 # 하나의 리스트에 제품명과 가격을 순서대로 넣으면 가능 # 만약에 순서 변화 나 속성 추가 있을때 힘들다.
제품목록 = [ '아메리카노' ,  5800 , '카페라떼' , 6300 , '자몽차' , 5500 ]
# (2-2) 속성(특성) 마다 리스트에 다 넣기 #  서로 다른 리스트 간의 인덱스를 일치화 하는데 힘들수 있다.
제품명목록 = ['아메리카노','카페라떼','자몽차']
제품가격목록 = [ 5800 , 6300 , 5500 ]
# (2-3)
가게정보 = [   { '아메리카노' : 5800 , '카페라떼' : 6300 , '자몽차' : 5500  }     ]
# (3)
# 튜플 = ( ) # 리스트와 동일 해서 생략 , 차이점 : 요소의 수정/삭제 가 안된다.

# (3-1)
#딕셔너리 = { } # 자료들 중에 누가 key 고 누가 value 선정 # key는 중복값이 없어야 한다. ( 가격은 중복이 있으므로 제품명을 key 선정하자 )
제품목록 = { '아메리카노' : 5800 , '카페라떼' : 6300 , '자몽차' : 5500  }
# key=제품명 , value=가격 일때 한쌍(제품1개) 구성하여 여러개 쌍(제품 들) 을 저장하는 구조

# 변수 = "문자열" : 하나의 문자열 에 여러개의 자료들을 *구분(문)자를 넣어서 여러개의 자료들을 넣는다.
변수 = "아메리카노,5800\n카페라떼,6300\n자몽차,5500" # 문자열 1개 자료
    # 제품명과 가격을 구분은 ,(쉼표)
    # 제품간의 구분은 구분은 \n(줄바꿈)
    # 내 마음대로 구분자를 정해서 사용이 가능하지만 , 일반적으로 주로 사용되는 CSV 형식 구조이다.