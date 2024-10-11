# [4] 파이썬을 이용한 큐 구조 구현 활용
'''
    큐 구조 기능 구현
    1. isFull() : 큐가 다 찾는지 확인 함수
    2. isEmpty() : 큐가 다 비어 있는지 확인 함수
    3. peek() : 가장 앞에 위치에 데이터 확인 함수
    4. enQueue : 큐에 데이터를 삽입 함수
    5. deQueue : 큐에 데이터를 삭제 함수
'''


# 1. isEmpty() 함수 구현
def isEmpty() :
    global SIZE, queue, frontm, rear # 정역변수를 함수 안에 가져온다
    if front == rear : # 만약 위치가 같으면
        return True # 큐가 다 비어 있다는 뜻
    else :
        return False
# 2. deQueue() 함수 구현
def deQueue() :
    global SIZE, queue, frontm, rear
    if isEmpty() : # 만약에 비어있으면 삭제 불가능
        return # 함수 강제 종료
    # 데이터 삭제
    front += 1
    queue[front] = None

# 3. peek()
    global SIZE, queue, frontm, rear
    if isEmpty() : # 비어있으면
        return None
    return queue[front+1]

# 4. isFull() 함수
def isFull():
    global SIZE, queue, frontm, rear
    if rear != SIZE-1 : # 현재 rear 위치가 전채 크기와 같지 않으면
        return False # 빈칸이 존재 햇을때
    elif rear == SIZE -1 and front == -1 :
        return True # 빈칸이 존재하지 않을때
    else: # 그외 남아 있는 데이터들을 한칸씩 앞으로
        for i in range( front +1, SIZE) :
            queue[i-1] = queue [i]
            # 앞전 데이터가 위치했던곳에 새로운 데이터 대입
            queue[i] = None
        frontm -= 1
        rear -= 1
        return False
# 5. enQueue 함수
def enQueue(data):
    global SIZE, queue, frontm, rear
    if isFull() : # 다 차면
        return None
    rear += 1
    queue[rear] = data # rear 위치에 데이터 대입