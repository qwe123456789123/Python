# [2] 파이썬을 이용한 스택 구조 구현 활용
'''
    구현할 기능
        1. 스택구조가 full 인지 여부 확인 함수
        2. 스택구조내 Empty 여부 확인 함수
        3. 스택구조내 Push 데이터 삽입 함수
        4. 스택구조내 pop 데이터 삭제 함수
        5. 스택구조내 peek 최상위 위치와 데이터 확인 함수
'''

# 1. full 인지 여부 확인 함수
def isFull(): # 함수 선언
    global SIZE , stack , Top # 함수내 전역변수를 식별하는 키워드
    # 만약 현재 top 위치가 사이즈와 같으면 # 다 찾으면
    if Top >= SIZE -1 : # -1 : top - 인덱스가 0부터 시작흐므로
        return True # 함수가 종료되면서 호출했던곳으로 반환되는 값
    else: # 아니면
        return False
# 2. push 함수
def push(data) :
    global SIZE, stack, Top
    if isFull() : # 스택내 모두 차있으면
        print("자리없음")
        return
        # 스택구조의 Top 한칸 올리기
        Top += 1
        stack[top] = data

# isEmpty 함수 # 스택내 비어 있는 자리가 있는 확인
def isEmpty () :
    global SIZE, stack, Top
    if Top == -1 :
        return True # -1(인덱스 없다)
    else:
        return False
# 4. Top 함수 # 스택내 최상단 위치의 데이터 제거 함수
def pop() :
    global SIZE, stack, Top
    if isEmpty() : # 비어있으면 삭제 불가능
        return
    stack[Top] = None # 최상단 위치에 데이터를 제거
    Top -= 1 # 한칸 내리기
# 5. PEEK 함수 # 스택내 최상단 위치의 데이터 확인 함수
def peek() :
    global SIZE, stack, Top
    if isEmpty() :
    # 만약 비어있으면 확인 불가능
        return
    return stack[Top]

#####

# 스택 관련 함수들 활용
SIZE = int(input('stack size : ')) # 스택 사이즈를 입력받기
stack = [ None for _ in range(SIZE)] # SIZE 만큽 개수를 반복하여 리스트 선언
Top = -1

while True:
    print( stack ) # 확인용
    select = int(input('1, 삽입 2.삭제 3.확인 4,종료 :'))
    if select == 1:
        newData = input('save Data : ')
        push( newData) # 위에서 입력받은 자료를 push 함수에 대입
    if  select == 2 :
        pop()
    if select == 3 :
        data = peek()
        print( f'stack to data : {data}')
    if select == 4 :
        break

















