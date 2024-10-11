# [1] 파이썬을 이용한 스택 구조 구현 예제

# 1. 파이썬의 리스트를 활용하여 None(자료가 없다) 5개를 가지는 리스트 변수 선언

stack = [ None, None, None, None, None] # 스택의 크기는 5

# 2. 스택 구조내 현제 가장 위에 있는 데이터 위치 기억하기 위한 변수 선언
top = -1    # 인덱스는 0부터 시작하므로 -1는 데이터 위치를 기억하고 있지 않다 # 초기화 값
print( stack ) # 스택 구조 확인 # [None, None, None, None, None]
# 3. 임의 데이터를 삽입하기 # 스택구조의 삽입 기능읜 push 기능 구현
top += 1        # 현재 top 위치를 한칸 올리기
stack[top] = '커피' # 현재 top 위치에 데이터 대입 # stack[top] = '커피'
print(stack)       # ['커피', None, None, None, None]

top += 1              # 현재 top 위치를 한칸 올리기
stack[top] = '녹차'     # 현재 top 위치에 데이터 대입 # stack[top] = 녹차'
print(stack)      # ['커피', '녹차', None, None, None]

top += 1              # 현재 top 위치를 한칸 올리기
stack[top] = '꿀물'     # 현재 top 위치에 데이터 대입 # stack[top] = '꿀물'
print(stack)      # ['커피', '녹차', '꿀물', None, None, None]

# 4. 최근에 저장된 데이터 삭제 # 스택구조의 삭제 기능인 pop 기능을 구현
stack[top] = None   # 현재 top 위치의 데이터를 None 변경 하기
top -= 1    # 한칸 내리기
print(stack) # ['커피', '녹차', None, None, None]

stack[top] = None
top -= 1
print(stack)      # ['커피', None, None, None, None]

stack[top] = None
top -= 1
print(stack)     # [None, None, None, None, None]

