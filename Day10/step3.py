'''
    - 시나리오1 : Todo(할일) List 애플레이션 개발
        - 조건1 : 할일내용 과  할일상태를 여러번 저장 한다.
        - 조건2 : 저장 , 할일전체출력 , 상태수정 , 할일삭제 기능을 선택하여 실행한다.
        - 조건3 : 출력 예시
            순번  할일내용    할일상태           딕셔너리
            1    파이썬공부    X                     key : 할일내용      value : 파이썬공부
            2    운동하기     O                클래스/객체
            3    집가기       X                    self.할일내용 = 파이썬공부
        - 조건4 : 클래스/객체 사용 불가능 합니다.

    - 요구사항 의 자료/값 와 이벤트/함수
        자료 : 할일내용 , 할일상태
        행위 : 저장 , 전체출력 , 수정 , 삭제
'''
# [1] 딕셔너리 와 리스트 를 이용한 메모리 설계
할일목록 = [ { '할일내용' : '파이썬공부' , '할일상태' : '미완료' } ,
            { '할일내용' : '운동하기' , '할일상태' : '완료' } ,
            { '할일내용' : '집가기' , '할일상태' : '미완료' } ]
    # 각 딕셔너리 3개를 하나의 리스트에서 관리
# [2] 각 기능 들의 함수 정의
def 할일저장( 할일내용 , 할일상태 ) :
    dic = { '할일내용' : 할일내용 , '할일상태' : 할일상태 }   # 매개변수 로 부터 전달받은 2개의 값을 이용한 딕셔너리 생성
    할일목록.append( dic )  # 생성한 딕셔너리 를 리스트 에 저장

def 할일전체출력( ) :
    순번 = 0
    for 할일 in 할일목록 :
        순번 += 1
        print(f'{ 순번 } \t { 할일['할일내용']} \t { 할일['할일상태']}')

def 할일상태수정( 순번 , 할일상태 ) :
    할일목록[ 순번-1]['할일상태'] = 할일상태

def 할일삭제( 순번 ):
    del 할일목록[순번-1]

# [3] 함수들을 실행 하는 코드(실행문)
while True :  # 무한루프( 종료조건 )
    choose = input('1.저장 2.전체출력 3.상태수정 4.삭제 5.종료')
    if choose == '5' :
        break # 무한루프 종료
    if choose == '1' :
        # 입력
        할일내용 = input('할일내용 : ')
        할일상태 = '미완료' # 할일상태는 기본값은 '미완료'
        # 저장 함수 호출
        할일저장( 할일내용 , 할일상태 )
    if choose == '2' :
        할일전체출력()
    if choose == '3' :
        할일전체출력()
        순번 = int( input('수정할 순번 선택 : ') )
        할일상태 = input('수정할 상태 : ')
        할일상태수정( 순번 ,할일상태  )
    if choose == '4' :
        할일전체출력()
        순번 = int(input('삭제할 순번 선택 : '))
        할일삭제( 순번 )

        '''
            - 시나리오1 : Todo(할일) List 애플레이션 개발
                - 조건1 : 할일내용 과  할일상태를 여러번 저장 한다.
                - 조건2 : 저장 , 할일전체출력 , 상태수정 , 할일삭제 기능을 선택하여 실행한다.
                - 조건3 : 출력 예시
                    순번  할일내용    할일상태           딕셔너리
                    1    파이썬공부    X                     key : 할일내용      value : 파이썬공부
                    2    운동하기     O                클래스/객체
                    3    집가기       X                    self.할일내용 = 파이썬공부
                - 조건4 : 클래스/객체 사용 가능 합니다.

            - 요구사항 의 자료/값 와 이벤트/함수
                자료 : 할일내용 , 할일상태
                행위 : 저장 , 전체출력 , 수정 , 삭제
        '''


        # [1] 객체 와 리스트를 이용한 메모리 설계
        class Todo:
            def __init__(self, content, state):
                self.content = content
                self.state = state
            # 메소드
            def save(self):
                toDoList.append(self)

            # 메소드
            def info(self, num):
                print(f'{num} \t {self.content} \t {self.state}')

            def update(self, state):
                self.state = state

            def delete(self):
                toDoList.remove(self)


        toDoList = [Todo('파이썬공부', '미완료'), Todo('운동하기', '완료'), Todo('집가기', '미완료')]
        # 각 객체 3개를 하나의 리스트에서 관리

        # [2]
        while True:
            choose = input('1.저장 2.전체출력 3.상태수정 4.삭제 5.종료')
            if choose == '5':
                break  # 무한루프 종료
            if choose == '1':
                content = input('할일내용:')
                state = '미완료'
                task1 = Todo(content, state)
                task1.save()
            if choose == '2':
                num = 0
                for element in toDoList:
                    num += 1
                    element.info(num)
            if choose == '3':
                num = 0
                for element in toDoList:
                    num += 1
                    element.info(num)
                num = int(input('수정할 순번 선택 : '))
                state = input('수정할 상태 : ')
                toDoList[num - 1].update(state)
            if choose == '4':
                num = 0
                for element in toDoList:
                    num += 1
                    element.info(num)
                num = int(input('삭제할 순번 선택 : '))
                toDoList[num - 1].delete()