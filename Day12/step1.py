# [1] 파이썬 에서 스택 구조를 구현 하는 방법
    # (1) 스택구조에 저장할 자료들의 목록을 리스트로 구현
stack = [ None , None , None , None , None ]    # None 데이터 가 없다는 뜻
    # (2) 현재 가장 위에 있는 데이터의 위치 기억
top = -1    # -1 는 현재 스택구조의 데이터가 하나도 없다.

print( stack )

# [2] 데이터 push
top += 1                  # 위치 한칸 올리기
stack[ top ] = '커피'     # 커피 대입
print( stack )

top += 1                # 위치 한칸 올리기
stack[ top ] = '녹차'    # 녹차 대입
print( stack )

top += 1
stack[ top ] = '꿀물'
print( stack )

# [3] 데이터 pop
stack[top] = None       # 가장 위에 위치한 데이터를 None 변경
top -= 1                # 위치 한칸 내리기
print( stack )

stack[top] = None       # 가장 위에 위치한 데이터를 None 변경
top -= 1                # 위치 한칸 내리기
print( stack )

stack[top] = None       # 가장 위에 위치한 데이터를 None 변경
top -= 1                # 위치 한칸 내리기
print( stack )
