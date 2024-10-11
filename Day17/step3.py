# [3] 파이썬을 이용한 큐 규조 구현 예제

# 1. 큐 를 규 현하기 위한 리스트 선언
queue = [None, None, None, None]
# 2. 데이터들의 위치를 저장할 변수 선언
front = -1 # 나가는 인덱스의 위치 기억 변수 선언
rear = -1 # 들어오는 인덱스의 위치 기억 변수 선언
# 3. 임의 데이터를 삽입
rear += 1
queue[ rear ] = '유재석'
print(queue)
rear += 1
queue[ rear ] = '강호동'
print(queue)
rear += 1
queue[ rear ] = '서장훈'
print(queue)
# 4. 임의 데이터를 삭제
front += 1
queue[front] = None
print(queue)
front += 1
queue[front] = None
print(queue)
front += 1
queue[front] = None
print(queue)
front += 1
queue[front] = None
print(queue)
